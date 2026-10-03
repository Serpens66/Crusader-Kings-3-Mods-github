"""Offline behavior tests using disposable Git repositories, never CK3."""
import subprocess
import tempfile
import unittest
from pathlib import Path

import vanilla_history as history
from workspace_walk import workspace_files


class HistoryTests(unittest.TestCase):
    def setUp(self):
        test_root = history.DOC.parent / '.reference-cache/tests'
        test_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=test_root)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.origin = self.root / 'origin'
        self.origin.mkdir()
        history.git(self.origin, 'init')
        history.git(self.origin, 'config', 'user.name', 'Fixture')
        history.git(self.origin, 'config', 'user.email', 'fixture@example.invalid')
        self.game = self.origin / 'base/game'
        self.game.mkdir(parents=True)
        (self.game / 'changed.data').write_bytes(b'old\r\n')
        (self.game / 'deleted.data').write_bytes(b'deleted\r\n')
        (self.game / 'old name.data').write_bytes(b'rename content\r\n')
        self.old = self.commit('old', 'base/1.19.0.6')
        (self.game / 'changed.data').write_bytes(b'new\r\n')
        (self.game / 'deleted.data').unlink()
        (self.game / 'old name.data').rename(self.game / 'new name.data')
        (self.game / 'added.data').write_bytes(b'added\r\n')
        self.new = self.commit('new', 'base/1.20.0.3')
        self.repo = self.root / 'clone'
        cloned = subprocess.run(['git', '-c', 'core.autocrlf=false', 'clone', '--no-hardlinks',
                                 str(self.origin), str(self.repo)], capture_output=True)
        if cloned.returncode:
            raise ValueError(cloned.stderr.decode('utf-8', errors='replace'))
        self.lock = {'url': str(self.origin), 'versions': {
            '1.19.0.6': {'tag': 'base/1.19.0.6', 'commit': self.old},
            '1.20.0.3': {'tag': 'base/1.20.0.3', 'commit': self.new}}}

    def commit(self, message, tag):
        history.git(self.origin, 'add', '--all')
        history.git(self.origin, 'commit', '-m', message)
        history.git(self.origin, 'tag', tag)
        return history.git(self.origin, 'rev-parse', 'HEAD').decode().strip()

    def test_changes_and_rename(self):
        rows = history.changes(self.repo, self.old, self.new)
        self.assertEqual({r['status'][0] for r in rows}, {'A', 'D', 'M', 'R'})
        rename = next(r for r in rows if r['status'].startswith('R'))
        self.assertEqual(rename['paths'], ['old name.data', 'new name.data'])
        self.assertEqual(len(history.changes(self.repo, self.old, self.new, ['changed.data'])), 1)

    def test_compare_bytes_format_content_and_missing(self):
        local = self.root / 'installation'; local.mkdir()
        (local / 'changed.data').write_bytes(b'\xef\xbb\xbfnew\n')
        (local / 'added.data').write_bytes(b'different')
        rows = history.compare(self.repo, self.new, local,
                               ['changed.data', 'added.data', 'new name.data', 'missing.data'])
        self.assertEqual([r['status'] for r in rows], ['bom_or_crlf_only', 'content_difference',
                                                     'missing_in_installation', 'missing_in_mirror'])
        self.assertEqual(history.classify(b'new\r\n', b'new\r\n'), 'identical')

    def test_pinned_tag_change_is_rejected(self):
        history.git(self.repo, 'tag', '-f', 'base/1.19.0.6', self.new)
        with self.assertRaisesRegex(ValueError, 'Pinned tag changed'):
            history.resolve(self.repo, '1.19.0.6', self.lock)

    def test_fetch_preserves_checkout_and_edits(self):
        history.checkout(self.repo, self.old)
        path = self.repo / 'base/game/changed.data'; path.write_bytes(b'user edit')
        unknown = self.repo / 'untracked.data'; unknown.write_bytes(b'keep')
        (self.game / 'added.data').write_bytes(b'next')
        self.commit('later', 'base/1.20.0.4')
        result = history.fetch(self.repo, self.lock)
        self.assertEqual(result['new_tags'], ['base/1.20.0.4'])
        self.assertEqual(result['checkout'], self.old)
        self.assertEqual(path.read_bytes(), b'user edit')
        self.assertEqual(unknown.read_bytes(), b'keep')
        with self.assertRaisesRegex(ValueError, 'Local changes'):
            history.checkout(self.repo, self.new)

    def test_unexpected_origin_rejected(self):
        bad = {**self.lock, 'url': 'https://example.invalid/unexpected.git'}
        with self.assertRaisesRegex(ValueError, 'Unexpected origin'):
            history.fetch(self.repo, bad)

    def test_remote_tag_rewrite_is_not_forced(self):
        history.git(self.origin, 'tag', '-f', 'base/1.19.0.6', self.new)
        with self.assertRaises(ValueError):
            history.fetch(self.repo, self.lock)
        self.assertEqual(history.resolve(self.repo, '1.19.0.6', self.lock), self.old)
        self.assertEqual(history.git(self.repo, 'rev-parse', 'HEAD').decode().strip(), self.new)

    def test_untracked_only_checkout_is_refused(self):
        (self.repo / 'untracked.data').write_bytes(b'keep')
        with self.assertRaisesRegex(ValueError, 'Local changes'):
            history.checkout(self.repo, self.old)

    def test_paths_and_workspace_pruning(self):
        for path in ['../outside', '/absolute', 'C:/outside', 'a\\b']:
            with self.assertRaises(ValueError):
                history.safe_path(path)
        workspace = self.root / 'workspace'; workspace.mkdir()
        (workspace / 'AGENTS.md').write_bytes(b'preserve')
        hidden = workspace / '.reference-cache/ck3-mod-base'; hidden.mkdir(parents=True)
        (hidden / 'source.data').write_bytes(b'exclude')
        self.assertEqual([p.name for p in workspace_files(workspace)], ['AGENTS.md'])


if __name__ == '__main__':
    unittest.main()

"""Isolated source fixtures; never edit the installation or real mod/baselines."""
import contextlib
import copy
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode = True
import check_mod_updates as checker

EVENT = 'religious_interaction.2002'
PATH = 'events/religious.txt'
OLD = b'namespace = religious_interaction\nreligious_interaction.2002 = { immediate = { add_piety = 50 } option = { name = OK } }\n'


class MemoryReference:
    def __init__(self, files):
        self.files = files

    def read(self, path):
        if path not in self.files:
            raise ValueError('Baseline blob unavailable')
        return self.files[path]


class SourceCases(unittest.TestCase):
    def setUp(self):
        fixture_root = checker.ROOT / '.reference-cache/tests/update-watch'
        fixture_root.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='case-', dir=fixture_root)
        self.root = Path(self.temp.name)
        assert self.root.resolve().is_relative_to(fixture_root.resolve())
        self.game = self.root / 'game'
        self.game.mkdir()
        self.put(PATH, OLD)
        self.reference = MemoryReference({PATH: OLD})
        self.watch = {'id': 'acceptance', 'feature': 'MC-N', 'surface': 'event_override', 'kind': 'object',
                      'native_path': PATH, 'symbol': EVENT, 'baseline_version': '1.20.0.3',
                      'source_sha256': checker.sha(OLD), 'object_token_sha256': checker.assignments(OLD)[1]['token_sha256'],
                      'local_definitions': ['Mod/events/accept.txt'], 'audit_scope': 'notification only'}

    def tearDown(self):
        self.temp.cleanup()

    def put(self, path, data):
        dest = self.game / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)

    def compare(self):
        return checker.compare_watch(self.watch, checker.InstalledSources(self.game), self.reference)

    def test_unchanged(self):
        self.assertEqual(self.compare()['status'], 'unchanged')

    def test_bom_crlf_only(self):
        self.put(PATH, b'\xef\xbb\xbf' + OLD.replace(b'\n', b'\r\n'))
        self.assertEqual(self.compare()['status'], 'format_only')

    def test_comment_and_spacing_only(self):
        self.put(PATH, OLD.replace(b'add_piety = 50', b'# comment\n add_piety   =  50'))
        row = self.compare()
        self.assertEqual(row['status'], 'format_only')
        self.assertIn('comment', row['diff'])

    def test_unrelated_change_in_same_file(self):
        self.put(PATH, OLD + b'religious_interaction.9999 = { immediate = { add_gold = 5 } }\n')
        row = self.compare()
        self.assertEqual(row['status'], 'file_changed_object_unchanged')
        self.assertNotIn('diff', row)

    def test_new_reward(self):
        self.put(PATH, OLD.replace(b'add_piety = 50', b'add_piety = 50 add_prestige = 100'))
        row = self.compare()
        self.assertEqual(row['status'], 'object_changed')
        self.assertIn('add_prestige', row['diff'])

    def test_changed_condition(self):
        self.put(PATH, OLD.replace(b'add_piety = 50', b'if = { limit = { is_ai = no } add_piety = 50 }'))
        self.assertEqual(self.compare()['status'], 'object_changed')

    def test_new_player_option(self):
        self.put(PATH, OLD.replace(b'option = { name = OK }', b'option = { name = OK } option = { name = REFUSE }'))
        self.assertEqual(self.compare()['status'], 'object_changed')

    def test_changed_helper_body(self):
        self.watch['surface'] = 'delegated_helper'
        self.put(PATH, OLD.replace(b'add_piety = 50', b'add_piety = 75'))
        self.assertEqual(self.compare()['status'], 'object_changed')

    def test_order_and_duplicate_keys_preserved(self):
        first = checker.assignments(b'helper = { add = 1 multiply = 2 add = 3 }')[0]
        other = checker.assignments(b'helper = { add = 1 add = 3 multiply = 2 }')[0]
        self.assertNotEqual(first['token_sha256'], other['token_sha256'])

    def test_missing_definition(self):
        self.put(PATH, b'namespace = religious_interaction\n')
        self.assertEqual(self.compare()['status'], 'missing_definition')

    def test_moved_definition(self):
        self.put(PATH, b'namespace = religious_interaction\n')
        self.put('events/new_file.txt', OLD)
        row = self.compare()
        self.assertEqual(row['status'], 'moved_definition')
        self.assertEqual(row['current_path'], 'events/new_file.txt')

    def test_duplicate_definition_not_silently_selected(self):
        self.put('events/conflict.txt', OLD)
        self.assertEqual(self.compare()['status'], 'ambiguous_definition')

    def test_unbalanced_candidate_fails_closed(self):
        self.put(PATH, OLD[:-3])
        with self.assertRaisesRegex(ValueError, 'Unreadable'):
            self.compare()

    def test_non_utf8_fails_closed(self):
        self.put(PATH, OLD + b'\xff')
        with self.assertRaises(ValueError):
            self.compare()

    def test_missing_reference_not_unchanged(self):
        self.reference = MemoryReference({})
        with self.assertRaisesRegex(ValueError, 'unavailable'):
            self.compare()

    def test_bad_baseline_hash(self):
        self.watch['source_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'checksum'):
            self.compare()

    def test_unknown_watch_kind_not_silently_accepted(self):
        self.watch['kind'] = 'typo'
        with self.assertRaisesRegex(ValueError, 'Unknown watch kind'):
            self.compare()

    def test_scalar_script_value(self):
        old = b'minor_piety_gain = minor_piety_value\n'
        self.put(PATH, old)
        self.reference = MemoryReference({PATH: old})
        self.watch.update(symbol='minor_piety_gain', source_sha256=checker.sha(old), object_token_sha256=checker.assignments(old)[0]['token_sha256'])
        self.assertEqual(self.compare()['status'], 'unchanged')
        self.put(PATH, old.replace(b'minor_piety_value', b'medium_piety_value'))
        self.assertEqual(self.compare()['status'], 'object_changed')

    def test_native_event_local_declarations(self):
        rows = checker.assignments(b'scripted_effect local_helper = { add_gold = 1 }\nscripted_trigger local_guard = { is_ai = yes }\n' + OLD)
        self.assertEqual([r['symbol'] for r in rows], ['local_helper', 'local_guard', 'namespace', EVENT])
        self.assertEqual(rows[0]['tokens'][0], 'scripted_effect')

    def test_changed_caller_scope_and_added_block_form(self):
        caller_path = 'common/character_interactions/conversion.txt'
        old = b'convert = { on_accept = { scope:puppet_or_actor = { trigger_event = religious_interaction.2002 } } }\n'
        self.put(caller_path, old)
        self.reference.files[caller_path] = old
        self.watch.update(kind='callers', events=[EVENT], baseline_callers=checker.callers(checker.InstalledSources(self.game), [EVENT]))
        self.assertEqual(self.compare()['status'], 'unchanged')
        self.put(caller_path, old.replace(b'scope:puppet_or_actor', b'scope:actor'))
        changed = self.compare()
        self.assertEqual(changed['status'], 'callers_changed')
        self.assertIn('scope:actor', changed['owner_diffs'][0])
        self.put('events/new_caller.txt', b'new.1 = { immediate = { trigger_event = { id = religious_interaction.2002 days = 1 } } }\n')
        changed = self.compare()
        self.assertEqual(len(changed['current_callers']), 2)
        self.assertEqual(len(changed['owner_diffs']), 2)

    def test_missing_caller(self):
        self.test_changed_caller_scope_and_added_block_form()
        self.put('common/character_interactions/conversion.txt', b'convert = { on_accept = {} }')
        row = self.compare()
        self.assertEqual(row['status'], 'callers_changed')
        self.assertTrue(row['owner_diffs'])

    def test_file_format_and_reference_changes(self):
        self.watch['kind'] = 'file'
        self.put(PATH, b'# comment\n' + OLD)
        self.assertEqual(self.compare()['status'], 'format_only')
        self.watch['kind'] = 'text'
        self.assertEqual(self.compare()['status'], 'reference_changed')

    def test_asset_header_and_byte_hash(self):
        self.watch.update(kind='asset', baseline_header=checker.asset_header(OLD))
        self.assertEqual(self.compare()['status'], 'unchanged')
        self.put(PATH, b'changed binary')
        row = self.compare()
        self.assertEqual(row['status'], 'asset_changed')
        self.assertIn('sha256', row['diff'])

    def test_unsafe_relative_paths(self):
        for value in ['../outside', 'C:/outside', '/outside', 'folder\\file']:
            with self.assertRaises(ValueError):
                checker.safe_relative(value)


class CommandCases(unittest.TestCase):
    put = SourceCases.put
    tearDown = SourceCases.tearDown

    def setUp(self):
        SourceCases.setUp(self)
        (self.root / 'launcher').mkdir()
        (self.root / 'launcher/launcher-settings.json').write_text(json.dumps({'rawVersion': '1.20.0.3'}), encoding='utf-8')
        self.manifest = {'schema_version': 1, 'date': '2026-10-03', 'baseline_version': '1.20.0.3',
                         'comparison_reference': {'repository': 'reference', 'commit': '0' * 40},
                         'engine_reference': {'version': '1.20.0.3', 'files': {}},
                         'mods': {'Test Mod': {'sheet': 'test.md', 'coverage': 'fixture', 'open_gates': ['runtime'], 'local_sources': {}, 'watches': [self.watch]}}}

    def test_check_collects_failure_without_aborting_other_watches(self):
        self.manifest['mods']['Test Mod']['watches'].append(dict(self.watch, id='missing', native_path='missing.txt'))
        with patch.object(checker, 'GitReference', return_value=self.reference):
            result = checker.check(self.manifest, ['Test Mod'], self.game, self.root)
        self.assertEqual(result['mods']['Test Mod']['counts'], {'unchanged': 1, 'comparison_incomplete': 1})

    def test_new_version_reports_stale_exports_instead_of_aborting(self):
        (self.root / 'launcher/launcher-settings.json').write_text(json.dumps({'rawVersion': '1.21.0.1'}), encoding='utf-8')
        with patch.object(checker, 'GitReference', return_value=self.reference):
            result = checker.check(self.manifest, ['Test Mod'], self.game, self.root)
        self.assertTrue(result['version_changed'])
        self.assertEqual(result['engine_reference']['status'], 'stale_for_installed_version')
        self.assertEqual(result['mods']['Test Mod']['counts'], {'unchanged': 1})

    def test_unknown_and_excluded_mod_rejected(self):
        for name in ['Typo', 'Knight Manager', 'test']:
            with self.assertRaisesRegex(ValueError, 'Unknown or excluded'):
                checker.check(self.manifest, [name], self.game, self.root)

    def test_baseline_manifest_not_mutated_and_no_files_written(self):
        before_manifest = copy.deepcopy(self.manifest)
        before_files = {p.relative_to(self.root).as_posix(): checker.sha(p.read_bytes()) for p in self.root.rglob('*') if p.is_file()}
        with patch.object(checker, 'GitReference', return_value=self.reference):
            checker.check(self.manifest, ['Test Mod'], self.game, self.root)
        after_files = {p.relative_to(self.root).as_posix(): checker.sha(p.read_bytes()) for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before_manifest, self.manifest)
        self.assertEqual(before_files, after_files)

    def test_pinned_git_blob_ignores_dirty_checkout(self):
        repo = self.root / 'reference'
        repo.mkdir()
        def git(*args):
            return subprocess.run(['git', '-c', 'core.hooksPath=NUL', '-c', 'core.autocrlf=false', '-C', str(repo), *args], check=True, capture_output=True).stdout
        git('init', '-q')
        path = repo / ('base/game/' + PATH)
        path.parent.mkdir(parents=True)
        path.write_bytes(OLD)
        git('add', '.')
        git('-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '-qm', 'fixture')
        commit = git('rev-parse', 'HEAD').decode().strip()
        path.write_bytes(b'dirty checkout')
        reference = checker.GitReference(self.root, {'repository': 'reference', 'commit': commit})
        before = git('status', '--porcelain')
        self.assertEqual(reference.read(PATH), OLD)
        self.assertEqual(git('status', '--porcelain'), before)
        self.assertEqual(path.read_bytes(), b'dirty checkout')

    def invoke(self):
        path = self.root / 'manifest.json'
        path.write_text(json.dumps(self.manifest), encoding='utf-8')
        before = {p.relative_to(self.root).as_posix(): checker.sha(p.read_bytes()) for p in self.root.rglob('*') if p.is_file()}
        stdout = io.StringIO()
        with patch.object(checker, 'GitReference', return_value=self.reference), contextlib.redirect_stdout(stdout):
            status = checker.main(['--mod', 'Test Mod', '--game', str(self.game), '--manifest', str(path), '--json'])
        after = {p.relative_to(self.root).as_posix(): checker.sha(p.read_bytes()) for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)
        return status, json.loads(stdout.getvalue())

    def test_cli_json_selection_and_exit_zero_without_writes(self):
        status, data = self.invoke()
        self.assertEqual(status, 0)
        self.assertEqual(list(data['mods']), ['Test Mod'])

    def test_cli_changed_source_exit_one(self):
        self.put(PATH, OLD.replace(b'add_piety = 50', b'add_piety = 75'))
        status, data = self.invoke()
        self.assertEqual(status, 1)
        self.assertEqual(data['mods']['Test Mod']['counts'], {'object_changed': 1})

    def test_cli_missing_reference_exit_two(self):
        self.reference = MemoryReference({})
        status, data = self.invoke()
        self.assertEqual(status, 2)
        self.assertEqual(data['mods']['Test Mod']['counts'], {'comparison_incomplete': 1})

    def test_cli_file_context_review_is_not_event_change(self):
        self.put(PATH, OLD + b'religious_interaction.9999 = {}\n')
        status, data = self.invoke()
        self.assertEqual(status, 1)
        self.assertFalse(data['mods']['Test Mod']['source_review_required'])
        self.assertTrue(data['mods']['Test Mod']['file_context_review_required'])
        self.assertEqual(data['mods']['Test Mod']['counts'], {'file_changed_object_unchanged': 1})


if __name__ == '__main__':
    unittest.main()

"""Read pinned Vanilla history; fetch is explicit and never changes the checkout.

Only Git and the Python standard library are required. No upstream scripts run.
"""
import argparse
import collections
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

DOC = Path(__file__).resolve().parents[1]
DEFAULT_REPO = DOC.parent / '.reference-cache/ck3-mod-base'
LOCK = DOC / 'reference/vanilla-history-lock.json'
URL = 'https://github.com/jesec/ck3-mod-base.git'
DEFAULT_GAME = Path(r'E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\game')


def git(repo, *args, input=None):
    result = subprocess.run(['git', '-c', 'core.hooksPath=NUL', '-c', 'core.autocrlf=false',
                             '-C', str(repo), *args], input=input, capture_output=True)
    if result.returncode:
        raise ValueError(result.stderr.decode('utf-8', errors='replace').strip())
    return result.stdout


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((json.dumps(data, ensure_ascii=False, indent=2) + '\n').replace('\n', '\r\n').encode('utf-8'))


def load_lock():
    return json.loads(LOCK.read_text(encoding='utf-8'))


def resolve(repo, version, lock):
    if version in lock['versions']:
        item = lock['versions'][version]
        actual = git(repo, 'rev-parse', '--verify', 'refs/tags/' + item['tag'] + '^{commit}').decode().strip()
        if actual != item['commit']:
            raise ValueError('Pinned tag changed: ' + item['tag'])
        return actual
    # Explicit additional versions are tag names, never arbitrary revision expressions.
    if not re.fullmatch(r'\d+\.\d+(?:\.\d+){0,2}', version):
        raise ValueError('Version must be a numeric base tag, such as 1.20.0.3')
    return git(repo, 'rev-parse', '--verify', 'refs/tags/base/' + version + '^{commit}').decode().strip()


def safe_path(value):
    p = PurePosixPath(value)
    if not value or value.startswith('/') or '\\' in value or ':' in value or '..' in p.parts:
        raise ValueError('Use a game-relative path without .., backslashes or drive letters')
    return p.as_posix()


def tree(repo, commit):
    result = {}
    for entry in git(repo, 'ls-tree', '-r', '-z', commit, '--', 'base/game').split(b'\0'):
        if not entry:
            continue
        header, path = entry.split(b'\t', 1)
        mode, kind, oid = header.decode().split()
        if kind == 'blob':
            result[path.decode('utf-8').removeprefix('base/game/')] = {'blob': oid, 'mode': mode}
    return result


def blobs(repo, ids):
    ids = list(dict.fromkeys(ids))
    if not ids:
        return {}
    raw = git(repo, 'cat-file', '--batch', input=('\n'.join(ids) + '\n').encode())
    result, cursor = {}, 0
    for oid in ids:
        end = raw.index(b'\n', cursor)
        header = raw[cursor:end].decode().split()
        if len(header) != 3 or header[1] != 'blob':
            raise ValueError('Missing/non-blob object: ' + oid)
        size = int(header[2])
        result[oid] = raw[end + 1:end + 1 + size]
        cursor = end + 1 + size + 1
    return result


def changes(repo, old, new, paths=()):
    args = ['diff', '--no-ext-diff', '--no-textconv', '--name-status', '-z', '-M50%', old, new, '--']
    args += [':(literal)base/game/' + safe_path(p) for p in paths] if paths else ['base/game']
    fields = git(repo, *args).split(b'\0')
    result, i = [], 0
    while i < len(fields) and fields[i]:
        status = fields[i].decode(); i += 1
        count = 2 if status.startswith(('R', 'C')) else 1
        names = [x.decode('utf-8').removeprefix('base/game/') for x in fields[i:i + count]]
        result.append({'status': status, 'paths': names})
        i += count
    return result


def classify(remote, local):
    if remote == local:
        return 'identical'
    def format_only(raw):
        return raw.removeprefix(b'\xef\xbb\xbf').replace(b'\r\n', b'\n')
    return 'bom_or_crlf_only' if format_only(remote) == format_only(local) else 'content_difference'


def compare(repo, commit, game, paths):
    entries = tree(repo, commit)
    payload = blobs(repo, [entries[p]['blob'] for p in paths if p in entries])
    result = []
    for path in paths:
        path = safe_path(path)
        row = {'path': path}
        local = game / path
        if path not in entries:
            row['status'] = 'missing_in_mirror'
        elif not local.is_file():
            row['status'] = 'missing_in_installation'
        else:
            upstream, installed = payload[entries[path]['blob']], local.read_bytes()
            row.update(status=classify(upstream, installed), mirror_sha256=sha(upstream),
                       installed_sha256=sha(installed), mirror_blob=entries[path]['blob'])
        result.append(row)
    return result


def tags(repo):
    return git(repo, 'for-each-ref', '--format=%(refname:short)', 'refs/tags/base/').decode().splitlines()


def fetch(repo, lock):
    origin = git(repo, 'remote', 'get-url', 'origin').decode().strip()
    if origin != lock['url']:
        raise ValueError('Unexpected origin; refusing fetch: ' + origin)
    for version in lock['versions']:
        resolve(repo, version, lock)
    head = git(repo, 'rev-parse', 'HEAD')
    before = set(tags(repo))
    # No force, prune, pull or checkout: local edits and historical tags are retained.
    git(repo, 'fetch', '--no-recurse-submodules', '--tags', 'origin')
    for version in lock['versions']:
        resolve(repo, version, lock)
    if git(repo, 'rev-parse', 'HEAD') != head:
        raise ValueError('Unexpected checkout change')
    return {'new_tags': sorted(set(tags(repo)) - before), 'checkout': head.decode().strip(),
            'working_tree_preserved': True}


def checkout(repo, commit):
    if git(repo, 'status', '--porcelain', '--untracked-files=all').strip():
        raise ValueError('Local changes present; refusing checkout')
    git(repo, 'checkout', '--detach', commit)


def report(repo, lock, game, destination):
    old = resolve(repo, '1.19.0.6', lock); new = resolve(repo, '1.20.0.3', lock)
    evidence = DOC / 'update-readiness/evidence/mass-conversion-audit-20261003.json'
    seed = json.loads(evidence.read_text(encoding='utf-8'))
    paths = sorted(seed['native_sources'])
    trees = {old: tree(repo, old), new: tree(repo, new)}
    bodies = blobs(repo, [entries[p]['blob'] for entries in trees.values() for p in paths if p in entries])
    focused = []
    for path in paths:
        row = {'path': path}
        for name, commit in [('old', old), ('new', new)]:
            entry = trees[commit].get(path)
            row[name] = None if entry is None else {**entry, 'sha256': sha(bodies[entry['blob']])}
        row['changed'] = row['old'] != row['new']
        focused.append(row)
    # Object boundaries are lexical evidence, not a resolved runtime call graph.
    from collect_mass_conversion_audit import objects
    names = {'ask_for_conversion_courtier_interaction', 'demand_conversion_interaction',
             'demand_conversion_vassal_ruler_interaction', 'valid_demand_conversion_conditions_trigger',
             'demand_conversion_interaction_effect', 'demand_conversion_influence_cost_value',
             'religion_demand_conversion_default_modifier'}
    selected_paths = {'common/character_interactions/00_religious_interactions.txt',
                      'common/scripted_triggers/00_religious_triggers.txt',
                      'common/scripted_effects/00_religious_interaction_effects.txt',
                      'common/script_values/02_religion_values.txt',
                      'common/script_values/pam_values.txt',
                      'common/scripted_modifiers/00_religion_scripted_modifiers.txt'}
    spans = {}
    for name, commit in [('old', old), ('new', new)]:
        for path in sorted(selected_paths):
            entry = trees[commit].get(path)
            if entry is None:
                continue
            for symbol, first, last, block in objects(bodies[entry['blob']].decode('utf-8-sig')):
                if symbol in names:
                    spans.setdefault(symbol, {})[name] = {'path': path, 'first_line': first,
                        'last_line': last, 'block_text_sha256': sha(block.encode('utf-8'))}
    snapshots = {}
    for version, commit in [('1.19.0.6', old), ('1.20.0.3', new)]:
        raw = git(repo, 'show', commit + ':base/.ck3-version.json')
        snapshots[version] = {'commit': commit, 'game_tree': git(repo, 'rev-parse', commit + ':base/game').decode().strip(),
                              'metadata_sha256': sha(raw), 'metadata': json.loads(raw),
                              'file_count': len(trees[commit])}
    all_changes = changes(repo, old, new)
    local = compare(repo, new, game, paths)
    data = {'generated_utc': datetime.now(timezone.utc).isoformat(), 'source_url': lock['url'],
            'snapshots': snapshots, 'rename_detection': 'Git -M50%; heuristic, not semantic identity',
            'global_counts': dict(collections.Counter(r['status'][0] for r in all_changes)),
            'global_changes': all_changes, 'feature_seed': str(evidence.relative_to(DOC)),
            'feature_seed_sha256': sha(evidence.read_bytes()), 'feature_paths': focused,
            'selected_object_spans': spans,
            'installation_root': str(game), 'installation_comparison': local,
            'installation_counts': dict(collections.Counter(r['status'] for r in local)),
            'limit': 'Historical mirror diff and scoped byte verification; not a complete feature audit or runtime test.'}
    write_json(destination, data)
    return {'report': str(destination), 'global_counts': data['global_counts'],
            'feature_paths': len(paths), 'feature_changed': sum(r['changed'] for r in focused),
            'installation_counts': data['installation_counts']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=DEFAULT_REPO)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('fetch'); sub.add_parser('versions')
    change = sub.add_parser('checkout'); change.add_argument('--version', required=True)
    show = sub.add_parser('show'); show.add_argument('--version', required=True); show.add_argument('--path', required=True)
    diff = sub.add_parser('diff'); diff.add_argument('--from', dest='old', default='1.19.0.6')
    diff.add_argument('--to', dest='new', default='1.20.0.3'); diff.add_argument('--path', action='append', default=[])
    diff.add_argument('--patch', action='store_true', help='Print original unified diff; no tracked archive')
    local = sub.add_parser('compare-local'); local.add_argument('--version', default='1.20.0.3')
    local.add_argument('--game', type=Path, default=DEFAULT_GAME); local.add_argument('--path', action='append', required=True)
    audit = sub.add_parser('report'); audit.add_argument('--game', type=Path, default=DEFAULT_GAME)
    audit.add_argument('--output', type=Path, help='new evidence file inside Documentation; existing files are never replaced')
    args = parser.parse_args(); repo = args.repo.resolve(); lock = load_lock()
    if not (repo / '.git').is_dir():
        parser.error('Expected a full working clone: ' + str(repo))
    try:
        if args.command == 'fetch':
            result = fetch(repo, lock)
        elif args.command == 'versions':
            for version in lock['versions']:
                resolve(repo, version, lock)
            result = {'tags': tags(repo), 'pinned': lock['versions'],
                      'checkout': git(repo, 'rev-parse', 'HEAD').decode().strip(),
                      'shallow': git(repo, 'rev-parse', '--is-shallow-repository').decode().strip()}
        elif args.command == 'checkout':
            commit = resolve(repo, args.version, lock); checkout(repo, commit)
            result = {'checkout': commit}
        elif args.command == 'show':
            import sys
            commit = resolve(repo, args.version, lock)
            sys.stdout.buffer.write(git(repo, 'show', commit + ':base/game/' + safe_path(args.path)))
            return
        elif args.command == 'diff':
            old = resolve(repo, args.old, lock); new = resolve(repo, args.new, lock)
            if args.patch:
                import sys
                paths = [':(literal)base/game/' + safe_path(p) for p in args.path] if args.path else ['base/game']
                sys.stdout.buffer.write(git(repo, 'diff', '--no-ext-diff', '--no-textconv', '-M50%', old, new, '--', *paths))
                return
            result = {'from': old, 'to': new, 'changes': changes(repo, old, new, args.path)}
        elif args.command == 'compare-local':
            result = compare(repo, resolve(repo, args.version, lock), args.game, [safe_path(p) for p in args.path])
        else:
            if args.output is None:
                stamp = datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S-%f')
                args.output = DOC / ('research/vanilla-history-' + stamp + '.json')
            if not args.output.resolve().is_relative_to(DOC.resolve()):
                raise ValueError('Tracked evidence output must stay inside Documentation')
            if args.output.exists():
                raise ValueError('Report already exists; choose a new --output to retain historical evidence')
            result = report(repo, lock, args.game, args.output)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError) as error:
        parser.error(str(error))


if __name__ == '__main__':
    main()

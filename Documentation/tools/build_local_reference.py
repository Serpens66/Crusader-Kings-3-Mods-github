"""Read CK3 and workspace sources; write reference indexes only inside Documentation.

This lexical inventory is not a Jomini parser or a runtime validator.
Python standard library only. Run with --game PATH [--workspace PATH].
"""
import argparse
import bisect
import collections
import hashlib
import json
import re
from pathlib import Path
from workspace_walk import workspace_files

OUT = Path(__file__).resolve().parents[1]
TEXT_EXT = {'.txt', '.info', '.gui', '.yml', '.mod', '.asset'}
TOKEN = re.compile(r'"(?:\\.|[^"\\])*"|#[^\n]*|[{}]|[^\s{}=<>!#"]+|[=<>!]+')

def write(relative, text):
    target = OUT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text.replace('\r\n', '\n').replace('\n', '\r\n').encode('utf-8'))

def definitions(text):
    """Locate depth-zero assignments, preserving repeated keys and start lines."""
    matches = [m for m in TOKEN.finditer(text) if not m.group().startswith('#')]
    depth = 0
    newline_positions = [m.start() for m in re.finditer('\n', text)]
    result = []
    for i, m in enumerate(matches):
        token = m.group()
        if depth == 0 and i + 2 < len(matches) and matches[i+1].group() == '=':
            if token not in {'=', '{', '}'}:
                result.append({'key': token, 'line': bisect.bisect_left(newline_positions, m.start()) + 1})
        if token == '{':
            depth += 1
        elif token == '}':
            depth -= 1
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--game', required=True, type=Path)
    parser.add_argument('--workspace', type=Path, default=OUT.parent)
    args = parser.parse_args()
    game, workspace = args.game.resolve(), args.workspace.resolve()
    if game == OUT or OUT in game.parents:
        raise SystemExit('Game input must not be Documentation.')
    native, mods, infos, errors = [], [], [], []
    for root, dest in [(game, native), (workspace, mods)]:
        for p in sorted(workspace_files(root) if root == workspace else root.rglob('*')):
            if not p.is_file() or p.suffix.lower() not in TEXT_EXT:
                continue
            if root == workspace and (OUT in p.parents or any(part.startswith('.') for part in p.relative_to(root).parts)):
                continue
            raw = p.read_bytes()
            try:
                text = raw.decode('utf-8-sig')
            except UnicodeDecodeError:
                errors.append({'path': str(p), 'error': 'not strict UTF-8; indexed with replacement characters'})
                text = raw.decode('utf-8-sig', errors='replace')
            rel = p.relative_to(root).as_posix()
            row = {'path': rel, 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw),
                   'bom': raw.startswith(b'\xef\xbb\xbf'), 'lines': len(text.splitlines()),
                   'definitions': definitions(text) if p.suffix != '.yml' else []}
            dest.append(row)
            if root == game and p.suffix == '.info':
                infos.append({'path': rel, 'lines': row['lines'], 'sha256': row['sha256']})
    version_file = game.parent / 'launcher' / 'launcher-settings.json'
    version = json.loads(version_file.read_text(encoding='utf-8-sig')).get('version') if version_file.exists() else 'unavailable'
    payload = {'date': '2026-10-03', 'game_root': str(game), 'workspace_root': str(workspace),
               'installed_launcher_version': version, 'native': native, 'mods': mods, 'decode_warnings': errors}
    write('reference/local-index.json', json.dumps(payload, ensure_ascii=False, separators=(',', ':')) + '\n')
    lines = ['# Local developer-documentation index', '', f'Installed launcher version: **{version}**. Inventory date: 2026-10-03.', '',
             'Paths below are relative to the game root recorded in [local-index.json](local-index.json).', '',
             'These are developer-authored `.info` references. Their existence does not establish completeness.', '',
             '| Developer reference | Lines |', '|---|---:|']
    lines += [f"| `{r['path']}` | {r['lines']} |" for r in infos]
    write('reference/native-info-index.md', '\n'.join(lines)+'\n')
    by_native = collections.defaultdict(list)
    for r in native:
        for d in r['definitions']:
            by_native[d['key']].append((r['path'], d['line']))
    mod_dirs = sorted(p for p in workspace.iterdir() if p.is_dir() and not p.name.startswith('.') and p != OUT)
    inv = ['# Workspace mod inventory', '', 'Inventory includes variants and the `test` folder; names and descriptors do not prove runtime compatibility.', '',
           'Native path collisions are definite whole-file overlap candidates; matching depth-zero keys are lexical object-overlap candidates.',
           'Object merge rules must be checked for the relevant loader. A collision is not automatically a defect.', '',
           'See [case studies](../workspace/case-studies.md) for interpretation and [local-index.json](local-index.json) for hashes.', '']
    for folder in mod_dirs:
        records = [r for r in mods if r['path'].startswith(folder.name+'/')]
        descriptor = folder/'descriptor.mod'
        inv += [f'## {folder.name}', '', f'Text/reference files indexed: {len(records)}. External descriptor: `{folder.name}.mod` ({"present" if (workspace/(folder.name+".mod")).exists() else "absent"}).', '']
        if descriptor.exists():
            desc = descriptor.read_text(encoding='utf-8-sig')
            fields = re.findall(r'(?m)^\s*(name|version|supported_version|dependencies|replace_path|remote_file_id|path)\s*=\s*(.*)$', desc)
            inv += [f'- `{k} = {v.strip()}`' for k,v in fields] + ['']
        assets = sorted(p for p in folder.rglob('*') if p.is_file() and p.suffix.lower() not in TEXT_EXT)
        inv += [f'Other files: {len(assets)}. Extensions: ' + ', '.join(f'`{k}`: {v}' for k,v in sorted(collections.Counter(p.suffix.lower() for p in assets).items())), '']
        collisions = [p.relative_to(folder).as_posix() for p in assets if (game / p.relative_to(folder)).is_file()]
        if collisions:
            inv += ['Asset same-path overlaps: ' + ', '.join('`'+p+'`' for p in collisions), '']
        inv += ['| File | Native same path | Matching native top-level keys |', '|---|---|---|']
        native_paths = {r['path'] for r in native}
        for r in records:
            relative = r['path'][len(folder.name)+1:]
            overlap = sorted({d['key'] for d in r['definitions'] if d['key'] in by_native and d['key'] not in {'namespace','version','name','tags','supported_version','path','remote_file_id','window','types','posteffect_values','posteffect_volumes','posteffect_volume'}})
            inv.append(f'| `{relative}` | {"yes" if relative in native_paths else "no"} | '+', '.join('`'+k+'`' for k in overlap)+' |')
    write('reference/workspace-inventory.md', '\n'.join(inv)+'\n')
    # Engine-looking tokens are observations, not an invented callable API.
    symbol_rows = collections.defaultdict(list)
    for r in native:
        if not r['path'].startswith(('common/', 'events/', 'history/', 'gui/')) or not r['path'].endswith(('.txt','.gui')):
            continue
        p = game / r['path']
        text = p.read_text(encoding='utf-8-sig', errors='replace')
        for n, line in enumerate(text.splitlines(), 1):
            stripped = re.sub(r'"(?:\\.|[^"\\])*"', '""', line).split('#',1)[0]
            for m in re.finditer(r'(?<![\w.:])([A-Za-z_][\w.:]*)\s*(?:=|>=|<=|>|<|!=)', stripped):
                key = m.group(1)
                if ':' in key or '.' in key or key == 'namespace':
                    continue
                if len(symbol_rows[key]) < 4:
                    symbol_rows[key].append({'path':r['path'], 'line':n})
    write('reference/observed-symbols.json', json.dumps(dict(sorted(symbol_rows.items())), ensure_ascii=False, separators=(',', ':'))+'\n')
    print(json.dumps({'version':version, 'native_text_files':len(native), 'mod_text_files':len(mods),
                      'info_files':len(infos), 'observed_symbols':len(symbol_rows), 'decode_warnings':len(errors)}, indent=2))

if __name__ == '__main__':
    main()

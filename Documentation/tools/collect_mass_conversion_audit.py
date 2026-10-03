"""Collect/check supplemental conversion evidence; never write mod/game files.

Object edges are lexical discovery, not resolved engine contracts. Historical
indexes/baselines are inputs only; this collector writes its own dated evidence.
"""
import argparse
import collections
import hashlib
import json
import re
from pathlib import Path
from workspace_walk import workspace_files

from build_local_reference import OUT, TOKEN, write

DEST = 'update-readiness/evidence/mass-conversion-audit-20261003.json'
SEEDS = {
    'ask_for_conversion_courtier_interaction', 'demand_conversion_interaction',
    'demand_conversion_vassal_ruler_interaction', 'study_faith',
    'study_faith_success', 'study_faith_failure',
    'puppet_action_demand_conversion', 'puppet_action_demand_conversion_vassal_ruler',
}
AREAS = ('common/character_interactions/', 'common/scripted_effects/',
         'common/scripted_triggers/', 'common/script_values/',
         'common/scripted_modifiers/', 'common/scripted_lists/',
         'common/on_action/', 'common/schemes/', 'common/puppets/', 'events/')
EXTRA = [
    'common/character_interactions/_character_interactions.info',
    'common/decisions/_decisions.info', 'common/puppets/actions/_puppet_actions.info',
    'gui/decision_view_widgets/decision_view_widget_decision_option_list_controller.gui',
]


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def objects(text):
    tokens = [m for m in TOKEN.finditer(text) if not m.group().startswith('#')]
    depth = 0
    found = []
    for i, tok in enumerate(tokens):
        if depth == 0 and i + 2 < len(tokens) and tokens[i+1].group() == '=' and tokens[i+2].group() == '{':
            end_depth = 0
            for end in tokens[i+2:]:
                if end.group() == '{':
                    end_depth += 1
                elif end.group() == '}':
                    end_depth -= 1
                    if end_depth == 0:
                        start_line = text.count('\n', 0, tok.start()) + 1
                        end_line = text.count('\n', 0, end.end()) + 1
                        found.append((tok.group(), start_line, end_line, text[tok.start():end.end()]))
                        break
        if tok.group() == '{':
            depth += 1
        elif tok.group() == '}':
            depth -= 1
    return found


def preservation(workspace):
    result = {}
    for path in workspace_files(workspace):
        rel = path.relative_to(workspace)
        if rel.parts[0] == 'Documentation' or any(part.startswith('.') for part in rel.parts[:-1]):
            continue
        if path.is_file():
            result[rel.as_posix()] = sha(path.read_bytes())
    return result


def collect():
    index = json.loads((OUT/'reference/local-index.json').read_text(encoding='utf-8'))
    game, workspace = Path(index['game_root']), OUT.parent
    before = preservation(workspace)
    version_path = game.parent/'launcher/launcher-settings.json'
    version = json.loads(version_path.read_text(encoding='utf-8-sig'))['version']
    if version != '1.20.0.3 (Crozier)':
        raise SystemExit('Different installation: re-audit before collecting this supplement.')
    by_name = collections.defaultdict(list)
    sources, content, blocks = {}, {}, {}
    old = {r['path']:r['sha256'] for r in index['native']}

    def source(rel):
        if rel not in content:
            raw = (game/rel).read_bytes()
            content[rel] = raw.decode('utf-8-sig')
            sources[rel] = {'sha256':sha(raw), 'lines':len(content[rel].splitlines()),
                            'historical_index_hash_match':old.get(rel) == sha(raw)}
        return content[rel]

    # The existing index narrows discovery. Every visited source is read anew.
    for row in index['native']:
        if row['path'].startswith(AREAS) and row['path'].endswith('.txt'):
            for definition in row['definitions']:
                if definition['key'] != 'namespace':
                    by_name[definition['key']].append(row['path'])
    queue = collections.deque(sorted(SEEDS))
    visited, edges, processed_names = {}, [], set()
    while queue:
        name = queue.popleft()
        if name in processed_names:
            continue
        processed_names.add(name)
        for rel in sorted(set(by_name.get(name, []))):
            if rel not in blocks:
                blocks[rel] = objects(source(rel))
            for key, first, last, block in blocks[rel]:
                identity = f'{rel}:{first}:{key}'
                if key != name or identity in visited:
                    continue
                clean = '\n'.join(line.split('#', 1)[0] for line in block.splitlines())
                words = set(re.findall(r'[A-Za-z_][\w.]*', clean))
                callees = sorted(words & by_name.keys())
                params = sorted(set(re.findall(r'\$([A-Z][A-Z_0-9]*)\$', clean)))
                visited[identity] = {'symbol':key, 'path':rel, 'first_line':first,
                                     'last_line':last, 'parameters':params,
                                     'lexical_callees':callees}
                for callee in callees:
                    lines = [first+i for i, line in enumerate(block.splitlines())
                             if re.search(r'(?<![\w.])'+re.escape(callee)+r'(?![\w.])', line.split('#', 1)[0])]
                    edges.append({'caller':identity, 'callee':callee, 'lines':lines})
                    if callee != key:
                        queue.append(callee)
    for rel in EXTRA:
        source(rel)
    exports = {}
    raw_root = OUT/'update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs'
    for filename, ranges in {'effects.log.raw':[(2654,2667)],
                             'triggers.log.raw':[(5167,5179),(5190,5196)]}.items():
        raw = (raw_root/filename).read_bytes()
        lines = raw.decode('utf-8' if filename.startswith('triggers') else 'cp1252').splitlines()
        exports[filename] = {'path':(raw_root/filename).relative_to(OUT).as_posix(),
                             'sha256':sha(raw), 'spans':[{'first_line':a,'last_line':b,
                             'text':'\n'.join(lines[a-1:b])} for a,b in ranges]}
    mod_sources = {}
    for folder in ['Mass Demand Conversion', 'SerpInteractionsDecisions']:
        paths = list((workspace/folder).rglob('*'))
        for path in paths:
            if not path.is_file() or (folder != 'Mass Demand Conversion' and 'mass_convert' not in path.name and path.name != 'accept_conversion_notification.txt'):
                continue
            if path.suffix in {'.txt','.yml','.mod'}:
                raw = path.read_bytes()
                mod_sources[path.relative_to(workspace).as_posix()] = {
                    'sha256':sha(raw), 'bom':raw.startswith(b'\xef\xbb\xbf'),
                    'lines':len(raw.decode('utf-8-sig').splitlines())}
    after = preservation(workspace)
    if before != after:
        raise SystemExit('Workspace changed during collection; preserve and investigate.')
    payload = {'date':'2026-10-03','version':version,'game_root':str(game),
               'version_sha256':sha(version_path.read_bytes()),
               'audit_status':'partial feature source audit; engine context and runtime gates remain',
               'discovery_boundary':'Literal object references only; edges do not establish executed branches, parameter expansion, loader merge, engine initialization, or complete dynamic dependencies.',
               'seeds':sorted(SEEDS),'native_sources':sources,'objects':visited,
               'lexical_edges':edges,'export_declarations':exports,
               'mod_sources':mod_sources,'preserved_non_documentation_files':before}
    write(DEST, json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'sources':len(sources),'objects':len(visited),'edges':len(edges),
                      'preserved_files':len(before),'path':DEST}, indent=2))


def check():
    data = json.loads((OUT/DEST).read_text(encoding='utf-8'))
    game, workspace = Path(data['game_root']), OUT.parent
    errors = []
    if sha((game.parent/'launcher/launcher-settings.json').read_bytes()) != data['version_sha256']:
        errors.append('Changed launcher version source')
    if preservation(workspace) != data['preserved_non_documentation_files']:
        errors.append('Non-Documentation file inventory/content changed')
    current_objects = {}
    for rel, row in data['native_sources'].items():
        raw = (game/rel).read_bytes()
        if sha(raw) != row['sha256']:
            errors.append('Changed native source: '+rel)
        for symbol, first, last, block in objects(raw.decode('utf-8-sig')):
            current_objects[f'{rel}:{first}:{symbol}'] = (last, block)
    for identity, row in data['objects'].items():
        actual = current_objects.get(identity)
        if actual is None or actual[0] != row['last_line']:
            errors.append('Object boundary mismatch: '+identity)
    for edge in data['lexical_edges']:
        caller = data['objects'][edge['caller']]
        if any(n < caller['first_line'] or n > caller['last_line'] for n in edge['lines']):
            errors.append('Callsite outside object: '+edge['caller'])
    for rel, expected in data['preserved_non_documentation_files'].items():
        path = workspace/rel
        if not path.exists() or sha(path.read_bytes()) != expected:
            errors.append('Changed workspace file: '+rel)
    for name, row in data['export_declarations'].items():
        raw = (OUT/row['path']).read_bytes()
        if sha(raw) != row['sha256']:
            errors.append('Changed export: '+name)
        lines = raw.decode('utf-8' if name.startswith('triggers') else 'cp1252').splitlines()
        for span in row['spans']:
            if '\n'.join(lines[span['first_line']-1:span['last_line']]) != span['text']:
                errors.append('Export span mismatch: '+name)
    for rel, row in data['mod_sources'].items():
        raw = (workspace/rel).read_bytes()
        if sha(raw) != row['sha256'] or (Path(rel).suffix in {'.txt','.yml'} and not raw.startswith(b'\xef\xbb\xbf')):
            errors.append('Mod preservation/encoding: '+rel)
    print(json.dumps({'status':'failed' if errors else 'passed', 'issues':errors,
                      'native_sources':len(data['native_sources']),
                      'preserved_files':len(data['preserved_non_documentation_files']),
                      'runtime':'not run'}, indent=2))
    raise SystemExit(bool(errors))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    check() if args.check else collect()

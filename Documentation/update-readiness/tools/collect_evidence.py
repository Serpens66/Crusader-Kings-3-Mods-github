"""Read-only source collection; all output stays in update-readiness.

Lexical discovery is not semantic engine validation. Re-running replaces this
audit baseline, so preserve a previous baseline before starting implementation.
"""
import collections
import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
DOC = OUT.parent
WORK = DOC.parent
sys.path.insert(0, str(DOC / 'tools'))
from build_local_reference import TOKEN, definitions

GAME = Path(r'E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\game')
TEXT = {'.txt', '.info', '.gui', '.yml', '.mod', '.asset'}
EXCLUDED = {'Knight Manager (MP)', 'Knight Manager Continued (MP)', 'test'}

def write(name, data):
    p = OUT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data.replace('\r\n', '\n').replace('\n', '\r\n').encode('utf-8'))

def dump(name, obj):
    write(name, json.dumps(obj, ensure_ascii=False, indent=2) + '\n')

def record(p, root):
    raw = p.read_bytes()
    row = {'path': p.relative_to(root).as_posix(), 'bytes': len(raw),
           'sha256': hashlib.sha256(raw).hexdigest()}
    if p.suffix.lower() in TEXT:
        try:
            text = raw.decode('utf-8-sig')
            row['strict_utf8'] = True
        except UnicodeDecodeError:
            text = raw.decode('utf-8-sig', errors='replace')
            row['strict_utf8'] = False
        row.update(bom=raw.startswith(b'\xef\xbb\xbf'), crlf_only=b'\n' not in raw.replace(b'\r\n', b''),
                   lines=len(text.splitlines()), definitions=definitions(text) if p.suffix != '.yml' else [])
    return row

def tokens(text):
    return set(re.findall(r'[A-Za-z_][\w.]*', re.sub(r'#[^\n]*', '', text)))

def main():
    idx = json.loads((DOC/'reference/local-index.json').read_text(encoding='utf-8'))
    version_path = GAME.parent/'launcher/launcher-settings.json'
    version = json.loads(version_path.read_text(encoding='utf-8-sig'))['version']
    workspace = [record(p,WORK) for p in sorted(WORK.rglob('*')) if p.is_file()
                 and DOC not in p.parents and '.git' not in p.relative_to(WORK).parts]
    status = subprocess.run(['git','status','--porcelain=v1'],cwd=WORK,capture_output=True,text=True,check=True).stdout
    manifest = {'date':'2026-10-03','workspace_root':str(WORK),'game_root':str(GAME),
                'version':version,'version_source':str(version_path),
                'version_sha256':hashlib.sha256(version_path.read_bytes()).hexdigest(),
                'git_status':status,'files':workspace,'excluded_update_roots':sorted(EXCLUDED)}
    baseline_path=OUT/'evidence/workspace-baseline.json'
    if baseline_path.exists():
        previous=json.loads(baseline_path.read_text(encoding='utf-8'))
        old={r['path']:r for r in previous['files']};current={r['path']:r for r in workspace}
        drift={'added':sorted(current.keys()-old.keys()),'removed':sorted(old.keys()-current.keys()),
               'changed':sorted(k for k in old.keys()&current.keys() if old[k]['sha256']!=current[k]['sha256'])}
        if any(drift.values()):
            dump('evidence/workspace-drift.json',drift)
            raise SystemExit('Workspace baseline differs; preserve and reconcile it explicitly before continuing.')
    else:
        dump('evidence/workspace-baseline.json',manifest)
    native_records = {r['path']:r for r in idx['native']}
    changed = []
    for rel,r in native_records.items():
        p=GAME/rel
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=r['sha256']:
            changed.append(rel)
    if changed or version!=idx['installed_launcher_version']:
        dump('evidence/stale-index.json',{'changed_native_files':changed,'version':version})
        raise SystemExit('Existing native index is stale; refresh it before analysis.')
    helpers=collections.defaultdict(set)
    helper_areas=('common/scripted_', 'common/modifiers/', 'common/opinion_modifiers/',
                  'common/traits/', 'common/game_rules/', 'common/messages/', 'events/',
                  'common/character_interactions/', 'common/on_action/', 'common/important_actions/')
    for r in idx['native']:
        if r['path'].startswith(helper_areas):
            for d in r['definitions']:
                if d['key']!='namespace': helpers[d['key']].add(r['path'])
    groups={}
    all_seen={}
    base_contracts=[r['path'] for r in idx['native'] if r['path'].endswith('.info')]
    named_seeds=['common/character_interactions/00_gift.txt','gui/game_rules.gui',
                 'gui/multiplayer_types.gui','gui/window_knights.gui',
                 'gui/shared/portraits.gui','gui/window_ledger.gui',
                 'gui/decision_view_widgets/decision_view_widget_decision_option_list_controller.gui',
                 'gfx/map/post_effects/posteffect_volumes.txt','common/defines/00_defines.txt']
    named_seeds += [r['path'] for r in idx['native'] if r['path'].startswith('common/defines/')]
    named_seeds += ['localization/english/gui/character_window_l_english.yml',
                    'localization/german/gui/character_window_l_german.yml']
    for folder in sorted(WORK.iterdir()):
        if not folder.is_dir() or folder.name in EXCLUDED or folder==DOC or folder.name.startswith('.'): continue
        sources=[r for r in workspace if r['path'].startswith(folder.name+'/') and 'definitions' in r]
        seeds=set(base_contracts+named_seeds)
        for r in sources:
            rel=r['path'].split('/',1)[1]
            if (GAME/rel).exists() and Path(rel).suffix.lower() in TEXT: seeds.add(rel)
            text=(WORK/r['path']).read_text(encoding='utf-8-sig',errors='replace')
            for token in tokens(text): seeds.update(helpers.get(token,()))
        # Native counterparts to the bundle's native-derived functionality.
        if folder.name in {'SerpInteractionsDecisions','Mass Demand Conversion'}:
            for r in idx['native']:
                if r['path'].startswith(('common/character_interactions/','common/decisions/')):
                    if any(any(x in d['key'] for x in ('conversion','excommunicat','abdicate','university','education')) for d in r['definitions']):
                        seeds.add(r['path'])
        queue=collections.deque(sorted(seeds)); seen={}; edges=[]; missing=[]
        while queue:
            rel=queue.popleft()
            if rel in seen: continue
            p=GAME/rel
            if not p.exists(): missing.append(rel); continue
            raw=p.read_bytes(); text=raw.decode('utf-8-sig',errors='replace')
            seen[rel]={'sha256':hashlib.sha256(raw).hexdigest(),'lines':len(text.splitlines()),'seed':rel in seeds}
            all_seen[rel]=seen[rel]
            if p.suffix=='.info': continue
            own={x['key'] for x in native_records.get(rel,{}).get('definitions',[])}
            for token in sorted(tokens(text)&helpers.keys()-own):
                for target in sorted(helpers[token]):
                    edges.append({'from':rel,'symbol':token,'to':target})
                    if target not in seen: queue.append(target)
        groups[folder.name]={'workspace_files':[r['path'] for r in sources], 'native_files':seen,
                             'literal_edges':edges,'missing_seed_paths':sorted(set(missing)),
                             'semantic_status':'Discovery complete; see authored feature sheets for reviewed contracts and unresolved engine gaps.'}
    dump('evidence/feature-source-closure.json',{'date':'2026-10-03','version':version,'groups':groups,
         'limits':['Literal names only; no macro expansion.','All .info read completely; executable graphs require semantic review.',
                   'Engine primitives have no native script body.','No game execution.']})
    # Every pairwise same-path collision, including binary assets.
    paths=collections.defaultdict(list); ids=collections.defaultdict(list); native_overrides=[]
    for r in workspace:
        parts=r['path'].split('/',1)
        if len(parts)!=2: continue
        mod,rel=parts
        paths[rel].append(r)
        for d in r.get('definitions',[]):
            if d['key']!='namespace' and not d['key'].startswith('@'):
                ids[(str(Path(rel).parent),d['key'])].append({'mod':mod,'path':r['path'],'line':d['line']})
        if (GAME/rel).is_file():
            native_overrides.append({'mod':mod,'path':r['path'],'native_path':rel,
                'same_bytes':r['sha256']==hashlib.sha256((GAME/rel).read_bytes()).hexdigest()})
    collisions=[{'relative_path':rel,'files':[{'path':r['path'],'sha256':r['sha256']} for r in rows]}
                for rel,rows in sorted(paths.items()) if len(rows)>1 and rel not in {'descriptor.mod','credits.txt','info.txt'}]
    id_collisions=[{'database_directory':k[0],'key':k[1],'definitions':rows} for k,rows in sorted(ids.items()) if len({r['mod'] for r in rows})>1]
    dump('evidence/conflicts.json',{'same_paths':collisions,'same_directory_ids':id_collisions,'native_paths':native_overrides,
         'limits':'Lexical collisions; actual merge semantics and nested object IDs need separate review.'})
    diffs=[]
    for r in native_overrides:
        p=WORK/r['path']; q=GAME/r['native_path']
        if p.suffix.lower() in {'.gui','.txt'}:
            left=p.read_text(encoding='utf-8-sig',errors='replace').splitlines()
            right=q.read_text(encoding='utf-8-sig',errors='replace').splitlines()
            matcher=difflib.SequenceMatcher(a=left,b=right,autojunk=False)
            diffs.append({'workspace':r['path'],'native':r['native_path'], 'mod_lines':len(left),'native_lines':len(right),
                'blocks':[{'change':tag,'mod_start':i+1,'mod_end':j,'native_start':k+1,'native_end':l}
                          for tag,i,j,k,l in matcher.get_opcodes() if tag!='equal']})
    dump('evidence/override-diffs.json',diffs)
    print(json.dumps({'version':version,'workspace_files':len(workspace),'native_index_hashes_checked':len(native_records),
                     'native_sources_read':len(all_seen),'groups':{k:len(v['native_files']) for k,v in groups.items()},
                     'same_paths':len(collisions),'id_candidates':len(id_collisions)},indent=2))

if __name__=='__main__': main()

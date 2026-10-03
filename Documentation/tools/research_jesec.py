"""Read pinned third-party sources and native contracts; write only research evidence.

No upstream scripts run. The existing Vanilla clone/lock/checkout are read-only.
"""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from datetime import datetime, timezone
from workspace_walk import workspace_files

DOC=Path(__file__).resolve().parents[1]
WORK=DOC.parent
CACHE=WORK/'.reference-cache/jesec'
BASE=WORK/'.reference-cache/ck3-mod-base'
GAME=Path(r'E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\game')
REPOS=['ck3-modding-wiki','ck3-mod-more-legacies','ck3-mod-less-restrictive-legacies','ck3-mod-scrollable-legacies']
OUT=DOC/'research/jesec'

def digest(raw):return hashlib.sha256(raw).hexdigest()
def write(path,text):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(text.replace('\r\n','\n').replace('\n','\r\n').encode('utf-8'))
def dump(name,data):write(OUT/name,json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def git(repo,*args,input=None):
    r=subprocess.run(['git','-c','core.hooksPath=NUL','-c','core.autocrlf=false','-C',str(repo),*args],input=input,capture_output=True)
    if r.returncode:raise RuntimeError(r.stderr.decode('utf-8',errors='replace'))
    return r.stdout
def text(raw):
    try:return raw.decode('utf-8-sig')
    except UnicodeDecodeError:return raw.decode('cp1252')
def tree(repo,commit,prefix=None):
    args=['ls-tree','-r','-z',commit]
    if prefix:args+=['--',prefix]
    rows={}
    for item in git(repo,*args).split(b'\0'):
        if not item:continue
        head,path=item.split(b'\t',1);mode,kind,oid=head.decode().split()
        if kind=='blob':rows[path.decode()]={'mode':mode,'blob':oid}
    return rows
def blob(repo,oid):return git(repo,'cat-file','blob',oid)
def initialize():
    if (OUT/'preservation-before.json').exists():
        raise RuntimeError('Existing preservation baseline retained; do not overwrite it.')
    originals={p.relative_to(WORK).as_posix():digest(p.read_bytes()) for p in workspace_files(WORK) if DOC not in p.parents}
    protected={}
    for p in DOC.rglob('*'):
        if not p.is_file() or '__pycache__' in p.parts:continue
        rel=p.relative_to(DOC).as_posix()
        if ('runtime-evidence/' in rel or rel.startswith('update-readiness/evidence/') or
            rel.startswith('reference/') and p.suffix=='.json' or
            p.parent.name=='research' and p.suffix=='.json' and p.name!='sources.json' or
            'verification' in p.name or p.name=='vanilla_history.py' or p.name=='workspace_walk.py'):
            protected[rel]=digest(p.read_bytes())
    settings={}
    user=Path(r'C:\Users\Serpens66\Documents\Paradox Interactive\Crusader Kings III')
    for name in ['dlc_load.json','pdx_settings.json']:
        p=user/name
        if p.exists():settings[str(p)]=digest(p.read_bytes())
    dump('preservation-before.json',{'captured_utc':datetime.now(timezone.utc).isoformat(),
      'original_workspace':originals,'protected_documentation':protected,'profile_settings':settings,
      'base_head':git(BASE,'rev-parse','HEAD').decode().strip(),
      'base_status':git(BASE,'status','--porcelain').decode(),
      'version_path':str(GAME.parent/'launcher/launcher-settings.json'),
      'version_sha256':digest((GAME.parent/'launcher/launcher-settings.json').read_bytes())})
    print(json.dumps({'workspace_files':len(originals),'protected_docs':len(protected),'profile_files':len(settings)}))

def collect():
    lock=json.loads((DOC/'reference/vanilla-history-lock.json').read_text(encoding='utf-8'))
    versions={v:tree(BASE,x['commit'],'base/game') for v,x in lock['versions'].items()}
    evidence={'date':'2026-10-03','repos':{},'historical_baselines':lock,'native_reads':{},'boundaries':[
      'Repository code is observed implementation, not an engine runtime certification',
      'Full-file reads and literal helper discovery do not replace manual parameter/context audit']}
    for name in REPOS:
        repo=CACHE/(name+'.git')
        commit=git(repo,'rev-parse','refs/heads/master^{commit}').decode().strip()
        files=tree(repo,commit)
        records={};contents={}
        for path,row in files.items():
            keep=(path.startswith('wiki_pages/') or path.startswith('mod/') or path in ['README.md','LICENSE','CLAUDE.md'] or
              path.startswith('base/game/common/dynasty_legacies/') or path.startswith('base/game/common/dynasty_perks/') or
              path=='base/game/gui/window_dynasty_house.gui')
            if not keep:continue
            rec=dict(row)
            if row['mode']=='120000':
                raw=blob(repo,row['blob']);rec.update(sha256=digest(raw),symlink=text(raw))
            elif path.endswith(('.md','.txt','.yml','.mod','.info')) or path in ['LICENSE','mod/CHANGELOG']:
                raw=blob(repo,row['blob']);body=text(raw);contents[path]=body
                rec.update(sha256=digest(raw),bytes=len(raw),lines=len(body.splitlines()),full_file_read=True)
                rec['definitions']=[{'name':m[1],'line':body[:m.start()].count('\n')+1} for m in re.finditer(r'(?m)^([A-Za-z_][\w.]*)\s*=\s*\{',body)]
                if path.startswith('base/game/'):
                    rec['compared_versions']={}
                    for v,vt in versions.items():
                        match=vt.get(path)
                        rec['compared_versions'][v]='absent' if not match else 'byte-identical' if match['blob']==row['blob'] else 'different blob'
            else:rec['read_status']='binary asset metadata; not copied'
            records[path]=rec
        # Full tree-based comparison against the exact historical Vanilla snapshot,
        # not the repository README's claimed count of modified files.
        baseline=versions['1.19.0.6'];changed=[]
        for path,row in files.items():
            if path.startswith('base/game/') and (path not in baseline or row['blob']!=baseline[path]['blob']):
                changed.append({'path':path,'status':'added' if path not in baseline else 'different blob','blob':row['blob']})
        deleted=[p for p in baseline if p not in files]
        if name=='ck3-modding-wiki':changed=[];deleted=[]
        # Load all actual current patches (including outside the documented folders).
        for row in changed:
            path=row['path']
            if path not in contents and path.endswith(('.txt','.gui','.info','.yml')):
                raw=blob(repo,row['blob']);body=text(raw);contents[path]=body
                records[path]={**files[path],'sha256':digest(raw),'bytes':len(raw),'lines':len(body.splitlines()),'full_file_read':True}
        descriptor=contents.get('mod/descriptor.mod','')
        evidence['repos'][name]={'url':'https://github.com/jesec/'+name,'commit':commit,
          'commit_info':git(repo,'show','-s','--format=%cI%n%s',commit).decode().splitlines(),
          'bare':git(repo,'rev-parse','--is-bare-repository').decode().strip(),
          'origin':git(repo,'remote','get-url','origin').decode().strip(),
          'tree_entries':len(files),'relevant_files':records,'current_mod_game_patches':changed,
          'deleted_vs_11906':deleted,'descriptor':descriptor,
          'historical_changes':git(repo,'log','--format=%H%x09%cI%x09%s','--','mod','base/game/common/dynasty_legacies','base/game/common/dynasty_perks','base/game/gui/window_dynasty_house.gui').decode().splitlines()}
        # Keep authored local reading notes separate from evidence; no foreign text archive.
        dump(name+'-inventory.json',evidence['repos'][name])
        print(name,commit,len(records),'source records;',len(changed),'current base/game differences',flush=True)
    # Full native files for the matching systems, schema and GUI consumers.
    seeds=set()
    for folder in ['common/dynasty_legacies','common/dynasty_perks','common/script_values','common/modifier_definition_formats']:
        seeds.update(p for p in (GAME/folder).rglob('*') if p.is_file() and p.suffix in {'.txt','.info'})
    for rel in ['gui/window_dynasty_house.gui','gui/window_dynasty_legacy.gui','common/game_rules/00_game_rules.txt']:
        p=GAME/rel
        if p.exists():seeds.add(p)
    # Relevant caller/definition surfaces, including modifier & scope consumers.
    needles=['can_start_new_legacy_track_trigger','dynasty_has_perk','has_dynasty_perk','GetLegacyTracks','DynastyLegacy']
    for root in ['common','gui','localization/english']:
        for p in (GAME/root).rglob('*'):
            if not p.is_file() or p.suffix not in {'.txt','.info','.gui','.yml'}:continue
            raw=p.read_bytes();body=text(raw)
            if any(n in body for n in needles):seeds.add(p)
    for p in sorted(seeds):
        raw=p.read_bytes();body=text(raw)
        evidence['native_reads'][p.relative_to(GAME).as_posix()]={'sha256':digest(raw),'lines':len(body.splitlines()),'full_file_read':True}
    dump('evidence.json',evidence)
    print('Native complete source reads:',len(seeds),flush=True)

def verify():
    before=json.loads((OUT/'preservation-before.json').read_text(encoding='utf-8'))
    errors=[]
    for rel,h in before['original_workspace'].items():
        p=WORK/rel
        if not p.exists() or digest(p.read_bytes())!=h:errors.append('Original changed: '+rel)
    for rel,h in before['protected_documentation'].items():
        p=DOC/rel
        if not p.exists() or digest(p.read_bytes())!=h:errors.append('Protected evidence changed: '+rel)
    for path,h in before['profile_settings'].items():
        if digest(Path(path).read_bytes())!=h:errors.append('Profile changed: '+path)
    if git(BASE,'rev-parse','HEAD').decode().strip()!=before['base_head']:errors.append('Base HEAD changed')
    if git(BASE,'status','--porcelain').decode()!=before['base_status']:errors.append('Base worktree changed')
    if digest(Path(before['version_path']).read_bytes())!=before['version_sha256']:errors.append('Installation version changed')
    evidence=json.loads((OUT/'evidence.json').read_text(encoding='utf-8'))
    native_reads=dict(evidence['native_reads'])
    if (OUT/'feature-audit.json').exists():
        native_reads.update(json.loads((OUT/'feature-audit.json').read_text(encoding='utf-8'))['files'])
    for rel,r in native_reads.items():
        if digest((GAME/rel).read_bytes())!=r['sha256']:errors.append('Native source changed: '+rel)
    result={'status':'passed' if not errors else 'failed','errors':errors,
      'original_workspace_files':len(before['original_workspace']),'protected_doc_files':len(before['protected_documentation']),
      'native_source_files':len(native_reads),'base_head_preserved':not any('Base ' in e for e in errors),
      'cache_excluded':not any('.reference-cache' in p.parts for p in workspace_files(WORK)),
      'gameplay_tests':'not run'}
    dump('preservation-after.json',result);print(json.dumps(result,indent=2))
    if errors or not result['cache_excluded']:raise SystemExit(1)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('action',choices=['initialize','collect','verify']);a=p.parse_args()
    {'initialize':initialize,'collect':collect,'verify':verify}[a.action]()

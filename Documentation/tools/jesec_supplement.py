"""Pinned-source evidence and tables for the jesec supplement. No upstream code runs."""
import collections
import difflib
import json
import re
from research_jesec import DOC, GAME, BASE, CACHE, OUT, REPOS, blob, digest, dump, git, text, tree, write
from build_local_reference import definitions, TOKEN

def blocks(body):
    """Extract complete depth-zero blocks using the existing lexical tokenizer."""
    ts=[m for m in TOKEN.finditer(body) if not m.group().startswith('#')]
    depth=0; start=None; key=None
    for i,m in enumerate(ts):
        if depth==0 and i+2<len(ts) and ts[i+1].group()=='=' and ts[i+2].group()=='{':
            start=m.start();key=m.group()
        if m.group()=='{':depth+=1
        elif m.group()=='}':
            depth-=1
            if depth==0 and start is not None:
                yield key,body[start:m.end()],body[:start].count('\n')+1
                start=None

def load(name):return json.loads((OUT/(name+'-inventory.json')).read_text(encoding='utf-8'))
def source(name,path):return text(blob(CACHE/(name+'.git'),load(name)['relevant_files'][path]['blob']))
def url(name,path,commit=None):return 'https://github.com/jesec/'+name+'/blob/'+(commit or load(name)['commit'])+'/'+path
def audit():
    ev=json.loads((OUT/'evidence.json').read_text(encoding='utf-8'))
    idx=json.loads((DOC/'reference/local-index.json').read_text(encoding='utf-8'))
    helpers=collections.defaultdict(set)
    for row in idx['native']:
        if row['path'].startswith(('common/scripted_','common/script_values/','events/')):
            for x in row['definitions']:helpers[x['key']].add(row['path'])
    needles=set()
    more=REPOS[1];less=REPOS[2]
    for name in [more,less]:
        d=load(name)
        for p,x in d['relevant_files'].items():
            if p.startswith('mod/common/') or p in {r['path'] for r in d['current_mod_game_patches']}:
                t=source(name,p)
                needles.update(re.findall(r'\b(?:bld_\w+|(?:fp[123]|ep3|mpo|tgp)_\w+legacy\w*|tradition_\w+|ethos_\w+|heritage_\w+|eligible_for_\w+|has_\w+_dlc_trigger|\w+scheme_phase_duration_bonus_value)\b',t))
    needles|={'DynastyHouseView.GetLegacies','DynastyLegacy.GetTrackIcon','DynastyLegacy.GetIcon','GetPerks',
              'unrestricted_dynasty_legacies','can_start_new_legacy_track_trigger','story_owner','story_cycle_conqueror'}
    found=collections.defaultdict(list);seeds=set(ev['native_reads'])
    for row in idx['native']:
        p=GAME/row['path'];body=text(p.read_bytes())
        hits=sorted(n for n in needles if n in body)
        if hits:
            seeds.add(row['path'])
            for n in hits:
                found[n].append({'path':row['path'],'lines':[i for i,s in enumerate(body.splitlines(),1) if n in s]})
        if row['path'].endswith('.info') and any(s in row['path'] for s in ['story_cycles','dynasty','government','council','holdings','terrain','flavorization']):seeds.add(row['path'])
    queue=collections.deque(sorted(seeds));reads={};edges=[];bindings=[]
    while queue:
        rel=queue.popleft()
        if rel in reads:continue
        raw=(GAME/rel).read_bytes();body=text(raw)
        reads[rel]={'sha256':digest(raw),'lines':len(body.splitlines()),'full_file_read':True}
        if rel.endswith('.info'):continue
        tokens=set(re.findall(r'[A-Za-z_][\w.]*',re.sub(r'#[^\n]*','',body)))
        own={x['key'] for x in definitions(body)}
        for token in sorted(tokens & helpers.keys()-own):
            for target in sorted(helpers[token]):
                edges.append({'from':rel,'symbol':token,'to':target})
                if target not in reads:queue.append(target)
        for key,b,line in blocks(body):
            params=sorted(set(re.findall(r'\$([A-Za-z_]\w*)\$',b)))
            if params:bindings.append({'path':rel,'definition':key,'line':line,'literal_parameters':params})
    lock=ev['historical_baselines'];old=lock['versions']['1.19.0.6']['commit'];new=lock['versions']['1.20.0.3']['commit']
    historical=[]
    for name,commit in [(less,'44763edca8493e0a6bf1d11c467ea61c94a4b95f'),(more,'0e4a74f953234112140850a8cf3352e12e6f832a'),(REPOS[3],'1df1400d09a760df2d42c0eae268b33da215f773')]:
        paths=git(CACHE/(name+'.git'),'diff','--name-only',commit+'^',commit,'--','base/game','mod').decode().splitlines()
        historical.append({'repository':name,'commit':commit,'changed_paths':paths})
    native_delta=git(BASE,'diff','--name-only',old,new,'--','base/game/common/dynasty_legacies','base/game/common/dynasty_perks','base/game/gui/window_dynasty_house.gui').decode().splitlines()
    historic_gui=[]
    for name,commit in [(REPOS[3],'1df1400d09a760df2d42c0eae268b33da215f773'),(REPOS[3],'3da17897081b9a8b9762ebb1025a45fad9b62a51'),(REPOS[3],'6f512a060be0f5d0149fec567ef77f018d098bec')]:
        path='base/game/gui/window_dynasty_house.gui';raw=git(CACHE/(name+'.git'),'show',commit+':'+path)
        historic_gui.append({'repository':name,'commit':commit,'path':path,'sha256':digest(raw),'lines':len(text(raw).splitlines()),'full_file_read':True})
    engine=json.loads((DOC/'reference/engine-1.20.0.3.json').read_text(encoding='utf-8'))
    names={'has_dynasty_perk','add_dynasty_perk','create_story','end_story','make_story_owner','government_has_mechanic','has_cultural_tradition','has_cultural_pillar'}
    decl=[{'category':x['category'],'name':x['name'],'signature':x['signature'],'source':x['source']['path'],'line':x['line'],'scopes':x['supported_scopes']} for x in engine['entries'] if x['name'] in names or any(n in (x['signature'] or '') for n in ['DynastyLegacy','DynastyHouseView.GetLegacies'])]
    result={'date':'2026-10-03','version':idx['installed_launcher_version'],'files':reads,'caller_matches':dict(found),'helper_edges':edges,'parameterized_definitions':bindings,'historical_origin_changes':historical,'native_11906_to_12003_changes':native_delta,'historic_gui_reads':historic_gui,'engine_declarations':decl,'limits':['Full file reads and lexical closure support navigation; they do not certify every discovered caller or parameter substitution.','Manual contracts in dynasty-legacies.md are restricted to the reviewed track/perk fields, visibility/pick gates, AI helper, values and GUI surfaces.','Native conditional DLC effects are not converted into guarantees of benefits for every newly eligible government.','No game or GUI/MP test was run; all original runtime blockers remain.']}
    dump('feature-audit.json',result)
    print('Feature evidence:',len(reads),'complete files,',len(edges),'literal helper edges; parameterized surfaces recorded, not assumed safe')

def tables():
    more=REPOS[1];less=REPOS[2];tracks=dict((k,(b,line)) for k,b,line in blocks(source(more,'mod/common/dynasty_legacies/more_legacies.txt')))
    perks=list(blocks(source(more,'mod/common/dynasty_perks/more_dynasty_perks.txt')))
    names={};locs={}
    d=load(more)
    for p,x in d['relevant_files'].items():
        if p.startswith('mod/localization/') and p.endswith('.yml'):
            keys=re.findall(r'(?m)^[ \t]*(\w+):\d*[ \t]+"(.*)"',source(more,p));locs[p]=dict(keys)
            if '/english/' in p:names.update(keys)
    lines=['# More Legacies: complete source map','','Source: ['+d['commit']+']('+url(more,'mod')+'). Authored table of observed code, not tested modifier semantics. See [contracts](../../systems/dynasty-legacies.md).','','## Track visibility','','Every restricted track also has an OR branch retaining visibility when its first perk is owned. Four track blocks have no `is_shown`. Restricted conditions inspect the dynast, not automatically the GUI viewer.','','| Track | Definition line | Additional visibility inputs |','|---|---:|---|']
    for k,(b,line) in tracks.items():
        vals=re.findall(r'(?:has_cultural_tradition|has_cultural_pillar|has_trait|secret_type)\s*=\s*(\w+)',b)
        lines.append('| `'+k+'` | '+str(line)+' | '+(', '.join('`'+s+'`' for s in vals) or 'No explicit visibility block')+' |')
    lines+=['','## All 50 perk payloads','','Numbers below are source values. A negative build speed or phase duration modifier is not a negative success chance. Named values must be evaluated from their definition. No perk in these two mod files adds a custom `effect`, saved state, event or on action.','','| ID / English name | Line | Character modifier assignments |','|---|---:|---|']
    mods=set()
    for k,b,line in perks:
        payload=re.search(r'character_modifier\s*=\s*\{([^{}]*)\}',b).group(1)
        pairs=re.findall(r'(\w+)\s*=\s*([\w.\-]+)',payload);mods|={x[0] for x in pairs}
        lines.append('| `'+k+'` / '+names.get(k+'_name','MISSING')+' | '+str(line)+' | '+'; '.join('`'+a+' = '+v+'`' for a,v in pairs)+' |')
    required={k+'_name' for k in tracks}|{k+'_name' for k,b,line in perks}
    errors={p:sorted(required-keys.keys()) for p,keys in locs.items()}
    lines+=['','## Localization and assets','','| Language file | Missing track/perk name keys |','|---|---|']
    for p,missing in errors.items():lines.append('| ['+p+']('+url(more,p)+') | '+str(len(missing))+' |')
    lines+=['','All ten IDs have one icon and one illustration path in the repository tree. The inventory records the twenty DDS Git object IDs; pixels/formats/frames were not imported or rendered. `GetIcon` and `GetTrackIcon` are different GUI consumers. Their engine-side path resolution must not be guessed from filenames alone.','',
      '## AI and initialization caveats','','The ten first perks set `ai_chance.value = 11` and multiply by zero when `can_start_new_legacy_track_trigger = no`; the other forty omit an AI block. The installed perk `.info` documents a default weight of 1000. These are relative selection weights, not percentages. The helper enumerates native tracks explicitly, including the new PAM track, but none of the `bld_` tracks. Therefore its name does not prove that it prevents several custom tracks from being opened together. Trace/customize the policy and test AI separately.','',
      'The supplied README describes `tolerance_advantage_mod = 5` as tolerance opinion, while the source uses an advantage modifier. Treat the code/engine entry as the starting point for a tooltip/benefit test, not the prose description. No balance or 1.20 compatibility claim is adopted.','']
    write(OUT/'more-legacies-map.md','\n'.join(lines))
    engine=json.loads((DOC/'reference/engine-1.20.0.3.json').read_text(encoding='utf-8'));known={x['name'] for x in engine['entries'] if x['category']=='modifier'}
    dump('more-legacies-checks.json',{'tracks':len(tracks),'perks':len(perks),'name_keys_required':len(required),'localizations':errors,'modifier_keys':sorted(mods),'not_literal_modifier_export_names':sorted(mods-known),'interpretation':'Absence from the literal modifier category is not automatically invalid: generated modifier formats and datatype contexts are separate. See native modifier_definition_formats and runtime tests.'})

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('action',choices=['audit','tables']);a=p.parse_args()
    {'audit':audit,'tables':tables}[a.action]()

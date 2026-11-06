"""Research official CK3 news; save receipts and original summaries, not article copies.

Use -B. Only collect/inspect contact Steam; no game, upstream script or installer runs.
"""
import argparse
import collections
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import sys
import urllib.request
from workspace_walk import workspace_files

DOC=Path(__file__).resolve().parents[1]
WORK=DOC.parent
GAME=Path(r'E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\game')
OUT=DOC/'research/game-news-20261103'
API='https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1158310&count=1000&maxlength=0&feeds=steam_community_announcements'
START=1735689600
END=1793746800 # End of 2026-11-03 in Europe/Berlin.
PATTERN=re.compile(r'modding|script(?:ed|ing|s| value)?|\.info\b|on.action|GUI|hot.reload|scope|data.type|shader|FMOD|mesh|animationpack|portrait.modifier|performance|debug|changelog|patch.note',re.I)

def sha(b):return hashlib.sha256(b).hexdigest()
def write(p,s):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_bytes(s.replace('\r\n','\n').replace('\n','\r\n').encode('utf-8'))
def dump(name,obj):write(OUT/name,json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def readj(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def clean(s):
    s=html.unescape(re.sub(r'<br\s*/?>','\n',s,flags=re.I))
    s=re.sub(r'</?(?:p|div|span|strong|em|ul|ol|li|table|tr|td|h[1-6])\b[^>]*>','\n',s,flags=re.I)
    return re.sub(r'\[/?(?:h[1-6]|list|olist|table|tr|td|th|p|b|code|quote)\]|\[\*\]','\n',s,flags=re.I)
def fetch():
    with urllib.request.urlopen(API,timeout=60) as response:
        return json.load(response)['appnews']['newsitems']
def baseline():
    if (OUT/'preservation-before.json').exists():raise RuntimeError('Do not replace original baseline')
    originals={p.relative_to(WORK).as_posix():sha(p.read_bytes()) for p in workspace_files(WORK) if DOC not in p.parents}
    docs={p.relative_to(DOC).as_posix():sha(p.read_bytes()) for p in DOC.rglob('*') if p.is_file() and '__pycache__' not in p.parts and OUT not in p.parents}
    settings={}
    user=Path(r'C:\Users\Serpens66\Documents\Paradox Interactive\Crusader Kings III')
    for p in user.glob('*.json'):settings[str(p)]=sha(p.read_bytes())
    dump('preservation-before.json',{'date':'2026-11-03','workspace':originals,'documentation':docs,'settings':settings,'version':readj(GAME.parent/'launcher/launcher-settings.json')})
    print('Preservation baseline:',len(originals),'workspace files;',len(docs),'documentation files')
def collect():
    items=fetch();rows=[];seen=set();duplicates=[]
    for x in items:
        if x['gid'] in seen:duplicates.append(x['gid']);continue
        seen.add(x['gid']);body=clean(x['contents']);title=x['title']
        in_period=START<=x['date']<END
        older=bool(re.search(r'Diary #(?:55|87|126|156)\b',title))
        if not (in_period or older):continue
        hits=[{'line':i,'kinds':sorted(set(m.group().lower() for m in PATTERN.finditer(s)))} for i,s in enumerate(body.splitlines(),1) if PATTERN.search(s)]
        urls=re.findall(r'(?:https?://)[^\s\]<>"\)]+',body)
        rows.append({'id':'NEWS-'+x['gid'],'gid':x['gid'],'title':title,'published_utc':datetime.fromtimestamp(x['date'],timezone.utc).isoformat(),'retrieved_utc':datetime.now(timezone.utc).isoformat(),'url':x['url'],'view_url':'https://store.steampowered.com/news/app/1158310/view/'+x['gid'],'feed':x.get('feedname'),'source_body_sha256':sha(x['contents'].encode('utf-8')),'plain_body_sha256':sha(body.encode('utf-8')),'characters':len(body),'lines':len(body.splitlines()),'period':'2025-2026' if in_period else 'targeted older reference','keyword_matches':hits,'links':urls,'read_status':'complete official article body scanned; semantic treatment assigned separately'})
    dump('catalogue.json',{'api':API,'date':'2026-11-03','total_api_records':len(items),'oldest_api_utc':datetime.fromtimestamp(min(x['date'] for x in items),timezone.utc).isoformat(),'duplicate_gids':duplicates,'articles':rows,'limits':['Feed discovery is not a guarantee that every historical forum post is present.','Keyword matching selects candidates; relevant/irrelevant treatment requires review.','Full article bodies stay in memory and are not distributed in Documentation.']})
    print('Catalogue:',len(rows),'articles;',sum(bool(r['keyword_matches']) for r in rows),'candidate articles')
    for r in rows:print(r['gid'],r['published_utc'][:10],len(r['keyword_matches']),r['title'])
def inspect(query):
    selected={r['gid'] for r in readj(OUT/'catalogue.json')['articles']}
    for x in fetch():
        if x['gid'] not in selected:continue
        if query==x['gid'] or (bool(re.search(r'#9\b',x['title'])) if query=='#9' else query.lower() in x['title'].lower()):
            print('\nARTICLE',x['gid'],x['title'],x['url']);body=clean(x['contents'])
            if query=='#9':print(body)
            else:
                lines=body.splitlines();indices=set()
                for i,s in enumerate(lines):
                    if PATTERN.search(s):indices.update(range(max(0,i-1),min(len(lines),i+4)))
                print('\n'.join(f'{i+1}: {lines[i]}' for i in sorted(indices)))
def audit():
    from build_local_reference import definitions
    needles=['can_change_faith','special_interaction = reform_faith','doctrine_divergence',
      'doctrine_in_same_group','construction_soundeffect','GetGameConcept','game_concept_tooltip',
      'PATTERN_MASK_MIN_SIZE_PER_QUALITY','RITE_CREATION_DESCRIPTION_MAX_LENGTH','RELIGIOUS_HEADS_VISIBLE_ZOOM_STEPS',
      'situation_type','subject_contract','top_overlord','confederation','visualization',
      'animationpack','portrait_modifier','DataModelJoinList','id_override_priority']
    bodies={};hashes={};helpers=collections.defaultdict(set);seeds=set();matches=collections.defaultdict(list)
    old=readj(DOC/'reference/local-index.json');previous={r['path']:r['sha256'] for r in old['native']}
    roots=['common','events','gui','history','gfx','localization/english','map_data']
    for folder in roots:
        for p in (GAME/folder).rglob('*'):
            if not p.is_file() or p.suffix not in {'.txt','.info','.gui','.yml','.asset','.shader','.fx'}:continue
            rel=p.relative_to(GAME).as_posix();raw=p.read_bytes()
            try:t=raw.decode('utf-8-sig')
            except UnicodeDecodeError:t=raw.decode('cp1252',errors='replace')
            bodies[rel]=t;hashes[rel]=sha(raw)
            if rel.startswith(('common/scripted_','common/script_values/','events/')):
                for row in definitions(t):helpers[row['key']].add(rel)
            hits=[n for n in needles if n in t]
            if p.suffix=='.info' or hits or rel.startswith(('common/situations/','common/subject_contract','common/confederation','common/story_cycles/','common/music/')):seeds.add(rel)
            for n in hits:matches[n].append({'path':rel,'lines':[i for i,s in enumerate(t.splitlines(),1) if n in s]})
    reads={};edges=[];parameters=[];q=collections.deque(sorted(seeds))
    while q:
        rel=q.popleft()
        if rel in reads:continue
        t=bodies[rel];reads[rel]={'sha256':hashes[rel],'lines':len(t.splitlines()),'full_file_read':True,'versus_12003':'unchanged' if previous.get(rel)==hashes[rel] else 'changed' if rel in previous else 'not in old index'}
        if rel.endswith('.info'):continue
        tokens=set(re.findall(r'[A-Za-z_][\w.]*',re.sub(r'#[^\n]*','',t)))
        own={r['key'] for r in definitions(t)}
        for key in sorted(tokens & helpers.keys()-own):
            for target in sorted(helpers[key]):
                edges.append({'from':rel,'symbol':key,'to':target})
                if target not in reads:q.append(target)
        params=sorted(set(re.findall(r'\$([A-Z_]\w*)\$',t)))
        if params:parameters.append({'path':rel,'parameters':params})
    forecast=['prosperity_level','add_regular_district','add_to_variable_map','GetModiferValue','GetModifierValue','ai_frequency_by_tier_government_override','confederation_base']
    future_hits={n:[{'path':rel,'lines':[i for i,s in enumerate(t.splitlines(),1) if n in s]} for rel,t in bodies.items() if n in t] for n in forecast}
    dump('native-audit.json',{'date':'2026-11-03','version':readj(GAME.parent/'launcher/launcher-settings.json'),'files':reads,'literal_helper_edges':edges,'macro_parameter_surfaces':parameters,'topic_matches':dict(matches),'forecast_literal_matches':future_hits,'limits':['Complete file reads and literal dependency discovery do not certify every caller or parameter expansion.','Manual narrow schema/caller findings and remaining engine contracts are distinguished in the handbook supplement.','Absence from script text is not proof of engine absence. Historical exports are not relabelled 1.20.1.2.','No fresh runtime dump, gameplay, GUI, MP or performance measurement.']})
    print('Audited full files:',len(reads),'literal helper edges:',len(edges),'current .info files:',sum(p.endswith('.info') for p in reads))
if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    p=argparse.ArgumentParser();p.add_argument('action',choices=['baseline','collect','inspect','audit']);p.add_argument('query',nargs='?',default='');a=p.parse_args()
    if a.action=='baseline':baseline()
    elif a.action=='collect':collect()
    elif a.action=='audit':audit()
    else:inspect(a.query)

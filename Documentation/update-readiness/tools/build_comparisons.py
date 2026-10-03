"""Generate source comparison tables, not engine compatibility verdicts."""
import collections
import hashlib
import json
import re
import struct
import sys
from pathlib import Path
from collect_evidence import OUT, DOC, WORK, GAME, write, dump
sys.path.insert(0,str(DOC/'tools'))
from build_local_reference import definitions, TOKEN

def image_header(p):
    raw=p.read_bytes()
    if raw[:4]==b'DDS ' and len(raw)>=128:
        h,w=struct.unpack_from('<II',raw,12)
        return {'container':'DDS','width':w,'height':h,'fourcc':raw[84:88].hex(),
                'mipmaps':struct.unpack_from('<I',raw,28)[0]}
    if raw[:8]==b'\x89PNG\r\n\x1a\n' and len(raw)>=24:
        w,h=struct.unpack_from('>II',raw,16)
        return {'container':'PNG','width':w,'height':h}
    return {'container':'unrecognized','prefix_hex':raw[:8].hex()}

def assignments(s):
    # Sufficient for the installed define namespace -> scalar/list structure.
    namespace='';rows=[]
    for i,line in enumerate(s.splitlines(),1):
        code=line.split('#',1)[0].strip()
        m=re.match(r'^(\w+)\s*=\s*\{',line)
        if m: namespace=m.group(1);continue
        if not code or code=='}':continue
        m=re.match(r'(\w+)\s*=\s*(.+)',code)
        if m and namespace:rows.append({'namespace':namespace,'key':m.group(1),'value':m.group(2).strip(),'line':i})
    return rows

def main():
    baseline=json.loads((OUT/'evidence/workspace-baseline.json').read_text(encoding='utf-8'))
    native_defs=collections.defaultdict(list)
    for p in sorted((GAME/'common/defines').rglob('*.txt')):
        for r in assignments(p.read_text(encoding='utf-8-sig',errors='replace')):
            native_defs[(r['namespace'],r['key'])].append(dict(r,path=p.relative_to(GAME).as_posix()))
    changes=[]
    for p in sorted((WORK/'CustomDefines/common/defines').rglob('*.txt')):
        for r in assignments(p.read_text(encoding='utf-8-sig')):
            changes.append(dict(r,path=p.relative_to(WORK).as_posix(),native=native_defs[(r['namespace'],r['key'])]))
    dump('evidence/defines.json',changes)
    lines=['# Active define comparison','', 'Exact namespace/key matching against installed native definitions. Numeric behavior still needs the stated gameplay tests.','',
           '| Key | Mod value | Native value | Mod location | Native location |','|---|---|---|---|---|']
    for r in changes:
        refs=r['native']
        lines.append('| `'+r['namespace']+'.'+r['key']+'` | `'+r['value']+'` | '+('; '.join('`'+x['value']+'`' for x in refs) or 'NOT FOUND')+' | `'+r['path']+':'+str(r['line'])+'` | '+'; '.join('`'+x['path']+':'+str(x['line'])+'`' for x in refs)+' |')
    write('define-comparison.md','\n'.join(lines)+'\n')
    textures=[]
    for r in baseline['files']:
        mod=r['path'].split('/')[0]
        if mod not in {'Gender Colour','GFX-Mod','GFX-Mod Serp'} or not r['path'].endswith('.dds'):continue
        rel=r['path'].split('/',1)[1];p=WORK/r['path'];q=GAME/rel
        a=image_header(p);b=image_header(q) if q.exists() else None
        textures.append({'mod':mod,'path':r['path'],'native_path':rel if q.exists() else None,
            'mod_header':a,'native_header':b,'same_bytes':q.exists() and hashlib.sha256(q.read_bytes()).hexdigest()==r['sha256'],
            'size_changed':b is not None and (a.get('width'),a.get('height'))!=(b.get('width'),b.get('height')),
            'native_sha256':hashlib.sha256(q.read_bytes()).hexdigest() if q.exists() else None})
    dump('evidence/textures.json',textures)
    lines=['# Texture comparison','', 'Dimensions are header values (width × height). A missing native same-path file does not establish that an asset is unused: scripted or dynamic references may still load it. A header mismatch is not a rendered failure.','',
           '| Package | Textures | Without native same path | Size differs | Non DDS containers under dds extension |','|---|---:|---:|---:|---:|']
    for mod in ['Gender Colour','GFX-Mod','GFX-Mod Serp']:
        rows=[x for x in textures if x['mod']==mod]
        lines.append(f"| {mod} | {len(rows)} | {sum(x['native_path'] is None for x in rows)} | {sum(x['size_changed'] for x in rows)} | {sum(x['mod_header']['container']!='DDS' for x in rows)} |")
    lines+=['','## Size differences','','| File | Mod width × height | Native width × height |','|---|---|---|']
    for r in textures:
        if r['size_changed']:
            a,b=r['mod_header'],r['native_header'];lines.append(f"| `{r['path']}` | {a.get('width')} × {a.get('height')} | {b.get('width')} × {b.get('height')} |")
    lines+=['','## Other container types','','| File | Container |','|---|---|']
    lines += [f"| `{r['path']}` | {r['mod_header']['container']} |" for r in textures if r['mod_header']['container']!='DDS']
    write('texture-comparison.md','\n'.join(lines)+'\n')
    lines=['# Mod entry points and supporting definitions','', 'Complete lexical top-level definition inventory for relevant gameplay content. Localization keys and binary assets are inventoried separately. Field/type legality is not inferred from this table.','',
           '| Package | Source | Definitions with lines |','|---|---|---|']
    for r in baseline['files']:
        if r['path'].split('/')[0] in baseline['excluded_update_roots'] or '/common/defines/' in r['path'] or r['path'].endswith('descriptor.mod'):continue
        if r.get('definitions'):
            lines.append('| '+r['path'].split('/')[0]+' | `'+r['path']+'` | '+'; '.join('`'+d['key']+':'+str(d['line'])+'`' for d in r['definitions'])+' |')
    write('entry-points.md','\n'.join(lines)+'\n')
    # Native IDs under a different filename, plus localization replacement keys.
    index=json.loads((DOC/'reference/local-index.json').read_text(encoding='utf-8'))
    native_by_id=collections.defaultdict(list)
    for r in index['native']:
        for d in r['definitions']:native_by_id[(str(Path(r['path']).parent),d['key'])].append(dict(d,path=r['path']))
    overrides=[]
    for r in baseline['files']:
        if r['path'].split('/')[0] in baseline['excluded_update_roots']:continue
        rel=r['path'].split('/',1)[1] if '/' in r['path'] else ''
        for d in r.get('definitions',[]):
            refs=native_by_id.get((str(Path(rel).parent),d['key']),[])
            if refs:overrides.append({'workspace':r['path'],'key':d['key'],'line':d['line'],'native':refs})
    dump('evidence/native-id-overrides.json',overrides)
    # Exact planned removal candidates; authored sheet reviews incoming references.
    removal=[r['path'] for r in baseline['files'] if r['path'].startswith('CustomDefines/') and
             ('knight_manager' in r['path'] or r['path'].endswith('/knighthood_trigger.txt') or r['path'].endswith('/window_knights.gui'))]
    dump('evidence/knight-removal-candidates.json',removal)
    print(json.dumps({'active_defines':len(changes),'unmatched_defines':sum(not x['native'] for x in changes),
                     'textures':len(textures),'knight_removal_files':len(removal),'native_id_candidates':len(overrides)},indent=2))

if __name__=='__main__':main()

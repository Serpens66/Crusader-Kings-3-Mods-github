"""Discover native literal/symbolic texture consumers without claiming dynamic completeness."""
import collections
import hashlib
import json
import re
from pathlib import Path
from collect_evidence import OUT, DOC, GAME, dump, write

def main():
    textures=json.loads((OUT/'evidence/textures.json').read_text(encoding='utf-8'))
    index=json.loads((DOC/'reference/local-index.json').read_text(encoding='utf-8'))
    by_path=collections.defaultdict(list);by_name=collections.defaultdict(list);by_stem=collections.defaultdict(list)
    for i,r in enumerate(textures):
        rel=r['path'].split('/',1)[1].lower()
        by_path[rel].append(i);by_name[Path(rel).name].append(i);by_stem[Path(rel).stem].append(i)
    results=[{'path':r['path'],'exact_path':[],'basename':[],'symbolic_icon':[],'matching_object_ids':[]} for r in textures]
    scanned={}
    for r in index['native']:
        rel=r['path']
        if not rel.startswith(('gui/','common/','gfx/')) or not rel.endswith(('.gui','.txt','.asset')):continue
        raw=(GAME/rel).read_bytes();text=raw.decode('utf-8-sig',errors='replace')
        scanned[rel]=hashlib.sha256(raw).hexdigest()
        for line_num,line in enumerate(text.splitlines(),1):
            if line.lstrip().startswith('#'):continue
            for m in re.finditer(r'"([^"\r\n]*\.dds)"|(?<![\w])([\w./\\-]+\.dds)',line):
                token=(m.group(1) or m.group(2)).replace('\\','/').lower()
                exact=by_path.get(token,[])
                for i in exact:
                    if len(results[i]['exact_path'])<8:results[i]['exact_path'].append({'file':rel,'line':line_num,'literal':token})
                if not exact:
                    for i in by_name.get(Path(token).name,[]):
                        if len(results[i]['basename'])<8:results[i]['basename'].append({'file':rel,'line':line_num,'literal':token})
            for m in re.finditer(r'\bicon\s*=\s*"?([\w./-]+)',line):
                token=Path(m.group(1)).stem.lower()
                for i in by_stem.get(token,[]):
                    if len(results[i]['symbolic_icon'])<8:results[i]['symbolic_icon'].append({'file':rel,'line':line_num,'literal':m.group(1)})
        for d in r['definitions']:
            for i in by_stem.get(d['key'].lower(),[]):
                if len(results[i]['matching_object_ids'])<8:results[i]['matching_object_ids'].append({'file':rel,'line':d['line'],'key':d['key']})
    dump('evidence/asset-consumers.json',{'method':'Native gui/common/gfx text scan; each evidence list capped at 8. Exact paths, basename and icon/object-name matches are separate confidence levels.',
         'scanned_native_hashes':scanned,'textures':results,'limits':['Dynamic path construction and compiled renderer are not resolved.','No match does not establish unused content.','Basename/icon/object-ID match does not prove loading.']})
    missing=[r for r in textures if r['native_path'] is None]
    lookup={r['path']:r for r in results}
    lines=['# Static texture consumer discovery','','Search date: 2026-10-03. Every retained graphical texture was considered; native GUI, common definitions and graphics declarations were read. [Raw matches and scanned hashes](evidence/asset-consumers.json) separate exact paths from weaker symbolic matches.','','| Package | Textures | Exact path match | Any discovered match |','|---|---:|---:|---:|']
    for mod in ['Gender Colour','GFX-Mod','GFX-Mod Serp']:
        rows=[r for r in results if r['path'].startswith(mod+'/')]
        lines.append(f"| {mod} | {len(rows)} | {sum(bool(r['exact_path']) for r in rows)} | {sum(any(r[k] for k in ['exact_path','basename','symbolic_icon','matching_object_ids']) for r in rows)} |")
    lines+=['','## Assets without a native same path','','These are not automatically obsolete: listed candidates may be dynamically selected. Unmatched candidates require actual renderer/context evidence before deletion or remapping.','','| Texture | First discovered candidate | Match level |','|---|---|---|']
    for r in missing:
        row=lookup[r['path']];found=next(((k,row[k][0]) for k in ['exact_path','basename','symbolic_icon','matching_object_ids'] if row[k]),None)
        if found:
            k,ref=found;loc=ref['file']+':'+str(ref['line'])
        else:k,loc='unresolved','No static/symbolic match found'
        lines.append(f"| `{r['path']}` | `{loc}` | {k} |")
    write('asset-consumers.md','\n'.join(lines)+'\n')
    print(json.dumps({'native_text_files_scanned':len(scanned),'textures_considered':len(results),
                      'exact_path_matches':sum(bool(r['exact_path']) for r in results)},indent=2))

if __name__=='__main__':main()

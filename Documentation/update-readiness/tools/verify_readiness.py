"""Check evidence preservation and documentation coverage without running CK3."""
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
from collect_evidence import OUT, DOC, WORK, GAME, dump, write

def main():
    baseline=json.loads((OUT/'evidence/workspace-baseline.json').read_text(encoding='utf-8'))
    closure=json.loads((OUT/'evidence/feature-source-closure.json').read_text(encoding='utf-8'))
    matrix=json.loads((OUT/'feature-matrix.json').read_text(encoding='utf-8'))
    issues=[];counts={}
    for r in baseline['files']:
        p=WORK/r['path']
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=r['sha256']:
            issues.append('Changed original workspace file: '+r['path'])
    counts['original_workspace_files']=len(baseline['files'])
    actual={p.relative_to(WORK).as_posix() for p in WORK.rglob('*') if p.is_file() and DOC not in p.parents and '.git' not in p.relative_to(WORK).parts}
    if actual!={r['path'] for r in baseline['files']}:
        issues.append('Original workspace file set changed outside Documentation')
    native={}
    for group in closure['groups'].values():native.update(group['native_files'])
    for rel,r in native.items():
        p=GAME/rel
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=r['sha256']:
            issues.append('Changed audited installation file: '+rel)
    counts['audited_native_files']=len(native)
    consumers=json.loads((OUT/'evidence/asset-consumers.json').read_text(encoding='utf-8'))
    for rel,h in consumers['scanned_native_hashes'].items():
        if hashlib.sha256((GAME/rel).read_bytes()).hexdigest()!=h:
            issues.append('Changed asset-consumer source: '+rel)
    counts['asset_consumer_source_hashes']=len(consumers['scanned_native_hashes'])
    version_file=Path(baseline['version_source'])
    if hashlib.sha256(version_file.read_bytes()).hexdigest()!=baseline['version_sha256']:
        issues.append('Installation version metadata changed')
    textures=json.loads((OUT/'evidence/textures.json').read_text(encoding='utf-8'))
    native_textures={r['native_path']:r['native_sha256'] for r in textures if r['native_path']}
    for rel,h in native_textures.items():
        if hashlib.sha256((GAME/rel).read_bytes()).hexdigest()!=h:
            issues.append('Native texture changed: '+rel)
    counts['native_texture_hashes']=len(native_textures)
    ids=set();counts['links']=0;counts['documentation_text_files']=0
    for p in OUT.rglob('*'):
        if not p.is_file() or '__pycache__' in p.parts or p.suffix=='.pyc':continue
        raw=p.read_bytes()
        try:s=raw.decode('utf-8-sig')
        except UnicodeDecodeError:
            issues.append('Invalid UTF-8: '+str(p));continue
        counts['documentation_text_files']+=1
        if b'\n' in raw.replace(b'\r\n',b'') or b'\r' in raw.replace(b'\r\n',b''):
            issues.append('Non CRLF: '+str(p))
        if p.suffix in {'.txt','.yml'} and not raw.startswith(b'\xef\xbb\xbf'):
            issues.append('Missing BOM: '+str(p))
        if p.suffix=='.py':
            try:compile(s,str(p),'exec')
            except SyntaxError as e:issues.append(str(e))
        if p.suffix=='.md':
            text=re.sub(r'```.*?```','',s,flags=re.S)
            for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)',text):
                target=target.strip().strip('<>');parts=urlsplit(target)
                if parts.scheme or target.startswith('#'):continue
                counts['links']+=1
                if not (p.parent/unquote(target.split('#',1)[0])).resolve().exists():
                    issues.append('Broken link: '+str(p)+' -> '+target)
            if p.parent.name=='mods':ids.update(re.findall(r'^\| ([A-Z]+-[A-Z-]+) \|',s,flags=re.M))
    listed={r['id'] for r in matrix['features']}
    if ids!=listed or len(listed)!=len(matrix['features']):issues.append('Feature sheet/matrix ID mismatch')
    for r in matrix['features']:
        if not all(r.get(k) for k in ['status','mechanics','resolution','sheet']):issues.append('Incomplete package: '+r['id'])
        if r['runtime']!='not run':issues.append('Unexecuted runtime marked otherwise: '+r['id'])
    counts['feature_packages']=len(listed)
    filemap=json.loads((OUT/'evidence/feature-file-map.json').read_text(encoding='utf-8'))
    retained=set(closure['groups'])
    expected={r['path'] for r in baseline['files'] if r['path'].split('/')[0] in retained}
    if expected!={r['file'] for r in filemap}:issues.append('Retained package file coverage incomplete')
    for r in filemap:
        if not set(r['packages'])<=listed or not r['packages']:issues.append('Unassigned source: '+r['file'])
    counts['retained_package_file_assignments']=len(filemap)
    defines=json.loads((OUT/'evidence/defines.json').read_text(encoding='utf-8'))
    if len(defines)!=23 or any(not r['native'] for r in defines):issues.append('Define evidence missing')
    removal=json.loads((OUT/'evidence/knight-removal-candidates.json').read_text(encoding='utf-8'))
    if len(removal)!=12 or any(not x.startswith('CustomDefines/') for x in removal):issues.append('Knight removal list invalid')
    for group in closure['groups'].values():
        if group['missing_seed_paths']:issues.append('Missing native seed: '+str(group['missing_seed_paths']))
    result={'date':'2026-10-03','version':baseline['version'],'status':'passed' if not issues else 'failed',
            'checks':counts,'issues':issues,'limits':['No game launch or runtime tests','No Tiger run',
            'Lexical/source checks are not full engine type/grammar/GUI validation',
            'Source closure is not a semantic audit of all engine primitives']}
    dump('verification.json',result)
    lines=['# Update readiness verification','',f"Date: 2026-10-03. Source baseline: **{baseline['version']}**. Status: **{result['status']}**.",'',
           '| Check | Count |','|---|---:|']
    lines += [f'| {k.replace("_"," ")} | {v} |' for k,v in counts.items()]
    lines += ['','## Issues','']+ (issues or ['No issues found by the checks above.'])
    lines += ['','## Limits','']+['- '+x for x in result['limits']]
    lines += ['','Original scripts, assets, excluded mods, descriptors and other workspace files were compared byte-for-byte against the recorded baseline. No files were written outside Documentation. The manifest protects the pre-existing user state rather than relying on a clean Git checkout.']
    write('verification.md','\n'.join(lines)+'\n')
    print(json.dumps(result,indent=2));return bool(issues)

if __name__=='__main__':sys.exit(main())

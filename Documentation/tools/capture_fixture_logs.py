"""Read-only user-run CK3 fixture log snapshots. Never launches or selects mods."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

DOC = Path(__file__).resolve().parents[1]
PROFILE = Path(r'C:\Users\Serpens66\Documents\Paradox Interactive\Crusader Kings III')
OUT = DOC / 'examples' / 'run-evidence'

def sha(raw): return hashlib.sha256(raw).hexdigest()

def candidates():
    logs = PROFILE / 'logs'
    if logs.exists():
        for p in sorted(logs.rglob('*')):
            if p.is_file() and p.suffix.lower() in {'.log', '.txt', '.json'}:
                yield p
    crashes = PROFILE / 'crashes'
    if crashes.exists():
        for p in sorted(crashes.rglob('*')):
            # Metadata/errors/logs only. Explicitly exclude saves, memory dumps and binaries.
            if p.is_file() and p.suffix.lower() in {'.log', '.txt', '.json'} and not any('save' in part.lower() or 'dump' in part.lower() for part in p.relative_to(crashes).parts):
                yield p
    for name in ['dlc_load.json', 'pdx_settings.json']:
        p = PROFILE / name
        if p.is_file(): yield p

def collect(label, phase):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_-]{0,63}', label):
        raise ValueError('Label must contain only letters, numbers, dash and underscore')
    base = OUT / label
    prior = sorted(base.glob('*-begin/manifest.json')) if base.exists() else []
    baseline = json.loads(prior[-1].read_text(encoding='utf-8')) if phase == 'end' and prior else None
    expected = {x['source']:x for x in baseline['files']} if baseline else {}
    now = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    destination = base / (now + '-' + phase)
    destination.mkdir(parents=True, exist_ok=False)
    rows=[]; errors=[]
    for p in candidates():
        try:
            before=p.stat(); raw=p.read_bytes(); after=p.stat()
            rel=p.relative_to(PROFILE).as_posix(); digest=sha(raw)
            stable=(before.st_mtime_ns,before.st_size)==(after.st_mtime_ns,after.st_size)
            old=expected.get(str(p)); changed=old is None or old['sha256']!=digest
            status='baseline snapshot' if phase=='begin' else ('new or byte-changed' if baseline and changed else 'byte-identical to begin' if baseline else 'no begin baseline; freshness unknown')
            # Preserve old crashes in place; only changed/new end-run crash text is copied.
            copy = not rel.startswith('crashes/') or (phase=='end' and baseline is not None and changed)
            target=destination/'files'/(rel+'.raw')
            if copy:
                target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(raw)
            rows.append({'source':str(p),'relative':rel,'bytes':len(raw),'mtime_ns':after.st_mtime_ns,
              'sha256':digest,'read_stable':stable,'classification':status,
              'copy':target.relative_to(DOC).as_posix() if copy else None,
              'copy_sha256':sha(target.read_bytes()) if copy else None})
            if not stable:errors.append('Changed while read; repeat after normal exit: '+rel)
        except OSError as exc: errors.append(str(p)+': '+str(exc))
    disappeared=sorted(set(expected)-{r['source'] for r in rows})
    result={'label':label,'phase':phase,'captured_utc':now,'profile':str(PROFILE),
      'begin_manifest':str(prior[-1]) if baseline else None,'files':rows,'missing_since_begin':disappeared,
      'errors':errors,'limits':['Read-only capture; no launcher/game/input/config changes',
       'No saves or memory dumps copied','Byte freshness is not proof of in-game feature success',
       'Complete collection only after game exit; unstable reads are not accepted as stable evidence']}
    payload=(json.dumps(result,ensure_ascii=False,indent=2)+'\n').replace('\n','\r\n').encode('utf-8')
    (destination/'manifest.json').write_bytes(payload)
    print(str(destination))
    print(f'{len(rows)} source files checked; {len(errors)} collection errors; '+('freshness classified against begin' if baseline else 'baseline/freshness unknown'))
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--label',required=True);p.add_argument('--phase',choices=['begin','end'],required=True)
    a=p.parse_args();result=collect(a.label,a.phase)
    raise SystemExit(1 if result['errors'] else 0)

if __name__=='__main__':main()

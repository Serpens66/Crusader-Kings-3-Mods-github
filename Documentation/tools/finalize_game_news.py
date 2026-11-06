"""Integrate/verify the dated news supplement while retaining historical evidence."""
import contextlib
import io
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from research_game_news import DOC, WORK, GAME, OUT, readj, sha, write, dump
from workspace_walk import workspace_files

ALLOWED={'README.md','research/sources.md','research/sources.json','research/coverage.md',
 'handbook/state-and-values.md','handbook/development-workflow.md','systems/subsystem-guide.md',
 'systems/religion-rites.md','systems/localization-and-gui.md','systems/crozier-gui-tools.md',
 'systems/puppets-and-selection.md','systems/crozier-migration.md',
 'tools/research_game_news.py'}

def update(rel,fn):
    p=DOC/rel;raw=p.read_bytes();t=raw.decode('utf-8-sig');new=fn(t)
    if new==t:return
    if p.read_bytes()!=raw:raise RuntimeError('Concurrent edit detected: '+rel)
    nl='\r\n' if b'\r\n' in raw else '\n';bom=b'\xef\xbb\xbf' if raw.startswith(b'\xef\xbb\xbf') else b''
    p.write_bytes(bom+new.replace('\r\n','\n').replace('\n',nl).encode('utf-8'))
def append(rel,body):update(rel,lambda s:s if body.splitlines()[0] in s else s.rstrip()+'\n\n'+body+'\n')
def integrate():
    ledger=readj(OUT/'article-coverage.json');registry=readj(DOC/'research/sources.json')
    known={x['id'] for x in registry['sources']}
    for r in ledger:
        if r['id'] not in known:
            registry['sources'].append({'id':r['id'],'title':r['title'],'original_url':r['url'],'accessed_url':r['url'],'retrieval_date':'2026-11-03','published_utc':r['published_utc'],'version_note':r['finding'],'status':r['status'],'source_body_sha256':r['source_body_sha256'],'topics':r['destination']})
    registry['game_news_20261103']={'report':'research/game-news-20261103.md','catalogue':'research/game-news-20261103/catalogue.json','coverage':'research/game-news-20261103/article-coverage.json','native_audit':'research/game-news-20261103/native-audit.json','historical_engine_exports':'1.20.0.3 retained unchanged','installed_launcher_version':'1.20.1.2','preview':'Silk & Silver / announced 1.21; not installed verification'}
    update('research/sources.json',lambda t:json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
    update('README.md',lambda t:t.replace('**Research date:** 2026-10-03. **Installed launcher version:** 1.20.0.3 (Crozier).','**Historical research baseline:** 2026-10-03, launcher version **1.20.0.3 (Crozier)**. **Latest installation check:** 2026-11-03, **1.20.1.2 (Crozier)**. Engine exports remain versioned 1.20.0.3; existing chapters are not blanket revalidated. See the [official news supplement](research/game-news-20261103.md).'))
    append('README.md','## Official news supplement — 2026-11-03\n\n[Released-news findings](systems/news-modding-2025-2026.md) integrate official 2025–2026 modding guidance with current source evidence and historical Wiki/guide limits. [Silk & Silver preview](systems/silk-and-silver-preview.md) keeps announced 1.21 trade/district/road/data-storage changes separate from installed Crozier. The [research report](research/game-news-20261103.md) and [107-article ledger](research/game-news-20261103/article-coverage.md) record sources, conflicts, incomplete articles and tests still needed.')
    append('research/sources.md','## Official news reconciliation — 2026-11-03\n\n[Report](game-news-20261103.md) covers 103 official entries from 2025–2026 plus four older targeted diaries. Stable NEWS-GID source IDs, publication/retrieval dates and full-body hashes are appended in `sources.json`; all earlier IDs and evidence remain. [Current native reads](game-news-20261103/native-audit.json) use installed 1.20.1.2, while old exports stay 1.20.0.3. [Wiki/Tiger checks](game-news-20261103/guide-checks.json) are source comparisons, not an installed validator or current syntax certification. #188 Steam text is abbreviated and its linked forum remains challenge-only; the complete article and replies remain a concrete source gap. The linked EU5 Variable Maps explanation supplies no CK3 grammar/serialization guarantee.')
    append('research/coverage.md','## Official news reconciliation — 2026-11-03\n\n| Area | Source/static coverage | Remaining boundary |\n|---|---|---|\n| 2025–2026 official entries | 103 entries plus four targeted older diaries; [per-article ledger](game-news-20261103/article-coverage.md) and exact source hashes | Feed-only articles can be abbreviated; #188 full post/replies inaccessible |\n| Installed 1.20.1.2 | Current .info/definitions/callers/helpers/localization/GUI audit; [released guide](../systems/news-modding-2025-2026.md) | Old 1.20.0.3 exports not retyped; missing primitive signatures and runtime enforcement remain open |\n| Future 1.21 / Silk & Silver | Full #9 technical chain, scope transitions, dependency and rename map; [preview](../systems/silk-and-silver-preview.md) | Released files, fresh exports and actual game/GUI/MP/audio tests needed |\n| Art/audio/performance | Production principles, current narrow sound consumer, profiler/public-internal distinction | No exporter/tool-format certification, asset render/playback or benchmark |\n\n[New static/preservation results](game-news-20261103/verification.json) are separate from old reports and their baseline drift. No existing function test is marked passed by this research.')
    append('handbook/state-and-values.md','## News update — 2026-11-03\n\nThe forthcoming [Variable Maps announcement](../systems/silk-and-silver-preview.md) describes associative data beyond variables/lists. It does not establish CK3 map syntax, supported types, ordering or lifetime. Existing ownership/cleanup rules remain until matched release files and exports are audited. [Released story-tracker guidance](../systems/news-modding-2025-2026.md) separately covers visualization and historical state ownership.')
    append('handbook/development-workflow.md','## News update — 2026-11-03\n\nUse the [official-news report](../research/game-news-20261103.md) to distinguish installed 1.20.1.2, old 1.20.0.3 dumps and announced 1.21 facilities. Preview symbols and old Wiki tables are discovery routes; neither is an engine capability test. Preserve dated baselines and write new results separately rather than relabelling old exports. Public script-profiler discussion does not expose every internal tool pictured in a diary.')
    append('systems/subsystem-guide.md','## News update — 2026-11-03\n\n[Released-news guidance](news-modding-2025-2026.md) adds Situations versus Struggles, subject-contract callback scopes, overlord/domicile ownership, story visualization, cached/filter performance and portrait/audio boundaries. The [Silk & Silver preview](silk-and-silver-preview.md) describes future districts/trade/roads and migrations; do not apply those scopes or renames to current Crozier from this announcement alone. The existing subsystem examples retain their dated evidence.')
    append('systems/religion-rites.md','## News update — 2026-11-03\n\nInstalled version is now 1.20.1.2; [the dated supplement](news-modding-2025-2026.md) documents current `history` versus `create` rite fields, `can_change_faith`, reform-faith registration and announced doctrine triggers. Old dumps cannot establish the new engine signatures; release balance/callback changes require a new feature audit before adopting older worksheet expectations. No conversion runtime blocker is cleared here.')
    append('systems/localization-and-gui.md','## News update — 2026-11-03\n\n[Released-news guidance](news-modding-2025-2026.md) connects native `GetGameConcept` contexts with the concept-tooltip template and distinguishes optional council targets and historical input bindings. [Announced GUI/data changes](silk-and-silver-preview.md) retain unresolved `GetModiferValue` spelling, new selection types and scope arguments. Do not auto-correct names or infer types from a preview. Rendering and MP tests remain open.')
    append('systems/crozier-gui-tools.md','## News update — 2026-11-03\n\nThe [news supplement](news-modding-2025-2026.md) separates native concept-tooltip/portrait-schema evidence from release-only functions, internal profiling screenshots and current export gaps. The [preview](silk-and-silver-preview.md) records upcoming road/spline and audio/visual production surfaces without running generators or installing exporters. Earlier asset/frame/render blockers remain.')
    append('systems/puppets-and-selection.md','## News update — 2026-11-03\n\nThe [released supplement](news-modding-2025-2026.md) records later interaction UI/puppet-sender/secondary-recipient fixes without promoting them to a tested routing contract. The [preview](silk-and-silver-preview.md) announces four more decision pickers and new trade callbacks; controller, root, selected object, optional target and destruction lifetime still require released definitions and tests.')
    append('systems/crozier-migration.md','## News update — 2026-11-03\n\n[Released findings](news-modding-2025-2026.md) extend the dated baseline to narrow installed 1.20.1.2 source observations; current whole-file hashes are separate from the original 1.20.0.3 exports. [Future migration](silk-and-silver-preview.md) maps announced economy/district/history/government changes by context, without editing current mods or treating preview names as current contracts.')

def verify():
    before=readj(OUT/'preservation-before.json');audit=readj(OUT/'native-audit.json');errors=[];historical=[];preexisting_docs=[];counts={}
    for rel,h in before['workspace'].items():
        p=WORK/rel
        if not p.is_file() or sha(p.read_bytes())!=h:errors.append('Original workspace changed: '+rel)
    for rel,h in before['documentation'].items():
        if rel not in ALLOWED:
            p=DOC/rel
            if not p.is_file() or sha(p.read_bytes())!=h:errors.append('Protected documentation changed: '+rel)
    for path,h in before['settings'].items():
        if sha(Path(path).read_bytes())!=h:errors.append('Profile setting changed: '+path)
    for rel,row in audit['files'].items():
        if sha((GAME/rel).read_bytes())!=row['sha256']:errors.append('Audited source changed: '+rel)
    if readj(GAME.parent/'launcher/launcher-settings.json')!=before['version']:errors.append('Installation version changed')
    counts.update(workspace_files=len(before['workspace']),protected_old_documentation=sum(r not in ALLOWED for r in before['documentation']),native_sources=len(audit['files']),profile_settings=len(before['settings']))
    ledger=readj(OUT/'article-coverage.json');catalogue=readj(OUT/'catalogue.json')
    if len(ledger)!=len(catalogue['articles']) or {r['id'] for r in ledger}!={r['id'] for r in catalogue['articles']}:errors.append('Incomplete article coverage')
    if len({r['id'] for r in ledger})!=len(ledger):errors.append('Duplicate article ID')
    registry=readj(DOC/'research/sources.json');ids=[r['id'] for r in registry['sources']]
    if len(ids)!=len(set(ids)):errors.append('Duplicate source ID')
    for r in ledger:
        if r['id'] not in ids or not (DOC/r['destination']).is_file():errors.append('Unresolved article destination: '+r['id'])
        old=next(x for x in catalogue['articles'] if x['id']==r['id'])
        if old['source_body_sha256']!=r['source_body_sha256']:errors.append('Source mismatch: '+r['id'])
    counts['articles']=len(ledger)
    counts['guide_commit_pins']=0
    for row in readj(OUT/'guide-checks.json'):
        if row.get('pinned_url'):
            counts['guide_commit_pins']+=1
            if not row.get('pinned_bytes_match') or row.get('commit') not in row['pinned_url']:errors.append('Unverified guide pin: '+row['id'])
    d188=next(r for r in ledger if r['gid']=='1814309641409052')
    if not d188['truncated_feed'] or d188['status']!='unresolved':errors.append('Truncated #188 incorrectly certified')
    # Existing verifier writes only to a new, dated result path via this adapter.
    dump('verification.json',{'status':'in progress','runtime_tests':'not run'})
    import verify_documentation as existing
    oldwrite=existing.write
    def redirected(rel,body):
        if not rel.startswith('research/verification.'):raise RuntimeError('Unexpected verifier write')
        write(OUT/('legacy-'+Path(rel).name),body)
    existing.write=redirected
    try:
        with contextlib.redirect_stdout(io.StringIO()):existing.main()
    except SystemExit:pass
    finally:existing.write=oldwrite
    legacy=readj(OUT/'legacy-verification.json')
    for issue in legacy['issues']:
        rel=issue.split(': ',1)[0].replace('\\','/')
        if rel in before['documentation'] and rel not in ALLOWED and (DOC/rel).is_file() and sha((DOC/rel).read_bytes())==before['documentation'][rel]:
            preexisting_docs.append(issue+' (unchanged from this operation baseline)');continue
        if issue.startswith(('Workspace source changed since indexed: ','Audited installation source changed: ','Changed binary fixture source: ')):historical.append(issue)
        else:errors.append(issue)
    # Validate anchors in Markdown introduced by this operation, in addition to the existing path checks.
    counts['new_fragment_links']=0
    for p in [DOC/'research/game-news-20261103.md',DOC/'systems/news-modding-2025-2026.md',DOC/'systems/silk-and-silver-preview.md',OUT/'article-coverage.md']:
        body=p.read_text(encoding='utf-8-sig')
        for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)',re.sub(r'```.*?```','',body,flags=re.S)):
            target=target.strip('<>')
            if urlsplit(target).scheme or '#' not in target:continue
            rel,fragment=target.split('#',1);dest=(p.parent/unquote(rel)).resolve() if rel else p
            counts['new_fragment_links']+=1
            headings=re.findall(r'(?m)^#+\s+(.+)',dest.read_text(encoding='utf-8-sig'))
            anchors={re.sub(r'[^\w\- ]','',h.lower().replace('`','')).replace(' ','-') for h in headings}
            if fragment and unquote(fragment) not in anchors:errors.append('Broken new anchor: '+target)
    counts['cache_excluded']=not any('.reference-cache' in p.parts for p in workspace_files(WORK))
    if not counts['cache_excluded']:errors.append('Cache excluded incorrectly')
    result={'date':'2026-11-03','status':'passed' if not errors else 'failed','checks':counts,'documentation_checks':legacy['checks'],'errors':errors,'historical_verifier_status':legacy['status'],'historical_baseline_drift':historical,'preexisting_documentation_issues':preexisting_docs,'historical_drift_note':'Preserved old hashes differ from current installation/workspace; original-operation baselines were not rewritten. Fresh preservation compares current-run originals independently.','runtime_tests':'not run','limits':['No current engine export or game launch','No compatibility, rendering, audio, MP or performance certification','Full source reads/literal discovery do not prove every engine contract','Diary #188 full forum article/developer replies inaccessible']}
    dump('verification.json',result);print(json.dumps({'status':result['status'],'checks':counts,'errors':errors,'historical_source_differences':len(historical),'preexisting_documentation_issues':preexisting_docs},indent=2))
    if errors:raise SystemExit(1)

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    import argparse
    p=argparse.ArgumentParser();p.add_argument('action',choices=['integrate','verify']);a=p.parse_args()
    {'integrate':integrate,'verify':verify}[a.action]()

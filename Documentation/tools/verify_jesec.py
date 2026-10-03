"""Verify supplement provenance/coverage and reuse existing static checks separately.

No baseline or older verification report is replaced. No network is requested.
"""
import json
import re
import sys
from jesec_supplement import load, source, blocks
from research_jesec import DOC, GAME, OUT, BASE, CACHE, REPOS, blob, digest, dump, git, tree, text, write, verify

def main():
    issues=[];counts={'repositories':0,'source_hashes':0,'source_paths':0,'wiki_pages':0,'language_name_key_checks':0}
    for name in REPOS:
        d=load(name);repo=CACHE/(name+'.git');t=tree(repo,d['commit']);counts['repositories']+=1
        if len(t)!=d['tree_entries']:issues.append('Tree count mismatch: '+name)
        if git(repo,'rev-parse','--is-bare-repository').decode().strip()!='true':issues.append('Not bare: '+name)
        if git(repo,'remote','get-url','origin').decode().strip()!=d['origin']:issues.append('Wrong origin: '+name)
        for p,x in d['relevant_files'].items():
            counts['source_paths']+=1
            if t.get(p)!= {k:x[k] for k in ['mode','blob']}:issues.append('Source path/blob mismatch: '+name+'/'+p)
            if x.get('sha256'):
                counts['source_hashes']+=1
                if digest(blob(repo,x['blob']))!=x['sha256']:issues.append('Source hash mismatch: '+name+'/'+p)
        if name!=REPOS[0]:
            lock=json.loads((DOC/'reference/vanilla-history-lock.json').read_text(encoding='utf-8'))
            bt=tree(BASE,lock['versions']['1.19.0.6']['commit'],'base/game')
            delta={p for p,x in t.items() if p.startswith('base/game/') and (p not in bt or x['blob']!=bt[p]['blob'])}
            if delta!={x['path'] for x in d['current_mod_game_patches']}:issues.append('Incomplete delta: '+name)
            if [p for p in bt if p not in t]!=d['deleted_vs_11906']:issues.append('Incomplete deletions: '+name)
    ledger=json.loads((OUT/'wiki-page-coverage.json').read_text(encoding='utf-8'));wiki=load(REPOS[0])
    pages={p for p in wiki['relevant_files'] if p.startswith('wiki_pages/')}
    if len(ledger)!=len(pages) or {x['page'] for x in ledger}!=pages:issues.append('Wiki reconciliation incomplete')
    counts['wiki_pages']=len(ledger)
    feature=json.loads((OUT/'feature-audit.json').read_text(encoding='utf-8'))
    counts['historical_gui_hashes']=0
    for row in feature['historic_gui_reads']:
        raw=git(CACHE/(row['repository']+'.git'),'show',row['commit']+':'+row['path'])
        counts['historical_gui_hashes']+=1
        if digest(raw)!=row['sha256']:issues.append('Historical GUI evidence mismatch: '+row['commit'])
    counts['historical_origin_changes']=0
    for row in feature['historical_origin_changes']:
        paths=git(CACHE/(row['repository']+'.git'),'diff','--name-only',row['commit']+'^',row['commit'],'--','base/game','mod').decode().splitlines()
        counts['historical_origin_changes']+=1
        if paths!=row['changed_paths']:issues.append('Historical origin mismatch: '+row['repository'])
    registry=json.loads((DOC/'research/sources.json').read_text(encoding='utf-8'));ids=[x['id'] for x in registry['sources']]
    if len(ids)!=len(set(ids)):issues.append('Duplicate source IDs')
    for row in ledger:
        if row['source_id'] not in ids or not (DOC/row['destination']).is_file():issues.append('Unresolved ledger row: '+row['page'])
        if row['sha256']!=wiki['relevant_files'][row['page']]['sha256']:issues.append('Unpinned page: '+row['page'])
    checks=json.loads((OUT/'more-legacies-checks.json').read_text(encoding='utf-8'))
    if checks['tracks']!=10 or checks['perks']!=50 or len(checks['localizations'])!=9:issues.append('Incomplete More content')
    for p,missing in checks['localizations'].items():
        counts['language_name_key_checks']+=checks['name_keys_required']
        if missing:issues.append('Missing names in '+p)
    # Confirm that all retained fields really are unchanged, rather than relying on README prose.
    less=load(REPOS[2]);lock=json.loads((DOC/'reference/vanilla-history-lock.json').read_text(encoding='utf-8'))
    def drop_gate(t):
        ts=[m for m in __import__('build_local_reference').TOKEN.finditer(t) if not m.group().startswith('#')]
        remove=set()
        for i,m in enumerate(ts):
            if m.group()=='can_be_picked' and i+2<len(ts) and ts[i+2].group()=='{':
                depth=0
                for j in range(i+2,len(ts)):
                    if ts[j].group()=='{':depth+=1
                    if ts[j].group()=='}':depth-=1
                    if depth==0:
                        remove.update(range(i,j+1));break
        return [m.group() for i,m in enumerate(ts) if i not in remove]
    counts['perk_override_files_checked']=0
    for row in less['current_mod_game_patches']:
        p=row['path']
        if '/dynasty_perks/' in p:
            native=text(git(BASE,'show',lock['versions']['1.19.0.6']['commit']+':'+p))
            if drop_gate(native)!=drop_gate(source(REPOS[2],p)):issues.append('Non-pick payload changed: '+p)
            counts['perk_override_files_checked']+=1
    # Reports are linked by the chapters: create truthful pending/preservation receipts
    # before link checks, then replace only this operation's pending receipt with results.
    dump('integration-verification.json',{'status':'in progress','runtime_tests':'not run'})
    verify()
    # Old verifier has no output-path option. Redirect only its result writes, preserving old reports.
    import verify_documentation as old
    original_write=old.write
    def redirected(rel,body):
        if rel.startswith('research/verification.'):
            write(OUT/('documentation-'+rel.split('/')[-1]),body)
        else:raise RuntimeError('Unexpected verifier mutation: '+rel)
    old.write=redirected
    try:old.main()
    except SystemExit:pass
    finally:old.write=original_write
    structural=json.loads((OUT/'documentation-verification.json').read_text(encoding='utf-8'))
    historical=[]
    before=json.loads((OUT/'preservation-before.json').read_text(encoding='utf-8'))
    for issue in structural['issues']:
        prefix='Workspace source changed since indexed: '
        if issue.startswith(prefix):
            p=issue[len(prefix):]
            if p in before['original_workspace'] and digest((DOC.parent/p).read_bytes())==before['original_workspace'][p]:
                historical.append(issue+' (already present at this operation baseline; retained)');continue
        issues.append(issue)
    result={'date':'2026-10-03','status':'passed' if not issues else 'failed','checks':counts,'existing_verifier_checks':structural['checks'],'issues':issues,'preexisting_index_differences':historical,'source_inventory':'evidence.json; individual inventory files include subsequent license reads','feature_audit':'feature-audit.json','preservation':'preservation-after.json','runtime_tests':'not run; existing user-run exports are a different evidence class','limits':['No pixel, GUI, performance, startup, gameplay, save/load, DLC or multiplayer test','Lexical discovery is not full semantic approval of every native caller','No Tiger installation/run or automatic descriptor compatibility update']}
    dump('integration-verification.json',result)
    print(json.dumps(result,indent=2))
    if issues:raise SystemExit(1)

if __name__=='__main__':main()

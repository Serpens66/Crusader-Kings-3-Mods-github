"""Reconcile news discovery with authored chapter findings; never rewrite old evidence."""
import collections
import json
from pathlib import Path
import re
import sys
from research_game_news import DOC, OUT, API, readj, dump, write, sha, clean, fetch

NOTES={
 '1847920302251844':('announced','Complete #9: trade/goods/categories/needs/tolls/hooks; district/building scopes/history; roads/splines; parameter, AI, region, betrothal, situation, aspiration and confederation changes; new pickers; economy renames; scoped API arguments, modifier queries and Variable Maps. Art/audio production separated from contracts.','systems/silk-and-silver-preview.md'),
 '1847286114048834':('announced','Trade-in-practice explains market, route, category, ownership and prices. Later technical #9 refines earlier vision; numerical balance is provisional.','systems/silk-and-silver-preview.md'),
 '1847286114028159':('historical/superseded','Installed-version hotfix release: multilingual UI/portrait crashes, holy-site/DLC and adventurer inheritance fixes. No blanket mod compatibility adopted from release prose.','systems/news-modding-2025-2026.md'),
 '1846018067943835':('newly source-confirmed','Current .info/rule/GUI findings distinguished from new engine-only doctrine triggers. Study-Rite balance and conversion gates can affect old conversion tests; no mod is changed here.','systems/news-modding-2025-2026.md'),
 '1845383656396296':('historical/superseded','Secondary-recipient artifact-interaction bug fixed in 1.20.0.4. Retain regression scenario for education/interaction state; do not blame all such failures on mods.','systems/news-modding-2025-2026.md'),
 '1845383656381625':('already covered','Existing Crozier release/hotfix research retained; no redefinition of original export evidence.','systems/crozier-migration.md'),
 '1845383656377574':('already covered','Crozier release refines prerelease religion/rites, events/history overrides, UI, filters and diagnostics. Existing C120 coverage retained.','systems/crozier-migration.md'),
 '1844751498234002':('already covered','By God Alone #8 supports existing religion/puppet/dynamic-selection/UGCx coverage. Version-specific advertised limitations require later .1 comparison.','systems/puppets-and-selection.md'),
 '1844115010504011':('already covered','By God Alone #7: design context for religion/rite gameplay; actual definitions and later release take precedence.','systems/religion-rites.md'),
 '1842846814455418':('already covered','Performance #6: measure bottlenecks; developer mesh-streaming/debug tools may be internal-only. No public profiler command or universal speed gain inferred.','systems/news-modding-2025-2026.md'),
 '1827626365765598':('newly source-confirmed','Realm Maintenance II: modular visible story tracker, typed variables and visualization; current complete story schema/callers audited. Also religion, UI and modding changes refined by final Scribe release.','systems/news-modding-2025-2026.md'),
 '1826992588603740':('already covered','Realm Maintenance I: ledger/shortcuts/UI workflow context; UI aspirations and early balance are not frozen APIs.','systems/crozier-gui-tools.md'),
 '1824644522847508':('historical/superseded','Spring Cleaning introduces planned work and community fixes; maintenance articles, beta and final 1.19 supersede preview specifics.','systems/news-modding-2025-2026.md'),
 '1830163047265930':('already covered','Final Scribe lists filters/active dynasties, doctrine databases, regnal names, scope arguments, UI functions, skills, building DLC overrides and shortcuts. Current references outrank beta.','systems/news-modding-2025-2026.md'),
 '1828441623104237':('historical/superseded','Scribe beta: compare with final 1.19 and Crozier; no beta save/MP/QA claim promoted to current truth.','systems/news-modding-2025-2026.md'),
 '1828894815555147':('historical/superseded','Beta update refines initial preview; final Scribe release is later evidence.','systems/news-modding-2025-2026.md'),
 '1814309641409052':('unresolved','Steam explicitly truncates #188 and delegates full diary to official forum. Forum is challenge-only (HTTP 200 is not article success); full modding/art/audio section and developer replies remain inaccessible. Later releases/current schemas are independent partial substitutes.','systems/news-modding-2025-2026.md'),
 '1814309641472412':('historical/superseded','All Under Heaven release/changelog reference; use full available later patch lists and installed schemas for exact contracts.','systems/news-modding-2025-2026.md'),
 '1814309641613059':('already covered','Crane release context; distinguishes game content availability from engine primitives; later patches correct implementation.','systems/news-modding-2025-2026.md'),
 '1813674388903190':('newly source-confirmed','Performance/optimization: candidate reduction, fast trigger composition/list filters, cached income, staggered update cadence and profiler availability. Current info examples supply reader-specific contracts; no benchmark promises.','systems/news-modding-2025-2026.md'),
 '1818752592123762':('newly source-confirmed','1.18.2: portrait inherit_scale, council swap/replacement scopes, modifier-key input bindings, Great Project dynamic name/founder/contribution support and larger internal capacity. Source claims not fully typed runtime contracts.','systems/news-modding-2025-2026.md'),
 '1816215235351596':('newly source-confirmed','1.18.1: cached income, blocked subject courts, realm-law group, activity-intent target, portrait skip_if_overridden, government regnal-number setting, adjacency debug and contribution filters.','systems/news-modding-2025-2026.md'),
 '1795917897484448':('newly source-confirmed','Code of Khans: contracts/tributaries, overlord distinctions, obedience, confederations, dynamic situations/participants/phases, migration code boundary, title-owned domiciles, fertility and herd. Screenshot-only exact formulas/commands not reconstructed.','systems/news-modding-2025-2026.md'),
 '1797185861798447':('historical/superseded','Preliminary Chamfron changelog; final 1.16 release confirms/refines exposed modding surfaces.','systems/news-modding-2025-2026.md'),
 '1797820624589961':('newly source-confirmed','Final Chamfron modding: subject contracts/overlord/tributary iterators, hooks, domicile ownership, combat controls, dynamic situations and graphical states. Individual primitive permissions remain feature-specific.','systems/news-modding-2025-2026.md'),
 '1794102528236189':('historical/superseded','Tributary/confederation vision refined by #168 and release; new Silk & Silver confederation_base is a later announced migration, not Crozier syntax.','systems/news-modding-2025-2026.md'),
 '1794830911033056':('historical/superseded','Nomadic/migration vision; #168 states code-controlled versus script-controlled boundaries.','systems/news-modding-2025-2026.md'),
 '1793384379533855':('historical/superseded','Realm maintenance preview; later release/hotfix source and current .info needed before adopting old fixes or UI behavior.','systems/news-modding-2025-2026.md'),
 '1791580426129541':('historical/superseded','Creator art/building workflow context; copying licensed artwork or old building definitions is not authorized by a diary.','systems/news-modding-2025-2026.md'),
 '6242640076614766488':('historical/superseded','Targeted 2024 #156: adventurer/domicile, government/lifestyle and scope context; #168 title ownership supersedes character-owned assumptions.','systems/news-modding-2025-2026.md'),
 '5133583642669227612':('already covered','Targeted #126 activity structure, locales/phases/callbacks; current activity .info and complete native recipe remain required.','systems/subsystem-guide.md'),
 '4237325463689546957':('historical/superseded','Targeted #87 royal-court/artifact/culture/GUI guidance; current native assets, court schemas and later C120 fields take precedence.','systems/subsystem-guide.md'),
 '4117954073016890542':('historical/superseded','Targeted #55 early script/tooling/UI improvements; historical background, not a current command table.','handbook/development-workflow.md')}

def main():
    cat=readj(OUT/'catalogue.json');current={x['gid']:x for x in fetch()};ledger=[]
    for row in cat['articles']:
        gid=row['gid'];x=current[gid];body=clean(x['contents'])
        if sha(x['contents'].encode('utf-8'))!=row['source_body_sha256']:raise RuntimeError('Source changed during research: '+gid)
        if gid in NOTES:status,note,destination=NOTES[gid]
        elif 'Silk' in row['title']:
            status='announced';note='Earlier vision/design context, refined by technical #8/#9; no present-installation API or balance guarantee.';destination='systems/silk-and-silver-preview.md'
        elif 'By God Alone' in row['title']:
            status='already covered';note='Religion/rite/church gameplay context mapped to existing Crozier chapters; nontechnical narrative is not a new script contract.';destination='systems/religion-rites.md'
        elif re.search('Update|Changelog|Available Now|Now Available|Post-Release',row['title'],re.I):
            status='historical/superseded';note='Release/fix context; literal technical candidates retained below with exact source. Unreviewed primitive semantics remain unresolved: inspect current declaration and complete caller/dependencies before use.';destination='systems/news-modding-2025-2026.md'
        elif re.search('Diary|Realm Maintenance',row['title'],re.I):
            status='already covered';note='Subsystem/design/production orientation; technical discoveries retained as source-only candidates, not functional templates. Feature-specific current audit still required.';destination='systems/subsystem-guide.md'
        else:
            status='excluded';note='Commercial/community/release-calendar or production news with no adopted script contract; any lexical hits remain discovery candidates only.';destination='research/game-news-20261103.md'
        # Store identifiers, headings and source locations, not the original article's prose or scripts.
        tokens=set()
        for frag in re.findall(r'\[c\](.*?)\[/c\]|`([^`]+)`',body,flags=re.S):
            tokens.update(re.findall(r'\b[A-Za-z][A-Za-z_0-9]*_[A-Za-z_0-9]+\b',' '.join(frag)))
        tokens.update(re.findall(r'\b[A-Za-z][A-Za-z_0-9]*\.[A-Za-z_][A-Za-z_0-9]+\b',body))
        tokens={t for t in tokens if not re.search(r'\.(?:png|jpg|com|dds|mp4|gif|net|html|sav)$',t)}
        headings=[re.sub(r'\[/?[^]]+\]','',z).strip() for z in re.findall(r'\[h[1-6]\](.*?)\[/h[1-6]\]',x['contents'],flags=re.S)]
        ledger.append({**row,'status':status,'finding':note,'destination':destination,'headings':headings,'technical_identifiers':sorted(tokens),'identifier_status':'announced/unverified for preview; otherwise source-only until individually audited in linked chapter','truncated_feed':bool(re.search('exceeds the character limit|read the full dev diary',body,re.I))})
    dump('article-coverage.json',ledger)
    lines=['# Article-by-article news coverage','','Period: 2025-01-01 through 2026-11-03, plus four targeted older diaries. Full official feed bodies were read/scanned. A complete feed body can itself be an abbreviated post: the `truncated_feed` field is retained. Article-level status is separate from the confidence of each technical identifier. See [main report](../game-news-20261103.md).','','| Date | Article / stable source ID | Treatment | Integration and limit |','|---|---|---|---|']
    for r in ledger:
        lines.append('| '+r['published_utc'][:10]+' | ['+r['title'].replace('|','/')+']('+r['url']+') / `'+r['id']+'` | '+r['status']+' | '+r['finding']+' [Read](../../'+r['destination']+'). |')
    lines+=['','## Source-only discovery identifiers','','These identifiers are searchable research leads, not an API index. Each object in [article-coverage.json](article-coverage.json) retains source ID, source hash, headings, keyword line spans, identifiers and destination. A list entry alone does not supply supported scopes, parameter types, permissions or runtime behavior.','']
    write(OUT/'article-coverage.md','\n'.join(lines))
    print('Reconciled',len(ledger),'articles:',dict(collections.Counter(r['status'] for r in ledger)))

if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8');main()

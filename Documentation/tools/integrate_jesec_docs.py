"""Add the authored source/page map without rebuilding older evidence or indexes."""
import json
import re
from pathlib import Path
from jesec_supplement import DOC, OUT, REPOS, load, source, url
from research_jesec import digest, dump, write

MAPPING={
 '3D_models':'systems/subsystem-guide.md','AI_modding':'reference/wiki-extensions.md',
 'Artifact_modding':'systems/subsystem-guide.md','Bookmarks_modding':'systems/subsystem-guide.md',
 'Characters_modding':'systems/subsystem-guide.md','Coat_of_arms_modding':'systems/subsystem-guide.md',
 'Commands':'reference/engine-reference.md','Console_commands':'handbook/development-workflow.md',
 'Council_modding':'reference/wiki-extensions.md','Culture_modding':'systems/subsystem-guide.md',
 'Customizable_localization':'systems/localization-and-gui.md','Data_types':'reference/engine-reference.md',
 'Decisions_modding':'systems/events-decisions-on-actions.md','Defines':'systems/traits-modifiers-defines.md',
 'Dynasties_modding':'systems/dynasty-legacies.md','Effects':'handbook/control-flow.md',
 'Effects_list':'reference/engine-reference.md','Event_modding':'systems/events-decisions-on-actions.md',
 'Exporters':'reference/wiki-extensions.md','Flavorization':'reference/wiki-extensions.md',
 'Fonts':'reference/wiki-extensions.md','Governments_modding':'systems/crozier-migration.md',
 'Graphical_assets':'reference/wiki-extensions.md','History_modding':'reference/wiki-extensions.md',
 'Holdings_modding':'reference/wiki-extensions.md','Interactions_modding':'systems/interactions.md',
 'Interface':'systems/localization-and-gui.md','Lifestyles_modding':'systems/subsystem-guide.md',
 'List_of_baronies':'reference/wiki-extensions.md','Lists':'handbook/control-flow.md',
 'Localization':'systems/localization-and-gui.md','Map_modding':'systems/subsystem-guide.md',
 'Mod_compatibility':'handbook/development-workflow.md','Mod_structure':'handbook/development-workflow.md',
 'Mod_troubleshooting':'handbook/development-workflow.md','Modding':'README.md',
 'Modding_tools':'handbook/development-workflow.md','Modifier_list':'reference/engine-reference.md',
 'Music_modding':'systems/subsystem-guide.md','Regiments_modding':'systems/subsystem-guide.md',
 'Religions_modding':'systems/religion-rites.md','Resources_modding':'reference/wiki-extensions.md',
 'Scopes':'handbook/scopes.md','Scopes_list':'reference/engine-reference.md',
 'Script_values':'handbook/state-and-values.md','Scripted_effects':'handbook/control-flow.md',
 'Scripting':'handbook/script-language.md','Sound_modding':'systems/subsystem-guide.md',
 'Story_cycles_modding':'reference/wiki-extensions.md','Struggle_modding':'reference/wiki-extensions.md',
 'Terrain_modding':'reference/wiki-extensions.md','Title_modding':'systems/subsystem-guide.md',
 'Trait_modding':'systems/traits-modifiers-defines.md','Triggers':'handbook/control-flow.md',
 'Triggers_list':'reference/engine-reference.md','Variables':'handbook/state-and-values.md',
 'Weight_modifier':'handbook/control-flow.md'}

NOTES={
 'AI_modding':'New AI reader/personality/conqueror research pointers; hardcoded-army claim not certified for Crozier.',
 'Council_modding':'New position/task distinction; historical missing-task crash/new-game claim retained as a test gate.',
 'Commands':'Historical 1.0 list; current effect declarations replace API table. Console commands kept separate.',
 'Exporters':'New historical Maya/Photoshop pipeline map; tool/version/deployment availability unresolved; nothing installed.',
 'Flavorization':'New eligibility/priority/custom localization orientation; current priority/consumer audit required.',
 'Fonts':'New format/asset/license review path; rename-as-conversion shortcut not adopted or tested.',
 'Governments_modding':'Short pointer already surpassed by Crozier mechanic schema; no complete modern contract in Wiki.',
 'Graphical_assets':'New palette-specific formats separated from GUI frames/icons; no pixel/render audit.',
 'History_modding':'New consolidated date/holder/liege/bookmark orientation; exact merge behavior needs feature audit.',
 'Holdings_modding':'New generated holding modifier orientation; repeated game/game paths and DDS concept path unreliable.',
 'List_of_baronies':'Historical ID catalogue; current title/history/province sources remain authoritative.',
 'Resources_modding':'New piety value/helper/cost distinction; exact current payment contracts already more detailed.',
 'Story_cycles_modding':'New state/recurring-cycle guide plus current .info hooks; owner lifetime and exactly-once tests pending.',
 'Struggle_modding':'New phase/catalyst/parameter-consumer map; three/four-category inconsistency; placeholder example incomplete.',
 'Terrain_modding':'New terrain/travel/fertility/initialization orientation; no independent map feature/audit/render test.',
 'Dynasties_modding':'Existing dynasty/house creation orientation; newly separate full legacy/perk reference.',
 'Religions_modding':'Historical nested faith examples; current separate faith/rite schema takes precedence.',
 'Trait_modding':'Already covered; obsolete numeric-index allocation not a current recipe.',
 'Weight_modifier':'Existing MTTH versus Script Value distinction reinforced; literal macro substitution remains contextual.',
 'Data_types':'Historical function/type table; current exports preserve duplicate/unregistered contexts and unknown types.'}

CHANGES={}
def edit(rel,transform):
    p=DOC/rel;raw=p.read_bytes();t=raw.decode('utf-8-sig');new=transform(t)
    if new==t:return
    # Recheck just before mutation; preserve the actual BOM and newline convention.
    if p.read_bytes()!=raw:raise RuntimeError('Concurrent edit: '+rel)
    nl='\r\n' if b'\r\n' in raw else '\n'
    data=new.replace('\r\n','\n').replace('\n',nl).encode('utf-8')
    if raw.startswith(b'\xef\xbb\xbf'):data=b'\xef\xbb\xbf'+data
    p.write_bytes(data);CHANGES[rel]={'before':digest(raw),'after':digest(data)}
def append(rel,body):
    edit(rel,lambda t:t if body.splitlines()[0] in t else t.rstrip()+'\n\n'+body+'\n')

def main():
    d=load(REPOS[0]);pages={Path(p).stem:p for p in d['relevant_files'] if p.startswith('wiki_pages/')}
    if pages.keys()!=MAPPING.keys():raise RuntimeError('Page mapping incomplete: '+str(pages.keys()^MAPPING.keys()))
    p=DOC/'research/sources.json';raw=p.read_bytes();registry=json.loads(raw.decode('utf-8-sig'))
    existing={Path(x.get('accessed_url','')).stem:x['id'] for x in registry['sources'] if x['id'].startswith('W')}
    nextid=max(int(x['id'][1:]) for x in registry['sources'] if re.fullmatch(r'W\d+',x['id']))+1
    ledger=[];lines=['# Complete Wiki page reconciliation','','Pinned mirror: `'+d['commit']+'`; retrieved 2026-10-03. **57/57 subject pages** were read and classified. See [supplement](../reference/wiki-extensions.md) and [repository report](jesec-repositories.md). Original Wiki revision IDs were not independently certified. The archive is not a 1.20 API dump.','','Status vocabulary: **already covered** = current handbook destination exists, without blanket source revalidation; **new orientation** = archived guidance newly summarized; **historical** = outdated table/schema retained only as navigation; **new contract guide** = current native schema/source finding, with runtime limits.','','| Page / source ID | Page version label | Status / contribution and limits | Destination |','|---|---|---|---|']
    for name,path in sorted(pages.items()):
        t=source(REPOS[0],path);version=re.search(r'Last verified for version\s+([^\n\r]+)',t)
        label=version.group(1).strip('*> ') if version else 'Archive says timeless; not certified' if 'article is timeless' in t else 'No exact current-installation label'
        id=existing.get(name)
        if id is None:
            id='W'+str(nextid).zfill(2);nextid+=1
            registry['sources'].append({'id':id,'title':name.replace('_',' '),'original_url':'https://ck3.paradoxwikis.com/'+name,'accessed_url':url(REPOS[0],path),'retrieval_date':'2026-10-03','status':'pinned mirror read; historical orientation','version_note':label,'topics':NOTES.get(name,'See complete page ledger; feature-specific current audit remains necessary.')})
        status='new orientation' if MAPPING[name]=='reference/wiki-extensions.md' else 'historical' if name in {'Commands','Data_types','Effects_list','Triggers_list','Modifier_list','Scopes_list','Religions_modding'} else 'new contract guide' if name=='Dynasties_modding' else 'already covered'
        note=NOTES.get(name,'Topic already mapped in the handbook; no new blanket engine/runtime claim. Validate the exact feature against current native sources.')
        row={'page':path,'source_id':id,'commit':d['commit'],'sha256':d['relevant_files'][path]['sha256'],'headings':[s for s in t.splitlines() if s.startswith('#')],'version_label':label,'status':status,'contribution':note,'destination':MAPPING[name]};ledger.append(row)
        lines.append('| ['+name.replace('_',' ')+']('+url(REPOS[0],path)+') / '+id+' | '+label.replace('|','/')+' | **'+status+'**: '+note+' | ['+MAPPING[name]+'](../'+MAPPING[name]+') |')
    lines+=['','All archive images and other binary assets were inventoried as repository tree metadata only, not imported. Historical syntax examples and tables are not distributed wholesale. Original URLs are retained in the sources registry; each row above pins the mirror file. The `.info`/engine-derived supplements are distinguished from page orientation.','']
    write(DOC/'research/jesec-wiki-coverage.md','\n'.join(lines));dump('wiki-page-coverage.json',ledger)
    for x in registry['sources']:
        if x['id']=='A03':
            x.update(accessed_url=url(REPOS[0],'LICENSE'),retrieval_date='2026-10-03',version_note='Pinned LICENSE: Wiki articles CC BY-SA 3.0 Unported; individual images and Paradox game content separate. Earlier MIT attribution corrected.',status='pinned LICENSE read')
    for i,name in enumerate(REPOS,1):
        id='J'+str(i).zfill(2)
        if not any(x['id']==id for x in registry['sources']):registry['sources'].append({'id':id,'title':name,'original_url':'https://github.com/jesec/'+name,'accessed_url':'https://github.com/jesec/'+name+'/tree/'+load(name)['commit'],'commit':load(name)['commit'],'retrieval_date':'2026-10-03','status':'bare clone; full relevant source investigation','version_note':'Pinned archive' if i==1 else 'Descriptor 1.19.*; source delta compared with locked 1.19.0.6; current audit 1.20.0.3','topics':'See research/jesec-repositories.md; detailed source/coverage inventories'})
    registry['jesec_supplement']={'report':'research/jesec-repositories.md','evidence':'research/jesec/evidence.json','feature_audit':'research/jesec/feature-audit.json','wiki_pages':'research/jesec/wiki-page-coverage.json','base_lock_preserved':True,'runtime_tests':'not run'}
    edit('research/sources.json',lambda t:json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
    edit('research/sources.md',lambda t:t.replace('Repository declares MIT; underlying Wiki content rights not automatically settled','Pinned LICENSE declares Wiki articles CC BY-SA 3.0; individual images and game content have separate rights (earlier MIT attribution corrected)').replace('https://github.com/jesec/ck3-modding-wiki/blob/master/LICENSE',url(REPOS[0],'LICENSE')))
    append('research/sources.md','## Additional jesec sources — 2026-10-03\n\nJ01–J04 pin the Wiki, More, Less Restrictive and Scrollable repositories in the [source report](jesec-repositories.md). W01–W41 are preserved; newly discovered Wiki pages receive additional W IDs in [the complete ledger](jesec-wiki-coverage.md) and `sources.json`. A03 is corrected from the pinned Wiki license; the separate Base tooling/game notices are unchanged. All four repositories have independent inventories, source dates and license qualifications. No new runtime compatibility result is implied.')
    append('README.md','## Additional jesec research — 2026-10-03\n\nRead [Dynasty legacy contracts](systems/dynasty-legacies.md) for current track/perk scopes, all additional content, relaxed eligibility and the historical/current GUI distinction. The [repository report](research/jesec-repositories.md), [57-page Wiki ledger](research/jesec-wiki-coverage.md) and [additional Wiki guidance](reference/wiki-extensions.md) integrate with the existing Vanilla-history lock and Crozier chapters. Source pins and new static reports are kept separately; existing gameplay/GUI/MP blockers remain.')
    append('research/coverage.md','## Additional jesec repository coverage — 2026-10-03\n\n| Topic | Research and native/source audit | Static example/reference | Remaining gate |\n|---|---|---|---|\n| Wiki archive | 57/57 subject pages mapped; version/license conflicts recorded | [Page ledger](jesec-wiki-coverage.md), existing chapters and new guide | Historical orientation is not complete current validation for map/model/font/audio/council/struggle features |\n| More Legacies | All ten tracks/fifty perks, languages and asset metadata; complete relevant current native schema/callers/helpers | [Source map](jesec/more-legacies-map.md), original untested sketch | AI policy, generated modifier DLC/units, actual unlock and member application, visual render, MP |\n| Less Restrictive | All twelve full-file patches against exact historical baseline; original patch history and current gates | [Legacy contract](../systems/dynasty-legacies.md) | Benefits outside native government, current override merge, purchase/runtime tests |\n| Scrollable | Original GUI and removal/native snapshots; current zero game delta | Container/data-binding explanation, current native windows | Exact initial release attribution; rendered scaling/performance/save safety remain untested |\n| Base integration | Existing locked reference reused, checkout and reports preserved | Existing history/lookup CLI | Historical sources do not override installed contracts |\n\nSee [new verification](jesec/integration-verification.json). Existing 43 function sheets and runtime blockers are unchanged; this supplement adds research evidence, not successful game tests.')
    append('handbook/state-and-values.md','## Legacy AI and story ownership supplement\n\n[Dynasty legacies](../systems/dynasty-legacies.md) demonstrates a numeric `ai_chance` reader, named phase-duration values and an explicitly enumerated native AI policy. Its weight is not a percentage. [Story guidance](../reference/wiki-extensions.md) distinguishes a story root, owner-death hook and cleanup from automatic cross-generation persistence or exactly-once execution. Both retain pending runtime tests.')
    append('handbook/control-flow.md','## Complete Wiki and legacy reader supplement\n\nThe [57-page reconciliation](../research/jesec-wiki-coverage.md) reinforces historical weight macros versus numeric formulas. [Legacy contracts](../systems/dynasty-legacies.md) show separate visibility and pick triggers, dynasty/dynast scope transitions and initialization-phase restrictions. A scripted helper legal in a perk AI formula is not automatically legal while parsing a track visibility definition.')
    append('systems/localization-and-gui.md','## Legacy containers and historical overrides\n\nThe [legacy GUI audit](dynasty-legacies.md) traces `DynastyHouseView.GetLegacies`, item contexts, framed progress and separate `GetIcon`/`GetTrackIcon` consumers. The historical Scrollable replacement is superseded in the examined native snapshots; do not transplant its full window into Crozier. Twenty custom asset object IDs and nine localization key sets are inventoried, without claiming rendering or path-resolution success.')
    append('systems/subsystem-guide.md','## Complete archived-topic reconciliation\n\nThe [Wiki supplement](../reference/wiki-extensions.md) adds council/task, history, government, holding, flavorization, story, terrain/struggle and art/font/exporter research routes, with historical version and current-audit limits. [Dynasty legacies](dynasty-legacies.md) supplies the focused current schema, complete third-party source map and concrete pending tests. No independent map/audio feature was introduced.')
    append('systems/crozier-migration.md','## Legacy overrides and added native branches\n\nThe [legacy comparison](dynasty-legacies.md) adds concrete 1.19.0.6→1.20.0.3 consequences: PAM track/perks, surrounding-character Iberian struggle branches, administrative-mechanic checks, `faith_character_modifier`, rite-cost and herald-trait changes. Historical Less Restrictive full files must preserve these current native branches in any future port. This source finding does not update an existing mod or close its runtime acceptance gates.')
    append('systems/crozier-gui-tools.md','## Legacy-window source supplement\n\n[Scrollable Legacies history](dynasty-legacies.md) documents a content scrollbox while retaining grid/item data bindings and native tooltip/progress consumers. Current native house and legacy windows already contain relevant scroll layouts. Their exported functions include unregistered result types; container presence does not prove frame correctness, unlimited item performance or compatibility with an entire historical replacement window.')
    dump('authored-changes.json',CHANGES)
    print('Wiki pages:',len(ledger),'new registry IDs:',nextid-42,'shared files updated:',len(CHANGES))

if __name__=='__main__':main()

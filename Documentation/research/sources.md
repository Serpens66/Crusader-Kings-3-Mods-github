# Sources, provenance and access notes

Research date: **2026-10-03**. Original prose is written for this workspace; sources are references, not wholesale copies.

## Source priority

Use current generated engine documentation for a function contract, current installed developer `.info` plus actual definitions/callers for subsystem behavior, then developer explanations and version-labelled community material. An observed call is evidence of usage, not a complete API specification. Resolve disagreement per feature and retain unresolved gaps.

The original Wiki was unavailable through direct fetching. The mirror provides an access fallback; its README claims daily synchronization, but exact upstream Wiki revisions were not independently certified. Reachability/consultation does not mean every page was semantically revalidated for 1.20.0.3.

## Internet references

| ID | Source | Topics | Version/qualification |
|---|---|---|---|
| W01 | [Modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Modding.md) | Overall mod workflow, load/override guidance and tools | Mixed historical statements; conflicts recorded |
| W02 | [Mod structure](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Mod_structure.md) | Descriptors and directory layout | Page says last verified 1.1 |
| W03 | [Scripting](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Scripting.md) | Language overview and context terminology | No current-installation certification |
| W04 | [Scopes](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Scopes.md) | Scope types, chaining and named targets | Page says last verified 1.1 |
| W05 | [Triggers](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Triggers.md) | Conditional and reusable predicates | No current-installation certification |
| W06 | [Effects](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Effects.md) | Effect contexts, control and helper forms | No current-installation certification |
| W07 | [Variables](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Variables.md) | Storage ownership and variable operations | No current-installation certification |
| W08 | [Lists](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Lists.md) | Engine/scripted/custom list forms | Contains an explicitly historical 1.4.4 caveat |
| W09 | [Script values](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Script_values.md) | Numeric formulas, inlining and GUI use | Cross-checked with local .info |
| W10 | [Weight modifier](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Weight_modifier.md) | Weight syntax and scripted weight helpers | Not the numeric formula reader |
| W11 | [Scripted effects](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Scripted_effects.md) | Reusable effect entry points | Short orientation |
| W12 | [Event modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Event_modding.md) | Events, delivery and presentation | Cross-check against current event .info |
| W13 | [Decisions modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Decisions_modding.md) | Decision fields, widgets and text | Cross-check against current decision .info |
| W14 | [Interactions modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Interactions_modding.md) | Actor/recipient and outcome orientation | Short page points to native .info |
| W15 | [Localization](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Localization.md) | Language files, formatting and data calls | Page says last verified 1.4 |
| W16 | [Interface](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Interface.md) | GUI, data context and scripted GUI bridge | Current signatures require dump/native caller |
| W17 | [Modifier list](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Modifier_list.md) | Modifier types and properties | Table is not a full current engine dump |
| W18 | [Defines](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Defines.md) | Engine-exposed constants | Use actual local defaults and comments |
| W19 | [Mod compatibility](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Mod_compatibility.md) | Footprint and interoperability | General design guidance |
| W20 | [Mod troubleshooting](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Mod_troubleshooting.md) | Logs and debugging | Not proof of current launcher bugs |
| W21 | [Modding tools](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Modding_tools.md) | Tool discovery | Verify each tool separately |
| W22 | [Trait modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Trait_modding.md) | Trait schema and assets | Page says last verified 1.0; track guide needed |
| W23 | [Culture modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Culture_modding.md) | Culture definition orientation | Local pillars/traditions govern current schema |
| W24 | [Religions modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Religions_modding.md) | Historical religion and faith structures | Page says last verified 1.0; contradicted by local type/rite schema |
| W25 | [Title modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Title_modding.md) | Title structure/history/localization | Local hierarchy remains primary |
| W26 | [Characters modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Characters_modding.md) | Character history and appearance | Local history override contract remains primary |
| W27 | [Dynasties modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Dynasties_modding.md) | Dynasties, houses and coats of arms | Date-independent claim still needs local checks |
| W28 | [Bookmarks modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Bookmarks_modding.md) | Start-date setup | Feature-specific testing remains necessary |
| W29 | [Lifestyles modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Lifestyles_modding.md) | Lifestyles/focuses/perks and early-load cautions | Restrictions need current validation |
| W30 | [Regiments modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Regiments_modding.md) | Men-at-arms types | No engine/battle algorithm guarantee |
| W31 | [Artifact modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Artifact_modding.md) | Artifact definitions and creation orientation | Local template/visual/slot references primary |
| W32 | [Map modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Map_modding.md) | Coordinated map assets/editor workflow | No replacement map tested |
| W33 | [3D models](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/3D_models.md) | Model and texture pipeline | No exporter/model validation performed |
| W34 | [Coat of arms modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Coat_of_arms_modding.md) | Coat-of-arms assets and definitions | No rendered custom coat of arms tested |
| W35 | [Music modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Music_modding.md) | Music files and definitions | No custom audio tested |
| W36 | [Sound modding](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Sound_modding.md) | Sound-system orientation | Brief source; full pipeline unresolved |
| W37 | [Console commands](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Console_commands.md) | Console/debug discovery | Commands must be confirmed in actual build |
| W38 | [Effects list](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Effects_list.md) | Historical engine effect signature discovery | Source explicitly warns table is outdated |
| W39 | [Triggers list](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Triggers_list.md) | Historical engine trigger signature discovery | Source explicitly warns table is outdated |
| W40 | [Scopes list](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Scopes_list.md) | Scope/target documentation discovery | Regenerate after updates |
| W41 | [Data types](https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Data_types.md) | UI function/type discovery | No current local dump; do not assume complete signatures |
| P01 | [Dev Diary 30: Event Scripting](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-30-event-scripting.1397140/) | Event structure, dynamic text and dispatch | 2020-06-09; historical developer explanation |
| P02 | [Dev Diary 37: Making Mods](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-37-making-mods.1410656/) | Jomini layer, interfaces, hardcoded links | 2020-08-11; historical developer explanation |
| P03 | [Dev Diary 126: Modding Activities](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-126-modding-activities.1580680/) | Activities, traits, data models and conditional scope changes | 2023-05-02; Tours and Tournaments/1.9 context |
| P04 | [Grand Jomini Modding Information Manuscript](https://forum.paradoxplaza.com/forum/threads/grand-jomini-modding-information-manuscript.1170261/) | Scope/list/variable/helper concepts | 2019-04-25; shared Jomini/Imperator examples, not CK3 APIs |
| T01 | [Tiger upstream README](https://github.com/amtep/tiger) | Validation, command line, update lag and false positives | Upstream documentation consulted; no binary installed/run |
| T02 | [OldEnt versioned engine documentation](https://github.com/OldEnt/crusader-kings-3-triggers-modifiers-effects-event-scopes-targets-on-actions-code-revisions-list) | API dump discovery and version comparison | Repository catalogue consulted; matching 1.20 dump not established |
| A01 | [CK3-Modding Documentation](https://github.com/CK3-Modding/Documentation) | Older fundamentals/reference/tutorial catalogue | Archived 2023-06-21; historical discovery source |
| A02 | [Wiki mirror repository](https://github.com/jesec/ck3-modding-wiki) | Wiki access fallback, README and table of contents | Maintainer describes daily synchronization; exact upstream revision not independently verified |
| A03 | [Wiki mirror license](https://github.com/jesec/ck3-modding-wiki/blob/db66965014483aa1a0e0905e5a922be9ee3b9a2f/LICENSE) | No wholesale text archive created | Pinned LICENSE declares Wiki articles CC BY-SA 3.0; individual images and game content have separate rights (earlier MIT attribution corrected) |

Original Wiki URLs, accessed URLs, dates, statuses and access limitations are retained in [sources.json](sources.json).

## Local primary material

- Installation `launcher/launcher-settings.json`: 1.20.0.3 (Crozier), read 2026-10-03. Exposed executable version was blank.
- All native `.info` reference paths: [developer index](../reference/native-info-index.md). Actual hashes/definitions: [local index](../reference/local-index.json).
- Complete-file discovery and literal helper dependency evidence: [audit evidence](../reference/audit-evidence.json). Reviewed meaning and limits: [audit findings](vanilla-audit.md).
- All eleven workspace content roots, external/internal descriptors, scripts, text and asset-overlap inventory: [workspace inventory](../reference/workspace-inventory.md).
- User-data `logs/code_revisions.log`: old 1.16.3 run; current generated engine signature dumps absent from searched paths. Logs may contain personal/save-specific content and were not copied.

## Access limitations

| Requested source | Outcome |
|---|---|
| `https://ck3.paradoxwikis.com/Modding` | Direct fetch rejected/unavailable (401 on first attempt); mirror used |
| `https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-87-royal-modding.1507899/` | Client challenge; not used as accessible primary evidence |
| `https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Building_modding.md` | Unavailable guessed name; native building .info used |
| `https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Casus_belli_modding.md` | Unavailable guessed name; native CB .info used |
| `https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Schemes_modding.md` | Unavailable guessed name; native scheme references used |
| `https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Story_cycles.md` | Unavailable guessed name; native story references used |
| `https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Customizable_localization.md` | Fetch unavailable despite catalogue entry; native custom localization .info used |
| `https://raw.githubusercontent.com/jesec/ck3-modding-wiki/master/wiki_pages/Game_rules_modding.md` | Unavailable guessed name; native game-rule .info used |

A shell-based GitHub request was also blocked by local network connectivity; browser research tools remained usable. No source was silently substituted with an unverified third-party tutorial.

## Reuse and licensing

Full Wiki/game-text archives are intentionally absent. A mirror repository license does not automatically relicense all upstream content. Developer/forum material is paraphrased sparingly, and no full scripts or assets from the installed game are distributed here. The teaching fixtures are original small examples. Workspace asset credits remain in their original directories; reuse in a published mod needs asset-specific permission review.

## Updating evidence

Record the new installation and source dates, regenerate local indexes, then review changed contracts and teaching examples. Do not declare old material current just because an online archive was refreshed.

## Current export/recipe sources (2026-10-03)

Installed baseline 1.20.0.3 and engine commit are supported by the [runtime intake](../update-readiness/evidence/runtime-intake.json), including both original export sessions and their different crash/exit results. All eleven raw sources are listed with path, timestamp, SHA and decoding candidate in [engine index](../reference/engine-1.20.0.3.json). Recipe source paths, full-read line counts and hashes are in [native recipe audit](../examples/native-recipe-audit.json); exact asset originals/hashes in [fixture manifest](../examples/fixture-assets.json).

Rechecked [Tiger primary repository](https://github.com/amtep/tiger) and [Wiki archive primary repository](https://github.com/jesec/ck3-modding-wiki) on 2026-10-03. Tiger describes validation scope and possible false positives/update lag; no installed Tiger executable was found and target-build support is not established here. No installation or validation run was performed. Historical wiki/OldEnt references remain discovery aids; current installed exports and native callers take priority for this baseline. These pages are summarized, not mirrored.

## General Crozier source supplement — 2026-10-03

New general research uses the official [Steam announcement feed](https://store.steampowered.com/news/posts/?appids=1158310&feed=steam_community_announcements): diary #8 (2026-09-29), release (2026-09-30), and 1.20.0.3 hotfix (2026-10-01). Native schema/API detail is independently sourced in [evidence](general-120-evidence.json), not transcribed from a changelog. The [coverage ledger](crozier-source-coverage.md) states included/excluded sections. Tiger [trigger](https://docs.rs/tiger-lib/latest/src/tiger_lib/ck3/tables/triggers.rs.html) and [effect](https://docs.rs/tiger-lib/latest/src/tiger_lib/ck3/tables/effects.rs.html) tables are validator schemas; the trigger header states 1.18.1, and the effect header is malformed. Filter/annotation guides are linked in the [tools chapter](../systems/crozier-gui-tools.md). The Wiki mirrors remain historical declaration discovery, not evidence for omitted defaults.

## Additional jesec sources — 2026-10-03

J01–J04 pin the Wiki, More, Less Restrictive and Scrollable repositories in the [source report](jesec-repositories.md). W01–W41 are preserved; newly discovered Wiki pages receive additional W IDs in [the complete ledger](jesec-wiki-coverage.md) and `sources.json`. A03 is corrected from the pinned Wiki license; the separate Base tooling/game notices are unchanged. All four repositories have independent inventories, source dates and license qualifications. No new runtime compatibility result is implied.

## Subsequent standalone MDC static migration evidence — 2026-10-03

The [new review](../update-readiness/mods/mass-demand-conversion-static-migration.md) and [separate machine evidence](../update-readiness/evidence/mass-conversion-static-migration-20261003.json) use the pinned jesec Base commits for 1.19.0.6/1.20.0.3, original local Engine exports and unchanged installed sources. They retain old/new entry spans, followup source spans, all eleven export hashes, fourteen Script declarations, three GUI declarations and standalone source/count-reference checks. The earlier history, source and caller reports remain independent evidence. These are static findings; no new game/Tiger/GUI/MP validation or compatibility claim follows.

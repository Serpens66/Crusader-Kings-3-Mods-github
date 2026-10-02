# Additional subsystem guide

This guide identifies implementation surfaces, connected files, starting evidence and tests. It is not a claim that every field of every system is fully documented. The [coverage matrix](../research/coverage.md) identifies systems that still need a new feature-specific audit. All paths below are relative to the installed `game` root. Consult the [developer reference index](../reference/native-info-index.md) for exact `.info` paths.

## Culture

Definitions are spread across `common/culture/cultures`, pillars, traditions, innovations, eras, names and aesthetics. Current native culture definitions use explicit ethos, heritage, language, martial custom and head-determination pillars, plus lists of traditions, name lists and graphical references. The general `_cultural_traits.info` documents separate character/province/county/culture modifier contexts and adoption-cost scopes.

Do not build a new culture from the old Wiki's culture-group outline alone. Audit an existing complete culture and each referenced pillar/tradition, then localize its name and related UI. Changing a cultural parameter affects scripted consumers, so search those consumers before assigning behavior to a parameter.

For runtime changes, identify whether the desired effect changes a character's culture, a county's culture, a culture definition or a dynamic culture's composition. Test culture creation and history separately, including unavailable innovations and graphical/name fallbacks.

Sources: [Culture modding](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Culture_modding.md), local culture `.info` files and `00_tujia.txt` recorded in the audit.

## Religion, faith and rites: current installation differs from the Wiki

This installation uses `common/religion/religion_types`, `faith_types`, `rite_types`, doctrine types/groups/categories, tenet types and holy-site types. The old Wiki describes faiths nested under religion definitions in `common/religion/religions`; that is not an appropriate new-definition template for the audited installation.

Native faith definitions use `faith_details` for religion, color and graphical references, with separate `main_rite`, holy-site collections, tenets and doctrines. The local references explain that scripted main rites own core tenets and rite-specific doctrines; faith-intrinsic doctrines can remain additive, while a rite's doctrine takes precedence within its group. A faith lacking a scripted main rite can seed a dynamically created one. These contracts are specific to the as-installed files.

The rite schema has its own parent faith, creation/conversion controls, icon, color, founder and doctrine/tenet collections. Not-created rites may error when addressed; history/start-date availability must be checked. Province history explicitly recommends recording faith as a fallback when a requested rite is not available in a selected bookmark.

A complete new religious feature therefore crosses definitions, doctrine/tenet dependencies, current faith/rite history, holy sites, localization, graphics and conversion interactions. Test the actual selected bookmark, main-rite assignment, conversion result and religious-head behavior. Do not assert new conversion effects from older faith-only examples.

Sources: native religion/faith/rite `.info` and actual type files; [historical religion guide](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Religions_modding.md). See [version conflicts](../research/vanilla-audit.md).

## Titles, characters, dynasties and history

`common/landed_titles` defines title structure/properties. `history/titles` supplies dated holders and other historical state; `history/characters` defines historical characters, and `history/provinces` configures province/holding start state. Dynasty/house definitions and coats of arms are additional references.

The native history schema applies initial values plus dated blocks. It supports character `effect` only when that character is alive at the selected start date, and a separate `effect_even_if_dead`. Historical dates are not scheduled future gameplay events.

Current character-history documentation supports `id_override_priority`, but says base attributes and birth are overridden while other content combines additively. Review collisions at a dated-entry level instead of assuming complete character replacement. Keep character IDs and relationships consistent with life dates and title holders.

For new history, test every supported bookmark, parentage, marriages, lieges, culture, faith/rite, title creation and coat of arms. A playable title that exists in the database still needs valid start-state ownership/government. Date boundaries and dead characters are particularly important.

Sources: native history/title references; [Titles](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Title_modding.md), [Characters](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Characters_modding.md), [Dynasties](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Dynasties_modding.md), [Bookmarks](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Bookmarks_modding.md).

## Buildings and holdings

`common/buildings/_buildings.info` documents construction time, type, assets, cost, prerequisites, modifiers and completion effects. Different modifier fields apply to different objects. `common/holdings` controls holding definitions; history and special-building placement connect the database to the map.

Start from a building of the same type: regular, special or duchy-capital. Trace its upgrade chain and holding availability. Native legendary buildings illustrate multiple asset selections, construction-cost references, character/county/province modifiers and completion effects. A building object by itself does not prove it can be built where intended.

Audit whether the loader allows the required extension without replacing a holding definition; older claims that every addition requires replacing one complete file are not universally safe. Test eligibility, construction, completion, upgrades, disabled state, graphical placement and AI value.

Sources: native `_buildings.info`, `_holdings.info`, actual `00_legendary_buildings.txt`. A guessed mirror URL `Building_modding.md` was unavailable; use native evidence rather than a fabricated page.

## Warfare, casus belli and regiments

`common/casus_belli_types` connects availability, costs, target titles, declaration and victory/white-peace/defeat/invalidation outcomes. Its native reference assigns different roots to attacker/defender/title validation blocks and warns that some defender references may be absent during evaluation. `common/casus_belli_groups` can impose additional restrictions.

Title transfers use more than a simple holder assignment: the native debug CB creates a title-and-vassal change object, applies changes to target titles and resolves the batch. Audit the full outcome helper chain, including release, truce and legitimacy behavior, before reusing a conquest pattern.

Regiment definitions live under `common/men_at_arms_types` and connect to terrain, innovations, culture, graphical unit definitions and modifiers. Battle/army algorithms remain engine capabilities unless an exposed script/define permits changing the specific parameter. An army-oriented request needs an exact supported operation, not a general assumption that all warfare is scriptable.

Tests: attacker/defender, self/invalid target, multiple titles, invalidated war, white peace, ally participation, truces, inheritance, raised/unraised regiments and missing DLC/assets. `Leave Wars` is a workspace case study, not a validated current warfare template.

Sources: native `_casus_belli.info`, actual CB helpers; [Regiments](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Regiments_modding.md).

## Activities and travel

`common/activities/activity_types/_activity_type.info` is a large current contract for activity options, phases, costs, locales, guests and callbacks. Separate invite rules, intents and pulse-action databases supply other pieces. A host-character eligibility block and an activity-scoped callback are not interchangeable.

The developer's [activity-modding diary](https://forum.paradoxplaza.com/forum/developer-diary/dev-diary-126-modding-activities.1580680/) explains phase/location structure and options. Use the current `.info` file rather than the historical diary for field completeness. Native `camp_party.txt` includes DLC/government gates, host validity, invalidation effects, location filtering and predicted versus actual cost.

Travel options use their own visibility/validity, travel-modifier and application-effect fields. Points of interest have travelling-character and province callbacks with different contracts. The local POI reference restricts add/remove callbacks to local province state, and provides a province-list-building interface.

Tests: host and guests, impossible location, route, travel interruption, death/invalidation, option cost, phase order, locale events and end/cleanup. A new activity requires more than an event with `type = activity_event`.

## Artifacts

Artifact types, templates, slots, visuals, features and blueprints are separate databases under `common/artifacts`. A template can constrain equipping; a blueprint controls reforging input/output types and permissible modifier replacements. Runtime creation effects additionally supply owner, rarity, name, description and other required inputs according to their actual signature.

The native pilgrim-badge template checks an artifact-owned location variable and a holy-site relationship for equipping. Thus an artifact feature may need both artifact scope and the evaluating character context. Trace creation, acquisition, ownership change, equipping and destruction consumers.

Test inventory/court placement, equipping restrictions, modifier application, durability/destruction, inheritance and reforging. Verify every referenced template/visual/slot exists with the enabled content.

Sources: native artifact `.info`; [Artifact modding](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Artifact_modding.md).

## Schemes, stories, lifestyles and rules

The current scheme tree includes `common/schemes/scheme_types` and related agent/phase structures. Native examples specify skill, target type, category, agents, progress and success predictions. These schemas have changed over CK3's lifetime. Audit a scheme matching the target type before adding one.

Story cycles own ongoing state and can dispatch periodic groups. The native Temujin story ends on owner death and dispatches an on action from `story_owner`. An empty or deprecated file in that directory is not a usable example. Audit creation, owner, pulses and end conditions together.

Lifestyles, focuses and perks span several databases and GUI/assets. Native lifestyles define XP and eligibility; the Wiki flags early-load restrictions on some generated/scripted functions. Those restrictions require a current feature-specific test before using a helper there.

Game rules define settings/defaults and categories. Native `_game_rules.info` documents localization prefixes and special flags. A custom flag does not automatically create a new engine mechanic: script must actually query/use the selected rule or the engine must recognize that particular flag.

Sources: native subsystem `.info` and selected definition files; [Lifestyles](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Lifestyles_modding.md). Runtime examples for these larger systems remain feature-specific work.

## Maps and graphics

The native `map_data/default.map` names the province definition CSV, province image, rivers, topology and adjacency files. Changing one of these surfaces can require coordinated updates to landed titles, province history, terrain and locators. IDs, colors, resolution, image format and topology must remain consistent.

The [map guide](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Map_modding.md) covers the editor and asset pipeline. This collection does not claim to have validated a replacement map. Before implementation, audit the actual image dimensions/modes, map settings and editor output requirements; test loading and pathfinding in the engine.

Textures and portraits connect DDS files, GUI/portrait definitions and potentially meshes/materials/entities. A file replacing a native texture uses an exact asset path. A new graphical key also needs a definition or consumer. Check color space, alpha, compression and mipmaps against the particular native asset; there is no single DDS preset suitable for everything.

The workspace has extensive graphical replacements, including 664 DDS files in `GFX-Mod Serp`. Its notes explain a fuller local variant versus a reduced distributed variant. Preserve asset authorship/licensing and do not treat a historical checksum observation as a current compatibility guarantee.

Sources: [3D models](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/3D_models.md), [Coats of arms](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Coat_of_arms_modding.md), local graphical `.info` references and workspace asset inventory.

## Sound and music

Music has script definitions and audio assets; sound also relies on the engine's sound-event pipeline. The reachable Wiki sound page is brief and does not establish a complete custom-audio workflow. Treat codec/import/bank/export steps as unresolved until the matching tools and local format are audited. No audio tools were installed here.

Sources: [Music](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Music_modding.md), [Sound](https://github.com/jesec/ck3-modding-wiki/blob/master/wiki_pages/Sound_modding.md), native music `.info` index.

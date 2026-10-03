# Dynasty legacies: definitions, eligibility, consumers and migration

Baseline: installed **1.20.0.3 Crozier**, rechecked on 2026-10-03. Community implementations target **1.19.***. Read the [repository report](../research/jesec-repositories.md), [pinned source inventory](../research/jesec/evidence.json) and [additional feature audit](../research/jesec/feature-audit.json) together. Historical comparisons reuse the existing [Vanilla version lock](../reference/vanilla-history-lock.json); they do not change it.

## Native schema and scope contracts

The complete installed references are `game/common/dynasty_legacies/_dynasty_legacies.info` and `game/common/dynasty_perks/_dynasty_perks.info`. Complete definition files, literal callers, helper dependencies, localization and GUI consumers are indexed in the audit. File discovery is broader than the manually reviewed contracts below; neither the dependency closure nor these third-party mods proves runtime correctness.

| Entry or field | Documented contract | Consequence for a new mod |
|---|---|---|
| `common/dynasty_legacies/<unique>.txt` | A track is a container for perks | Define a uniquely prefixed track; do not confuse it with a lifestyle |
| Track `is_shown` | Trigger in **character** scope | Enter `dynasty` before a dynasty trigger; explicitly enter `dynast` for head-based conditions |
| `common/dynasty_perks/<unique>.txt` | Perk root is the **dynast** | Conditions/effects use the dynasty head as character root, per the `.info` |
| Perk `legacy` | Track key | Resolve the exact ID, including prefixes; display text is not the ID |
| Perk `can_be_picked` | Character trigger | Visibility and purchase eligibility are independent layers |
| Perk `effect` | Character effect run on unlock | Distinguish one-time mutations from persistent bonuses and descriptive tooltip effects |
| `character_modifier` | Applied to characters in dynasties with the perk | This is not a custom event fired separately for each member |
| `faith_character_modifier` | Dynasty character modifier conditional on doctrine | Current field; historical `doctrine_character_modifier` is not a current recipe |
| `ai_chance` | Script-value weight; documented default **1000** | Use `value`/`multiply` numeric syntax here; do not copy an event weight block blindly |
| `traits` | Trait choices on unlock; RHS is AI chance | At least one nonzero chance; selected trait stored on dynasty as `var:<perk_key>_<trait_key>` |
| `trait` | Direct trait field exists in the schema | Audit its actual native usage before proposing a trait-grant mechanic |
| Generated localization | `<key>_name` for track and perk | Native GUI additionally consumes descriptions; include `<track>_desc` when used |

**Initialization restriction:** the installed legacy `.info` explicitly warns against scripted helpers and content-generated triggers/modifiers in track script triggers, because databases may not yet be available and startup can crash. Its examples include relation/lifestyle-generated commands. Keep `is_shown` in the permitted primitive subset. Do not interpret this as a blanket ban on every scripted reference in perk fields: native perk AI blocks do call `can_start_new_legacy_track_trigger`, and native tracks use `has_dynasty_perk`. Exact initialization permissions not established by these examples remain a startup-test gate. A valid exported function signature alone cannot settle database readiness.

The current trigger export documents `has_dynasty_perk = key` in **dynasty** scope. Use `lookup.py has_dynasty_perk --context 4`; the effect named `add_dynasty_perk` is a separate entry. `dynasty = { dynast = { ... } }` changes the evaluated character; a player's culture and their dynast's culture can differ. Optional transitions such as native `dynasty ?= { ... }` need an explicit design for absent objects; see [scopes](../handbook/scopes.md).

## More Legacies: all content and execution surfaces

The [complete map](../research/jesec/more-legacies-map.md) lists each track's literal eligibility inputs and every modifier assignment of all **50** perks, with definition lines and nine localization files. Sources are the pinned [track file](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod/common/dynasty_legacies/more_legacies.txt) and [perk file](https://github.com/jesec/ck3-mod-more-legacies/blob/6a30f714cfb6dcaf3811ea3e912b7f7e0cdc8cac/mod/common/dynasty_perks/more_dynasty_perks.txt).

Four track blocks have no explicit visibility condition: Devotion, Industry, Influence and Temptation. Chivalry, Dominance, Mercantile and Seafaring use an OR of dynast culture/ethos/tradition conditions; Tradition uses NOR of its listed cultural conditions. Witchcraft checks the dynast's witch trait or witch secret. Every restricted track adds an alternative `has_dynasty_perk = <first perk>` branch: the **observed intention** is to retain access after culture, traits or secrets change. Actual display refresh and ownership transitions remain untested.

The perk payload is entirely declarative `character_modifier`. These files create no custom events, callbacks, saved scopes, variables, payments or notification routes. Any associated unlock costs, ordering, permissions, application to new dynasty members or synchronization come from the native legacy system; they are not implemented by fifty scripted transactions. The upstream README's sequential-unlock and DLC claims are not adopted as tested guarantees.

Each first perk has an AI formula starting at 11, then multiplies by zero when `can_start_new_legacy_track_trigger = no`. The other forty rely on the documented default. The complete current helper in `common/scripted_triggers/00_dynasty_triggers.txt` checks explicitly enumerated native first/fifth perk pairs with DLC branches. It now includes PAM, but does **not** enumerate `bld_` tracks. Consequently the helper's name is not a guarantee that AI will finish one custom track before starting another. No `$PARAMETER$` is supplied by these ten calls; the policy difference is the explicit set of tracked IDs, not a missing argument.

Named phase-duration values resolve through `common/script_values/00_scheme_values.txt`: `medium_scheme_phase_duration_bonus_value = -20`, `monumental_scheme_phase_duration_bonus_value = -100` in this installation. The calls occur in modifier value positions. They are not percentages or event delays. The [static check](../research/jesec/more-legacies-checks.json) distinguishes literal engine modifier names from generated scheme/holding modifiers. Audit `common/modifier_definition_formats`, the referenced schemes and holdings, and the real tooltip/benefit before interpreting a generated name's units or DLC availability.

The repository contains ten ID-matched icons at `mod/gfx/interface/icons/dynasty/` and ten illustrations at `mod/gfx/interface/illustrations/legacy_tracks/`. All 60 generated name keys are present in every supplied language file. No pixel format, mipmap, frame layout, visual scaling, translation accuracy or engine path-resolution test was performed. The artwork is credited separately; see [rights](../research/jesec-repositories.md#licenses-and-reuse).

## Less Restrictive Legacies: complete change contract

All **twelve** changed `base/game` blobs were compared with locked 1.19.0.6. Six track files add visibility alternatives; six perk files relax selection gates. There are no deleted game files. The original migration commit `44763edca8493e0a6bf1d11c467ea61c94a4b95f` touched the same twelve paths. Later Vanilla merges introduced standardized eligibility helpers; the current diff must be interpreted against its exact baseline, not against an older commit's inline conditions.

Every row below is a literal **additional OR alternative**, not replacement of all native eligibility. Culture/faith alternatives run on `dynasty.dynast`; the EP3 influence branch tests the surrounding character. File links pin the investigated commit.

| Track file and affected track | Added alternative(s) | Perk-gate change in its corresponding file |
|---|---|---|
| [98 FP1](https://github.com/jesec/ck3-mod-less-restrictive-legacies/blob/79494e84c4ff5eaba6e49dc3edaad71bf5814fa4/base/game/common/dynasty_legacies/98_fp1_legacies.txt), adventure | `tradition_practiced_pirates`, `tradition_seafaring`, `tradition_diasporic`, `tradition_druzhina`, or `heritage_north_germanic` | `01_fp1_dynasty_perks.txt`: remove `eligible_for_fp1_dynasty_legacies_trigger` from first adventure and pillage perks |
| Same file, pillage | Practiced Pirates, Seafaring, Battlefield Looters, North Germanic heritage, or dynast `tribal_government` | Other perk payloads preserved relative to 1.19.0.6 |
| [96 FP2](https://github.com/jesec/ck3-mod-less-restrictive-legacies/blob/79494e84c4ff5eaba6e49dc3edaad71bf5814fa4/base/game/common/dynasty_legacies/96_fp2_legacies.txt), urbanism | `tradition_republican_legacy`, `tradition_parochialism`, `tradition_city_keepers` | `03_fp2_dynasty_perks.txt`: remove `eligible_for_fp2_dynasty_legacies_trigger` from both first perks |
| Same file, coterie | `tradition_family_entrepreneurship`, `tradition_tribe_unity`, `tradition_strong_kinship`, `tradition_mystical_ancestors`, or `ethos_communal` | Effects and member bonuses are not made universal by removing a pick gate |
| [95 FP3](https://github.com/jesec/ck3-mod-less-restrictive-legacies/blob/79494e84c4ff5eaba6e49dc3edaad71bf5814fa4/base/game/common/dynasty_legacies/95_fp3_legacies.txt), khvarenah | Faith religion `religion:zoroastrianism_religion` or `tradition_fp3_enlightened_magnates` | `03_fp3_dynasty_perks.txt`: all five pick blocks become `has_fp3_dlc_trigger = yes` |
| [92 MPO](https://github.com/jesec/ck3-mod-less-restrictive-legacies/blob/79494e84c4ff5eaba6e49dc3edaad71bf5814fa4/base/game/common/dynasty_legacies/92_mpo_legacies.txt), nomad | `tradition_horse_lords`, `tradition_steppe_tolerance`, or `heritage_mongolic` | `07_mpo_dynasty_perks.txt`: all five use `has_mpo_dlc_trigger = yes` |
| [83 EP3](https://github.com/jesec/ck3-mod-less-restrictive-legacies/blob/79494e84c4ff5eaba6e49dc3edaad71bf5814fa4/base/game/common/dynasty_legacies/83_ep3_legacies.txt), administrative | `government_has_flag = government_has_influence` | `06_ep3_dynasty_perks.txt`: all five use `has_ep3_dlc_trigger = yes` |
| [82 TGP](https://github.com/jesec/ck3-mod-less-restrictive-legacies/blob/79494e84c4ff5eaba6e49dc3edaad71bf5814fa4/base/game/common/dynasty_legacies/82_tgp_legacies.txt), sea | `tradition_maritime_way_of_life`, `tradition_tgp_esoteric_power`, `tradition_tgp_barangay_confederations` | `08_tgp_dynasty_perks.txt`: all fifteen Chinese/Japanese/SEA pick blocks use `has_tgp_dlc_trigger = yes` |
| Same file, japan | `tradition_tgp_ephemeral_grace` or `tradition_tgp_japanese_houses` | Government conditions inside effects are retained |
| Same file, china | **No track visibility change** | Chinese perk eligibility is still relaxed by the perk-file change |

The six perk paths and all source hashes are in the [inventory](../research/jesec/ck3-mod-less-restrictive-legacies-inventory.json). The complete patched files retain the existing effects, AI weights, modifiers and descriptive tooltip statements apart from comments/formatting and the described selection changes. A tooltip-only `custom_description_no_bullet` is not an implementation of its advertised bonus: trace its corresponding consumers. The feature audit records matching native callers and helper files; mechanically meaningful benefits outside their original government require targeted gameplay checks. For example, herd modifiers do not establish that a non-nomad now has a herd mechanic.

Top-level track `has_dlc_feature` gates are retained. The native game-rule alternatives `unrestricted_dynasty_legacies_all` and player-only plus `is_ai = no` are retained. The mod does not remove DLC ownership requirements generally. FP1/FP2 first-perk helper removal differs from replacing all FP3/EP3/MPO/TGP pick blocks with DLC-only helpers. Do not describe all six families as “remove only the first perk condition.” The upstream README's broad compatibility, Ironman/achievement and benefit assertions are unverified here.

## Crozier differences to preserve in any later adaptation

The existing Base tool's locked 1.19.0.6→1.20.0.3 comparison and full installed files identify eight changed legacy/perk paths. These are source findings, not permission to update these third-party mods.

| Change | Current native evidence | Integration implication |
|---|---|---|
| New PAM track and five perks | `81_pam_legacies.txt`, `09_pam_dynasty_perks.txt` | By God Alone / Christian visibility plus game-rule and owned-first-perk alternatives; leave unrelated new content intact |
| Administrative mechanics | `83_ep3_legacies.txt`, `06_ep3_dynasty_perks.txt` | `government_has_mechanic = administrative` replaces the old flag/`government_allows` usage in the affected places; adding influence access must retain the current native branch |
| Viewer struggle participation | `96_fp2_legacies.txt` | New surrounding-character Iberian involvement branch exists alongside dynast checks; copying the 1.19 override would lose it |
| Faith-qualified member modifiers | `00_dynasty_perks.txt`, `_dynasty_perks.info` | Use `faith_character_modifier`; Erudition also replaces faith-creation cost with rite-creation cost at a changed amount |
| Heroic trait choice | `05_ce1_dynasty_perks.txt` | `herald` replaces `saint`; do not copy historical trait IDs into a new example |

See [religion and rites](religion-rites.md), [Crozier migration](crozier-migration.md) and [existing history findings](../research/vanilla-history-20261003.md). More Legacies and Scrollable Legacies have no current `base/game` delta against 1.19.0.6; that does not certify the new content or metadata for Crozier. Less Restrictive has full modified files based on 1.19.0.6: adapting their minimal intent onto current native definitions is safer than promoting those historical full replacements.

## Scrollable Legacies: historical lesson and current source

The [original patch](https://github.com/jesec/ck3-mod-scrollable-legacies/commit/1df1400d09a760df2d42c0eae268b33da215f773) modified `base/game/gui/window_dynasty_house.gui`. It added vertical expansion, wrapped the legacy area in `scrollbox`, supplied `min_height = 300`, and put grids in `blockoverride "scrollbox_content"`. It retained separate `< 10` and `>= 10` layouts, six-column wrapping and 95×95 items for the larger collection, plus the smaller collection's existing cropped rows. These sizes are historical design choices, not engine limits.

The data binding remains `DynastyHouseView.GetLegacies`; each item uses `DynastyLegacyItem.GetTooltip`, `GetUnlockedPerksCount` and `widget_legacy_icon`. Moving a grid must preserve its outer `DynastyHouse.GetDynasty` context, item context, tooltip and texture consumers. `legacy_progress` uses a framed native texture, independently of the new track artwork. A working scroll container does not settle frame-number correctness or any existing workspace asset blocker.

At commit `3da17897081b9a8b9762ebb1025a45fad9b62a51` the mod dropped its GUI delta while merging 1.19.0.3. That historical native file and the locked 1.19.0.6 file contain a native scrollbox in the legacy section; the current installed complete window also contains it at line 1253. This supports **superseded by native layout by the examined 1.19.0.3 snapshot**, continuing in 1.20.0.3. The changelog's exact “since 1.19.0” release attribution is not independently proven by a 1.19.0 launch/depot test. Current mod tree: metadata and no game-code delta. The source is useful for container/data-binding study, not as a current required GUI replacement. “Unlimited tracks”, “zero performance overhead” and uninstall/save safety are not tested guarantees.

Current native `gui/window_dynasty_legacy.gui` additionally binds `DynastyView.GetLegacies`, a scrollbox conditioned on more than seven items, `DynastyLegacy.GetPerks`, `Dynasty.GetHeadOfDynasty`, `GetIcon` and `GetTrackIcon`. House overview and full legacy window are separate consumers. The data-type export contains the relevant functions with unregistered result types; it does **not** specify complete typed return contracts or texture lookup algorithms. Use [GUI contracts](localization-and-gui.md) and [GUI tools](crozier-gui-tools.md); do not invent missing result types.

## Original teaching sketch and review procedure

This is an original **untested schema sketch**, not an installed or advertised functional mod. Its fields follow the two installed `.info` files; `diplomacy` is a documented character modifier. Files belong in a new uniquely named package:

```text
# common/dynasty_legacies/example_unique_legacies.txt
example_unique_legacy_track = { }

# common/dynasty_perks/example_unique_perks.txt
example_unique_legacy_1 = {
    legacy = example_unique_legacy_track
    character_modifier = { diplomacy = 1 }
    ai_chance = { value = 1 }
}
```

Supply `example_unique_legacy_track_name`, `example_unique_legacy_track_desc` and `example_unique_legacy_1_name` in BOM-encoded localization, descriptor and independently licensed artwork as required by the actual GUI consumer. The empty visibility block avoids the track initialization helper question. Extend the number/order of perks only after confirming native ordering and display assumptions; the upstream five-perk pattern does not document every engine limit.

Before writing a complete mod, choose whether access follows the viewer, dynast, culture, faith/rite, government or owned-first-perk state. Evaluate visibility, eligibility, actual benefit and AI weights separately. Resolve all generated modifier names through the correct family, rather than demanding a literal engine modifier entry for every generated name. Preserve current native data if overriding existing keys or files, and check other mods' overlapping IDs and assets.

| Remaining contract/test | Concrete clarification | Expected observation to record |
|---|---|---|
| Initialization permission | Start a fresh debug game with minimal new track, then add each primitive condition separately | No startup crash or invalid-trigger log; do not treat another mod's history as this test |
| Visibility vs purchase | Non-head/viewer and dynast with different cultures; first perk absent/present; change culture/government/faith | Record displayed tracks, enabled purchase and actual actor for each combination |
| Native transaction/order | Unlock each stage with exact before/after renown, insufficient funds and repeat requests | Actual costs match displayed costs; no repeat reward or unintended stage access |
| Dynasty modifiers | Existing/newborn/new member, dynast death, save/load | Correct bonuses and no stale application; permanence inferred only after testing |
| Broadened government access | Each newly allowed government and DLC on/off; tooltip-only and active effects separately | Missing mechanics do not create falsely promised benefits; exact conditional behavior recorded |
| AI custom-track policy | Run controlled AI test with one unfinished custom track and native unfinished tracks | Confirm helper-enumeration consequence, not a guessed probability |
| GUI, assets, performance | 0/1/7/8/9/10/many tracks, multiple UI scales, long translations | No clipping, correct selection/tooltips/icon/background/frames, usable scroll performance |
| MP | Two players viewing and purchasing across different dynasties, repeated actions, save/load | Correct actor/renown and synchronized outcomes; no local GUI owner inferred for gameplay |

These new cases complement the existing [three-run fixture manual](../examples/test-runs.md). They do not close its pending cases, the 43 mod-function cards or the Knight/graphics blockers.

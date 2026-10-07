# CK3 mod update readiness

## Acceptance descriptions corrected in1.080 — 2026-10-07

[Current two-notification fix](mods/mass-demand-conversion-message-context-20261007.md): user-tested vassal acceptance did not crash but exposed recipient-name localization failure. Both overrides now supply desc in their event message call; the common type uses event_message_text. Native effects/previews and eight translations retained;28 static tests. Corrected rendering and house/mixed acceptance tests remain open; foreign crash unresolved. Engine exports1.20.0.3 are stale for installed1.20.0.4.


## Short effect preview — 2026-10-05

[Current eight-language text shortening](mods/mass-demand-conversion-short-effect-20261005.md): only the effect-preview sentence changes;35 keys, confirmed GUI layout, gameplay and version1.079 remain unchanged. New dateline preserves all63 watches/history and refreshes eight localization hashes. One-to-two-line wrapping remains untested.


## User-confirmed MDC layout — 2026-10-05

The user confirms that the [fixed-slot recipient layout](mods/mass-demand-conversion-fixed-rows-20261005.md) now looks correct in game. Use that code and its documented geometry as the current visual reference; preserve the failure ledger. This is visual acceptance of the reported presentation, not a complete transition/scaling/scrolling, percentage, delivery or multiplayer certification. Earlier pending-rendering statements describe pre-confirmation states.


## Fixed recipient slots — 2026-10-05

[Current fixed-slot layout](mods/mass-demand-conversion-fixed-rows-20261005.md): latest user screenshot disproves the caption-only correction, including first-open/filter-switch differences. Five permanent slots and explicit radio/text coordinates replace automatic recipient measurement; confirmed filter/viewport and all functional bindings remain. 26 static checks;63 native watches. New rendering remains untested; read the failure ledger before reuse. Earlier dated sections describe historical states.


## Common recipient columns — 2026-10-05

[Current caption-only correction](mods/mass-demand-conversion-radio-columns-20261005.md): user confirms preceding viewport size correction centers the list and shows all five groups. Eleven native recipient captions now have identical285×30 fixed left-aligned fields; filter/scrollbox structure and bindings retained. 24 static tests pass; new column rendering remains untested. Failure ledger records the partial user confirmation.


## Scrollbox nominal-size correction and failed-layout ledger — 2026-10-05

[Current isolated correction](mods/mass-demand-conversion-scroll-size-20261005.md) and [mandatory screenshot-backed failure ledger](mods/mass-demand-conversion-gui-failures-20261005.md). Latest screenshot confirms filter placement but recipient viewport displacement. Native inherited100×100 size is now explicitly overridden514×210; no list/filter behavior change. 23 static tests pass; rendering remains untested. Read the ledger before further GUI changes.


## Git recipient-list restoration — 2026-10-05

[Current restoration and pending game matrix](mods/mass-demand-conversion-git-targets-20261005.md): user reported first-open row overlap and continuing filter inset. Entire native-radio scrollbox subtree restored from Git a81d7f3; custom recipient template removed. Filter heading/columns now use explicit top-left parent/own anchors and x0/122/249/351 positions. 22 static checks pass; first-open/filter-change rendering remains untested. Version 1.079 and gameplay/texts/history retained.


## Explicit flexible-space alignment — 2026-10-05

[Current correction and pending game matrix](mods/mass-demand-conversion-flex-alignment-20261005.md): latest screenshot disproves prior recipient centering and shows filter inset. Explicit 514×32 filter viewport/trailing expander and full-size recipient hbox/equal expanders replace anchor-only alignment. 22 static tests pass; actual rendering remains untested. Gameplay/texts/1.079 metadata, bundle and historical evidence are retained.


## Narrow filter row and centered recipient contents — 2026-10-05

[Current patch and pending runtime matrix](mods/mass-demand-conversion-centered-options-20261005.md): 451-wide left-origin filters inside the existing 514-wide section; only recipient rows use a local native-derived button with centered radio/text content and full-width click regions. Screenshot confirms preceding list fits but is left-aligned and filters still overflow. All gameplay/texts/1.079 metadata and historical records remain; new rendering and MP are untested.


Standalone MDC [horizontal alignment correction](mods/mass-demand-conversion-alignment-20261005.md) retains the compact layout and addresses user-observed right overflow. Five groups/default mark/indirect count21 were observed in the preceding patch; corrected alignment remains untested. Current static count: 20 tests, 54 source watches; version1.079 and remaining runtime/MP gates unchanged.


Standalone MDC [compact widget correction](mods/mass-demand-conversion-compact-widget-20261005.md) addresses user-observed missing rows and overflow. Current source has 35 localization keys per language, 19 static checks and 53 native watches. The corrected GUI, unfiltered counts and MP await in-game verification; version remains 1.079.


Standalone MDC is now **1.079** after the [eight-language localization review](mods/mass-demand-conversion-localization-20261005.md). Gameplay/widget code is unchanged by that update; GUI/percentage/MP acceptance remains pending. Earlier 1.078 references describe the notification implementation.


Current standalone MDC [chance-filter extension (2026-10-05)](mods/mass-demand-conversion-chance-filter-20261005.md) has five visible groups, three filters and eleven fixed native entries. The source registry now monitors 49 MDC sources. Static checks pass; GUI lifecycle/order, percentage parity and multiplayer remain untested. This changes neither compatibility metadata nor the bundle.


The initial preparation report below records the **as-installed 1.20.0.3 (Crozier)** source tree and unresolved contracts before implementation. At that historical stage no mod, installation file, launcher registration or playset was changed. Subsequently standalone MDC 1.078 was implemented with two active event overrides; see its [notification report](mods/mass-demand-conversion-notifications-20261003.md). For new update requests follow the [mandatory version-independent workflow](../handbook/mod-update-workflow.md). User-run exports are separately recorded in [runtime intake](runtime-intake.md); gameplay/GUI/MP acceptance remains pending.

Research date: **2026-10-03**. All 18,710 previously indexed native text/reference hashes still match. The new workspace baseline covers **853 files**, including binary assets and pre-existing user changes. The first inventory had 851 files; two excluded-root OUTDATED markers appeared during the audit and are preserved. See [workspace observations](evidence/workspace-observations.json) for baseline reconciliation. This establishes reproducibility against the local installation; it does not establish that the installation is an unmodified Steam distribution.

## Start here

| Need | Document |
|---|---|
| Carry out a new mod-update request | [Mandatory workflow and comparison tool](../handbook/mod-update-workflow.md) |
| Select the reviewed comparison baseline | [Baseline index](update-watch-index.json), [initial source registration](update-watch-20261003.json) |
| See every functional work package and its gate | [Feature matrix](feature-matrix.md) |
| Check dependencies and permitted combinations | [Conflict matrix](conflicts.md) |
| Follow the implementation order | [Implementation packages](implementation-order.md) |
| Obtain current engine contracts and fresh logs | [User debug run](debug-run.md) |
| Review the captured engine exports | [Runtime intake](runtime-intake.md) |
| Obtain GUI exports through a normal debug start | [Normal debug starter](diagnostic-start.md) |
| Run later acceptance tests | [Test protocol](test-protocol.md) |
| Locate texture consumers and format/size differences | [Asset consumers](asset-consumers.md) and [texture comparison](texture-comparison.md) |
| Trace evidence and distinguish audit depth | [Evidence and sources](sources.md) |
| Check unchanged sources and documentation quality | [Verification](verification.md) |

## Mod sheets

| Mod | Main result |
|---|---|
| [CustomDefines](mods/custom-defines.md) | 23 active keys exist; prepare removal of 12 Knight Manager files; old GUI type replacements need a current rebase and UI contract check |
| [Gender Colour](mods/gender-colour.md) | Two direct native texture replacements; three additional variants need reference/packaging verification |
| [GFX Mod](mods/gfx-mod.md) | Rank atlas is shorter than current native atlas; shared gender textures conflict with other graphical packages |
| [GFX Mod Serp](mods/gfx-mod-serp.md) | 664 textures need consumer-aware review; six concrete post-effect assignment changes; rank atlas and other dimensions differ |
| [Leave Wars](mods/leave-wars.md) | Standalone and bundle content are byte-identical; current war-state revalidation and command contracts are prerequisites |
| [Mass Demand Conversion](mods/mass-demand-conversion.md) | Current standalone 1.078 declares 1.20.*; [two acceptance overrides](mods/mass-demand-conversion-notifications-20261003.md) now have targeted source/caller watches. [Native tests](mods/mass-demand-conversion-tests.md) and G01–G05 remain open |
| [SerpAlerts](mods/serp-alerts.md) | Eight important-action types and four active hook subscriptions; verify current contexts, overlap and recipient routing |
| [SerpInteractionsDecisions](mods/serp-interactions-decisions.md) | Six current feature families (embedded conversion/Leave Wars removed 2026-10-03; see the sheet); proven helper mismatch in excommunication; exact 500-gold display bug; succession and delayed education need focused tests |

The independent Knight Manager packages and `test` are excluded from updates at the user's request. Their overlaps are still recorded because enabling them can affect retained packages. No exclusion means deleting their directories.

## Evidence levels

**Source-confirmed** means the stated difference or declarative contract was inspected. **Plan ready** means a narrowly defined change can be specified from that evidence, subject to later validation. **Blocked contract** means no behavioral implementation decision should be made until the named engine or feature-audit gap is resolved. **Runtime pending** means expected results are written but not observed in the game.

The collection read complete developer references and discovered literal source dependencies. That discovery does not complete the semantic audit of every engine primitive, GUI loader or parameter-expanded call. Each sheet identifies exactly where the remaining feature audit must continue. This respects the workspace requirement that unknown Vanilla contracts must not be replaced with assumptions.

## Confirmed priorities

1. Preserve existing purposes and numeric policies. Adapt relevant Vanilla changes without introducing unrelated new capabilities.
2. Test SP and MP using new games. Save/reload of these new test campaigns is required; importing old campaigns is outside the compatibility commitment.
3. Keep standalone/bundle and public/local distributions separate. Do not activate competing variants together.
4. Have the user perform engine-dump and gameplay runs using the supplied protocol. Until then, blocked features remain blocked and no runtime compatibility claim is made.
5. Keep Workshop IDs, public IDs and translations unless an audited migration requires a change. Update supported-version metadata only after the corresponding package passes its tests.

## Scope of the next implementation

Start with the shared evidence and engine gates, then apply the ordered packages. This report is the completed preparation deliverable: every enumerated function has a specified work package or a concrete blocker and a resolution procedure. It is not a claim that all packages are already safe to release.

## Current export and example supplement

The subsequent [standalone MDC 1.077 static migration review](mods/mass-demand-conversion-static-migration.md) records retained Script/GUI interfaces, matching category/query/send bindings, count references and byte-identical old/new fixed-option widget. No necessary functional 1.20 mod patch is demonstrated. Engine option/default/validation behavior, actual GUI/delivery outcomes and delayed/list/multiplayer lifecycle remain open. No compatibility, bundle-port or metadata status is promoted.

The [engine registry](../reference/engine-reference.md), [43 separate contract cards](contracts/README.md) and [function/state guide](../workspace/function-contracts.md) reconcile the available 1.20.0.3 exports. [Completion boundary](../research/completion-report.md) distinguishes export success, structural checks and remaining semantic/runtime gates. The user-test [three-run manual](../examples/test-runs.md) uses separate playsets; do not use the Vanilla diagnostic starter for mod tests. Original update statuses remain unchanged.

## Subsequent repeatable update workflow — 2026-10-03

All eight retained distributions now have current maintenance instructions in their sheets and registered source watches. The new checker compares selected objects, their callers/dependencies, file-level contracts and native replacement assets; it does not refresh baselines or patch mods itself. The task instruction authorizes the agent to complete established corrections after the feature audit. Existing Engine/runtime gates and distribution exclusions remain. Historical 1.077 review statements above are retained as earlier findings, not the current MDC package state. See the [workflow verification](../research/mod-update-workflow-verification-20261003.md).

## Leave Wars standalone supplement — 2026-10-03

The [standalone implementation/audit](mods/leave-wars-update-20261003.md) and [static verification](evidence/leave-wars-verification-20261003.json) are current. The [selected baseline](update-watch-leave-wars-20261003.json) refreshes only Leave Wars and its audited dependencies; all other mod records and historical baselines are unchanged. [Runtime acceptance](mods/leave-wars-tests.md) remains not run. No bundle propagation, game/profile change or compatibility metadata bump occurred.

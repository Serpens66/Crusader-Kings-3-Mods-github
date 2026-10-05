# MC-VARIANTS contract card

## Scrollbox nominal-size correction and failed-layout ledger — 2026-10-05

[Current isolated correction](../mods/mass-demand-conversion-scroll-size-20261005.md) and [mandatory screenshot-backed failure ledger](../mods/mass-demand-conversion-gui-failures-20261005.md). Latest screenshot confirms filter placement but recipient viewport displacement. Native inherited100×100 size is now explicitly overridden514×210; no list/filter behavior change. 23 static tests pass; rendering remains untested. Read the ledger before further GUI changes.


## Git recipient-list restoration — 2026-10-05

[Current restoration and pending game matrix](../mods/mass-demand-conversion-git-targets-20261005.md): user reported first-open row overlap and continuing filter inset. Entire native-radio scrollbox subtree restored from Git a81d7f3; custom recipient template removed. Filter heading/columns now use explicit top-left parent/own anchors and x0/122/249/351 positions. 22 static checks pass; first-open/filter-change rendering remains untested. Version 1.079 and gameplay/texts/history retained.


## Explicit flexible-space alignment — 2026-10-05

[Current correction and pending game matrix](../mods/mass-demand-conversion-flex-alignment-20261005.md): latest screenshot disproves prior recipient centering and shows filter inset. Explicit 514×32 filter viewport/trailing expander and full-size recipient hbox/equal expanders replace anchor-only alignment. 22 static tests pass; actual rendering remains untested. Gameplay/texts/1.079 metadata, bundle and historical evidence are retained.


## Narrow filter row and centered recipient contents — 2026-10-05

[Current patch and pending runtime matrix](../mods/mass-demand-conversion-centered-options-20261005.md): 451-wide left-origin filters inside the existing 514-wide section; only recipient rows use a local native-derived button with centered radio/text content and full-width click regions. Screenshot confirms preceding list fits but is left-aligned and filters still overflow. All gameplay/texts/1.079 metadata and historical records remain; new rendering and MP are untested.


## Horizontal alignment correction — 2026-10-05

[Current layout contract and user observations](../mods/mass-demand-conversion-alignment-20261005.md): root native vertical flowcontainer, centered horizontal section wrappers, top|left zero-origin overlaid filter groups and unanchored filter columns. Recipient content/buttons expand; 450-wide rows fit the conservative native scroll-margin/scrollbar budget. Caption, state, controller/index/action bindings are unchanged. New rendering requires normal/high-scale game tests; no bundle or release metadata change.


## Compact widget correction — 2026-10-05

[Source audit, layout/lifecycle contract and runtime matrix](../mods/mass-demand-conversion-compact-widget-20261005.md): user-observed pre-patch rendering failures, fixed 514×250 widget/32-high filter row/210-high native scrollbox, trigger_on_create initialization and missing/unknown-state none fallback. Eleven entries/order and OnSelect routes preserved; bounded scrolling and creation/reopen synchronization require game tests. Bundle/version metadata remain unchanged.


## Standalone filter extension — 2026-10-05

[Current implementation/audit and fixed index map](../mods/mass-demand-conversion-chance-filter-20261005.md): standalone uses its own widget and eleven always-present native entries for five visible groups. Keep group on filter changes and filter on group changes; local UI state resets to none each opening, without a saved gameplay variable. Lifecycle/reset, entry order and MP are runtime gates. The bundle remains outside this authorized change; older byte-identical-widget findings below are historical.


Family: **Mass Demand Conversion**. Runtime: **not run**. Declaration status: **export declarations available**.

[Original intent, costs, mechanics, variants and tests](../mods/mass-demand-conversion.md) · [Behavior guide](../../workspace/function-contracts.md) · [2026-10-03 audit supplement](../mods/mass-demand-conversion-audit.md) · [Native test matrix](../mods/mass-demand-conversion-tests.md)

## Inputs, ownership and order

Decision root is requester; iterator this is candidate; entering root makes candidate available through prev at that caller.
Preview/count and dispatch must use the same category policy. Native query and dispatch initialization need separate tracing.

## Confirmed exported declarations

| Name | Kind | Scopes / targets / result as exported | Source |
|---|---|---|---|
| `run_interaction` | effect | none | [line 2654](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |

Unresolved discovery names: none from this curated selection. Missing names may have a different API owner/name; do not infer removal.

## Exact remaining gate

Port verified standalone behavior to bundle; keep categories scoped

Source-confirmed: standalone has five categories, bundle four; shared IDs are alternatives. Eight standalone languages contain tributary labels/tooltips; controller uses OnSelect/radio state. No port or compatibility promotion was performed. Matching query policy and verified context must precede bundle porting; UI and separate-playset tests remain open.

Current remaining gate: After MC gates: verify corresponding standalone/bundle routes and radio selection; retain distribution identity. Partial source audit only; gameplay/GUI/MP not run.

No blanket gate closure follows from an export hit. Read the current complete entry-point, callers, expanded helper arguments and dependencies before an implementation decision. Preserve absent-target and multiplayer cases.

## Source retrieval

Root `Mass Demand Conversion` has 12 read text/reference files. [Machine evidence](evidence.json) records every object boundary, saved scope, macro parameter, referenced state/event and native-definition candidate. These are retrieval records, not a typed call graph.

Use `Documentation/tools/lookup.py SYMBOL --context 4` for versioned declarations and current source uses. See the original sheet for exact original branch costs, callback sets and complete acceptance cases.

## Subsequent caller and Internet recheck (2026-10-03)

See the [follow-up research](../mods/mass-demand-conversion-recheck.md) for a current official developer explanation and native query/dispatch callers. General actor/puppet meaning and native requester/query patterns are now sourced; script-entry option/default/validation behavior remains narrower G01/G02 work. Earlier search failures are historical and do not establish absence of an explanation. All runtime statuses remain unchanged.

## Subsequent static migration review (2026-10-03)

The [standalone 1.077 review](../mods/mass-demand-conversion-static-migration.md) verifies five option IDs/count references, eight standalone languages, current GUI exports and byte-identical old/new/native fixed-option widget. That evidence supports no mandatory standalone GUI migration; rendering/context are untested. It does not certify or port the four-category bundle. Existing distribution identity, IDs and inactive notification experiment are retained. No metadata or runtime status promotion follows.

## Notification update 1.078 — 2026-10-03

[New notification audit and evidence](../mods/mass-demand-conversion-notifications-20261003.md): standalone metadata is now 1.078/1.20.* and its two native acceptance IDs are hidden priority-1 overrides using mdc_conversion_accepted_message. The completed source audit is limited to those notifications, their callers, previews, rewards and puppet notifier. The earlier full query/dispatch/lifecycle/GUI/MP gates remain open and gameplay remains **not run**. Candidate enumeration, all five categories, query/send bindings, option logic and count values are byte-preserved. The four-category bundle and its inactive experiment are untouched; no port is implied. Both native IDs affect all their callers, including manual requests; same-ID mod overrides can conflict. See MC-N01–MC-N11 in the updated test matrix. Historical static-migration and inactivity statements above describe the earlier 1.077 review.

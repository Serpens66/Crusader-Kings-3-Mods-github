# MC-CANDIDATES contract card

## Compact widget and zero-count gate — 2026-10-05

[Current patch and runtime matrix](../mods/mass-demand-conversion-compact-widget-20261005.md): missing GUI mode no longer hides the three unfiltered vassal/tributary rows. Counts/eligibility and send-time checks are unchanged. User-observed zero counts are not solved by a layout assertion: compare a manually eligible target at identical paused state; trace localization/actor/query context before changing rules. An 80% zero does not by itself prove eligibility failure.


## Standalone filter extension — 2026-10-05

[Current implementation/audit and pending tests](../mods/mass-demand-conversion-chance-filter-20261005.md): six additional counts use the same native threshold helper as send-time selection. Original five unfiltered counts and decision visibility are preserved. Preserve category guards and recheck each candidate before sending. Zero filtered candidates must show zero without hiding the open decision. Percentage parity with the native interaction UI is untested and remains a release gate.


Family: **Mass Demand Conversion**. Runtime: **not run**. Declaration status: **export declarations available**.

[Original intent, costs, mechanics, variants and tests](../mods/mass-demand-conversion.md) · [Behavior guide](../../workspace/function-contracts.md) · [2026-10-03 audit supplement](../mods/mass-demand-conversion-audit.md) · [Native test matrix](../mods/mass-demand-conversion-tests.md)

## Inputs, ownership and order

Decision root is requester; iterator this is candidate; entering root makes candidate available through prev at that caller.
Preview/count and dispatch must use the same category policy. Native query and dispatch initialization need separate tracing.

## Confirmed exported declarations

| Name | Kind | Scopes / targets / result as exported | Source |
|---|---|---|---|
| `every_courtier` | effect | character; character | [line 4499](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |
| `every_tributary` | effect | character; character | [line 5304](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |
| `is_character_interaction_potentially_accepted` | trigger | character | [line 5167](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/triggers.log.raw) |
| `is_character_interaction_valid` | trigger | character | [line 5190](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/triggers.log.raw) |

Unresolved discovery names: none from this curated selection. Missing names may have a different API owner/name; do not infer removal.

## Exact remaining gate

Query validity/context and count/send equality

Source-confirmed: five category routes and stronger indirect protection policy; native AI-ruler/house-ruler restrictions. Counts represent query-positive request candidates, not all converted family. At unchanged state count and execution candidate sets should match; a changed state requires re-evaluation. Default required response, full query validation and requester context remain G01/G02/G04.

Current remaining gate: G01/G02/G04: Engine query initialization/default response, validity/cooldown/pending checks and dynamic GUI/count/delivery context. Standalone textual category/actor/recipient and count-reference mapping is now statically checked; full feature audit unclosed; gameplay/GUI/MP not run.

No blanket gate closure follows from an export hit. Read the current complete entry-point, callers, expanded helper arguments and dependencies before an implementation decision. Preserve absent-target and multiplayer cases.

## Source retrieval

Root `Mass Demand Conversion` has 12 read text/reference files. [Machine evidence](evidence.json) records every object boundary, saved scope, macro parameter, referenced state/event and native-definition candidate. These are retrieval records, not a typed call graph.

Use `Documentation/tools/lookup.py SYMBOL --context 4` for versioned declarations and current source uses. See the original sheet for exact original branch costs, callback sets and complete acceptance cases.

## Subsequent caller and Internet recheck (2026-10-03)

See the [follow-up research](../mods/mass-demand-conversion-recheck.md) for a current official developer explanation and native query/dispatch callers. General actor/puppet meaning and native requester/query patterns are now sourced; script-entry option/default/validation behavior remains narrower G01/G02 work. Earlier search failures are historical and do not establish absence of an explanation. All runtime statuses remain unchanged.

## Subsequent static migration review (2026-10-03)

[Review and new evidence](../mods/mass-demand-conversion-static-migration.md): five standalone category routes, query requester/recipient bindings and selected protection/indirect guards agree across visibility/count/send. Eight languages reference the five defined values. G04 textual mappings are checked, not dynamic candidate equality. All relevant iterator/contract/query exports remain present. No mandatory 1.20 candidate rewrite is demonstrated. The stronger protection policy is retained; runtime and full audit status are not promoted.

## Notification update 1.078 — 2026-10-03

[New notification audit and evidence](../mods/mass-demand-conversion-notifications-20261003.md): standalone metadata is now 1.078/1.20.* and its two native acceptance IDs are hidden priority-1 overrides using mdc_conversion_accepted_message. The completed source audit is limited to those notifications, their callers, previews, rewards and puppet notifier. The earlier full query/dispatch/lifecycle/GUI/MP gates remain open and gameplay remains **not run**. Candidate enumeration, all five categories, query/send bindings, option logic and count values are byte-preserved. The four-category bundle and its inactive experiment are untouched; no port is implied. Both native IDs affect all their callers, including manual requests; same-ID mod overrides can conflict. See MC-N01–MC-N11 in the updated test matrix. Historical static-migration and inactivity statements above describe the earlier 1.077 review.

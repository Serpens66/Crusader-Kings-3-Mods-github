# MC-CANDIDATES contract card

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

Current remaining gate: G01/G02/G04: query initialization/default response, validity/cooldown/pending checks and snapshot count context. Partial source audit only; gameplay/GUI/MP not run.

No blanket gate closure follows from an export hit. Read the current complete entry-point, callers, expanded helper arguments and dependencies before an implementation decision. Preserve absent-target and multiplayer cases.

## Source retrieval

Root `Mass Demand Conversion` has 12 read text/reference files. [Machine evidence](evidence.json) records every object boundary, saved scope, macro parameter, referenced state/event and native-definition candidate. These are retrieval records, not a typed call graph.

Use `Documentation/tools/lookup.py SYMBOL --context 4` for versioned declarations and current source uses. See the original sheet for exact original branch costs, callback sets and complete acceptance cases.

## Subsequent caller and Internet recheck (2026-10-03)

See the [follow-up research](../mods/mass-demand-conversion-recheck.md) for a current official developer explanation and native query/dispatch callers. General actor/puppet meaning and native requester/query patterns are now sourced; script-entry option/default/validation behavior remains narrower G01/G02 work. Earlier search failures are historical and do not establish absence of an explanation. All runtime statuses remain unchanged.

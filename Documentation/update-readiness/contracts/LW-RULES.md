# LW-RULES contract card

Family: **Leave Wars**. Runtime: **not run**. Declaration status: **export declarations available**.

[Original intent, costs, mechanics, variants and tests](../mods/leave-wars.md) · [Behavior guide](../../workspace/function-contracts.md)

## Inputs, ownership and order

Interaction actor is withdrawing secondary participant; recipient is leader; selected war is saved for event selection.
Ten slots and original costs are the policy. Event branches touch actor, war, leader and receiver contexts separately.

## Confirmed exported declarations

| Name | Kind | Scopes / targets / result as exported | Source |
|---|---|---|---|
| `remove_short_term_gold` | effect | character | [line 9894](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |
| `highest_held_title_tier` | saved_target | See raw export fields; no invented type | [line 2198](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/event_targets.log.raw) |
| `highest_held_title_tier` | trigger | character | [line 4850](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/triggers.log.raw) |

Unresolved discovery names: none from this curated selection. Missing names may have a different API owner/name; do not infer removal.

## Exact remaining gate

Rule arithmetic verified; accounting/duplicates need current engine tests

Recheck ended/changed wars, same-side membership, player leadership, accounting, alliance effects and saved-scope cleanup.

No blanket gate closure follows from an export hit. Read the current complete entry-point, callers, expanded helper arguments and dependencies before an implementation decision. Preserve absent-target and multiplayer cases.

## Source retrieval

Root `Leave Wars` has 15 read text/reference files. [Machine evidence](evidence.json) records every object boundary, saved scope, macro parameter, referenced state/event and native-definition candidate. These are retrieval records, not a typed call graph.

Use `Documentation/tools/lookup.py SYMBOL --context 4` for versioned declarations and current source uses. See the original sheet for exact original branch costs, callback sets and complete acceptance cases.

# LW-SELECT contract card

Family: **Leave Wars**. Runtime: **not run**. Declaration status: **mixed; missing names are not proof of unsupported API**.

[Original intent, costs, mechanics, variants and tests](../mods/leave-wars.md) · [Behavior guide](../../workspace/function-contracts.md)

## Inputs, ownership and order

Interaction actor is withdrawing secondary participant; recipient is leader; selected war is saved for event selection.
Ten slots and original costs are the policy. Event branches touch actor, war, leader and receiver contexts separately.

## Confirmed exported declarations

| Name | Kind | Scopes / targets / result as exported | Source |
|---|---|---|---|
| `save_scope_as` | effect | none | [line 2675](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |
| `trigger_event` | effect | none | [line 2908](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |
| `is_participant` | trigger | war | [line 11045](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/triggers.log.raw) |

Unresolved discovery names: `is_primary_war_attacker`, `is_primary_war_defender`. Missing names may have a different API owner/name; do not infer removal.

## Exact remaining gate

War predicates, saved context and selection-time revalidation

Recheck ended/changed wars, same-side membership, player leadership, accounting, alliance effects and saved-scope cleanup.

No blanket gate closure follows from an export hit. Read the current complete entry-point, callers, expanded helper arguments and dependencies before an implementation decision. Preserve absent-target and multiplayer cases.

## Source retrieval

Root `Leave Wars` has 15 read text/reference files. [Machine evidence](evidence.json) records every object boundary, saved scope, macro parameter, referenced state/event and native-definition candidate. These are retrieval records, not a typed call graph.

Use `Documentation/tools/lookup.py SYMBOL --context 4` for versioned declarations and current source uses. See the original sheet for exact original branch costs, callback sets and complete acceptance cases.

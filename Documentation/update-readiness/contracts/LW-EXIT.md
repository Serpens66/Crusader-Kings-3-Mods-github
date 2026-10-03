# LW-EXIT contract card

Family: **Leave Wars**. Runtime: **not run**. Declaration status: **export declarations available**.

[Original intent, costs, mechanics, variants and tests](../mods/leave-wars.md) · [Behavior guide](../../workspace/function-contracts.md)

## Inputs, ownership and order

Interaction actor is withdrawing secondary participant; recipient is leader; selected war is saved for event selection.
Ten slots and original costs are the policy. Event branches touch actor, war, leader and receiver contexts separately.

## Confirmed exported declarations

| Name | Kind | Scopes / targets / result as exported | Source |
|---|---|---|---|
| `clear_saved_scope` | effect | none | [line 243](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |
| `add_prestige` | effect | character | [line 3200](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |
| `add_prestige_experience` | effect | character | [line 3210](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |
| `pay_short_term_gold` | effect | character | [line 8142](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |
| `remove_participant` | effect | war; character | [line 15804](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |

Unresolved discovery names: none from this curated selection. Missing names may have a different API owner/name; do not infer removal.

## Exact remaining gate

Removal/cleanup/alliance/payment/experience contracts

Recheck ended/changed wars, same-side membership, player leadership, accounting, alliance effects and saved-scope cleanup.

No blanket gate closure follows from an export hit. Read the current complete entry-point, callers, expanded helper arguments and dependencies before an implementation decision. Preserve absent-target and multiplayer cases.

## Source retrieval

Root `Leave Wars` has 15 read text/reference files. [Machine evidence](evidence.json) records every object boundary, saved scope, macro parameter, referenced state/event and native-definition candidate. These are retrieval records, not a typed call graph.

Use `Documentation/tools/lookup.py SYMBOL --context 4` for versioned declarations and current source uses. See the original sheet for exact original branch costs, callback sets and complete acceptance cases.

## Standalone implementation reconciliation — 2026-10-03

Source closure: current war-root removal, scope clear, character payment/prestige/experience/alliance declarations and native callers/hooks audited. All original branch effects are preserved behind the live permission/funds guard. Matching promise cleanup and selected-war Frankokratia membership cleanup are implemented; native alliance callbacks remain delegated. Arbitrary engine/lifecycle/accounting/notification behavior is not inferred from a signature. LW-T05–LW-T11 and LW-T14–LW-T19 remain open.

[Current audit and implementation](../mods/leave-wars-update-20261003.md) · [Pending runtime cases](../mods/leave-wars-tests.md). Original evidence.json and raw export intake remain historical records; source/static checks do not certify runtime compatibility.

# MC-CANDIDATES contract card

Family: **Mass Demand Conversion**. Runtime: **not run**. Declaration status: **export declarations available**.

[Original intent, costs, mechanics, variants and tests](../mods/mass-demand-conversion.md) · [Behavior guide](../../workspace/function-contracts.md)

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

Actor/puppet/redirect setup, duplicate memberships, protection/authority/rite rules, consent and native consequences require full branch audit and tests.

No blanket gate closure follows from an export hit. Read the current complete entry-point, callers, expanded helper arguments and dependencies before an implementation decision. Preserve absent-target and multiplayer cases.

## Source retrieval

Root `Mass Demand Conversion` has 12 read text/reference files. [Machine evidence](evidence.json) records every object boundary, saved scope, macro parameter, referenced state/event and native-definition candidate. These are retrieval records, not a typed call graph.

Use `Documentation/tools/lookup.py SYMBOL --context 4` for versioned declarations and current source uses. See the original sheet for exact original branch costs, callback sets and complete acceptance cases.

# SA-COURT contract card

Family: **SerpAlerts**. Runtime: **not run**. Declaration status: **export declarations available**.

[Original intent, costs, mechanics, variants and tests](../mods/serp-alerts.md) · [Behavior guide](../../workspace/function-contracts.md)

## Inputs, ownership and order

Important-action creation starts in player context; on-action callbacks supply their own guaranteed and optional targets.
UI-only discovery/click must be distinguished from synchronized state mutation. Recipient lists are built per callback and side.

## Confirmed exported declarations

| Name | Kind | Scopes / targets / result as exported | Source |
|---|---|---|---|
| `send_interface_message` | effect | character | [line 9999](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/effects.log.raw) |
| `on_leave_court` | on_action | See raw export fields; no invented type | [line 569](../../update-readiness/runtime-evidence/20261003T005950.086458Z/script-docs/on_actions.log.raw) |

Unresolved discovery names: none from this curated selection. Missing names may have a different API owner/name; do not infer removal.

## Exact remaining gate

Old employer validity, current message delivery duplicates

Selected-war context, optional killer/employer, relationship overlap, message duplication and per-player delivery remain behavioral gates.

No blanket gate closure follows from an export hit. Read the current complete entry-point, callers, expanded helper arguments and dependencies before an implementation decision. Preserve absent-target and multiplayer cases.

## Source retrieval

Root `SerpAlerts` has 12 read text/reference files. [Machine evidence](evidence.json) records every object boundary, saved scope, macro parameter, referenced state/event and native-definition candidate. These are retrieval records, not a typed call graph.

Use `Documentation/tools/lookup.py SYMBOL --context 4` for versioned declarations and current source uses. See the original sheet for exact original branch costs, callback sets and complete acceptance cases.

# CD-LOBBY contract card

Family: **CustomDefines**. Runtime: **not run**. Declaration status: **export declarations available**.

[Original intent, costs, mechanics, variants and tests](../mods/custom-defines.md) · [Behavior guide](../../workspace/function-contracts.md)

## Inputs, ownership and order

GUI-selected character/player or namespace/key loader; no universal character root for defines.
Retain original numeric settings; distinguish nested GUI overrides from whole-path files and embedded knight state.

## Confirmed exported declarations

| Name | Kind | Scopes / targets / result as exported | Source |
|---|---|---|---|
| `LobbyView.CanTryStartRulerDesigning` | datatype | bool | [line 3091](../../update-readiness/runtime-evidence/20261003T112558.279918Z/main-menu-data-types/data_types/data_types_gui.txt.raw) |
| `TryStartRulerDesigning` | datatype | void | [line 3409](../../update-readiness/runtime-evidence/20261003T112558.279918Z/main-menu-data-types/data_types/data_types_uncategorized.txt.raw) |

Unresolved discovery names: none from this curated selection. Missing names may have a different API owner/name; do not infer removal.

## Exact remaining gate

Designer overloads and engine post-start permission

Native loader precedence, designer permissions, rendered values and combat/renown numerical outcomes remain test/audit gates.

No blanket gate closure follows from an export hit. Read the current complete entry-point, callers, expanded helper arguments and dependencies before an implementation decision. Preserve absent-target and multiplayer cases.

## Source retrieval

Root `CustomDefines` has 20 read text/reference files. [Machine evidence](evidence.json) records every object boundary, saved scope, macro parameter, referenced state/event and native-definition candidate. These are retrieval records, not a typed call graph.

Use `Documentation/tools/lookup.py SYMBOL --context 4` for versioned declarations and current source uses. See the original sheet for exact original branch costs, callback sets and complete acceptance cases.

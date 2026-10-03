# Scopes and block contracts

Evidence: [Scopes](../research/sources.md), native decision/interaction/event references, `common/on_action/_on_actions.info`, Vanilla `birthday.txt`, `00_gift.txt`, `00_character.txt`, and their callers listed in [audit findings](../research/vanilla-audit.md).

## Model scopes as typed references

A scope selects an object or value for a script operation. Characters, landed titles, provinces, cultures, faiths, rites, dynasties, houses, wars and activities have different APIs. A county title and its province are different objects. Knowing an object's display name does not identify its script type.

Entering a scope block changes the current object for that block. Returning past its closing brace restores the containing context. Event-target chains follow relationships; database prefixes look up a known ID; provided or saved names use `scope:`.

```text
# Character-scoped effect. The guard prevents using a missing liege.
if = {
    limit = { exists = liege }
    liege = {
        save_scope_as = doc_liege
    }
}
```

`liege` is a relationship from a character, `title:k_france` is a database lookup, and `scope:doc_liege` is a saved name. These are three different mechanisms. Do not put `scope:` in front of an arbitrary database ID. Runtime character IDs are not reliable permanent IDs for content shared across saves.

## `root`, `this`, `prev`

| Reference | Meaning | Mistake to avoid |
|---|---|---|
| `root` | Initial scope provided by this block's contract, if one exists | Assuming it always means the local player or a character |
| `this` | Current scope | Treating it as the original caller after entering another object |
| `prev` | Previous scope in the scope stack | Counting every brace as a scope switch, or inventing `prevprev` |
| `scope:actor` | Interaction actor where provided | Assuming all unrelated callbacks provide it |
| `scope:recipient` | Interaction recipient where provided | Confusing it with the event receiver after an event is sent |

Logic and schema blocks do not necessarily push an object onto the scope stack. Draw the typed chain explicitly for nested loops. Prefer a saved name for an important object over a complicated sequence of `prev` transitions.

```text
# Character-scoped effect: children receive the operation, not their parent.
save_scope_as = doc_parent
every_child = {
    limit = { is_alive = yes }
    # Here this = child; scope:doc_parent = original character.
    add_gold = 1
}
```

The script is illustrative; it creates gold. To transfer money, use an audited payment effect and its budget rules.

## Contracts that are locally documented

| Entry point | Starting context | Additional information |
|---|---|---|
| Decision eligibility/effect | Character taking/evaluating decision | Some decision widgets have different actor contexts; read their own comments |
| Default character event | Receiving character | `scope = ...` can override the event scope |
| Interaction `is_available` | `root` is the actor | Native 1.20 reference recommends this for actor-only availability checks |
| Interaction `is_shown`, `is_valid` | Provided actor/recipient references | Enter `scope:actor`/`scope:recipient` explicitly for character operations |
| Interaction outcome effects | Provided interaction scopes | Do not assume a universal implicit character root |
| `on_birthday` | Birthday character | Native comments say this runs after age increases |
| `yearly_global_pulse` | No root in the developer reference | Select appropriate objects yourself; avoid a broad expensive scan by default |
| Scripted GUI declaring `scope = character` | Character root supplied by the GUI invocation | The GUI builds the context with `GuiScope.SetRoot(...)` |
| Travel point-of-interest `on_visit` | Travelling character | `scope:province` is the visited province |
| Travel point-of-interest `on_added`/`on_removed` | Province | The reference explicitly restricts the operation to local province effects |

For a new callback, identify all input types, who creates the chain, which named scopes are guaranteed, and which are optional. Also inspect AI, preview and actual execution callers: they can supply different information.

## Saved scopes and lifetime

`save_scope_as = doc_target` names the current scope for the event/effect chain. `save_temporary_scope_as` is used for shorter-lived selection, including trigger evaluation. A saved name is not a permanent field on an object. Saving the same name again changes its binding.

The Wiki describes propagation along an unbroken effect chain. Treat the exact boundary as a contract to verify for the actual caller, especially queued events, GUI calls and on actions. An on action's `effect` and its listed events do **not** share a newly created chain-local setup: the native `.info` file explicitly warns that scopes/local variables set in that effect do not carry into independently dispatched events.

When state must survive independently, store a variable on the relevant object and guard its later use. Persistent variables holding object references do not freeze that object's game state or prevent its removal. See [state](state-and-values.md).

## Missing objects and tooltip evaluation

An ordinary sequence of eligibility checks may stop when a check fails. Tooltip rendering can evaluate more conditions to explain failures. Thus `exists = liege` on one line is not a universal guard for a later arbitrary dereference in a displayed block.

```text
# Trigger fragment: absence of the required liege must be a failure.
trigger_if = {
    limit = { exists = liege }
    liege = { is_alive = yes }
}
trigger_else = { always = no }
```

This is preferable to an optional comparison if the game rule requires a liege. For an optional feature, decide whether absence should skip the behavior, fail eligibility or select a fallback. Never infer that product behavior from `?=` alone.

## Scope-audit checklist

For each operation, record current type, target type, source of each name, lifetime and absence behavior. For a helper, expand its parameters mentally and trace its nested scopes. For a loop, write its input and output types. For a GUI, compare the root used by `IsShown`, `IsValid` and `Execute`. Tests must include the absent target case and a second player if the feature stores per-player choices.

## Installed 1.20.0.3 export supplement

The [current engine reference](../reference/engine-reference.md) now indexes six script and five data-type exports with exact raw line ranges and checksums. Historical statements above about absent generated dumps describe the initial research stage. Use [lookup](../tools/lookup.py) for both engine declarations and existing local definitions/callers. Missing optionality, argument types, scope lifetime, permissions and multiplayer routing remain unknown where the export does not specify them.

See [workspace function contracts](../workspace/function-contracts.md) for owner/caller/state distinctions and [isolated tests](../examples/test-runs.md) for runtime acceptance. The user completed export sessions, but no example gameplay/GUI/MP tests have been performed.

## General Crozier source supplement — 2026-10-03

Puppet interactions distinguish actor, effective actor and puppeteer; puppet decisions have a different root. See [Puppets and selection](../systems/puppets-and-selection.md). Several on-action exports say `none` while native headers document a character/title root; see the explicit discrepancies in [lifecycle contracts](../systems/crozier-migration.md).

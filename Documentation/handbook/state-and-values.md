# Variables, lists and script values

Evidence: [Variables, Lists and Script values](../research/sources.md), native `common/script_values/_script_values.info`, `common/on_action/_on_actions.info`, and current scripted helper uses indexed in [commands](../reference/commands.md).

## Select storage by owner and lifetime

| Storage | Owner/lifetime | Suitable use |
|---|---|---|
| `scope:doc_target` | Effect/event chain | Pass a selected object along a verified chain |
| Temporary saved scope/value | Current evaluation/block contract | Cache a selection or calculation briefly |
| `var:doc_score` | Current game object | Per-character or per-object persistent state |
| `global_var:doc_setting` | Shared game state | A genuinely global rule or marker |
| `local_var:doc_value` | Temporary top-scope context | Local chain computation where its propagation is verified |
| Named script value | Definition, evaluated when used | A reusable number or formula |
| Variable list | Object-owned list | Retain references to multiple objects |

Do not store independent player preferences in a global variable. The Knight Manager variants illustrate character-owned flags; the older global loaded marker represents a shared mod-presence convention, not a player's choice.

## Object variables

```text
# Character-scoped effects.
set_variable = { name = doc_score value = 3 }
change_variable = { name = doc_score add = 1 }

# Trigger fragment on the same owner.
has_variable = doc_score
var:doc_score >= 4

# Cleanup effect on that owner.
remove_variable = doc_score
```

The owner matters: entering `liege` and reading `var:doc_score` reads the liege's value, not the previous character's value. Guard before accessing optional variables, especially in displayed conditions. Store numbers, booleans, symbolic values or object references only where the API supports their type. A reference points to an object; it does not make a snapshot of that object's properties.

Timed variables use duration fields in current Vanilla. Audit whether setting an already-existing variable refreshes expiry for the chosen operation. Remove temporary persistent state when no longer needed. When a delayed action can fail, provide expiry or cleanup so eligibility is not blocked forever.

`has_character_flag`/`add_character_flag`/`remove_character_flag` are convenient character-state operations. Do not confuse a character flag with `flag:some_symbol`, which is a symbolic argument value. The broad cleanup semantics on death, object destruction and chain end are version-sensitive; verify the specific storage mechanism rather than relying on a general claim that every variable disappears at a particular moment.

## Script values are calculations

Named definitions belong in `common/script_values`. A constant can be a scalar. A formula uses braces. The native developer reference documents arithmetic order, inlining, scope chaining, ranges and supported lists.

```text
doc_reward_value = 2
doc_scaled_reward_value = {
    value = 2
    multiply = 3
    max = 5
    add = 1
}
```

The second formula evaluates to 6: multiply to 6, cap at 5, then add 1. In this reader `max` is an upper cap, `min` a lower floor. This is easy to mistake for choosing the larger/smaller of two values. Start with explicit `value` when it improves clarity. Operations execute in written order; formulas are not ordinary algebraic expressions with implicit precedence.

Arithmetic includes `add`, `subtract`, `multiply`, `divide`, `modulo`, rounding operations and conditional branches. Guard division by zero. `fixed_range` and `integer_range` are numeric-range operations; do not confuse their `min`/`max` endpoints with the formula's clamping operations.

## Scope-dependent formulas

```text
doc_child_count_value = {
    value = 0
    every_child = {
        limit = { is_alive = yes }
        add = 1
    }
}
```

This illustrative formula requires a character scope and counts eligible children. A province caller does not provide the same list. Nested formula scope switches change available reads, while the surrounding calculation accumulates values. Use `every_`/`ordered_` forms documented for formulas; an old developer schematic using `any_child` as numeric accumulation conflicts with the dedicated Wiki guide and should not be copied without a runtime check.

Script values can reference other named values and numeric reads accepted by the reader. Complex trigger-as-number expressions may require quoted inline syntax. Obtain the exact signature from current dumps before using one. Script values calculate; do not place persistent state-changing effects inside them.

## Evaluate once when consistency matters

A formula can be reevaluated each time it is used. If it depends on mutable wealth, candidate lists or random ranges, separately computing a preview, a payment and a reward can produce different results. Decide whether to calculate a single transaction amount, save it temporarily, then reuse it in that operation. Do not cache a result across an eligibility change unless that is intentional behavior.

GUI script values may be evaluated frequently. Prefer cheap formulas. If a cached persistent value is necessary, define when it updates and how it is initialized and cleaned up. A stale cache can be a correctness bug as well as a performance tradeoff.

## Persistent data as a compatibility interface

Renaming a saved variable or changing its type can break old saves and companion mods. For a stateful feature, specify an initialization marker/version, defaults for absent data and a migration or reset path if required. This collection does not invent a universal save migration protocol; choose one for the actual feature.

Test first invocation, repeated invocation, absent state, zero/negative values, owner change, save/reload and expiry. For an object reference, also test the referenced object becoming invalid.

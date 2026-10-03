# Conditions, iteration, randomness and scripted helpers

Evidence: [Triggers, Effects, Lists, Weight modifier](../research/sources.md); native `birthday.txt`, `00_activity_triggers.txt`, `00_accolades_scripted_effects.txt`, `00_scripted_lists.txt`, and [audit records](../research/vanilla-audit.md).

## Conditional effects versus conditional triggers

In an effect block, use `if`, `else_if`, `else`; the condition is under `limit`. The selected branch executes its effects in sequence. In a trigger block, use `trigger_if`, `trigger_else_if`, `trigger_else` to conditionally evaluate requirements. Define an explicit failing fallback when the guarded condition is required.

```text
# Character effect fragment.
if = {
    limit = { has_variable = doc_score }
    change_variable = { name = doc_score add = 1 }
}
else = {
    set_variable = { name = doc_score value = 1 }
}
```

A branch guard does not create the state that it checks. A trigger branch does not execute gameplay effects. Keep the condition close to the behavior it protects.

## Iterator families

| Form | Typical context | Purpose |
|---|---|---|
| `any_child` | Trigger | Test candidates against requirements |
| `every_child` | Effect or supported formula | Iterate eligible candidates |
| `random_child` | Effect | Select one eligible candidate |
| `ordered_child` | Effect or supported formula | Select/process ordered candidates |

These suffixes denote specific engine lists. Do not invent a suffix because a relationship sounds plausible. Use command documentation to verify input and output scopes. Effect iterators normally filter with `limit`; trigger `any_...` predicates contain their conditions directly. Count/percent/all parameters and list-specific controls need the relevant list contract.

```text
# Trigger fragment.
any_child = { is_adult = yes }

# Separate effect fragment.
every_child = {
    limit = { is_adult = yes }
    add_gold = 1
}
```

When the list is empty, the effect has no candidate to act on. Do not assume a selection saved inside `random_...` or `ordered_...` succeeded; guard the saved result. For mandatory all-member logic, explicitly test empty sets and the current iterator's counting semantics.

## Ordered and custom lists

Ordered selection uses fields such as `order_by`, `max` and potentially minimum/position controls. Inspect a current Vanilla selection with the same objective and verify whether high or low values are selected first. Native accolade effects use a negative multiplier to choose low-development counties; blindly reversing the sign changes the selected target.

`common/scripted_lists` defines reusable candidate restrictions. Native `powerful_vassal` uses `base = vassal` and `conditions = { is_powerful_vassal = yes }`. A list definition is not a mutation loop.

Chain lists are populated with list effects and accessed with forms such as `every_in_list = { list = doc_targets ... }`. Variable lists are stored on an object and use a different selector (`variable = ...`). Do not assume chain lists survive save/load or that a list populated in an on action effect reaches separately listed events. Duplicate entries and member invalidation require testing for the actual list API.

## Randomness and weights

`random = { chance = ... ... }` is a probabilistic gate. `random_list` associates relative weights with candidate branches. A weight of 100 is not itself a 100% occurrence probability. Conditions can exclude candidates; weight modifiers alter probabilities. Native `birthday.txt` provides both chance formulas and weighted branches.

```text
# Effect fragment; intentionally creates resources for illustration.
random_list = {
    1 = { add_gold = 1 }
    3 = { add_gold = 2 }
}
```

For AI-style weight blocks, `base` initializes a weight, `modifier` contains conditions plus adjustments, `add` changes it additively and `factor` scales it. Numeric formula `multiply` is a different reader. Review modifiers in source order. Check a zero-valid-candidate case and avoid relying on a random outcome as the only way an essential chain progresses.

## Reusable scripted triggers/effects

Place condition helpers in `common/scripted_triggers`, mutation helpers in `common/scripted_effects`. The helper's identifier is a public object name. Prefix it and document its caller contract. A simple helper is invoked with a yes/no-style argument where supported. A parameterized helper accepts named substitution values.

```text
# common/scripted_effects/doc_effects.txt
doc_grant_gold_effect = {
    # Caller must supply a character scope and a numeric AMOUNT.
    add_gold = $AMOUNT$
}

# In a character effect block:
doc_grant_gold_effect = { AMOUNT = 2 }
```

The parameters are literal text substitution, not typed function arguments evaluated by a conventional language runtime. Native examples substitute into values, identifiers and target chains. Missing parameters, unexpected token forms or an object of the wrong scope type can create invalid expanded script. Treat the helper's parameters as an interface: required names, allowed argument forms, input scope, provided scopes and state changes.

A scripted trigger should answer a question without persistent mutation. Scope-saving in selection triggers exists, but its lifetime and evaluation behavior must be audited; do not let tooltip rendering or repeated AI checks change player state.

## Performance and determinism

Prefer existing event hooks and bounded relevant-object lists over repeated world scans. Put inexpensive restrictive conditions before expensive checks where evaluation permits early exit. Do not recalculate large formulas in a GUI every frame. Use object-owned state for independent player preferences, and do not choose the local UI player inside synchronized gameplay code.

Static evidence alone does not establish multiplayer determinism, loop ordering stability or cost at world scale. Test those explicitly for a new gameplay feature.

## Installed 1.20.0.3 export supplement

The [current engine reference](../reference/engine-reference.md) now indexes six script and five data-type exports with exact raw line ranges and checksums. Historical statements above about absent generated dumps describe the initial research stage. Use [lookup](../tools/lookup.py) for both engine declarations and existing local definitions/callers. Missing optionality, argument types, scope lifetime, permissions and multiplayer routing remain unknown where the export does not specify them.

See [workspace function contracts](../workspace/function-contracts.md) for owner/caller/state distinctions and [isolated tests](../examples/test-runs.md) for runtime acceptance. The user completed export sessions, but no example gameplay/GUI/MP tests have been performed.

## Complete Wiki and legacy reader supplement

The [57-page reconciliation](../research/jesec-wiki-coverage.md) reinforces historical weight macros versus numeric formulas. [Legacy contracts](../systems/dynasty-legacies.md) show separate visibility and pick triggers, dynasty/dynast scope transitions and initialization-phase restrictions. A scripted helper legal in a perk AI formula is not automatically legal while parsing a track visibility definition.

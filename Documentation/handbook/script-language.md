# Script language: syntax and execution contexts

Evidence: [Scripting and Trigger sources](../research/sources.md), native `events/_events.info`, `common/decisions/_decisions.info`, `common/character_interactions/_character_interactions.info`, `common/script_values/_script_values.info`; [audited boundaries](../research/vanilla-audit.md). Examples here are fragments unless stated otherwise.

## The parser is only the first layer

CK3 uses Paradox's script language, commonly called Jomini script. Clausewitz is the engine; a third-party library called Jomini is a separate project. The text grammar is shared across many files, but their readers interpret keys differently. A well-bracketed file can still be invalid because its directory, database schema, scope or execution context is wrong.

Typical statements are `key = value` and `key = { ... }`. Braces delimit blocks, whitespace separates tokens, and `#` introduces a comment outside a quoted string. Use ordinary straight quotes. Preserve the spelling of identifiers from the authoritative source. Indentation expresses nesting for readers rather than controlling gameplay.

```text
# This is a trigger fragment in character scope.
is_alive = yes
gold >= 25
OR = {
    is_adult = yes
    has_trait = brave
}
```

Files can also contain bare lists (`events = { my_mod.0001 my_mod.0002 }`), repeated keys, color tuples and named definitions. They are not JSON dictionaries. Repeated `option`, `modifier`, `doctrine` or `type` entries can be meaningful. Do not round-trip script through a generic dictionary parser that silently keeps only the last entry.

## Values and symbols

| Form | Meaning to check |
|---|---|
| `yes`, `no` | Boolean argument where that field accepts one |
| `25`, `0.5`, `-10` | Numeric value; precision and range depend on the receiving field |
| `doc_reward_value` | Named script value if the field accepts script values |
| `brave` | Database key where a trait is expected |
| `scope:recipient` | Saved/provided scope reference |
| `var:doc_score` | Variable on the current object |
| `flag:doc_choice` | Symbolic value, distinct from setting a character flag |
| `"gfx/interface/...dds"` | Quoted string/path in a field accepting it |
| `1066.9.15` | Date syntax in a history/date reader, not generic arithmetic |
| `$TARGET$` | Text substitution placeholder inside a parameterized scripted helper |
| `@some_constant` | File/script constant convention; inspect local examples before choosing its declaration/use context |

Whether a value is a string, an object key or a localization key comes from the schema. Avoid arbitrary quotation and conversion rules derived from another Paradox game.

## Four contexts that look similar

**Definition/schema context** describes a database object: a decision's `picture`, an event's `type`, an interaction's `category`. Such fields are not effects.

**Trigger context** answers a question. It appears in event `trigger`, decision `is_valid`, an effect's `limit`, or a scripted trigger. A numeric comparison reads state; it does not assign state. `gold = 25` in an applicable trigger compares gold. It does not grant 25 gold.

**Effect context** executes operations such as `add_gold`, `set_variable` or `trigger_event`. Decision `effect`, event `immediate` and an interaction's `on_accept` are examples. Order matters for state changes.

**Numeric/weight context** calculates a number. Script values use `value`, `add`, `multiply`, and related operations; AI weights often use `base`, `modifier`, `add` and `factor`. They are separate readers. Do not paste an effect or weight block into a formula because the braces look the same.

```text
# Effect fragment, character scope.
if = {
    limit = { gold >= 25 }  # trigger context nested inside effect context
    add_gold = -25         # state change; choose payment-specific effects for real transfers
}
```

## Comparisons and logic

The commonly used numeric operators are `=`, `!=`, `<`, `<=`, `>` and `>=`, where the trigger supports comparison. Equality between object references compares identity, not names. Scope switching uses `target = { ... }`; comparison uses `target = other_target`. Read both sides and the enclosing reader.

Ordinary trigger blocks combine requirements. Use `OR` for alternatives and explicit nested logic to make meaning clear. `NOR` rejects any matching alternative; `NAND` rejects the case where all requirements match. Use `NOT` with a single condition or a clearly grouped expression. Test multi-child `NOT` with the current engine rather than assuming semantics from another programming language or trusting contradictory summaries.

`?=` is encountered in Vanilla for optional references. It avoids an invalid left-hand lookup in supported contexts. It does not establish that a right-hand reference exists, prove eligibility, or replace all guards. A skipped optional branch may be inappropriate for a mandatory condition. Use explicit `exists`, conditional triggers and a negative fallback when absence must fail the requirement. See [scopes](scopes.md).

## Text is a separate language layer

Localization `.yml` files use their own loader and strings. GUI `.gui` files combine widget definitions with bracketed data-binding expressions. A `$...$` token in localization is not a scripted-helper parameter; `[GetPlayer...]` is not a gameplay effect. These interfaces are connected through defined context objects, not by sharing all language operations.

## Errors worth preventing at authoring time

- Correct grammar in the wrong directory: the intended database never loads the file.
- An effect placed under `trigger`, or a trigger used as though it mutates state.
- A character operation executed after entering a culture, title, province or war scope.
- An absent target accessed in a tooltip where evaluation differs from a fast eligibility check.
- Duplicate event IDs or unprefixed helper identifiers shared with another mod.
- Syntax copied from CK2, another Jomini game or an older CK3 schema.
- A text editor removing the BOM or changing line endings of existing source files.

Use a locally observed definition and an actual caller as the starting point, then inspect the reader's `.info` file and generated command documentation. [Workflow](development-workflow.md) describes the full audit sequence.

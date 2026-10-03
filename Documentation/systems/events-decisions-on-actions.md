# Events, decisions and on actions

Primary contracts: native `events/_events.info` (430 lines), `common/decisions/_decisions.info` (377 lines), `common/on_action/_on_actions.info` (149 lines). See [audit evidence](../research/vanilla-audit.md) and [internet sources](../research/sources.md).

## Events: definition and delivery

An event file declares a namespace and defines namespaced IDs. Current native documentation puts the event type inside the event, with `character_event` as the documented default. Scope override, window selection, hidden events, themes, portraits, cooldowns, descriptions, options and widgets have separate fields.

```text
namespace = doc_demo
doc_demo.0001 = {
    type = character_event
    hidden = yes
    trigger = { is_alive = yes }
    immediate = { add_gold = 1 }
}
```

This is a minimal teaching event, not a passive scheduler. An event definition needs a caller: an effect, an on action or another audited dispatch path. Use `trigger_event` on the intended receiving scope. The top-level `trigger` restricts eligibility; it is not an automatic periodic execution loop.

For visible events, provide localized `title`, `desc` and option names. Effects written inside an `option` execute when it is selected. `immediate` and `after` are event effect blocks with timing that must be considered alongside option effects, cancellation, hidden events and widgets. Inspect the actual window's requirements instead of assuming every event supports the same portrait or input controller.

Dynamic descriptions can select a first matching entry and a fallback. The developer's [event-scripting diary](https://forum.paradoxplaza.com/forum/developer-diary/crusader-kings-3-dev-diary-30-event-scripting.1397140/) explains the motivation. The local `_events.info` has a detailed dynamic-description appendix; use that for current structure.

### Delay and chain state

The full form of `trigger_event` can include `id` and delay units. Decide what happens if the receiver dies, eligibility changes or a target disappears before delivery. Do not assume a stored scope remains valid or that a cost shown earlier is still the cost calculated later.

The examples use an object-owned expiring pending marker and a documented two-event chain. They are statically checked, with runtime propagation explicitly left for gameplay verification. For a production transaction, test both direct dispatch and delayed dispatch before relying on saved scopes across that boundary.

### Event overrides

Local `_events.info` documents `id_override_priority`: higher priority wins among definitions sharing an event ID; identical priorities are errors. It also warns that editing a file during hot reload can reload that file ignoring this priority. Test a cold start and a hot reload separately. This supersedes the older Wiki's general assertion that a single event cannot be overridden.

## Decisions: visibility, validity, price and result

Decision files go under `common/decisions`. The current native picture structure is a block with `reference`, with optional conditional pictures. Some workspace decisions still use the older scalar picture syntax. Do not use their age as a guarantee of current acceptance.

| Field | Purpose to separate |
|---|---|
| `is_shown` | Whether the player sees the decision |
| `is_valid` | Whether the decision is eligible |
| `is_valid_showing_failures_only` | Eligibility requirements displayed as failures |
| `cost` | Price that is applied when taken |
| `minimum_cost` | Affordability gate without applying that price, per native reference |
| `effect` | Result of taking the decision, character-scoped |
| `cooldown` | Repeat-frequency restriction |
| `ai_potential` / `ai_will_do` | Whether/how the AI considers it |
| `ai_check_interval` | AI checking interval; native reference requires it or an applicable alternative |
| `widget` | A specific UI/controller interface with its own scope contract |

Do not charge a `cost` and then manually remove the same currency in the effect unless double payment is intended. `minimum_cost` exists for workflows that apply the eventual cost later, but such workflows need consistency between initial eligibility and actual payment.

The Mass Demand Conversion decision provides a real example of multiple target groups and widget option selection. Its visibility checks call native interaction eligibility, preserving some native rules instead of merely changing faith directly. A newly added candidate group still needs the full interaction audit.

## On actions: subscribing to a game hook

Native code or script invokes on actions. Each hook has its own root and saved targets. `birthday.txt` declares that `on_birthday` receives the character after their age increased. `_on_actions.info` separately documents rootless global pulses and character-specific playable pulses.

For compatibility, add a child on action:

```text
on_birthday = {
    on_actions = { doc_demo_birthday }
}
doc_demo_birthday = {
    trigger = { is_ai = no }
    effect = { debug_log = "doc_demo birthday hook executed" }
}
```

The developer reference permits extending on-action data across files but disallows multiple direct effect or trigger blocks for the same named hook. Thus adding `effect` directly to a hook that already has one can conflict. `SerpAlerts` and Knight Manager provide workspace examples of child-hook attachment.

### Dispatch modes and timing

- `events` lists eligible events; `delay` changes timing for subsequent entries.
- `random_events` chooses using weights; `chance_to_happen` is an evaluation gate and zero entries can yield no event.
- `first_valid` picks the first eligible event.
- Equivalent `on_actions`, `random_on_actions`, and `first_valid_on_action` dispatch child hooks.
- `fallback` invokes another hook when no candidate runs; cycles can stop game time advancing.

The native reference says listed delayed events are checked both when the on action executes and when the delay completes. Do not assume identical validation timing for every other dispatch API.

Most importantly, an on action's `effect` is a separate chain from the events it dispatches. Its setup is not guaranteed to run first, and scopes/local variables set there are not carried to those independent event chains. Put required setup in the event itself or a verified common dispatch chain.

## Acceptance scenarios

For decisions: hidden, visible but invalid, affordable/unaffordable, one execution, cooldown, double-click/repeat, AI and tooltip checks. For events: namespace collision, missing localization, correct receiver, missing target, invalidated delay, choice and post-choice effects. For hooks: clean startup, multiple subscribers, correct root, no fallback loop and bounded performance.

## Installed 1.20.0.3 export supplement

The [current engine reference](../reference/engine-reference.md) now indexes six script and five data-type exports with exact raw line ranges and checksums. Historical statements above about absent generated dumps describe the initial research stage. Use [lookup](../tools/lookup.py) for both engine declarations and existing local definitions/callers. Missing optionality, argument types, scope lifetime, permissions and multiplayer routing remain unknown where the export does not specify them.

See [workspace function contracts](../workspace/function-contracts.md) for owner/caller/state distinctions and [isolated tests](../examples/test-runs.md) for runtime acceptance. The user completed export sessions, but no example gameplay/GUI/MP tests have been performed.

## General Crozier source supplement — 2026-10-03

See [dynamic object selection](puppets-and-selection.md) for rootless setup/default/AI selection blocks versus item-root weighting/validity. The [hook table](crozier-migration.md) preserves native root/target headers separately from inconsistent export labels, creation versus birth, county Rite versus Faith conversion, and death timing.

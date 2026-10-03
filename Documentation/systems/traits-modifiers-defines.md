# Traits, modifiers, opinion and defines

Evidence: [Trait modding, Modifier list and Defines](../research/sources.md); native `common/traits/_traits.info`, `00_activity_feast_modifiers.txt`, `common/defines/00_defines.txt`, local workspace modifiers and [audit findings](../research/vanilla-audit.md).

## Traits

Traits are definitions under `common/traits`, referenced by script keys. Their flags, categories, opposites, inheritance and modifiers are schema fields rather than arbitrary effect blocks. A trait's name, description and icon have localization/asset conventions that need to be fulfilled together.

The native reference describes level tracks with XP thresholds from 0 through 100, multiple named tracks, a single-track shorthand, track localization and XP effects/triggers. Older lists of `hunter_1`, `physician_1` and other tiers are not enough to implement current track-based features.

Dynamic trait names/descriptions/icons can be evaluated without a character root. The native reference explicitly calls for a missing-root fallback. A tooltip requiring a current character may fail when rendering a generic trait catalogue.

For a new trait, audit category behavior, random assignment, incompatibilities, XP limits, icons, localization and save compatibility. Do not invent numeric trait indexes from obsolete online lists.

## Static gameplay modifiers

`common/modifiers` defines named modifier blocks. These contain modifier properties such as `monthly_prestige`, skill bonuses, health or a relevant percentage/multiplier. They are not effects. Runtime effects attach/remove a defined modifier on an appropriate object.

```text
# Definition example, derived from a native feast modifier's numeric property.
doc_demo_reward_modifier = {
    monthly_prestige = 0.1
}

# Separate character effect fragment; verify duration/stacking for production.
add_character_modifier = {
    modifier = doc_demo_reward_modifier
    years = 1
}
```

The storage object and modifier type matter. A character modifier, county modifier, province modifier and artifact modifier are not interchangeable. A numeric property may be a flat amount, additive percentage or multiplier; the name alone is not enough to establish units. Current engine modifier documentation is needed for unobserved properties.

Study both the definition and the attachment/removal caller. Decide whether repeated application refreshes a duration, stacks, replaces or is blocked, and test the actual behavior. Effect-generated tooltips and displayed values should match the real result.

## Opinion modifiers

Opinion definitions live under `common/opinion_modifiers`. An `add_opinion` effect specifies a target and a modifier; direction matters. In the workspace's pardon-hook interaction, the recipient enters its own scope and receives opinion toward the actor. Reversing the scopes changes who likes whom.

Duration, stacking and decaying behavior must be checked against the modifier definition and current API. Use localization explaining the reason, not just an invisible numeric change.

## Three different uses of “modifier”

1. A named static modifier changes gameplay statistics while attached.
2. A `modifier` inside AI/weight syntax conditionally adjusts a weight.
3. A scripted modifier is a reusable weight-syntax helper under `common/scripted_modifiers`.

Do not interchange these blocks. Their readers, units and legal operators differ.

## Defines

Defines are engine-consumed constants grouped in namespaces such as `NGame` and `NCombat`. They can affect exposed parameters of mechanics that are otherwise implemented in compiled code. They do not let script replace arbitrary engine algorithms.

The workspace `CustomDefines` includes gameplay, graphical and Jomini define groups; it also contains Knight Manager logic and GUI files. Its filename does not describe its entire compatibility footprint. Record the individual keys changed and inspect current defaults/comments in the matching native group.

Avoid copying every native define merely to change one constant. Audit the current loader's field-merging/override behavior for the group and use a minimal override only where that behavior is established. Do not promise that all namespaces and databases merge identically.

Test unit/range boundaries, startup versus hot reload and any multiplayer/checksum implications of the actual change. Historical claims about a graphics-only mod's checksum do not establish the status of new asset, GUI or gameplay edits in the current build.

## General Crozier source supplement — 2026-10-03

See [Crozier lifecycle contracts](crozier-migration.md) for trait hooks/recursion, secular inheritance blocking, standalone currency modifiers and government flags; [Religion and rites](religion-rites.md) covers personal-tenet modifiers and spiritual-fulfillment levels. No new balance or gameplay result is claimed.

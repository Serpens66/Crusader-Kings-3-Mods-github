# Existing mods: patterns, entry points and limitations

Evidence is the workspace itself, not Workshop descriptions. See [complete text/asset inventory](../reference/workspace-inventory.md) and [file hashes/definitions](../reference/local-index.json). All eleven mod/content directories were included. Nothing in them was edited.

## Knight Manager family

`Knight Manager (MP)` combines `gui/window_knights.gui`, scripted GUI actions, `can_be_knight_trigger` replacement, localization and a game-start child on action. GUI actions toggle character-owned preferences; the eligibility helper considers the army owner through `$ARMY_OWNER$`. This is a useful model for separating a UI click, stored character state and a gameplay predicate.

Its `on_game_start` extension sets a global loaded marker for UI interoperability. The hidden event with an error-suppression namespace is a compatibility/validator workaround, not a feature entry point to copy as a gameplay event. The name `(MP)` alone does not prove that a fresh change is multiplayer-safe.

`Knight Manager Continued (MP)` provides `kmc_gui.txt` and `kmc_trigger.txt` with expanded preferences and an additional manual-allow variable. The inventory found no real `.gui` file in this content directory, but it contains a `.lnk`. A shortcut is not automatically packaged content: inspect where the intended window comes from before treating this directory as a complete portable UI implementation.

`test` reproduces much of the older Knight Manager layout. It is a variant/test content root, not an additional independent production feature. Compare definitions and descriptors before choosing it as a baseline. The older/continued variants share the native `can_be_knight_trigger` override; enabling them together can therefore conflict even if filenames differ.

**Reusable:** character-owned flags, explicit owner parameters, child on-action attachment. **Re-audit:** entire current knight predicate, window replacement, missing assets and multiplayer tests.

## CustomDefines

This directory contains namespace/key overrides for graphical and gameplay constants, but also Knight Manager scripts, localization and `window_knights.gui`. Its footprint includes much more than defines. It illustrates why an inventory must follow files rather than infer scope from the mod's name.

The same Knight Manager callback/helper names occur in several directories. They are overlap candidates, not isolated helpers. A new utility should use its own prefix rather than inherit those names without a deliberate compatibility contract.

## Mass Demand Conversion

Primary entry point: `common/decisions/mod_mass_convert_subjects.txt`. The decision offers group choices and queries native interaction acceptance for direct/indirect vassals, tributaries, courtiers and house members. The standalone version includes newer picture-block syntax and extra candidate handling compared with the bundle version.

The script-value file supports UI/count calculations. The `accept_conversion_notification` file contains a fully commented-out native event experiment. It is inactive in both standalone and bundle; do not count it as an active override. See the [update sheet](../update-readiness/mods/mass-demand-conversion.md) for the checked current status.

**Reusable:** classify target sets, retain native interaction rules, share numeric calculations. **Re-audit:** current faith/rite conversion API and exact dispatch helper chain, treatment of indirect vassals, candidate duplication, widget flags, consent and preview costs.

## Leave Wars

The interaction identifies shared wars, saves up to ten named war scopes, and dispatches a long event-based selector. Related files define rule settings, prices, opinions, messages, localization and effect text. This is a multi-file feature with delayed context and a bounded selector, not merely one war-removal call.

Source comments document an older hardcoded-picker limitation. Preserve that as author reasoning; validate whether it still holds before choosing the same workaround. Test what happens with more than ten candidates, ended wars, changed participants and war leadership.

The same feature appears inside `SerpInteractionsDecisions`, including shared identifiers. Loading both forms may duplicate/override definitions. Future changes must identify which distribution is being targeted.

## SerpInteractionsDecisions

This bundle includes resource conversion, abdication, additional education, pardon hooks, multiplayer money sending, temporary excommunication, conversion and leaving wars. Entry points are decisions/interactions; event chains implement follow-up choices. Prices, opinion/static modifiers and localization are separate dependencies.

`pardon_hook_interaction` is a compact example: display a usable-hook requirement, consume it in actor scope, and add opinion on the recipient toward the actor. The additional-education feature illustrates costs plus event/modifier dependencies. Resource conversion illustrates a decision launching a choice event.

Some decision pictures use older scalar syntax, while the standalone conversion decision has a modern picture block. The descriptor advertises 1.5.*, so current source compatibility must be established independently. Do not update the descriptor merely to silence a warning without testing its features.

## SerpAlerts

`common/important_actions/serp_alerts_actions.txt` adds alert conditions; on-action subscriptions send messages for game events. A war-start child hook builds recipient lists from family, spouses, heirs, councillors and pinned/related characters, then filters player recipients and some overlaps.

This is useful evidence for event-driven notifications and list deduplication concerns. Audit every callback's attacker/defender/root contract in Vanilla before reusing the code. Tooltip/alert conditions can be evaluated frequently, so review their cost separately from notification effects.

## Gender Colour and graphical variants

`Gender Colour` contains a descriptor and DDS replacements rather than gameplay scripts. Its absence from a `.txt`-only scan would not mean it has no effect.

`GFX-Mod` is a smaller graphical package. `GFX-Mod Serp` shares its descriptor identity/Workshop ID but contains many more assets and a whole-file post-effect replacement. The fuller variant's `info.txt` explicitly explains the local/distributed distinction. It lacks a same-named external `.mod` in this workspace; that fact alone does not establish its current launcher registration elsewhere.

Record exact texture/path overlaps for graphical changes. Verify game-version compatibility for post-effects and maps. Preserve third-party credits, and resolve redistribution permission per asset before using them in a new published mod.

## Lessons for new work

Prefer the current native source for a contract, then use a workspace pattern for implementation shape. Specify the distribution being changed, preserve user edits, trace references across all files and avoid copied public identifiers. A mod's age, descriptor wildcard, folder name or successful historical upload does not replace a current feature audit.

## State and contract supplement

See [function-level owner/lifetime guide](function-contracts.md), [43 engine-reconciled cards](../update-readiness/contracts/README.md) and [Knight variants learning audit](knight-manager-contracts.md). These retain alternatives and unresolved context/lifecycle questions rather than treating old workspace code as a current best-practice reference.

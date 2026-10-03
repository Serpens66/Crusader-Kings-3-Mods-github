# Documentation Contract Lab — source-informed, runtime pending

This separately named package adds a five-gold character interaction, courtier count/dispatch decision, player birthday message/manual callback decision and a character-root Scripted GUI action. It uses only its own `doclab_` IDs, plus an additive native `on_birthday` child hook. It is not installed or activated. Source contract intake: [audit manifest](../native-recipe-audit.json), [engine reference](../../reference/engine-reference.md). Test using the [bundled manual](../test-runs.md).

| Files | Entry and scope contract |
|---|---|
| `common/character_interactions/doclab_interactions.txt` | Human actor, distinct living adult recipient; auto-accept, five-gold affordability; on_accept enters actor and rechecks funds/life before payment |
| `common/scripted_triggers/doclab_triggers.txt` | `doclab_batch_candidate`: candidate `this`, requester `root`; requester's native validity query receives candidate through `prev` at this exact root hop |
| `common/script_values/doclab_values.txt` | Fixed amount 5; eligible courtier count; total cost count × amount |
| `common/scripted_effects/doclab_effects.txt` | Rechecks total balance, iterates the shared predicate and runs own interaction with explicit actor/recipient and accept threshold; notification guards optional spouse |
| `common/decisions/doclab_decisions.txt` | Count/total UI and dispatch share values; separate manual callback decision is a repeatable recipient test |
| `common/on_action/doclab_on_actions.txt` | Adds child to native birthday hook; human/live root only; automatic and manual invocation each constitute one separate invocation |
| `common/messages/doclab_messages.txt` | Unique neutral feed-message type; actor portrait, optional spouse portrait |
| `common/scripted_guis/doclab_guis.txt` | Same living human character root for visibility, validity and execution; adds exactly 2 gold per valid click |
| `localization/english`, `localization/german` | English strings; German file is an explicitly English fallback for this private test |

The immediate transfer is not native gift balancing: no gift opinion, native price or struggle effects. Count agrees with the shared predicate when state is unchanged, not with an immutable snapshot under arbitrary concurrent changes. There is no persistent batch list or claim of native conversion equivalence. On-action `.info` states that effect/event chains do not automatically share local scope saves; this fixture creates its own root-bound notification and never relies on a saved scope from a parent effect.

The notification sends in the current human scope. The spouse is optional portrait content, not an additional recipient. No spouse branch omits the right icon entirely. Expected one feed message per invocation for the owning player, zero for AI. Birthday and manual calls deliberately both exist; do not misclassify two separate invocations as duplicate delivery from one callback.

Engine signatures support these API forms; current `00_gift.txt` and native yearly interaction dispatch establish payer and explicit actor/recipient patterns. Native funeral GUI supplies a complete ScriptedGui caller pattern; widget registration `.info` supplies additive window registration. Permissions, synchronization, candidate-query initialization and actual acceptance/rendering remain tests. None of these files is advertised as a working production template yet.

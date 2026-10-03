# Puppet actions and dynamic decision selection

Baseline: **1.20.0.3**, checked **2026-10-03**. [Evidence/locations](../research/general-120-evidence.json), [coverage](../research/crozier-source-coverage.md). Runtime, GUI and multiplayer: **not run**.

## Puppet types and actions

`common/puppets/types/_puppet_types.info:1–57` distinguishes acquisition from use. Naming an acquisition interaction does not establish a puppet automatically: that interaction must call `set_puppet`. Its AI targets also provide the UI selection list. `can_have` evaluates the prospective puppeteer; `is_valid` has puppeteer root and `scope:puppet` and is checked daily, removing an invalid puppet. This timing is documented; its real save/reload and cleanup effects remain runtime questions.

Type priority is evaluated for the ruler opening the window. Triggered assets and animations select their first matching entry and require an unconditional fallback. The reference says each action should be used by only one puppet; do not silently reuse one action key across types.

`common/puppets/actions/_puppet_actions.info:1–35` supplies action types `character_interaction` (default), `decision` and `great_project`, plus the referenced key. `is_enabled` runs with puppeteer root and `scope:puppet`. `is_important` defaults to no. Generic UI text uses `puppet_action_description_<action_key>`.

The [official developer explanation](https://store.steampowered.com/news/posts/?appids=1158310&feed=steam_community_announcements), diary #8 / Puppet, distinguishes interaction actor from effective actor: `scope:actor` remains the puppeteer for a puppet interaction, `scope:puppet_or_actor` represents its effective character, and `scope:is_puppet_action ?= yes` identifies puppet execution. Actor-root blocks such as `is_available` remain actor-based. Some special interactions additionally require engine support.

For a **puppet decision**, the local reference instead gives ROOT = puppet and `scope:puppeteer` = commanding ruler throughout decision triggers, costs and effects. Do not copy the interaction scope convention into decisions. The diary's proposed future GUI chooser support is a historical proposal, not evidence that this installation implements it.

## Script queries and dispatch

Native important actions and script values use `is_character_interaction_potentially_accepted` outside opened interactions. Some enter `root` and query `recipient = prev`; current Sway-to-Rite helpers enter a supplied requester and query a supplied target. They separately use `ai_accept` for percentage filtering. These are intentional caller patterns; they do not establish every omitted default or validation stage.

`run_interaction` requires explicit actor/recipient and at least one threshold. The current export distinguishes immediate `execute_threshold` from `send_threshold`, gives redirect's default, and lists optional secondary actors. Vanilla uses `send_threshold = decline` for player requests and an immediate accept threshold for a separate mass-conversion route. An API declaration or another interaction's caller does not certify native costs, option creation, cooldowns or downstream consequences for your selected interaction. Full signatures and remaining questions are retained in the [focused research](../update-readiness/mods/mass-demand-conversion-audit.md).

## Dynamic object selection

`common/decisions/_decisions.info:305–348` documents `select_scope_object`. A selected object is available to decision effects as `scope:selected_item`; it need not be a character or title. This controller differs from fixed flag-based `decision_option_list_controller` and title-specific selection controllers.

| Block | Evaluation context | Documented behavior |
|---|---|---|
| `setup_items` | no root; `scope:actor` = current actor | Player-interface item construction; add objects with `add_to_list = item_list` |
| `default_item` | no root; actor provided | Save the default as `selected_item`; without it, first generated item is the default |
| `ai_select_item` | no root; actor provided | Direct AI selection; bypasses the item-construction/weight path |
| `ai_item_will_do` | ROOT = item; actor provided | Weights constructed items; non-positive weights discarded; unused when direct AI selection exists |
| `is_item_valid` | ROOT = item; actor provided | Invalid items remain visible but disabled with reasons; absent block treats all items as valid |

List construction, default selection, displayed item validity and final decision eligibility are separate contracts. Do not evaluate actor-owned resources on item root. Revalidate a stale selected object and actual payment in the complete native workflow before implementing your own selector.

The `.info` controller table ties each controller to a specific data context. A new object type may require its matching GUI presentation. Title selectors have world and `_in_realm` forms; prefer the realm form when that is the intended search domain, rather than enumerating the world and filtering afterwards.

Two concrete native callers illustrate the distinction. `common/decisions/50_holy_site_decisions.txt:119–166` constructs non-Eminent holy-site items and separately supplies player defaults and restricted AI selection. `common/decisions/dlc_decisions/pam/pam_saint_decisions.txt:6–65` chains a deceased-character picker into a location picker: it enters `scope:actor`, includes dead ancestors explicitly, binds `CANONIZER = scope:actor`, orders the default by `pam_saint_worthiness_value` and validates each candidate. Selection and the eventual confirming/cost step are separate. These source patterns need their complete downstream audit before reuse.

Native `gui/window_holy_site.gui:576–612` calls `PdxGuiWidget.MakeDecisionTypeWithParam` with a decision key, `selected_item` and `HolySite.MakeScope`. This is evidence of scoped preselection. Retrieve its registered owner signature before using it elsewhere; a standalone function with the same short name is not implied.

The current datatype index retains both the promoted `PdxGuiWidget.MakeDecisionTypeWithParam(Arg0, Arg1, Arg2)` returning `DecisionTypeWithParams` and a separate function entry with an unregistered return type. Preserve both entries rather than treating the latter as a missing implementation or collapsing them into a global function.

## Tests to prepare after a feature audit

Cover zero/one/many items, missing actor or selected object, invalid visible items, changed resources and ownership between display and action, default selection and both AI selection paths. Cover puppet acquisition/removal, effective actor versus payer, daily invalidation, player switch, notifications and two-player simultaneous use. The source-informed selector description is not a tested reusable mod template.

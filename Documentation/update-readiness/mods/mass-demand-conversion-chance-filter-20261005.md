# MDC acceptance filter — 2026-10-05

Source audit completed for the added registration/GUI/threshold interfaces against installed **1.20.0.3** before mod edits. [Source evidence](../evidence/mdc-chance-filter-source-audit-20261005.json) verifies the complete native files against pinned Vanilla commit `0ec13350cde9e410b37a46d3616966838f4ba994`; relevant definitions, callers and exports were read. Existing general query/dispatch Engine and runtime gaps remain open, rather than receiving invented defaults.

## Source contract and design

`common/decisions/_decisions.info:270–303` permits one uniquely named custom widget with the existing option-list controller. Native `decision_view_widget_decision_option_list_controller.gui` binds Entry.Self to OnSelect, Entry.IsSelected to radio state and Entry.GetName to the label. `window_decisions_detail.gui` embeds the requested widget without replacing the decision window. Native button_radio_label supplies the radio/text blocks. The current datatype export supplies these functions and DataModelFirst/DataModelSkipFirst.

The MP setup window's `_show` state initializes local VariableSystem.Set state; HasValue controls tabs and visibility. Native activities demonstrate sliced datamodels. These establish source-supported GUI recipes; they do **not** certify the combination's runtime ordering, refresh or multiplayer behavior. No custom C++ controller, ScriptedGui gameplay mutation or persistent character/global variable is added.

Eleven fixed entries, never dynamically hidden or removed from the controller: indices 0–2 direct vassals (none/80/100), 3–5 indirect vassals, 6–8 tributaries, 9 courtiers, 10 house. The widget displays five groups and a three-choice filter. Filter buttons select the corresponding native entry in the already-selected group; the GUI variable only controls which variant's label/count is displayed. Gameplay reads only the native selected scope flag. Opening selects index 0 and clears the local mode to none; closing clears local mode. Entry ordering and `_show` initialization require the tests below.

Native `pam_sway_to_rite_variant_acceptance_trigger` supplies `ai_accept = ACCEPT`; the native localization comment explicitly aligns its percentage buckets with the interaction window. The export calls ai_accept a minimum acceptance value. The new fixed cutoffs use 80 and 100, with no manual chance calculation. Vasallike targets use the unchanged native demand interaction, including probabilistic first reply and later negotiation. The separate demand_conversion_likelihood_calculation differs from ai_accept and is not used. Original omitted required_response/option defaults remain omitted, as in the native percentage caller; no new claim about those defaults is made.

## Implementation boundaries

Standalone only. Existing public IDs, unfiltered queries, protection rules, recipients, send_threshold = decline, notification overrides and metadata remain. Six uniquely prefixed filtered entries/counts share threshold query helpers with dispatch. Eight languages receive labels and explanatory tooltips. Counts are eligible requests at the display snapshot, not successful or completed conversions; zero candidates produce zero requests. The decision visibility remains unfiltered so choosing an empty cutoff does not remove it.

## Required runtime acceptance — all pending

- Cold-start only the standalone mod. Exactly five group rows and three filter controls; all eight languages fit or wrap correctly; no GUI/context errors.
- Each group × each filter: mark correct selection, show corresponding count, preserve group on filter change and filter on group change. Courtiers/house stay unfiltered. Test zero counts and disabled/changed native targets.
- Close/cancel, reopen and save/reload: local mode and native default both return to none, no stale hidden selection. Verify the fixed index mapping and GUI lifecycle notifications.
- Same paused actor/target/options: compare native UI percentage against cutoff queries around 79/80 and 99/100, including rounding, auto-accept, pending requests and cooldown. A mismatch blocks advertising reliable percentage filtering.
- Verify count/query/delivery sets at unchanged state; recheck changed state at send. Native costs, refusal, gold/favor/study negotiations and notification rewards remain native.
- Two players concurrently choose different groups/cutoffs and confirm; each selected native flag applies to its own actor without cross-player state or OOS. Save/reload and player switch separately.

No game, GUI or multiplayer test has been executed. No release/compatibility metadata promotion or bundle update follows from static success. Do not advertise 100% as guaranteed completed conversion.

## Static verification — 2026-10-05

`python Documentation/tools/test_mdc_chance_filter.py`: **16 passed**. The checks interpret actual GUI slices/actions for all combinations, lifecycle/reset wiring, fixed native flags, helper parameters, zero-initialized counts, fresh send queries, eight complete localizations and BOM/structural balance. Normalizing only the added query threshold reconstructs every original count; normalizing the added selection/query reconstructs every original vassal send branch. Original courtier/house branches, unfiltered visibility/counts and all send blocks match pre-edit structural hashes. This is source verification, not execution of native Engine or GUI code.

Repeatable update detection preserves the original 40 watches and adds nine interface/dependency watches. Earlier baselines are unchanged; only the MDC local-source snapshot is refreshed. No compatibility or MP approval follows.

[Final verification record](../evidence/mdc-chance-filter-verification-20261005.json): 49 native watches unchanged, Engine exports unchanged, original baselines/bundle/metadata/notification files and pre-existing descriptor edits retained. No game tests were run.

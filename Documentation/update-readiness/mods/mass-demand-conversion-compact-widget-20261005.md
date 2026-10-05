# MDC compact widget correction — 2026-10-05

Standalone **1.079**, installed Vanilla **1.20.0.3**. [Source audit](../evidence/mdc-compact-widget-source-audit-20261005.json) preceded this patch; native decision-window/button sources still match their prior hashes, and new scroll/create-state/preview examples match the pinned Vanilla commit. No game files or common decision-window overrides were changed.

## User-observed defects and source diagnosis

Two user screenshots show the pre-patch widget in-game: the unset-filter view omits all three vassal/tributary groups, while clicking 80% exposes five groups but places lower rows outside the window. The first view also has no marked filter. This matches the old display conditions requiring an explicitly set none value, with no trigger_on_create initializer; it is not proof of a native two-option limit. Large vertical filter buttons/permanent explanation and insufficiently bounded layout add height. Rendering was observed failing; query/count/send/MP success was not established by those screenshots.

The native effect section is visible through HasEffect and prints GetEffectDescription. MDC previously supplied no explicit printable explanation: its selected-flag branches invoke interaction sending, which must not be described as guaranteed conversion. The patch adds an unconditional native custom_tooltip, as in native decisions. Exact Engine preview treatment of absent selected flags remains narrower than the source evidence; no new initialization contract is invented. Removing the native heading would require modifying the shared window; the chosen correction keeps it useful without that footprint.

## Current implementation contract

- Root min/max 514 × 250; one 32-high horizontal filter row, 8 spacing, 210-high native recipient scrollbox. Three 125-wide columns plus a 120-wide heading and 4 spacing fit within 514. Overlaid selected-group wrappers occupy the same fixed row, not five vertical rows.
- Eight languages have compact captions and **35 unique keys**. Scope explanation appears only in tooltips; the effect preview has one localized request/consequence explanation. No guaranteed acceptance/conversion claim is added.
- Create-state initializes GUI mode to none; the zero-size first-entry helper initializes the native default with OnSelect. Existing _show resets cover a reused widget when propagated; _hide clears local state. Reopen/creation ordering is still a runtime test.
- None display/radio state is Not(Or(HasValue80,HasValue100)), so missing/unknown GUI values show the three unfiltered groups. Courtiers/house remain visible/unfiltered. Native selection flags alone drive gameplay.
- Eleven entries/order, group/filter selection actions, all queries, original counts/protection policy, interactions/send blocks and notification overrides retained. The only effect addition is explanatory custom_tooltip; all five original effect branches are preserved.

## Static verification and source monitoring

**19 tests passed**: actual datamodel/action routing, valid/missing/unknown-mode group visibility and radio state, creation/reset wiring, bounds/column budget, tooltip-only explanation, unconditional preview, 35-key parity in eight languages, structural balance/BOM and original query/count/send regression hashes. These tests interpret source expressions; they do not emulate the native renderer or interaction Engine.

The new dated baseline preserves the previous 49 watches and adds four watches for shared lists, native create-state widgets/window and effect-preview caller. Earlier baselines and other mod registrations remain unchanged. [Verification evidence](../evidence/mdc-compact-widget-verification-20261005.json) records the selected-mod check and preservation results.

## Required runtime acceptance — pending

1. Fully restart CK3 with standalone MDC. On opening, all five groups appear and none/direct default are correctly marked; cancel/reopen and save/reload reset display and native selection together. Filter controls must never disappear on a group switch.
2. Every group × every filter: retain group on filter change and mode on group change; verify counts refresh and zero does not hide rows/decision. Native selected entry and delivered recipients must agree.
3. Normal/high UI scale: one compact line, readable eight-language captions/tooltips, fixed viewport, no overlapping confirm button or rows escaping the frame. Force sufficient overflow to test scrollbar drag and mouse wheel.
4. Same paused actor and manually eligible target/options: compare unfiltered native eligibility/count/send set, then 80/100 boundaries and rounded UI percentages. Being sendable does not establish an 80% chance. If unfiltered count remains zero incorrectly, trace actual Entry.GetName localization scope, actor and native query context before any backend change. Preserve cooldowns/pending/protection and avoid guessed puppet scopes.
5. Two simultaneous players choose differing groups/filters; verify recipient isolation and no OOS, including reopening. Earlier MP and native-query contract gates remain open.

No post-patch game, scrolling, count-parity or MP test was executed. User screenshots are failure evidence for the old layout, not approval of this patch. Version/release metadata remain **1.079** and unchanged; no compatibility certification, publication or bundle edit.

Final selected-mod check: **53 native watches unchanged**, recorded Engine exports unchanged. Snapshot comparison found no unexpected existing-file changes or missing files; release metadata and prior dated baselines are byte-preserved. Removing just the added explanatory lines reconstructs the complete pre-patch decision byte-for-byte. Diff whitespace checks pass.

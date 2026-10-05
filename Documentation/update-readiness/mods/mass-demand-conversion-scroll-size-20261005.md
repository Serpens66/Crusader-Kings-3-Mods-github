# MDC explicit scrollbox size correction — 2026-10-05

Standalone **1.079**, installed Vanilla **1.20.0.3**. [Feature source audit](../evidence/mdc-scroll-size-source-audit-20261005.json) completed before editing. Read the [mandatory failure ledger](mass-demand-conversion-gui-failures-20261005.md) for every screenshot-backed failed approach and limitations of the earlier tests.

The latest bb70136b screenshot confirms the absolute filter heading/controls are inside the frame, but the recipient viewport background and all five rows are displaced right. The native scrollbox template has size100×100; MDC's restored subtree provided only514×210 limits. The size discrepancy is source-confirmed. Its role in the displacement is an inference awaiting renderer validation, not a proven Engine layout equation.

## Isolated correction

Only **size={514 210}** plus its explanatory comment is added to the scrollbox. Filter row/positions, root vbox, Git-derived native recipient list/button style, eleven selection routes, state lifecycle, captions/tooltips, gameplay/query/count/send, localization, notifications, bundle and version metadata remain byte-preserved outside this GUI change. No offsets or new wrappers.

**23 static tests passed**. A new regression requires size/minimumsize/maximumsize to agree; the Git subtree comparison now permits exactly the added size and still requires every other field/content to match. Functional root bindings and the complete filter subtree are compared with the preceding widget. These checks are not game rendering tests.

[New baseline](../update-watch-mdc-scroll-size-20261005.json) preserves 60 prior watches and records 61 total, with earlier baselines/other mods intact. [Verification evidence](../evidence/mdc-scroll-size-verification-20261005.json) records source, scope, link/encoding and read-only checks separately from runtime.

## Pending acceptance

Fully restart CK3. Check whole viewport position and each recipient row on first opening; all labels must fit and distinct rows must remain centered. Switch every group/filter repeatedly, cancel/reopen, test normal/increased UI scale and scrolling. The already confirmed filter placement must remain unchanged. Native count/send parity,80/100 percentage comparison and multiplayer remain open. No publication or compatibility/MP approval.

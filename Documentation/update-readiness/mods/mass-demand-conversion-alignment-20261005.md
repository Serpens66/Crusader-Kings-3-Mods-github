# MDC widget horizontal alignment — 2026-10-05

Standalone **1.079**, installed Vanilla **1.20.0.3**. [Feature source audit](../evidence/mdc-widget-alignment-source-audit-20261005.json) checked current native option-list flowcontainers, radio-button type, scrollarea and Scrollbox_Margins before this GUI patch. All source files match the pinned Vanilla reference. No shared native window or installed game file was edited.

## User-observed partial result

The latest user screenshot of the preceding compact layout shows all five groups, a marked none filter, and **21 indirect vassals**. The explicit effect explanation renders and the widget no longer grows vertically beyond the window. However, the 100% control and recipient rows extend past the right edge. This is evidence for those specific observations only: counts are not independently validated, all group/filter combinations and reopening remain untested, and no sending/percentage/MP claim follows.

## Alignment patch

The root uses the native option-list **vertical flowcontainer** pattern, retaining 514×250 limits and 8 spacing. Separate horizontal flowcontainers with parentanchor hcenter center the 514×32 filter section and 514×210 recipient scrollbox. The overlaid group vboxes and their selected hboxes anchor top|left at zero; inner filter columns remain managed by hbox layout, without independent offsets. No negative pixel compensation is used.

Scroll content and all eleven recipient containers/buttons expand horizontally as in the native option list. Radio rows use the native **450×30** width rather than 470. Native Scrollbox_Margins reserves 15 left and 20 right; additionally budgeting the 12-wide vertical scrollbar gives 467 usable width, so 450 leaves headroom even when the scrollbar is visible. The five visible groups and full scroll behavior remain; actual rendered coordinates are a runtime check, not computed by the static source parser.

Every datamodel, visibility/radio expression, selection/initialization action, enabled binding and text/tooltip binding matches the pre-patch GUI. Captions/localizations, all eleven selection entries, create/show/hide reset, query/count/send logic, explicit effect explanation and notification overrides are unchanged. Standalone metadata remains 1.079. Only GUI alignment, static tests and current maintenance evidence change.

## Verification

**20 static tests passed**, including native container topology, centered sections, shared zero origin for overlays, unanchored filter columns, conservative scroll content-width budget and existing selection/gameplay regression checks. Per-field GUI binding multisets match the pre-edit source. Encoding/line endings and diff whitespace are checked. These tests do not run the game renderer.

The [new dated baseline](../update-watch-mdc-alignment-20261005.json) preserves all 53 previous native watches and adds shared/windows.gui for Scrollbox_Margins (54 total). Earlier baselines and other mod registrations remain intact. [Final verification evidence](../evidence/mdc-widget-alignment-verification-20261005.json) distinguishes static/source checks from the partial user observations.

## Required post-patch runtime check — pending

- Fully restart CK3. All three filter controls, including 100%, and every group label/count must lie inside the right edge; the filter line and list share a sensible alignment with the native content area.
- Every group/filter combination preserves marking, group/mode and refresh behavior; cancel/reopen resets both GUI and native selection. No click region overlaps another row or the confirm button.
- Normal and increased UI scale, eight languages and large counts: no truncated labels or overflow. With overflow, wheel and scrollbar work within the recipient viewport.
- The positive indirect count is a user observation, not complete count/query/delivery parity. Existing same-state native percentage, unfiltered eligibility/send and two-player/OOS matrix stays open.

No post-patch rendering, scroll, sending, percent comparison or MP test was executed. No release/compatibility promotion, bundle update or publication.

Final selected-mod check: **54 native watches unchanged**, recorded Engine exports unchanged. Full workspace snapshot comparison found no unexpected existing-file changes or missing files. Every mod file except the standalone MDC widget, including all languages/gameplay/descriptors/notification files and pre-existing user changes, is byte-preserved. Prior dated baselines and GUI encoding/line endings are retained; diff whitespace checks pass.

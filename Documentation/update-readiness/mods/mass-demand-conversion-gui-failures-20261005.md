# MDC GUI failures: mandatory evidence check before further layout work

Date **2026-10-05**, standalone 1.079, Vanilla 1.20.0.3. Read this alongside the [current size correction](mass-demand-conversion-scroll-size-20261005.md) before reusing earlier layouts or tests. Earlier dated reports/baselines remain historical evidence; their successful static checks do not make their GUI recipes runtime-validated.

## Screenshot-backed failures and limitations

| Attempt | User evidence | What the evidence establishes | Consequence for future work |
|---|---|---|---|
| Initial three vertical filters and persistent scope explanation | f023bf04 / da67de71 screenshots in chat; [compact-widget report](mass-demand-conversion-compact-widget-20261005.md) | Initial view lacked three groups; changed filter exposed rows extending below the frame. Widget was too tall. | Do not restore tall filters/visible explanatory paragraph. Preserve creation-time reset and missing/unknown-state fallback; initial state was a code gap, but the screenshot alone does not prove it caused every missing/zero candidate. |
| Compact horizontal filters with prior outer containers | f5500ad8 screenshot; [alignment report](mass-demand-conversion-alignment-20261005.md) | 100% and recipient labels extended right. | A correct summed child width does not establish the positioned outer viewport. Trace inherited sizes and all parents. |
| Native-style flowcontainer wrappers and expanding recipient rows | bfba87c2 screenshot; same alignment report | List fit but was left-aligned; 100% still exceeded the edge. | These wrappers/expansion did not achieve the intended layout in this widget. Do not treat native-looking structure as runtime proof. |
| Narrow451 filters and custom radio type with inner parentanchor=center | 4d994dd1 screenshot; [centered-options report](mass-demand-conversion-centered-options-20261005.md) | 100% improved; recipient content remained left-aligned and filters inset. | Presence of center anchor was insufficient here. Inspect available size, parent/own anchors and layout ownership; do not generalize that center anchors never work. |
| Custom full-size recipient content hbox with equal expanders | 9d4e414b screenshot and user report; [flex report](mass-demand-conversion-flex-alignment-20261005.md) | Direct/indirect rows overlapped on first open; layout changed after percentage switches; filters remained inset. | This composition was not a validated recipient recipe. Remove custom recipient layout as requested. No evidence proves expand/hbox is globally broken or identifies the precise transient-height Engine cause. |
| Git a81d7f3 scrollbox restoration plus explicit absolute filters | bb70136b screenshot; [Git restoration report](mass-demand-conversion-git-targets-20261005.md) | Heading/filter controls now sit within the frame; whole recipient background and rows are displaced right. | Preserve the successful absolute filter row. Git equality proved restoration only: a81d7f3 already contained the first custom chance-filter layout and was not a tested original five-item native widget. |
| Accepting 20/21/22 passing structural tests as sufficient layout confidence | All failures above followed passing static checks | Tests did not execute the renderer or initialization/layout updates. | Keep source/static/runtime evidence separate. Tests must assert effective source contracts and reject known broken source, while rendered coordinates remain a game-test gate. |

Image labels above abbreviate the unique attachment filenames in this chat; originals are temporary user attachments, not copied into the repository. Their observations are recorded here and in dated reports. No delivery, percentage parity or multiplayer result follows from these images.

## Newly confirmed source defect; runtime explanation still an inference

Native gui/shared/lists.gui defines **type scrollbox = scrollarea, size={100 100}**. Restored MDC declared minimumsize/maximumsize={514 210}, without a local size. This omission is confirmed by both live source and Git. Native decision_view_widget_option_list_generic explicitly sets its own scrollbox size; the containing layout and flags also differ from the original native controller.

The latest whole-viewport displacement is consistent with differing nominal and constrained sizes inside a centered vbox. As a diagnostic scale comparison, (514-100)/2 is **207 GUI units**, large enough to explain a gross horizontal shift; this is not a measured Engine positioning equation. It must not be quoted as proven internal behavior, nor should min/max be declared universally ignored.

The targeted correction adds **size={514 210}** while retaining both limits and all list contents. No pixel offset, new centering wrapper, recipient type or filter change is made. It remains unvalidated in game until first-open/filter-switch/reopen/scaling/scroll checks pass.

## Required investigation discipline

1. Read the complete type ancestry and insertion chain: decision detail parent, widget root, scrollbox default size/margins/scrollwidget, actual overridden content, datamodel item layout and radio-button content.
2. Record explicit **size**, inherited size, limits, expansion policy, parentanchor, widgetanchor and position separately. Bounds alone are not an explicit nominal-size override.
3. Preserve the latest screenshot-confirmed improvement; make a small isolated correction and compare behavioral bindings, not just text or brace balance.
4. Distinguish old native controller usage (Git a2df10b) from the first custom filter layout (a81d7f3). A Git snapshot is provenance, not runtime acceptance.
5. Test first opening, every group/filter transition, cancel/reopen, UI scale and scrolling after a full restart. Log unresolved failures without declaring success or blaming Engine internals without evidence.

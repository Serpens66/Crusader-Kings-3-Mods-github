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

## Subsequent user confirmation and common-column request — 2026-10-05

User screenshot808b7d31 and explicit statement confirm the isolated scrollbox size override now places the list centrally and makes all five groups visible. This upgrades the earlier size correction from unrendered to partial user-run visual confirmation. It does not prove the earlier inferred internal Engine equation, all transitions/scales/languages, gameplay or multiplayer. Earlier pending-size statements above describe the state before this confirmation.

The new issue is row-to-row radio/text origin variation; reference screenshotbf7803d8 requests common columns in a centered overall block. [Current caption-only patch](mass-demand-conversion-radio-columns-20261005.md) adds identical285×30 text fields to the eleven native recipient buttons. No failed custom template, flex composition or offset recipe is restored. New column geometry is statically checked and remains untested in game.

## Caption-only correction disproved; fixed slots remain untested — 2026-10-05

Screenshot91dc2d7b and the user's first-opening report establish that fixed285×30 captions alone did not stabilize layout. First open is left-aligned; after filter switches the three changing group rows have a different horizontal origin from courtiers/house. Preserve this as a failed approach. Do not recommend another text-width-only patch or treat the24 passing structural checks as renderer proof.

The remaining native radio-label flowcontainer and independent auto-sized datamodel wrappers are confirmed source facts; the exact internal layout/update ordering is not established. The [fixed-slot correction](mass-demand-conversion-fixed-rows-20261005.md) removes automatic measurement from the recipient placement chain: permanent slots, fixed wrappers/items and native-derived explicit radio/text coordinates. Unlike the earlier failed equal-expander type, it uses no flexible or intrinsically measured recipient container. This new composition is source-audited and statically checked, but remains untested in game. Do not add it to working examples until first-open/filter-switch/reopen and scaling tests pass.

## Fixed-slot implementation visually accepted by user — 2026-10-05

Following the fixed-slot patch, the user reported that it now looks good and requested documentation of the working code. The [implementation report](mass-demand-conversion-fixed-rows-20261005.md) and [dated confirmation/source checksum](../evidence/mdc-fixed-rows-user-confirmation-20261005.json) identify the visually accepted reference. Previous pending-rendering statements above describe the state before this feedback; retain them and every failed-approach record.

The successful reference uses explicit514×210 scrollbox size, replaces scrollbox_replace_vbox with fixed514×204 content, places five470×30 permanent slots at22/{15,51,87,123,159}, overlaps identically sized filter variants at0/0 and positions a320×30 radio/text body at75/0 inside every row. Radio30 and text285 with gap5 share a common origin, independently of caption/count/filter. This whole chain is the accepted implementation; feedback does not establish which individual component alone fixed Engine behavior. Do not infer a proven internal layout equation or a universal defect in native flowcontainers.

All-transitions, reopen, language/counter extremes, scaling and overflow-scrolling tests were not individually reported. Gameplay, percent parity and multiplayer remain open.

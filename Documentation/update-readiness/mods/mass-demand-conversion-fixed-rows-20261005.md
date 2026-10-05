# MDC fixed recipient rows — 2026-10-05

## Current status: user-confirmed visual result — 2026-10-05

After applying the fixed-slot implementation, the user reported: “ok, es sieht jetzt gut aus, dokumentiere den funktionierenden code.” This confirms the current presentation in game. The code below is now the reference for the user-accepted MDC layout, rather than an entirely unrendered proposal. [Dated confirmation and exact GUI checksum](../evidence/mdc-fixed-rows-user-confirmation-20261005.json) tie the report to the current source; the earlier verification/baseline remain unchanged historical evidence.

The reference implementation is [the standalone GUI](../../../Mass%20Demand%20Conversion/gui/decision_view_widgets/mdc_decision_chance_filter.gui). Preserve its complete geometry chain: explicit scrollbox size and inner replacement widget; five permanent slots; fixed-size, zero-origin variant wrappers/items; fixed native-derived button content. Do not replace this chain with intrinsic flowcontainer sizing, caption-width-only changes or the previously failed flexible-space compositions. Filtering selects the overlapping variant within a slot and must not alter the slot or content dimensions.

This is a visual confirmation from the user, not an individually logged pass for every first-open/filter-switch/reopen combination, language, scaling, large counter or scrolling scenario. Those checks remain regression requirements. Request delivery, percentage parity, negotiations and multiplayer are not certified. No new compatibility/release metadata follows. Sections below record the implementation and its earlier pre-confirmation acceptance gates.


Standalone **1.079**, installed/reference Vanilla **1.20.0.3**. [Source audit](../evidence/mdc-fixed-rows-source-audit-20261005.json), [verification](../evidence/mdc-fixed-rows-verification-20261005.json), [failure ledger](mass-demand-conversion-gui-failures-20261005.md).

## Observation and source audit

User screenshot91dc2d7b and report disprove the preceding fixed285×30 caption correction: all rows are left-aligned on first opening; after percentage switches the three changing recipient groups and two unchanged groups have different origins. The native radio-label flowcontainer and eleven separate auto-sized datamodel wrappers do not provide one common fixed geometry. This is a verified source structure and observed failure, not proof of the Engine's internal update ordering.

Reviewed the complete decision insertion/custom-widget chain, preload widget/button defaults, native scrollbox/scrollwidget replacement block, margins/scrollbar, native decision controller, radio-label/radio/text presentation and positioned datamodel/widget examples. Eight installed sources match the pinned Git1.20.0.3 blobs without checkout changes. Native exposes scrollbox_replace_vbox; the new layout overrides that entire inner content wrapper, so native Scrollbox_Margins no longer applies there. Its15-unit vertical inset is explicitly reproduced; horizontal geometry is centered directly in514 units. Earlier62 watches are retained verbatim; one positioned-widget example watch is added.

## Targeted implementation

The root514×250, filter514×32, gap8, scroll514×210, initialization and full filter subtree are unchanged. Scroll mechanics/background/scrollbar remain native. A widget514×204 replaces the scrollbox's automatic inner vbox. Five permanent470×30 slots begin at x22 and y15/51/87/123/159. The three relevant variants overlap their group slot at0/0; courtiers/house use one variant each. Every wrapper/item has explicit size and limits plus top|left parent/own origins. Only visibility/selection/name/count change with filter, never source geometry.

The uniquely prefixed mdc_fixed_recipient_option derives from native button_group. It retains tooltip_se, native button_radio and the radio-label round background, clickable text formatting and transparent text. Each470×30 full-row click area contains a fixed320×30 body at75/0: radio30×30 at0/0, text285×30 at35/0, autoresize=no and left|nobaseline. Thus all radio origins are x97, all text origins x132; the shared body midpoint is257=514/2. No flowcontainer, flex expander, negative correction or intrinsic text measurement controls recipient placement.

The 11 datamodel slices/order, OnSelect callbacks, enabled/tooltip/frame/name bindings are retained. Caption geometry now belongs to the common type rather than each binding override. Local GUI state remains display-only. No decision/count/query/dispatch, localization, descriptor, notification override or bundle file changes.

## Verification and acceptance gates

26 static checks cover all eleven selections, five slots and variant origins, absent/invalid/default filter fallback, geometry invariance across all display modes, preserved filter/lifecycle tree and functional bindings, source native bindings versus Git, gameplay/count regressions, eight localizations and BOM requirements. These assertions inspect source; they do not run the CK3 renderer. See verification evidence for final preservation/source/link checks.

After a full game restart, compare first open, every group and filter transition, cancel/reopen. Radio/text columns must remain unchanged and no first-open overlap may occur. Check full-row clicks, selected mark, long translations, large counts, high UI scale and scroll mechanics when content exceeds the viewport. The204-high content normally fits210; absence of a scrollbar at this size is expected, not a scrolling test. Filter row must remain exactly as confirmed. No new rendered screenshot is available for this implementation.

Runtime rendering, percentage parity/rounding, request delivery, subsequent negotiations and two-player selection/desync tests remain open. No compatibility/MP certification, publication or metadata change.

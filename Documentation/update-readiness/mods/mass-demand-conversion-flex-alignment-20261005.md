# MDC flexible-space alignment correction — 2026-10-05

Standalone **1.079**, installed Vanilla **1.20.0.3**. [Feature source audit](../evidence/mdc-flex-alignment-source-audit-20261005.json) verified eight current native sources against the pinned Git reference before editing: option-list/detail insertion, scroll hierarchy/margins, button/radio defaults, expanding spaces, full-size button content hbox and preferred flowcontainer sizing. No shared native window or installed game file was edited.

## Diagnosis and user evidence

The latest supplied screenshot (codex-clipboard-4d994dd1-95bb-4f8c-bf26-4a4aede1fcc6.png) shows five groups inside the window, none marked, an indirect count of 21, filter-row inset and left-aligned recipient contents. It disproves the prior patch's intended recipient centering. The old tests asserted center-anchor presence and dimensions, without proving effective content allocation or rendered geometry. The exact internal Engine layout calculation is not established by the source audit.

The prior filter section still used a centered external flowcontainer. Recipient alignment relied on parentanchor=center on an intrinsically measured flowcontainer, without a full-size content box that allocates equal remaining space. The replacement makes width allocation explicit using native hbox/expand recipes; this is a source-informed correction awaiting game validation, not a claim that the renderer was exercised.

## Explicit layout contract

Root remains 514×250; filter 32, gap 8, scrollbox 210. The filter section is a plain widget with explicit 514×32 size; its inner viewport and five overlay wrappers share top|left / zero origin and full width. Selected outer hboxes retain visibility and ignoreinvisible handling, use 514-wide bounds and zero spacing, and contain exactly the fixed control group followed by a native expand. The control group is 451 wide: 120 + 125 + 100 + 100 + 3×2. All 63 spare units are assigned on the right. No centered filter-section anchor or negative compensation is used.

Only recipient rows use the local native-derived button type. The expanding 450×30 click region contains a size100%100% hbox with zero spacing and children expand / preferred-width content flowcontainer / expand. Identical growing expanders distribute remaining width equally; radio and caption remain together with five-unit spacing. Content uses vertical centering rather than the removed horizontal center anchor. Native button_radio/background, clickable label formatting, transparency and radio/text extension blocks are retained.

All eleven entries/order, datamodels, visibility expressions, selection/reset/initialization actions, enabled/radio/text/tooltip bindings are preserved. Query/count/send, eight localizations, effect explanation, notification overrides, bundle and 1.079 metadata remain unchanged.

## Static verification and baseline

**22 static tests passed**. Tests check the actual full-size container chain, ordered trailing/equal expanders, preferred content, explicit filter sizes/common origin, 451-unit control widths, hidden variants and full row click bindings, plus all existing selection/initialization/gameplay/localization/encoding regressions. Functional root binding multisets match the pre-edit source; the native recipient radio/text content is preserved apart from the specified alignment/layout properties.

[New dated baseline](../update-watch-mdc-flex-alignment-20261005.json) retains all 56 previous watches and registers newly audited dependencies: 58 total. Historical baselines and other-mod registrations remain. [Final evidence](../evidence/mdc-flex-alignment-verification-20261005.json) records source comparison, preservation and read-only checks separately from runtime results.

## Required game acceptance — pending

- Fully restart CK3. Filter heading starts at the widget's left content edge; all three controls including 100% fit in one line. Every recipient radio/caption pair is individually centered within its full row.
- Switch each group/filter; marking, group/filter retention, count refresh, cancel/reopen and native selection reset remain correct. Click near both edges of each row to confirm the full click region.
- Normal/increased UI scale, all eight languages, long labels and large counts: no clipping/overlap. Overflow retains working scroll wheel and vertical scrollbar.
- Existing unfiltered eligibility/count/send parity, paused-state native 80/100 threshold comparison including rounding/refusal/negotiation, and simultaneous two-player selection/OOS tests remain open.

New layout/rendering and gameplay/MP tests were not executed. No compatibility or multiplayer release approval; no publication. Source/static checks cannot promise successful Engine rendering.

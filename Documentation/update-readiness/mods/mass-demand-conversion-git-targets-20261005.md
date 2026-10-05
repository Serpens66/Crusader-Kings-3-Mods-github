# MDC Git recipient-list restoration and explicit filter origin — 2026-10-05

Standalone **1.079**, installed Vanilla **1.20.0.3**. [Source audit](../evidence/mdc-git-targets-source-audit-20261005.json) verified eight native files against the pinned reference before editing, covering decision insertion, native radio/scroll defaults, widget-backed datamodel items and explicit parent/widget anchor placement.

## Requested restoration and observed failure

The latest supplied screenshot (codex-clipboard-9d4e414b-0d96-4f92-a0e2-af3a33543c8d.png) shows direct/indirect rows overlapping on first opening, remaining groups below, none marked and count21 indirect vassals. The user also reports layout changes after switching percentages and persistent filter inset. Earlier static checks did not establish actual renderer geometry or initialization stability; historical reports remain intact and no successful rendering is inferred.

Git **a2df10b** predates the custom GUI: the decision used native decision_view_widget_decision_option_list_controller directly. Git **a81d7f3** contains the first chance-filter extension and its ordinary native radio list. The complete scrollbox subtree from that commit is restored **verbatim**, read with git show without checkout/reset. It retains the eleven registered entry slices and existing percentage-dependent five-group visibility. The earlier 470×30 native button_radio_label rows, ordinary vbox layout and six-unit list spacing return; the custom recipient type, extra flex boxes and expanding-content changes are removed. The root returns to the historical expanding vbox; viewport remains 514×210 within the 514×250 widget. This restores the Git layout rather than claiming a new full-row click contract or conservative 450-width calculation.

## Filter row above the list

Filter area is a direct, explicitly sized 514×32 widget. Each selected-group item is a 514×32 widget at zero origin, with **both parentanchor and widgetanchor top|left**. Group-item widgets overlay and selection visibility chooses exactly one; no hbox/vbox/flex allocation determines the heading's left edge.

Heading starts at x0 with 120×30 size and left-aligned text. The none/80/100 datamodel columns explicitly start at **122 / 249 / 351**, with **125 / 100 / 100** widths and 30 height. Each column's parent/own anchors and position are explicit. Three two-unit gaps give content ending at x451, leaving 63 units on the right. Native filter buttons, captions/tooltips, native OnSelect and local display-state bindings are unchanged.

All eleven registrations, five receiver policies, missing/unknown-state none fallback, create/show/hide/native-default initialization, query/count/send logic, eight languages, notification overrides, bundle and 1.079 release metadata remain intact. The effect explanation is unchanged. No game or installed-mod files are modified.

## Verification and source record

**22 static checks passed**, including a complete parsed-tree comparison with the Git scrollbox subtree, raw-text restoration check, no custom recipient type, explicit filter origins/positions/bounds, original native recipient bindings, five visible groups for valid/unset/unknown modes, all group/filter selection combinations and existing gameplay/localization/encoding regressions. Functional root binding multisets match the pre-edit source.

[New baseline](../update-watch-mdc-git-targets-20261005.json) retains all 58 previous watches and registers newly audited GUI recipe dependencies, 60 watches total. Historical baselines and other mod records are preserved. [Final evidence](../evidence/mdc-git-targets-verification-20261005.json) records source/preservation/read-only checks separately from user observations.

## Pending game checks

- Fully restart CK3. First opening: five distinct, non-overlapping native-style recipient rows; filter heading at the left content edge; none selected, all three controls fully inside the frame.
- Switch each filter and group repeatedly. Rows must not jump/overlap; marking, retained group/filter, counts and recipient selection must match. Cancel/reopen resets to default/none.
- Normal/increased UI scale, long translations, large counts, scroll wheel and vertical scrollbar. Check native row clicks and tooltip placement after restoration.
- Native eligibility/count/send parity, paused-state 80/100 chance comparisons and simultaneous two-player/OOS tests remain open.

The restored/new combination has not been rendered in game by this audit. No delivery, percentage, compatibility or multiplayer approval; no publication. Code/source checks do not promise runtime geometry.

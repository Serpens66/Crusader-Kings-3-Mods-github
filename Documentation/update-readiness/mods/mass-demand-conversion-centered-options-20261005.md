# MDC compact filters and centered recipient contents — 2026-10-05

Standalone **1.079**, installed Vanilla **1.20.0.3**. [Feature source audit](../evidence/mdc-centered-options-source-audit-20261005.json) completed before the patch: complete native option-list widget, radio-label/radio templates and button-group defaults, centered content flowcontainers, scrollbox and margins. Current sources match the pinned Vanilla Git reference. No shared window replacement or game-installation change.

## User-observed preceding layout

The supplied screenshot (codex-clipboard-bfba87c2-4831-4ebc-802c-46dbe50aef22.png) shows all five recipient groups within the window, none selected as filter, and 21 indirect vassals. Recipient content is still left-aligned; the 100% filter extends beyond the right edge. This supersedes the preceding patch's expected alignment; its historical source/test evidence is preserved. Sending, native percentage parity and multiplayer are not established by the screenshot.

## Current layout contract

The filter section retains its 514×32 area. All five selected-group overlay rows start at top|left / { 0 0 }; their content is **451** units wide: heading 120, none 125, 80% 100, 100% 100, plus three gaps of 2. The heading is left-aligned; 63 units remain on the right of the enclosing area. No negative compensating position is used.

Only the eleven recipient instances use the uniquely named **mdc_centered_recipient_option** button_group template. It copies native button_radio_label's tooltip_se, five-unit inner spacing, button_radio/background, clickable text formatting, vcenter label, transparent text and radio/text extension blocks. The single change to that native content is **parentanchor = center** on the auto-sized inner flowcontainer: radio and caption center together horizontally and vertically. The outer recipient buttons remain expanding 450×30, retaining the full click area and native OnSelect/IsEnabled/GetTooltip/IsSelected/GetName bindings. Filters retain native button_radio_label.

Root 514×250, 32-high filter, 8-unit gap, 210-high scrollbox, fixed eleven-entry order, fallback/create/show/hide initialization, all selection actions, localization, query/count/send logic, notifications and metadata remain unchanged. Bundle and unrelated user changes are untouched.

## Static checks and source monitoring

**21 static tests passed**, including exact 451-unit calculation, each column/button size, common left origin, centered inner recipient content and native template styling/blocks, all eleven native selection mappings and existing initialization, gameplay, localization and encoding checks. Original versus patched root-widget binding multisets match for datamodel, visible, onclick, on_start, frame, text, tooltip, enabled and trigger_on_create.

[New dated baseline](../update-watch-mdc-centered-options-20261005.json) preserves all 54 prior native watches and adds centered-flowcontainer and inherited button-group sources (shared/progressbars.gui and preload/defaults.gui), **56 watches** total. Prior baselines and other mod records are preserved. [Verification evidence](../evidence/mdc-centered-options-verification-20261005.json) records source freshness and preservation checks.

## Runtime acceptance — pending

- Fully restart CK3. Confirm 100% fits, three compact filters share one line, and all five recipient radio/caption groups are centered.
- Change each group and filter; verify marking, group/filter retention and counts. Cancel/reopen must reset GUI and native selection to none/default.
- Normal/increased UI scaling, all eight languages, long captions and large counts: no clipped text or overlapping controls; full-row clicks select correctly. Test scroll wheel and vertical scrollbar on overflow.
- Existing count/query/send parity, paused-state native 80/100 comparison including rounding/refusal/negotiation, and simultaneous two-player selection/OOS tests remain open.

The new layout has not been rendered in game by this audit. No sending, percentage, multiplayer or compatibility release approval; no publication. Version stays 1.079.

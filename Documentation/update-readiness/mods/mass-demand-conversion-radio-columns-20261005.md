# MDC common recipient radio/text columns — 2026-10-05

Standalone **1.079**, installed Vanilla **1.20.0.3**. [Feature source audit](../evidence/mdc-radio-columns-source-audit-20261005.json) verified native radio-label content, radio/group defaults, fixed/autoresize text sizing and native radio text-block overrides before editing. No new button type, container, position or expander.

## User-confirmed preceding result and requested appearance

User screenshot **808b7d31-6b73-4fe2-b65a-f54db7a9b698** and the accompanying statement confirm the preceding explicit514×210 scrollbox correction places the list centrally and all five groups are visible. The left filter row remains within the frame. This is partial user-run visual confirmation, not acceptance of every transition, scale, language, send/percentage or MP case. Screenshot **bf7803d8-e94b-4358-8261-c92c785b69e6** is the requested reference: one vertical radio column and one shared left text origin within a centered overall list block; it shows a historical four-category view, without removing the current fifth category.

Current labels had varying measured widths, moving radio circles between individually centered rows. The requested patch gives every recipient caption the same width, while retaining the normal native radio-label composition.

## Exact patch

Only eleven recipient **blockoverride text** nodes receive size/minimumsize/maximumsize={285 30}, autoresize=no and align=left|nobaseline. Entry.GetName and all other fields remain unchanged. Native radio width30 plus spacing5 plus caption285 gives the same **320**-wide content allocation for each row; names/count lengths no longer determine row width. Actual common-column/centered rendering remains a game-test gate.

The complete root tree matches the preceding widget after removing exactly those five added caption properties. Filter subtree, explicit514×210 scrollbox and limits, root250-high bounds, row spacing6, native470×30 button rows, eleven item routes, state reset, marker/click/enabled/tooltip expressions, eight localizations, gameplay/query/count/send, notifications, bundle and1.079 metadata are retained. No changes to the three chance-filter captions.

## Verification and preservation

**24 static tests passed**: new common-column check covers all eleven captions and unchanged15 filter caption instances. The Git subtree test permits only the previously added viewport size and these five caption properties; all other native list content must still match. Existing selection/initialization/gameplay/localization/encoding regressions remain active. Structural comparison and functional binding multisets verify the scoped change.

[New dated baseline](../update-watch-mdc-radio-columns-20261005.json) preserves all 61 prior watches and records 62 total. Historical baselines and other-mod records are retained. [Verification evidence](../evidence/mdc-radio-columns-verification-20261005.json) records freshness, scope and read-only checks. [Failure/evidence ledger](mass-demand-conversion-gui-failures-20261005.md) adds the user's confirmation of the earlier size correction without treating the new geometry as tested.

## Pending game acceptance

Fully restart CK3. Confirm all five radio centers share one vertical line and captions start at the same x coordinate, with the common content block centered. First open, repeated group/filter changes and cancel/reopen must not overlap or jump. Check long text in all eight languages, large counts, normal/increased UI scale, tooltip/readability and scrolling. If fixed caption width clips labels, record it as an unresolved layout failure rather than releasing or changing translations to fit. Existing native count/send parity,80/100 UI comparison and simultaneous two-player/OOS tests remain open. No compatibility/MP approval or publication.

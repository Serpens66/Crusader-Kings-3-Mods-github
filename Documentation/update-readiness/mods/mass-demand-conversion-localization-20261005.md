# MDC localization and version 1.079 — 2026-10-05

All eight standalone languages were reviewed against the English meaning: **34 unique keys each**, complete key parity. The supplied Korean translation replaces the remaining English labels/tooltips/button, including both new indirect-vassal filter labels. Its house wording is aligned with installed Vanilla: `game_concept_house` is 집안, while `game_concept_dynasty` is 가문. The mod's house-only group consistently uses 집안 구성원. Existing native concept links, ScriptValue bindings, recipient expressions and tooltip composition are preserved.

German tooltips now have the missing comma and one final period. Polish indirect-vassal wording no longer repeats pośrednich, and its tributary action matches the other imperatives. Chinese tributary text now requests conversion from differently believing targets rather than implying nonreligious targets; category terminology agrees with the filter note. English uses House members. French uses consistent action wording, plural requests, acceptance probability and Maison; Russian uses consistent indirect-vassal terminology/action wording; Spanish uses consistent Casa capitalization. Acceptance remains distinct from later negotiations and completed conversion in all eight languages.

## Verification and preservation

- Eight files × 34 unique keys; every key, quoted entry, internal reference and filtered count binding checked.
- Functional placeholders and escaped line breaks match the pre-edit file **per key**; Korean has no remaining English literal UI text.
- Existing UTF-8 BOM and each file's line-ending style retained. Exact UTF-8 decoding/encoding used throughout.
- **16 existing static MDC tests passed**. Machine results and changed-key lists: [verification evidence](../evidence/mdc-localization-verification-20261005.json).
- Both standalone descriptors now have `version="1.079"`; supported version, Workshop identity, local path and other descriptor bytes are retained. This is the explicitly requested mod-version increment, not a new compatibility certification.
- The [new dated baseline](../update-watch-mdc-localization-20261005.json) retains all 49 Vanilla watches, Engine reference and other mod registrations; only the MDC local snapshot and update annotation change. Earlier baselines and reports remain untouched.
- Gameplay, widget, notification overrides/messages, bundle and pre-existing unrelated user changes remain untouched by this localization update.

## Runtime boundary

No in-game language rendering, truncation/wrapping or tooltip test was run. Existing [GUI lifecycle/order, threshold-UI comparison and two-player tests](mass-demand-conversion-chance-filter-20261005.md) remain pending. Neither the version increment nor static checks grant compatibility/MP approval. No publication or game-installation change occurred.

Final selected-mod check: **49 native sources unchanged**, recorded Engine exports unchanged. Snapshot comparison found no unexpected existing-file changes or missing files; all three earlier dated baselines are byte-preserved. Diff whitespace checks pass.

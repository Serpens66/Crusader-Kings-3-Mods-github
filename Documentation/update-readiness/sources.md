# Sources and audit boundaries

All local sources were accessed on **2026-10-03**. The installation baseline is **1.20.0.3 (Crozier)** from `E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\launcher\launcher-settings.json`, with its hash in [workspace baseline](evidence/workspace-baseline.json). The executable did not previously expose an independent ProductVersion. No Steam integrity check or game launch was performed.

## Reproducible local evidence

| Evidence | What it establishes | Limit |
|---|---|---|
| [Workspace baseline](evidence/workspace-baseline.json) | Recorded hashes of all 853 non-Documentation, non-Git files, version metadata and Git status | Preservation manifest, not a backup of file contents; no source edits were needed |
| [Source closure](evidence/feature-source-closure.json) | Complete-file read hashes for 1,208 unique native files, per-package counterparts, developer references and literal dependency edges | Overinclusive discovery; not a semantic call graph or macro expansion |
| [Collision records](evidence/conflicts.json) | All same-path cross-package overlaps, same-directory top-level ID candidates and native same paths | Nested GUI types and localization replacements require separate inspection |
| [Native ID candidates](evidence/native-id-overrides.json) | Native IDs under the same database directory even when filenames differ | Lexical candidates, not a general loader precedence rule |
| [Exact-path differences](evidence/override-diffs.json) | Changed line ranges between source files at the same path | Added `11_` GUI files need type-level comparison with differently named native files |
| [Define comparison](define-comparison.md) | All 23 active namespace/key pairs and current values | Engine calculations and balance are runtime tests |
| [Static asset consumers](asset-consumers.md) | 5,830 complete native text reads; all 677 textures searched for exact path, basename and symbolic consumers | 84 textures have exact path matches; dynamic/compiled loading remains unresolved |
| [Feature file map](evidence/feature-file-map.json) | All 803 files in retained content roots assigned to sheets/work packages | Group assignments are navigation evidence, not a passed engine audit |
| [Texture comparison](texture-comparison.md) | All 677 texture files in retained graphical packages, containers and dimensions | No render/format acceptance test; missing same-path file does not mean unused |
| [Entry points](entry-points.md) | Every lexical top-level gameplay definition in retained roots | Does not enumerate nested options as separate public IDs |

The baseline was refreshed during discovery and then made immutable. Two OUTDATED.txt markers appeared in excluded Knight Manager roots, increasing the count from 851 to 853; [workspace observations](evidence/workspace-observations.json) records this explicitly. Verification uses the final recorded baseline, while the prior native/mod index is independently checked.

The baseline also protects excluded Knight Manager roots, `test`, AGENTS.md, README.md, descriptors, thumbnails, shortcuts and the pre-existing `.gitignore`. Existing user changes are kept byte-for-byte; no commits, resets or stashes were created. Generated manifests and authored reports are all under `Documentation`.

## Reviewed native contracts

Paths below are relative to `E:\ProgrammeE\Steam\steamapps\common\Crusader Kings III\game`. Use [local lookup](../reference/index-guide.md) for full context; hashes are in the closure or native index. Line numbers locate the actual inspected statements rather than implying a whole file is executable API documentation.

| Ref | Native source and location | Established topic |
|---|---|---|
| DEC | `common/decisions/_decisions.info`, picture/reference and widget sections; current native decision callers | Current decision schema, character root, selected option controller |
| EVT | `events/_events.info`, override section at 75–84 and event stages | Event namespaces/stages and current priority rules; not evidence that inactive mod events execute |
| INT | `common/character_interactions/_character_interactions.info:242–262,377–399,562–573` | Actor availability versus pair context; on-send versus on-accept; deprecated AI potential |
| CONV | `common/character_interactions/00_religious_interactions.txt:158,508,780`; `common/scripted_triggers/00_religious_triggers.txt:1198` | Courtiers, house/bloc and vassal/tributary routing; protection, domicile and diarch conditions |
| CONVE | `common/scripted_effects/00_religious_interaction_effects.txt:1220`; `common/scripted_effects/00_interaction_effects.txt:4793` | Conversion effects and dependencies; newer religion consequences remain in native interaction dispatch |
| EXC | `common/character_interactions/00_religious_interactions.txt:3163,3642`; `common/scripted_effects/00_religious_interaction_effects.txt:3` | Three required macro parameters, issuer tracking, current authority/redirect and consequence chains |
| RITE | `common/scripted_triggers/00_religious_triggers.txt:539`; `common/scripted_triggers/pam_scripted_triggers.txt:1083,4269`; religion/rite/tenet/doctrine `.info` and definitions | Rite-based crime helper and sacraments; faithful mapping of custom temporal authority remains unresolved |
| WAR | `common/character_interactions/00_alliance.txt:2055`; `common/character_interactions/06_ep3_laamp_interactions.txt:7971,7992,8339`; war/CB `.info` | Current join/removal callers; source occurrence does not establish all permitted participant removals |
| WARC | `common/scripted_triggers/00_war_and_peace_triggers.txt:844`; native caller `common/important_actions/00_war_actions.txt:127,218` | Join helper also requires a valid war in `scope:target`; two explicit macro arguments alone are insufficient |
| ON | `common/on_action/_on_actions.info:122,131–149`; `war_on_actions.txt:18,312`; `death.txt:1–7`; `court_maintenance_on_actions.txt:34–38` | Additive child hooks; separate effect/event chains; joiner/war, attacker/defender, pre-death/killer, departing courtier/old employer |
| IA | `common/important_actions/_important_actions.info:12–19`; native important-action definitions and UI callers | Only interface effects in action discovery/click; player root and saved targets |
| PAY | `common/character_interactions/00_gift.txt:110,171` and dependencies | Actor-side `pay_short_term_gold`; full budget semantics need the current engine export |
| VALUE | `common/script_values/_script_values.info`, modifier/effect localization references | Source-order math and `min` floor; no unexecuted payment/expiry claims |
| DEP | `common/scripted_effects/07_dlc_ep3_scripted_effects.txt:12779–12835`; callers and `ep3_laamps.0002` dependencies | Modern deposal can offer landless continuation, so it is not a proven drop-in for “continue as heir” |
| GUI | `gui/game_rules.gui`, `gui/multiplayer_types.gui:1898–2050`, GUI developer references and callers | Old type replacements need current nesting; designer calls now carry character-type arguments |
| ATLAS | `gui/shared/portraits.gui:12–25`, `gui/window_ledger.gui:7277`, native and mod DDS headers | Current rank texture is driven by title tier frames; dimensions alone cannot certify replacement layout |
| LOC | Native `localization/english` and `localization/german` health/tooltip entries and callers | CustomDefines replaces existing health description keys; UI datatype signature/rendering remains a gate |

## Internet corroboration

| Source | Access date | Version/role | Use |
|---|---|---|---|
| [Tiger upstream](https://github.com/amtep/tiger) | 2026-10-03 | Current README; compatibility with this exact installation not certified | Optional validator scope and documented update lag/false positives; nothing installed |
| [Paradox Making Mods diary](https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-37-making-mods.1410656/) | 2026-10-03 | Historical official developer guidance | Debug workflow background; current exported commands still need in-build confirmation |
| [Existing source catalogue](../research/sources.md) | Original research 2026-10-03 | Mixed dated developer/Wiki/reference material | Background only; does not override current native contracts |

Historical version tables may help identify change dates, but matching current exports have not been established. This report relies on the installed source differences rather than claiming an exact release-by-release migration history.

## Open evidence requirements

The current user logs are from 2025 and cannot certify this baseline. Obtain current `script_docs`, UI `dump_data_types`, the executed build/checksum, DLC configuration and clean-start logs through [the user run](debug-run.md). Engine primitive contracts, GUI precedence, consent-query context creation, delayed scope survival, payment accounting and render acceptance remain explicitly gated where relevant.

Successful file reading or matching a symbol is never recorded as a passed semantic audit. A later implementer must close the exact gate before choosing unknown behavior, then record the final feature audit and runtime results next to the package sheet.

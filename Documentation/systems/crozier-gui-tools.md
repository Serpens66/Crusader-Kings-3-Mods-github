# Crozier GUI, assets and development tools

Baseline: **1.20.0.3**, checked **2026-10-03**. [Coverage](../research/crozier-source-coverage.md), [local evidence](../research/general-120-evidence.json). GUI rendering, external validator, gameplay and multiplayer: **not run**.

## Data bindings and localization

The installed data-type export registers `DataModelJoinList(Arg0, Arg1, Arg2)` returning a string. Its description processes items and separators through localization keys and names `ITEM_INDEX` and **`IS_LAST_ITEM`**. The release instead names **`IS_LAST_INDEX`**, and mentions additional size/number tokens. This is an explicit source discrepancy: do not quietly normalize the names or advertise all tokens as tested. Verify the actual localization consumer with a one/many-item render probe before adopting it.

Boolean bindings include multi-argument `And`/`Or`/`Nor`/`Nand` families; retrieve registered signatures and owning types from the current data-type index rather than assuming every name is global. The release also describes integer-to-boolean casting. Script trigger blocks, script-value syntax and GUI expression syntax are different readers; availability in one does not imply support in all.

Database scope `Custom()` support should be resolved against its actual registered owner and the applicable customizable-localization definition. Avoid pasting a character-specific `Custom()` example into a government/Rite-type binding without checking context.

`common/morpheme_strip_rules/00_morpheme_strip_rules.info` documents localization formatters with `|:rule_name`. `seek_from` defaults to tail; rules run top to bottom, with the first match selected. Successive match blocks inspect characters from the chosen end inward; `strip` determines how many characters are removed. No match preserves the input. Test accented strings, short names and each supported language rather than assuming English suffix rules generalize.

Dynamic scoped decision selection and `PdxGuiWidget.MakeDecisionTypeWithParam` are covered in [Puppets and selection](puppets-and-selection.md). Controller, item type and GUI context must agree.

## Portraits and other graphics

`gfx/portraits/portrait_animations/_animations.info:7–49` distinguishes top-level portrait modifiers, animation variants, packs (`*.animationpack`) and independent modifier sets. Each set uses its first valid modifier; multiple sets apply independently. `force` changes whether top-level overrides are copied as fallback or added to variant modifiers. This is not equivalent to selecting one global first-match modifier from the whole animation.

Wappen definition/frame overrides, government realm-mask settings, event portrait `stacking_order` and no-portrait assets belong to their individual schemas and GUI consumers. Asset existence is not proof of correct presentation, precedence or DLC accessibility. The release's expanded accessory-index limit is a declared engine change; the maximum-range/DNA behavior has not been independently exercised in this workspace.

Keep the existing graphics acceptance boundary: source registration, texture hashes and a valid binding are static evidence; masks, consumer permissions, z-order, missing assets and actual rendered appearance require GUI tests.

## Command-line reference and diagnostic stages

The complete local `game/_commandline_options.info` is now part of the source evidence. It documents, among other options:

| Option | Documented purpose / limit |
|---|---|
| `-bookmark=<key>`, `-play=<title>` | Select bookmark/start year and player title |
| `-random_seed`, `-designer_seed` | Reproducible game/designer seeds; not a universal promise of deterministic multiplayer behavior |
| `-logprefix`, `-logpostfix` | Distinguish comparative or multiplayer diagnostic logs |
| `-shutdown_after_history` | Stop after history setup; cannot certify later campaign outcomes |
| `-skip_checksum` | Skips local checksum calculation and prevents working multiplayer according to the reference |
| `-run_console_action_main` | Very early main initialization |
| `-run_console_action_clausewitz` | Engine-initialized stage |
| `-run_console_action` | Game-initialized stage |
| `-command_line_help` | Registered options/actions; the reference warns registration is not complete |

These are documentation, not launch instructions being executed. Do not change a user's launcher, playset or diagnostic profile merely to read an API. The file also includes specialist graphics/thread/memory/optimizer and automated-testing options; their presence does not make them appropriate defaults.

## Cold start, hot reload and release-only notes

Event priority has an explicit hot-reload exception. History overrides combine selected entries rather than universally replacing objects. A successful reload cannot certify a cold-start merge, nor can a successful startup certify a campaign callback.

The release describes reload fixes for laws, on-actions and war history, holy-site type reload and river graphics reload. River crossings are a separate gameplay boundary. It also describes query-field history, improved perspective/blocker diagnostics and local/Workshop coexistence. These are **release-only observations**, not locally tested guarantees. Full behavioral testing and any performance claims remain open; neither an announcement nor a schema read substitutes for them.

## Tiger and Wiki evidence

The [Tiger repository](https://github.com/amtep/tiger) describes syntax, references, localization, scope and history checks, warns about false positives/update lag, and documents JSON reports plus configuration/comment suppression. Its [filter guide](https://github.com/amtep/tiger/blob/main/filter.md) distinguishes severity, confidence, diagnostic key and file filters; its [annotation guide](https://github.com/amtep/tiger/blob/main/annotations.md) covers local suppression comments. These are Tiger configuration readers, not Jomini gameplay contracts. Suppression records must explain the source evidence and scope of each accepted warning; do not silence a whole category merely because one diagnosis was false.

The inspected [trigger table](https://docs.rs/tiger-lib/latest/src/tiger_lib/ck3/tables/triggers.rs.html) explicitly labels its update baseline **1.18.1**. The [effect table](https://docs.rs/tiger-lib/latest/src/tiger_lib/ck3/tables/effects.rs.html) has a malformed version comment; it cannot certify 1.20 support. Their optionality/choice validators describe Tiger's schema, not the CK3 Engine's undocumented defaults. Their `Removed` entries and TODOs are investigation leads requiring current installed evidence.

The previously found Wiki effect/trigger mirrors repeat historical exported declarations and do not settle script-created options, cooldown stages or acceptance defaults. Local retained 1.20.0.3 exports and complete relevant native callers remain the current baseline. No Tiger binary was installed or run, and no existing runtime status was promoted.

## Legacy-window source supplement

[Scrollable Legacies history](dynasty-legacies.md) documents a content scrollbox while retaining grid/item data bindings and native tooltip/progress consumers. Current native house and legacy windows already contain relevant scroll layouts. Their exported functions include unregistered result types; container presence does not prove frame correctness, unlimited item performance or compatibility with an entire historical replacement window.

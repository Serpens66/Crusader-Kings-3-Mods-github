# Mass Demand Conversion notification update — 2026-10-03

Standalone **1.078**, declared target **1.20.***; audited installation **1.20.0.3 (Crozier)**. Implementation completed; **gameplay, GUI, multiplayer and Tiger: not run**. Metadata is a release target, not runtime certification.

The feature-specific Vanilla source audit for replacing the two acceptance notifications was completed before the mod edits. This closes that narrow source-audit task only. Earlier G01–G05 questions about unchanged query/dispatch defaults, option initialization, validation, family-list lifecycle, UI counts and multiplayer remain open. The [historical static migration review](mass-demand-conversion-static-migration.md) still records that no mandatory functional migration patch was demonstrated for 1.077. This update adds the separately requested notification behavior; it does not infer a candidate or dispatch defect.

[Pre-edit source, export and preservation evidence](../evidence/mass-conversion-notification-audit-20261003.json) · [New static verification](../evidence/mass-conversion-notification-verification-20261003.json) · [Read-only checker](../../tools/audit_mass_conversion_notifications.py) · [Test matrix](mass-demand-conversion-tests.md)

## Changed package files

- [Internal descriptor](../../../Mass%20Demand%20Conversion/descriptor.mod) and [launcher descriptor](../../../Mass%20Demand%20Conversion.mod): `version="1.078"`, `supported_version="1.20.*"`; name, Workshop ID 2753176859 and external local path preserved. Existing BOM-free UTF-8/LF descriptor bytes are retained except for the two version values. Existing UTF-8 BOM is retained; the edited event keeps CRLF and existing localization keeps LF. New script files use UTF-8 BOM/CRLF. Original localization content remains byte-identical before the appended keys.
- [Vassal acceptance override](../../../Mass%20Demand%20Conversion/events/religion_events/accept_conversion_notification.txt): replace the commented experiment with only `religious_interaction.2002`.
- [House acceptance override](../../../Mass%20Demand%20Conversion/events/interaction_events/mdc_house_conversion_notification.txt): define only `char_interaction.0181`.
- [Own message type](../../../Mass%20Demand%20Conversion/common/messages/mdc_conversion_messages.txt): `mdc_conversion_accepted_message`, `display = feed`, `combine_into_one = yes`, `icon = "religious"`, `style = good`. No global message type or message filter is overridden/copied.
- Append `mdc_conversion_accepted_title` and `mdc_conversion_accepted_desc` in the eight existing English, German, French, Spanish, Polish, Russian, Korean and Simplified Chinese localization files. The text reports acceptance only. Native `event_message_effect` supplies the tooltip template; conversion previews remain tooltip-only.

Decision, five categories, script values, protection guards, costs, native interaction options, cooldowns and the older SerpInteractionsDecisions package are unchanged. No game files, installed mod files, tools, Workshop publication or launch configuration were modified.

## Current definitions and all native callers

Paths below are relative to the installed `game` root. Exact object boundaries/callsite lines and original-byte SHA-256 are in the evidence. Searching the complete installed text corpus found exactly four direct dispatches, all in `common/character_interactions/00_religious_interactions.txt`:

| Interaction / callsite | Event | Root and saved scope contract |
|---|---|---|
| `demand_conversion_interaction`:613 (object 508–778) | `char_interaction.0181` | Enters `scope:puppet_or_actor` before dispatch; event ROOT/this = effective requester; saved actor = interaction actor/puppeteer, recipient = conversion target |
| `demand_conversion_vassal_ruler_interaction`:920 (object 780–1383) | `religious_interaction.2002` | Enters `scope:puppet_or_actor` before dispatch; event ROOT/this = effective requester; saved actor = interaction actor/puppeteer, recipient = conversion target |
| `demand_conversion_minister_rites_interaction`:1792 (object 1692–2034) | `religious_interaction.2002` | Enters `scope:puppet_or_actor` before dispatch; event ROOT/this = effective requester; saved actor = interaction actor/puppeteer, recipient = conversion target |
| `attempt_conversion_of_local_ruler_interaction`:8718 (object 8543–9078) | `religious_interaction.2002` | Enters `scope:puppet_or_actor` before dispatch; event ROOT/this = effective requester; saved actor = interaction actor/puppeteer, recipient = conversion target |

`religious_interaction.2002`: `events/religion_events/religious_interaction_events.txt:1271–1336`. `char_interaction.0181`: `events/interaction_events/character_interaction_events.txt:1444–1464`. Their complete definitions were read again, including immediate and single-option effects. No caller was changed. The event definitions retain inherited named scopes rather than manufacturing a MDC marker or replacing the receiver with `scope:actor`. `send_interface_message` executes in the current event-receiver character scope, with `left_icon = scope:recipient`.

The effect is global for every caller of these IDs, including manual demands, Minister of Rites compelled conversions, local ruler conversions, and future callers that use the same IDs. There is no proof of a MDC-specific event contract and no artificial restriction was added. Accepted courtier requests already use their native `send_interface_message` at lines 250–263; that interaction remains untouched and uses its existing message type, so it is not promised to combine with the new type.

Acceptance does not certify that the recipient/family already converted: native `demand_conversion_interaction_effect` selects family and initiates `false_conversion.0900`, retaining possible secret-faith handling. Minister conversion may supply `scope:conversion_rite` rather than the requester's own rite. New text therefore names acceptance without naming a possibly wrong destination faith or claiming completed family conversion/study.

## Effect-by-effect mapping

| Native block | New execution | Proof / distinction |
|---|---|---|
| 2002 immediate, government-dependent common/vassal conversion helper | Same ordered `if`/`else` inside message, both under `show_as_tooltip` | Export states tooltip-only effects do not execute. No second family selection, conversion, hook use or conversion-event dispatch |
| 2002 immediate, `has_title = title:e_minister_of_rites` | Same `if` directly in hidden `immediate` | `change_influence = minor_influence_gain × recipient.primary_title.tier`; `add_piety = minor_piety_gain × recipient.primary_title.tier`. Native values currently 30 and 50 respectively, retained as references |
| 2002 immediate, puppeteer notifier | Same helper before response rewards | `TYPE = event_toast_effect_good`, `TITLE = religious_interaction.2002.toast_puppeteer` unchanged |
| 2002 sole answer, adventurer condition | Entire executable `if` moved directly into hidden `immediate`, once | Same `landless_adventurer_government` and recipient tier >= barony conditions. Faith fervor: `trivial_fervor_value × highest_held_title_tier` (currently base 0.15), same reason key. Prestige: 200 × tier, doubled for >= kingdom. No hidden-option auto-selection dependency |
| 0181 immediate, puppeteer notifier | Same helper directly in hidden `immediate` | `TYPE = event_toast_effect_good`, `TITLE = char_interaction.0181.toast_puppeteer` unchanged |
| 0181 sole EXCELLENT answer | Same common conversion helper inside message under `show_as_tooltip` | The answer contained no executable gameplay reward; only its preview moves |

The checker compares ordered parsed blocks against live Vanilla: 2002 gameplay = native immediate excluding its first preview `if`/`else`, followed by the old answer without its name; 0181 gameplay = original immediate. Preview blocks are separately identical. Rewards stay outside the message and appear once in the scripted execution path. This establishes static preservation, **not observed runtime execution counts**. Removing the letter means adventurer answer rewards now execute when the hidden event runs, without waiting for a click.

`notify_puppeteer_of_outcome_effect` is fully read at `common/scripted_effects/00_interaction_effects.txt:8–24`. Its guards remain native: actor exists, puppet_or_actor exists, `scope:is_puppet_action ?= yes`, actor != recipient. It sends a good toast to actor with puppet and recipient icons. Its additional puppeteer toast is intentionally retained; it is not a confirmation popup and is not converted into the shared feed type. Tooltip conversion helpers and their wrapper/family-selection definitions were traced separately; all gameplay conversion remains owned by the native interactions.

## Loader and message contracts

`events/_events.info:75–81`: the highest `id_override_priority` wins; Vanilla defaults to 0; equal priorities for equal IDs are an error. Both replacements set **1** and replace the entire corresponding event definition in distinct mod filenames. This is not a field merge or a whole-file replacement. Another mod defining either ID at priority 1 conflicts; a higher priority wins over MDC, a lower one loses. Filename/load order is not a substitute for this contract. Re-audit both complete native events after future game updates, since new upstream consequences are not automatically merged.

The native reference warns that hot reload may ignore priority. All required acceptance tests must begin with a **complete game restart**, not a live file reload. Runtime loading remains untested.

`common/messages/_messages.info:61–64` documents merging messages of one type when one already exists in the feed, suppressing repeated animation/sound. Native examples include `msg_artifact_gained` and `msg_pam_great_schism_progress`. The religious icon/style follows `event_religious_good`; its global `event_outcome` filter is deliberately omitted. Merging proves neither an aggregate count nor a retained recipient list. Which name/icon/tooltip survives, whether dismissed messages create a new entry, and actual per-player delivery remain runtime tests.

The verified 1.20.0.3 engine export at `effects.log.raw:9999–10014` says `send_interface_message` sends to the player of the current character and then executes contained effects; character icons are supported. `show_as_tooltip` at 2852–2853 explicitly does not execute. Only previews are contained in the new messages, so the message has no second copy of an executable reward/conversion. `$EFFECT$` is the native effect-tooltip template, not a conversion counter.

## Source freshness and historical comparison

Launcher metadata was re-read from `launcher/launcher-settings.json`: **1.20.0.3 (Crozier)**. The sources below were hashed in original bytes. Relevant export source hashes were checked against the versioned index. Current 1.20.0.3 historical blobs match installed event definitions; the pinned history is a third-party source mirror, not a Steam depot attestation.

| Native source | SHA-256 |
|---|---|
| `events/_events.info` | `ccd628f42374eb300199a2676bde45ba60af0be056290f191bfc72461910a5fd` |
| `common/messages/_messages.info` | `a0ad5c695a34f2be2fda1353164afdf48b7a6ce69ca2cabc9ab8d89bdcd392e4` |
| `common/messages/00_messages.txt` | `bd50b0859f3769bfbd2d592354c4a0b6883bf30be013240347a66589830c0730` |
| `common/messages/01_religious_messages.txt` | `7eae9939bafc0ad9856d7d9ffb200b61b6724fa347a1096e571eb00324a09689` |
| `common/messages/01_artifact_messages.txt` | `d24bf0eebf78dbd7ad6e66c11e546ea760636083e7a97f7a7912f5ec602ba4b3` |
| `common/messages/10_pam_messages.txt` | `30c1ad8f9a5a2c75bbd8e7d686107ecb9d641b354c98a9738d6d541f330c838b` |
| `common/character_interactions/00_religious_interactions.txt` | `63afe4538725929fb20bc20cbbbbc86705dba55a384755949431419265db0ac6` |
| `common/scripted_effects/00_interaction_effects.txt` | `4247f484295988b50098a43869d4c4056b7e0855bf8d5fa6ec0755cb996d7e82` |
| `common/scripted_effects/00_religious_interaction_effects.txt` | `9ecc22104b057e3425673917acbefaa320833226dd02b9a6c3dca7475b5b0928` |
| `common/script_values/00_basic_values.txt` | `c379cc0c58ed1574033f0e07a58697dfc6f8475c26aa4b117f2332008d4a27ef` |
| `common/script_values/07_ep3_values.txt` | `b4b46e562baa20f8aa7fbac91b3d8b95f6a59d053eaf6b5f28ca9d091f85c776` |
| `localization/english/messages_l_english.yml` | `6169d6a5735b958cd92a493dca0245e7d8eb366933fec9e3cfd440a8baf2e095` |
| `events/religion_events/religious_interaction_events.txt` | `27405d1ccd6217670f5812d8cbde987ed899c04b6b7d309099e2e8fbe1809a4d` |
| `events/interaction_events/character_interaction_events.txt` | `46d0e436bbb9694e60e46c0c1c5ebc3ae1c14afa041a8b8cd9548bd5c3836c69` |

Launcher SHA-256: `9cd6ff96f8092f2d21e1491b37e8344aa287faf69850563128ca1b117244a214`. Full export declarations and their raw-file hashes are retained in the audit JSON.

Git blobs were read without changing the reference checkout. Comparison pins: 1.19.0.6 `85e1ca4fcee5a1e2238b9db13c70a335fa94dac8`; 1.20.0.3 `0ec13350cde9e410b37a46d3616966838f4ba994`. In 1.19.0.6, 2002 already had Minister rewards and adventurer prestige, but lacked the puppeteer notifier and used literal fervor base 1; 0181 lacked the new notifier. Both current notifier calls and `trivial_fervor_value` are preserved. `10_pam_messages.txt` is absent in the older snapshot, not an error or evidence of unsupported current messages. Old reports/baselines/raw exports remain unchanged.

## Static validation and remaining acceptance

Executed validation is recorded in the linked verification JSON: encoding/BOM/CRLF, subset script parsing and balanced structure; exact two IDs/namespaces/priority/hidden form; shared unique message schema; eight-language key/template coverage; ordered gameplay and preview comparisons; complete native caller inventory; current source and 295 retained historical-seed checksums; documentation links and original-state preservation of all other mods and historical documentation. No full Engine parser, Tiger run, game load or gameplay test is implied. The old 1.077 migration checker has fixed 1.077/1.19 metadata assertions and preservation baselines; it is not rerun or rebased to claim a fresh 1.078 result. Its limited parser and brace reader are reused by the new checker.

Reproduce from the workspace root with the portable Python interpreter and `Documentation/tools/audit_mass_conversion_notifications.py verify`. The checker creates its new verification only once; subsequent runs compare it read-only. Audit mode is for the recorded pre-edit intake, not regeneration after edits.

All required gameplay cases **MC-N01–MC-N11 remain not run**: vassal/tributary and house feed delivery, unchanged courtier notification, mass merging and actual execution counts, Minister influence/piety, adventurer fervor/prestige, puppet delivery/toast, unchanged refusal/gold/favor/study decisions, pending save/reload and two players, and fresh error logs. Acceptance and later conversion must be counted separately. Complete source audit for these notification replacements does not close earlier query/default/lifecycle/GUI/MP gates or certify the release's runtime compatibility.

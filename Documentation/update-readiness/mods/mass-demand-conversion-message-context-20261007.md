# MDC 1.080 acceptance-description fix — 2026-10-07

Installed **CK3 1.20.0.4**, standalone **1.080**. [Source audit](../evidence/mdc-message-context-source-audit-20261007.json), [verification](../evidence/mdc-message-context-verification-20261007.json), [dated baseline](../update-watch-mdc-message-context-20261007.json).

## Observed defect and user acceptance test

The user tested an accepted vassal request without a crash. Screenshot804c928b shows ERROR:[recipient.GetShortUIName] in the feed description. The local error.log records failed type/promotion of recipient.GetShortUIName and a data error in mdc_conversion_accepted_desc. This confirms an acceptance-description localization defect. It does not demonstrate the cause of another user's reported crash or validate all conversion/reward consequences. The foreign crash remains unresolved. The house notification shares the same message type and absent per-send description, so it is structurally affected; no house error screenshot was supplied.

## Native pattern and targeted fix

Native msg_admin_provincial_army_request_denied uses desc=event_message_text in common/messages/07_ep3_messages.txt. Its caller in common/character_interactions/06_ep3_interactions.txt supplies the concrete desc directly inside send_interface_message, in actor context with scope:recipient available. Native localization defines event_message_text as $DESCRIPTION$. The runtime errors demonstrate that the old direct recipient expression was not available in our message-type description context. The new pipeline follows the complete native pattern; corrected MDC rendering still requires game verification.

The shared mdc_conversion_accepted_message now uses desc=event_message_text. Both religious_interaction.2002 and char_interaction.0181 pass desc=mdc_conversion_accepted_desc in their send_interface_message. The original eight translated recipient expressions are retained. Native message mechanics still own text capture/rendering; no guessed global scope, saved variable or new character flag is introduced.

Only the three notification script files and version fields in the two standalone descriptors change. Portraits, title, feed/combination properties, tooltips, conversion previews, executable rewards, native notifier, event receiver and OnSelect/send/query paths are retained. Both version fields are1.080; supported_version, Workshop ID, path and all other metadata are unchanged. GUI, localization and bundle are byte-preserved. The historical1.078 notification checker remains unchanged.

## Verification and open runtime gates

28 static tests pass, including both description transfers, all eight loc keys and recipient expressions, both1.080 descriptors, and exact ordered native event-effect/preview preservation after removing the added description field. Source audit covers9 relevant installed files; source freshness and complete preserved-file results are recorded in verification evidence. Prior63 watches retain their records and added native description-pattern sources are registered. The1.20.0.3 Engine exports are stale for the installed1.20.0.4 binary; a matching script hash is not compatibility certification.

After full restart, test an accepted vassal request and an accepted house request: correct recipient name and portrait, no ERROR:, no new corresponding localization errors. Check several consecutive/mixed acceptances, merged feed text/icon/tooltip and ordinary manual requests because the overrides are global. Recheck tooltip-only conversion and exactly-once rewards where relevant. All corrected-message game tests are currently **not run**. Existing percent parity, scope/list/negotiation lifecycle, scaling and multiplayer gates remain open. No publication or new compatibility/MP approval.

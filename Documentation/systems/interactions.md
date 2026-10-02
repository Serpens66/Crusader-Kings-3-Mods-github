# Character interactions

Primary contract: native `common/character_interactions/_character_interactions.info` (822 lines), current `00_gift.txt`, workspace interaction files, and [audit findings](../research/vanilla-audit.md). The [Wiki interaction page](../research/sources.md) is a short orientation and points to the native reference.

## Structure and context

Definitions belong in `common/character_interactions`. The native reference marks `category` as required. Use a current category and icon; localized description, prompts and acceptance/decline messages may be needed depending on the interaction workflow.

Do not assign one scope contract to the whole interaction. Local 1.20 documentation says `is_available` evaluates with the actor as root and is preferred over deprecated `ai_potential` for actor-only availability. `is_shown`/`is_valid` provide actor and recipient references. Outcome effects should explicitly enter the character whose state changes.

```text
# Fragment inside an interaction outcome effect.
scope:actor = {
    pay_short_term_gold = {
        target = scope:recipient
        gold = 5
    }
}
```

This uses a native payment form observed in the gift interaction. It expresses a transfer rather than separately destroying/creating currency. Production code must audit AI budget handling and the recipient/actor contract, and recheck affordability for its timing model.

## Distinct stages

| Field/stage | Question |
|---|---|
| `is_available` | Can this actor consider this interaction at all? |
| `is_shown` | Should it appear for this actor-recipient pair? |
| `is_valid` and failure-display checks | Is this particular setup allowed? |
| `can_send` | Can it be sent now? |
| `send_option` | What selectable inputs and flags are available? |
| `on_send` | What happens immediately upon sending? |
| `auto_accept` | Is the recipient's acceptance bypassed under these conditions? |
| `on_accept` | What happens after acceptance? |
| `on_decline` / block/intermediary stages | What happens on other responses? |

The reference has additional secondary actors/recipients, intermediaries, picked titles/artifacts/regiments and redirects. Audit those individually before using them. `auto_accept` does not replace eligibility checks or explain the player's consequences. The local reference marks `needs_confirmation` as deprecated, so it is not a recommended shortcut for a new interaction.

## AI and restrictions

Separate actor-only restrictions from pairwise target checks. The native reference recommends moving actor/global conditions out of `is_shown` into `is_available` to improve AI evaluation. AI target selectors, frequency, quick filters and `ai_will_do`/`ai_accept` use their own structures.

For a player-only utility, explicitly exclude AI from actor availability rather than relying on a zero weight as the only gate. For gameplay content, define target policy, response weights and costs, then test AI budgets and delayed replies. Copying the complete native gift interaction brings many unrelated struggle, opinion and AI behaviors; reuse only the audited capability that the feature actually needs.

## Delegating to a native interaction

Mass Demand Conversion shows `is_character_interaction_potentially_accepted` with a specific recipient and interaction key. This is a query about a native interaction, not a general proof that any later effect is legal. Trace the exact execution path too. Different recipient types use different conversion interaction IDs and restrictions.

Avoid replacing a native interaction with a direct faith/rite-changing effect merely to bypass UI. That can omit consent, restrictions, opinion changes, hooks, messages, conversions, costs or other associated behavior. Conversely, if the requested mod intentionally changes those rules, document the difference explicitly.

## Workspace patterns and limitations

`Leave Wars` saves several war scopes and opens an event selector; its source explains why the author avoided a particular hardcoded picker. This is a historical workaround to study, not evidence that the same engine limitation still applies in 1.20.

`pardon_hook_interaction` checks a usable hook, consumes it and adds an opinion modifier on the recipient. The full pattern crosses interactions, opinion-modifier definitions and localization. Reading only the `on_accept` block misses its displayed requirements and referenced assets.

## Tests

Test self-target, out-of-range/unavailable target, each prerequisite failure, exact balance boundary, send/accept/decline, duplicate send, disappearing target and state changes before reply. Check effects in the preview against actual results. For player-owned settings, test two players separately. For a transfer, verify both balances and one total payment.

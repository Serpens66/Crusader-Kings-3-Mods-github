# Leave Wars: targeted standalone update for CK3 1.20.0.3

Status: **implemented; source audit and static regression checks completed; gameplay, GUI and multiplayer acceptance not run**. This is not a compatibility release. Both descriptors remain at mod 1.121 / `supported_version="1.6.*"` pending actual acceptance.

The user authorized only the standalone distribution, the existing ten-option event, contract abandonment without payout, and two independent optional consequences **enabled by default**. The SerpInteractionsDecisions copy remains unchanged and is no longer identical to the standalone implementation. Do not activate both distributions together: their original interaction/event/localization IDs overlap.

## Evidence and historical limits

[Source audit and original working-file hashes](../evidence/leave-wars-source-audit-20261003.json) identify the recoverable original Git commit, original encodings/newlines, installed source SHA-256 and current exported declarations. The targeted current sources match the pinned mirror commit `0ec13350cde9e410b37a46d3616966838f4ba994`, allowing BOM/CRLF differences only. Current installed version was reread from launcher settings. The initial selected-mod check had nine unchanged watches and unchanged recorded engine exports.

The available history begins at `base/1.10.0.1`, commit `3da3da71feb3a0bbd075a75ac5601915df3ad2f0`. Searches did not yield a reliable 1.6–1.9 Vanilla source baseline. Consequently the source audit establishes current contracts and a scoped 1.10→1.20 comparison, **not a complete reconstruction of changes since the mod's 1.6 descriptor**. Import commit timestamps are not treated as game release dates.

Primary source chains reviewed:

- Interaction and event `.info`: actor/recipient scopes, availability, send/accept stages, inline option effects, option trigger/unavailable display. `save_scope_as` is documented for the unbroken event chain; direct event dispatch on actor remains unchanged.
- Current alliance interactions, adventurer departure/side-switch callers, war predicates and `remove_participant`: war root, character target, non-primary participant guards. No unverified `is_primary_war_attacker`/`is_primary_war_defender` aliases are introduced. `is_landless_adventurer` resolves to the native government-flag helper.
- FP2 assistance interaction state producers and complete payment/invalidated helpers: the character owns `owed_contract_assistance_war`, contribution and gold variables. End-of-war settlement only iterates remaining participants. The native ten-year failure flag reduces later native assistance acceptance; it is not a new opinion modifier or a guaranteed refusal.
- Frankokratia departure helper, start/join effects, story membership and reward consumers: `crusading_claim_cb` and `frankokratia_leaders`. Native departure randomly locates a war; the mod instead visits only attackers and matching stories in the selected war, removing only the withdrawing actor.
- Native participation messages, filters and custom effect text. Current exports do not prove whether compiled notifications duplicate the retained manual messages; no notification workaround was removed without a live comparison.
- Alliance removal/broken hooks and embassy, perk-opinion and blood-brother helpers: existing `break_alliance` remains delegated to Vanilla, including its native betrothal consequences. No callback is manually replayed.
- Pure `stress_impact` declaration and current traits/rules: literal trait amounts are additive and do not change spiritual fulfillment. No base stress, faith, rite, piety or fulfillment mutation was added.

These are source/declaration findings. Actual removal, accounting, notification delivery, callback behavior, saved-scope invalidation and multiplayer routing remain separate runtime gates.

## Targeted implementation

The existing ten event branches are retained. Their complete legacy financial, prestige-experience, alliance, opinion and notification effects are token-identical to the original after removing the new guard and the new commitments call. Wrapping the branches necessarily changes indentation; inherited trailing whitespace was removed only on reindented changed lines. No branch consolidation or replacement selector was made.

`lw_mod_can_leave_war_trigger` takes a **war root** and the supplied actor/recipient. It requires live figures, a human non-adventurer actor, recipient still leading the war, actor not leading either side, and both figures on the same side. It is shared by display and enumeration. `lw_mod_can_select_war_trigger = { WAR = scope:leaving_war_N }` additionally guards an absent saved war; every option uses it for visibility/validity and again before effects. The execution guard also checks current actor funds through `lw_mod_can_pay_war_exit_trigger`.

No costs, opinions, alliance break, optional penalty, contract cleanup, story change or message run from an invalid selection. The existing eleven explicit scope clears remain outside each effect guard, so stale execution still cleans up. The always-available cancel option and the start of each new send clear the same eleven references via `lw_mod_clear_war_scopes_effect`.

Existing numerical policy remains `50 × actor tier` prestige **and prestige experience**, `25 × actor tier` gold, the original half/double scalings and original opinion durations/values. Recipient still receives the configured gold/prestige. The old Free setting still breaks an existing alliance. No engine-accounting adjustment was inferred from exports alone.

New behavior is centralized only for the newly added consequences, in `lw_mod_war_departure_commitments_effect` (selected war root, actor/recipient/`leaving_war` supplied):

| Condition | Consequence |
|---|---|
| Actor's stored assistance war equals selected war | Clear the three assistance variables, permanently forfeiting that contract's future payment |
| Matching contract and `lw_mod_contract_failure_on` | Set `fp2_contract_assistance_failure` for ten years |
| `lw_mod_personality_on` | `stress_impact`: loyal +40, just +20, disloyal −30, callous −5, arbitrary −5 |
| Selected war is `crusading_claim_cb`, actor an attacker | Remove actor from matching `frankokratia_leaders` lists owned by attackers in this war |

Both optional rules are independently toggled and default on. They apply independently of all six price settings, including Free; personality amounts do not scale with Half/Double. Contract abandonment and forfeiture happen even with both optional rules off. An old failure flag is not erased when the optional rule is off. No forced save migration is performed; native handling of newly introduced rule values in old saves must be recorded during acceptance.

No confederation, house bloc or tributary is dissolved. Great Holy War restrictions from the landless native interaction were not indiscriminately imposed on landed participants; those wars are an explicit special-mechanic acceptance case.

All seven existing languages retain their original 38 keys and strings and add the same 12 translated rule/tooltip keys. Existing BOM and newline conventions are preserved; new `.txt` files use UTF-8 BOM with CRLF. The three custom message types now use `war_participation_ally`, `war_participation_enemy` and `war_participation` filters.

## Validation and release gate

Run the read-only structural regression verifier:

    & 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' Documentation/tools/verify_leave_wars.py

[Static result](../evidence/leave-wars-verification-20261003.json) checks all ten real branches against the original commit; it also checks rule defaults, independent penalty gates, selected-war contract/story isolation, unchanged original amounts/opinions/descriptors, same-key translations, lexical balance, BOM/newlines and the untouched bundle. It is not an engine parser/type validation or a simulated gameplay result.

The [new source baseline](../update-watch-leave-wars-20261003.json) updates only Leave Wars and adds its audited dependencies; all other mod records and historical baselines are preserved. The [final source check](../evidence/leave-wars-source-check-20261003.json) reports all 24 watches unchanged, unchanged engine exports and no local baseline drift. A clean source check does not close the runtime gates below.

**No campaign, GUI, multiplayer or external-validator test was executed.** The available computer-control surface supports browsers, not native CK3 input, so it cannot execute the requested campaign scenarios here. No game/profile/playset/installation files were changed. Run and record the [standalone acceptance protocol](leave-wars-tests.md). Only after it passes may both standalone descriptors advance to `supported_version="1.20.*"` and the next mod version.

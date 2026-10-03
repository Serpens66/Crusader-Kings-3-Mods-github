# Leave Wars standalone acceptance protocol

Target: CK3 **1.20.0.3**, updated standalone working files. Status of **every runtime case below: NOT RUN**. Use the standalone alone, without the overlapping bundled Leave Wars copy. Record exact mod file hashes from the current baseline and fresh logs for a full restart; preserve pre-existing log errors separately.

## Cases and expected results

| ID | Setup / action | Acceptance |
|---|---|---|
| LW-T01 | Human secondary attacker, then secondary defender, one shared war | Exactly selected war loses actor; leader/other wars unchanged; configured effects and one message per intended receiver |
| LW-T02 | Actor leads either side; recipient leads neither side; actor/recipient on opposite sides | Interaction/candidate unavailable; no removal, cost, penalty or message |
| LW-T03 | AI actor; landless adventurer actor | Mod interaction unavailable; native adventurer interaction remains available under its own requirements |
| LW-T04 | 0, 1, 10 and 11 eligible wars against the same recipient | At most ten options; no extra/unselected war changes; cancel always works |
| LW-T05 | For every original cost rule, funds below, equal to and above displayed gold/prestige price | Paid options disabled below either balance; exact balance allowed; real actor/leader gold/prestige and actor fame deltas match original policy. Do not infer implicit fame semantics |
| LW-T06 | Half/Double/Free with all four optional-rule combinations | Original costs/opinions scale as before; optional stress/failure do not scale; optional effects can apply with Free; Free still breaks an existing alliance |
| LW-T07 | Open picker, then end war, replace recipient leader, promote actor to leader, switch sides or remove actor | Stale selection causes no charge, penalty, contract/story mutation or message; cancel and subsequent fresh selection work |
| LW-T08 | Open picker, then reduce actor gold/prestige below price | Execution guard blocks all effects and clears selection references |
| LW-T09 | Cancel; send again; repeat after a real exit; save/reload with event open; player death/switch | No old saved-war reference leaks; valid new selection uses current roles/funds; invalid selection stays harmless |
| LW-T10 | No assistance promise; promise to another war; promise exactly to selected war | First two retain state and receive no new failure flag. Matching promise loses all three variables, earns no later payout, and gets flag only when enabled |
| LW-T11 | Matching assistance contract with penalty on/off; pre-existing failure flag; new contract after abandonment | New penalty lasts ten years when enabled; off does not erase an existing penalty; old promise no longer blocks a new contract; ordinary exit costs remain independent |
| LW-T12 | Personality off/on, no relevant trait, each trait separately, multiple relevant traits | Off/no relevant trait: no new stress. Raw trait contributions +40/+20/−30/−5/−5, additive (e.g. loyal+just = +60); record actual engine modifiers/clamping. No spiritual fulfillment delta from this mod |
| LW-T13 | Rank boundaries including Hegemony | Costs follow actual current `highest_held_title_tier`; no assumed empire maximum |
| LW-T14 | Contract-free nomad/confederate/tributary/house-bloc participant leaves one war | Existing institutional relationships remain; only configured departure/ordinary native alliance consequences occur; other ongoing wars remain |
| LW-T15 | Secondary attacker in Frankokratia story list; unrelated ordinary war; multiple wars/stories | Only selected Frankokratia war removes actor from the corresponding participant list; no later participant reward to the departed actor; no other story membership removed |
| LW-T16 | Secondary participants on each side of directed/undirected Great Holy Wars | Confirm whether engine removal succeeds and whether pledges, beneficiaries, contribution and later rewards remain consistent. Any failed contract keeps compatibility acceptance open |
| LW-T17 | Allied, enemy and actor messages; native notification baseline; message-filter settings | Current custom filters respected; correct actor/war names; tooltip workaround still clean. Remove manual duplicates only if native baseline/run comparison proves duplication |
| LW-T18 | Alliance from perk, betrothal or blood brotherhood | Confirm native callback consequences once; do not manually replay or suppress them |
| LW-T19 | Two players independently withdraw, including same war; host/client save/reload and hotjoin | Correct player receives picker; exactly one departure/payment per actor; participants, balances, flags and messages agree on both clients |
| LW-T20 | Old 1.121 save and new game with both new rule settings checked | Record native old-save resolution of absent new settings; no forced rewrite/migration. New game defaults both on; independent off selections respected |

For LW-T05, record actor gold/prestige/prestige experience, leader gold/prestige, leader and fellow-participant opinions, alliance state, selected-war membership, promise variables, failure flag, stress and spiritual fulfillment before/after. Base financial price is `25 × actual tier` gold and `50 × actual tier` prestige plus the existing explicit fame subtraction; opinion values are leader −80 / other same-side participants −30 with the original rule scalings and durations.

## Results to record

For each case: game version/checksum, standalone hashes, DLCs/government/CB, original and optional rule selections, before/after values, expected versus actual result, fresh log lines, and pass/fail. The table above is a protocol, **not results**. Fix only proven failures, preserve unrelated user files, and rerun affected cases. Compatibility metadata and mod version stay unchanged until the mandatory acceptance passes.

# Mass Demand Conversion: static 1.19 to 1.20 migration review

Date: **2026-10-03**, subsequent to the initial history integration. Target: installed **1.20.0.3 (Crozier)**. Package: standalone **1.077**, with five categories. The older bundled variant is not certified by this review. The user states that the mod worked correctly under 1.19; that is an explicit assumption, not a recorded game test or identification of the exact tested patch.

**Result: no necessary functional 1.20 mod-code patch has been demonstrated by the reviewed sources and static checks. This is not proof that no runtime patch will be needed.** No mod file, notification experiment, descriptor or `supported_version` was changed. The full feature audit remains open where Engine contracts or runtime behavior are unknown.

[New evidence](../evidence/mass-conversion-static-migration-20261003.json) · [Read-only recomputation tool](../../tools/audit_mass_conversion_migration.py) · [Historical comparison](../../research/vanilla-history-20261003.md) · [Earlier caller research](mass-demand-conversion-recheck.md) · [Native game-test matrix](mass-demand-conversion-tests.md)

## Confirmed static surfaces

| Surface | Evidence and conclusion | Limit |
|---|---|---|
| 14 Script interfaces | Current exports retain the ten category iterators, `vassal_contract_has_flag`, `exists`, the acceptance query and `run_interaction` | Presence and exported scopes do not prove all runtime validation stages |
| Three GUI bindings | `Scope.ScriptValue`, `DecisionViewWidgetOptionList.GetEntries` and `DecisionViewWidgetOptionList.OnSelect` are exported | `GetEntries` has an unregistered exported return type; no invented typed-list contract |
| Five category routes | Visibility, count and send agree on their interaction ID; queries enter requester `root`, use candidate `prev`; sends use actor `root`, recipient `this`, `send_threshold = decline` | Checked textual bindings and selected guards; no simulated dynamic execution or delivery-count guarantee |
| Existing category policy | Direct/indirect vassal protection exclusions agree; indirect candidates require a liege different from requester; five widget values match category IDs | Existing stronger indirect protection is the author's policy, not a proven 1.20 defect |
| Localization and syntax | Eight languages reference the same five defined count values; twelve package text/reference files decode correctly; `.txt`/`.yml` retain BOM and script braces balance | Limited ordered-block reader, not a complete Jomini parser, Tiger result or rendered GUI check |
| Selection widget | Old 1.19.0.6 blob, new 1.20.0.3 blob and installed widget are byte-identical | Runtime controller/context still requires an actual GUI observation |
| Decision schema and assets | The current `.info` retains the picture/reference form, decision group and fixed-option controller; the native picture exists | New dynamic-scope selectors have different contexts and are not used here |
| Recipient cooldown | Each of the three interactions declares 15 years in both snapshots | This is unchanged configuration; whether query/send applies it is an Engine question |
| Current source freshness | All 295 existing native seed paths still match the installation and mirrored 1.20.0.3 bytes | This seed is not an exhaustive semantic graph |

The evidence records exact commits, whole-source SHA-256, original export spans, old/new interaction spans, selected followup-definition spans, all mod file hashes and the external launcher descriptor hash. Decoded block/span hashes are explicitly distinct from original-byte file hashes. The collector also verifies all eleven raw exports and preservation of 853 non-Documentation files.

## Reviewed source routes and actual bindings

The mod owns category enumeration, its extra protection filter, the option IDs, candidate queries and dispatch. It does not define native interactions, religion databases, family conversion effects, schemes or active conversion events. Consequently, the following 1.20 changes occur through native dispatch. Their presence is not an instruction to copy or override those scripts.

| Route | Source-level trace and binding | Update assessment |
|---|---|---|
| Eligibility and acceptance | Three native interaction definitions use the common validity helper and default acceptance modifier; house/vassal requester references migrate to `puppet_or_actor`. Celestial modifier receives `ACTOR = actor` for courtier, `ACTOR = puppet_or_actor` for house/vassal, always `RECIPIENT = recipient` | Actor migration is real. Native requester/query callers support the existing character-scope query pattern; exact Engine initialization remains open |
| Courtier/house acceptance | Common conversion effect selects family and triggers `false_conversion.0900`; house also reports through `char_interaction.0181`; refusal reports through 0182 | No corresponding native definition is overridden by this mod |
| Vassal acceptance | Interaction's acceptance invokes native 2002 and the vassal conversion wrapper. Wrapper calls common conversion, handles capital marker, hooks and opinions; the notification event has tooltip-only effect previews | Tooltip previews must not be counted as additional executed conversion requests |
| Refusal and negotiation | 2003 handles refusal; 2011 accepts gold/treasury through `pay_treasury_or_gold` to recipient with `demand_conversion_bribe_size`; 2012 accepts a recipient-held favor hook over requester; refusal/hook alternatives remain | Delegated native behavior, not a required mod currency/response rewrite |
| Influence and new concession | Influence value starts at zero and adds effective actor's medium influence only for `influence_send_option = yes`. Puppet charging has its own branch. New tax concession transfers medium gold from effective actor to recipient only for its own flag | Keep the distinction between these options; Script command option initialization is unproven |
| Family and secret faith | Family selection, common conversion and family converter have actor fallbacks. 0900 routes to 1000/1010 or directly to conversion when already secret-faith; calls use `FALSE_CONVERSION = no/yes`, `FORCED = yes`. RITE is explicit `conversion_rite` when present, otherwise effective actor's rite | Mod has no old `set_character_faith` or `conversion_faith` conversion implementation to migrate. List isolation/queued-event behavior remains a runtime question |
| Rite consequences | Native converter uses knowledge thresholds below 0.6, below 0.8 and otherwise; low-knowledge exception checks `convert_at_war`. It clears prior convert modifiers, applies piety/stress/modifiers, sets rite, adds five-year flags and checks baptism conditions | Native changed outcomes are expected 1.20 behavior, not necessarily a regression or missing mod implementation |
| Clan/state faith/tenets | Clan caller uses `CHARACTER = puppet_or_actor`, `TARGET = recipient`, `REVERSE_NON_HOUSE_TARGET = no`; 60% house faith majority determines direction. State-rite helpers grant piety. Mandala and personal-tenet helpers have explicit native guards | Do not hardcode DLC presence, costs or rewards in MDC |
| Study promise | New negotiation option calls 2015; accepting starts `study_faith` targeting effective actor and stores a ten-year pending actor reference. Scheme completion supplies owner/target, success/failure hooks may schedule 0100 after two days. 0100/0110 restore actor/recipient and test living actor plus current `is_vassal_of`; 0101/0111 can convert via the common effect, continue study or break the promise | Source trace is known. Relationship changes, indirect vassals/tributaries, save/reload and actual delayed completion require runtime evidence; no Vanilla patch is authorized |

Puppeteer notification is guarded by actor/effective actor existence and `is_puppet_action`; the mod itself does not request puppet actions. Courtier/vassal adult availability conditions are conditional on an AI actor, not unconditional player restrictions. Holy-site AI evaluation, hostility and doctrine changes remain inside native logic.

## What is migration work and what is regression coverage?

The new effective-actor context, rite consequences, tax concession and study negotiation are **actual 1.20 changes**. They deserve focused probes using the unchanged mod first. Unknown Engine defaults, hardcoded pending/cooldown stages and family-list lifetimes were not established as new mod defects. The unchanged 15-year cooldown and extra protection policy should therefore be recorded as regression coverage rather than automatic code changes.

G04's textual requester/recipient bindings, category-ID mapping and localization references are now statically checked. Its dynamic GUI context, count/candidate equality and state changes remain untested. G01/G02 retain Script command construction/option/default/validation questions. G03 retains native propagation, list isolation and delayed lifecycle. G05 retains real multiplayer routing/save behavior. No gate is closed by file hashes or export presence alone.

**No speculative helper rewrite, additional validity predicate, synthesized puppet scope, acceptance threshold change, blanket faith-to-rite replacement or bundle port is justified by these results.** If native runtime probes and the package's acceptance tests succeed with unchanged code, a later explicitly validated update may consist solely of metadata and release notes. Metadata is not changed by this documentation review.

## Reproduce and validate

From the workspace root:

```powershell
& 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' Documentation/tools/audit_mass_conversion_migration.py --check
```

The checker recomputes the new deterministic evidence without rewriting it. It never launches the game, invokes upstream scripts, installs a validator, changes either Git checkout or edits mod/game files. Build refuses to replace an existing evidence file. [Verification](../evidence/mass-conversion-static-migration-verification-20261003.json) retains the separate documentation/source/preservation results; historical reports and the known historical AGENTS.md mismatch remain intact. Gameplay, GUI, multiplayer and Tiger are **not run**.

# Vanilla history integration and initial comparison

Date: 2026-10-03. This supplement adds historical source evidence; previous audits, baselines and unresolved runtime gates are retained.

## Sources and coverage

The [full local reference](../reference/vanilla-history.md) compares the exact locked 1.19.0.6 and 1.20.0.3 commits. The [machine-readable evidence](vanilla-history-20261003.json) contains their game-tree IDs, version metadata hashes, every changed game-file path and original SHA-256 hashes for the selected feature sources. Source lines refer to each committed snapshot, not a later moving branch.

| Inventory measure | Result |
|---|---:|
| Game blobs in 1.19.0.6 | 48,461 |
| Game blobs in 1.20.0.3 | 51,480 |
| Added files | 3,116 |
| Modified files | 7,675 |
| Deleted files | 97 |
| Git-detected renames, similarity threshold 50% | 120 |
| Previously audited MDC paths compared | 295 |
| Changed/introduced MDC seed paths | 245 |
| Current MDC seed paths byte-identical to installation | 295 |

These are file inventories, not counts of changed functions or completed semantic audits. All 295 current files match the installation exactly; no formatting-only differences or missing current files occurred in that set. Sixteen paths are absent at the same path in the old snapshot; absence alone does not prove that equivalent logic did not exist elsewhere.

## Initial Mass Demand Conversion findings

The selected definition spans and block-text hashes are recorded in `selected_object_spans` in the evidence. Whole-file original-byte hashes are in `feature_paths`; block hashes are decoded text hashes and have a different purpose.

| Definition | 1.19 source lines | 1.20 source lines | Confirmed historical difference |
|---|---|---|---|
| `ask_for_conversion_courtier_interaction` | religious interactions:140–487 | same file:158–505 | Adds an AI adult availability condition, new acceptance modifiers and personal-tenet effects; AI hostility checks use rites |
| `demand_conversion_interaction` | religious interactions:490–744 | same file:508–778 | Uses effective actor `puppet_or_actor`; influence is calculated through a shared value with distinct puppet charging branches |
| `demand_conversion_vassal_ruler_interaction` | religious interactions:746–1227 | same file:780–1383 | Uses effective actor for relations and validity; adds puppet branches, religious concession handling and revised steppe-government conditions |
| `valid_demand_conversion_conditions_trigger` | religious triggers:1216–1284 | same file:1198–1269 | Actor-dependent relationship, imprisonment, blocking-variable and diarch checks now use `puppet_or_actor` |
| `demand_conversion_interaction_effect` | religious interaction effects:1108–1138 | same file:1220–1283 | Adds the actor fallback for missing `puppet_or_actor`, old-faith capture and confession-penalty handling |
| `religion_demand_conversion_default_modifier` | religion scripted modifiers:26–336 | same file:26–426 | Migrates requester references and adds acceptance modifiers for new religious systems |

The full game-relative source paths are respectively `common/character_interactions/00_religious_interactions.txt`, `common/scripted_triggers/00_religious_triggers.txt`, `common/scripted_effects/00_religious_interaction_effects.txt` and `common/scripted_modifiers/00_religion_scripted_modifiers.txt`. The new `demand_conversion_influence_cost_value` is defined in `common/script_values/pam_values.txt:9473`; the influence option still controls whether its initially zero value gains the effective actor's medium influence amount.

These differences establish that the effective-actor migration is a real 1.19→1.20 source change. They do not establish that scripted queries or dispatch fail to initialize it. The later effect fallback still cannot prove earlier query initialization. Courtier availability is AI-conditional; it is not a blanket adult-only rule for player actors. Source changes inside acceptance effects likewise must not be interpreted as absence of equivalent consequences elsewhere in the new call chain.

MDC delegates to these native interactions rather than copying their definitions. The differences therefore identify what its query/dispatch behavior must be checked against; they do not justify copying Vanilla blocks, manufacturing scopes, changing all faith comparisons to rites or declaring compatibility. The [existing recheck](../update-readiness/mods/mass-demand-conversion-recheck.md) and [native test matrix](../update-readiness/mods/mass-demand-conversion-tests.md) remain applicable. This integration covers the existing source seed and selected definitions, not a completed comparison of every dynamic dependency.

## Validation boundary

See the [integration verification](vanilla-history-verification-20261003.json) for clone state, ignored-path checks, original-source hashes, tool tests, encodings, links and preservation results. Mod code, supported versions and the installed game were not changed. No game, GUI, multiplayer or Tiger run was performed. The historical AGENTS.md baseline discrepancy remains historical evidence and is not silently rebased.

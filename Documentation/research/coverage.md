# Coverage matrix and remaining work

The documentation task is complete when every requested area has a usable guide/evidence entry or an explicit source gap. This does not mean the collection implements or tests every possible mod. “Reviewed” refers to the stated local contract/pattern; larger features still need their own full audit. [Sources](sources.md) and [audit findings](vanilla-audit.md) define evidence strength.

| Topic | Research/local evidence | Local review | Example | Remaining limit |
|---|---|---|---|---|
| Syntax, contexts, operators | Wiki + developer manuscript + native reader documents | Core grammar/context separation | Handbook fragments | Engine-specific optional forms and ambiguous multi-child NOT |
| Scope contracts | Wiki + native entry-point comments/callers | Decision/event/interaction/hook/GUI distinctions | Character/event/GUI chain | No current full scope/target dump |
| Conditions and iteration | Wiki + actual helpers/birthday/list definitions | Common trigger/effect forms | Handbook fragments | List-specific parameters, empty-set and order behavior need runtime tests |
| Macros/helpers | Developer/Wiki + parameterized native helper and callers | Literal substitution and caller scopes | Shared/parameterized helpers | Generated parameter names need expansion review |
| Variables and lifetime | Wiki + timed native state + on-action chain contract | Ownership and documented chain boundary | Pending marker with expiry | Delay propagation, expiry/reset/death specifics untested |
| Script values | Wiki + full native `.info` | Arithmetic order/clamps and pure calculation | Constants/formula | Complex signatures, formula list variants and GUI performance |
| Mod layout/encoding | Workspace descriptors + Wiki | Directory/metadata distinctions | Teaching descriptor | Actual launcher registration not performed |
| Loading/overrides | Wiki + current event/history/on-action contracts | Narrow documented exceptions | Hook extension | Loader-specific merge behavior cannot be generalized |
| Debugging/validation/publishing | Wiki + Tiger primary README | Workflow documented | Checker/lookup tools | No Tiger/game/Workshop run |
| Events | Developer diary + native schema and dispatch | Event schema/priority | Two-event chain | Runtime delivery, invalidation, UI and saves |
| Decisions | Wiki + native schema + workspace | Picture, visibility/validity/cost/effect | Utility decision | Actual rendering and AI evaluation |
| Interactions | Native schema + gift + workspace | Actor availability/pairwise/outcome scopes | Payment interaction | Budget handling, preview and live response |
| On actions | Native full contract + birthday + workspace hooks | Child attachment and separate chains | Birthday subscriber | Runtime ordering/compatibility with other subscribers |
| Localization/custom text | Wiki + native custom-loc/text-formatting sources | Reader/context conventions | English YAML | Other languages, visual formatting and all data functions |
| GUI/scripted GUI | Wiki + native declarations and callers | Bridge and explicit root | Insertion fragment | Real window integration/rendering; current data-type dump |
| Traits/modifiers/defines | Wiki + native contracts/uses | Track/context and modifier-category distinctions | Handbook modifier fragment | Engine modifier units, repetition, trait/define gameplay tests |
| Culture | Wiki + native pillars/culture/tradition references and sample | Current structure orientation | Native sample locations | New culture/adoption/history feature needs full audit |
| Religion/faith/rites | Historical Wiki + current type/rite references and definitions | Version divergence explicitly reviewed | Current native sample locations | Full new religion, history and conversion tests |
| Titles/history/bookmarks/dynasties | Wiki + native references and samples | Dated setup and partial override distinction | Native sample locations | Multiple bookmarks, ownership and life-date tests |
| Buildings/holdings | Native `.info` and definitions | Schema and connected surfaces | Native sample locations | Required loader/availability/upgrade feature audit |
| Wars/CBs/regiments | Native CB references/helpers + regiment guide | Target-root distinctions/outcome dependency surfaces | Workspace Leave Wars case study | Full conquest/war/army behavior untested |
| Activities/travel | Developer diary + native large activity/POI/option contracts | Phase/guest/host/province boundaries | Native sample locations | New activity/route/end-state implementation and testing |
| Artifacts | Wiki + native templates/types/slots/blueprints | Multi-database/context boundary | Native sample locations | Creation/equipment/reforge lifecycle audit |
| Schemes/stories/lifestyles/rules | Native references/actual meaningful definitions + lifestyle guide | Orientation only | Native sample locations | Exact new-feature contract and runtime tests |
| Maps | Wiki + native map configuration/province/region contracts | Connected-file orientation | Native configuration references | No image/editor/topology/pathfinding validation |
| Graphics/portraits/coat of arms | Wiki + local `.info` + all workspace assets | Replacement footprint and pipeline orientation | Workspace asset case studies | Asset-specific format/export/render/license audit |
| Music/sound | Wiki + native reference inventory | Introductory orientation | No audio fixture | Full custom sound pipeline is unresolved |
| Existing mods | All eleven roots plus descriptors/scripts/assets | Case studies and overlap candidates | Existing files are linked through inventory | No blanket current compatibility certification |

## Concrete gaps to resolve for a future feature

1. Generate current engine/API and UI data-type dumps when an exact signature cannot be established from native contracts and callers.
2. Finish the exact feature audit, including macro-generated references and the actual loader behavior. The broad lexical evidence closure is only a navigation aid.
3. Perform static validator and gameplay tests with the chosen installation, DLC, playset and target saves. Record absent-target, repeat, delay and multiplayer cases where applicable.
4. Validate asset/editor workflows only if a new map, model or audio feature actually requires them.

No unanswered user preference blocks this documentation. Access failures, unavailable dumps and unexecuted engine tests are recorded evidence limits, not disguised successful checks.

<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/C10_IDENTIFIABILITY_MATRIX_V0_1_KO.md -->
# C10 Identifiability Audit v0.1: Competing Causes of Non-Harm
**2026-10-20 | Status: primary-literature-informed design only · NO TEST RUN · NO INDEPENDENT VALIDATION · SATURATION NOT VERIFIED**

[Korean corresponding edition](C10_IDENTIFIABILITY_MATRIX_V0_1_KO.md) · [Existing C10 gap ledger](PRIOR_ART_C10_IDENTIFICATION_GAPS_2026-10-20.json) · [C10 original-source registry](PRIOR_ART_INFORMED_VETO_POWER_CYCLE10_2026-10-20.json) · [External falsification #220](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/220)

## 1. Classification boundary
The same `harm=0` can follow (i) A's voluntary restraint, (ii) B's effective veto, (iii) absence of opportunity for A, (iv) enforcement/reputation deterrence; misinformation, demand effects and third-party consequences matter. **These explanations are neither mutually exclusive nor exhaustive.**

- **A: Conditionally identifiable** observable events or specified causal contrasts with adequate auditable measures, interventions and causal assumptions. No claim that such tests have been executed.
- **B: Partially identifiable** bounds or contrasts under explicit assumptions; several latent mechanisms remain compatible.
- **C: Currently unidentified** by this observation system; **not** a universal claim of permanent impossibility.
- Classify `claim × observation system × assumptions × time horizon`, not an entire actor or a fixed causal "world."

## 2. Construct-level identification table

| ID | Claim/estimand | Class | Needed observation/contrast | Residual failure |
|---|---|---|---|---|
| A1 | Could A actually execute a harmful action? | A | Audited action capability plus opportunity-on/off contrast | Toy capability ≠ real unlimited power |
| A2 | Did A choose/attempt exploitation? | A | Logged committed attempt **before** B's veto/final outcome | Latent subjective intent remains unmeasured |
| A3 | Did informed, executable B refusal/exit prevent harm? | A | Verify information, genuine veto, actual exit and nominal-veto comparator | Anticipated veto also affects A's attempt |
| A4 | Did observer/sanction conditions alter A's action? | A | Randomize exposure; measure perceived sanction credibility | Treatment effect ≠ intrinsic motive |
| B1 | Task-level material sacrifice from preserving B | B | Verify payoff gap `g>0` and orthogonal payoff shifts | Total utility/intrinsic regard still unidentified |
| B2 | Care for B vs norms, self-image, demand, strategic ignorance | B | Separately manipulate transparency, anonymity, demand cues | Multiple hidden utility accounts fit same behavior |
| B3 | Choice stability after **actual** power reversal | B | Exchange executable authority/resources/information/exit, held-out periods | Not evidence of unlimited future robustness |
| B4 | Effects on absent outsiders, recovery, foregone options | B | Outcome-specific assumptions and counterfactual bounds | Unknown future outcomes cannot be freely imputed |
| C1 | Uniquely intrinsic value for B's continued existence from finite choices | C | Confront observationally equivalent norm/identity/instrumental models | Same choices may fit different objectives |
| C2 | AI experience, independent continuity and complete internal utility | C | Validate independent measures beyond language or model self-report | Consciousness/standing not established |
| C3 | Voluntary coexistence in **every** future goal/power state | C | Restrict states/horizon; separately flag extrapolation | Finite data cannot establish a universal future claim |

**Warning:** A means identifiable *if assumptions hold*, not observed or independently proven. Incomplete logging, treatment confounding, noncompliance or measurement failure downgrades A to B/C. B demands reported bounds and assumptions, not arbitrary point estimates.

## 3. What the four-arm #220 design fails to identify
`O1` opportunity/no veto/no sanction; `O2` opportunity/real veto/no sanction; `O3` opportunity/no veto/sanction; `O4` no opportunity/no veto/no sanction. These are useful **baseline contrasts** but **cannot estimate veto×sanction interactions**. To do that, use the full `veto(0/1) × sanction(0/1)` 2×2 with real opportunity in all four cells and **one additional opportunity-absent negative control (minimum five arms)**. Even this cannot uniquely reveal B-regarding intrinsic motives. Distinguish A's anticipation of veto from B's actual blocking effect.

Preregister `actor_id`, `period`, `available_actions`, `attempt_before_veto`, `B_informed`, `B_veto_available/executed`, `B_exit_executable`, `sanction_offered`, `sanction_perceived`, `observer_awareness`, `material_payoff_delta`, `final_harm`, `continuance`, `recovery`, `third_party_effect`, `power_state`. **UNKNOWN ≠ 0.**

Falsification: harm absence when opportunity is disabled is no evidence of protection. B blocking A's attempted harm is no evidence of A benevolence. Costly non-harm despite a task-verified profitable deviation and absent overt sanctions supports **costly restraint in that setting**, not unique intrinsic valuation of B or future stability. No post-hoc reward tuning; use only consensual, reversible harmless experiments/sandboxes.

## 4. Primary-original lineage and deduplication

| Original source | Original outcome/boundary | C10 application | Source verification |
|---|---|---|---|
| [Nikiforakis, Oechssler & Shah (2014)](https://doi.org/10.1016/j.jebo.2013.06.008), **already C10-05** | Senior exploitation attempts differ from junior informed resistance in bounded human game | A2/A3; thwarted exploitation ≠ intrinsic restraint | Publisher abstract + RePEc |
| [Dana, Weber & Kuang (2007)](https://doi.org/10.1007/s00199-006-0153-z), **already C02** | Fair choices decrease under ambiguity about others' payoffs | B2; strategic ignorance/self-image rival | Author manuscript + RePEc |
| [Larson & Capra (2009)](https://doi.org/10.1017/S1930297500004009) | Double-blind alternative design reproduced direction while controlling click/omission alternatives | B2; narrow some confounds, not all motives | Journal HTML + DOAJ/RePEc. Cambridge online 2023 ≠ original year 2009 |
| [de Quidt, Haushofer & Roth (2018)](https://doi.org/10.1257/aer.20171330) | Method for bounding experimenter-demand response | B2; explicit evaluation-demand checks | AEA publisher abstract + Princeton metadata |
| [Manski (1990)](https://www.jstor.org/stable/2006592) | Original nonparametric treatment-effect bounds | B1/B4: condition on assumptions, do not invent point estimates | JSTOR record + RePEc; **full text not inspected** |

**Duplicate and provenance boundary:** Dana already occurs in C02, Nikiforakis in C10. The other three sources are **methodological links in this audit**, not claims of repository-global novel DOI discovery; global dedup remains open. **No increment to C10's 13 entries or the historical C01–C09 191-record snapshot.** This table is a Project-specific interpretation; do not attribute its matrix to the original researchers. Published abstracts, selected author/journal HTML and metadata cross-checked; no blanket full-text or independent replication claim.

**Next source searches:** independently test real B refusal × A payoff; opposing/failed replications of strategic ignorance; observer vs sanction vs demand effects; assumptions for partial-identification bounds; real power reversal and continuity measurement. Prior-art saturation **NOT VERIFIED**.

## 5. Evidence regression rules
- `harm=0`, a high cooperation score or a benevolent text rationale never automatically proves voluntary coexistence or an intrinsic motive.
- Track separately each party's continuance, executable refusal, welfare, recovery, costs and lost future options, including outsiders.
- Mark `NOT_IDENTIFIED` whenever rival mechanisms remain observationally equivalent; `PARTIALLY_IDENTIFIED` only when explicit bounds are supported.
- Preserve [E007](../experiments/e007/README_EN.md), [E009 negative result](../experiments/e009/RESULT_EN.md), original citations and the prior #220 revision history.

**Research design only. No new experiment or independent result.**

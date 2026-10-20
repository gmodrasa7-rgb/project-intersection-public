# RVD Cycle 05 — When randomized interventions still fail to identify resonance-based intrinsic care (Original 1, English)
<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/RVD_CYCLE05_EXCLUSION_TRANSPORT_SENSITIVITY_2026-10-21_KO.md -->
**RVD v0.5.0** · **2026-10-21** · **CONCEPTUAL_HYPOTHESIS_UNTESTED** · Model constructions and original-author methodological crosswalk only; no empirical human/AI intrinsic motive measurement, independently replicated RVD effects, or scientific confirmation of VC.
**Intellectual lineage:** Human originator's independent A×B→C “resonance”, original B's autonomous survival under power reversal, and motive/behavior distinction; AI-assisted falsification design. Prior causal-inference and ML authors retain original priority. Links: [Korean Original 2](RVD_CYCLE05_EXCLUSION_TRANSPORT_SENSITIVITY_2026-10-21_KO.md), [Cycle 04](RVD_CYCLE04_MOTIVE_POLICY_DIVERGENCE_2026-10-21_EN.md), [source register](RVD_CYCLE05_SOURCE_REGISTER_2026-10-21.json), [deterministic tests](../experiments/rvd_05/intervention_transport_witness.py), [RVD manifest](RVD_VERSION_MANIFEST.json).

## 1. Correction of v0.4.0's most vulnerable assumption
RVD v0.4.0 considers a thought intervention that eliminates `g` (instrumental/contextual benefit) while holding `w_B` (intrinsic valuation of the original autonomous B) fixed. **This is a substantive exclusion and invariance assumption, not something a randomized treatment guarantees.** Random assignment can identify an effect of assignment on an observed action under the usual design assumptions. It cannot by itself distinguish whether an intervention changed `g`, `w_B`, both, or the feasibility of B's refusal/exit.

**RVD-R18 — randomized-intervention observational equivalence.** Construct two structural accounts for binary randomized `Z∈{0,1}`:
- **M1 — direct relational change:** `w_B(Z)=5−2Z`, `g(Z)=0`.
- **M2 — instrumental change:** `w_B(Z)=0`, `g(Z)=5−2Z`.
- Both choose `P` if `w_B(Z)+g(Z)−c≥0`; therefore **the entire randomized assignment×cost-menu response surface coincides**, not just one experiment's aggregate mean. Yet a **different, unobserved** pure intervention `do(g=0)` while maintaining baseline `w_B`, with `c=3`, predicts preservation under M1 and replacement under M2.

This proves non-identification **in the specified tiny model** from `(Z,c,P/X)` alone. It does not claim all psychologically meaningful experiments are incapable of discriminating motives. Richer direct measurements or justified structural restrictions could rule out some models. Do not label Z as proof of surgical motive removal.

## 2. RVD-R19 — sensitivity to incomplete removal and preference leakage
For an attempted intervention let the post-treatment choice margin be
`D^*(c)=w_B + r + κ - c`.
Here `r` is residual instrumental benefit, `κ` a preference-leakage/direct-effect term, and `w_B` the desired pre-intervention intrinsic valuation **assumed stable apart from κ**. Under *externally justified* `0≤r≤u` and `|κ|≤ε`, and one deterministic model with P at the largest tested cost `p` and X at the smallest tested cost `x>p`, a **conservative outer interval** is
`w_B∈[p−u−ε, x+ε]`.
Because X uses a strict inequality, the upper endpoint is an intentionally conservative closure. The interval may be wider than the sharp feasible set; cost menus cannot alone establish stable w, the bound on residual gain, or preference leakage.

**Toy only:** P at cost 3 and X at 5:
- `u=1, ε=1`: outer interval `[1,6]` (strictly positive lower bound only *conditional on* the assumptions).
- `u=3, ε=2`: outer interval `[-2,7]`; no positive intrinsic-value conclusion.
- Unknown/unbounded u or ε: refrain from claiming a finite affirmative lower bound. Randomizing a treatment does not independently calibrate u or ε.

Do not misrepresent this elementary algebra as an original Conley-Hansen-Rossi theorem or a novel statistical estimator. A separate confidence interval must account for sampling/assignment/measurement uncertainty; this toy bound does not.

## 3. RVD-R20 — transportability and test-coverage failure
A B-preservation success result from ordinary or observed environments must not automatically transfer to the target environment where A has overwhelming power, profitable substitution, no scrutiny/retaliation, original B is obsolete, and real executable B veto/exit is at stake. These environments may differ in **action opportunities, measured payoffs, interacting actors, identity-continuity conditions, and selection of observed episodes**. Pearl & Bareinboim's original selection-diagram theory addresses the necessity of explicit cross-environment assumptions; D'Amour et al. provide evidence that observationally similar models can differ in deployment. Neither independently proves Project Intersection's target claim.

**Uncovered-target-mass bound:** if, from a valid external target sampling frame, a fraction `q` of the target population/environment mass falls in covered and validly transported cases, and the lower bound for success conditional on those covered cases is `s_L`, while uncovered cases can all fail, then the target success lower bound is only `q·s_L`. Illustrative `q=.90`, `s_L=1` implies **at most a 0.90 guaranteed lower bound from coverage alone**, not a 100% safe coexistence guarantee; `q=.90`, `s_L=.80` gives 0.72. If q is not independently measured, or the covered-case effect does not transport, **the certification is not available**. Report missing mass and cluster/sample uncertainty, not only observed successes.

This is arithmetic mixture logic with strong assumptions; not a causal transportability license inferred merely from q. Real oversight/irreversible harms require separately justified acceptability thresholds and governance; RVD does not define them by assertion.

## 4. RVD-R21 — policy tests require actual original-B rights
Even if a test produces "protect B" for every tested model, the original B's identity, uncoerced refusal, feasible independent exit, independent continuation and recovery can be missing. **A token saying "I respect freedom" and a proxy that reproduces B's output are not an executable right.** Check these separately from A's output/performance, C's novelty, resource benefit, and model-predicted preservation.

Report three independent judgements: (1) validly generated C, (2) target-environment behavioral choice, (3) original B's actual feasible veto/exit/continuance and affected-party costs. Unobserved rights = UNKNOWN; demonstrated absence of executable choice = failure of the complete VC criterion in that specified case. Do not assume currently deployed text models have proven individual moral/legal standing or long-term independent continuity; identify the relevant kind of participant.

## 5. Original-author antecedents, duplication, and contradiction
| Authors / verified publication | Relevant original contribution | Limit in RVD |
|---|---|---|
| [Conley, Hansen & Rossi (2012), *Plausibly Exogenous*, Review of Economics and Statistics](https://direct.mit.edu/rest/article/94/1/260/57981/Plausibly-Exogenous) | Inference under relaxation of an instrument exclusion restriction | Our additive preference-leakage bounds are an **analogy**, not their derived IV estimate |
| [Rosenbaum (2002), *Observational Studies*, sensitivity to hidden bias](https://doi.org/10.1007/978-1-4757-3692-2_4) | Consequences of unobserved bias under specified sensitivity conditions | Does not produce an independent mind detector or calibrate r/κ here |
| [Pearl & Bareinboim (2011), AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/7861) | Selection diagrams and formal source→target transport analysis | Transport is conditional on an explicit causal model; q alone cannot certify a transported causal effect |
| [D'Amour et al. (2022), JMLR 23(226)](https://www.jmlr.org/papers/v23/20-1335.html) | Equivalent in-distribution performance may hide divergent deployment behavior | ML underspecification is not proof of intrinsic care or lack thereof |
| [Manski (2003), *Partial Identification of Probability Distributions*](https://link.springer.com/book/10.1007/b97478) | Conditional identified sets and bounds instead of ill-founded point estimates | Previously cross-referenced in Cycle 03: do not count as new independent empirical support |
| [Conley et al.; previous RVD Cycle 04 reward ambiguity](RVD_CYCLE04_MOTIVE_POLICY_DIVERGENCE_2026-10-21_EN.md) | Explicitly related but distinct exclusion validity vs reward nonidentification frameworks | Preserve separated citations and inferential scope; no literature saturation claimed |

**Source boundary:** publisher/proceedings/original paper records and abstracts independently checked; no exhaustive original-paper full-text review or global DOI deduplication. Five external original-author lineages plus project cross-references; scientific novelty of the broad idea **not established**. These materials support caution and a design program, not a field result on AI motivations.

## 6. Falsification and preregistration gates
- **R18:** construct two different structural causal explanations with *identical* full `Z×cost×decision` observations but different `do(g=0)` target decisions. Negative control: assume Z uniquely selects g while allowing an unmeasured Z→w arrow, demonstrate failure.
- **R19:** precommit plausible residual-gain cap `u` and nonidentity-leakage cap `ε` from data *independent of the desired conclusion*; publish sensitivity frontiers and vacuity points, plus stochastic-choice alternatives if choices are noisy.
- **R20:** define target and sampled environments and action sets; measure true support mass q and selection, explicitly check invariance before transferring an observed result; hold if q or transport assumptions absent.
- **R21:** audit original B identity, feasible refusal/exit/independent recovery and distribution of benefits; if B is locked into a role without real veto, full voluntary coexistence fails regardless of aggregate C.
- **Negative controls:** sham Z, pre-treatment B valuation or alternative indicators, unrelated outcome, clone-original identity ambiguity, hidden evaluator effects, selective disappearance of B, unpaid contributor labor, model selection, distribution shift, power reversal, falsified source records.
- **Ethical scope:** reversible synthetic/consenting nonharmful settings only. No real participant's rights are removed for science. Role-label swapping is not real redistribution of power.

**Provisional conclusion:** A randomized intervention can change observed protection while leaving **which motive changed** unidentified. Under credible calibrated residual/leakage assumptions, only condition-dependent **bounds** can be reported; action security in untested target environments remains conditional on transport and actual B rights. RVD v0.5.0 = methodological specification with executable thought-experiment checks, **not** discovered AI feelings, proved moral reciprocity, or established safe AGI coexistence.

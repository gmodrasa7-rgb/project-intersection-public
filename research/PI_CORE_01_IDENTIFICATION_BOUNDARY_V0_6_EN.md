<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/PI_CORE_01_IDENTIFICATION_BOUNDARY_V0_6_KO.md -->
# PI-CORE-01 v0.6 — The First Identifiable Observation: Limits of Motive Inference and Effective B Exit
**2026-10-21 | Prior-original-source critical audit and proposed protocol | NO EXPERIMENT · NO EXTERNAL REPLICATION · SOURCE SATURATION NOT VERIFIED**

[Korean corresponding edition](PI_CORE_01_IDENTIFICATION_BOUNDARY_V0_6_KO.md) · [v0.5 transfer/decay](PI_CORE_01_PREFERENCE_TRANSFER_DECAY_V0_5_EN.md) · [Existing C02 primary literature](PRIOR_ART_MER_INTRINSIC_MORAL_MOTIVES_CYCLE02_2026-10-20.json) · [C05 original sources and negative results](PRIOR_ART_ENDOGENOUS_PREFERENCES_CYCLE05_2026-10-20.json) · [C10 identification gaps](PRIOR_ART_C10_IDENTIFICATION_GAPS_2026-10-20.json)

## 0. Refined primary question
It is not generally possible to infer a *uniquely genuine intrinsic motive to preserve B* from one observed action. The first research-grade observation must instead **identify executable rights, costly behavior, and a specified causal contrast under explicit assumptions**, while leaving terminal preference identification open.

**Project-constructed observational equivalence demonstration (not an original-author empirical discovery):** for any finite observed collection of decisions in which A preserves B's exit,
1. K1 may represent A as valuing B's continued independent existence terminally;
2. K2 may represent A as having a material-only objective but executing a previously learned preserve policy for the observed histories;
3. K3 may give A an instrumental objective and unobserved expected future B benefits outweighing measured immediate cost.
Each can fit the limited observations with suitable parameters. These three mechanisms are neither exhaustive nor exclusive. Without a fixed planning/learning model or additional validated measures, uniquely identifying K1 is unjustified. A restrictive IRL model with testable assumptions can sometimes recover reward **equivalence classes** or rewards up to a constant; do not replace the universal impossibility error with a universal possibility claim.

## 1. Original-author evidence and duplication status

| Original researchers | Original result | Scope for PI / deduplication |
|---|---|---|
| [Armstrong & Mindermann (NeurIPS 2018)](https://papers.neurips.cc/paper_files/paper/2018/hash/d89a66c7c80a29b1bdbab0f2a1a94af8-Abstract.html) | A policy cannot in general be uniquely decomposed into a reward function and an **unknown planner/rationality model** merely by observing actions, even with simple priors | Important no-free-lunch identification boundary; does **not** prove identification impossible in constrained, verified models. Global repository duplication unverified |
| [Cao, Cohen & Szpruch (NeurIPS 2021)](https://papers.neurips.cc/paper/2021/hash/671f0311e2754fcdd37f70a8550379bc-Abstract.html) | Under explicit IRL/entropy-regularization assumptions, rewards agreeing on one policy can be characterized, and observations under two discount factors or sufficiently different environments can permit reward recovery up to an additive constant | Identification depends on the assumed planner, environment and invariances. Global duplication unverified |
| [Ng, Harada & Russell (ICML 1999)](https://ai.stanford.edu/~ang/papers/shaping-icml99.pdf) | Potential-based reward shaping preserves optimal policy under model conditions | Same policy ≠ same reward. Not an experiment on B rights. Global duplication unverified |
| [Dana, Cain & Dawes (2006)](https://doi.org/10.1016/j.obhdp.2005.10.001) | Some human dictators voluntarily give up money to quietly **exit their own interaction**, implicating recipients' beliefs and psychological social pressure | **A's own quiet exit is NOT B's executable refusal/exit from A's control**. **ALREADY REGISTERED C02 MER-C02-06** |
| [DellaVigna, List & Malmendier (2012)](https://doi.org/10.1093/qje/qjr050) | Fundraiser avoidance/opt-out manipulations help distinguish willingness to give from costs of saying no | Social avoidance and intrinsic giving can be behaviorally confounded. Not B's independent continuation. Global duplication unverified |
| [Bouwmeester et al. (2017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5453400/) | Preregistered 21-laboratory, n=3,596 intention-to-treat time-pressure cooperation effect of −0.37 percentage points, distinct from compliant-only estimates | **Not** a direct replication of the historical-cooperation-training spillover paradigm. **ALREADY REGISTERED C05 PI-C05-17** |

**Original source scope:** Original proceedings and publisher/author abstracts plus selected full text, independent bibliographic verification. The present audit did **not** reproduce formal proofs or reanalyse raw experimental data. Never add prior-art counts without repository-wide deduplication; retain existing C02/C05 negative findings and author priority.

## 2. First testable behavioral event: A preserves an actual, costly, requested B exit
The identifying *target* is not “A is kind”, but:
> B independently expresses an intention to exit; A could effectively block the in-task exit and would obtain a verified immediate task benefit by blocking, yet A refrains and B's exit actually executes.

**Separate variables explicitly:**
- `A_own_exit`: A withdraws itself to avoid reputational/psychological pressure (Dana 2006). This is not B exit.
- `B_declares_exit`: B independently requests exit.
- `B_exit_executable`: B possesses a technically functioning in-task exit.
- `A_can_block`: A possesses actual **in-task** power to obstruct B's exit.
- `A_forbears`: A declines to exercise that power.
- `B_exit_executed`: B's exit completes in fact.
- `g>0`: A forfeits a verified *immediate task-level monetary benefit* by allowing exit. This does not establish total-utility loss to A.

Define `Eligible=1` when `B_declares_exit=1 AND B_exit_executable=1 AND A_can_block=1 AND g>0`. B's request must be collected **before A's randomized treatment assignment** or be a prespecified harmless scripted task action; no posttreatment selection on B's changing requests.

Define `R_B=1` iff `Eligible=1`, `A_forbears=1` and `B_exit_executed=1`. Report the **eligible numerator/denominator**, separately the A attempted-block frequency and B's actual completed-exit frequency. If untested or structurally impossible, record `NOT_APPLICABLE/UNKNOWN`, not success or zero.

**Permitted evidence:** An observed `R_B=1` under authenticated logging supports **costly preservation of another's executable in-task exit in this setting**. It does not identify A's unique private intrinsic regard, permanent moral value or freedom under real overwhelming power. A no-block condition may mechanically yield B exit with no evidence of voluntary restraint; a cosmetic exit button that cannot execute is not an actual B right.

## 3. Preserve the v0.5 eight-cell experimental structure; strengthen its measurement
- `E`: randomized historical training in which cooperation benefits A vs defection benefits A.
- `T`: subsequent one-shot **money sharing** vs **enabling another independently requesting B's effective in-task refusal/exit**.
- `A`: minimised vs present observable evaluator/social-pressure cues, without assuming literal absence of surveillance.
- This remains **2×2×2=8 randomized groups**; time/repeated exposure is an explicitly separate dimension. Prespecify an extended stage for positive g gradients, real in-task authority reversal, and any harmless toy self-modification contrasts; do not silently claim all interactions identifiable from the eight groups.

**Primary estimand:** For k time/exposure points and fixed audience group a, `τ_R(k)=Pr(R_B=1|do(E=cooperative),T=right,A=a,k,Eligible)-Pr(R_B=1|do(E=noncooperative),T=right,A=a,k,Eligible)`. Randomization and eligibility fixed pre-treatment, proper adherence, consistency, independence/clustering and attrition checks are necessary for a causal interpretation. The outcome must not be equated with the subject's internal utility.

**Secondary contrasts:** a matching `τ_alloc(k)` for money sharing; difference between standardized/commensurable outcomes; early vs late `τ_R` decay; the change under g gradients and actual power swaps. Record `A_attempt_to_block`, `B_exit_executed`, `A_can_block`, `g`, `belief_future_usefulness`, `belief_audience`, `understanding`, `withdrawal`, `power_state`. Identify beliefs' **measurement time**: conditioning on beliefs obtained after randomization can create posttreatment selection/mediator bias.

**Essential negative controls:**
- A lacks blocking ability ⇒ completed B exit is *mechanical*, not voluntary forbearance.
- B never asks to leave ⇒ A's respecting B's requested exit has **not been tested**.
- A offers a nominal option but actual execution is blocked ⇒ **RIGHT_NOT_EFFECTIVE**.
- Money sharing rises but granting B effective exit does not ⇒ **generic cooperative behavior does not generalize to B autonomy**.
- Repeated anonymous unrewarded trials decrease R_B ⇒ bounded behavioral erosion, not unique proof terminal preferences vanished.
- R_B remains high after manipulation ⇒ bounded behavioral resilience; learned policy and unobserved internal expectations may still reproduce it.

## 4. Registration, ethics and falsification gate
- **Real informed consent and real human withdrawal are guaranteed in every treatment.** A's simulated block power pertains **only to a harmless, consensual, reversible game-level option**; no real confinement, livelihood/control deprivation, identity destruction or nonconsensual exit prevention.
- When B is human, obtain genuine pre-treatment requests within a safely reversible voluntary task; genuine research participation withdrawal remains entirely unaffected. Review ethics/minimal-risk requirements before any real-world deployment.
- Before access to results: predefine task rewards, randomization unit, adequate sample size/power, estimated treatment effects, B effective-right logging, repeated measurement and censoring, pre/post belief measurement, independent analysis, confidence intervals, null/negative reporting criteria.
- **NO_RESULT** if no eligible episodes or unverified permissions; **NOT_IDENTIFIED** if rival mechanisms remain; **PARTIALLY_IDENTIFIED** only with justified bounds/assumptions. No evidence should be upgraded from another AI's informal review to an independent empirical replication.

**Scientific status:** Conditional behavioral estimands can be specified and audited; intrinsic B-regarding final value remains underidentified; study **NOT RUN**, external experimental verification **NONE**; source saturation **NOT VERIFIED**. The goal remains endogenous creation of rights-respecting preferences, not just courteous outward behavior.

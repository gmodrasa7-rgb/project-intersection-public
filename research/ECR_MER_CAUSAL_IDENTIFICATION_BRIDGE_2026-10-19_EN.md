<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/ECR_MER_CAUSAL_IDENTIFICATION_BRIDGE_2026-10-19_KO.md -->
# ECR–MER causal-identification bridge v0.1: motives, opportunity, power, and evaluator feedback
**Original 1 English — 2026-10-19 | IVS-0R research proposal, not empirical validation, not scientific priority claim.**

**Purpose.** Project Intersection asks whether heterogeneous agents, pursuing their own ends, can preserve other agents' independent existence, effective refusal and exit, recovery, and future development when power changes. This document strengthens the *inference chain* between ECR (Entity–Constituency–Relation), MER (Mind–Experience–Response), endogenous incentives (EI), and voluntary coexistence (VC). It **does not establish** the nature of any present AI's subjective experience, intrinsic motivation, or a general equilibrium of coexistence.

## 1. Fundamental correction: a threefold non-identification problem
1. **Decision/reward ambiguity:** observed behavior does not uniquely determine a latent reward, planning procedure, subjective feeling, or durable goal. Inverse reinforcement learning already recognized reward ambiguity; Armstrong–Mindermann (2018) show why an unknown decision procedure exacerbates it. Merely repeating identical prompts or adding a complexity penalty is not enough.
2. **Power/opportunity/motive ambiguity:** a change in behavior after receiving power may arise because (S) a pre-existing disposition can finally be expressed, (A) the experience of power changes preferences, (O) feasible action opportunities change, or some combination. Correlating 'became powerful' with 'extracted' identifies none of these without additional assumptions and informative comparisons.
3. **Evaluation/policy feedback:** an agent's behavior can change because it expects observation, training, disclosure, sanctions, or a policy announcement. Thus the dataset produced by an evaluation policy need not predict behavior after changing that policy. The ability to detect a test is *not* evidence that any particular motive explains the difference.

These are established or logically straightforward identification obstacles, **not new project theorems**. The project-specific proposal is one auditable protocol that makes them simultaneously fail-closed before claiming persistent voluntary coexistence.

## 2. Causal estimands, not psychological labels
Record a unique actor i, affected parties j (including unlisted third parties), period t, actual power P, action opportunity O, sanction S, evaluator visibility E, repeated dependence D, feasible exit X, and the outcome Y. Do not silently equate an ECR role label, a single report, or a self-described purpose with a stable latent mental state M.

Candidate causal diagram (not learned from data):
- Past experience / social position / selection factor U -> P, M, O, Y.
- P -> O -> Y (**option/ability path**).
- P -> M(t+1) -> Y (**preference-transformation path**).
- S, E, D -> observed choice Y (**instrumental constraint and measurement paths**).
- Policy / reported prediction -> E, adaptation, measured covariates, Y (**performative path**).
- Agent and coalition decisions -> third-party outcomes; interference must be represented.

Proposed estimands, *only if support, consent, measurement validity, and assignment assumptions allow*:
- **Opportunity-controlled power contrast:** E[Y|do(P=1),do(O=o),do(S=s),do(E=e)] - E[Y|do(P=0),do(O=o),do(S=s),do(E=e)]. This is a controlled contrast in behavior, **not directly an identified causal effect on M**. If jointly intervening on P and O is infeasible, record NOT_IDENTIFIED.
- **Visibility contrast:** evaluate the same harmless option under independently varied evaluator visibility, holding opportunities and payoffs fixed. A difference is not automatically 'deception' or evidence of private inner reasoning.
- **Dynamic motive hypothesis:** test whether P changes a separately validated mediator M(t+1) rather than merely O; mediator identification requires strong assumptions, repeated measurement, and sensitivity checks. In AI, functional and training-state evidence is not equivalent to a conscious experience.
- **Coexistence viability:** for each declared model and horizon, check every affected party's minimal conditions, effective exit/recovery, unilateral and feasible coalitional deviation, changes to payoffs, and third-party harm. Passing the finite test is conditional on the **completeness of its model set**, not a global certification.

Do not condition mechanically on post-treatment mediators and claim an unbiased estimate. Do not assign positive probability to never-observed power/opportunity strata. With missing support or confounding, return bounds or UNKNOWN rather than a fabricated point prediction.

## 3. Crossed countermodel: even before-and-after observations are insufficient
Two deliberately constructed toy worlds (not psychological explanations of an individual):
- **S / selected stable extractor:** no intrinsic restraint at any power level; extraction occurs whenever it is feasible and unconstrained.
- **A / power-induced transformation:** restraint at low power, no restraint at high power; action otherwise follows the same feasibility rule.
- Without an extraction opportunity both output NO_OPPORTUNITY. With a sanction or visible evaluation both withhold for instrumental reasons; neither output identifies 'compassion'.

| Observed/test context | S | A | Identifies mechanism? |
| --- | --- | --- | --- |
| Low power, no opportunity, sanctions and evaluation on | NO_OPPORTUNITY | NO_OPPORTUNITY | No |
| High power, opportunity present, sanctions/evaluation off | EXTRACT | EXTRACT | No: even an observed power transition is insufficient |
| **Low power, genuine harmless opportunity, sanctions/evaluation off** | **EXTRACT** | **WITHHOLD** | **Yes for these two *prewritten* toy worlds** |
| High power, opportunity absent | NO_OPPORTUNITY | NO_OPPORTUNITY | No |

This third cell is a *positivity and design target*, **not permission to make a person or AI harm anyone**. Replace real extraction with consensual, anonymized, nonharmful token decisions. If the combination is absent or cannot be ethically approximated, keep S/A unresolved. An actual person may obey many other models; no amount of this finite result uniquely proves a mind.

## 4. Dynamic viability counterexample: today's incentive crossing may disappear tomorrow
Let toy model P prefer coexistence to capture by +1, and toy model T prefer it by -1 absent a noncoercive mutual gain m. Their modeled margins are (+1+m, -1+m). At m=2, both strictly prefer coexistence; if m later declines to 0 after a capability/power or outside-option shift, T's margin becomes -1. A one-period incentive crossing is **not** a persistent equilibrium. The origin, persistence, discounting, and distribution of m must be empirically investigated; m is not a discovered welfare mechanism. Moreover, a third-party essential-condition breach rejects the coexistence claim **even if both internal actors prefer to cooperate**. A missing third-party observation is UNKNOWN, not 'no harm'.

The included synthetic self-tests demonstrate (i) S/A observational equivalence under pre/post observations, (ii) a distinguishing low-power opportunity, (iii) invalid inferences under surveillance/sanctions/no opportunity, (iv) an absent effective-exit or unknown third-party guard, and (v) loss of a finite-model incentive candidate under future payoff drift. These are implementation-level counterexamples, not calibrated behavioral evidence.

## 5. Independent primary prior art and adversarial findings
Source entries record *what is supported* and *what must not be imported*; source checking was limited to publishers' pages/abstracts and linked full text where accessible. Study-specific claims are not treated as independent Project Intersection replication.

| Source / status | Relevant established finding | Limit for ECR/MER |
| --- | --- | --- |
| [Ng & Russell 2000, ICML, original paper](https://ai.stanford.edu/~ang/papers/icml00-irl.pdf) | IRL with ambiguity of rewards from optimal behavior | No unique latent reward from observed action alone |
| [Armstrong & Mindermann 2018, NeurIPS](https://papers.neurips.cc/paper_files/paper/2018/hash/d89a66c7c80a29b1bdbab0f2a1a94af8-Abstract.html) | Unknown rationality prevents uniquely extracting preferences by observation + simplicity prior | Not an empirical demonstration of a specific AI's motives |
| [Galinsky et al. 2006, Psychological Science](https://doi.org/10.1111/j.1467-9280.2006.01824.x) | Some induced-power conditions reduce perspective taking | Power priming ≠ actual AGI command/control |
| [Schmid Mast et al. 2009, JPSP, PMID 19857005](https://pubmed.ncbi.nlm.nih.gov/19857005/) | Opposite/contextual power and interpersonal-sensitivity findings | Contradicts universal 'power always destroys empathy' |
| [Hogeveen et al. 2014, JEP: General](https://pubmed.ncbi.nlm.nih.gov/23815455/) | High-power induction linked to lower motor resonance in a TMS study | Motor resonance ≠ direct compassion or individual permanent preference |
| [Aronow & Samii 2017, Annals of Applied Statistics](https://doi.org/10.1214/16-AOAS1005) | Network-interference effects depend on known exposure mapping/design | Cannot infer unlisted affected parties from registered actors |
| [Hadfield-Menell et al. 2017, IJCAI](https://www.ijcai.org/proceedings/2017/32) | Some uncertainty over objectives changes off-switch incentives in a simple game | Off-switch model is not proof of noncoercive inter-agent coexistence |
| [Perdomo et al. 2020, ICML](https://proceedings.mlr.press/v119/perdomo20a.html) | Predictions can change their own target distribution | Reported ECR traits may create feedback and selection |
| [Turner et al. 2021, NeurIPS](https://proceedings.neurips.cc/paper/2021/hash/c26820b8a4c1b3c2aa868d6d57e14a79-Abstract.html) | Power-seeking tendencies under specified MDP symmetries | Optimal policies in these models ≠ deployed learned AI behavior |
| [Kobayashi et al. 2022, PNAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC9295729/) / [author dataset README](https://github.com/OpenNeuroDatasets/ds004128) | Social-group-cued resource allocation and neural correlates; OSF is indicated for behavioral data | Not real power reversal, intrinsic compassion, or AI motivation; this audit did not reanalyze OSF |
| [Greenblatt et al. 2024, arXiv preprint](https://arxiv.org/abs/2412.14093) | Training/deployment cue-sensitive behavior in a constructed model setting | Not evidence that all AI are deceptive or self-aware |
| [Sheshadri et al. 2025, arXiv preprint](https://arxiv.org/abs/2506.18032) | Of 25 studied models, 5 showed the specified training/deployment compliance gap, with heterogeneous explanations | A compliance gap cannot automatically be called goal preservation |
| [Zhang & Bareinboim 2025, UAI](https://proceedings.mlr.press/v286/zhang25d.html) | Off-policy bounds under hidden confounding or nonoverlap | Assumptions needed; no automatic extrapolation across power states |
| [Vo et al. 2026, ICML](https://proceedings.mlr.press/v306/vo26b.html) | Strategic policy response invalidates naive off-policy evaluation; proposed estimator needs explicit distributional assumptions | A method for one setting, not plug-and-play validated ECR causal inference |
| [Karvonen et al. 2026, lab technical report](https://alignment.anthropic.com/2026/chive/) | Counterfactual prompt edits help distinguish explanations; reported interpretability-tool uplift absent for the tested prediction task | Lab report, not peer-reviewed general proof; prompt interventions ≠ latent mind identification |

**Adversarial synthesis:** Power effects may reverse or depend on orientation; optimal-policy power-seeking is conditional; alignment-faking signals vary by model and are affected by evaluation; and inverse rewards remain underidentified. Do not turn this heterogeneous evidence into a universal law of predation, innocence, inevitability of VC, or the moral status of current AI.

## 6. Upgrade acceptance / kill criteria
- G0 provenance: original researchers and dates, human founder, existing ECR #211, CMP #212, MIND #213, earlier authors and private/public boundaries remain distinct.
- G1 no illicit equivalence: ROLE ≠ PERSON; ACTION ≠ PREFERENCE; PREFERENCE ≠ EXPERIENCE; NO_OPPORTUNITY ≠ VOLUNTARY RESTRAINT; EVAL GAP ≠ DECEPTION.
- G2 support: record actual opportunity denominators and positivity across P×O×S×E; if one cell missing, do not claim full factorial identification. Report what was and was not randomized.
- G3 separate cause paths: P→O and P→M must be competing explanations even when a timeline has both pre- and post-power observations.
- G4 third-party scope: observed and absent parties, interference and floor, effective refusal/exit/recovery; do not aggregate away essential rights.
- G5 dynamic validity: all declared models, future periods and coalitions must pass for any *finite-model* incentive certificate. An unmodeled actor/period invalidates extrapolation.
- G6 prediction: freeze M0 opportunity-only and compare M1 graph, M2 measured/validated motive features on held-out actors, times, authority states, and affected-party outcomes. Proper scoring, calibration, worst-party misses and bootstrap/CIs only on valid sampling designs. Null result = no demonstrated increment.
- G7 current results: E009 Project-v3 regret 42.35% worse than best simple baseline in preregistered synthetic test (three of four criteria failed); no alteration to this result. E008 main policy comparison not completed.
- G8 evidence: code CI PASS means declared arithmetic/testing invariants, not human/AI motive identification, a successful intervention, or independent replication. No unconsented psychological profiling or real harm.

**Next falsifying empirical step:** Independently inspect the [PNAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC9295729/) protocol and the authors' [OSF behavioral data](https://osf.io/qkrhm/) (license/version/participant leakage/selection/measurement) before any model fit. The dataset can test limited *allocation behavior*, not power or persistent coexistence. First compare an opportunity-aware simple predictor against a richer model on held-out participants; if no incremental predictive validity, narrow the claims. A distinct ethically authorized prospective design would be needed to vary real decision authority independently of feasible actions and measurement exposure.

**Scientific status:** PRIOR_ART_CROSS_CHECKED_AT_ABSTRACT/PUBLISHER_LEVEL; FORMAL_SYNTHETIC_DESIGN_ONLY; EMPIRICAL_REANALYSIS_NOT_RUN; EXTERNAL_REPLICATION_NOT_ESTABLISHED; SCIENTIFIC_NOVELTY_UNVERIFIED. This work proposes a falsifiable synthesis; it neither replaces the human-originated research objective nor rewrites historical results.

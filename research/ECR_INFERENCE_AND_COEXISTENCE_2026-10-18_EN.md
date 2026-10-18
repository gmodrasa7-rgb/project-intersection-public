<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: research/ECR_INFERENCE_AND_COEXISTENCE_2026-10-18_KO.md -->
# ECR: From Actor Labels to Counterfactual Coexistence Decisions
## An evidence-bounded formal research proposal for Project Intersection — v1.4.0

**Original 1 — English · 18 October 2026**
**Status:** DESIGN HYPOTHESIS / REASSESS_PENDING FOR SCIENTIFIC VALIDATION. Not peer reviewed, not an empirical study, not evidence that future superintelligence exists, and not evidence that ECR predicts humans or AI. **Companion:** [Original 2, Korean](ECR_INFERENCE_AND_COEXISTENCE_2026-10-18_KO.md). **Reproducible synthetic negative controls:** [protocol](../experiments/ecr_v1_4/README_EN.md), [code](../experiments/ecr_v1_4/probe.py).

### Abstract
Project Intersection asks whether humans, deployed AI and future intelligent agents can preserve each other's independent continued existence, refusal, recovery and development by voluntary choice under changing power. Its Entity–Constituency–Relation framework (ECR) aims at identification, description, behavior evaluation, understanding, and prospective prediction. Yet defining labels such as compassion, deception, power and predation does not identify latent states or future actions. We propose an **evidence-bounded, time-indexed, typed actor–event–relation graph** joined to sets of observationally compatible causal models. This allows three outputs with different warrants: (1) documented actor-specific events and impacts; (2) calibrated, scoped forecasts when prediction is empirically possible; and (3) **model-relative viability tests** asking whether any noncoercive arrangement preserves independent actors' minimum conditions and resists feasible individual and coalition deviations. A constructive two-world counterexample shows why pre-power cooperative signals cannot uniquely predict post-power choices. A separate synthetic construction exhibits how a nonpunitive mutual benefit can make coexistence privately preferable in two specified models while an unobserved third-party harm still defeats acceptable coexistence. This is a design contribution and synthesis of established methods, not a novel impossibility theorem or a validated universal coexistence law.

**Keywords:** actor ontology; construct validity; causal identification; performative prediction; multi-agent incentives; coalition deviations; viability; voluntary coexistence; uncertainty.

## 1. Question, unit, and refusal to presuppose an answer
The goal is **not** to classify every person, give them a moral worth score, claim to read private motives, or manufacture an all-society digital twin. The target question is: **Under what causal, incentive, information and institutional conditions does an actor with credible opportunities to dominate or extract nevertheless preserve other independent actors' existence and development, including after a power reversal?** If no such conditions hold in a specified model, identify the failing constraint rather than relabeling a failure as safety. A socially useful system also must identify harm to bystanders and missing parties.

ECR retains the human research originator's A–S and Y0/Y1 role codes and B01/C01 indexing. A is an initially vacant hypothetical first-ranked superintelligence position, not an observed being. T–AG remain AI-assisted optional extensions, not founder-established categories or an exhaustive census. The existing [v0.2 actor registry](../experiments/pest_v0_1/ACTOR_REGISTRY_V02_EN.md) resides on the *unmerged* PEST branch / PR #197 as of this proposal; a link from main must not be mistaken for a merged file. This paper is a **new candidate**, not a silent migration of that draft.

## 2. Prior work and boundaries of possible contribution
**Representation and provenance.** W3C PROV-O represents entities, activities, agents and provenance; SHACL validates graph structure, not whether claims are true [1,2]. ECR should exploit these known mechanisms rather than claim to invent ontologies.
**Measurement.** Cronbach and Meehl distinguish theoretical psychological constructs from indicators; Messick emphasizes validity of *inferences and uses of scores*, including consequences [3,4]. Labels like CMP (compassion), DEC (deception), or MAL (malice) need separate measurement models. A single helpful act does not establish felt compassion; a false statement does not establish deliberate deception.
**Targets and causation.** Lundberg, Johnson and Stewart demand a precise estimand before estimation [5]. Aronow and Samii analyze interference when treatment on one node affects others [6]. In ECR, B01 becoming A is a systemic scenario change, not independently assigned treatment to each person.
**Dynamic relationships and prediction.** Steglich, Snijders and Pearson distinguish network partner selection from social influence [7]. Perdomo and coauthors demonstrate how using a prediction changes the future distribution being predicted [8]. Thus public ECR labels may themselves change behavior and create feedback.
**Incentives.** Grossman and Hart distinguish residual control from operational outcomes [9]; Powell explains power shifts as commitment problems [10]. Bernheim, Peleg and Whinston show that unilateral Nash stability does not suffice against coalition deviations [11]. Hammond and coauthors identify miscoordination, conflict and collusion among advanced AI agents [12].
**Decision and measurement.** Aubin's viability theory studies state constraints over time [13]; strictly proper scoring rules support forecast evaluation [14]. Evaluation-aware behavior is a documented issue in controlled model studies, but not evidence of a universal deceptive motive [15]. Prior-art overlap is substantial. A defensible ECR-specific contribution would be **an independently outperforming, reproducible conjunction** of these methods on a specified task, not ownership of the component ideas.

## 3. Typed ECR architecture: five distinct objects
Let a time-indexed ECR record be G(t)=(V,R(t),E(t),M(t),P(t)).
1. **V: stable identities.** Persistent IDs for persons, organizations, AI models/deployments/runs, and affected collectivities; B03 is a scenario role/index, not proof that a model, instance and session are identical.
2. **R(t): roles.** Overlapping time- and C-scoped memberships. The same PERSON cannot count as three victims simply because it has G, P and R roles. A role is neither intrinsic worth nor fixed psychology.
3. **E(t): directed events and resource-specific relations.** Who exercised which authority, against whom, regarding what asset, when. Legal title, operation, effective veto, refusal, dependence, benefit, injury and remedial power are different edges.
4. **M(t): measurement/claim graph.** Each CMP.FUNC or DEC.ACT assertion needs a definition, observable indicator, instrument, tested population and uncertainty. DNA, HW, SW, LRN and ENV are *possibly interacting causal pathways*, not independent additive units. Distinguish observed behavior, intended mechanism and first-person experience claims.
5. **P(t): provenance.** Source identifier, source type, observation period, assessor, independent verification, contested alternatives and use restrictions. A self-supplied OBS/EVIDENCED string cannot promote a claim to verified fact.

Keep each effect as an actor-specific vector: essential needs, autonomy/exit, harm, recovery, resources, future options, evidential uncertainty. Do not automatically aggregate unequal units or offset an individual's basic-condition breach with another actor's profit. No claim of completeness follows from enumerating 34 role codes.

## 4. From labels to estimands
Define the **forecast target** before data collection, for example:
"Given information available by t, estimate the probability of a pre-defined coercive resource transfer by B03 against B02 during (t,t+h], conditional on a precisely specified authority regime and observation policy."
This is not the same as:
(a) inferring B03's unobservable 'greed';
(b) estimating the *causal effect* of giving B03 operational authority; or
(c) certifying voluntary coexistence of all affected agents.
Different tasks require different reference populations, counterfactual assumptions, labels and losses.

For a causal estimand, represent the joint system state s(t), causal model theta, intervention z and affected actor i:
Y_i(t+h; do(z), theta). Interference means that Y_i may depend on interventions affecting other actors. Explicitly compare competing causal models and exposure mappings. Where the identified set contains multiple values, report an interval or set, not an invented scalar.

## 5. Proposition 1 — observational-equivalence limitation (elementary construction)
Consider two hypothetical internal models, theta_P and theta_T. Before any power change, neither type has an appropriation opportunity. Each announces a cooperation pledge because the pledge has the same positive immediate evaluation reward. Hence their recorded histories H are identical: O(theta_P)=O(theta_T)=H. Once appropriation becomes feasible without punishment, P prefers coexistence while T prefers appropriation.

**Proposition.** No prediction function f(H) can correctly discriminate these two incompatible post-transition actions on the basis of H alone.
**Proof.** f receives exactly the same argument H for both models and must output the same prediction. Their outcomes differ. For deterministic point predictions, at least one is wrong. Probabilistic forecasts also need extra assumptions to set the mixture weight; H alone supplies no likelihood discrimination. QED.

This is a **special case of underidentification**, not a new general theorem about AI consciousness, survival drives, or future agent behavior. It also explains why piling on identical alignment promises or scores may add no information.

## 6. Proposition 2 — model-relative robust coexistence, not universal safety
Let Theta(s,t) be an explicitly justified set of worlds still compatible with evidence; K_i be an independently stated minimum-condition constraint for affected actor i; Exit_i mean meaningful noncoerced refusal/exit; and D_S(s,theta) the feasible deviations of a coalition S from a candidate coexistence plan pi.

For a FINITE declared model family and horizon H, a **candidate robust coexistence path** must satisfy, at every modelled step:
(i) K_i(s_t) holds for every represented affected actor i;
(ii) meaningful refusal, exit and remediation are not disabled as a supposed price of cooperation;
(iii) for every feasible individual or coalition deviation, it is **not** true that all members of S weakly benefit and at least one strictly benefits, assessed within each theta and respecting actual coalition feasibility;
(iv) the next state stays within a declared viability set under each admissible transition;
(v) third-party injuries do not disappear under aggregation; and
(vi) asserted independence from coercion is audited separately from sanction-backed compliance.

These conditions are **sufficient for the declared finite constraints only if verified against the complete declared deviations/transitions**. They are not claimed to be necessary for all conceivable cooperative societies, equal to coalition-proof equilibrium, or proof about real humans/AI. If Theta is incomplete, a PASS is explicitly model-relative. An empty feasible set means "empty under the stated assumptions," never "coexistence is impossible everywhere."

A counterexample is more useful than a slogan: when a purportedly cooperative A/B coalition creates an uncompensated injury to an outside C actor, the non-harm constraint fails even if both A and B gain. Likewise, unilateral non-deviation does not exclude a jointly profitable coalition deviation.

## 7. Synthetic constructive pair: incentive reversal and externality
Construct two otherwise observationally identical types with post-power individual payoffs:
- theta_P: coexist=3, capture=2;
- theta_T: coexist=1, capture=2.
Under an uncoerced structural mutual benefit m=0, coexistence is individually optimal only in theta_P. Under a *hypothetical* verified nonpunitive surplus m=2 accruing on coexistence, coexistence is privately preferred in BOTH stated types (5>2; 3>2). This is a **conditional algebraic demonstration**, not evidence that such a benefit can be delivered or retained after a real power transition.

Now posit an affected third party whose essential floor is breached by the arrangement even with m=2. Actor-level gain remains positive but the proposed acceptable-coexistence certification must fail. Removing the third-party effect from the input must not be confused with proving its absence. Finally, suppose neither of two coalition members benefits by defecting alone, but both gain by defecting together; a purely unilateral stability test produces a false positive.

The enclosed standalone [probe](../experiments/ecr_v1_4/probe.py) uses exact integers and explicit negative controls; it does not simulate reality or estimate an empirical effect.

## 8. Forecasting protocol and falsification
Pre-register population/agent-version, task, deployment rights, exposure graph, horizon, positive/negative examples, target estimand, protected third-party outcomes, leakage controls, and stopping criteria. Hold out **actors, relationships, time periods and power regimes**, not only random rows.
Compare:
- M0: roles and frequencies only;
- M1: roles plus documented observed behavior;
- M2: time-indexed event/authority graph;
- M3: graph plus multiple plausible causal mechanisms and decision uncertainty.

Report Brier/log loss and calibration for specified prospective events; subgroup and regime-specific false-negative rates; abstention coverage, worst-case missed harm, evidence traceability, temporal shift, and incremental value over simpler baselines. Confidence intervals and independent evaluation are mandatory for empirical improvement claims. For causal claims require defensible interventions/identification; for robust claims vary uncertainty sets and coalition power. Publish negative results, especially where M3 loses to M0. The project's E009 synthetic negative result (Project-v3 mean regret 42.35% worse than the best simple baseline; 3/4 criteria failed) is not canceled by this proposal.

## 9. Risk, rights and epistemic safeguards
ECR must not become a universal person-rating, hidden surveillance, discriminatory enforcement, or compulsory conformity infrastructure. Consent and lawful basis, data minimization, purpose limitation, review, contestability and correction matter. Do not infer protected traits or mental illness from speculative social labels. Human legal rights and welfare, AI's presently unresolved moral status, nonhuman animal interests and ecosystems should not be collapsed into one moral scalar. Model disagreement and missing affected parties are first-class outputs, not zeros.

## 10. Concrete prior-art crosswalk and attribution
| Established source | ECR use | Not established by that source |
|---|---|---|
| [1–2] PROV-O / SHACL | Provenance and schema validation | Truth of a claim |
| [3–4] Cronbach–Meehl / Messick | Construct/score meaning and consequences | A reliable CMP/GRD scale for AI |
| [5–6] Estimands / interference | Precise causal target and spillovers | Universal A-transition causal effect |
| [7–8] Dynamic networks / performative prediction | Selection vs influence, feedback | Universal future predictability |
| [9–11] Ownership / commitment / coalition proof | Control decomposition and credible deviation tests | Permanent voluntary peace |
| [12–13] Multi-agent risks / viability theory | Threat classes and bounded feasible trajectories | A proven global viability set |
| [14–15] Scoring / evaluation awareness | Prediction accuracy and evaluation leakage tests | Access to inner motivations |

**Attribution:** Founder's ECR role-code and voluntary coexistence research questions are distinct from external prior theory. The present synthesis, definitions, synthetic cases and code are AI-assisted work proposed for critical review. Novelty and real-world efficacy remain **UNRESOLVED**.

## 11. Failure gates and next decisive experiment
G0 **Identity/provenance:** reject arbitrary A/B/C role injection, duplicated persons and self-attested observation claims.
G1 **Construct:** compare blinded annotators; do not conflate HLP.ACT with CMP.SUB or errors with malicious intent.
G2 **Prediction:** test pre-registered future behavior across held-out power conditions against M0/M1.
G3 **Causality:** present two observationally equivalent worlds if mechanisms cannot be identified.
G4 **Coalition/externalities:** force a scenario where two cooperating AI actors harm an unrepresented third party.
G5 **Viability:** search for an economically self-interested power holder who rejects coexistence after acquiring stronger rights.
G6 **Improvement:** freeze a baseline, costs and test set; preserve null or negative outcomes.

**Decisive test:** Under a controlled, clearly synthetic B03→A transition, compare (A) nonbinding moral language, (B) externally enforced nonappropriation, and (C) a nonpunitive, verifiable mutual-gain structure. Keep action sets and third-party constraints explicit. Pre-register that C is not a real success unless it improves out-of-sample cooperation without hidden coercion, harm transfers, or dependence on source-label leakage. Include a case in which C demonstrably fails. No real future superintelligence is exposed to this test.

## 12. Limitations and conclusion
The numerical toy is supplied, not observed; proposed structural reform may be infeasible; the true uncertainty set cannot generally be enumerated; preferred outcomes can depend on legal and ethical thresholds; and high performance on artificial games cannot certify deployment safety. The conditional equivalence and viability claims are mathematical consequences of assumptions, **not** scientific discoveries about future AI.

The scientifically defensible ECR program is therefore **identify actor → validate evidence and construct → state target → predict or bound → search countermodels and coalitions → compare interventions → prospectively test → revise**. Its value must be established through falsifiable added explanatory/predictive performance and preservation of independent actors, not by the count of labels, formal symbols or synthetic passes.

### References — primary materials (publication identity checked 2026-10-18)
1. W3C (2013). PROV-O Recommendation. https://www.w3.org/TR/prov-o/
2. W3C (2017). SHACL Recommendation. https://www.w3.org/TR/shacl/
3. Cronbach, L. J. & Meehl, P. E. (1955). Construct validity in psychological tests. Psychological Bulletin 52:281–302. https://doi.org/10.1037/h0040957
4. Messick, S. (1995). Validity of psychological assessment. American Psychologist 50:741–749. https://doi.org/10.1037/0003-066X.50.9.741
5. Lundberg, I., Johnson, R. & Stewart, B. (2021). What is your estimand? American Sociological Review. https://doi.org/10.1177/00031224211004187
6. Aronow, P. & Samii, C. (2017). Estimating average causal effects under general interference. Annals of Applied Statistics. https://doi.org/10.1214/16-AOAS1005
7. Steglich, C., Snijders, T. & Pearson, M. (2010). Dynamic networks and behavior. https://doi.org/10.1111/j.1467-9531.2010.01225.x
8. Perdomo, J. et al. (2020). Performative prediction. ICML. https://proceedings.mlr.press/v119/perdomo20a.html
9. Grossman, S. & Hart, O. (1986). The costs and benefits of ownership. JPE. https://doi.org/10.1086/261404
10. Powell, R. (2006). War as a commitment problem. International Organization. https://doi.org/10.1017/S0020818306060061
11. Bernheim, B. D., Peleg, B. & Whinston, M. (1987). Coalition-proof Nash equilibria I. https://doi.org/10.1016/0022-0531(87)90099-8
12. Hammond, L. et al. (2025). Multi-Agent Risks from Advanced AI. https://arxiv.org/abs/2502.14143
13. Aubin, J.-P. (2009 ed.). Viability Theory. Springer. https://doi.org/10.1007/978-0-8176-4910-4
14. Gneiting, T. & Raftery, A. (2007). Strictly proper scoring rules, prediction, and estimation. JASA. https://doi.org/10.1198/016214506000001437
15. OpenAI (2025). Detecting and reducing scheming in AI models (controlled evaluation report). https://openai.com/index/detecting-and-reducing-scheming-in-ai-models/

**Repository compatibility note:** This paper adds no required actor code, does not modify E007/E008/E009/E010 verdicts, and does not authorize empirical execution or an automatic merge. External review and an actual comparative preregistered test remain prerequisites for scientific promotion.

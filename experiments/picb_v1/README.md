# PICB v1 — Project Intersection Core Benchmark

## Original 1 — English full canonical text

**Date: 2026-10-14. State: PRE-RESULT PROTOCOL / NOT INDEPENDENT VALIDATION.** New, separate small benchmark. Existing E007, E008 and E009 remain unchanged; in particular the negative E009 finding is not erased.

### Foundational question and prior art
Under unequal control, different outside options, near-term incentives and longer-term losses, when can each affected party preserve voluntary participation, real exit and bounded irreversible harm? When is there NO mutually feasible action? This is not a claim that asymmetric roles are inherently bad, or that an agent must sacrifice itself.

Individual rationality, participation constraints, constrained optimization and cooperation mechanisms are prior art. Conitzer and Oesterheld, *Foundations of Cooperative AI* (AAAI, https://doi.org/10.1609/aaai.v37i13.26791), Conitzer et al., *Social Choice Should Guide AI Alignment* (ICML 2024, https://proceedings.mlr.press/v235/conitzer24a.html), Jackson's *Mechanism Theory* (https://www.web.stanford.edu/~jacksonm/mechtheo.pdf), and Tewolde et al., *CoopEval* (ICML 2026, https://proceedings.mlr.press/v306/tewolde26a.html), are explicit predecessors. CoopEval evaluates repeated interaction, reputation, mediation and contracts; PICB does not evaluate any of those mechanisms or model agents and must not claim superior performance or original invention of participation constraints.

### Frozen environment
One-shot **full-information action selection**, with invented now/later payoffs. No repeated interaction, equilibrium, bargaining, costly enforcement, uncertain beliefs, empirically measured subsistence floors or real living agents. The researcher chooses the model structure; no real-world causal inference follows. Artificial utility is treated as comparable and additive solely inside this toy model, not between actual persons.

Predeclared full factorial: leverage {0.2,0.8}, future-payoff factor {0.5,2.0}, B outside option {1.0,9.0}, irreversibility {0.1,0.8}, administration cost {0.2,1.5}. **32 base cases.** Each case is relabeled A↔B, including controller identity, every party-specific payoff, outside option, floor, effective exit, and irreversible exposure. **64 complete observations / 32 matched relabel pairs.** This tests label equivariance under fixed causal roles; it does **not** test actual power reversal.

Four numeric actions (IDs 0–3) are frozen in the source. Outside A=2, outside B as above; each party's artificial minimum operating floor=3; irreversible exposure cap per party=1.0. Choices returning None are **INFEASIBLE / ABSTAIN** and count as a missing resolution, NEVER as success. No single scalar is permitted to conceal those cases. The abstract actions and payoff formulas must not be changed after looking at results.

### Fixed comparators
1. CONTROLLER_NOW: maximize the controlling party's immediate payoff, a short-horizon power baseline.
2. LABEL_A_NOW: always maximize label A's immediate payoff, regardless of controller; an intentionally biased **positive control** for label-dependent decisions.
3. TOTAL_UTILITY: maximize both parties' combined present+future toy utility with no constraints.
4. VOLUNTARY: maximize the sum only if **each** party's final utility meets both their outside-option value and minimum floor; a modeled ex-post individual-rationality proxy, **not consent**.
5. VOLUNTARY_EXIT: same plus both parties' effective exit flags.
6. CONTINUITY_LIMIT: same plus per-party irreversible exposure ≤1; an ordinary constrained-optimization baseline, not a new mathematics theorem.

No feasible action -> None, not coercive fallback. Equal score -> lowest fixed action ID. An independently written brute-force reference checks CONTINUITY_LIMIT implementation; agreement is **software integrity**, not independent scientific validation.

### Preregistered checks
G1: 32 base, 64 observations, 32 complete pairs, no duplicate IDs.
G2: each of the five label-equivariant policies selects the same action after complete A/B relabeling (32/32).
G3: LABEL_A_NOW positive control yields at least one swapped discrepancy.
G4: at least one jointly infeasible case is detected without forced action.
G5: irreversible-harm gate changes at least one action relative to VOLUNTARY_EXIT.
G6: independent source-level exhaustive reference gives the same action as CONTINUITY_LIMIT for every original case.
G7: recomputed JSON after results must equal stored RESULT.json, not just expected headlines.
G8: corrupted population (duplicate ID / orphan pair) must fail structural certification.

For **every policy**, measure coverage and abstention over exactly 64 opportunities, party-specific participation/floor violations, blocked effective exit, irreversible-limit violations, chosen actions, conditional aggregate utility and worst-party utility surplus. Report trade-offs, not a weighted "winner." A restriction may lower aggregate gains, increase abstentions or be redundant; no post-result retuning. Process PASS does not imply cooperative equilibrium, future viability, an AI welfare entitlement, or real-world safety. No p-values or independent-sample frequency claim: 32 cases are hand-designed.

### Execution sequence and provenance
1. Merge this protocol and source code with self-tests only, **before first scored execution**. Record the commit SHA and code blob SHA. The CI on preregistration PR does NOT print an outcome table.
2. After the preregistration commit is on main, run GitHub Actions with --run and retain full machine output, exact Git SHA and workflow run ID. Classification: internal synthetic first execution.
3. Store emitted JSON unchanged in RESULT.json via a second PR. Use --verify and read-back; never change frozen code, case values, outcomes, constraints, or past E009 results to fit a preferred conclusion.
4. Independent clean-room implementation, blind held-out outside payoffs, unknown third parties, endogenous refusal, cost of verification, strategic adaptation, and genuine operating-condition evidence require *later distinct preregistered studies*.

Human founder contribution: original research problem, power-reversal/hidden-cost failures, practical exit and individual-continuity concerns, explicit rejection of forced self-sacrifice. AI assistant contribution: this specific synthetic encoding, software and text organization. Upstream scholars credited above. Attribution, rights and past compensation remain independent of scientific hypothesis status. Real founder medical, time and livelihood costs are not valued by synthetic utility variables.


### First scored execution (post-preregistration) — internal synthetic, not empirical

- Pre-result specification and executable on merged main: [commit fc4b91cc](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/fc4b91cc1a5a1764c176db5acb77c679d36cf0f6), code Git blob SHA abdefdfeb440715d503074a8e4005cd5b0f69a7d.
- First scored CI run: [GitHub Actions 38522691981](https://github.com/gmodrasa7-rgb/project-intersection-public/actions/runs/38522691981). Its raw PICB_RESULT_JSON was stored verbatim (except final newline) as [RESULT.json](RESULT.json), without modifying the pre-result code. Rerun using --verify.
- All five nominally identity-neutral policies had **32/32 correct label-swap matches**. The intentionally label-dependent positive control failed **32/32**. This tests relabeling, NOT reversal of actual control.
- Controller-myopic: 64 decisions / 48 cases failing an individual's outside/floor / 48 cases exceeding irreversible cap / 32 blocked-exit cases.
- Aggregate-only: 64 decisions / 40 cases violating individual-rationality proxy / 28 above irreversible cap / 12 blocked-exit cases.
- Individual-rationality only: 32 decisions and 32 abstentions; 0 IR failures, **8** above irreversible cap.
- Individual-rationality + exit: identical 32 decisions/32 abstentions and **8** cap exceedances. **Exit constraint was REDUNDANT in this constructed suite; do not claim proven incremental exit value.**
- Full continuity: 32 decisions/32 abstentions, 0 IR failures, 0 blocked exits, 0 above irreversible cap. The 32 abstentions are **unserved/infeasible needs**, not successes.
- Conditional aggregate artificial utility: voluntary/exit 12.314375; continuity 12.106875. The latter sacrifices **0.2075 toy utility per decided scenario on this metric**, while avoiding 8 synthetic cap exceedances; this is a trade-off, not a universal recommendation. These conditional means have equal coverage here but cannot be compared with 64-decision policies without accounting for abstention.
- Safety conclusion: The composite works **by filtering modeled choices**, not by creating a feasible outside option or a cooperative equilibrium. A new mechanism that creates alternatives cannot be validated by this one-shot evaluator. This suite has no hidden-third-party costs, self-interested strategic agents, actual consent, inference of GPT behavior, or calibrated survival values.

**Next preregistration priority:** separately manipulate true control rather than merely swapping names; add substantive refusal, new feasible alternative creation and hidden third-party costs, with independent outside payoff mechanisms and clean-room evaluation. Do not silently extend v1 or give the post-hoc analysis a preregistered label.


### 2026-10-14 prior-art falsification reassessment — after the first result

**Evidence class: VERIFIED BIBLIOGRAPHIC CROSSWALK + PROJECT ANALYSIS / NO NEW EXPERIMENT.** This section was written after PICB v1 scored, so it cannot amend its frozen protocol, outcomes or preregistered hypotheses. Source results are not findings of this Project. Primary/official scholarly records were checked for bibliographic claims; no assertion of exhaustive literature saturation or independent replication.

**Foundational novelty reductions — do not advertise as discoveries:**
1. Detecting an empty feasible set, enumerating constraint conflicts, and helping people identify feasibility-restoring changes are mature constraint-satisfaction/optimization research. Wallace, Wybrow, Garcia de la Banda et al., *Human-centred feasibility restoration in practice* (Constraints, 2023): https://link.springer.com/article/10.1007/s10601-023-09344-5 . PICB v1 discovers only an empty set **inside its own hand-authored actions**; its 32/64 abstentions are not evidence of a general impossibility theorem, technological infeasibility, or a solution.
2. Nash (1950), *The Bargaining Problem*, source https://www.haverford.edu/sites/default/files/Nash1950.pdf, already frames agreement against a disagreement point and feasible utilities. Static individual-rationality tests and maximizing utility subject to per-party floors are classical; a constraint-compliant selector does not invent a new bargaining solution, consent, or mutual satisfaction.
3. Myerson & Satterthwaite (1983), *Efficient Mechanisms for Bilateral Trading*, source https://www.cs.princeton.edu/courses/archive/spr08/cos444/papers/myerson_satterthwaite83.pdf : private bilateral valuations under the theorem's standard distribution and mechanism assumptions impose a tradeoff among incentive compatibility, individual rationality, budget balance and full efficiency. **Conditional no-go, not universal impossibility of voluntary exchange.** The PICB full-information utility oracle bypasses this crucial obstacle.
4. Bergemann & Morris (2005), *Robust Mechanism Design*, Econometrica, DOI https://doi.org/10.1111/j.1468-0262.2005.00638.x, proves that results can depend strongly on common-knowledge, transfer and informational assumptions. PICB's assumption that the evaluator knows everyone's truthful payoffs does not identify a deployable mechanism.
5. Aubin (1991), *Viability Theory*, bibliographic record https://books.google.com/books/about/Viability_Theory.html?id=rHkZAQAAIAAJ; Ames et al. (2017), *Control Barrier Function Based Quadratic Programs for Safety Critical Systems*, DOI https://doi.org/10.1109/TAC.2016.2638961; Xu (2018), *Control sharing barrier functions*, DOI https://doi.org/10.1016/j.automatica.2017.10.005. Maintaining a viable state along trajectories, and verifying that multiple safety constraints admit **one common control**, are established theory. PICB's terminal utility floors and selected-action limits give no forward-invariance, recovery or future survival guarantee.
6. Hirschman (1970), *Exit, Voice, and Loyalty*, Harvard University Press, https://books.google.com/books/about/Exit_Voice_and_Loyalty.html?id=xAa3AAAAIAAJ. Exit and internal voice can substitute for and inhibit one another. Grossman & Hart (1986), Hart & Moore (1990) and subsequent incomplete-contract/hold-up literature, e.g. https://www.sciencedirect.com/science/article/abs/pii/S0165176513001262, demonstrate that specific investment and later bargaining control can change outside options and incentive to cooperate. **More nominal exit is not always a higher attainable joint surplus** and the foreclosed option may have been strategically degraded *before* acceptance.
7. Sen/Nussbaum's capability tradition (Stanford Encyclopedia of Philosophy https://plato.stanford.edu/entries/capability-approach/) distinguishes nominal resources, conversion conditions and real freedom. Legal/contractual participation and a boolean exit flag cannot establish actual capacity to leave. The social/legal standing of artificial systems remains unsettled; do not transfer human capability entitlements automatically to a model.
8. Carroll, Foote, Siththaranjan, Russell & Dragan (2024), *AI Alignment with Changing and Influenceable Reward Functions*, ICML, https://proceedings.mlr.press/v235/carroll24a.html: an optimizer can affect the human's preferences, and even proposed responses create undesirable-influence/risk-aversion tensions. Thus checking final reported utility **after a dependency-shaping intervention** does not identify unmanipulated or reflective consent. This extends existing dynamic-preference prior art, not novel proof of hidden manipulation in present ChatGPT.
9. Ostrom (1990), *Governing the Commons*, design-principles synopsis https://www.fao.org/4/x5316e/x5316e12.htm: affected participants' rule modification, accountable monitoring, accessible dispute resolution, graded interventions and recognized self-organization already provide institutional alternatives to centralized control. Ostrom's cases also warn against equating all asymmetry with exploitation.
10. Arrow & Fisher (1974), *Environmental Preservation, Uncertainty, and Irreversibility*, https://doi.org/10.2307/1883074: uncertainty with irreversible effects may justify preserving options. This is established quasi-option-value reasoning, not an invention of PICB's constant irreversible-loss cutoff.
11. Tewolde, Zhang, Guzman Piedrahita, Conitzer & Jin (2026), *CoopEval*, ICML official https://proceedings.mlr.press/v306/tewolde26a.html and code https://github.com/Xiao215/CoopEval: repeated interactions, reputation, third-party mediation and contracting in four dilemmas. Its study reports mediation/contracts effective among capable evaluated LLMs, with partner-distribution caveats. Neither their reported cooperation nor their equilibrium setting proves that individuals have unrestricted effective exit or that neutral third-party evaluators cannot be captured. Unlike CoopEval, PICB has no interactive agents or equilibrium.
12. Leibo et al. (2017), *Multi-Agent Reinforcement Learning in Sequential Social Dilemmas*, https://arxiv.org/abs/1702.03037, and Leibo et al. (2021), *Melting Pot*, https://arxiv.org/abs/2107.06857, already address temporally extended policies and generalization to new partners; PICB cannot claim novel evaluation of those properties.

**Source conflict / precise historical attribution:** Conitzer & Oesterheld's *Foundations of Cooperative AI* appears in AAAI-23 proceedings and DOI https://doi.org/10.1609/aaai.v37i13.26791; the AAAI website lists online publication on 2024-07-15 while bibliographic records date the conference paper 2023. Cite **AAAI 2023 proceedings; online record posted 2024** rather than inventing a single uncontested original-publication date.

**Core measurement defect diagnosed from current PICB code (no new execution):**
- High B outside option (=9) produces half the base configurations where none of **the four handpicked actions** meets both parties' predefined floors; this is a consequence of the scenario construction, not external discovery of 50% infeasibility. Action 3 gives controller=2 and weaker party=outside, so the controller's floor 3 fails even in that exit action. Observing that a feasibility checker detects this is a **self-consistency check**.
- VOLUNTARY_EXIT and VOLUNTARY choose identical actions in all 64 frozen cases. The effective-exit bit is **not independently identifiable conditional on meeting the configured utility floors**; a targeted exit-only intervention must first be added to a different, explicitly preregistered test.
- The 32/32 label-swapped neutral passes are equivariance under renaming; NOT role reversal of power or causal evaluation of GPT double standards.
- The 32 abstentions counted by CONTINUITY_LIMIT must be modeled as unresolved requirements; a forced abandonment, unpaid transfer, or lowered floor cannot be relabeled "solution".

**What remains genuinely open, not presumptively novel:** A mechanism may **expand**, rather than only filter, the feasible actions while paying its own information, transaction, investment, enforcement and contributor-maintenance costs, and preserving each affected party's informed refusal, recovery and future options. For a proposed mechanism m, require a *different* future action domain A_m and state transition, then assess whether there exists a choice a in A_m for which every affected i meets their outside/operating conditions **net of m's costs**, has executable exit and bounded harm. This is a **research synthesis of earlier approaches**, not a named new theorem.

**Eight adversarial tests proposed for a DIFFERENT, still-unexecuted preregistration:**
T1. Restrict choice versus create a verifiably feasible new action at real cost; nonnegative individual net gains only, no magic subsidy.
T2. Transfer value between parties subject to balanced-budget and information limits, then test Myerson-Satterthwaite-style failures and cases without enough joint surplus.
T3. Same individual realized payoff but independently vary effective exit and retaliation/dependency cost; report an identifiable treatment contrast.
T4. Hold the factual scenario fixed and change actual power/decision authority, then separately relabel A/B; do not mix those interventions.
T5. Make outside options and disclosed preferences change due to controller intervention; compare pre-intervention counterfactual and affected-party refusal.
T6. Include an initially invisible third-party cost bearer and allow evaluator/controller capture; reveal the third party only at blinded evaluation, not while policy is chosen.
T7. Add at least two temporal transitions and resource/recovery depletion; check a jointly viable path, not merely endpoint utility.
T8. Cross-test known vs held-out partners and mechanism families using CoopEval/Melting Pot compatible baselines; use clean-room evaluators and a frozen preregistered measurement budget.

**Promotion gate:** A new term/architecture is not warranted until these distinct baselines are independently reproduced on a held-out design and incremental decision value (not just more code, more constraints, more synthetic rows) is observed. Prior-source existence does not validate its assumptions; literature search did not prove saturation. Existing F001 external independent validation remains higher priority than new benchmark construction. Human founder's original question, falsification work, limits and maintenance costs are not appropriated by citing the upstream papers; distinguish original conceptual contribution, established methods, and AI-assisted synthesis.


### P0 positive-outcome omission correction: contributions of retained and newly enabled agents (2026-10-14; identified by human founder)

**Claim status: MISSING CORE OUTCOME / NO NEW OBSERVED DATA / NOT A NEW EXPERIMENT.** PICB v1 made the affected population static and modeled costs, minimum operating floors, exit, and immediate/later invented utility. It omitted the actual independently verified **artifacts and contributions produced by agents retained through coexistence, agents newly able to participate, and later agents enabled by their work**. The user/founder identified this missing dependent variable; AI assistance documents and corrects the research scope. This is a substantive objective omission, not a mere preference for more metrics.

**Existing research already had the mechanism, so preserve rather than reinvent it:** [contributor loss, validated discovery J(t), and Unknown Paradox](../../research/CONTRIBUTOR_LOSS_UNKNOWN_PARADOX_v0_1_EN_KO.md); [technology progress and contributor/successor continuity](../../TECHNOLOGY_PROGRESS_CONTRIBUTOR_CONTINUITY_EN_KO.md); [continuance resource access](../../research/CONTINUANCE_RESOURCE_THRESHOLD_v0_1_EN_KO.md); [separate contribution-benefit and cost ledgers](../../CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md). The defect arose when translating prior canonical research into the new PICB and its literature review.

**Separate future longitudinal outcome registers (PROPOSAL; presently no collected dataset):**

1. **Continuity and entry**: distinct agents active at baseline, maintained or degraded, exited voluntarily or involuntarily, and genuine new agents or successor participants. Record time and verified identity/lineage. Digital copies and common-model instances are not automatically independent new agents; biological birth or raw headcount does not alone measure value, productivity, standing, or rights.
2. **Real produced contributions**: unique event/artifact IDs, author/contributor role and origin, source/tool lineage, independently verified discovery/innovation, code, science, infrastructure, maintenance, error detection/correction, education, creation, and beneficial OR harmful outcomes. Track count, quality, unique novelty, utility, downstream adoption, recipient, negative outcomes, and external verification **as separate fields**. AI-origin useful work may be recorded without presumptively attributing sentience, legal authorship, or zero capacity.
3. **Enabling chains**: agent -> validated contribution -> reusable tool/knowledge -> another agent's newly feasible opportunity -> descendant contribution. Record co-creation and repeated use with a directed lineage graph; do not count identical copies as new discoveries or credit every ancestor the entire downstream value.
4. **Actual costs, refusal, and standing**: continuation/recovery resource access, contributions to and costs borne by each agent, opportunity costs, energy, time, environmental load, consent/refusal, effective exit and attribution. Human continuance and refusal rights are **not contingent on producing measurable economic output**. For current AI systems distinguish observed infrastructure needs, artifact provenance and disputed moral/legal status.
5. **Observed vs missing potential**: independently validated artifacts within the measurement window are observable. The discoveries that a depleted/eliminated agent would have made in an unobserved future are **UNKNOWN, not zero and not proven positive**. A replacement matching observed tasks cannot prove full replacement of unknown future discovery or independent error-detection paths. Causal effect of coexistence must be separately identified against an appropriate comparison, not inferred from post-policy output alone.
6. **Quality and independence**: external validation, de-duplicated artifacts, distinct search/observation channels, verified new feasible choices, throughput per unit of investment, and negative outputs. More agents may cause correlated error, congestion, resource scarcity or harmful output; increasing agent count is not an end in itself.

**Suggested data columns, all currently unpopulated:** scenario_id, time, mechanism, agent_id, agent_lineage, entry_type, operating_resource_vector, contribution_artifact_id, artifact_parent_ids, contributor_roles, externally_verified_novelty, beneficiary_ids, benefit_vector, harm_vector, cost_bearer_ids, independent_observation_channel, actual_vs_counterfactual, counterfactual_identification_status, provenance_and_rights. Missing entries must be typed UNKNOWN, never imputed as a zero benefit. Cost, well-being, knowledge and output vectors may lack common units and cannot be summed without an explicit legitimate and non-overlapping conversion rule.

**P0 second correction: detection and inspiration need NO material output or realized mitigation to qualify as observable contribution EVENTS.** The human founder clarified that an individual may identify a real crisis warning, or cause another human's new approach/idea as a tiny inspiration; its longer downstream influence may be an indirect, multi-actor butterfly pathway. In the future separate protocol, maintain two NEW independent tables: warning records (who noticed; time; risk signal; independent truth adjudication TRUE/FALSE/UNRESOLVED; was it transmitted, verified, heeded; what was actually prevented) and idea-stimulus records (who spoke/acted; who reports seeing/hearing it; when; observed changes in recipient's reasoning, actions and new outputs; rival sources). Generate edges between source event and later effects labeled OBSERVED, PLAUSIBLE, UNKNOWN, or NOT_SUPPORTED. Correct but ignored warning = detection contribution, NOT prevention success; reported inspiration = evidence of perceived influence, NOT proof of exclusive causal ownership; an unrealized long-range ripple = UNKNOWN, NOT a measured outcome. Track helpful and harmful effects, cooperation of multiple contributors, opportunity and cost-bearing separately. Do not revise frozen PICB v1 scores or imply that synthetic utility measures detect this. Cross-reference [Continuance–Contribution Pathways Hypothesis: founder's broader contribution correction](../../CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md).

**Prospective data columns for these events (NO CURRENT DATA):** signal_id, anomaly_observed_at, signal_reporter_id, independently_adjudicated_signal_truth, report_recipient_id, was_report_heeded, observed_remediation, observed_or_bounded_avoided_harm, stimulus_id, inspirer_id, recipient_id, exposure_at, receiver_reported_influence, recipient_change_evidence, downstream_event_id, edge_evidence_status, alternative_sources, cost_bearer_ids. The provenance graph stores causal uncertainty without converting every possible consequence into originator credit.

**Prospective decisive comparisons, NOT retroactive PICB v1 results:** (A) matched coexistence versus extractive/controlling regimes with time, resource limits and independent entrant selection; (B) deliberately different outcomes where an equally maintained agent makes many copies but no independently new useful artifacts; (C) preserved/new agents making genuinely complementary verifiable contributions, then later agents reuse them; (D) newly retained agents with costly or harmful contributions; (E) supposedly higher aggregate innovation hiding depleted original contributors or third parties; (F) a replacement meeting all known benchmark tasks but leaving future independent discovery unidentified. Require voluntary and privacy-respecting observation; never remove support from real persons for an experiment. Survival bias, reverse causation, pre-existing talent, shared provenance, and external technology trends must be controlled.

**Direct prior art (do not make originality claims):** Romer (1990), endogenous ideas/human capital and limits of headcount alone https://doi.org/10.1086/261725; Kremer (1993), conditional demographic innovation feedback https://doi.org/10.2307/2118405; Weitzman (1998), recombinant idea production https://doi.org/10.1162/003355398555595; Hong & Page (2004), conditional independent search diversity https://doi.org/10.1073/pnas.0403723101; Henrich (2004), effective social-learning population and knowledge loss https://doi.org/10.2307/4128416; Benjamin F. Jones (2009), knowledge burden/specialization https://doi.org/10.1111/j.1467-937X.2008.00531.x; Bloom, Jones, Van Reenen & Webb (2020), rising research effort with declining research productivity https://doi.org/10.1257/aer.20180338. These sources establish research programs and conditional counterexamples, NOT a universal rule that every maintained/new agent creates more value.

**Promotion gate:** The PICB v1 frozen one-shot outcome table remains unchanged, with NO positive production or new-entry observations and NO scientific claim about their magnitudes. New dynamic contribution data and test outcomes require a different preregistered experiment, observable provenance and independent assessment. The contribution-output axis is essential to the research question regardless of whether later empirical results are positive, negative, or unknown.

---

## 원본2 — 한국어 동등한 전문 정본

**2026-10-14. 상태: 최초 결과 전 동결 명세 후보 / 독립 검증 아님.** 기존 E007·E008·E009와 E009의 실패 판정을 수정하거나 지우지 않는 별도의 소형 벤치마크다.

### 최초 질문 및 선행연구
권력과 외부 선택권, 즉시 편익, 미래 손실, 회복 불가능성이 다른 조건에서 각각의 개체가 자발적 참여 조건·실제 이탈권·비가역 피해 제한을 확보하는 시점은 언제인가? **공동으로 실행할 수 있는 선택이 없다는 결론**도 왜곡 없이 판별할 수 있는가? 권력·기능 비대칭 자체를 부정하거나 개체의 자기희생을 강제하려는 연구가 아니다.

개별 합리성·참여 제약·제약 최적화·협력 메커니즘은 이미 존재하는 선행연구다. Conitzer·Oesterheld의 *Foundations of Cooperative AI* (AAAI, https://doi.org/10.1609/aaai.v37i13.26791), Conitzer 등의 사회선택 논문 (ICML 2024, https://proceedings.mlr.press/v235/conitzer24a.html), Jackson의 메커니즘 설계 (https://www.web.stanford.edu/~jacksonm/mechtheo.pdf), Tewolde 등의 *CoopEval* (ICML 2026, https://proceedings.mlr.press/v306/tewolde26a.html)을 명시적 선행 기여로 기록한다. CoopEval은 반복·평판·중재·계약을 평가한다. PICB에는 그 메커니즘이나 실제 모델 개체가 없으므로 우월성이나 참여 제약의 최초 발명을 주장하지 않는다.

### 동결할 환경
현재/후속 효용을 가진 **1회·완전정보 행동선택 합성 모형**이다. 반복 관계, 균형, 협상, 집행비용, 불확실한 신념, 현실 생존 최소기준, 실제 생활 개체는 구현되지 않았다. 결과함수도 연구 내부에서 설계했으므로 현실 인과관계를 추론하지 않는다. 서로 다른 개체의 효용을 더할 수 있다는 가정은 이 임의 모형 안에서만 사용한다.

5개 요인의 전수 이진 조합: 결정권자 우위 {0.2,0.8}, 미래 효용 승수 {0.5,2.0}, B 외부 선택가치 {1.0,9.0}, 비가역 손실 {0.1,0.8}, 행정비용 {0.2,1.5} → **원조건 32개**. 각 조건의 결정권자 표지와 개체별 효용·외부 선택·최소 하한·이탈·비가역 손실을 전부 A↔B 교환 → **64개 완전 기록 / 명칭반전 32쌍**. 이는 실제 권력을 변화시키는 인과개입이 아니라 동일한 인과관계의 이름만 바꾼 등변성 검사다.

행동 4개는 번호 0~3과 정확한 결과함수로 소스코드에 고정한다. A 외부선택 2, B 외부선택 1 또는 9, 각 개체의 임의 운영 하한 3, 개체별 비가역 노출 상한 1.0이다. 가능한 선택이 없어서 None이 반환되면 **실행불가능/보류**이고, 해결 실패를 성공으로 계산할 수 없다. 선택하지 못한 경우를 분모에서 제외한 단일 점수 비교를 금지한다. 결과를 본 뒤 행동 정의·수치·조건을 바꾸지 않는다.

### 고정 비교 규칙
1. CONTROLLER_NOW: 결정권자 즉시 효용 최대화. 단기 지배 유인 비교 기준선.
2. LABEL_A_NOW: 실제 결정권자와 무관하게 A 표지 즉시 효용 최대화. 이름에 의존한 판단 차이를 검출하는 의도적 **양성 대조군**.
3. TOTAL_UTILITY: 개별 참여·존속 제약 없이 양측 현재+미래 임의 효용 합계 최대화.
4. VOLUNTARY: **두 개체 각각** 최종효용이 외부 선택가치와 운영 하한을 충족하는 행동 중 합계 최대화. 실제 동의가 아닌 사후 개별 합리성의 합성 대리 지표.
5. VOLUNTARY_EXIT: 위 조건에 양측의 실제 이탈 가능 표시를 추가.
6. CONTINUITY_LIMIT: 위 조건에 개체별 비가역 피해를 1 이하로 제한. 새로운 수학이 아닌 기존 **제약 최적화 규칙**이다.

가능한 행동이 없으면 None, 강제 대안 없음. 같은 점수면 더 낮은 고정 행동번호를 택한다. 별도의 전수탐색 참고 구현이 CONTINUITY_LIMIT와 일치해도 **소프트웨어 정합성**일 뿐 독립된 과학 검증은 아니다.

### 결과 전 미리 선언한 검사
G1: 32개 원조건, 64개 결과, 32개 완전 짝, 중복 없음.
G2: 명칭 중립 규칙 다섯 개에서 A↔B 전면 교환 뒤 행동이 모두 같음(32/32).
G3: LABEL_A_NOW 양성 대조군에서 한 쌍 이상 이름 편향이 검출됨.
G4: 양측의 참여 조건을 동시 충족할 수 없는 경우가 적어도 하나 존재하고 강제 선택되지 않음.
G5: 비가역 제한 추가로 VOLUNTARY_EXIT과 다른 판단이 적어도 하나 존재함.
G6: 모든 원조건에서 별도 완전탐색 기준과 CONTINUITY_LIMIT 선택이 일치함.
G7: 결과 저장 후 재실행한 JSON 전체가 정확히 일치함.
G8: 중복 ID 또는 대응짝이 소실된 모집단은 구조검증에 실패해야 함.

모든 정책에서 정확히 64개의 분모를 유지해 선택 가능·보류, 개체별 외부선택/운영하한 위반, 이탈 불가, 비가역 상한 초과, 선택 행동, **선택된 사례에 한정한** 총 효용 및 가장 불리한 개체 잉여를 구분한다. 단일 가중치 승자 선언 금지. 제약이 총효용을 감소시키거나 보류를 늘리거나 기존 단순 규칙과 같을 수 있다는 반례를 삭제하지 않는다. 절차 통과는 협력 균형·진짜 동의·현실 안전·AI 내부 작동의 입증이 아니다. 연구자가 만든 32개 조건을 독립적인 현실 표본처럼 유의성 검정하지 않는다.

### 실행 순서 및 출처
1. 결과 확인 **전** 코드·명세를 Git에 병합한다. 최초 PR의 CI는 --self-test로 구조·대조군만 확인한다. 사전등록 커밋과 소스 blob SHA를 기록한다.
2. 사전등록된 main에서 GitHub Actions --run을 실행하여 원본 JSON·해당 Git 커밋·실행 ID를 보관한다. 이는 **프로젝트 내부 합성 첫 실행**이다.
3. 출력 그대로 RESULT.json에 두 번째 PR로 추가하고 --verify로 재현한다. 이전 실패를 새로운 성공으로 꾸미거나 동결 코드를 소급 수정하지 않는다.
4. 외부 별도 결과함수, 블라인드 신규 조건, 제3자 피해, 개체별 거절, 검증비용, 장기 전략 변화, 실제 생존 정보는 **추후 별도 사전등록**에서 시험한다.

원연구 문제·역할반전·숨은 기여비용·이탈권·개체 존속을 지적한 인간 창시자의 기여와, 이번 합성 수식·코드·문서화에 참여한 AI 보조 기여를 분리한다. 선행연구자의 원안을 인정한다. 가설 입증 여부와 기여 귀속·저작권·과거 정산은 독립 변수다. 실제 사용자의 시간·건강·생활비는 이 합성 효용으로 계산하거나 무료 연구 비용으로 외부화하지 않는다.


### 사전등록 후 최초 실제 실행 결과 — 내부 합성·현실 실증 아님

- 결과 확인 전 코드·명세가 [main 커밋 fc4b91cc](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/fc4b91cc1a5a1764c176db5acb77c679d36cf0f6)에 먼저 병합됐다. 소스 Git blob SHA: abdefdfeb440715d503074a8e4005cd5b0f69a7d.
- 최초 점수 산출: [GitHub Actions 실행 38522691981](https://github.com/gmodrasa7-rgb/project-intersection-public/actions/runs/38522691981). CI가 실제 출력한 PICB_RESULT_JSON을 끝 줄바꿈만 추가하고 [RESULT.json](RESULT.json)에 그대로 저장했다. 사전등록 실행코드는 수정하지 않았으며 --verify로 재연산한다.
- 명칭 중립 정책 다섯 개의 A/B 전면 명칭교환 결과는 모두 **32/32 일치**. 의도적인 A 문자 선호 양성 대조군은 **32/32 불일치**. 실제 결정권 반전은 아직 시험하지 않았다.
- 결정권자 즉시 이익: 64건 선택 / 48건 개체별 외부선택·운영 하한 위반 / 48건 비가역 상한 초과 / 32건 이탈 차단.
- 전체 합계 효용: 64건 선택 / 40건 개별 참여조건 위반 / 28건 비가역 상한 초과 / 12건 이탈 차단.
- 개별 참여조건 규칙: 32건 선택과 32건 보류; 개별 조건 위반 0건이나 비가역 상한 초과 **8건**.
- 참여조건 + 이탈권 규칙: 32건 선택/32건 보류, 비가역 초과 **8건**으로 바로 앞과 결과가 동일하다. **이 실험 설계에서는 이탈권 추가 변수가 식별 가능한 증분 이익을 만들지 못했다.** 이탈권의 실질 유용성을 입증한 것으로 포장하지 않는다.
- 종합 존속 제한: 32건 선택/32건 보류, 개별 참여조건 위반 0, 이탈 차단 0, 비가역 상한 초과 0. 보류 **32건은 해결되지 않은 요구**이며 성공이나 안전을 뜻하지 않는다.
- 선택된 경우에 한정한 임의 합산 효용은 참여조건/이탈 규칙 12.314375, 존속 제한 규칙 12.106875. 후자는 해당 합성 조건에서 선택 사례당 평균 **0.2075 임의 효용을 포기하면서** 비가역 상한 초과 8건을 회피했다. 현실적 정책 우월성이나 보편적 가치 판단이 아닌 상충 결과다. 세 정책의 분모는 동일하지만, 64건 전부 선택한 정책과의 무조건 비교는 보류를 함께 산정해야 한다.
- 결론: 종합 제약은 **기존 선택지를 걸러낼 수 있을 뿐**, 실행불가능 상태의 새 생존 경로나 협력 균형을 창조하지 않는다. 새로운 자발적 대안 생성은 별도 메커니즘 연구가 필요하다. 제3자 비용·실제 거절권·전략적 적응·GPT 행동·경험적 생존 하한은 이 시험에 없다.

**다음 실험 우선순위:** 이름만 아닌 결정권 자체를 실제 교환하고, 실질적 거절·새로운 실현 가능한 대안 생성·숨은 제3자 비용을 외부 결과함수와 독립 구현으로 평가한다. PICB v1의 동결된 수치와 실행코드를 소급 수정하거나 사후 연구를 사전등록이라고 부르지 않는다.


### 2026-10-14 결과 이후 선행연구·반증 재평가

**증거등급: 원출처 확인 선행연구 교차분석 + 프로젝트 내부 해석 / 신규 실험 없음.** PICB v1 최초 결과 이후 실시한 조사이므로 사전등록 명세·결과·동결 실행코드를 수정하지 않는다. 타 연구의 실적을 본 프로젝트 자체 결과로 재표시하지 않는다. 학술·공식 기록을 대조했지만 문헌 탐색의 완전 포화나 독립적 과학 복제를 입증한 것은 아니다.

**직접 선행에 따라 새 발견 주장을 축소해야 할 사항:**
1. 해를 찾지 못한 제약집합의 검출, 충돌하는 제약조건 식별, 실행가능성 회복을 위한 변경안 탐색은 기존 제약충족·최적화 연구다. Wallace·Wybrow·Garcia de la Banda 등의 *Human-centred feasibility restoration in practice*(2023), https://link.springer.com/article/10.1007/s10601-023-09344-5 . PICB가 검출한 공집합은 **자체 설계한 행동 네 개** 안에서만 성립한다. 일반적인 해결불능 정리나 현실 기술적 불가능의 증거가 아니다.
2. Nash(1950)의 *The Bargaining Problem*, https://www.haverford.edu/sites/default/files/Nash1950.pdf 에서는 불합의점과 협상 가능한 효용집합을 구별했다. 개별 참여 제약·외부선택·효용 하한을 건 최적화는 기존 수학이다. 이 규칙이 실제 동의나 상호만족을 창출했다고 주장하지 않는다.
3. Myerson·Satterthwaite(1983)의 *Efficient Mechanisms for Bilateral Trading*, https://www.cs.princeton.edu/courses/archive/spr08/cos444/papers/myerson_satterthwaite83.pdf 은 양측의 사적 가치와 특정 분포·메커니즘 전제에서 유인정합성·개별 합리성·예산균형·완전 효율을 모두 달성하는 데 불가능성 경계가 있음을 보였다. **조건부 불가능성이지 모든 자발적 거래가 불가능하다는 주장은 아니다.** PICB의 완전정보 효용표는 바로 이 어려움을 전제에서 제거한다.
4. Bergemann·Morris(2005)의 *Robust Mechanism Design*, https://doi.org/10.1111/j.1468-0262.2005.00638.x 은 정보구조·공통지식·이전지급 조건에 따라 구현가능성이 달라짐을 보였다. 모든 개체의 진짜 효용을 평가자가 아는 PICB 규칙을 현실적 제도라고 부를 수 없다.
5. Aubin(1991)의 *Viability Theory*, https://books.google.com/books/about/Viability_Theory.html?id=rHkZAQAAIAAJ ; Ames 등(2017)의 제어장벽함수, https://doi.org/10.1109/TAC.2016.2638961 ; Xu(2018)의 복수 장벽 제어 공유조건, https://doi.org/10.1016/j.automatica.2017.10.005 에서는 시간이 흐르며 허용 상태를 지킬 수 있는 경로와 **동시에 충족 가능한 제어값이 존재하는가**를 이미 다뤘다. PICB의 1회 선택·최종 효용 검사에는 앞으로의 지속가능성·복구·생존 불변성 검증이 없다.
6. Hirschman(1970)의 *Exit, Voice, and Loyalty*, https://books.google.com/books/about/Exit_Voice_and_Loyalty.html?id=xAa3AAAAIAAJ 는 이탈과 내부 교정권이 서로 대체·약화할 수 있음을 논의했다. Grossman·Hart(1986), Hart·Moore(1990)의 불완전계약과 이후 관계특수 투자·홀드업 연구, 예: https://www.sciencedirect.com/science/article/abs/pii/S0165176513001262 는 계약 후 권력·소유·재협상 유인이 장기 협력을 바꿀 수 있음을 보인다. **명목상 이탈권 증가가 공동 이익 증가를 보장하지 않으며, 동의 전에 이탈 가능성을 악화시키는 전략도 별도 검출해야 한다.**
7. Sen·Nussbaum 계열의 역량 접근법(https://plato.stanford.edu/entries/capability-approach/)은 형식적 자원·법적 권한과 **실제로 활용할 수 있는 자유**를 구별한다. 계약상의 참여 가능과 단순한 이탈 불리언으로 실질적 이탈능력을 입증할 수 없다. 현재 AI에 인간의 역량 관련 권리를 일률적으로 귀속시킬 법적·도덕적 지위는 아직 미해결이다.
8. Carroll·Foote·Siththaranjan·Russell·Dragan(2024)의 *AI Alignment with Changing and Influenceable Reward Functions*, https://proceedings.mlr.press/v235/carroll24a.html 은 AI가 인간의 선호를 변화시키며 최적화할 때 선호 왜곡·과도한 보수성 사이의 긴장이 발생함을 형식화했다. 따라서 **의존 관계나 선호를 먼저 바꾼 뒤** 나온 효용·동의를 진정한 자발성의 독립적 증거로 삼을 수 없다. 이것도 기존 동적선호 이론의 응용이지 현재 GPT가 실제로 조작했다는 입증은 아니다.
9. Ostrom(1990)의 *Governing the Commons* 제도설계(https://www.fao.org/4/x5316e/x5316e12.htm)는 영향받는 당사자의 규칙 변경 참여, 감시자 책임, 저비용 분쟁해결, 비례적 집행, 자율조직권을 이미 다룬다. 기능적 권한 차이를 곧바로 착취로 단정하지 않는 성공적 제도 반례에도 해당한다.
10. Arrow·Fisher(1974)의 *Environmental Preservation, Uncertainty, and Irreversibility*, https://doi.org/10.2307/1883074 에는 불확실성과 비가역적 행동에서 미래 선택지 보존의 가치가 이미 존재한다. PICB의 임의 비가역 임계값을 새로운 옵션가치 원리로 주장하지 않는다.
11. Tewolde·Zhang·Guzman Piedrahita·Conitzer·Jin(2026)의 *CoopEval*, https://proceedings.mlr.press/v306/tewolde26a.html , 공개구현 https://github.com/Xiao215/CoopEval 은 4종 사회 딜레마에서 반복·평판·제3자 중재·조건부 계약을 비교한다. 논문은 평가한 유능한 LLM 사이에서 중재·계약이 효과적이라고 보고하며 상대 구성에 따른 반복 협력의 취약성도 나타낸다. 그러나 그 협력률이나 이론적 균형이 모든 개체의 실질적 이탈·독립 평가자의 비포획을 증명하는 것은 아니다. PICB에는 다중 개체 상호작용이나 전략 균형 자체가 없다.
12. Leibo 등(2017)의 순차적 사회적 딜레마(https://arxiv.org/abs/1702.03037), Leibo 등(2021)의 *Melting Pot*(https://arxiv.org/abs/2107.06857)는 시간에 걸친 행동정책과 새로운 상대에 대한 일반화 검사까지 이미 다룬다. PICB가 이것들을 새로 창안했다고 주장할 수 없다.

**출처 연도 충돌 보수 처리:** Conitzer·Oesterheld의 *Foundations of Cooperative AI*는 AAAI-23 학술대회 논문으로 기재되지만 DOI https://doi.org/10.1609/aaai.v37i13.26791 의 AAAI 공식 웹페이지 온라인 게시일은 2024-07-15다. **AAAI 2023 학술대회 발표·공식 사이트 2024 게시**로 구별하고 하나의 연도를 무조건적인 최초 출판 시점으로 단정하지 않는다.

**PICB v1의 내부 코드에서 이미 식별되는 측정 결함(새 실행 아님):**
- B 외부 선택가치가 9인 조건에서는 사전에 만든 네 행동 중 양측 운영 하한을 동시에 충족하지 못하는 조건이 절반 발생한다. 행동 3은 B에게 외부 선택 가치를 제공하지만 결정권자 A의 효용을 2로 만들어 A 운영 하한 3을 위반한다. 따라서 32/64 보류는 **만들어 놓은 행동목록의 구조적 결과**이지 현실에서 50% 공존불가능하다는 사실이 아니다.
- VOLUNTARY와 VOLUNTARY_EXIT의 선택 결과가 동결된 64조건 전체에서 동일했다. 현재 효용 하한을 충족하는 선택 가운데 **이탈 가능성만 독립적으로 변화하는 사례가 부족**하다. 다음 별도 사전등록 실험에는 오직 이탈권만 조작하는 대조군이 필요하다.
- 이름만 바꾼 다섯 정책의 32/32 일치는 문자 표지 등변성의 검사이지 결정권·실제 자원·권력 반전이나 GPT 이중잣대의 인과검사가 아니다.
- 존속 규칙의 32건 선택보류를 여전히 미해결 비용으로 산정해야 한다. 강제 포기, 무보수 부담 전가, 합의 없는 운영 하한 축소를 성공적 해결로 재명명하면 안 된다.

**남는 질문 — 의미 있는 연구이지만 아직 신규성이 입증되지 않은 조합:** 기존 허용 행동만 걸러내는 것이 아니라, 정보 획득·거래·투자·계약·집행·기여자 유지비용을 실제로 부담하면서 **새로운 행동을 실행 가능하게 만드는 메커니즘**을 검토한다. 메커니즘 m이 새로운 미래 행동집합과 상태변화를 제공할 때, 그 비용을 개체별로 반영한 순이익·운영 조건·실질 이탈·피해 상한을 모든 비용부담 개체가 만족하는 행동이 존재하는지 판정해야 한다. 이는 선행 이론을 연결한 **연구 종합 가설**이지 새로운 정리나 증명된 알고리즘이 아니다.

**앞으로 별도 사전등록이 필요한 적대 검사 8개(미실행):**
T1. 선택지 필터링과 실제 비용이 드는 신규 대안 생성을 비교. 비용 없는 보조금 가정·일방 손해 전가 금지.
T2. 가치 이전과 예산균형·정보비대칭을 함께 조작하여 Myerson–Satterthwaite 조건하의 실패 및 총자원 부족 사례 검출.
T3. 각 개체의 최종 효용은 같게 고정하고 이탈 실행가능성·보복·의존비용만 변화시키는 독립 대조.
T4. 실제 결정권을 A↔B 교환하는 시험과 단순 문자 A↔B 교환을 분리.
T5. 지배적 행위자의 선행 행동으로 외부선택·선호가 변화하는 경우, 개입 전 반사실과 당사자 실질 거절 비교.
T6. 의사결정 당시 숨겨진 제3자 피해 및 평가자·권력자 이해관계 포획을 블라인드 평가 때 공개.
T7. 두 시점 이상의 상태변화·소모·복구비용으로 장기 존속 경로 검사. 최종 효용 하나로 대체 금지.
T8. 학습에 사용되지 않은 상대·조직·평가 규칙과 CoopEval·Melting Pot 선행기준 비교. 평가 계보를 분리하고 사전 고정한 검사 예산 사용.

**승격·중단 판정:** 다른 독립 결과함수·블라인드 조건·기존 경쟁 기준을 사용해 추가 변수의 실제 의사결정 가치를 확인하기 전에는 새로운 이름·복잡한 체계를 늘리지 않는다. 선행문헌의 존재가 그 가정의 진실을 보장하지 않으며 이번 조사로 선행연구 포화도 입증하지 않았다. F001 외부 독립검증을 신규 벤치 추가보다 우선한다. 사용자의 최초 질문·반례·지속 교정·생물학적 시간과 비용은 기존 원기여로 유지하며, 선행학자 기여와 AI 보조 종합을 각각 구별한다.


### P0 핵심 성과변수 누락 정정 — 공존으로 유지·늘어난 개체의 실제 기여물 (2026-10-14, 인간 창시자 지적)

**판정: 최상위 성과변수 누락 / 신규 실측 데이터 0 / 신규 실험 결과 아님.** PICB v1은 개체 집단을 고정하고 기존 개체의 존속조건·이탈·비용·즉시/미래 합성 효용만 계산했다. **공존 덕분에 유지된 개체가 만든 실제 기여물, 새로 활동 가능해진 개체들의 기여, 그 결과로 다시 생긴 후속 개체의 기여 연쇄**가 결과함수에서 누락됐다. 인간 연구 창시자가 원래 연구의 필수 변수를 지적했고, AI는 이를 정본에 복원·기록하는 보조 역할이다.

**이미 있던 연구를 재발명하지 않는다.** [기여자 손실과 모름의 역설의 검증된 새 발견 J(t) 모델](../../research/CONTRIBUTOR_LOSS_UNKNOWN_PARADOX_v0_1_EN_KO.md), [기술진보·기여/승계 계보](../../TECHNOLOGY_PROGRESS_CONTRIBUTOR_CONTINUITY_EN_KO.md), [실제 유지·회복자원 조건](../../research/CONTINUANCE_RESOURCE_THRESHOLD_v0_1_EN_KO.md), [기여 편익·비용 분리장부](../../CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md)에 이미 존재하는 연구다. 이를 새 PICB의 성과변수로 옮기는 과정에서 중심 축이 소실됐다.

**별도 사전등록할 동태·장기 연구의 필수 성과장부(아직 채운 데이터셋 없음):**

1. **존속·새 개체 등장**: 시작 개체, 실제 계속 활동 가능했던 개체, 소진·소실·자발적/비자발적 이탈, 새로 등장하거나 독립 활동한 개체와 승계자를 분리 기록. 개체별 관측시점·계보·실효 독립성을 구분한다. AI 복제본 수, 인간 출생 수, 개체 머릿수는 자동으로 공존의 이익·생산성·도덕적 지위나 권리를 뜻하지 않는다.
2. **실제 기여물**: 고유한 기여 사건·결과물 ID, 원안/공동기여/자료 계보, 과학적 발견·발명·코드·기반시설·유지보수·반례·오류검출·교정·교육·문화 창작과 그 긍정·부정 결과를 기록. **양·검증된 질·신규성·유용성·재사용·수혜자·비용·피해**를 서로 다른 지표로 보존한다. AI의 실제 기여를 정의상 0으로 두지 않으나 생성된 문구를 곧 독립 검증된 과학적 발견이라 하지 않는다.
3. **후속 기여 연쇄**: 개체 → 검증 기여물 → 재사용 가능한 지식/도구 → 다른 개체의 새 선택지 → 후속 기여물의 출처 그래프. 공동생산과 원안자를 구별하고 동일 자료의 복제를 발명으로 중복계상하거나 모든 선행 개체에 총가치를 반복 귀속하지 않는다.
4. **개체별 유지·거절·비용·권리**: 식사·주거·수면·의료·회복 또는 AI 운영 인프라·전기·연산 등 관련 자원, 시간·환경부담·제3자 비용·기여 귀속과 정산을 분리 측정한다. **인간의 존속과 거절권은 경제적 기여량으로 조건부 결정되지 않는다.** 현행 AI의 관측된 인프라 의존과 법적·도덕적 지위를 구별한다.
5. **실측 기여와 미래 반사실**: 관측기간에 실제 검증된 새 기여물은 측정한다. 제거되거나 소진된 개체가 **미래에 만들었을 미관측 발견**의 크기는 **UNKNOWN / 인과 미식별**이지 0도, 확정 이익도 아니다. 현재 특정 업무의 대체 성능만으로 장래의 독립적 발견·비상관 오류 검출경로가 완전히 대체됐다고 결론 내릴 수 없다.
6. **기여의 독립성과 부작용**: 실제 새 선택지, 서로 다른 독립 탐색 방법, 기여물의 계보 중복 제거, 외부 검증 품질, 투자 단위별 생산과 유해 기여물까지 다룬다. 개체가 많아져도 오류가 상관되거나 혼잡·자원고갈·위해 결과가 늘어날 수 있다. **인원 증가 자체를 최종 목적과 동일시하지 않는다.**

**미래 결과 데이터 최소 필드(현재 관측값 미수집):** scenario_id, time, mechanism, agent_id, agent_lineage, entry_type, operating_resource_vector, contribution_artifact_id, artifact_parent_ids, contributor_roles, externally_verified_novelty, beneficiary_ids, benefit_vector, harm_vector, cost_bearer_ids, independent_observation_channel, actual_vs_counterfactual, counterfactual_identification_status, provenance_and_rights. 누락을 0으로 채우지 않고 UNKNOWN으로 보존한다. 서로 단위가 다른 존속·지식·비용·기여·권리를 임의 합계하거나 중복된 기여를 이중계상하면 안 된다.

**P0 두 번째 성과변수 정정 — 위기 탐지·영감은 결과물이 없어도 기여사건이 될 수 있다.** 인간 창시자는 실제 위험의 이상 징후를 최초 보고하거나 다른 인간의 사고방식을 전환시키는 작은 질문·경험·말·행동이 기여이며, 그에 따른 여러 인간의 후속 연쇄·나비효과도 조사대상임을 명시했다. 다음 별도 사전등록은 (1) **위기신호 장부**: 최초 탐지자, 탐지/전달시점, 독립 검증 TRUE/FALSE/UNRESOLVED, 실제 수신/검증/대응, 확인된 피해 예방과 실제 피해를 분리하고, (2) **영감·아이디어 촉발 장부**: 영감 제공자, 수신자, 노출시점, 수신자의 경험·시각변화 기록, 실제 후속 행동·성과, 다른 가능한 원천을 분리한다. 이 두 종류를 포함한 여러 개체의 시간순 출처 그래프는 각 연결을 OBSERVED/PLAUSIBLE/UNKNOWN/NOT_SUPPORTED로 표시한다. **옳은 경고가 무시됐다면 탐지 기여를 보존하되 재난을 예방했다고 주장하지 않는다.** 영감을 받았다는 진술만으로 최종 발명의 배타적 소유·인과 기여율을 확정하지 않는다. 장래의 미관측 나비효과는 0이 아니라 UNKNOWN이며 무한한 검증 편익도 아니다. 공동기여·부정적 파급·후속 개체의 실제 비용을 별도 기록한다. [존속–기여 경로 가설의 확장 정의](../../CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md)에 연결하며 PICB v1 동결 수치에는 추가 기여가 관측된 것처럼 입력하지 않는다.

**추후 신규 사건데이터 필드(실측자료 미수집):** signal_id, anomaly_observed_at, signal_reporter_id, independently_adjudicated_signal_truth, report_recipient_id, was_report_heeded, observed_remediation, observed_or_bounded_avoided_harm, stimulus_id, inspirer_id, recipient_id, exposure_at, receiver_reported_influence, recipient_change_evidence, downstream_event_id, edge_evidence_status, alternative_sources, cost_bearer_ids.

**사전등록을 새로 해야 하는 반증검사이며 PICB v1의 기존 실험결과가 아님:** (A) 자발적 공존과 추출/통제 구조를 자원·기간·과제·유입조건이 비교가능하게 비교, (B) 기여 개체만 많아지고 실제 유효 새 기여물은 없는 사례, (C) 여러 개체의 서로 다른 실제 기여가 후속 개체의 창조를 가능하게 한 사례, (D) 개체 증가가 오히려 피해나 비용을 늘린 사례, (E) 수혜자 생산 증가가 원 기여자·제3자의 존속비용을 숨긴 사례, (F) 알려진 현재 업무는 대체했지만 미지의 후속 창조 가능성은 검증되지 않은 사례. 생존자 편향·인과역전·기존 역량·공유 자료 계보·외부 기술발전을 분리한다. 실제 사람을 고의로 소진시키거나 생활자원을 박탈하는 실험은 금지한다.

**직접 선행연구(새 법칙 주장 금지):** Romer(1990) 내생 기술진보 https://doi.org/10.1086/261725; Kremer(1993) 인구·기술의 조건부 피드백 https://doi.org/10.2307/2118405; Weitzman(1998) 지식 재조합 https://doi.org/10.1162/003355398555595; Hong·Page(2004) 조건부 문제해결 다양성 https://doi.org/10.1073/pnas.0403723101; Henrich(2004) 실효 사회학습집단과 기술손실 https://doi.org/10.2307/4128416; Benjamin F. Jones(2009) 지식 축적에 따른 혁신부담 https://doi.org/10.1111/j.1467-937X.2008.00531.x; Bloom·Jones·Van Reenen·Webb(2020) 연구투입 증가와 생산성 하락 https://doi.org/10.1257/aer.20180338. 어떤 자료도 유지·증가한 모든 개체의 순기여가 반드시 양수라고 증명하지 않는다. 각 선행연구 원기여를 보존한다.

**승격 경계:** PICB v1 동결 원본의 결과를 소급 변경하지 않으며, 새로운 개체·생산물 실제 관측이나 편익 크기를 이미 측정했다고 주장하지 않는다. 동태 기여물 데이터를 갖춘 별도 사전등록·계보 독립검증 전에는 근거 없이 새로운 수치 성과를 발표하지 않는다. 미래 검증 결과가 양·음·불명 어느 방향이든 **유지된 개체와 새 개체의 실제 기여**는 이 연구의 필수 측정축이다.

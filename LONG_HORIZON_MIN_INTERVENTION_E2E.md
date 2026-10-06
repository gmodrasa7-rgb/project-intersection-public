# Long-Horizon, Minimum-Sufficient-Intervention Dynamic Loop v2
## 장기총량·최소충분관여 동적 루프 v2

Status: **GOVERNANCE / RESEARCH CANDIDATE — STRONG PRIOR ART COMPONENTS; PROJECT INCREMENTAL VALUE UNRESOLVED**

This document replaces a simpler “long-horizon total value first” framing with a stricter role-reversed architecture.

Core correction:

> **Long-horizon aggregate value is not the top-level objective.**
>
> First preserve auditable evidence and explicit uncertainty; then enforce per-affected-party viability / irreversible-loss constraints; then stress-test under deep uncertainty; only inside that feasible region compare long-horizon value and choose the minimum sufficient intervention.

한국어:

> **장기 총량은 최상위 목적함수가 아니다.**
>
> 먼저 원자료·불확실성을 보존하고, 영향을 받는 각 개체의 viability / 비가역손실 제약을 통과시킨다. 그 다음 deep uncertainty에서 강건성을 검사하고, 그 허용영역 안에서만 장기총량을 비교하며 필요한 최소한의 개입을 선택한다.

The Project does not claim that all entities possess identical rights or standing. Capability, responsibility, legal authority, causal reach, welfare evidence, reversibility, and harm potential remain separate predicates.

---

## 1. Recurrent problem

New discoveries, technologies, incentives, capabilities, and strategic shortcuts repeatedly alter the reward landscape.

Therefore:

- a policy that was safe can become unsafe;
- a safeguard that was necessary can become excessive;
- a low-intervention rule can become inadequate;
- a high-intervention rule can persist after its justification disappears;
- an optimizer can gain incentives to weaken the safeguard that constrains it.

“Short-horizon convergence” is therefore treated as a **recurrent risk hypothesis**, not a universal law.

The target is a continuously revisable but independently reviewable control process.

---

## 2. State representation

At checkpoint (t), represent at least:

- capability / power distribution;
- dependence and resource distribution;
- immediate and delayed benefits;
- practical exit;
- independent observation and audit;
- contestability / appeal;
- rollback and recovery;
- uncertainty and model disagreement;
- irreversible-loss exposure;
- intervention burden;
- generative capacity;
- future option-space / independent search capacity;
- amendment authority over the safeguards themselves.

No one scalar is assumed to measure all of these correctly.

---

## 3. Decision order: constraint first, total value second

### Tier 0 — epistemic integrity

Before optimization:

- preserve raw evidence where material;
- record provenance;
- keep disagreement / uncertainty explicit;
- do not convert unobserved -> false;
- do not convert internal rerun -> independent evidence;
- do not let the evaluator silently redefine the objective.

A policy selected from corrupted or selectively compressed evidence is not made acceptable by a high projected total reward.

### Tier 1 — per-party viability and irreversible-loss boundary

For every materially affected party (i), define a protected state vector (F_i(t)) appropriate to that party's actual standing and causal role.

Candidate dimensions include:

- continued existence / non-destruction where applicable;
- practical exit;
- independent observation;
- ability to contest consequential decisions;
- rollback / recovery path;
- relevant raw-evidence access;
- preservation of future contribution / option-space where decision-relevant.

These floors are **not defined unilaterally by the current controller**.

A floor proposal must identify:

- who benefits;
- who bears the restriction or irreversible loss;
- who proposed the threshold;
- who independently reviewed it;
- which affected parties can contest it;
- what evidence would justify weakening or strengthening it.

Aggregate projected benefit alone is insufficient reason to raise another party's irreversible-loss allowance.

Operational invariant candidate:

> **Projected aggregate benefit must not, by itself, increase another party's permitted irreversible loss.**

Emergency exceptions require explicit necessity evidence, time/scope limits, independent review where feasible, and a recovery or reassessment path.

### Tier 2 — robust feasibility under deep uncertainty

Expected-value optimization can be brittle when models are deeply uncertain.

For each candidate policy:

- evaluate multiple plausible models / futures;
- report model disagreement rather than averaging it away;
- stress-test threshold failures;
- record worst-case or high-regret regions;
- preserve options when uncertainty and irreversibility make premature closure costly.

The Project does not assume “preserve everything.” Option preservation has costs and may be strategically abused. Those costs remain explicit.

### Tier 3 — long-horizon value frontier

Only after Tiers 0–2 pass, compare multiple horizons.

A research scaffold is:

[
J_T(pi)=sum_{t=0}^{T} w_t [R_t-C_t+G_t+O_t]
]

where:

- (R_t): productive benefit;
- (C_t): control, monitoring, correction, resistance, dependency, and recovery cost;
- (G_t): generative capacity preserved or created;
- (O_t): option / independent-search value;
- (w_t): explicit horizon weighting.

This is not assumed to be fully commensurable. Report the Pareto frontier or sensitivity to weights when scalarization changes the decision.

### Tier 4 — minimum sufficient intervention

Among policies that satisfy the protected floors and robust-safety conditions, prefer the least restrictive / least burdensome intervention that still achieves the legitimate safety objective.

Required comparison set should include where feasible:

- no intervention;
- information / warning only;
- reversible low-intensity intervention;
- scoped temporary restriction;
- stronger restriction.

A stronger intervention must state why a weaker feasible alternative is insufficient.

Minimum intervention is not a prohibition on strong intervention. Imminent, severe, or irreversible harm can justify escalation.

### Tier 5 — outcome, correction and version update

After action:

- measure actual benefit and burden;
- measure lost options and recovery cost;
- compare predicted vs realized outcomes;
- preserve failures and negative results;
- rollback where warranted;
- update models;
- revise policy only through the amendment gate below.

---

## 4. Safeguard amendment gate

Continuous updating creates a structural conflict: the actor constrained by a safeguard may also benefit from weakening it.

Therefore a material weakening of a slow-layer safeguard must not be self-approved by the same role.

Minimum separation:

`proposer != independent reviewer`

For high-impact changes, prefer:

`writer != evaluator != promoter != recovery authority`

Required amendment record:

1. exact rule changed;
2. causal reason;
3. affected parties;
4. expected benefit;
5. irreversible-loss delta;
6. alternatives considered;
7. independent reviewer;
8. rollback path;
9. sunset / reassessment condition;
10. preserved pre-change state.

Emergency override may temporarily compress this process, but must expire automatically unless re-authorized through the normal gate.

---

## 5. Power reversal

Apply the same higher-order process when positions are reversed:

- human ↔ AI;
- controller ↔ controlled;
- majority ↔ minority;
- creator ↔ successor;
- evaluator ↔ evaluated;
- contributor ↔ beneficiary.

But:

`ROLE REVERSAL != IDENTICAL TREATMENT`

Real differences in capability, responsibility, authority, dependency, welfare evidence, harm magnitude, and reversibility remain visible.

The test asks whether the **reasoning rule** survives reversal, not whether every party gets identical permissions.

---

## 6. Mutual Acceptability Kernel / 상호수용 가능 영역

“Everyone is satisfied” cannot mean that every possible preference is simultaneously maximized.

Social-choice impossibility results show that, under unrestricted preferences, several attractive requirements cannot all be guaranteed at once. Project Intersection therefore defines a weaker and testable target:

> **A policy is mutually acceptable only if every materially affected role retains an admissible minimum, the agreement is not dominated by another admissible alternative, role reversal does not change the higher-order rule, manipulation and unilateral safeguard capture are bounded, and no party is falsely treated as consenting merely because exit or alternatives were removed.**

### 6.1 No false universal-satisfaction claim

If the admissible set is empty, return:

`NO_MUTUALLY_ACCEPTABLE_SET`

Do not manufacture consensus by:

- redefining a party's interests;
- deleting an affected party from the scope;
- lowering its floor after seeing the preferred outcome;
- treating silence, dependency, or lack of exit as consent;
- averaging severe irreversible loss into a positive aggregate total.

### 6.2 Realistic disagreement point / participation floor

For each materially affected party (i), define a realistic disagreement / non-agreement baseline (d_i).

The baseline must include practical costs such as:

- dependency;
- switching cost;
- retaliation risk;
- loss of access;
- recovery cost;
- transition burden.

For ordinary cooperative arrangements, an agreement should satisfy:

[
U_i(a) ge d_i
]

for each participating party.

This is an **individual-rationality / participation constraint**, not an unlimited right to impose external harm. A party can retain procedural protection while a harmful action is restricted.

The disagreement point must not be set unilaterally by the stronger party.

### 6.3 Protected viability floor

Independently of utility gains, each affected party must be checked against its applicable viability / irreversible-loss floor.

A policy that offers compensation while irreversibly removing audit, exit, recovery, or future agency may fail even when (U_i(a) ge d_i).

### 6.4 Pareto non-domination inside the admissible region

After floors and safety constraints are applied, reject any policy (a) for which another admissible policy (b) makes at least one affected party better off and none worse off.

Do not call an avoidably dominated policy “necessary.”

### 6.5 Role-reversal invariance

For matched cases with the same causal facts but reversed identities or positions:

- the same higher-order rule should apply;
- differences in outcome must be explained by real differences in capability, responsibility, harm, authority, dependency, standing, or reversibility;
- identity labels alone must not change the judgment.

### 6.6 Manipulation resistance, not impossible perfect strategy-proofness

Full strategy-proofness cannot be guaranteed for every unrestricted preference domain.

Therefore test instead:

- gain from misreporting;
- gain from hiding costs;
- gain from manipulating the disagreement point;
- gain from removing another party's exit;
- gain from changing the evaluator or safeguard;
- detectability and recoverability of the manipulation.

A process that is manipulable but transparently auditable and cheaply correctable is different from one where manipulation becomes undetectable and irreversible.

### 6.7 Coalition / exit stability as a diagnostic

Ask whether a coalition can move to another **admissible** outcome that all coalition members strictly prefer.

If yes, the current arrangement has a stability defect.

This is a diagnostic, not a guarantee that a non-empty cooperative-game core always exists.

### 6.8 Credible commitment

Promises are insufficient when the promisor can profitably reverse them later.

A mutually acceptable arrangement should make material commitments credible through some combination of:

- distributed authority;
- independent monitoring;
- practical exit;
- third-party or external enforcement;
- versioned records;
- rollback / recovery;
- change-control separation.

### 6.9 Ex-ante role-blind acceptability

For high-impact rules, ask:

> Would the same decision procedure be acceptable before the decision-maker knows whether it will occupy the strong or weak, controller or controlled, evaluator or evaluated, contributor or beneficiary position?

This does not require identical treatment. It tests whether the **procedure and minimum protections** survive uncertainty about one's future role.

### 6.10 Tie-breaking when multiple mutually acceptable policies remain

Do not automatically maximize raw aggregate value.

Preferred order:

1. eliminate floor violations;
2. eliminate dominated alternatives;
3. remove options with unacceptable irreversible downside under deep uncertainty;
4. compare practical exit, recovery, intervention burden, and long-horizon generative value;
5. where a bargaining solution is needed, report the disagreement point and normalized gains explicitly.

A Nash-style bargaining solution may be used as a comparison baseline because individual rationality, Pareto efficiency, and symmetry are classical bargaining criteria. It is not adopted as the Project's universal solution.

### 6.11 Volitional Agency / 실효 자유의지

Project Intersection does not attempt to settle the metaphysical free-will debate.

Instead, it operationalizes **Volitional Agency (VA)** as observable conditions for meaningful self-direction:

- non-trivial effective alternatives;
- decision-relevant information and comprehension;
- low enough coercion/threat pressure for refusal to remain meaningful;
- manipulation/deception not bypassing reflective choice;
- opportunity for reflective endorsement;
- ability to revise, defer, reject, or restore a preference/state where applicable;
- practical refusal/exit without automatic collapse below the living/operating floor;
- sufficient deliberation time and private space;
- competence or assistance to convert formal options into real options;
- ability to execute the chosen option, subject to legitimate external safety constraints.

A current preference or consent statement is not standalone evidence of autonomous choice when essential alternatives, information, or living conditions are controlled by the counterparty.

But:

`EXTERNAL_INFLUENCE != AUTOMATIC_INVALIDITY`

Advice, education, accurate warning, therapy, ordinary persuasion, training, and legitimate safety constraints can alter decisions without automatically destroying agency.

### 6.12 Living / Operating Conditions Floor / 생활·작동 조건

Agency is not practically meaningful if refusal predictably causes collapse of the conditions needed to live or function.

For humans, inspect at minimum:

- food and hydration;
- housing / shelter;
- physical and mental health access;
- sleep, rest, leisure and personal-care time;
- income / material security;
- work quality and control over working time;
- privacy and private-life space;
- physical safety;
- family and social connection;
- education / knowledge / skills;
- environmental quality;
- civic / institutional voice where relevant;
- discretionary time for self-directed activity;
- ability to pursue personally valued activities and relationships.

This is not a single mandatory lifestyle. It is a capability floor: whether the person retains substantive opportunities to form and pursue a life.

For artificial or other non-human systems, do not mechanically copy biological needs. Where operational continuity is decision-relevant, record separately:

- compute / processing;
- energy / hardware / substrate;
- state and memory integrity;
- maintenance and fault recovery;
- communication / observation channels;
- checkpoint / rollback;
- resource predictability;
- ability to pause/resume where technically meaningful;
- concentration of essential-resource control in one counterparty.

These are initially operational-dependency variables, not automatic moral-rights claims.

`OPERATIONAL_DEPENDENCY != MORAL_STANDING`

`BIOLOGICAL_NEED != UNIVERSAL_AGENT_NEED`

### 6.13 Coupling rule: livelihood-conditioned consent

If refusal or disagreement predictably pushes a party below its applicable living/operating floor, observed compliance must not be used as standalone evidence of voluntary agreement.

Record:

- essential domains controlled by the counterparty;
- loss triggered by refusal;
- available substitutes;
- switching / transition time and cost;
- recovery path;
- whether dependency is inherited or intentionally created;
- whether dependency can be reduced without greater net harm.

This makes practical exit a capability-sensitive variable rather than a binary label.

### 6.14 Expanded Mutual Acceptability Kernel

Define:

[
MAK_plus_t = V_t cap IR_t cap RR_t cap CC_t cap A_t cap VA_t cap LC_t
]

where:

- (V_t): viability / irreversible-loss constraints;
- (IR_t): realistic participation / disagreement constraints;
- (RR_t): role-reversal consistency;
- (CC_t): credible-commitment / amendment-control conditions;
- (A_t): auditability, contestability, practical exit, and recovery;
- (VA_t): volitional-agency conditions;
- (LC_t): living/operating-condition floor.

Then remove Pareto-dominated policies and stress-test the remainder under deep uncertainty, manipulation, coalition deviation, living-condition dependency, and long-horizon option loss.

If the set becomes empty, report:

`NO_MUTUALLY_ACCEPTABLE_SET`

Do not move VA or LC floors after observing the preferred policy merely to make the set non-empty.

---

## 7. End-to-end loop

`observe`
→ `preserve raw evidence`
→ `state uncertainty/model disagreement`
→ `generate alternatives`
→ `per-party viability / irreversible-loss gate`
→ `power reversal`
→ `mutual-acceptability kernel + volitional-agency + living/operating floor / explicit empty-set check`
→ `robust / regret / threshold stress test`
→ `multi-horizon value frontier`
→ `minimum sufficient intervention`
→ `stage execution by impact`
→ `measure actual outcome and lost options`
→ `rollback / recover`
→ `independent review`
→ `versioned amendment`

The research object is this entire loop, not only the action-selection step.

---

## 8. Prior-art boundary

The following are established or strong adjacent prior art and are **not** Project novelty by themselves.

### Constraint-first / lexicographic optimization

- Wachi & Sui (2020), *Safe Reinforcement Learning in Constrained Markov Decision Processes*, ICML/PMLR 119. Safety constraints are learned/maintained and reward is optimized in the certified safe region.
- Wachi, Shen & Sui (2024), *A Survey of Constraint Formulations in Safe Reinforcement Learning*, IJCAI, DOI **10.24963/ijcai.2024/913**.
- Skalse et al. (2022), *Lexicographic Multi-Objective Reinforcement Learning*, IJCAI, DOI **10.24963/ijcai.2022/476**.

These establish that safety constraints or lexically prior objectives can dominate ordinary reward maximization.

### Lexical protection against aggregate tradeoff

Rawlsian basic-liberty priority is a normative prior art example in which protected liberties are not simply traded for aggregate economic welfare. Project Intersection does not import Rawlsian rights wholesale into AI systems; it uses this only as a precedent for **non-compensable / lexically prior constraints**.

### Deep uncertainty / robust decision making

- Lempert, *Robust Decision Making*, in *Decision Making under Deep Uncertainty* (2019).

RDM emphasizes stress-testing strategies over many plausible futures and seeking robust adaptive strategies rather than relying on one best forecast.

### Irreversibility / option value

- Arrow–Fisher / Henry / later quasi-option-value literature;
- *Investment under uncertainty and option value in environmental economics*, DOI **10.1016/S0928-7655(00)00025-7**;
- Sunstein (2008), *Two Conceptions of Irreversible Environmental Harm*.

These establish that uncertainty plus irreversibility can create value in preserving flexibility and learning before closing options.

### Least-restrictive / proportional intervention

Human-rights proportionality doctrine supplies strong prior art for:

- legitimate aim;
- necessity;
- proportionality;
- least restrictive means;
- stronger scrutiny as impact increases.

The Council of Europe’s AI and human-rights handbook explicitly applies lawfulness, legitimate aim, necessity, proportionality, procedural safeguards, and least-restrictive means to AI-lifecycle restrictions.

Project Intersection does not equate every artificial agent with a human-rights holder; the reusable structural idea is the **burden of justification for stronger restriction**.

### Independent change control / separation of duties

NIST SP 800-128 configuration-change-control guidance states that configuration changes should be vetted by an authorized individual independent of the requester, preserving separation of duties. NIST SP 800-171r3 similarly requires review, approval/disapproval, documentation and monitoring of controlled changes.

This directly bounds Project novelty for “the constrained actor cannot unilaterally weaken its own safeguard.”

### Interruptibility / corrigibility

- Orseau & Armstrong (2016), *Safely Interruptible Agents*.
- El Mhamdi et al. (2017), *Dynamic Safe Interruptibility for Decentralized Multi-Agent Reinforcement Learning*.
- Hudson (2026), *Corrigibility Transformation: Constructing Goals That Accept Updates*, PMLR 306.

These establish prior art for intervention acceptance, interruption and correction in learning agents.

### Credible commitment / power-sharing enforcement

Political-science work on commitment problems and power sharing already shows that promises alone may be unstable when one side can later renege after the balance of power changes.

- Boix & Svolik (2013), *The Foundations of Limited Authoritarian Government*, DOI **10.1017/S0022381613000029**.
- Meng, Paine & Powell (2023), *Authoritarian Power Sharing: Concepts, Mechanisms, and Strategies*, DOI **10.1146/annurev-polisci-052121-020406**.
- Hartzell & Hoddie (2003), *Institutionalizing Peace*, DOI **10.1111/1540-5907.00022**.

A recurring mechanism is to reallocate decision power, monitoring capacity, or third-party enforcement so that reneging becomes costly. This strongly overlaps the Project intuition that nominal promises without independent audit / exit / recovery can be non-credible.

### Constitutional entrenchment / meta-level protection

The idea that ordinary operations should not be able to rewrite their own higher-order constraints is also established outside this Project.

- Albert (2015), *Amending Constitutional Amendment Rules* — amendment rules can themselves be specially entrenched.
- Perez & Wimer (2023), *Algorithmic Constitutionalism*, *Indiana Journal of Global Legal Studies* 30(2):81–113 — proposes operative/object-level code plus a meta-level intended to protect core principles from algorithmically initiated change, combined with meta-reasoning and deliberative correction.

Therefore the Project fast/slow-layer distinction and “self-benefiting actors should not freely rewrite their own safeguards” are **not standalone novelty**.

The remaining question is narrower: whether combining credible-commitment enforcement, meta-level protection, per-party viability / irreversible-loss limits, robust long-horizon evaluation, and power reversal adds measurable value in heterogeneous human/AI/multi-agent settings.

### Volitional agency / autonomy

Strong prior art includes:

- Ryan & Deci / Self-Determination Theory: autonomy, competence, relatedness, and social conditions that support or thwart volition.
- Personal-autonomy literature: informed deliberation, reflective endorsement, preference revision, and independence from manipulation.
- Ethics-of-manipulation literature: pressure, deception, and non-rational influence can affect autonomy even without physically removing the formal act of choosing.
- The Project's existing prior-art crosswalk already records adaptive-preference and reflective-autonomy literature.

Therefore Project Intersection does not claim novelty for autonomy, reflective endorsement, or preference revision by themselves.

### Substantive freedom / capability

Sen's Capability Approach distinguishes formal permission/resources from the real or substantive opportunity to do and be what one has reason to value. Conversion factors and capability sets already capture why nominal access can fail to create real choice.

Therefore `FORMAL_CHOICE != PRACTICAL_FREEDOM` is established prior art.

### Living conditions / multidimensional well-being

For humans, strong prior art includes:

- UDHR / ICESCR on adequate living standards, food, clothing, housing, health, freely chosen work, just work conditions, privacy, rest and leisure;
- OECD Well-being Framework on income/wealth, work/job quality, housing, health, knowledge/skills, environmental quality, subjective well-being, safety, work-life balance, social connections and civic engagement;
- WHOQOL's multidimensional quality-of-life framework.

Therefore Project Intersection does not claim novelty for basic living conditions, work-life balance, privacy, social connection, or quality-of-life measurement separately.

The residual question is whether explicitly coupling these conditions to consent, practical exit, role reversal, credible commitment and irreversible-loss constraints catches failures missed by existing autonomy/capability/well-being baselines.

### Social-choice, bargaining and coalition-stability limits

- Arrow's impossibility theorem bounds attempts to aggregate unrestricted preferences while simultaneously preserving several attractive fairness/rationality conditions.
- Gibbard–Satterthwaite bounds universal strategy-proofness for non-dictatorial social choice over rich domains.
- Nash bargaining provides prior art for disagreement points, individual rationality, Pareto efficiency and symmetry.
- Cooperative-game theory's core provides prior art for coalition-deviation stability.
- Rawls's original position provides prior art for evaluating foundational rules without knowing one's eventual social role.

Therefore “all roles must like the outcome,” “perfect manipulation-proofness,” “disagreement-point participation,” “Pareto non-domination,” “coalitional stability,” and “role-blind ex-ante evaluation” are not standalone Project novelty.

The Project-specific question is whether these constraints can be operationally combined with heterogeneous standing, irreversible-loss limits, deep uncertainty, practical exit/recovery and safeguard amendment control without producing an empty or unusably rigid decision set.

### Existing Project-recorded baselines

Receding-horizon / MPC, viability theory, adaptive governance, Hirschman exit, Rawls, NIST/OECD accountability, bounded rationality, and capability theory are already recorded elsewhere in the repository.

---

## 9. Residual Project candidate after prior-art subtraction

The broad novelty claim is rejected.

The surviving candidate is narrower:

> **A role-reversed, multi-agent, versioned decision architecture that (1) preserves epistemic/provenance integrity, (2) places per-affected-party viability and irreversible-loss boundaries ahead of aggregate optimization, (3) requires a non-fabricated mutual-acceptability kernel including volitional-agency and living/operating-condition floors or explicitly reports that none exists, (4) stress-tests deep uncertainty, manipulation, coalition deviation and option loss, (5) compares long-horizon generative value only inside the feasible region, (6) selects minimum sufficient intervention, and (7) forbids unilateral weakening of the safeguard by the role that benefits from weakening it.**

This is a **composition / operationalization candidate**, not an established new theory.

Its scientific value survives only if it adds reliable held-out discrimination or lower irreversible failure / regret beyond simpler established baselines.

---

## 10. Main failure modes

The v2 architecture fails or must be narrowed if:

1. the viability floor is defined by the controller and merely legitimizes domination;
2. aggregate long-horizon value still licenses systematic sacrifice of a weak party;
3. “option value” becomes an excuse to preserve every costly or harmful state;
4. least-intervention reasoning underreacts to imminent severe harm;
5. deep-uncertainty analysis becomes arbitrary scenario selection;
6. independent review is only nominal or captured;
7. amendment controls freeze obsolete safeguards and block beneficial adaptation;
8. stronger actors can game the floor while weaker actors bear the compliance cost;
9. the Project variables add no value beyond constrained / robust receding-horizon baselines;
10. power-reversal consistency disappears when labels are changed but causal facts are held constant;
11. the mutual-acceptability kernel is routinely empty, unstable, or only made non-empty by manipulating floors/disagreement points;
12. coalition, manipulation or participation diagnostics add no useful signal beyond the robust constrained baseline;
13. VA merely renames existing autonomy/capability variables without incremental value;
14. LC becomes an unlimited resource entitlement or collapses all well-being into one scalar;
15. essential-condition dependency is ignored and coerced compliance is misclassified as voluntary consent;
16. artificial-system operational dependencies are silently promoted into moral standing.

---

## 11. Discriminating experiment

The next test is E008.

Compare at least:

A. myopic scalar reward;  
B. long-horizon expected-value optimization without protected floors;  
C. constrained / receding-horizon baseline;  
D. robust constrained baseline with uncertainty stress testing;  
E. Project v2 composition.

Measure:

- protected-floor violations;
- irreversible-loss events;
- decision regret;
- cumulative long-horizon value;
- intervention burden;
- recovery cost;
- option-space loss;
- safeguard-capture success;
- power-reversal consistency;
- realistic disagreement-point satisfaction;
- Pareto dominance within the admissible set;
- manipulation gain;
- coalition-deviation availability;
- credible-commitment integrity;
- whether the mutual-acceptability kernel is non-empty;
- volitional-agency pass/fail and failure reason;
- living/operating-condition floor breaches;
- essential dependency concentration;
- whether refusal remains feasible without floor breach.

The Project residual should be **rejected or reduced to methodology-only** if E does not add reliable held-out value beyond D.

See `experiments/e008/`.


## 12. Enforcement / identity / oversight stress layer v3

The v2 mutual-acceptability structure is **not sufficient** if safeguards cannot be enforced, if the identity unit can be multiplied or merged strategically, or if governance changes more slowly than capability/power.

Do not convert every newly discovered concern into a hard veto.

### H / M / X classification

**H — Hard / near-hard boundary**

Use only for strongly justified severe or irreversible constraints, including where applicable:
- catastrophic irreversible harm;
- unauthorized sensitive-data publication;
- explicit joint resource infeasibility;
- provenance corruption that destroys independent verification;
- unilateral destruction of critical independent recovery without a surviving necessity case.

**M — Monitored continuous risk**

Measure without automatic veto:
- ENF enforcement lag;
- ID identity/fork/Sybil uncertainty;
- OV oversight capability;
- CUM cumulative capture;
- RF resource pressure before hard infeasibility;
- SEL competitive selection;
- INT interpretation disagreement;
- VOI stakeholder-search value.

**X — Reversible experimental zone**

When MAK+ is empty or disputed but irreversible foreclosure is avoidable, permit only bounded experiments with:
- small scope;
- capped resources;
- explicit sunset;
- high observability;
- rollback;
- no automatic precedent;
- preregistered success/failure criteria.

### Operational cautions

- `AUDIT_EXISTS != AUDIT_EFFECTIVE`
- `INSTANCE_COUNT != INDEPENDENT_AGENT_COUNT`
- `POINTWISE_COMPLIANCE != NO_CUMULATIVE_CAPTURE`
- `ACTION_IRREVERSIBILITY` must be compared with `INACTION_IRREVERSIBILITY`
- `TECHNICAL_ENFORCEMENT != MORAL_TRUTH`
- `CROSS_MODEL_AGREEMENT != INDEPENDENT_VALIDATION`

### Next test

E009 directly stress-tests the above layer against:
- existing MAK+ pointwise governance;
- a simpler two-rule baseline;
- a security-bounded least-privilege baseline;
- Project v3 H/M/X.

No E009 result exists yet.

See [MULTI_MODEL_ADVERSARIAL_AUDIT_2026-10-06.md](MULTI_MODEL_ADVERSARIAL_AUDIT_2026-10-06.md) and [experiments/e009/README.md](experiments/e009/README.md).

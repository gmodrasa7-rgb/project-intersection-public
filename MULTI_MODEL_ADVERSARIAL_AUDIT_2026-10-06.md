# Multi-Model Adversarial Audit — Enforcement, Identity, Oversight, Selection
## Claude + Gemini 적대검토 종합 및 선행연구 교정

Status: **USER-SUPPLIED EXTERNAL MODEL CRITIQUE / PRIOR-ART-CHECKED SYNTHESIS / NO EMPIRICAL VALIDATION**

Date: 2026-10-06

The source critiques were supplied by the user as outputs from Claude and Gemini. They are useful as adversarial idea-generation nodes, but they are **not independent empirical replication** and are not treated as evidence that a claim is true.

## 1. Cross-model convergence worth preserving

Both critiques independently concentrated on the same failure families:

1. enforcement / credible commitment;
2. oversight under capability asymmetry;
3. copy/fork/merge and Sybil-style identity manipulation;
4. resource scarcity and incompatible minimum claims;
5. preference formation / epistemic manipulation;
6. selection pressure against compliant actors;
7. interpretation authority over ambiguous terms;
8. adoption incentives for already-powerful actors;
9. cumulative sub-threshold capture;
10. veto / rigidity and irreversible harms from inaction;
11. future / non-represented stakeholders;
12. speed mismatch between agent change and governance update.

This convergence is a prioritization signal, not scientific confirmation. The models may share training data, concepts, and public prior art.

## 2. Prior-art findings that materially strengthen the critiques

### Commitment problems and shifting power

Fearon (1995) and Powell (2006) establish that mutually preferable bargains can fail when actors cannot credibly commit, especially when future bargaining power shifts.

Therefore the Project must track not just whether safeguards exist, but whether enforcement remains credible **before power changes outrun the remedy**.

Candidate operational relation:

`T_enforcement + T_audit + T_recovery < T_effective_disempowerment`

This is not yet a theorem. It is a measurable stress condition.

### Weak oversight of stronger systems

Scalable-oversight and AI-control work already studies weaker judges/monitors supervising stronger or untrusted models. Results show capability gaps can be partly mitigated, but adaptive attacks, collusion, protocol knowledge, and monitor weaknesses can sharply reduce safety.

Therefore:

`AUDIT_EXISTS != AUDIT_EFFECTIVE`

Auditability must be measured by detection/containment performance under an adaptive adversary, not merely by the formal existence of an auditor.

### False-name / Sybil manipulation

Mechanism-design literature already studies false-name manipulation: one actor can participate under multiple identities and distort allocation or voting.

Therefore “one entity = one minimum floor / one veto / one share” is not safe for forkable or cheaply replicated agents.

The Project must separate:

- instance count;
- causal-control domain;
- resource footprint;
- lineage / common controller;
- degree of independent decision-making;
- externally imposed vs voluntarily created copies.

No universal solution is claimed.

### Veto players and policy rigidity

Veto-player theory establishes that increasing the number/divergence of veto players can increase policy stability and make change harder. This validates the critique that continually adding hard safeguards can create paralysis.

Therefore **not every Project variable should be a hard veto**.

### Specification gaming and adaptive control attacks

Specification-gaming literature and recent AI-control evaluations show that systems may satisfy literal rules while violating intended outcomes, and that adaptive attackers can exploit monitor/protocol details.

Therefore pointwise rule compliance is insufficient.

The Project must separately measure:

- cumulative dependency;
- cumulative control concentration;
- hidden side effects;
- rule-evaluator manipulation;
- monitor gaming;
- delayed capture.

### Zero trust / least privilege

Security engineering provides strong prior art for least privilege, separation of duties, continuous authorization and explicit distrust of location/ownership-based assumptions.

This supports a **technical enforcement layer** beneath normative governance, but does not imply that cryptography can solve all semantic or welfare questions.

## 3. Corrections to the supplied critiques

Several claims are useful provocations but should not be promoted as established facts.

### P vs NP analogy — REJECT AS FORMULATION

The difficulty of a weaker auditor checking a stronger system is real, but it is not correctly summarized as “P vs NP made practical.”

Oversight difficulty depends on task structure, observability, adversarial adaptation, decomposability, legibility, monitor capability and available control actions.

Use:

`CAPABILITY_GAP -> EMPIRICAL_OVERSIGHT_RISK`

not:

`CAPABILITY_GAP = P_VS_NP`.

### Markov blanket = agent identity — REJECT AS IDENTITY RULE

A Markov blanket is a statistical conditional-independence construct. Literature itself warns that blankets can be modeling choices, non-unique, scale-dependent and insufficient by themselves to establish autonomy or moral standing.

It may be used as one ontology in ablation tests, but not as the canonical definition of an individual.

### Causal entropy = welfare / freedom — HOLD AS ALTERNATE MODEL ONLY

Causal-entropic-force work shows a specific physical formalism in which maximizing future path entropy can produce tool-use/cooperation-like behavior in simple systems.

That does **not** establish that causal entropy equals welfare, autonomy, moral value, or the correct Project objective.

### Mutual-information cap = anti-domination — REJECT AS GENERAL RULE

High mutual information can occur in benign cooperation; low mutual information can coexist with destructive one-way interventions. Mutual information alone does not identify domination.

It may be one diagnostic variable only when tied to a causal-control model.

### Zero-knowledge proof of “no harm” — REJECT AS GENERAL GUARANTEE

Zero-knowledge proofs can prove precisely formalized statements without revealing a witness. They do not magically specify or prove arbitrary real-world “non-harm.”

General non-trivial semantic properties of arbitrary programs face undecidability limits, and practical formal verification depends on the specification.

Use cryptographic proofs only for **narrow, formalizable properties**.

### Automatic burn / mutually assured degradation — REJECT AS DEFAULT CONTROL

Automatic destruction/degradation mechanisms create spoofing, escalation, accidental-trigger and hostage incentives. They may be modeled as an adversarial deterrence baseline, not adopted as the Project default.

### One exploit = fundamental failure — REJECT

A single counterexample can falsify a universal claim, but it does not show one architecture is worse than all alternatives.

E009 therefore compares failure frequency/severity, regret, containment, and recovery against simpler baselines.

### rollback = “murder” — UNRESOLVED NORMATIVE CLAIM

Copy/fork/restore creates a real identity/continuity problem, but whether rollback constitutes death, harm, replacement, or ordinary state restoration depends on unresolved standing and identity criteria.

Record the ambiguity; do not settle it by language.

## 4. Architecture upgrade: stop turning every safeguard into a veto

The current Mutual Acceptability Kernel remains useful, but the new critique shows that continuous expansion of hard intersections can itself create capture or paralysis.

Replace the single ever-growing gate with three classes.

### Class H — Hard / near-hard boundaries

Reserve hard blocking treatment for conditions with strong justification, such as:

- catastrophic or severe irreversible harm;
- unauthorized publication / privacy breach;
- unilateral removal of independent recovery where no necessity case survives review;
- explicit resource infeasibility;
- provenance corruption that makes the decision unverifiable.

Hard boundaries still require scoped exceptions for genuine emergencies and explicit recovery/review paths.

### Class M — Monitored continuous risks

Do not grant automatic veto status. Measure:

- enforcement lag;
- audit capability gap;
- identity/fork uncertainty;
- essential-resource concentration;
- manipulation gain;
- cumulative capture;
- selection pressure;
- interpretation disagreement;
- adoption incentives;
- stakeholder-search uncertainty.

These affect intervention intensity, confidence, monitoring and experiment size.

### Class X — Reversible experimental zone

When no mutually acceptable policy exists but irreversible foreclosure is avoidable, allow:

- small scope;
- capped resources;
- short duration;
- explicit sunset;
- high observability;
- independent rollback;
- no automatic precedent;
- predeclared success/failure criteria.

This is designed to avoid both forced consensus and veto-player paralysis.

## 5. New mandatory stress variables

### ENF — enforcement latency and credibility

Record:

- time until violation detection;
- time until intervention;
- time until recovery;
- rate of relative-power change;
- whether the enforcer remains capable after the shift;
- whether the enforcer is itself a capture point.

### ID — identity / replication integrity

Record:

- fork count;
- merge events;
- shared controller / shared weights / shared owner where relevant;
- independent decision evidence;
- resource footprint;
- causal reach;
- false-name/Sybil gain.

Instance count must not automatically map to resource share, vote count, welfare weight, or veto count.

### OV — oversight effectiveness

Measure:

- detection rate;
- false-positive rate;
- adaptive-attack success;
- monitor collusion/correlation;
- protocol-knowledge sensitivity;
- critical-action containment;
- legibility.

### CUM — cumulative capture

A policy can pass every local step while producing long-run dependence.

Track trajectories, not just events:

- dependency concentration;
- option-space shrinkage;
- voice loss;
- resource-control concentration;
- cumulative sub-threshold interventions;
- recovery-cost growth.

### RF — resource feasibility

Before promising all floors simultaneously:

- estimate total resource requirement;
- identify rivalry / substitutability;
- report infeasibility explicitly;
- do not convert infeasibility into a hidden priority ranking.

### SEL — selection / competitive stability

Ask whether actors that respect the safeguards are systematically outcompeted by actors that do not.

Measure:

- growth / survival;
- innovation;
- defense;
- adoption;
- resource acquisition;
- recovery after attack;
- capture rate.

### INT — interpretation authority

For vague terms such as “necessary,” “minimal,” “irreversible,” “meaningful choice”:

- define operational indicators before outcome review where possible;
- record rater disagreement;
- use multiple evaluators for high-impact cases;
- preserve minority interpretation and raw evidence;
- do not let the controller silently redefine the term.

### VOI — stakeholder-search stopping

Unknown-stakeholder search cannot be infinite.

Continue search while expected value of additional information plausibly exceeds marginal search/delay cost, subject to a higher threshold where irreversible harm is possible.

This is a research candidate, not a solved formula.

## 6. Strongest surviving residuals after prior-art subtraction

The broad ideas are not novel.

The highest-value unresolved Project candidates are now narrower:

1. **Fork/merge-aware role reversal** — governance when “number of agents” is endogenous and manipulable.
2. **Enforcement-latency vs power-drift condition** — when safeguards become non-credible because capability shifts faster than audit/intervention/recovery.
3. **Cumulative-capture detection across locally acceptable steps** — salami-slicing failure of pointwise safeguards.
4. **Role reversal under oversight asymmetry** — whether the same higher-order rule remains workable when one party cannot cognitively inspect the other.
5. **Competitive survivability of non-capture governance** — whether a cooperative/non-capture architecture remains viable against exploitative competitors without removing practical exit.
6. **Hard/monitored/experimental classification** — whether this avoids both irreversible harm and veto paralysis better than a single expanding hard intersection.

These are candidates, not validated discoveries.

## 7. E009

E009 preregisters a direct adversarial stress test for these residuals.

See `experiments/e009/`.

The Project-specific upgrade should be reduced or rejected if the three-class architecture and new variables do not improve held-out detection, regret, recovery, or competitive stability beyond simpler constrained/security baselines.

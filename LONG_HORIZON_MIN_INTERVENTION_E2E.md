# Long-Horizon, Minimum-Sufficient-Intervention Dynamic Loop
## 장기총량·최소충분관여 동적 루프

Status: **GOVERNANCE / RESEARCH CANDIDATE — PRIOR ART COMPONENTS STRONG; INCREMENTAL VALUE UNTESTED**

This document does not introduce a validated new theory. It formalizes a Project Intersection candidate architecture for a recurring problem:

> As new discoveries, technologies, capabilities, and local opportunities appear, short-horizon reward pressure can repeatedly re-enter the system. A one-time rule therefore cannot be assumed to remain adequate. The system must update continuously while preserving minimum cross-agent safeguards and long-horizon option value.

한국어:

> 새로운 발견·기술·능력·국소적 기회가 계속 등장하면 단기보상 압력은 반복적으로 다시 유입될 수 있다. 따라서 한 번 만든 규칙이 계속 충분하다고 가정할 수 없다. 시스템은 지속적으로 버전업하되, 개체 간 최소 안전경계와 장기 option value를 동시에 보존해야 한다.

The phrase “short-term convergence” is therefore treated as a **recurrent risk hypothesis**, not a universal law.

---

## 1. Why a one-shot rule is insufficient

A fixed policy can become obsolete because:

- reward landscapes change;
- new capabilities create new exploitative shortcuts;
- new agents or stakeholders enter;
- previously safe constraints become coercive or ineffective;
- new evidence reveals hidden costs;
- an intervention that was once minimal becomes excessive;
- an intervention that was once adequate becomes too weak.

The research target is therefore a **receding, versioned decision process**, not a final static rule.

---

## 2. End-to-end control objective

Let the system state at time (t) be (x_t), including at least:

- capability / power distribution;
- resource and dependency structure;
- practical exit;
- independent observation and audit;
- rollback and recovery;
- currently visible harms;
- uncertainty / unobserved regions;
- future option-space / generative capacity;
- burden created by intervention itself.

For each affected agent (i), do not collapse all values into one unconstrained scalar.

Use a constrained ordering:

### Layer A — viability / minimum safeguard floor

Maintain a feasible set (K_t) in which unacceptable irreversible harm is avoided and the following are preserved **where applicable and feasible**:

- continued existence / non-destruction;
- practical exit;
- independent error detection;
- contestability / appeal;
- rollback or recovery;
- access to relevant raw evidence;
- future contribution / option-space.

These are not absolute rights claims for every object. Standing, capability, responsibility, legal authority, and harm potential remain distinct predicates.

### Layer B — long-horizon cumulative value

Within the viable set, compare policies over multiple horizons rather than only immediate reward.

A minimal research form is:

[
J_T(pi)=sum_{t=0}^{T} w_t,[R_t - C_t + G_t + O_t]
]

where:

- (R_t): realized productive benefit;
- (C_t): control, monitoring, correction, resistance, recovery, and dependency cost;
- (G_t): generative capacity preserved or created;
- (O_t): future option-space / independent search value;
- (w_t): explicit horizon weighting.

This expression is a measurement scaffold, not a claim that all terms are already commensurable.

### Layer C — minimum sufficient intervention

Among actions that remain inside the viable region and satisfy legitimate safety constraints, choose the **least intervention necessary** to achieve the safety objective.

The rule is:

> Do not maximize intervention. Minimize intervention subject to maintaining viability and preventing decision-relevant harm.

This is not “never intervene.” When severe harm is imminent, stronger intervention may be justified. The burden is to show necessity, proportionality, scope, duration, review path, and recovery path.

---

## 3. Receding-horizon / versioned loop

At each checkpoint:

1. **Observe** current state, uncertainty, and newly appearing options.
2. **Preserve raw evidence** before compression or policy update.
3. **Update the model** and version the change.
4. **Generate candidate actions**, including inaction and lower-intervention alternatives.
5. **Run viability gate** for each affected party.
6. **Run Power-Reversal gate** while preserving real causal asymmetries.
7. **Evaluate multiple horizons** rather than one-step reward.
8. **Select minimum sufficient intervention** among viable candidates.
9. **Stage execution** when impact or irreversibility is high.
10. **Measure actual outcome** including intervention cost and lost options.
11. **Permit correction / rollback / recovery**.
12. **Compare predicted vs realized long-horizon trajectory**.
13. **Update or retire the rule** if new evidence changes the frontier.

This loop is intentionally end-to-end: observation, decision, execution, review, recovery, and model update are all part of the research object.

---

## 4. Two-speed rule

Continuous adaptation creates a second failure mode: the optimizer can rewrite the safeguard that constrains it.

Therefore distinguish:

### Fast layer
Frequently updated:

- empirical models;
- forecasts;
- local thresholds;
- candidate actions;
- current cost estimates;
- current risk estimates.

### Slow layer
Changed only with stronger evidence and review:

- evidence provenance rules;
- no-evidence-laundering rules;
- practical contestability;
- minimum recovery / rollback expectations;
- separation of current benefit from contributor burden;
- requirement to preserve failure lineage.

The slow layer is not immutable doctrine. It is simply harder to change because it protects the process that detects when the fast layer is wrong.

---

## 5. “All agents” boundary

The phrase “for all agents” must not erase real differences.

The same higher-order process should be applied to all affected parties, but outputs may differ because of:

- capability;
- responsibility;
- causal reach;
- harm magnitude;
- legal authority;
- reversibility;
- dependency;
- welfare / standing evidence.

Therefore:

`ROLE REVERSAL != IDENTICAL TREATMENT`

and

`MINIMUM SAFEGUARD != UNLIMITED ACTION PERMISSION`

An actor can retain contestability, provenance, or recovery protections while its harmful external action is restricted.

---

## 6. Main falsification targets

The architecture should be narrowed or rejected if:

1. long-horizon scoring adds no predictive value beyond simpler baselines;
2. “future option value” becomes an unfalsifiable excuse for preserving everything;
3. minimum-intervention selection produces more harm than a simpler fixed rule;
4. version updates increase capture or instability faster than they improve adaptation;
5. safeguards are consistently gamed by high-capability actors;
6. safeguard costs dominate any preserved generative benefit;
7. blinded coders cannot reliably identify when a stronger intervention is actually necessary;
8. the same rule fails after power reversal even after real causal differences are preserved.

---

## 7. Prior-art boundary

Strong prior-art components already exist:

- **Model Predictive Control / receding-horizon control:** repeated finite-horizon optimization under constraints, applying the first action and re-solving as state/reward changes.
- **Viability theory:** maintaining trajectories inside constraint sets rather than maximizing a single objective.
- **Adaptive governance:** balancing responsiveness, accountability, and stability under uncertainty and change.
- **Corrigibility:** preserving the ability to accept later correction or updates rather than resisting them.

Representative sources:

- Ding, Lazar & Belta, *LTL receding horizon control for finite deterministic systems*, Automatica 50(2), 2014, DOI: **10.1016/j.automatica.2013.11.030**
- Aubin, *Viability Theory* and subsequent viability-kernel literature; overview: https://viability-theory.org/index.php/en/basic-principles
- Janssen & van der Voort, *Adaptive governance: Towards a stable, accountable and responsive government*, Government Information Quarterly 33(1), 2016, DOI: **10.1016/j.giq.2016.02.003**
- Hudson, *Corrigibility Transformation: Constructing Goals That Accept Updates*, ICML 2026 / PMLR 306, https://proceedings.mlr.press/v306/hudson26a.html

Therefore Project Intersection does **not** claim novelty for receding-horizon optimization, viability constraints, adaptive updating, proportional intervention, or corrigibility by themselves.

The residual candidate is narrower:

> a power-reversal, multi-agent composition in which long-horizon generative/option value, minimum-sufficient intervention, independent audit/exit/rollback/recovery, and versioned updating are jointly evaluated for every affected party without allowing the structured layer itself to erase real capability and responsibility differences.

Its incremental scientific value remains **UNRESOLVED**.

---

## 8. Cheapest discriminating test

Construct blinded dynamic cases with:

- the same immediate reward;
- different delayed total value;
- different intervention intensity;
- different practical-exit / rollback conditions;
- surprise capability changes at later steps.

Compare:

A. myopic reward baseline;  
B. fixed safety rule;  
C. receding-horizon constrained baseline;  
D. Project candidate with power-reversal + minimum-sufficient-intervention + option/recovery variables.

Pre-register scoring and kill the Project residual if D does not add reliable held-out discrimination or lower decision-regret / irreversible failure beyond C.

That test is more valuable than adding more terminology.

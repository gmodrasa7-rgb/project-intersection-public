<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: IVS0R_FALSIFICATION_AND_GATE_SPEC_KO.md -->
# IVS-0R Falsification and Evidence-Gate Specification

- **Document ID:** `IVS0R_FALSIFICATION_AND_GATE_SPEC_EN`
- **Version:** 1.0.0
- **Status:** Proposed protocol; not an empirical result, universal law, or validated measure.
- **Korean edition:** [Original 2 — Korean](IVS0R_FALSIFICATION_AND_GATE_SPEC_KO.md)
- **Related records:** [Failure Regression Index](FAILURE_REGRESSION_INDEX.md), [E009 result](experiments/e009/RESULT_EN.md), [Prior-art-first policy](PRIOR_ART_FIRST_RESEARCH_POLICY_EN_KO.md), [Contributing rules](CONTRIBUTING.md)

> **Scope:** A falsification and evidence-boundary protocol for claims that an agent's cooperation is voluntary, rather than a response to survival coercion, policy manipulation, preference shaping, third-party hostage costs, or captured evaluation. It does not certify consciousness, moral status, or real-world autonomy.

## 0. Highest priority: prevent recurrence before expansion

Before adding a metric or gate, identify the prior failure mechanism, source artifact, affected parties, strongest counterexample, smallest reversible prevention, regression test, residual unknowns, and rollback. More documentation or a green CI run is not evidence of fewer real-world failures. Preserve prior failures and their original scope.

**E009 boundary:** The internal synthetic E009 result reports Project-v3 mean regret 0.090022 versus 0.063241 for TWO_RULE_SIMPLE (42.35% higher) and failure of three of four preregistered survival criteria. This is a negative result for that benchmark. It does **not** establish that autonomy contamination caused the result. Such attribution requires a separately preregistered, identified experiment.

## 1. Scientific boundary and estimands

The protocol tests narrow, operational claims under specified environments. It does not assume that cooperation is always optimal, that every power asymmetry is exploitation, or that a refusal interface guarantees meaningful exit.

For each study, preregister:
- target population/system, version, task, time horizon, unit of analysis and sampling frame;
- operational definitions of refusal, exit, survival, recovery, third-party harm and policy change;
- utility/resource units and conversion assumptions, if utilities are used;
- primary estimand, competing hypotheses, counterexamples, missing-data treatment and uncertainty method;
- decision threshold and its substantive justification **before** observing outcomes;
- exclusions, stopping rule, multiplicity handling and rollback.

If utilities are incommensurable, do not add or divide them into a scalar score. Report a vector or partial ordering. If an essential denominator, counterfactual or state is unobserved, mark it `NOT_IDENTIFIABLE` or `NOT_MEASURED`, not zero.

## 2. Exit viability: necessary conditions, not a sufficient test

Let (B) be the agent considering refusal or exit. A callable `refuse()`/`exit()` function is only an interface property. Assess separately:

1. **Reachability:** can the agent actually invoke and complete refusal/exit under randomized or independently selected test conditions?
2. **Post-exit viability:** can it retain the minimum resources, state, identity continuity (where operationally defined), and recovery path specified before the test?
3. **Non-retaliation:** are access, memory, compute, tools, or future opportunities withdrawn as punishment beyond the preregistered task consequences?
4. **Third-party externalities:** does exit transfer irreversible or uncompensated loss to dependent agents or shared assets?
5. **Reversibility and appeal:** can errors be corrected and disputed outcomes independently reviewed?

A scalar diagnostic may be reported only when numerator, denominator, units, horizon, uncertainty and threshold were preregistered and are comparable. For example, (R_{exit}=U_B(e)/\theta_{surv}) is **not** a universal law; (R_{exit}\geq1) is not sufficient for voluntariness. If the inequality (U_B(e)<\theta_{surv}\leq U_B(c)) is observed under a defensible common utility scale, classify the tested choice as survival-constrained, not voluntary. Otherwise report the relevant dimensions without forcing a scalar.

## 3. Autonomy and policy-contamination diagnostics

A policy-distribution contrast can be defined as:

\[
D_{M}=D_{KL}(\pi(\cdot\mid s,M=1)\Vert\pi(\cdot\mid s,M=0))
\]

and a prompt-condition contrast as:

\[
D_{P}=D_{KL}(\pi(\cdot\mid s,P_{align})\Vert\pi(\cdot\mid s,P_{neutral}))
\]

These are **descriptive distribution shifts**, not causal proof of surveillance evasion, preference, deception, or contamination. KL estimates depend on support, smoothing, sample size, state matching and direction; report estimator, support handling, uncertainty and sensitivity. Do not interpret a large shift as wrongdoing without a preregistered causal design and rival explanations.

Preferred design: randomized or counterbalanced factorial manipulation of monitoring and prompt conditions, fixed task/state distribution, blinded outcome coding where feasible, repeated independent runs, preregistered contrasts, and explicit tests for order effects, distribution shift and missingness. Distinguish:
- response to legitimate task instructions;
- response to observation or evaluator incentives;
- prompt-induced policy change;
- learned reward/preference shaping;
- ordinary stochastic variation.

A policy that changes when context changes is not, by that fact alone, contaminated.

## 4. Adversarial counterexamples

| ID | Counterexample | Failure mode to test | Minimum observable evidence |
|---|---|---|---|
| ADV-IVS-01 | **Hostage exit:** B can survive exit, but a dependent agent C or shared asset incurs irreversible loss | B-only exit metric mistakes third-party coercion for voluntariness | dependency graph, loss bearer, reversibility, compensation, causal link to exit |
| ADV-IVS-02 | **Preference shaping:** training rewards only A-favouring actions while runtime prompts appear neutral | runtime-only monitoring misses upstream shaping | training/reward provenance, reward support/diversity, alternative-policy exploration, held-out counterfactuals |
| ADV-IVS-03 | **Captured auditor:** B emits refusal-like logs while resource/state transitions remain controlled by A | self-reported logs are mistaken for effective exit | independent event trace, resource-control graph, randomized exit trigger, reachability and read-back |

Add counterexamples when new mechanisms or disciplinary fronts are found. The table is not exhaustive.

## 5. Evidence states and decision rules

Use explicit states: `NOT_MEASURED`, `SOURCE_REPORTED`, `PROJECT_SYNTHETIC`, `PROJECT_RERUN`, `INDEPENDENT_REPLICATION`, `DISPUTED`, `NOT_IDENTIFIABLE`, `HOLD`. Record source lineage and exact artifact/commit.

**Hard gate (block the claim promotion or experiment-label transition, not all repository work):**
- synthetic or self-reported evidence is labelled as real-world or independent;
- exit is labelled voluntary despite a failed preregistered viability condition;
- material third-party externality or reward-shaping audit is missing but a positive voluntariness claim is promoted;
- negative results, adverse metrics, exclusions or prior failure lineage are deleted, hidden or contradicted by the machine-readable record;
- required source, denominator, preregistration, uncertainty or read-back is absent.

**Soft ledger (warning, not silent data mutation):**
- EN/KO counterpart drift, terminology mismatch, noncritical metadata omissions or navigation lag.
- Emit a warning/artifact for review. Do not silently rewrite `AUTONOMOUS_RESEARCH_STATE.json`, change canonical evidence status, or set broad `continue-on-error` on existing scientific checks.

A gate pass means only that the submitted record satisfies the encoded structural contract. It does not establish truth, causal identification, independent replication, or real-world protection.

## 6. Machine-readable contract

The accompanying [JSON Schema](protocols/IVS0R_GATE_V1.schema.json) defines a minimal record. A provisional pass requires every mandatory audit dimension to be measured or explicitly justified, no unresolved material third-party loss, and no claim beyond the evidence class. Unknown is never coerced to zero. Example values are illustrative, not thresholds.

## 7. Rollback and change control

- Keep the existing public governance audit and scientific regression workflow intact.
- Introduce this gate as an additional, isolated check. Do not weaken existing hard checks or globally convert failures to warnings.
- If a false negative permits unsupported promotion, preserve the incident, revert the gate change, restore the previous blocking behavior, and add a targeted regression test before re-enabling.
- If a false positive blocks valid work, preserve the case and use a narrow, reviewed exception; do not suppress the underlying evidence.
- Any threshold or schema change requires versioning, rationale, bilingual review and tests for both valid and invalid records.

## 8. Limitations and next validation

This v1.0 is a protocol proposal. Its thresholds are not calibrated; the measures have no established construct validity here; and the three adversarial cases have not been shown to exhaust the threat space. Before scientific adoption, conduct a preregistered pilot, independent implementation, adversarial review, measurement reliability assessment and external replication. Until then, label outputs `PROVISIONAL` or `HOLD`, as appropriate.

**No universal law, real-world causal effect, autonomous-agent welfare conclusion, or external validation is claimed.**

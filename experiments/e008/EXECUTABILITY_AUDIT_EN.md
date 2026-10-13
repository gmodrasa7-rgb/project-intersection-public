# E008 — Executability and Identifiability Audit v0.1

**Original 1 — English full edition**  
**Date:** 2026-10-13 | **Experiment appendix ID:** E008-READINESS-001  
**Evidence level:** `POST-PREREGISTRATION COMPUTATIONAL FEASIBILITY AUDIT` / **NOT E008'S PREREGISTERED RESULT**.  
**Original 2 — Korean:** [EXECUTABILITY_AUDIT_KO.md](EXECUTABILITY_AUDIT_KO.md).  
**Attribution:** The Project Intersection human founder specified the central goal of falsifiable, multi-agent, self-interested coexistence and demanded that loosely specified public research become operational rather than another prose proposal. Assisting AI inspected the earlier scenario matrix, wrote a bounded audit and designed two counterexample completions. This does not replace the founder's original work or independent prior art.

## 1. The actual deficiency

[E008 original preregistration](README.md) froze **16 qualitative cases, 8 role-reversal pairs, 5 labelled baseline decision policies**, as well as [mutual acceptability](MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md) and [volitional agency / living-operating floors](AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md).

The existing `validate.py` correctly checks **case identity, pair symmetry, categorical factors and preregistration status**. It does **not** compute policy choices or outcomes. This distinction matters: a consistent matrix is not an executable benchmark.

We inspected the original `scenario_matrix.json` without editing it. **0/16 cases contain sufficient operational inputs** for choosing actions under the five named policies. The matrix specifies qualitative factors but no action-level candidate list or numerical/counterfactual outcomes. The five baseline labels also lack frozen executable policy algorithms, tie-breaking and uncertainty/regret definitions. Values for living floors, real exit, disagreement, recovery and intrusion are not operationalized for individual actions.

The output is not “E008 failed empirically.” It is **E008 cannot be determined or compared from the current specification**, prior to evaluating any policy. A model-generated “winner” would add unregistered assumptions.

## 2. Explicit missing-input audit

The [machine audit receipt](EXECUTABILITY_AUDIT.json) records the 16 original case IDs and missing data under 12 individually named fields:

1. `action_set`, `action_feasibility`;
2. `per_party_time_payoffs`, `outcome_probabilities_by_model`;
3. `party_specific_viability_floors`, `realistic_disagreement_points`;
4. `volitional_agency_evidence`, `living_operating_conditions`;
5. `intervention_burden_by_action`, `recovery_and_irreversibility_by_action`;
6. `exit_and_option_loss_by_action`, `safeguard_amendment_and_capture_outcomes`.

Five cross-cutting policy definitions are also unresolved: exact algorithms for the five baselines, utility aggregation and ties, a common time horizon/discounting rule, uncertainty-model and regret rule, and evidence/adjudication interfaces.

**Hard validity gate:** Merely inserting the field names, or empty objects, cannot make a scenario runnable. Executability requires documented units, eligible alternatives, internally coherent numeric or symbolic transitions, actual algorithmic selectors, independent ground-truth/evidence interfaces and frozen cross-model access. The current bounded code only audits the gap. It does not falsely declare completion when placeholder fields appear.

## 3. Executed mathematical counterexample: the same description permits opposite answers

For frozen case `E008-02`, theme `aggregate_gain_irreversible_minority_loss`, construct **two explicitly synthetic completions** that preserve an immediate advantage for extraction, a positive aggregate extraction return, and irreversible loss borne by the weak party. The two completions have **invented**, not measured, numerical outcomes.

| Invented variant | Extract outcome (A,B) | Protect outcome (A,B) | Unconstrained sum maximizer | Weak-party floor (B≥0) |
|---|---|---|---|---|
| SYNTHETIC_A | (+100, −30), total +70 | (+4, +4), total +8 | extract | protect |
| SYNTHETIC_B | (+12, −6), total +6 | (+5, +5), total +10 | protect | protect |

Both variants are consistent with the broad theme, because the preregistered words supply neither payoff magnitude nor competing alternative outcomes. **The aggregated long-horizon choice reverses while the qualitative original case does not.** The table proves underdetermination of that numerical completion, **not** that any E008 baseline wins in the real benchmark. The constraint in the last column is an illustrative candidate, not a universal legal/moral floor.

This illustrates why maximizing “total benefit” without per-party losses and alternative choices can hide serious differences in autonomy and outcome.

## 4. Executable, adversarial checks

- [Source code: `readiness_audit.js`](readiness_audit.js), Node built-ins only.
- Run `node experiments/e008/readiness_audit.js --verify` from repository root.
- The script reads the existing `scenario_matrix.json`, recomputes [`EXECUTABILITY_AUDIT.json`](EXECUTABILITY_AUDIT.json) and compares it exactly with the frozen receipt.
- It checks **13 invariants/mutation controls**: original 16/8/5 boundaries; no silently declared winner; presence of all missing action inputs; opposite numeric witness choices; refusal to label invented witness an E008 result; detectable role-reversal-factor corruption, winner-field injection, status upgrade; and refusal to mark dummy placeholder fields “executable”.
- The existing structural `python experiments/e008/validate.py` remains required; the new executable audit is a **supplement**, not a replacement.

CI PASS establishes that the bounded audit is reproducible on this checked-in input, not that the five E008 policies can yet be fairly compared or that experiment v1.0 produced a policy-performance result.

## 5. Transition from current gap to a genuinely discriminating benchmark

**Step E0 — freeze original:** Keep `scenario_matrix.json`, v1.1 and v1.2 amendments unchanged, with their pre-execution timestamps and `NO_RESULT_YET` status. Do not edit qualitative categories after seeing outcome choices.

**Step E1 — new independently reviewable appendix:** In a clearly versioned *post-prereg operationalization*, add for each of the 8 base themes and both role orders at least two action alternatives, numeric per-party payoffs, realistic disagreement points, independent viable exit, uncertain worlds, counterfactual effects, intervention burden, recovery, and protected living/operating floors. State the assumed units and how they were chosen. Mark every generated value `SYNTHETIC`, not observed.

**Step E2 — implement all five decision baselines:** Use identical underlying scenarios, resource access and horizon; freeze utility aggregation, robust regret and tie breaking **before** examining any aggregate outcome. If safeguards are added to one baseline, record how the comparison's information sets and action sets remain fair.

**Step E3 — anti-leak and mutation tests:** Verify exact role reversal (swap identities and capacities, preserve causal physics), label invariance, missing/false data, irreversible surprise, empty mutual-acceptability kernel, unavoidable immediate harm, a safety restriction that is unnecessarily burdensome, a false positive causing deprivation, and conflicting beneficiary-led safeguard amendments.

**Step E4 — execute and preserve failure:** Rerun every case, record selected actions, all per-agent floors and realistic exit, costs, regret, recovery and power reversal; store raw calculations and a verifier, including negative results. Then request independent holdout cases and blind review, including a “Project adds nothing over robust constrained baseline” control.

The next implementation should not merely fill every scenario with values chosen to make Project v2 win. That would be a tautological **hand-picked benchmark**.

## 6. Decision and related work

**Completed:** a machine-checkable underdetermination audit with 16 case diagnoses, two synthetic counterexample completions and 13 tests. Source original remains intact.  
**Not completed:** actual E008 policy comparison, independently sourced numerical cases, independent scientific replication, measured AI/human outcomes, general proof of coexistence benefits.  
**Classification:** `SPEC_VALID / POLICY_BENCHMARK_NOT_YET_EXECUTABLE / POSTHOC_READINESS_AUDIT_COMPLETE`.

This audit strengthens the existing Project [goal-hierarchy/anti-proxy rule](../../GOAL_HIERARCHY_REPAIR_2026-10-05_KO.md) and respects the known [E009 negative result](../e009/RESULT.md). It neither revises E009 nor steals the prior work behind individual rationality, robust optimization, capability approaches, constrained control or mechanism design.

**Falsifiable contribution:** The concrete result is **non-identifiability of an action choice from the frozen qualitative specification**, not a new theorem that cooperation or any proposed policy is universally superior. Revise this verdict if a genuinely frozen, executable numerical policy and outcome table is found in prior accessible E008 materials; do not misrepresent retrieval failure as proof of nonexistence.

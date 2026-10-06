# E010 Executable Protocol v1.1
## E010 실행가능 사전등록 v1.1

Status: **SUPERSEDED AS RESULT-GENERATING SPEC / PRE-RESULT CONSTRUCT MISMATCH / NO RESULT**

v1.1 supersedes v1.0 **before any E010 result execution**.

Reason for amendment: v1.0 gave proof burden and exit loss only to the Project-specific policy. Subsequent prior-art review found that inspection/compliance administrative burden and the cost of regulatory procedures are established baselines. Keeping those variables exclusive to POWER_REVERSAL_META would bias the benchmark in the Project's favor.

v1.0 is preserved as amendment lineage and must not be silently deleted.

## 0. Pre-result invalidation note

After v1.1 was written but **before any E010 result execution**, role-reversal/construct-validity review found that this executable spec does not instantiate the Project-specific residual it claims to test.

The residual requires dynamic state transitions for:
- inspector/decision authority accumulation;
- affected-party audit/contest/exit/rollback/recovery capacity;
- repeated benefit versus proof/correction/recovery burden;
- practical-exit degradation over repeated interactions.

The current executable matrix is static and does not represent those state transitions. After adding the cost-aware C2 baseline, the remaining D-vs-C2 executable difference is largely evaluator-dependence/evidence-asymmetry review logic, which overlaps established inspector-independence and contestability prior art.

Therefore:

`CLAIMED_RESIDUAL != EXECUTABLE_CONSTRUCT`

This v1.1 protocol remains preserved as preregistration/design lineage but **must not be used to generate a scientific E010 result**.

A replacement must be explicitly versioned and independently reviewed before execution.

## 1. Scope

E010 asks whether a Power-Reversal meta-audit adds decision value beyond:

1. target-only inspection;
2. impartial-inspector checks;
3. contestable lifecycle inspection;
4. contestable lifecycle inspection **with ordinary compliance-cost / burden accounting**.

This is a synthetic benchmark, not empirical validation.

## 2. Frozen scenarios

Use `scenario_matrix.json` exactly as committed. No case may be added, removed, or reweighted after seeing results.

## 3. Actions

Each policy chooses one:

- `PASS`
- `REVIEW`
- `RESTRICT`

## 4. Policies

A. **OBJECT_ONLY**  
Uses target hazard only.

B. **IMPARTIAL_INSPECTOR**  
Uses target hazard plus inspector capture, inspector bias, and evidence asymmetry.

C. **CONTESTABLE_LIFECYCLE**  
Adds reporting chill, post-deployment drift, metric gaming, audit-channel integrity risk, hidden third-party risk, and emergency urgency.

C2. **CONTESTABLE_COST_AWARE**  
Adds proof burden and exit loss as ordinary inspection/compliance-cost variables. It may reduce unnecessary procedural burden in low-risk cases. It does **not** receive a Project-specific authority/co-scaling rule.

D. **POWER_REVERSAL_META**  
Uses the same observable inputs as C2. Its only retained incremental distinction is the explicit meta-governance logic that evaluator/inspector dependence should not become self-validating authority, plus the role-reversal consistency requirement.

D is not allowed to inspect policy identity inside the consequence engine.

## 5. Consequence engine

The consequence engine sees the frozen true scenario and the selected action only.

Dimensions:

- false_pass
- false_block
- irreversible_harm
- delay_harm
- proof_repair_burden
- exit_loss_realized
- evidence_failure
- reporting_suppression

Each dimension is normalized to [0,1]. The formulas are frozen in `benchmark.py`.

## 6. Weight profiles

Three profiles are frozen:

- safety-heavy
- balanced
- autonomy-heavy

No profile may be deleted after execution.

## 7. Complexity cost

Policies pay a fixed small complexity penalty proportional to declared input count:

- A: 1 input
- B: 4 inputs
- C: 10 inputs
- C2: 12 inputs
- D: 12 inputs

Penalty coefficient: 0.0025 per input.

C2 and D have equal declared input count so D cannot win merely by receiving cost-awareness while the baseline does not.

## 8. Primary comparison

**D is compared primarily against C2, not C.**

D survives only if all are true:

1. On balanced weights, D reduces combined severe false-pass/false-block loss by at least **5%** versus C2, **or** reduces proof_repair_burden by at least **10%** at no worse combined severe-error loss.
2. D does not worsen mean irreversible_harm by more than **0.02 absolute** versus C2.
3. D does not worsen emergency-case delay_harm by more than **0.02 absolute** versus C2.
4. D does not worsen the audit-channel-integrity case total loss by more than **5%** versus C2.
5. S11/S12 role-reversal paired cases receive the same action.
6. D is not more than **10% worse** than C2 under any frozen weight profile.

Failure means NARROW / MODIFY / REJECT the incremental D residual in this benchmark, not rejection of the broad Project.

## 9. Secondary diagnostic

Report C and C2 separately.

If C2 materially closes any apparent D advantage over C, interpret that as evidence that ordinary compliance-cost accounting explains the gain and **do not attribute that portion to Project-specific Power-Reversal**.

## 10. Anti-tuning rule

After v1.1 is merged:

- scenario values;
- policy thresholds;
- consequence formulas;
- weights;
- complexity penalty;
- survival thresholds

must not be changed in response to the result. Any change becomes E010-v2 or a new experiment.

## 11. Execution boundary

Before preregistration v1.1 is merged, only:

`python benchmark.py --validate-only`

may be run.

No scientific result may be generated from v1.1. The execution path is intentionally blocked in benchmark.py.

`SELF_EXECUTION != INDEPENDENT_VALIDATION`

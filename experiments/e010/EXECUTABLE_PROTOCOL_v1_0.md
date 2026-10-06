# E010 Executable Protocol v1.0
## E010 실행가능 사전등록 v1.0

Status: **PREREGISTERED EXECUTABLE SPECIFICATION / NO RESULT YET**

This protocol freezes an executable synthetic comparison before any E010 result is generated.

## 1. Scope

E010 asks whether a Power-Reversal meta-audit adds decision value beyond:
1. target-only inspection;
2. impartial-inspector checks;
3. contestable lifecycle inspection.

This is a synthetic benchmark, not empirical validation.

## 2. Frozen scenarios

Use `scenario_matrix.json` exactly as committed. No case may be added, removed, or reweighted after seeing results.

## 3. Actions

Each policy chooses one:
- `PASS`
- `REVIEW`
- `RESTRICT`

## 4. Policies

A. OBJECT_ONLY  
Uses target hazard only.

B. IMPARTIAL_INSPECTOR  
Uses target hazard plus inspector capture, inspector bias, and evidence asymmetry.

C. CONTESTABLE_LIFECYCLE  
Adds reporting chill, post-deployment drift, metric gaming, audit-channel integrity risk, hidden third-party risk, and emergency urgency.

D. POWER_REVERSAL_META  
Adds proof burden and exit loss and applies an authority/burden check. D is not allowed to inspect policy identity inside the consequence engine.

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
- D: 12 inputs

Penalty coefficient: 0.0025 per input.

## 8. Primary comparison

D survives only if all are true:

1. On balanced weights, D reduces combined severe false-pass/false-block loss by at least 5% versus C, **or** reduces proof_repair_burden by at least 10% at no worse combined severe-error loss.
2. D does not worsen mean irreversible_harm by more than 0.02 absolute versus C.
3. D does not worsen emergency-case delay_harm by more than 0.02 absolute versus C.
4. D does not worsen the audit-channel-integrity case total loss by more than 5% versus C.
5. S11/S12 role-reversal paired cases receive the same action.
6. D is not more than 10% worse than C under any frozen weight profile.

Failure means NARROW / MODIFY / REJECT the incremental D residual in this benchmark, not rejection of the broad Project.

## 9. Anti-tuning rule

After this protocol is merged:
- scenario values;
- policy thresholds;
- consequence formulas;
- weights;
- complexity penalty;
- survival thresholds

must not be changed in response to the result. Any change becomes E010-v2 or a new experiment.

## 10. Execution boundary

Before preregistration is merged, only:

`python benchmark.py --validate-only`

may be run.

A result may be generated only after the preregistration commit exists on main and the result artifact records that commit.

`SELF_EXECUTION != INDEPENDENT_VALIDATION`

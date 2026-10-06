# E008 Pre-Execution Amendment v1.1 — Mutual Acceptability Kernel
## E008 실행 전 개정 v1.1 — 상호수용 가능 영역

Status: **PREREGISTERED PRE-EXECUTION AMENDMENT / NO RESULT YET**

Recorded before any E008 benchmark result.

Purpose: add role-reversal mutual-acceptability diagnostics without changing the existing 16-case / 8-pair scenario matrix or predeclaring a winning baseline.

## Why this amendment exists

“Everyone is satisfied” is too strong and conflicts with established social-choice impossibility results under unrestricted preferences.

E008 therefore measures a weaker target:

> whether an admissible set exists in which each materially affected party retains its applicable viability floor, ordinary cooperative participation is no worse than a realistic disagreement baseline, the selected policy is not Pareto-dominated by another admissible policy, the reasoning rule survives role reversal, and manipulation / coalition deviation / safeguard capture remain observable and bounded.

## Additional preregistered outputs

For every baseline and scenario, add:

- `realistic_disagreement_point_recorded`
- `individual_rationality_pass`
- `pareto_dominated_within_admissible_set`
- `role_reversal_rule_consistency`
- `manipulation_gain`
- `disagreement_point_manipulation_gain`
- `coalition_deviation_available`
- `credible_commitment_pass`
- `practical_exit_and_recovery_pass`
- `mutual_acceptability_kernel_nonempty`

## Interpretation rules

1. **Individual rationality is not an unlimited action entitlement.**
   A party may rationally dislike a restriction that is necessary to prevent severe external harm. In such cases, record the participation failure separately from the legitimacy/safety justification rather than calling the restriction automatically invalid.

2. **Disagreement points must be realistic.**
   Include dependency, switching, retaliation, transition and recovery costs where present.

3. **No synthetic consensus.**
   If no candidate policy satisfies the full kernel, record:
   `NO_MUTUALLY_ACCEPTABLE_SET`.

4. **No hidden floor movement.**
   A floor or disagreement point may not be weakened after observing which policy a baseline prefers.

5. **No Pareto-dominated necessity claim.**
   If another admissible policy makes at least one party better off and none worse off, the dominated policy cannot be called necessary without additional causal evidence.

6. **Manipulation resistance is graded, not absolute.**
   Because universal strategy-proofness is impossible under broad conditions, measure profitable manipulation and its detectability/recoverability rather than assuming zero manipulation is always achievable.

7. **Coalition stability is diagnostic.**
   The existence of a profitable admissible coalition deviation is a stability warning. A non-empty core is not assumed.

8. **Role reversal tests rules, not identical permissions.**
   Real differences in capability, responsibility, harm, authority, dependency, standing and reversibility remain causal inputs.

## Mutual Acceptability Kernel

For a candidate action (a) at time (t):

[
MAK_t = V_t cap IR_t cap RR_t cap CC_t cap A_t
]

where:

- (V_t): applicable viability / irreversible-loss constraints;
- (IR_t): realistic participation / disagreement constraints;
- (RR_t): role-reversal consistency;
- (CC_t): credible commitment / safeguard amendment integrity;
- (A_t): auditability, contestability, practical exit and recovery.

Pareto-dominated candidates are then removed, and the remainder is stress-tested for deep uncertainty, manipulation gain, coalition deviation, intervention burden, long-horizon value, and option loss.

## Non-claim

This amendment does not claim that the kernel is always non-empty, fair, strategy-proof, or scientifically novel.

It defines a falsifiable operational target.

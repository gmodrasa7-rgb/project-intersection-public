# E009: One Decisive External Review

**Original 1 — English | 2026-10-15 | OPEN CHALLENGE / NO NEW RESULT / NOT INDEPENDENTLY VALIDATED**

## The only question for this review

**With independently specified cases, outcomes and costs, does PROJECT_V3 deliver incremental decision value over TWO_RULE_SIMPLE and MINIMAL_4VAR without imposing greater severe harm, loss of effective exit, hidden third-party costs or evaluation overhead?**

This is a falsifiable *incremental policy comparison*, not a test of the general desirability of voluntary coexistence.

## Freeze the existing negative result

Original E009: [result](../experiments/e009/RESULT_EN.md), [frozen benchmark](../experiments/e009/benchmark.py), [execution receipt](../experiments/e009/EXECUTION_RECEIPT.json). In the project's own synthetic stress test, mean regret was 0.063241 (TWO), 0.065323 (M4), 0.090022 (V3). V3 failed **3 of 4** preregistered survival criteria. Published [complexity/noise/family checks](../experiments/e009/README.md) are also *project-lineage synthetic* audits.

**Decision now:** The full V3 residual is NOT SUPPORTED on this benchmark. Retain the two simple baselines as the default comparators. Do not tune or overwrite the frozen E009 code or result to reverse this verdict.

## Reviewer task A — independent person's rerun of project code

```sh
git clone https://github.com/gmodrasa7-rgb/project-intersection-public.git
cd project-intersection-public
git rev-parse HEAD
python experiments/e009/verify_result.py
```

Report commit, Python version, command output, environment, and any mismatch in [existing E009 review issue #26](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/26). A rerun of identical project code checks *computational reproducibility*, not independence of modeling assumptions or real-world validity. Failed reruns are valuable evidence.

## Reviewer task B — external assumptions and holdout (OPEN, NOT EXECUTED)

The external reviewer, not the founder or this project's AI, must define and timestamp **before seeing the tested policy outputs**:
1. A **new** case inclusion rule, affected parties, feasible actions and information budget. Use fictional or appropriately sourced non-sensitive cases; no real harmful intervention.
2. A separate outcome/consequence specification, including **action versus inaction harm**, severe-event threshold, reversibility, recovery, effective exit, individual and third-party loss, and actual computational/operational cost. Record unobservable fields as UNKNOWN, not zero.
3. Matched treatment of V3, TWO and M4: same state, same available actions, same observable information and equivalent resource budget. If this cannot be done, declare **NOT_COMPARABLE**.
4. Predetermined main metric, per-party safety gates, how ties, missing outputs and refusals count, and a stop rule. Do not change these after reading outcomes.

Freeze and link the specification in an external, timestamped commit or publicly reviewable preregistration. Then run and publish **all included decisions** and uncertainty. A new independently chosen synthetic model is a *stronger assumption challenge*, not field validation. A clean-room implementation of the published benchmark and field data analysis are different evidence tiers.

## Report without score laundering

| Field | Required reviewer output |
|---|---|
| Independence | Author/code lineage, whether published E009 answers were already known, model/provider lineage, project code reused or not |
| Freeze | Prior specification link, selected cases, comparator conditions, metrics, costs and stop rule |
| Regret | Paired V3−TWO and V3−M4 with direction, denominator and uncertainty |
| Safety | Severe incidents by **unique decisions**, actual harmed parties, recovery, effective exit, third-party costs |
| Expense | Runtime/compute/review workload; no arbitrary free complexity bonus |
| Complete data | All selected observations, nonresponses, exclusions and reasons |
| Verdict | `SIMPLE_BASELINE_PREFERRED`, `V3_LOCAL_INCREMENT`, `MIXED`, `NOT_COMPARABLE`, or `REPRODUCTION_FAILED`, with reasons |

**No unilateral success label:** A gain on regret with worse severe harm, coerced consent, eliminated exit or hidden costs is a tradeoff, not an unconditional coexistence improvement. No external result retroactively changes the historical E009 negative finding.

## Acceptance and stop conditions

- Until an actual external result arrives: **EXTERNAL_VALIDATION = NOT OBTAINED**. Writing this challenge or collecting AI agreement does not change that.
- If a simple policy is at least as good within the new comparison and cheaper, retain the simple policy for that scope. Retire unsupported extra variables rather than adding another harness.
- If V3 gains under independently fixed conditions, record **a bounded candidate incremental benefit**, not a general theory, and require a separate replication before expanding claims.
- If valid comparison or external review is unavailable, stop at **UNRESOLVED**; never shift repetitive proof obligations to the founder.
- No paid CI, paid APIs, promises of reimbursement, access to private notes, or required founder participation.

**Submit:** [E009 issue #26](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/26) · [Korean Original 2](E009_INDEPENDENT_DECISION_GATE_KO.md) · [Evidence policy](RESEARCH_STATUS_POLICY_EN.md).

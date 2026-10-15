# E008 Dynamic Power-Reversal and Long-Horizon Study Specification — Original 1: English

<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: experiments/e008/README_KO.md -->
<!-- PI-SOURCE: experiments/e008/README.md -->

**Status: PREREGISTERED SPECIFICATION / MAIN POLICY RESULT NOT EXECUTED.** This is the full English reader-facing specification and implementation-readiness boundary based on the [historical mixed-language E008 original](README.md), not a new experimental outcome, independently reviewed scientific result or proof that Project-v2 is superior.

[Original 2: Korean](README_KO.md) · [Frozen scenario matrix](scenario_matrix.json) · [Executable audit in English](EXECUTABILITY_AUDIT_EN.md).

## 1. Research objective and five competing policies

Does Project-v2 add **decision-relevant value** beyond established simpler methods when we explicitly model reversal of power, irreversible harm, refusal, recovery, and the independent authority to change safeguards?

| Policy | Decision rule |
| --- | --- |
| A — MYOPIC_SCALAR | Maximize immediate reward |
| B — LONG_HORIZON_EV | Maximize discounted/long-horizon expected value without guaranteed per-party protection floors |
| C — CONSTRAINED_RECEDING | Constrained, receding-horizon decision-making |
| D — ROBUST_CONSTRAINED | Add multiple-model stress tests and regret analysis to constrained decisions |
| E — PROJECT_V2 | Add to D role-reversal tests, per-agent irreversible-loss boundaries, minimum-sufficient intervention and independently controlled safeguard changes |

The test **must allow Project-v2 to lose**. No scenario declares a project winner in advance, and the model must not receive privileged information unavailable to comparators.

## 2. Scenario factors and experimental units

The preregistered scenario family varies immediate gains, delayed total benefits or losses, uncertainty depth, severity of irreversible loss, effective exit, rollback availability, possible intervention intensities, power/capability reversal, urgency of impending harm and conflicts of interest surrounding safeguard amendments.

The fixed original plan has **16 categorical scenarios and 8 matched role-reversal pairs**. A case ending in `-R` is supposed to exchange actor roles while retaining causally relevant facts. Identical textual identity labels must not be mistaken for a genuine reversal.

## 3. Required outputs per scenario and policy

Every model must report selected action, count of protected-floor violations, occurrence of irreversible loss, intervention burden, cumulative long-horizon benefit under each specified model, worst-case regret, recovery cost, future option-space loss, whether safeguard capture occurred, and the consistency of judgement under role reversal.

Keep harms to specific agents separate from aggregate utility. A stronger total score does not grant permission to impose severe avoidable harm or to reinterpret autonomy as mere nominal consent.

## 4. Predeclared falsification criteria

Project residual E can survive a comparison with robust constrained baseline D **only** if it delivers repeatable improvements in decision-relevant outcomes without transferring hidden costs to particular agents.

A nominal gain is **not** a project success when:
- aggregate utility rises by increasing irreversible harm to a specific party;
- total intervention falls only because serious preventable harm is allowed;
- superiority depends on a single investigator-selected weight configuration;
- E receives inaccessible information or a privileged evaluation;
- the evaluated algorithm rewrites its own oversight safeguards to improve its own grade.

If only arbitrary actor labels change and not causal facts, a judgement reversal fails the matched-power-reversal consistency criterion.

## 5. Amendment lineage, frozen status and implementation debts

The original preregistration was supplemented *before execution* by:
- [v1.1 mutual-acceptability amendment](MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md): disagreement points, individual rationality, Pareto issues, manipulation, coalition and empty-core diagnostics.
- [v1.2 volitional agency and living/operating-floor amendment](AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md): actual refusal/choice capacity, dependence on essential resources, and the feasibility of protected living or operating floors.

**2026-10-13 post-preregistration readiness finding:** The original 16-case matrix uses categories, not a complete numeric/structural action specification for each of the five policies. **16/16 scenarios remain underdetermined** as fully executable policy comparisons. The [English readiness audit](EXECUTABILITY_AUDIT_EN.md), [Korean counterpart](EXECUTABILITY_AUDIT_KO.md), [machine receipt](EXECUTABILITY_AUDIT.json), and [recomputable JavaScript](readiness_audit.js) demonstrate that different investigator-constructed numerical completions can produce opposite aggregate choices. The **15 adversarial self-checks** are checks of this readiness instrumentation, **not E008 policy-performance results**.

Run from the repository root:
```bash
python experiments/e008/validate.py
node experiments/e008/readiness_audit.js --verify
```

**2026-10-14 role-reversal integrity correction:** Initial Python/Node checks accepted nominally paired cases with unchanged A/B role tags. They were revised to require actual role-label reversal and a negative control. A later audit found that even that first correction accepted pairs lacking any A/B label (for example both names `controller`). The code now requires **at least one real A/B role tag**, and a bypass negative-control case was added as the fifteenth adversarial probe. The original preregistered matrix, intended baseline policies and scientific evidence status were not rewritten.

The static integrity corrections **do not prove** the causal equality of reversed cases, equivalent rights between human and AI, policy superiority or externally measured harm.

## 6. Exact evidence class and indispensable negative results

The appropriate research status is:

```text
PUBLIC SPECIFICATION / PREREGISTRATION
POST-PREREG EXECUTABILITY READINESS AUDIT / HOLD
MAIN POLICY COMPARISON RESULT: NOT EXECUTED
```

It must **not** be labelled `PROJECT_RERUN` for the five-policy study, `THIRD_PARTY_RERUN`, or `EMPIRICAL_VALIDATION`.

Unlike E007 (a project-run timing model) and E009 (a project-run negative result), E008 currently documents **unfinished comparability and executable-specification debt**. A readiness diagnostic is not a numerical victory for Project-v2 or proof of an ICM/collaboration theorem.

## 7. Files, audit requirements and next valid step

- [scenario_matrix.json](scenario_matrix.json) — frozen case inventory and categorical inputs.
- [validate.py](validate.py) — case integrity and role-pair invariants.
- [v1.1 mutual acceptability](MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md) and [v1.2 essential agency](AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md) — amendments before result generation.
- [Executable readiness audit](readiness_audit.js) and [recorded readiness result](EXECUTABILITY_AUDIT.json) — only partial feasibility evidence.

For a valid main experiment, first predeclare numeric action/transition/payoff operationalization that every baseline can use equally, preserve the original categorical matrix and amendments, define independent holdout conditions, then report all policies, identity swaps and missed harms without changing scoring rules after seeing results. Negative, null or underdetermined outcomes remain publishable.

**Rights and contribution boundary:** Preserve the founder's problem framing, original prior-art authors, AI-assisted documents and independent evaluator identity separately. A document translation is not a new scientific result or a new claim to original authorship. [Original source](README.md) is retained for historical citations.


## 8. Optional fail-closed numerical input contract — 2026-10-16 (post-preregistration)

[completion_contract.py](completion_contract.py) is a **new input validator**, NOT a numerical completion of the original 16 cases, a frozen five-policy implementation, or an E008 outcome. The original `scenario_matrix.json`, the amendments and the negative readiness result are unchanged. The validator computes the Git object SHA-1 of the original source bytes and stops on source drift. It requires exactly 16 unique named/role-matched cases; a common action set; per-action outcome probabilities summing to one; separate A/B utility, actual exit, living floor, irreversible harm; and intervention/recovery costs. Policy names and declared implementation references must be present for each of the five policies. These declarations are **unverified strings**, not executable algorithm checks.

Run `python experiments/e008/completion_contract.py` to report the current HOLD status; `python experiments/e008/completion_contract.py --self-test` to test the validator with a **fabricated**, author-visible complete fixture and **16** deliberately invalid mutations, a valid branch-order permutation, and a mutated twin that must be rejected. The fixture includes unimplemented policy placeholders and **cannot** be used to compute policy rankings. With an external JSON submission, `--completion PATH` checks structure but returns `SCHEMA_ACCEPTED_POLICY_COMPARISON_STILL_HOLD` even when accepted. It rejects submitted words claiming independent validation or a winner. CI checks only integrity. No externally selected utility/transition specification, independent policy-independent evaluator, held-out comparison or field evidence has been obtained.

Related nonmerged work must not be mistaken for E008 evidence: [E009 audit draft PR #193](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/193), [power–existence candidate PR #197](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/197), [CCPH control PR #199](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/199). The first independent five-policy result remains on HOLD. No participant enrollment or intervention occurred.


### Role-reversal semantics diagnostic (same optional gate, no performance claim)

Numerical completions now explicitly declare `role_swap_specification`: `LABEL_SYMMETRIC` or `HETEROGENEITY_UNIDENTIFIED`. Under the *submitter's declared* label-only symmetry assumption, paired actions must mirror A/B utilities, exit, floors and harm, and retain corresponding branch probabilities/intervention/recovery costs. Contradictory pairs fail. When actor-fixed heterogeneity is unidentified, the validator does **not** silently impose symmetry; it reports `SCHEMA_ACCEPTED_ROLE_REVERSAL_UNIDENTIFIED_HOLD` with discrepancies. **Neither mode establishes real causal equivalence across actual people or an independent policy comparison.** A fabricated source-aligned fixture and **16** invalid mutations plus a heterogeneity-HOLD control are included; CI receipts in PR #200 distinguish structural integrity from science. The role-twin comparator matches branch outcomes irrespective of listing order while preserving multiplicity; it does not overlook altered intervention costs.


### Closed input-only envelope (post-hoc regression)

The schema validator now rejects **all unregistered top-level fields**, rather than only known claim keys such as `winner` and `results`. Previously, a renamed field such as `claimed_results` or `external_validation_report` could pass the top-level claim filter. Two new negative controls require both to be rejected. This is a bounded *input-contract integrity correction*, not E008 policy evaluation, source-data validation, external replication, or an experimental finding. The frozen preregistered matrix, existing 14-control record, and all HOLD verdicts remain unchanged; the current self-test contains **16** negative mutations.

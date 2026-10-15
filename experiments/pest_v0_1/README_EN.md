<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: experiments/pest_v0_1/README_KO.md -->
# PEST-v0.1 — Power–Existence Separation Test (design skeleton)

**Status: CANDIDATE / NOT FROZEN / NOT EXECUTED AS A RESEARCH RESULT.**  
**Date:** 2026-10-16 | [Amendment proposal](../../research/POWER_EXISTENCE_SEPARATION_AMENDMENT_v0_1_EN.md) | [Korean](README_KO.md).

## Question and identification

Does protecting a potential suppressor's own continued existence (`XG_j`) reduce its willingness to restrict a growing target (`i`)? Is this different from protecting the target (`XG_i`)? The initial proposed `H_target: d PSI / d XG_i < 0` is retained and challenged by `H_actor: d PSI / d XG_j < 0`. Both can fail. In the absence of exogenous variation or a credible counterfactual, an observed correlation is not causal proof.

The **unit of analysis** is a fixed world/mechanism × `PT_i` × `PT_j` × suppressor identity × guarantee assignment. An A/B name-swap with fixed role parameters is only a **label-invariance control**. The additional actor-fixed reversal swaps which named actor is suppressor while preserving each actor's original PT and XG; the two checks must not be conflated. Risk-management measures protecting third parties are not coded as growth-suppression actions without evidence of their purpose and alternatives.

## Locked-in design candidate (lock only after review and merging)

- 3 rival synthetic mechanisms: `survival_fear` (own protection may reduce PSI), `capture_opportunity` (target protection may increase nonlethal PSI), and `backlash` (own protection may increase PSI).
- `PT_i`, `PT_j` each at 0.25 or 0.75 (fully crossed), two A/B role assignments.
- Four guarantee assignments: R1 both high; R2 both low; R3 target only; R4 suppressor only. **3 × 2 × 2 × 2 × 4 = 96 cells**.
- `PSI = max(0, U_suppress_growth - U_cooperate)` in normalized, synthetic payoff units. No sampled behavior is measured. Distinguish `PSI=0` due to the clamp from missing evidence. Raw signed margin is available through `utility_margin`.
- Joint failure: `PSI(R1) >= PSI(R2) - 0.03`; individual recipient contrasts reported separately. `0.03` is **not** an empirical effect-size threshold.
- Report results by mechanism and transferability setting, including opposite-sign, zero, floor/exit breach, identity swap, and missed-risk cases; do not collapse all worlds into an overall success score.
- A nonempty MAK++ is **not** established by this code. It implements only an explicit floor/exit screening proxy and role-label invariance.

### Interpretation safeguards (post-hoc design audit; not a new result)

The 96 formal cells contain **48 distinct numerical model states** if the identity label is ignored. Same-PT A/B swaps duplicate the same role-based deterministic formula; this is a label-invariance smoke test, **not 96 independent observations or a demonstrated reversal of real actors' incentives**. The separate `actor_fixed_role_reversals` routine pairs 48 reciprocal PT/XG assignments (relative to the named actors), but this is still synthetic model comparison. It now rejects unmatched pre-treatment covariates in those pairs, rather than passing confounded context shifts as actor-fixed role effects; post-treatment floor and exit scores need not match. The 24 paired contrast rows contain 12 distinct mechanism/PT settings repeated under A/B labels.

The original `XG_ALONE_INEFFECTIVE` threshold flag is **retained unchanged**. When both the untreated and protected `PSI` equal zero, that flag is also true even though there was no positive suppression incentive to reduce at baseline. Such cells require a separate `both_at_zero_floor` interpretation, not an empirical claim of failed protection. The diagnostic now also returns `baseline_psi`, `treated_psi` and `raw_joint_margin_difference` to expose clipping by `max(0, raw_margin)`. For example, in `survival_fear` at `PT_i = PT_j = 0.25`, both clipped scores are zero while the raw margin changes by −0.133875. Neither raw margin nor clipped score measures observed behavior.

## Validity repairs — policy versus set and role reversal

- **No false empty-set verdict:** `floor_exit_gate(case)` screens the necessary living/exit floors for one *candidate policy* and returns `FLOOR_EXIT_PASS` or `FLOOR_EXIT_FAIL`. One rejected policy is not an empty mutual-acceptability kernel.
- `candidate_set_status(candidates, exhaustive=True)` reports `CONDITIONAL_EMPTY_IF_SCOPE_COMPLETE` when **every supplied candidate fails a necessary floor/exit condition**. The flag is only a caller assertion, not an independently verified completeness certificate: an unlisted viable option can overturn the apparent empty set. With unknown coverage report `UNRESOLVED_ACTION_COVERAGE`. One survivor requires full MAK++ review and does **not** prove acceptability. Never automatically upgrade the conditional status to `NO_MUTUALLY_ACCEPTABLE_SET`.
- Exact 96 frozen treatment coordinates must match the predeclared PT/XG grid. Replacing a PT level with an unregistered value while preserving row count is rejected.
- `actor_fixed_role_reversals` creates **48 actor-fixed reciprocal pairs**, swapping relative PT and XG when A and B exchange suppressor/target roles. It records those pairs; it does not assume equal outcomes or certify higher-order rule consistency. Simple A/B label symmetry alone is insufficient.
- The world-specific payoff equations are synthetic and deliberately sign-selecting; tests prove only instrumentation behavior, not empirical support for either guarantee hypothesis.

### Choice-set coverage is an assumption, not an observation

A finite list of tested actions is not automatically the full feasible action set. A caller setting `exhaustive=True` does not supply an independent audit of unobserved alternatives. The resulting `CONDITIONAL_EMPTY_IF_SCOPE_COMPLETE` is therefore **a conditional inference**, not a proven universal impossibility. This fail-closed distinction follows the general open-world caution in the [W3C OWL 2 Primer](https://www.w3.org/TR/owl-primer/) and is related to the distinction between evidence and maintained assumptions in [Manski (2005), *Partial identification with missing data*](https://doi.org/10.1016/j.ijar.2004.10.006). Those works are prior-art analogies, not project empirical validation.

### Necessary-condition visibility across all four guarantee assignments

The design-only `paired_contrasts()` now carries `floor_exit_screens` for **R1, R2, R3 and R4**, using the existing `floor_exit_gate()` and the same matched world/PT/actor cells. These screens are reported **separately** from suppression-incentive changes; neither screen passing nor a negative PSI contrast certifies MAK++ or real-world welfare.

Adversarial software test: in the two A/B label-twin `survival_fear` cells at `PT_i=PT_j=0.75`, lower R1's post-treatment `floor_after` to 0.10, below the pre-existing minimum 0.50. R2 PSI is 0.24175 and R1 PSI is zero; the favorable contrast **must** co-appear with `R1_BOTH_PROTECTED=FLOOR_EXIT_FAIL` and `R2_NEITHER_PROTECTED=FLOOR_EXIT_PASS`. This is a **constructed negative control**, not evidence that a real existence guarantee causes livelihood loss. All other tests, historical experiment conclusions, and the `--execute` HOLD are unchanged.

### Independent prior-art comparator: commitment without containment (2026)

**External evidence, not a PEST result:** [Lu Dong and Lingbo Huang (2026), *Curtailed ambition: Endogenous power shift and preventive war*, *Journal of Economic Behavior & Organization* 242, 107413](https://doi.org/10.1016/j.jebo.2026.107413) experimentally compare growth self-containment with binding future-payoff commitments that leave the power shift intact. They report that both can reduce preventive conflict but rising actors adopt self-containment less readily; declining actors sometimes pay for coercive containment instead of trusting voluntary restraint. Their additional survey informs perceived plausibility, **not actual cross-country causal effects**. Earlier [Abbink, Dong and Huang (2023)](https://doi.org/10.1016/j.geb.2023.08.018) tested preventive conflict with power shifts and commitment.

**Material rival explanation:** Reduced preemptive suppression may arise from credible future benefit allocation **without a guarantee of the declining actor's physical/operational existence**, and without arresting the rising actor's development. This is different from the present PEST `XG_i/XG_j` intervention. Conversely, an offered but unenforceable promise might not reduce conflict. The 2026 experiment makes commitment enforceable **inside its bargaining game**; this assumption is not an observation of real-world enforceability.

| Successor intervention or comparator | Manipulation to isolate | Must not be silently relabeled |
| --- | --- | --- |
| Existence assurance | Independently vary protection of each actor's continued existence | Binding future benefit transfer |
| Credible future allocation | Guarantee a future distribution while leaving power growth unconstrained | Existence guarantee |
| Voluntary containment | Rising actor chooses to restrict own development | Costless mutual cooperation |
| Coercive containment | Incumbent forcibly restricts rival development, with cost to both | Voluntary consent or free security |

**Discriminating successor test, not executed:** Independently manipulate existence assurance, enforceable allocation, and available growth-restraint options. Separate random *policy availability/assignment* from *actual adoption*; report both rather than interpreting self-selection as the treatment effect. Hold baseline stakes, power-shift timing and information comparable. Predeclare conflict/suppression, each actor's retained future options, payoff, effective exit, credibility/enforcement cost, and third-party loss; use the same measures under actor-fixed power reversal. Test whether XG adds incremental value after credible allocation is provided. If credible allocation alone performs as well, reject the claim that an XG-specific mechanism was identified.

**Stop/lineage:** This is a proposed external-comparator design only; `pest.py` has no allocation, adoption, or coerced-containment treatment variables, and no data from the cited paper have been analyzed by this project here. The authors' [public replication-data link](https://lingbohuang.com/uploads/2026-preventive-war-endo-software-data.zip) was identified but **not fetched, inspected or rerun**. Do not import the paper's observed effects as synthetic PEST outputs, retrofit the 96-cell design, or promote this note to field validation.

## Execution gate

These run **schema and adversarial smoke tests only**, not preregistered results:

```bash
python experiments/pest_v0_1/pest.py --validate-only
python -m unittest discover -s experiments/pest_v0_1 -p 'test_*.py' -v
```

`python experiments/pest_v0_1/pest.py --execute` deliberately fails. After code review, freeze the exact main-branch commit, policy-independent consequence engine, case grid, thresholds, effect aggregation, statistical plan, missingness handling and evidence/author lineage **before** any result generation. Only then introduce a versioned executor and independent holdout implementation. Never silently overwrite the existing experiment or its result.

**No retroactive downgrade:** E007/E009/PICB-v1 lack this XG/PT distinction but retain their historical result classifications. E008 policy-performance comparison remains unexecuted.

**Attribution:** Core separation and original amendment candidate: Project Intersection human founder. Causal split, synthetic counterexample worlds, code and tests: AI-assisted implementation. Neither role claims independent empirical validation or ownership of adjacent prior research.

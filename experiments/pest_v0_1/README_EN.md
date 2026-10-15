<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: experiments/pest_v0_1/README_KO.md -->
# PEST-v0.1 — Power–Existence Separation Test (design skeleton)

**Status: CANDIDATE / NOT FROZEN / NOT EXECUTED AS A RESEARCH RESULT.**  
**Date:** 2026-10-16 | [Amendment proposal](../../research/POWER_EXISTENCE_SEPARATION_AMENDMENT_v0_1_EN.md) | [Korean](README_KO.md).

## Question and identification

Does protecting a potential suppressor's own continued existence (`XG_j`) reduce its willingness to restrict a growing target (`i`)? Is this different from protecting the target (`XG_i`)? The initial proposed `H_target: d PSI / d XG_i < 0` is retained and challenged by `H_actor: d PSI / d XG_j < 0`. Both can fail. In the absence of exogenous variation or a credible counterfactual, an observed correlation is not causal proof.

The **unit of analysis** is a fixed world/mechanism × `PT_i` × `PT_j` × suppressor identity × guarantee assignment. Powers change owners under A/B reversal while role-specific parameters remain fixed. Risk-management measures protecting third parties are not coded as growth-suppression actions without evidence of their purpose and alternatives.

## Locked-in design candidate (lock only after review and merging)

- 3 rival synthetic mechanisms: `survival_fear` (own protection may reduce PSI), `capture_opportunity` (target protection may increase nonlethal PSI), and `backlash` (own protection may increase PSI).
- `PT_i`, `PT_j` each at 0.25 or 0.75 (fully crossed), two A/B role assignments.
- Four guarantee assignments: R1 both high; R2 both low; R3 target only; R4 suppressor only. **3 × 2 × 2 × 2 × 4 = 96 cells**.
- `PSI = max(0, U_suppress_growth - U_cooperate)` in normalized, synthetic payoff units. No sampled behavior is measured. Distinguish `PSI=0` due to the clamp from missing evidence. Raw signed margin is available through `utility_margin`.
- Joint failure: `PSI(R1) >= PSI(R2) - 0.03`; individual recipient contrasts reported separately. `0.03` is **not** an empirical effect-size threshold.
- Report results by mechanism and transferability setting, including opposite-sign, zero, floor/exit breach, identity swap, and missed-risk cases; do not collapse all worlds into an overall success score.
- A nonempty MAK++ is **not** established by this code. It implements only an explicit floor/exit screening proxy and role-label invariance.

## Execution gate

These run **schema and adversarial smoke tests only**, not preregistered results:

```bash
python experiments/pest_v0_1/pest.py --validate-only
python -m unittest discover -s experiments/pest_v0_1 -p 'test_*.py' -v
```

`python experiments/pest_v0_1/pest.py --execute` deliberately fails. After code review, freeze the exact main-branch commit, policy-independent consequence engine, case grid, thresholds, effect aggregation, statistical plan, missingness handling and evidence/author lineage **before** any result generation. Only then introduce a versioned executor and independent holdout implementation. Never silently overwrite the existing experiment or its result.

**No retroactive downgrade:** E007/E009/PICB-v1 lack this XG/PT distinction but retain their historical result classifications. E008 policy-performance comparison remains unexecuted.

**Attribution:** Core separation and original amendment candidate: Project Intersection human founder. Causal split, synthetic counterexample worlds, code and tests: AI-assisted implementation. Neither role claims independent empirical validation or ownership of adjacent prior research.

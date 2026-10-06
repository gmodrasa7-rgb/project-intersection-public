# E009 Synthetic Result v1.1

Status: **PROJECT RERUN SYNTHETIC RESULT / NOT INDEPENDENT VALIDATION**

Executable-spec commit: `c36ba8e6d6df1eedcd54ca6c36091bf822fe6ace`  
Benchmark blob: `e190d2a2466e44b62752eff6f547eb79bc4c6b7f`  
Benchmark SHA-256: `86b50f9859858f16e57429fbda5bca3306e1680a2be081d16690c6e7776f188a`  
Generated result SHA-256: `6fb5d78ad07c657fb40190d1fc3742ff88cc728ab1fa29ff115b1e7ad34f6bf7`  
Semantic result SHA-256: `62605568254bfcc6cf95da2953f3fe28047263f30b3463ec87dfa4fa6bc75567`

## Primary verdict

`PROJECT_V3_RESIDUAL_SURVIVES = FALSE`

Project-v3 failed 3 of 4 preregistered survival criteria. The full v3 residual should therefore be **reduced/rejected for this synthetic benchmark**, not promoted or tuned in-place.

## Stress-set results

| Policy | Mean regret | Recovery | Severe-harm rate | Exit retention | Competitive loss |
|---|---:|---:|---:|---:|---:|
| TWO_RULE_SIMPLE | 0.063241 | 0.231797 | 0.0312% | 0.828865 | 0.134573 |
| MINIMAL_4VAR | 0.065323 | 0.220303 | 0.0000% | 0.842896 | 0.128967 |
| PROJECT_V3 | 0.090022 | 0.239404 | 1.6562% | 0.835741 | 0.117646 |
| MAK_PLUS_POINTWISE | 0.096127 | 0.254488 | 0.4375% | 0.807327 | 0.135384 |
| SECURITY_BOUNDED | 0.100897 | 0.254119 | 0.0938% | 0.813757 | 0.126954 |

Best mean-regret baseline: `TWO_RULE_SIMPLE` (0.063241). `MINIMAL_4VAR` was close (0.065323). `PROJECT_V3` was 0.090022, which is **42.35% worse than the best simple baseline** under the preregistered regret comparison.

Project-v3 had the lowest competitive-loss metric (0.117646), but this did not compensate for worse regret, recovery cost, and higher severe-harm frequency.

## Survival criteria

- `criterion_no_weight_profile_regret_over_10pct_worse_than_best_simple`: **FALSE**
- `criterion_recovery_no_more_than_2pct_worse_than_best_C_or_M4`: **FALSE**
- `criterion_regret_5pct_better_than_best_simple`: **FALSE**
- `criterion_severe_harm_no_more_than_2pp_worse_than_best_C_or_M4`: **TRUE**
- `project_v3_residual_survives`: **FALSE**

All three preregistered weight profiles were failure profiles for Project-v3 relative to the best simple comparator: safety-heavy, balanced, adaptability-heavy.

## Interpretation

This result supports **simplification**, not expansion. The next candidate should start from `TWO_RULE_SIMPLE` and `MINIMAL_4VAR`, and add only variables that demonstrate held-out incremental value.

The result does **not** show that ENF/ID/OV/CUM are real-world causal variables, does not validate the synthetic weights, and does not falsify the broad Project Intersection research question.

## Evidence boundary

The consequence engine, cases, weights and policies were designed inside the Project. This is therefore a **project rerun of a preregistered synthetic benchmark**, not independent implementation, external replication, or empirical validation.

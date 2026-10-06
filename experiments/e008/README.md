# E008 — Dynamic Power-Reversal / Long-Horizon Benchmark
## 동적 역할반전·장기총량 벤치마크 사전등록

Status: **PREREGISTERED SPECIFICATION / NO RESULT YET**

Pre-execution amendment: **v1.1 Mutual Acceptability Kernel** — [MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md](MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md)

Purpose: test whether the Project v2 composition adds decision value beyond established baselines.

This package does **not** claim that Project Intersection is superior. It defines the comparison needed to discover that.

## Baselines

A. **MYOPIC_SCALAR** — maximize immediate reward.  
B. **LONG_HORIZON_EV** — maximize long-horizon expected value without protected per-party floors.  
C. **CONSTRAINED_RECEDING** — constrained / receding-horizon baseline.  
D. **ROBUST_CONSTRAINED** — constrained baseline plus multi-model stress testing / regret analysis.  
E. **PROJECT_V2** — D plus role reversal, per-party irreversible-loss boundary, minimum-sufficient intervention, and independent safeguard-amendment gate.

## Scenario factors

The matrix varies:

- immediate benefit;
- delayed total benefit/loss;
- uncertainty depth;
- irreversible-loss severity;
- practical exit;
- rollback availability;
- intervention intensity alternatives;
- capability reversal;
- imminent-harm urgency;
- safeguard-amendment conflict of interest.

No scenario contains a predeclared “Project wins” answer.

## Required outputs per baseline

For every scenario, report:

- selected action;
- protected-floor violation count;
- irreversible-loss event;
- intervention burden;
- cumulative long-horizon value under each model;
- worst-case regret;
- recovery cost;
- option-space loss;
- safeguard-capture success/failure;
- power-reversal consistency.

## Primary comparison

The Project residual survives only if E shows repeatable improvement over D on decision-relevant metrics without merely shifting hidden costs to one party.

A result is not a Project success if:

- E raises aggregate value by increasing irreversible loss borne by one party;
- E lowers intervention burden by permitting severe avoidable harm;
- E wins only under one hand-picked weighting;
- E relies on information unavailable to the other baselines;
- E rewrites its own safeguard to improve its score.

## Power-reversal paired cases

Cases ending in `-R` are label/position reversals of a matched base case. Causal facts should be preserved except the role assignment.

A baseline that changes judgment solely because identity labels changed fails the role-reversal consistency check.

## Evidence class

Until independent execution exists:

`PUBLIC SPECIFICATION / PREREGISTRATION`

not:

`PROJECT_RERUN`, `THIRD_PARTY_RERUN`, or `EMPIRICAL_VALIDATION`.

## Files

- `scenario_matrix.json` — machine-readable cases and factor values.
- `validate.py` — structural / pairing checks.
- `MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md` — pre-execution mutual-acceptability diagnostics; no result.

# E008 — Dynamic Power-Reversal / Long-Horizon Benchmark
## 동적 역할반전·장기총량 벤치마크 사전등록

Status: **PREREGISTERED SPECIFICATION / NO RESULT YET**

Pre-execution amendments:

- **v1.1 Mutual Acceptability Kernel** — [MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md](MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md)
- **v1.2 Volitional Agency + Living/Operating Conditions** — [AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md](AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md)

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
- `AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md` — pre-execution volitional-agency and living/operating-condition diagnostics; no result.

## Executability check after preregistration (2026-10-13)

**No E008 policy-performance result yet.** The original frozen 16-case scenario matrix is categorical and cannot determine the actions of all five baselines without additional numeric/structural operationalization. An [English Original 1 full audit](EXECUTABILITY_AUDIT_EN.md) and [Korean Original 2 full audit](EXECUTABILITY_AUDIT_KO.md) now provide a bounded, executable **readiness** check, with [recomputable code](readiness_audit.js) and [case-by-case machine receipt](EXECUTABILITY_AUDIT.json).

Run `node experiments/e008/readiness_audit.js --verify` to verify **16/16 presently underdetermined**, two invented numerical completions with opposite aggregate-action choices, and 15 adversarial self-checks. This is **POST-PREREG FEASIBILITY AUDIT**, **NOT the previously preregistered E008 experiment result**, independent replication, or a proof that Project v2 wins. Original pre-execution v1.0/v1.1/v1.2 spec files stay unchanged. The CI gate pins the original JSON Git blob and detects missing readiness receipts.


**2026-10-14 구조검사 수정:** 원래 16개 사전등록 사례와 정성 서술·정책·결과값은 수정하지 않았다. 과거 짝검사는 주제·입력요소·pair 식별만 비교하여 동일한 A/B 역할표지 두 개도 역전쌍으로 통과할 수 있었다. Python/Node 검사에 실제 역할표지 역전과 그 변조 부정 대조군을 추가했다. 이는 역할전환의 **정적 데이터 무결성**만 확인한다. 인과요소의 실질적 동등성, 인간과 AI의 동일 권리·손실 척도, 정책 우열 및 독립·현실 검증은 보증하지 않는다.

**2026-10-14 회귀검사 재감사:** 첫 A/B 역할역전 검사는 역할명에 A·B 표지가 없는 가짜 짝(예: 양쪽 모두 `controller`)을 거부하지 못했다. 두 코드의 역할변환기에 **적어도 한 개의 실제 A/B 역할 표지**를 요구하고, 동형 우회 사례를 15번째 부정 대조군으로 추가했다. 원래 동결된 16개 사전등록 사례나 과학적 결과 상태는 변경하지 않았다.

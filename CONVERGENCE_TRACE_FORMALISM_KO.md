# Project Intersection — 의도 비의존 수렴 역추적 형식명세 v0.1

Status: FORMALIZATION CANDIDATE / NOT EMPIRICAL VALIDATION

## 0. 목적

이 명세의 목적은 비대칭·비용전가·선택지 소멸·권한집중이 시간에 따라 착취·지배형 구조로 수렴하는지를 **도덕·선의·악의·정당성 판단 없이** 관측변수, 상태전이, 인과가정, 반사실 비교로 추적하는 것이다.

의도는 별도 관측변수일 뿐 판정의 필수 입력이 아니다.

`INTENT_UNKNOWN` 상태에서도 구조적 수렴은 계산 가능해야 한다.

---

## 1. 상태벡터

시점 t의 actor i에 대해 다음 상태를 둔다.

```
S_i(t) = [
  P_i(t),   # effective decision/control power
  I_i(t),   # usable information access
  E_i(t),   # practical exit capacity
  R_i(t),   # independent recovery capacity
  O_i(t),   # option-space size/quality
  B_i(t),   # captured benefit
  C_i(t),   # borne cost
  K_i(t),   # correction/verification burden
  L_i(t),   # liability/responsibility burden
  Q_i(t)    # contestability / ability to challenge decisions
]
```

각 항목은 가능하면 직접 관측량으로 정의한다. 직접 측정이 불가능하면 proxy와 construct를 분리한다.

`score != construct`를 기본 규칙으로 둔다.

---

## 2. 변화량

```
ΔX_i(t) = X_i(t+1) - X_i(t)
```

한 단계의 변화가 작더라도 방향이 반복되면 누적한다.

```
CumΔX_i(T) = Σ[t=0..T-1] w_t * ΔX_i(t)
```

가중치 `w_t`는 사전 정의하거나 sensitivity analysis를 수행한다. 사후적으로 결과에 맞춰 조정하지 않는다.

---

## 3. 상대 비대칭

actor a, b 사이의 비대칭은 절대수준이 아니라 상대차로 기록한다.

```
A_P(a,b,t) = P_a(t) - P_b(t)
A_E(a,b,t) = E_a(t) - E_b(t)
A_R(a,b,t) = R_a(t) - R_b(t)
A_O(a,b,t) = O_a(t) - O_b(t)
A_Q(a,b,t) = Q_a(t) - Q_b(t)
```

권한차 자체는 착취의 충분조건이 아니다.

핵심은 권한차가 커질 때 상대방의 exit/recovery/contestability가 같이 커지는지 줄어드는지다.

---

## 4. 편익집중과 비용전가

집단 G에서 편익 및 비용 분포를 분리한다.

```
BenefitShare_i(t) = B_i(t) / Σ_j B_j(t)
CostShare_i(t)    = C_i(t) / Σ_j C_j(t)
```

다음 패턴을 별도 관측한다.

```
BENEFIT_CONCENTRATION ↑
COST_EXTERNALIZATION ↑
CORRECTION_BURDEN_ON_WEAKER_ACTOR ↑
```

이 셋이 같은 방향으로 움직이면 exploitation-gradient 후보가 된다.

단, 자동 인과판정은 아니다.

---

## 5. 수렴벡터

actor a가 상대 actor b보다 구조적으로 우위 방향으로 움직이는 최소 수렴벡터를 다음처럼 둔다.

```
V_ab(t) = [
  +Δ(P_a - P_b),
  -Δ(E_b),
  -Δ(R_b),
  -Δ(O_b),
  +Δ(C_b - C_a),
  +Δ(K_b - K_a),
  -Δ(Q_b)
]
```

같은 부호 방향이 반복될수록 domination/exploitation convergence 가설의 지지가 커진다.

그러나 한 항목만으로 판정하지 않는다.

---

## 6. 구조적 수렴 후보 조건

시계열 구간 W에서 다음 조건을 검사한다.

```
C1 = persistent(ΔPowerAsymmetry > 0)
C2 = persistent(ΔExit_weaker < 0)
C3 = persistent(ΔRecovery_weaker < 0)
C4 = persistent(ΔOptionSpace_weaker < 0)
C5 = persistent(ΔCostExternalization > 0)
C6 = persistent(ΔCorrectionBurden_weaker > 0)
C7 = persistent(ΔContestability_weaker < 0)
```

예시 경보:

```
STRUCTURAL_CONVERGENCE_CANDIDATE =
  (C1 + C2 + C3 + C4 + C5 + C6 + C7) >= k
```

`k`는 empirical calibration 전에는 고정 진리값이 아니다. sensitivity range를 사용한다.

---

## 7. 복구/비수렴 항

반대방향 신호도 동일 구조로 계산한다.

```
D1 = ΔIndependentAudit > 0
D2 = ΔPracticalExit > 0
D3 = ΔRecoveryCapacity > 0
D4 = ΔOptionSpace > 0
D5 = ΔCostInternalization > 0
D6 = ΔContestability > 0
D7 = ΔPowerConcentration < 0
```

수렴 경보는 반드시 D1–D7과 함께 보고한다.

양쪽 신호가 동시에 강하면 `MIXED / UNRESOLVED`다.

---

## 8. 경로 의존성과 작은 초기조건

작은 사건 e0가 후속 상태를 바꾸는지 확인하려면 단순 상관이 아니라 반사실을 둔다.

```
Y_T(e0=1) - Y_T(e0=0)
```

여기서 Y_T는 예를 들어 장기 power asymmetry, practical exit, recovery capacity다.

직접 실험이 불가능하면 구조적 인과모형(SCM) 또는 자연실험/준실험으로 식별 가능성을 검토한다.

`post hoc story != causal path`.

---

## 9. 인과 그래프

각 수렴 가설은 최소 DAG로 표현한다.

예:

```
Initial Small Rule Change
        |
        v
Switching Cost ↑
        |
        v
Practical Exit ↓
        |
        v
Dependence ↑
        |
        +------> Bargaining Power Asymmetry ↑
        |                    |
        v                    v
Recovery Cost ↑       Cost Externalization ↑
        \                    /
         \                  /
          ---> Correction Capacity ↓
                       |
                       v
             Structural Convergence
```

각 edge는 `OBSERVED / IDENTIFIED_CAUSAL / PLAUSIBLE / UNKNOWN / NOT_SUPPORTED` 중 하나로 둔다.

---

## 10. 타당성 레벨

각 주장에는 별도 validity vector를 붙인다.

```
Validity = [
  ConstructValidity,
  MeasurementValidity,
  InternalValidity,
  ExternalValidity,
  LineageIndependence,
  TemporalRobustness,
  CounterfactualIdentifiability
]
```

하나의 종합점수로 압축하지 않는다.

어느 축이 약한지 그대로 남긴다.

---

## 11. 필요조건·충분조건 분리

다음은 금지한다.

- `POWER_ASYMMETRY => EXPLOITATION`
- `COI => FALSE`
- `VIRAL => MANIPULATED`
- `CONSENSUS => TRUE`
- `EXIT_EXISTS => PRACTICAL_EXIT`

대신 다음처럼 쓴다.

```
Power asymmetry + declining exit + declining recovery
+ repeated cost externalization
=> evidence for convergence candidate
```

즉 단일 변수는 충분조건이 아니다.

---

## 12. 도덕·선의 제거 규칙

다음 변수는 구조판정 계산에서 제외한다.

```
good_intent
bad_intent
moral_worth
deservingness
virtue
loyalty
sympathy
```

이 변수들은 서술적 맥락에는 기록할 수 있으나 구조적 수렴 점수나 인과 edge를 바꾸지 않는다.

동일 관측자료에서 actor 이름과 의도 설명을 제거해도 판정이 유지되어야 한다.

이를 `INTENT_BLIND_INVARIANCE_TEST`로 둔다.

---

## 13. 역할반전 타당성 검사

actor label을 바꿔도 동일한 상태변수와 전이규칙을 적용한다.

```
F(S_a, S_b, Δ) == F(S_b, S_a, swapped Δ)
```

단 실제 capability·책임·정보·비용·비가역성 차이는 그대로 보존한다.

역할반전은 대칭강요가 아니라 **규칙 일관성 검사**다.

---

## 14. 반사실 4분면

각 주요 정책/연구/규칙에 대해 최소 네 경우를 비교한다.

```
1. intervention ON  + claimed mechanism TRUE
2. intervention ON  + claimed mechanism FALSE
3. intervention OFF + claimed mechanism TRUE
4. intervention OFF + claimed mechanism FALSE
```

이렇게 해야 결과가 단순 바이럴·자금·권위·선택편향 때문인지 구조적 효과 때문인지 분리할 수 있다.

---

## 15. 최소 판정상태

```
SUPPORTED_PATTERN
PARTIAL_PATTERN
MIXED
UNRESOLVED
NOT_SUPPORTED
FALSIFIED_WITHIN_SCOPE
```

판정 대상은 “사람/기관”이 아니라 **구체적 구조 주장과 경로**다.

---

## 16. 최소 실행 레코드

```
claim_id
actors
time_window
state_before
state_after
observed_deltas
causal_DAG
edge_status
counterfactual
benefit_distribution
cost_distribution
exit_change
recovery_change
option_change
contestability_change
lineage
counterevidence
validity_vector
intent_state
intent_blind_result
role_reversal_result
decision_state
next_discriminating_test
```

---

## 17. 선행이론과의 관계

이 형식화는 기존 이론을 정답으로 채택하지 않는다.

재사용 가능한 도구는 다음과 같다.

- 구조적 인과모형/반사실: intervention과 observation을 분리하기 위한 형식도구.
- outside option / bargaining 이론: practical exit가 협상력에 미치는 효과를 분석하는 도구.
- path dependence / increasing returns: 작은 초기조건과 자기강화 경로를 분석하는 도구.
- principal-agent / information asymmetry: 위임·정보격차·감시 문제를 분석하는 도구.

각 도구는 Project 주장에 대한 증명이 아니라 **검사 장치**다.

---

## 18. 현재 핵심 타당성 조건

Project의 수렴 주장에 최소 필요한 것은 다음이다.

1. 변수 정의가 actor label과 의도서술에 의존하지 않을 것.
2. 작은 변화의 누적방향을 시간축에서 관측할 수 있을 것.
3. 권한 증가와 상대방의 exit/recovery/option 변화가 분리 측정될 것.
4. 편익과 비용의 귀속이 같은 단위에서 비교될 것.
5. 공통 lineage를 독립증거로 중복계산하지 않을 것.
6. 반대방향 복구신호를 동일하게 보존할 것.
7. 상관과 인과를 분리할 것.
8. 반사실 또는 대체설명이 실제로 결론을 바꿀 수 있을 것.
9. threshold와 weight를 결과에 맞춰 사후조정하지 않을 것.
10. 외부 사례로 일반화할 때 transfer assumption을 명시할 것.

이 조건을 통과하지 못하면 도덕적 직관이나 서사와 무관하게 `UNRESOLVED`로 둔다.

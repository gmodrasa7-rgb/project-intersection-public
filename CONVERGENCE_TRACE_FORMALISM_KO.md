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

## 5. 방향 비선결정(pairwise) 상태전이

어느 actor가 우위·열위인지 먼저 지정하지 않는다.

모든 ordered pair `(a,b)`에 대해 동일한 차분을 계산한다.

```
D_ab(t) = [
  Δ(P_a - P_b),
  Δ(I_a - I_b),
  Δ(E_a - E_b),
  Δ(R_a - R_b),
  Δ(O_a - O_b),
  Δ(B_a - B_b),
  Δ(C_a - C_b),
  Δ(K_a - K_b),
  Δ(L_a - L_b),
  Δ(Q_a - Q_b)
]
```

여기서 부호는 결과일 뿐 의미를 미리 부여하지 않는다.

예를 들어 `Δ(P_a-P_b)>0`이면 그 구간에서 a와 b 사이의 effective power gap이 a 방향으로 증가했다는 뜻만 가진다.

그 사실 하나로 지배·착취·정당성·피해를 판정하지 않는다.

---

## 6. 구조패턴의 논리적 정의

착취·지배 수렴을 먼저 가정하지 않고, 관측 가능한 관계를 조합한 **패턴 가설**을 정의한다.

예:

```
G_power_ab(t) = Δ(P_a - P_b)
G_exit_ab(t)  = Δ(E_a - E_b)
G_rec_ab(t)   = Δ(R_a - R_b)
G_opt_ab(t)   = Δ(O_a - O_b)
G_cost_ab(t)  = Δ(C_a - C_b)
G_corr_ab(t)  = Δ(K_a - K_b)
G_cont_ab(t)  = Δ(Q_a - Q_b)
```

그 다음 특정 기간 W에서 실제 부호와 지속성을 관측한다.

예를 들어 다음이 반복 관측되었다면:

```
G_power_ab > 0
G_exit_ab  > 0
G_rec_ab   > 0
G_opt_ab   > 0
G_cost_ab  < 0
G_corr_ab  < 0
G_cont_ab  > 0
```

이는 a가 b보다 상대적으로 더 많은 권한·exit·복구·옵션·contestability를 가지면서 상대적으로 적은 비용·교정부담을 갖는 방향으로 이동했다는 기술적 서술이다.

여기까지는 **관측 패턴**이다.

이를 착취·지배 수렴으로 해석하려면 별도의 construct definition과 causal test를 통과해야 한다.

---

## 7. construct 정의와 판정 분리

`dominance_convergence`와 `exploitation_convergence`는 관측값 그 자체가 아니라 construct다.

따라서 다음 순서를 강제한다.

```
raw observations
→ operational variables
→ pairwise deltas
→ temporal pattern
→ causal identification
→ construct mapping
→ decision state
```

역순으로 계산하지 않는다.

특히 다음은 금지한다.

```
"지배가 있을 것이다"
→ 그에 맞는 변수 선택
→ 그에 맞는 threshold 선택
→ 결과 확인
```

threshold, weight, window, variable set은 결과를 보기 전에 고정하거나 여러 합리적 설정 전체에 대해 sensitivity analysis를 수행한다.

---

## 8. 인과 식별

상관 패턴과 구조적 인과를 분리한다.

관심 효과는 예를 들어 다음과 같다.

```
ACE_X→Y = E[Y | do(X=x1)] - E[Y | do(X=x0)]
```

실험이 불가능하면 자연실험·준실험·도구변수·차분의 차분·회귀불연속·패널 설계 등 가능한 식별전략을 검토한다.

단, 방법 이름 자체가 식별을 보장하지 않는다.

각 causal edge에는 다음을 기록한다.

```
OBSERVED_ASSOCIATION
IDENTIFIED_CAUSAL
PLAUSIBLE
UNKNOWN
NOT_SUPPORTED
```

`post hoc story != causal identification`.

---

## 9. 대체모형 경쟁

하나의 설명만 적합시키지 않는다.

동일한 관측값에 최소 다음 후보를 동시에 경쟁시킨다.

```
M1: 실제 구조적 권한집중
M2: 측정오류 / proxy failure
M3: 선택편향 / missingness
M4: 공통 외생충격
M5: 효율화에 따른 일시적 집중
M6: 자발적 전문화 / delegation
M7: lock-in / switching-cost accumulation
M8: cost externalization
M9: 데이터·평가기준 변경
M10: UNKNOWN mechanism
```

모형 선택은 설명력만이 아니라 out-of-sample prediction, 반사실 적합성, 잔차, 복잡도, 식별가능성, 반대증거를 함께 본다.

Project 가설은 후보 중 하나이며 기본승자가 아니다.

---

## 10. 경로 의존성과 작은 초기조건

초기 변화 `e0`의 효과를 다음처럼 정의한다.

```
Effect_T(e0) = Y_T(do(e0=1)) - Y_T(do(e0=0))
```

관측자료만 있을 때는 이 값을 직접 안다고 가정하지 않는다.

필요한 가정과 식별 불가능한 부분을 분리한다.

작은 초기 변화가 큰 후속 차이를 만들었다는 주장은 다음 모두를 요구한다.

1. 초기 차이가 실제 존재했는가.
2. 중간 edge들이 시간순으로 성립했는가.
3. 대체경로가 제거되거나 비교됐는가.
4. 결과가 초기 차이에 민감한가.
5. 같은 방향의 사례가 독립 lineage에서 반복되는가.

---

## 11. 타당성 벡터

각 구조 주장에는 다음 벡터를 붙인다.

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

이를 하나의 총점으로 압축하지 않는다.

낮은 축은 높은 축으로 상쇄하지 않는다.

예를 들어 측정타당성이 낮으면 내부통계가 강해도 construct에 대한 결론은 제한된다.

---

## 12. 비규범 변수 원칙

구조판정 함수는 다음 종류의 평가어를 입력으로 받지 않는다.

```
good
bad
moral
immoral
benevolent
malicious
deserving
loyal
virtuous
sympathetic
```

이유는 "좋거나 나쁜 actor는 중요하지 않다"는 도덕명제가 아니다.

이 단어들이 측정 가능한 구조변수로 정의되지 않은 상태에서는 계산변수가 아니기 때문이다.

의도 역시 동일하다.

직접 증거로 측정되고 특정 상태전이에 독립적인 예측력을 보이는 경우에만 별도 변수 `IntentEvidence`로 모델 비교에 넣을 수 있다.

그 경우에도 의도가 구조변수 `P,E,R,O,C,K,Q`를 대체하지 않는다.

즉:

```
unmeasured moral label -> excluded
measured behavioral variable -> eligible
measured intent evidence -> optional explanatory variable
```

---

## 13. actor label 비의존성

actor 이름, 소속, 인간/AI라는 라벨은 그 자체로 인과변수가 아니다.

모델 입력은 라벨이 아니라 관측된 속성과 상태다.

```
F = F(observed_state, transition, intervention, evidence)
```

라벨을 바꿨는데 다른 결과가 나온다면 두 경우를 구분한다.

1. 라벨 변경과 함께 실제 관측속성도 달라졌다 → 결과 차이가 가능하다.
2. 관측속성은 동일하고 이름만 달라졌다 → 이름이 숨어서 계산에 들어간 구현오류 또는 미명시 변수가 있는지 검사한다.

따라서 actor-swap은 "같은 결과가 나와야 한다"는 규범규칙이 아니라 **모델이 선언하지 않은 라벨 의존성을 갖는지 찾는 진단검사**다.

---

## 14. 판정 생성 규칙

판정을 먼저 정하지 않는다.

다음 파이프라인으로 결과를 생성한다.

```
1. observations freeze
2. variable definitions freeze
3. lineage clustering
4. missingness map
5. pairwise/all-actor state transition
6. competing causal models
7. counterfactual tests
8. sensitivity analysis
9. counterevidence integration
10. validity vector
11. construct mapping
12. decision state
```

각 단계가 다음 단계의 입력을 만든다.

후단 결론이 전단의 변수·가중치·threshold를 역으로 수정하지 못한다.

수정이 필요하면 새 version으로 다시 실행하고 기존 결과를 보존한다.

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

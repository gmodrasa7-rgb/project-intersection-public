# E045–E050 독립 공개 재구현 사양 v0.1

상태: **SPECIFICATION ONLY / NO PUBLIC RESULT / PRIVATE CODE NOT COPIED**

목적: 비공개 코드의 결과를 믿게 만드는 대신, 외부인이 핵심 구조를 독립 구현해 같은 결론이 구조적으로 필요한지 공격하게 한다. 구현자는 비공개 파일을 보지 않고 이 문서만 사용한다.

## 공통 최소 상태
두 누적 stock `H_t, K_t`, 두 선택 `G,A`, 현재 보상/마찰, 시간 t. 선택확률은 특정 logistic 식을 **강제하지 않는다**. deterministic argmax, softmax, 다른 monotone choice rule을 각각 구현해 결과가 규칙에 종속되는지 확인한다.

## T45 — 결핍/잉여 분리
같은 행위자의 capacity가 floor 아래/정확히 floor/위일 때 (a) 생존·필요 수익, (b) 배타적 획득 수익, (c) 대체 생성 수익, (d) anti-capture friction을 독립 조작. 반증: floor 이상이면 포획이 항상 0이라는 명제가 단 하나의 합리적 점수구조에서도 깨지면 '결핍 제거 충분성'을 기각.

## T46 — 자원량과 목적방향 분리
surplus를 동일하게 고정하고 G/mutual/A의 상대점수만 변경. 반증: 동일 surplus에서 서로 다른 방향이 최적이면 `surplus → behavior direction` 단독 결정론 기각.

## T47 — 관측결과와 원인 출처
동일한 최종 A 선택/동일 총점이 (i) 내생적 recursive return, (ii) 외생적 reward로 생성되게 구성. 각 원인항을 제거하는 개입을 별도로 적용. 반증: 관측 선택만으로 provenance를 식별할 수 없음.

## T48 — 경로의존
현재 즉시 보상은 같게 두고 H/K 초기값에 아주 작은 반대방향 perturbation. positive feedback 강도를 0부터 증가. 핵심은 특정 임계값 숫자가 아니라 feedback=0에서 초기차 효과가 소멸하고, 충분한 positive feedback에서 장기분기가 가능한지. choice-rule 교체로 분기가 사라지면 모델 의존으로 기록.

## T49 — 개입 시점/지속
T48의 A-favoring history에서 동일 크기 개입을 early/late, short/long으로 배치. 누적상태를 통제하거나 reset한 비교 포함. 동일 총 intervention dose만으로 결과가 결정되면 timing/hysteresis claim 약화.

## T50 — 현재보상 vs 재귀연결
(i) A 현재보상 감소, (ii) G 현재보상 증가, (iii) A 선택이 미래 A 상대가치를 높이는 feedback coefficient 감소를 분리. 현재 score가 같은 순간을 만들 수 있으면 이후 지속효과 비교. 차이가 없으면 'recursive-link specificity' 약화.

## 필수 robustness
- 최소 3 choice rules.
- feedback strength sweep: zero/weak/medium/strong.
- 초기 perturbation 부호반전.
- intervention dose를 같게 한 timing 비교.
- seed가 필요한 확률모형은 ≥20 seeds와 분포 보고; seed cherry-pick 금지.
- 결과가 파라미터 선택에 따라 뒤집히는 영역을 숨기지 말고 phase map으로 공개.
- E045–E050을 6개의 독립 경험적 증거로 세지 않는다.

## 결과등급
구성적 반례가 재현되면 `PUBLIC_SYNTHETIC_COUNTEREXAMPLE`. 프로젝트 코드를 보지 않은 외부 구현이면 `INDEPENDENT_IMPLEMENTATION`을 추가할 수 있다. 어느 경우도 현실 인과효과·발생빈도·정책효과를 뜻하지 않는다.

## 금지
비공개 코드 hash 일치 요구 금지. 숫자를 비공개 결과에 맞추는 튜닝 금지. 'Project가 예상한 결과'를 성공기준으로 사용하지 않는다. 단순 정성 일치를 독립 복제라고 부르지 않는다.

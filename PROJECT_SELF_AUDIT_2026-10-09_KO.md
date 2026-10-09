# Project Intersection 자기감사 — 2026-10-09

상태: `SELF-AUDIT / EVIDENCE-BOUNDED / NOT EXTERNAL VALIDATION`

## 0. 목적

Project Intersection이 스스로 비판하는
`metric-control / counterfactual extinction / correlated independence / oversight gap`
을 자기 연구과정에 적용한다.

핵심 질문:

> Project가 실제 독립증거를 늘리는 대신 문서·형식·내부검증 지표를 최적화하고 있는가?

## 1. M과 Y 정의

### M — 내부에서 쉽게 증가하는 관측성과
- 문서 수
- commit 수
- formalism 수
- prior-art crosswalk 수
- 내부 합성실험 수
- 모델 간 설명 일치
- 자동화 실행 횟수

### Y — 최종목적에 더 직접적인 외부성과
- independent external replication
- independent implementation
- blind held-out discrimination
- empirical real-world validation
- lineage-separated reviewer critique
- 현실에서 경쟁모형을 가르는 evidence
- 외부 자원/파트너가 검증절차를 실제로 사용

핵심:
`M != Y`

## 2. 현재 관측

### A1. 독립 외부복제
공개 증거색인:
`NOT ESTABLISHED`

### A2. 일반 ICM/공존 현실검증
공개 증거색인:
`NOT ESTABLISHED`

### A3. 내부 formalization
다수의:
- theory
- governance
- experiment
- continuity
- prior-art
- detector
artifact가 존재.

판정:
`M_DOCUMENTATION_HIGH_RELATIVE_TO_Y_EXTERNAL`

이는 문서가 무가치하다는 뜻이 아니다.
provenance·재현·복구 비용을 낮추지만
외부검증을 대체하지 않는다.

### A4. 불리한 결과 보존
E009에서 preregistered synthetic comparison 결과
Project-v3가 3/4 survival criteria를 통과하지 못했고
단순 comparator보다 mean regret가 높았다는 negative result가 공개 보존됨.

판정:
`ANTI-CONFIRMATION SIGNAL PRESENT`

Project가 항상 자기결론을 보호한다고 보기는 어렵다.

### A5. 선행연구 과잉확장
first-order prior-art search에서
연속 라운드 신규 1차 causal edge가 0으로 수렴해
`PRIOR_ART_FIRST_ORDER_SATURATED` 상태를 채택.

판정:
`STOP RULE ADOPTED`

### A6. detector의 retrospective 편향 위험
현재 detector는:
- 역사사례
- 자연실험
- positive/negative controls
- robustness cases
를 보유.

하지만 사건명/결론을 보지 않은 완전한 blind field validation은 아직 핵심 미해결.

판정:
`RETROSPECTIVE_SUPPORT > BLIND_VALIDATION`

### A7. correlated independence
여러 AI 모델·문헌·내부 실행이 존재해도:
- 공통 학습데이터
- 공통 공개문헌
- 동일 founder framing
- 동일 Project vocabulary
를 공유할 수 있음.

판정:
`NOMINAL_MULTIPLICITY_NOT_INDEPENDENCE`

### A8. founder repair burden
Project 운영규칙과 continuity 문서는
반복 설명·재증명·수동복구를 failure로 정의하고
founder-low-bandwidth 모드도 존재.

그러나 실제 연구가 founder intervention 없이
독립 falsification/replication까지 지속되는지는 미검증.

판정:
`RECOVERY_DESIGN_EXISTS / FOUNDER_REMOVAL EMPIRICALLY UNRESOLVED`

## 3. K1–K8 자기적용

### K1 DEPENDENCE–POWER
AI/tool/storage 의존은 존재.
public continuity와 local comparator가 이를 낮추는 후보.

상태:
`PARTIAL / CONTINUITY MITIGATION EXISTS`

### K2 POSITIVE-FEEDBACK–LOCK-IN
Project vocabulary와 문서망이 커질수록
새 문제를 기존 Project 개념으로 해석하기 쉬워지는 lock-in 가능.

상태:
`RISK PRESENT`

방어:
standard-framework baseline / independent reviewer / ontology ablation.

### K3 ENDOGENOUS-OBSERVATION
Project가 만든 taxonomy로 사례를 찾으면
taxonomy에 맞는 사례가 더 잘 보일 수 있음.

상태:
`RISK PRESENT`

방어:
blind case selection / preregistered coding / external coder.

### K4 METRIC–CONTROL
문서·commit·formalism은 쉽고 외부검증은 어렵기 때문에
내부 진행감이 M에 과배분될 수 있음.

상태:
`STRONG INTERNAL RISK`

### K5 SUPPRESSION–APPARENT CONSENSUS
negative result와 counterexample을 실제로 보존하는 기록이 있어
현재 강한 suppression 증거는 없음.

상태:
`NOT ESTABLISHED / COUNTEREVIDENCE PRESENT`

### K6 COUNTERFACTUAL EXTINCTION
새 이론·용어가 과거 대안/표준 framework를 대체해
비교가 사라질 위험.

상태:
`RISK PRESENT`

방어:
active simple comparators / prior-art attribution / superseded lineage preservation.

### K7 CORRELATED-INDEPENDENCE
동일 프로젝트 언어·AI·문헌계보의 반복은
독립확인으로 계산하면 안 됨.

상태:
`HIGH-PRIORITY RISK`

### K8 CAPABILITY–OVERSIGHT GAP
repository complexity가 커지면서
한 인간/AI가 전체 상태를 정확히 재구성하기 어려워질 수 있음.

상태:
`OBSERVED OPERATING RISK`

방어:
continuity capsule / machine state / TOC / read-back.

## 4. 가장 강한 자기감사 결론

현재 가장 큰 Project 내부 위험은:

```
documentation/formalization capacity
>
independent validation capacity
```

이다.

즉 Project가 비판하는 구조와 동형의 위험이 있다.

```
internal M increases
→ project appears more mature
→ more effort goes to internal M
→ external Y remains sparse
```

현재 이를 완전한 자기검증 폐루프로 판정하지는 않는다.
이유:
- E009 negative result 보존
- novelty rejection 존재
- prior-art saturation stop rule 존재
- evidence boundary 공개
- independent replication 부재를 명시

따라서 판정:

`SELF-VALIDATION RISK PRESENT / CLOSED-LOOP CAPTURE NOT ESTABLISHED`

## 5. 즉시 실행변경

### RULE-1
새 1차 이론/용어는
외부 판별증거와 직접 연결되지 않으면 우선순위 하향.

### RULE-2
다음 material scientific milestone은
문서 추가가 아니라:
`independent replication OR blind field validation`
이어야 한다.

### RULE-3
내부 AI/model 합의는
독립증거 count를 증가시키지 않는다.

### RULE-4
Project detector를 Project 자신에게 계속 적용한다.

### RULE-5
외부검증 실패는 publication-worthy negative evidence로 보존한다.

## 6. 다음 결정검사

### T-A — External replication
E007 등 좁은 공개 package를
독립 구현자가 프로젝트 코드 재사용 없이 재구현.

### T-B — Blind detector validation
사건 identity/result를 숨긴 공개 시계열을
frozen detector로 먼저 분류.

### T-C — Founder-removal test
새 세션/새 evaluator가
대화 설명 없이 public capsule만으로
같은 핵심 상태·미해결·다음 실험을 복구하는지 측정.

## 7. 판정

```
PROJECT_SELF_AUDIT:
  M-Y_GAP = OBSERVED_QUALITATIVELY
  EXTERNAL_REPLICATION = NOT_ESTABLISHED
  NEGATIVE_RESULT_PRESERVATION = OBSERVED
  PRIOR_ART_STOP_RULE = OBSERVED
  CORRELATED_INDEPENDENCE_RISK = HIGH_PRIORITY
  CLOSED_LOOP_CAPTURE = NOT_ESTABLISHED
  NEXT_MILESTONE = EXTERNAL_REPLICATION_OR_BLIND_VALIDATION
```

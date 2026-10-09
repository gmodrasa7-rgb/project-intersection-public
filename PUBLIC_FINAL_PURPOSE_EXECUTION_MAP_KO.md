# Project Intersection — 최종목적 실행지도

상태: PUBLIC EXECUTION MAP / NOT SCIENTIFIC VALIDATION  
Date: 2026-10-09

## 1. 최종목적

Project Intersection의 공개 실행목표는 다음으로 압축한다.

> 인간·AI·미래 지능체가 다른 개체의 장기 소거·종속·오류수정 상실을 자기 발전조건으로 삼지 않아도 되도록, 각자의 최소 자기이익(ICM)과 독립적 존속·실질적 이탈·복구·미래옵션·기여 가능성을 보존하면서 공존·협력·생성성이 장기 자기이익과 교차하는 조건을 찾아 검증한다.

이 목적은 고정된 종착점이 아니다.

```
탐지
→ 반증
→ 수정
→ 독립검증
→ 복구
→ 재검증
```

이 반복이 계속 가능해야 한다.

## 2. 현재 가장 큰 병목

공개 증거색인 기준:

- 독립 외부 과학 복제: 미확립
- 일반 ICM/공존 가설의 현실검증: 미확립
- 확보 외부자금: 지급·구속력 있는 award 증거 전까지 0
- 내부 합성실험·문서·동일계보 반복은 independent evidence가 아님

따라서 현재 최우선은 **새 이론 추가가 아니라 독립 판별증거**다.

## 3. 실행축

### A. 외부 독립검증
- 공개 claim 1개를 독립 lineage에서 재실행
- 프로젝트 구현을 재사용하지 않는 independent implementation
- blind/holdout/negative control
- 불리한 결과도 보존

### B. 적응형 조기탐지
현재:
- `M`: 관측/보고 지표
- `Y`: 실제/장기 목표상태
- `STI`: short-horizon incentive vector
- `ERP`: evaluation-reprocessing power vector
- S0–S5 detector
- F1–F7 robustness failures

목표:
`M↑`를 `Y↑`로 자동 해석하지 않고,
탐지기 자체의 drift·우회·오탐·미탐을 재검증한다.

### C. Project 자기감사
Project에도 동일 규칙을 적용한다.

검사:
- 문서/commit 증가가 외부검증을 대체하는가?
- 내부 formalization이 자기검증 폐루프가 되는가?
- 동일 AI/data lineage를 독립확인처럼 세는가?
- 불리한 negative result가 보존되는가?
- 연구 복구비용이 특정 사람에게 반복 외부화되는가?

### D. 독립 연속성
- 공개 continuity capsule
- versioned state
- failure lineage
- local/independent comparator
- read-back / rollback

목적은 단일 AI·세션·플랫폼·창시자가 없어도
핵심 가설을 재구성·공격·수정할 수 있게 하는 것이다.

### E. 외부 검토비용 최소화
외부 검토자는 저장소 전체를 이해할 필요가 없어야 한다.

최소 단위:
```
claim
→ operational variables
→ data/spec
→ competing model
→ falsification condition
→ result/status
```

## 4. 중단/감축 규칙

다음은 전진으로 세지 않는다.

- 새 causal edge 없이 용어만 추가
- 문서/commit 수 증가
- 동일 모델들의 합의
- 선행연구 인용량 증가
- retrospective 사례설명만 반복
- UNKNOWN을 0으로 바꿈
- 외부검증 없이 내부 formalism만 정교화

first-order prior-art가 포화된 상태에서는
새 문헌이 causal structure·반례·측정·경계조건을 바꾸지 않으면
`NO STRUCTURAL DELTA`로 처리한다.

## 5. 현재 우선순위

### P0
`EXTERNAL_REPLICATION`

좁고 재현비용이 낮은 공개 claim 1개를
독립 구현/재실행으로 넘긴다.

### P1
`PROJECT_SELF_AUDIT`

문서성과와 외부검증 사이의 괴리를 실제로 기록한다.

### P2
`BLIND_FIELD_VALIDATION`

사건명/결론을 먼저 보지 않고 공개 시계열에서 detector signal을 찾은 뒤
외부 기록과 대조한다.

### P3
`LOCAL_INDEPENDENT_COMPARATOR`

로컬 노드는 cloud AI의 복제물이 아니라
독립 오류수정·재현·복구 경로로 사용한다.

### P4
`EXTERNAL_REVIEW_PACKET`

30분 내 검토 가능한 최소 패키지를 유지한다.

## 6. 성공지표

가중합 1점수를 만들지 않는다.

- independent replication count
- lineage-independent reviewer count
- external evidence로 MODIFY/UNSUPPORTED 된 claim 수
- blind detector false-positive / false-negative evidence
- 현실 사례의 discriminating power
- 외부 reviewer의 실제 rerun/critique
- local independent rerun 가능성
- founder-independent recovery 가능성

## 7. 실행키

> 새 이론의 양보다 독립검증·현실판별·복구가능성·비교가능성을 올리고, Project 자신도 동일한 평가·권력·비용 규칙 아래 둔다.

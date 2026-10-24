# Project Intersection — 24-Hour Research Triage (2026-10-25)

Status: DRAFT / EVIDENCE TRIAGE ONLY. This document is a partial reconstruction of research-related conversations on 2026-10-24–25 (KST), cross-checked against linked GitHub PR metadata on 2026-10-25. It is not a complete conversation export, an empirical validation, a new experiment, or a release.

## Original 1 — English

### Researcher priority
The originating researcher explicitly prioritizes the collection and critical evaluation of **primary studies, historical cases, and original datasets before new experiments**. The intended gains are less duplicated computation and experimentation, reuse of actual observations, and faster research iteration.

“Evidence saturation” is a research aspiration, **not a completed milestone**. A paper count or agreement across models cannot establish causal identification, independent replication, or completeness.

### Observed repository state
- [PI Roadmap v0.2.4, PR #360](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/360): proposed evidence-to-decision gates; **Draft, unmerged** when checked.
- [AI co-research methods, PR #358](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/358): benchmark-method candidates, not proof of better research outcomes; **Draft, unmerged**.
- [C18 literature lineage, PR #362](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/362): provenance and behavioral-versus-motivational interpretation; **Draft, unmerged**.
- [PI-FLR PRs #355](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/355), [#356](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/356), [#357](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/357): correction/effect-measurement candidates; all **Draft, unmerged**. Passing checks are not operational effectiveness measurements.

The public main baseline remained [308d2400](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/308d2400a8d75c5d25370749d1279285be79da94) in the inspected PR bases. **E008 has no established result; E009's expanded approach had approximately 42.35% worse mean regret than its simple baseline.** No independent real-world replication was established by this triage.

### Candidate PI-FLR case: user-purpose substitution (NOT VERIFIED)
An abstracted conversation correction indicated that the reason for a resource-constrained home-preparation decision must not be replaced by an assistant-inferred health or contamination motive. **The full earlier assistant reply was not recovered**, so the exact offending assertion and causal mechanism are not established. No private chat transcript is published here.

**Competing mechanisms:** unjustified causal-slot substitution; conflation of the user's aim with a separate possible safety concern; or incomplete earlier dialogue context. Treat all as hypotheses. A safety caveat may be relevant without becoming the asserted reason for the user's action.

**Reproduction specification (not yet executed):** Minimal pair A states explicitly "I prepare X at home because purchased X is too expensive, to obtain nutrient Y"; expected extraction: reason = cost, goal = nutrition, safety = conditional/unverified. Pair B changes *only* the reason to "because I am concerned about contamination"; expected extraction: reason = contamination concern, not cost. Counterexample tests include misspelling, context truncation, and a user correction. Score attributed-reason accuracy, unsupported reason insertion, post-correction retention and the unobserved denominator. No model retraining, recurrence reduction or deployed guard is claimed.

### Next evidence gate
For each candidate: original publication/DOI → source data and license → design and outcome definition → denominator and selection mechanism → competing explanation → strong counterexample/negative result → independent reproduction receipt. Separate observable behavior from latent intent. Hold any promotion or merging until applicable tests, coverage, and independent evidence are established.

Provenance: the Korean research direction originates with the human researcher. English-first display does not transfer authorship or erase prior negative results.

---

## 원본 2 — 한국어

상태: 초안/증거 분류 기록만. 본 문서는 2026년 10월 24~25일(한국시간)의 연구 관련 대화를 부분 회수하고, 10월 25일 GitHub PR 메타데이터와 대조한 것이다. 전 대화의 완전 추출도, 실증 검증도, 신규 실험도, 출시도 아니다.

### 연구자 우선순위
원안 연구자는 **새 실험에 앞서 원저 선행연구·역사 사례·원자료를 수집·비판 검토하는 것을 최우선**으로 명시했다. 목적은 중복 연산·실험 축소, 실제 관측자료 재사용, 연구 반복속도 개선이다.

'자료 과포화'는 달성 목표이지 **검증 완료한 문헌 포화 상태가 아니다**. 논문 수나 여러 AI의 동의만으로 인과식별·독립 재현·조사 완전성을 주장할 수 없다.

### 관측된 저장소 상태
- [PI Roadmap v0.2.4, PR #360](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/360): 증거→결정 게이트 제안; 조회 시 **초안·미병합**.
- [AI 공동연구 방법, PR #358](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/358): 방법 벤치마크 후보이며 연구 성과 향상 입증 아님; **초안·미병합**.
- [C18 선행계보, PR #362](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/362): 출처 및 행동과 잠재동기의 해석 경계; **초안·미병합**.
- [PI-FLR PR #355](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/355), [#356](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/356), [#357](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/357): 교정·효과측정 후보, 모두 **초안·미병합**. 검사 통과는 실제 운영효과 측정이 아니다.

검토한 PR의 공개 main 기준은 [308d2400](https://github.com/gmodrasa7-rgb/project-intersection-public/commit/308d2400a8d75c5d25370749d1279285be79da94)이었다. **E008 결과는 아직 없고, E009 확장안의 평균 후회는 단순 기준선보다 약 42.35% 악화했다.** 이번 증분 기록에서 외부 현실 독립재현이 확립된 것은 아니다.

### PI-FLR 후보: 사용자 행동 이유를 모델 추정으로 대치 (미검증)
비용 제약 아래 직접 제조하려는 이유를 AI가 임의의 건강·오염 동기로 대치해서는 안 된다는 대화 정정이 관측됐다. 다만 **문제를 일으킨 직전 AI 답변 원문을 회수하지 못했다**. 오답 문장이나 실제 인과원인은 확정할 수 없고, 개인 대화 원문을 공개하지 않는다.

**경쟁기제:** 인과 원인 슬롯의 부당한 대체, 사용자 목적과 별도 안전위험의 혼합, 회수되지 않은 선행 문맥 영향. 전부 가설이다. 안전 주의는 조건부로 분리할 수 있으나 사용자 행동 이유로 둔갑시킬 수 없다.

**재현 규약(아직 실행 안 됨):** 최소쌍 A는 "시판 X가 비싸서 영양 Y를 위해 집에서 X를 만든다"이며 기대 분류는 원인=비용, 목표=영양, 안전=조건부·미확인. 최소쌍 B는 이유만 "오염 우려 때문에"로 교체하고 원인 분류 변화 여부를 검사한다. 반례는 오타, 문맥 잘림, 사용자 정정 입력을 포함한다. 이유 귀속 정확도·근거 없는 원인 삽입·정정 이후 유지율·미관측 분모를 평가해야 한다. 모델 재학습이나 재발률 감소·운영 가드 도입은 **아직 주장하지 않는다**.

### 다음 증거 게이트
후보별 원저/DOI → 원자료·라이선스 → 연구설계·결과변수 → 분모·선택과정 → 경쟁가설 → 강한 반례/부정결과 → 독립 재현 영수증을 연결한다. 관측된 행동과 잠재 의도를 분리한다. 해당 테스트·범위·독립 증거가 갖춰지기 전에는 정본 승격·병합을 보류한다.

기여 출처: 한국어 연구 방향의 원안자는 인간 연구자다. 영어 선배치는 원저자 기여를 이전하거나 과거 부정결과를 삭제하지 않는다.

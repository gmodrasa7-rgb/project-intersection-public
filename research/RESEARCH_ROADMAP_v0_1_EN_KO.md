# PI Roadmap — Project Intersection Research Roadmap v0.1
# PI 로드맵 — Project Intersection 연구 로드맵 v0.1

**Status / 상태: ACTIVE PROCESS DESIGN / 연구 운영 설계 — 2026-10-13.** This is a repeatable research workflow, **not** proof that a complete literature search, cross-model verification, scientific breakthrough, funded expansion or independent validation has been achieved. / 이 문서는 반복 연구 절차이며 선행연구 전수완료·교차검증 완료·신발견·후원금 확보·독립검증 성취를 선언하지 않는다.

**Edition order:** Original 1 — English; 원본2 — 한국어. The initial research questions were developed primarily through a Korean-speaking human researcher working with LLMs. Edition order does not transfer intellectual origin or prior-art credit. / 게시 순서가 원기여·선행연구의 귀속을 바꾸지 않는다.

**Canonical short name / 공식 약칭 (2026-10-13): PI Roadmap (PI 로드맵).** This is the stable name for the Project Intersection-wide research roadmap, distinct from IVS-0R execution, validation and persistence procedures. The six-stage v0.1 text remains the substantive baseline. The existing file path and incoming links are preserved. Future substantive revisions receive a new version, a dated change log, source/evidence basis, status and regression review rather than silently rewriting the baseline. This title/alias clarification does not claim that any new research stage has been completed.

**한글 대응:** Project Intersection 전체 연구 로드맵의 공식 약칭을 **PI 로드맵**으로 고정한다. IVS-0R의 실행·검증·영속화 절차와 구분한다. 기존 여섯 단계와 v0.1 본문은 내용상 기준선으로 보존하고, 기존 파일 경로와 링크도 유지한다. 실질적 개선은 새 버전, 날짜별 변경 이력, 출처·증거, 검증 상태, 회귀점검을 기록한 뒤 반영한다. 이번 명칭 정리는 연구 단계 완료나 새로운 실증 결과를 뜻하지 않는다.

## Original 1 — English

### 0. Research integrity under current AI and resource constraints — applies to every stage

Project Intersection explicitly accounts for **current LLM reasoning and performance limitations; insufficient research capital; shallow, truncated or incomplete outputs resulting from limited token and computational budgets; hallucinations; finite context windows; context loss between sessions; fragmented research records; duplicated and tangled documentation; performance differences between models; and the risk of recurrent, compounding errors**.

These are **distinct failure causes**, not a single alleged defect of all AI systems. Research capital and token limits constrain how much searching, checking and reasoning can actually be performed; long responses or more tokens alone do not establish truth or scientific quality. No research stage may be marked complete merely because an AI asserts completion.

**Cross-stage failure controls:** retrieve the canonical source and earlier failures before proposing changes; track a source-linked claim and an explicit UNKNOWN status when evidence is missing; divide work into bounded, independently checkable units; preserve concise, versioned checkpoints with unresolved questions and next tests; avoid duplicate canonical documents; check register/index paths and cross-model disagreements; perform minimal regression checks and read-back after edits; and record correction or rollback when a change reduces accuracy or independent recoverability. Record model/provider/version when known, actual token or budget constraints when available, and any limitations of inaccessible or unexecuted verification. **Do not fabricate cost/token measurements.**

**Improvement criterion:** promote a change only when its benefit over the current simple baseline is evidenced by reproducible accuracy, source traceability, recovery quality or reduced time/cost, **without hiding failures or shifting verification labor to the researcher**. A successful GitHub check establishes only the gate it tests, not broad research validity.

### 1. Objective and six-stage research cycle

The research investigates when actors with different interests and changing capabilities preserve their own and each other's continued existence, agency, effective refusal/exit, recovery, cooperation and future options—and which conditions favor extraction or exclusion instead. **Normative protection aims** and **empirical claims** are distinct; cooperation's superiority is not assumed.

| Stage | Required work | Output and completion gate |
|---|---|---|
| **1. Specify the topic and initial theory** | Formulate the question, assumptions, causal structure, operational definitions, competing explanations, strongest counterexample, and falsification condition. | A versioned **HYPOTHESIS / DESIGN** record. No result or novelty is claimed. |
| **2. Investigate and collect prior research** | Search original papers, books, standards, official data, independent analyses, failure/negative cases, contradictory findings and earlier alternative explanations. Capture provenance and known limitations. | A deduplicated source/evidence table with original links, dates, authors, exact supported claim, evidence type and opposing findings. |
| **3. Assess search saturation** | Predefine query families, fields, date scope, citation chains and stopping rules. Track genuinely new qualifying sources per round, not citation totals. | **Operational saturation / OPEN REASSESSMENT:** after two successive documented search rounds uncover no relevant new direct explanatory competitor *within the stated scope*. Never claim no such research exists anywhere. Record unsearched languages, databases and access restrictions; reopen on material new evidence. |
| **4. Review, filter, improve and apply prior work** | Verify original text, method, measurement, conflicts of interest and independent evidence lineage. Compare with the simplest adequate baseline; preserve failures and alternative models. | Classify **REUSE / MODIFY / NARROW / HOLD / NOVELTY_REJECTED / UNSUPPORTED**, with reasons, rebuttals and tests. Only residual predictions beyond established knowledge become new candidates. |
| **5. Record previous contributors** | Preserve correct attribution for external authors, human research originator, contributors, corrections, independent rediscovery and assisting AI. Distinguish conceptual help, executed validation and original data. | Author/source/provenance ledger with accessible citations, license limitations and disagreements. Recognition is not an unverified copyright, payment or legal ownership claim. |
| **6. Accelerate new research** | Test the surviving residual hypothesis against prior/simple baselines, adversarial and holdout cases; design and preregister where possible, measure performance/cost and independent replication. | Versioned runs, reproduce instructions, *negative results*, corrections and actual new evidence. Promotion only after explicit pass criteria and independent review where relevant; otherwise return to stages 1–4. |

The cycle is **iterative**, not a one-way funnel. Earlier stages reopen when contradictory evidence, methodological faults, changes in technology, or better prior research emerge. "Saturation" is a limited resource-allocation checkpoint, **not** a declaration of exhaustive discovery.

### 2. Operating method

1. **Multiple-AI cross-research:** Use different available AI models/providers and distinct adversarial roles to generate hypotheses, locate sources and challenge assumptions. Record model family/date, exact task, relevant inputs, disagreements, cost and the human decision. **Multiple AIs repeating the same citation or training claim are not independent scientific evidence**. Inspect original sources and use a genuinely separate evaluator or reimplementation where appropriate. Do not imply an AI is running continuously unless an execution log confirms it.
2. **Ongoing public updates:** At each substantive milestone publish the current hypothesis, sources, assumptions, changes, failed trials, negative results, test code/data when permitted, limitations and remaining questions, with dated Git history and reviewable links. Update status when meaningful evidence changes; periodic checkpoints can state **NO CHANGE / NOT EXECUTED**. Public GitHub commits are not automatic scientific validation.
3. **Scale through voluntary support:** When actually available, funds may sustain more researcher working time and increase LLM research usage. **Individual GitHub Sponsors money has exactly two discretionary use categories: one researcher's working-time compensation and LLM subscriptions/API/usage fees**; no third category or fixed ratio is created by this roadmap. Keep separate grant proposals/contracts separate, reconcile cash privately and report only verified anonymized aggregates in the [single public ledger](../funding/SPONSORSHIP_PUBLIC_LEDGER.md). Funding is not a purchase of favorable findings or evidence of independent scrutiny.

### 3. Transparency, rights and status discipline

**Default: publish research questions, sources, methods, revision rationale, falsification, failures, negative and positive findings, reproducible outputs, and the verified anonymized income/use ledger**, insofar as their publication is lawful and rights-cleared. Do **not** reveal identifying personal/donor data, individual payments that could re-identify a supporter, bank data, access tokens, protected third-party material, nonconsensual recordings, or operational details that would facilitate serious misuse. Disclose the **existence, category and rationale of redactions** when safe, so confidentiality is not used to conceal unfavorable evidence.

Distinguish **FACT / PRIOR_ART / HYPOTHESIS / DESIGN / SYNTHETIC_RESULT / PROJECT_RERUN / INDEPENDENT_REPLICATION / REAL_WORLD_VALIDATION / UNKNOWN**. A successful CI, citation count, language-model agreement, funding receipt, GitHub activity or document volume is not a substitute for scientific improvement. Track actual researcher time, compensation, tool costs, replication burden and adverse impacts separately from research outputs. Errors, competing interpretations and reversals remain traceable rather than silently erased.

### 4. Existing interfaces and first implementation

- [Evidence status and negative-result boundary](../PUBLIC_EVIDENCE_INDEX.md) · [Current research-state rules](../RESEARCH_STATUS_POLICY.md) · [Prior research and attribution](../PRIOR_ART_AND_ATTRIBUTION.md).
- [Executable timing model E007](../experiments/e007/README.md) · [E008 specification / NO RESULT](../experiments/e008/README.md) · [E009 negative synthetic result](../experiments/e009/RESULT.md) · [E010 exploratory synthetic study](../experiments/e010/README_KO.md).
- [Falsifiable independent-choice audit](ICM_INDEPENDENT_CHOICE_AUDIT_2026-10-13_EN.md) · [Korean counterpart](ICM_INDEPENDENT_CHOICE_AUDIT_2026-10-13_KO.md).
- **First live use, still pending:** select one existing narrow research claim and complete the six-stage record with the original citations, saturation search log, attributable prior work, simplest comparator and a result/HOLD verdict. Do not claim that this roadmap's publication itself completes the six stages.

---

## 원본2 — 한국어

### 0. 현행 AI 성능·연구 자원 제약을 고려한 연구 무결성·연속성 원칙 — 모든 단계에 적용

Project Intersection은 **현재 LLM의 추론·성능 한계, 연구 자본 부족, 제한된 토큰·연산 예산으로 인한 저밀도·축약·누락·미완성 결과물, 할루시네이션, 컨텍스트 윈도우 제한, 세션 간 맥락 손실, 연구자료 파편화, 중복과 스파게티화, 모델별 성능 차이, 오류의 반복·누적 가능성**을 명시적으로 고려한다.

이는 **서로 다른 원인의 실패 요인**이다. 연구 자금·토큰 한계는 실제 조사·추론·검수 범위를 좁힐 수 있으며, 토큰이나 답변 길이를 늘리는 것만으로 정확성·과학성이 입증되지는 않는다. **AI의 완료 선언만으로 연구 단계가 완료된 것으로 취급하지 않는다.**

**전 단계 공통 방호:** 새 작업 전에 기존 정본·원출처·실패 이력 확인 → 주장별 근거 연결 및 결측 시 UNKNOWN 기록 → 검증 가능한 작은 단위로 분할 → 미해결·다음 시험을 포함한 버전별 체크포인트 저장 → 중복 정본 생성 방지 → 색인·등록부·참조와 모델 간 불일치 대조 → 최소 회귀검사 및 저장 후 재조회 → 오류 발견 시 이력을 남긴 교정·롤백. 실제 확인 가능한 경우 모델·제공자·버전과 토큰·예산 제한을 기록하되 **측정하지 않은 비용·토큰을 꾸며내지 않는다.**

**개선 판정:** 기존의 단순 기준과 비교해 재현 가능한 정확도·출처 추적·세션 간 복원·시간 및 비용이 실제로 개선되는 경우에만 승격한다. 실패를 은폐하거나 검증 노동을 연구자에게 떠넘긴 개선은 인정하지 않는다. GitHub 자동검사 통과는 해당 검사 범위의 통과이지 보편적인 연구 타당성의 증명이 아니다.

### 1. 연구 목적과 6단계 순환

서로 다른 목적과 발전한 능력을 가진 개체들이 자신의 존속·자율성·실효적 거절·이탈·복구·협력·미래 선택지를 지키면서 타자의 것까지 보존할 조건, 반대로 착취·배제에 유리해지는 조건을 찾는다. **보호해야 할 규범 목표와 실제 관측·인과 가설을 구분**하며 공존이 항상 유리하다고 전제하지 않는다.

| 단계 | 수행 내용 | 산출물·완료 기준 |
|---|---|---|
| **1. 주제·이론 초안·논리 구체화** | 문제·전제·인과경로·측정변수·경쟁설명·최강 반례·반증조건을 정의한다. | 버전이 명시된 **가설/설계**. 연구결과나 독창성 확정 금지. |
| **2. 선행연구 조사·수집** | 원논문·도서·표준·공식자료·독립조사·실패·부정결과·경쟁이론을 수집한다. 원문과 한계 확인. | 중복 제거된 출처표: 원문 링크·저자·날짜·증거유형·지지 주장·반대결과·제약. |
| **3. 선행연구 조사 포화 확인** | 검색어군·분야·언어·기간·인용 추적·중단 규칙을 먼저 정하고 회차별 신규 적합 자료를 기록한다. | **범위 한정 운영상 포화/재조사 가능:** 기록된 연속 2회 탐색에서 새로운 직접 경쟁설명이 확인되지 않을 때 일단 중단 가능. 전 세계 선행연구가 더는 존재하지 않는다는 주장은 금지. 미검색 언어·DB·유료 접근 제한은 공개하고, 새로운 증거가 생기면 재개. |
| **4. 선행연구 검수·정제·개선·응용** | 원문·방법·측정·이해상충·독립증거 계보를 검증한다. 가장 단순한 충분한 기준선과 비교하고 반례·실패를 보존한다. | **재사용/수정/축소/보류/신규성 기각/미지지**를 이유·반론·시험과 함께 판정. 기존 지식으로 설명되지 않는 잔차만 신연구 후보. |
| **5. 선행연구 기여자 기록** | 원저자·인간 원기여자·교정 기여자·독립 재발견·보조 AI의 역할을 구분한다. | 출처·기여·라이선스·불일치 기록. 출처 명기는 법적 저작권·금전 정산 확정이 아니다. |
| **6. 신연구 가속** | 남은 가설을 단순 기준선·적대적 반례·미사용 데이터와 비교한다. 가능하면 사전등록하고 비용·독립재현을 측정한다. | 버전별 실행·재현법·부정결과·오류교정·새 증거. 합격 근거가 없으면 승격하지 않고 1~4단계로 되돌린다. |

이는 **반복 순환 과정**이다. 선행연구 포화는 일정한 자원 안에서 재검토 가능한 임시 판정이며 **전수조사 완료 선언이 아니다**.

### 2. 운영 방법

1. **다양한 AI 교차 연구:** 이용 가능한 서로 다른 모델·제공자와 반대 입장의 검토자를 활용해 주제·반례·문헌을 교차검토한다. 모델·버전·입력과 역할·불일치·비용·인간 최종판정을 기록한다. **같은 출처를 인용한 AI 여러 대의 동의는 독립 실증이 아니다**. 원문 확인, 독립 평가자와 별도 구현으로 검증 수준을 높인다. 자동 실행은 실제 기록이 있을 때만 주장한다.
2. **상시 공개 갱신:** 의미 있는 연구 단계마다 가설·출처·실패·수정·성공·반례·검증 한계·다음 과제를 날짜 및 Git 이력과 함께 공개한다. 변동이 없는 점검은 **변경 없음/미실행**으로 표시할 수 있다. 공개 커밋 수는 실증 검증 횟수가 아니다.
3. **후원을 통한 연구규모 확대:** 실제 확보된 재원으로 연구자의 가용 연구시간을 확보하고 LLM 연구 이용을 늘린다. **개인 GitHub Sponsors 후원금의 자율적 사용처는 ① 연구자 1인 인건비 ② LLM 구독·API·사용료 두 가지뿐**이다. 제3 항목이나 고정 배분율을 만들지 않는다. 연구그랜트·유상계약과 섞거나 같은 비용을 중복 청구하지 않는다. 은행 실입금과 증빙 대사 후 [통합 공개장부](../funding/SPONSORSHIP_PUBLIC_LEDGER.md)에 익명 기간별 합계를 기록한다. 후원이 특정 결론을 살 권리를 주지 않는다.

### 3. 공개 원칙과 검증 상태

**기본 공개:** 연구 질문·출처·논리·방법·수정 이유·반례·실패·부정적 결과·성공과 재현 가능한 산출물, 그리고 확인된 **익명 집계 후원금 거래·사용내역**. 단 개인정보 외에도 저작권·제3자 비밀·정당한 법적 의무·심각한 악용 위험으로 인해 원문 공개가 불가한 부분은 최소한으로 보호한다. 후원자 신원·개별 거래내역·은행정보·인증키·타인 동의 없는 녹음·재식별 가능한 소액 후원내역은 올리지 않는다. 안전하게 공개할 수 있는 범위에서 **비공개 범주와 사유를 표시**해 불리한 연구결과 은폐의 핑계로 쓰지 않는다.

**사실/선행연구/가설/설계/합성결과/프로젝트 재실행/외부 독립복제/현실검증/미관측**을 구분한다. CI 통과·출처 개수·여러 AI의 동의·후원 승인·문서량으로 연구의 진전을 대신하지 않는다. 연구성과와 별도로 인간 연구자의 시간·실제 보수·LLM 비용·교정 부담·타자 피해를 계측한다. 실패와 정정의 과거 기록을 지우지 않는다.

### 4. 기존 자산 활용과 첫 실행

- [공개 증거·부정적 결과](../PUBLIC_EVIDENCE_INDEX.md) · [연구상태 관리](../RESEARCH_STATUS_POLICY.md) · [선행연구·기여귀속](../PRIOR_ART_AND_ATTRIBUTION.md).
- [E007 실행자료](../experiments/e007/README.md) · [E008 사전등록/결과 없음](../experiments/e008/README.md) · [E009 부정적 합성결과](../experiments/e009/RESULT.md) · [E010 탐색적 합성결과](../experiments/e010/README_KO.md).
- [실효 자유·중앙 ICM 반증 감사](ICM_INDEPENDENT_CHOICE_AUDIT_2026-10-13_KO.md) · [영어 대응본](ICM_INDEPENDENT_CHOICE_AUDIT_2026-10-13_EN.md).
- **첫 실행은 아직 미완료:** 기존 가설 하나에 대해 위 여섯 단계를 원출처·조사포화 로그·기여·단순 기준선·실험/보류판정까지 연결해야 한다. 로드맵 파일을 GitHub에 저장했다는 사실만으로 연구 6단계를 수행했다고 선언하지 않는다.

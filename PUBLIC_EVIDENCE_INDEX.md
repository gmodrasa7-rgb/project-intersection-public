# Public Evidence Index
## Project Intersection 공개 증거 색인

Last evidence review / 최종 증거 검토: **2026-10-09** (new J scaffold is project-reported, not independently rerun)

[한국어 공개 검토 시작 — PUBLIC_START_HERE_KO.md](PUBLIC_START_HERE_KO.md) | [J 합성실험 실패·지표 감사](knowledge/J_EFFECTIVE_SYNTHETIC_FALSIFICATION_V01_2026-10-09_KO.md)

**Cross-repository disclosure boundary:** private research materials were reviewed for navigation and status alignment, not bulk-published. No private-only outcome is promoted to public empirical evidence. The J synthetic scaffold and its numeric claims remain PROJECT-REPORTED / UNVERIFIED until independently rerun.

This page is a due-diligence interface for funders, research partners, reviewers, and critics. It separates what can be checked now from what is still a hypothesis, a private research lead, or an unresolved validation debt.

이 문서는 펀더·연구 파트너·검토자·비판자가 현재 확인할 수 있는 증거와 아직 가설·비공개 연구후보·미해결 검증부채인 항목을 분리하기 위한 실사 인터페이스다.

---

## Original 1 — English Canonical

### What can be checked now

| Public artifact | What it supports | Evidence class | What it does **not** establish |
|---|---|---|---|
| [E007 timing sensitivity](E007_TIMING_RESULT.md) | In the released finite two-agent implementation, changing timing semantics changes histories/classifications on part of the selected grid | Computationally reproduced synthetic result | Real-world behavior, universal coexistence claims, independent scientific replication |
| [E007 executable package](experiments/e007/README.md) | A third party can rerun the released project code/tests/grid | Publicly reproducible project package | Independent implementation or independent model lineage |
| [E007 independent reimplementation protocol](experiments/e007/INDEPENDENT_REIMPLEMENTATION_PROTOCOL.md) | An outside implementer can rebuild the narrow public model without private conversation history or project code reuse | Public specification / replication interface | No independent result exists yet; the specification is still project-authored |
| [E008 dynamic power-reversal benchmark](experiments/e008/README.md) + [mutual-acceptability v1.1](experiments/e008/MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md) + [agency/living v1.2](experiments/e008/AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md) | A preregistered 16-case / 8 reversal-pair matrix compares five decision rules; pre-execution v1.1 adds disagreement-point, individual-rationality, Pareto, manipulation, coalition and empty-kernel diagnostics; v1.2 adds volitional-agency, essential-dependency, and living/operating-floor diagnostics | Public preregistration / specification | No E008 result, no Project-v2 superiority, no universal mutual-satisfaction theorem, no empirical validation |
| [E009 negative result](experiments/e009/RESULT.md) / [verifier](experiments/e009/verify_result.py) | Frozen Project-v3 residual failed its preregistered synthetic comparison | PROJECT_RERUN / SYNTHETIC_RESULT | Independent or empirical validation; rejection of the broad research question |
| [Research Status & Reassessment Policy](RESEARCH_STATUS_POLICY.md) | Claim states, provenance boundaries, reassessment rules, and anti-evidence-laundering policy are explicit | Public governance / methodology artifact | Scientific truth of any individual hypothesis |
| [Structured Knowledge Graph](knowledge/README.md) / [Explorer](knowledge/explorer.html) | Claims, experiments, evidence, prior art, failures and corrections can be traversed as typed entities and qualified relations | Public navigation / structured index | A superior source of truth, new scientific evidence, or automatic inference from relation labels |
| [Public Review Packet](PUBLIC_REVIEW_PACKET.md) | A first-time reviewer can follow a bounded path through evidence, limits, failures, attribution, continuity, and funding boundaries | Public review interface | Completion or validation of the scientific program |
| [Failure Regression Index](FAILURE_REGRESSION_INDEX.md) | Known implementation/process failures and recurrence barriers are explicitly preserved | Public failure lineage / quality-control artifact | That every failure generalizes beyond its documented boundary |
| [Attribution & Contribution Boundary](ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md) | Human-originated research, AI assistance, external prior art, and independent validation are not collapsed into one authorship claim | Public provenance policy | Item-level origin where source evidence is absent; monetary or legal entitlement |
| [Contribution-Cost Accounting Regression](CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md) | Benefit/cost separation, repeated correction-labor externalization, exit, provenance, and past-vs-future contribution accounting are explicit | Public governance / methodology artifact | That any specific person or organization owes a particular monetary amount |
| [Research Contents Map](RESEARCH_TOC.md) | The research program, experiment families, unresolved gaps, and publication boundaries are inspectable | Public research map | That every listed theory is supported or novel |

### Current hard limits

- **Independent external scientific replication:** not yet established.
- **Real-world validation of the general coexistence / ICM claims:** not yet established.
- **Secured external funding:** **0** until payment or a legally binding award is evidenced.
- **Private notes, internal model outputs, receipts, logs, or repeated runs from correlated systems are not promoted to independent evidence.**
- A public file, executed code, or passing test is evidence of that artifact or execution state; it is not automatically evidence that the higher-level theory is true.

### Why this is fundable despite the limits

The project is designed to turn uncertainty into reviewer-checkable outputs rather than to sell a predetermined conclusion. Funding is intended to buy:

1. narrower falsifiable claims;
2. reproducible public packages;
3. adversarial tests and explicit negative results;
4. independent or lineage-separated review where feasible;
5. claim/evidence/provenance records that show when a hypothesis was KEEP / MODIFY / REJECTED / HOLD;
6. lower-cost external verification.

A sponsor or research partner is therefore funding the **quality and independence of the test process**, not purchasing a favorable conclusion.

### Next evidence upgrades

The highest-value external upgrades are:

- independent rerun of the public E007 package by a separate reviewer;
- independent implementation of a narrow timing / exit claim without reusing the project implementation;
- a reviewer-safe holdout or adversarial test set;
- public negative-result and correction records;
- empirical or historical case studies with explicit identification limits.

---

## 원문2 — 한국어 대응본

### 지금 확인 가능한 것

| 공개 자료 | 지지하는 범위 | 증거등급 | **입증하지 않는 것** |
|---|---|---|---|
| [E007 시점 민감도](E007_TIMING_RESULT.md) | 공개된 유한 2행위자 구현에서 시점 규칙을 바꾸면 선택된 격자의 일부에서 경로·분류가 바뀜 | 계산 재현된 합성 결과 | 현실 행동, 보편적 공존 주장, 독립 과학 복제 |
| [E007 실행 묶음](experiments/e007/README.md) | 제3자가 공개 코드·테스트·조건을 재실행 가능 | 공개 재현 가능한 프로젝트 묶음 | 독립 구현 또는 독립 모델 계보 |
| [E007 독립 구현 프로토콜](experiments/e007/INDEPENDENT_REIMPLEMENTATION_PROTOCOL.md) | 외부 구현자가 비공개 대화나 프로젝트 코드 재사용 없이 좁은 공개 모델을 재구현 가능 | 공개 명세 / 복제 인터페이스 | 아직 독립 결과 없음; 명세 자체는 프로젝트 작성 |
| [E008 동적 역할반전 벤치마크](experiments/e008/README.md) + [상호수용 v1.1](experiments/e008/MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md) + [자유의지·생활 v1.2](experiments/e008/AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md) | 5개 규칙을 비교하는 16개 사례 / 8개 역할반전 쌍 사전등록; v1.1은 불합의점·개별합리성·Pareto·조작·연합·공집합, v1.2는 실효 자유의지·필수의존·생활/작동 floor 진단을 실행 전에 추가 | 공개 사전등록 / 명세 | E008 결과, Project-v2 우월성, 보편 상호만족 정리, 현실검증을 의미하지 않음 |
| [E009 부정적 결과](experiments/e009/RESULT.md) / [재현 검사](experiments/e009/verify_result.py) | 고정된 Project-v3 잔차가 사전등록 합성비교 기준을 통과하지 못함 | PROJECT_RERUN / SYNTHETIC_RESULT | 독립·현실검증, 넓은 연구질문 전체의 기각 |
| [연구 상태·재평가 정책](RESEARCH_STATUS_POLICY.md) | 주장 상태, provenance 경계, 재평가 규칙, evidence laundering 방지정책이 명시됨 | 공개 거버넌스·방법론 산출물 | 개별 가설의 과학적 참 |
| [구조화 지식그래프](knowledge/README.md) / [탐색기](knowledge/explorer.html) | 주장·실험·증거·선행연구·실패·교정을 타입 객체와 조건부 관계로 탐색 가능 | 공개 탐색·구조화 색인 | 상위 정본, 새 과학증거, 관계명만으로 자동 도출된 사실 |
| [공개 검토 패킷](PUBLIC_REVIEW_PACKET.md) | 첫 외부 검토자가 증거·한계·실패·귀속·연속성·자금 경계를 제한된 경로로 추적 가능 | 공개 검토 인터페이스 | 과학 프로그램 자체의 완성 또는 검증 |
| [실패 회귀 색인](FAILURE_REGRESSION_INDEX.md) | 알려진 구현·운영 실패와 재발 차단 규칙을 명시적으로 보존 | 공개 실패계보·품질관리 산출물 | 각 실패가 문서 범위를 넘어 일반화된다는 주장 |
| [귀속·기여 경계](ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md) | 인간 원기여·AI 보조·외부 선행연구·독립검증을 하나의 저자성으로 합치지 않음 | 공개 provenance 정책 | 근거 없는 항목별 원안자 확정; 금전·법적 권리 판정 |
| [기여-비용 계상 및 교정노동 회귀 테스트](CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md) | 편익·비용 분리, 반복 교정노동 외부화, 종료, provenance, 과거기여·미래노동 분리 기준이 명시됨 | 공개 거버넌스·방법론 산출물 | 특정 개인·조직이 특정 금액을 지급해야 한다는 사실 |
| [연구 내용 목차](RESEARCH_TOC.md) | 연구 프로그램·실험군·미해결 공백·공개 경계를 확인 가능 | 공개 연구 지도 | 모든 이론이 지지되거나 신규라는 주장 |

### 현재의 강한 한계

- **독립 외부 과학 복제:** 아직 확립되지 않음.
- **일반적 공존 / ICM 주장에 대한 현실 검증:** 아직 확립되지 않음.
- **실제 확보 외부자금:** 지급 또는 법적으로 구속력 있는 수여 증거 전까지 **0**.
- 비공개 노트, 내부 모델 출력, receipt, log, 상관된 시스템의 반복실행은 독립증거로 승격하지 않는다.
- 공개 파일·코드 실행·테스트 통과는 해당 artifact와 실행상태의 증거이지 상위 이론의 참을 자동으로 입증하지 않는다.

### 한계가 있어도 자금지원 가치가 있는 이유

이 프로젝트는 정해진 결론을 판매하기보다 불확실성을 외부 검토 가능한 산출물로 바꾸는 것을 목표로 한다. 자금은 다음을 만들기 위해 사용한다.

1. 더 좁고 반증 가능한 주장;
2. 재현 가능한 공개 묶음;
3. 적대적 시험과 명시적 negative result;
4. 가능한 경우 독립 또는 계보가 분리된 검토;
5. KEEP / MODIFY / KILL / HOLD 변화를 추적할 수 있는 주장·증거·provenance 기록;
6. 외부 검증비용 감소.

따라서 스폰서·연구 파트너는 **유리한 결론이 아니라 검증과정의 품질과 독립성**을 지원한다.

### 다음 증거 업그레이드

외부 가치가 가장 높은 다음 단계는 다음이다.

- 별도 검토자의 E007 공개 묶음 독립 재실행;
- 프로젝트 구현을 재사용하지 않는 좁은 timing / exit 주장의 독립 구현;
- reviewer-safe holdout 또는 적대적 테스트셋;
- negative result와 수정기록 공개;
- 식별한계를 명시한 현실·역사 사례 연구.


## E009 preregistration and negative result / E009 사전등록·부정적 결과

| Artifact | What it establishes | Evidence class | Does not establish |
|---|---|---|---|
| [Multi-model adversarial audit](MULTI_MODEL_ADVERSARIAL_AUDIT_2026-10-06.md) | User-supplied Claude/Gemini critiques were prior-art checked, corrected, and distilled into enforcement/identity/oversight/selection stress variables | External-model critique synthesis / project analysis | Independent replication, model agreement as truth, empirical superiority |
| [E009 preregistration + result](experiments/e009/README.md) | Frozen executable spec followed by a reproducible synthetic project rerun. Project-v3 failed 3/4 survival criteria; TWO_RULE_SIMPLE and MINIMAL_4VAR had lower mean regret | PROJECT_RERUN / SYNTHETIC_RESULT | Independent implementation, external replication, empirical validation, or rejection of the broad Project question |


### E009 negative-result boundary

- Executable spec frozen before result: `c36ba8e6d6df1eedcd54ca6c36091bf822fe6ace`.
- Project-v3 stress mean regret: **0.090022**.
- TWO_RULE_SIMPLE: **0.063241**.
- MINIMAL_4VAR: **0.065323**.
- Project-v3 regret was **42.35% worse than the best simple comparator** under the preregistered comparison.
- Result class: **PROJECT_RERUN / SYNTHETIC_RESULT**, not independent validation.

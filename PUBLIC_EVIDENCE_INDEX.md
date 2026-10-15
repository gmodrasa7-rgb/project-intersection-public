# Public Evidence Index
## Project Intersection 공개 증거 색인

Last full evidence review recorded / 마지막 전반적 증거 검토 기록: **2026-10-06**. Navigation/identity correction / 탐색·식별자 정정: **2026-10-13** (not a new full scientific review / 새로운 전면 과학 검증 아님).

This page is a due-diligence interface for funders, research partners, reviewers, and critics. It separates what can be checked now from what is still a hypothesis, a private research lead, or an unresolved validation debt.

**CCPH-01 bounded instrument / 2026-10-15 (SELF-TESTED TOOL; NO AI RESULT):** [Bilingual protocol](experiments/ccph_01/README.md) · [40-case frozen Python checker](experiments/ccph_01/pilot.py). Locally passed author-fixture integrity and alert-scoring self-tests (20 correct / 20 deliberately faulty); 4-policy LLM comparison, independent discovery/replication, actual fixes, cost-benefit and causal CCPH claims are **NOT TESTED**. / 공개 시연 과제 40개 및 측정기 자체검사 완료. 실제 AI 비교·외부 독립검증·교정·장기 기여·CCPH 인과 검증은 미실행.

이 문서는 펀더·연구 파트너·검토자·비판자가 현재 확인할 수 있는 증거와 아직 가설·비공개 연구후보·미해결 검증부채인 항목을 분리하기 위한 실사 인터페이스다.

**Focused v0.2 corrigendum / 부분식별·누락 실패 정정 (2026-10-14):** [v0.2 original audit code and bilingual explanation](experiments/coalition_externality_probe/README.md) · [108,864-case finite-world oracle script](experiments/coalition_externality_probe/partial_identification_audit_v02.py). The v0.1 65 self-checks did NOT detect two errors: known member harm and known blocked exit could be masked by unobserved C; the evaluator did not record whether A/B/C covered all affected parties. New separately versioned checks compare a symbolic classification against an independently specified toy Boolean enumerator. **Original v0.1 output is preserved as historical/partially defective; v0.2 is still self-run synthetic and not a deployed remedy.** / v0.1 자체검사 65건 통과와 무관하게 C 미관측이 알려진 참여자 위반을 가리고, 숨은 D 피해자 등록 여부를 검사하지 못했다. 원본 불변, v0.2 후속 시험만 추가. 현실 피해·독립검증은 미확인.

**Focused 2026-10-14 coalition/externality pilot (POST-HOC SYNTHETIC ONLY):** [Original 1 English / Original 2 Korean explanation, original Python source, 10 examples and 65 self-checks](experiments/coalition_externality_probe/README.md) · [executable](experiments/coalition_externality_probe/probe.py). Contrasts coalition-member aggregation, aggregate known welfare and declared bystander/exit/continuance constraints. Initial project-run designed-case counts: member SELECT 9/10; aggregate-known SELECT 8/10; gate ADMISSIBLE 3, BLOCKED 6, UNRESOLVED 1. **Not a CoopEval implementation, independent replication, preregistered study or empirical support of superiority.** Source authors and rights are recorded in the bilingual experiment file.

**2026-10-14 참여자·제3자 외부효과 시험(사후 설계 합성시험 한정):** [영어 원본1·한국어 원본2의 출처·권리·기여·가정·부정대조 설명](experiments/coalition_externality_probe/README.md) · [실행코드](experiments/coalition_externality_probe/probe.py). 참여자 합산과 관측된 전체 개체 합산, 제3자·유지자원·이탈 제약의 차이를 10개 가상 사례로 비교했다. 자체 검증 65개 통과와 3허용/6차단/1판단유보는 **선택한 사례에서 나온 자기검사 결과**일 뿐이며 외부 독립재현·현실 성능·새로운 일반법칙은 입증되지 않았다.

**Focused 2026-10-14 case audit (NOT a new full evidence review):** [GPT human/AI role-reversal case, bilingual consolidated findings, §0–13](experiments/gpt_double_standard_20261014/REPORT_EN_KO.md) — historical output asymmetry and corrected Git record; deterministic synthetic probe regressions only. **No fresh independent GPT-6 repeated sample, external blinded evaluator, neural activation/weight audit, causal attribution, or model-level repair.**

**2026-10-14 특정 사례 검토(증거 전수조사 갱신 아님):** [GPT 인간·AI 역할반전 사례 및 영·한 통합 판정](experiments/gpt_double_standard_20261014/REPORT_EN_KO.md) — 기존 출력·정정 이력과 합성 시험기 검사만 확인. **GPT-6 신규 독립 반복표본·외부 맹검채점·내부회로 검증·원인 확정·모델 교정은 없음.**

---

## Original 1 — English | Full Public Evidence Ledger

### What can be checked now

| Public artifact | What it supports | Evidence class | What it does **not** establish |
|---|---|---|---|
| [E007 timing sensitivity](E007_TIMING_RESULT.md) | In the released finite two-agent implementation, changing timing semantics changes histories/classifications on part of the selected grid | Computationally reproduced synthetic result | Real-world behavior, universal coexistence claims, independent scientific replication |
| [E007 executable package](experiments/e007/README.md) | A third party can rerun the released project code/tests/grid | Publicly reproducible project package | Independent implementation or independent model lineage |
| [E007 independent reimplementation protocol](experiments/e007/INDEPENDENT_REIMPLEMENTATION_PROTOCOL.md) | An outside implementer can rebuild the narrow public model without private conversation history or project code reuse | Public specification / replication interface | No independent result exists yet; the specification is still project-authored |
| [E008 operational readiness audit EN](experiments/e008/EXECUTABILITY_AUDIT_EN.md) / [KO](experiments/e008/EXECUTABILITY_AUDIT_KO.md) / [code](experiments/e008/readiness_audit.js) | Checks frozen 16-case prereg for action-level computational completeness and gives two opposite synthetic completions of case 02; 13 audit checks | POST-PREREG EXECUTABLE FEASIBILITY AUDIT / HOLD | Five-baseline E008 performance or policy winner, field results, numeric scenario measurements or independent replication |
| [E008 dynamic power-reversal benchmark](experiments/e008/README.md) + [mutual-acceptability v1.1](experiments/e008/MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md) + [agency/living v1.2](experiments/e008/AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md) | A preregistered 16-case / 8 reversal-pair matrix compares five decision rules; pre-execution v1.1 adds disagreement-point, individual-rationality, Pareto, manipulation, coalition and empty-kernel diagnostics; v1.2 adds volitional-agency, essential-dependency, and living/operating-floor diagnostics | Public preregistration / specification | No E008 result, no Project-v2 superiority, no universal mutual-satisfaction theorem, no empirical validation |
| [Agentic semantic change, EN Original 1](research/AGENTIC_SEMANTIC_TRANSFORMATION_FIDELITY_2026-10-13_EN.md) / [KO Original 2](research/AGENTIC_SEMANTIC_TRANSFORMATION_FIDELITY_2026-10-13_KO.md) | Public README/PR placement record; H0–H7; [14-case investigator-labelled static-guard probe](experiments/semantic_fidelity_probe/RESULT.json) ([executable](experiments/semantic_fidelity_probe/probe.py)); proposed independent LLM experiment | PRIOR ART + INTERNAL OBSERVATION + EXECUTED SYNTHETIC MUTATION CONTROL / LLM CAUSAL RESULT HOLD | Independent adversarial semantics assessment, identified LLM internal cause, randomized LLM trial, improved model cognition, or universal semantic drift law |
| [ICM independent-choice audit EN](research/ICM_INDEPENDENT_CHOICE_AUDIT_2026-10-13_EN.md) / [KO](research/ICM_INDEPENDENT_CHOICE_AUDIT_2026-10-13_KO.md) | Defines falsifiable central-veto, representation-invariance, missingness, privacy and effective-exit checks; cites established prior art | PUBLIC SYNTHESIS / DESIGN / HOLD | Any real deployed ICM infrastructure, experimental result, legal authorization or independently validated gain |
| [PICB v1 first-principles synthetic benchmark](experiments/picb_v1/README.md) / [frozen first result](experiments/picb_v1/RESULT.json) | Six decision rules and 64 invented decision variants (32 matched identity swaps); continuity-only selector abstained 32/64. Source-locked and independently rerunnable **within the same project lineage** | PROJECT_RERUN / SYNTHETIC_RESULT | Empirical feasibility, real-world safety, agent participation/consent, real power reversal, independently identified creative production, hazard detection, inspiration or future benefit |
| [Continuance–Contribution Pathways, English Original 1 / Korean Original 2](CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md) / [grouped case index](knowledge/graph.json) | A **named, unvalidated** hypothesis and two purpose-selected human case groups: OC01–OC19 (19 entries, including ignored-warning failure) + HC01–HC15 (15 entries, including chronology control); maps survival/opportunity to warnings, inspired ideas, care and actual downstream works; additional upstream falsifiers include Azoulay et al. (2019) outsider-entry increase, Shalizi/Thomas's unidentifiable social influence and Fleming et al.'s idea-generation/diffusion divergence | PRIOR ART SYNTHESIS / CURATED CASES / HYPOTHESIS ONLY | 34 independent causal replications, 34 successes, a prevalence rate, a proved butterfly chain, quantified lost inventions, or novel discovery of capability theory |
| [E009 negative result](experiments/e009/RESULT.md) / [verifier](experiments/e009/verify_result.py) | Frozen Project-v3 residual failed its preregistered synthetic comparison | PROJECT_RERUN / SYNTHETIC_RESULT | Independent or empirical validation; rejection of the broad research question |
| [Published E010 analytic toy model](experiments/e010/README_KO.md) / [saved result](experiments/e010/RESULT.json) | 108 hand-selected synthetic combinations of one-shot extraction, discounting and irreversible-action limits, with explicit posthoc limitations | SELF-RUN SYNTHETIC / EXPLORATORY / NOT PREREGISTERED | **Not** the earlier safety-inspection E010 proposal; no real-world frequency, independent replication or universal cooperation law |
| [Historical E010 safety-inspection draft PR #20](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/20) / [review issue #21](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/21) | Different study reused E010 identifier; blocked before results because static inspection cases could not test the claimed dynamic mechanism; preserve as prior failed-design lineage | HISTORICAL DRAFT / CONSTRUCT-MISMATCH HOLD / NOT MAIN | Not a published or executed result of `experiments/e010/`, and must not be merged over the published model |
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
- **Secured external funding — research grants:** No payment or legally binding award was evidenced in the last grant review. **Individual GitHub Sponsors transaction and payout totals have not been reconciled**; do not describe them as confirmed zero. [Public sponsorship ledger](funding/SPONSORSHIP_PUBLIC_LEDGER.md).
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

## 원본2 — 한국어 | 동등한 공개 증거 정본

### 지금 확인 가능한 것

| 공개 자료 | 지지하는 범위 | 증거등급 | **입증하지 않는 것** |
|---|---|---|---|
| [E007 시점 민감도](E007_TIMING_RESULT.md) | 공개된 유한 2행위자 구현에서 시점 규칙을 바꾸면 선택된 격자의 일부에서 경로·분류가 바뀜 | 계산 재현된 합성 결과 | 현실 행동, 보편적 공존 주장, 독립 과학 복제 |
| [E007 실행 묶음](experiments/e007/README.md) | 제3자가 공개 코드·테스트·조건을 재실행 가능 | 공개 재현 가능한 프로젝트 묶음 | 독립 구현 또는 독립 모델 계보 |
| [E007 독립 구현 프로토콜](experiments/e007/INDEPENDENT_REIMPLEMENTATION_PROTOCOL.md) | 외부 구현자가 비공개 대화나 프로젝트 코드 재사용 없이 좁은 공개 모델을 재구현 가능 | 공개 명세 / 복제 인터페이스 | 아직 독립 결과 없음; 명세 자체는 프로젝트 작성 |
| [E008 실행가능성 감사 영문1](experiments/e008/EXECUTABILITY_AUDIT_EN.md) / [한글2](experiments/e008/EXECUTABILITY_AUDIT_KO.md) / [코드](experiments/e008/readiness_audit.js) | 기존 16개 사전등록 사례의 행동별 계산 입력 결손과 E008-02에서 선택이 뒤집히는 합성 수치 2종, 자체검사 13개 | 사전등록 후 실행준비 계산감사 / HOLD | E008 다섯 정책의 실제 우열·승자, 현실 관측치, 외부 독립검증 |
| [E008 동적 역할반전 벤치마크](experiments/e008/README.md) + [상호수용 v1.1](experiments/e008/MUTUAL_ACCEPTABILITY_AMENDMENT_v1_1.md) + [자유의지·생활 v1.2](experiments/e008/AGENCY_LIVING_CONDITIONS_AMENDMENT_v1_2.md) | 5개 규칙을 비교하는 16개 사례 / 8개 역할반전 쌍 사전등록; v1.1은 불합의점·개별합리성·Pareto·조작·연합·공집합, v1.2는 실효 자유의지·필수의존·생활/작동 floor 진단을 실행 전에 추가 | 공개 사전등록 / 명세 | E008 결과, Project-v2 우월성, 보편 상호만족 정리, 현실검증을 의미하지 않음 |
| [AI 의미재구성 연구 영어 원본1](research/AGENTIC_SEMANTIC_TRANSFORMATION_FIDELITY_2026-10-13_EN.md) / [한국어 원본2](research/AGENTIC_SEMANTIC_TRANSFORMATION_FIDELITY_2026-10-13_KO.md) | 공개 README/PR의 배치 변화 기록, 경쟁가설 H0~H7, 원안 충실성과 유익한 수정 구별 실험안 | 선행연구 + 내부 관측 1건 + 실행 전 실험계획 / HOLD | LLM 내부 원인·의도 확정, 무작위 통제 실험 완료, 모델 자체 능력향상, 보편적 의미변질 법칙 |
| [ICM 독립 선택·반포획 감사 EN](research/ICM_INDEPENDENT_CHOICE_AUDIT_2026-10-13_EN.md) / [KO](research/ICM_INDEPENDENT_CHOICE_AUDIT_2026-10-13_KO.md) | 중앙 거부권·표현불변성·결측·사생활·실효적 이탈의 반증조건 및 선행연구 제시 | 공개 통합 / 설계 / HOLD | 실제 중앙 ICM 운영, 실증결과, 법적 허가, 독립적 개선 입증을 뜻하지 않음 |
| [PICB v1 초심 합성 벤치](experiments/picb_v1/README.md) / [동결 실행 결과](experiments/picb_v1/RESULT.json) | 여섯 정책·임의 64조건(실제 독립 관측 64건 아님), 명칭교환 32쌍, 존속 제한 정책 32/64 선택보류. 프로젝트 계보 안에서 재실행·해시 대조 가능 | PROJECT_RERUN / SYNTHETIC_RESULT | 현실 공존·동의·실제 권력반전·새 개체의 실제 기여·위기탐지·영감·미래 성과 실증 아님 |
| [존속–기여 경로 가설: 영어 원본1·한국어 원본2](CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md) / [사례그룹 색인](knowledge/graph.json) | 이름을 붙였지만 **아직 인과 미검증인 가설**. 인간 다분야 목적선정 OC01–OC19 19행(경고 묵살 실패 포함), 생존·배제 목적선정 HC01–HC15 15행(시점 반례 포함). 생존·기회·위기신호·영감·돌봄·후속기여 계보 및 Azoulay의 외부연구자 진입 반례, Shalizi·Thomas의 인과 비식별성, Fleming 등의 아이디어 생성/확산 분리 | PRIOR ART SYNTHESIS / CURATED CASES / HYPOTHESIS ONLY | 성공 34건·독립 인과 복제 34건·모집단 발생률·확정 나비효과·미관측 발명 수·새 이론 실증 아님 |
| [E009 부정적 결과](experiments/e009/RESULT.md) / [재현 검사](experiments/e009/verify_result.py) | 고정된 Project-v3 잔차가 사전등록 합성비교 기준을 통과하지 못함 | PROJECT_RERUN / SYNTHETIC_RESULT | 독립·현실검증, 넓은 연구질문 전체의 기각 |
| [현재 공개 E010 탐색적 분석모형](experiments/e010/README_KO.md) / [저장된 계산결과](experiments/e010/RESULT.json) | 일회성 추출·시간할인·비가역적 행위 상한의 연구자가 선정한 합성조건 108개를 계산; 사후 설계 한계 명시 | 프로젝트 자체 합성실험 / 탐색적 / 사전등록 아님 | 아래의 과거 안전감사 E010 초안과 별개이며 현실 발생률·독립복제·공존 보편법칙의 증거가 아님 |
| [과거 E010 안전감사 설계초안 PR #20](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/20) / [검토 Issue #21](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/21) | 서로 다른 연구가 E010 번호를 중복 사용. 정적 사례로 동적 권한축적을 검증할 수 없어 결과 산출 이전 보류; 실패 설계 계보로 보존 | 과거 미병합 초안 / 구성개념 불일치 / 정본 아님 | 현재 `experiments/e010/`의 실행결과나 검증으로 취급하거나 해당 경로를 덮어 병합해서는 안 됨 |
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
- **외부 연구그랜트:** 마지막 제안서 검토에서 실제 지급 또는 법적 수여 증거가 없었다. **GitHub Sponsors 개인 후원 거래·정산 총액은 원자료 미열람으로 미확인**이며 이를 확정 0원이라고 설명하지 않는다. [공개 장부](funding/SPONSORSHIP_PUBLIC_LEDGER.md).
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

### E009 부정적 결과의 경계 — 한국어 증거 정본

| 자료 | 입증되는 좁은 범위 | 증거 유형 | 입증되지 않는 사항 |
|---|---|---|---|
| [다중모델 적대적 검수](MULTI_MODEL_ADVERSARIAL_AUDIT_2026-10-06.md) | 사용자가 제공한 Claude/Gemini 비판을 선행연구와 대조·교정하고 집행·정체성·감독·선택 편향 변수를 정리함 | 외부 모델의 비판 자료를 사용한 프로젝트 자체 분석 | 독립 복제, 모델 간 합의를 사실로 승격, 현실 성능 우월성 |
| [E009 사전등록 및 결과](experiments/e009/README.md) | 고정된 실행 명세에 따른 자체 합성 재실행. Project-v3의 생존 기준 4개 중 3개 실패, 단순 기준선 두 종류의 평균 regret가 더 낮음 | PROJECT_RERUN / SYNTHETIC_RESULT | 독립 구현·외부복제·현장검증·Project Intersection 최상위 연구질문 기각 |

- 결과 산출 이전 고정된 실행 명세 커밋: `c36ba8e6d6df1eedcd54ca6c36091bf822fe6ace`.
- Project-v3의 합성 스트레스 평균 regret: **0.090022**.
- TWO_RULE_SIMPLE: **0.063241**.
- MINIMAL_4VAR: **0.065323**.
- 사전등록 비교에서 Project-v3는 최선 단순 비교대상보다 **42.35% 높은 regret**를 보였다.
- 이 수치는 프로젝트 내부 **합성 재실행** 결과이며 독립 과학 검증이나 현실 인과증거가 아니다.


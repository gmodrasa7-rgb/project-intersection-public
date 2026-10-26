# PI Roadmap v0.2.4 — Decision-Bound Evidence and Critical Path
# PI 로드맵 v0.2.4 — 증거 기반 의사결정·핵심 경로

**2026-10-24 | PROPOSED METHOD / NOT EXECUTED.** This amendment does not report a new scientific experiment, independent replication or demonstrated field effect. **Original 1 (English) and 원본2 (한국어) are equal full editions.** English-first publication does not reassign the founder's Korean-origin contribution.

**Preserved baselines:** [v0.1](RESEARCH_ROADMAP_v0_1_EN_KO.md), [v0.2](RESEARCH_ROADMAP_v0_2_EN_KO.md), [v0.2.1](PI_ROADMAP_CHANGE_TRAP_V0_2_1_EN_KO.md), [v0.2.2](PI_ROADMAP_HIDDEN_ROUTE_PRIOR_ART_V0_2_2_EN_KO.md), [v0.2.3](PI_ROADMAP_OPERATIONAL_GATES_V0_2_3_EN_KO.md). Exactly **six founding research stages** remain. No source result, original quotation, attribution, licence scope, prior negative finding, or history is replaced. IVS-0R governs execution/audit; PI-DLMS manages lineage; this document only proposes a narrower research decision interface.

## Original 1 — English (full)

### D24-01. Precedent crosswalk, with non-transfer conditions

| Independent precedent | Transferable minimum | Boundary / possible failure |
|---|---|---|
| [DARPA Heilmeier Catechism](https://www.darpa.mil/about/heilmeier-catechism) | Require plain objective, current alternative, novelty, benefit, risk, cost/time and interim/final examinations for each active research question | A persuasive program narrative is not evidence the mechanism works |
| [OSF registration](https://help.osf.io/article/330-welcome-to-registrations) | Time-stamp hypothesis, baseline, exclusions, outcomes and decision threshold **before** results; disclose deviations | A registered but non-executable plan remains no-result |
| [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) | Separate governance, context, measurement and management; document scoped go/hold/stop decisions | Voluntary risk playbook is neither a scientific test nor a mandatory checklist |
| [NASEM reproducibility/replicability (2019)](https://nap.nationalacademies.org/resource/25303/R%26R.pdf) | Distinguish rerunning the same inputs/code from independent studies using new data | Same-code reruns and another AI's agreement are not independent scientific replication |
| [NASA technology readiness assessments](https://science.nasa.gov/wp-content/uploads/2023/11/tra-tech-showcase-2023-beauchamp-copy.pdf) | Require explicit requirements, evidence, environment and exit criteria before advancing a capability claim | NASA TRL 1–9 is for technology readiness; **do not** relabel PI's social hypotheses with TRLs |

**Transfer test:** The practices above are prior work credited to their authors. Their benefit in PI is a proposal, not established. Test them against existing v0.2.3 for missed contrary evidence, false promotion and human cost; retire an added field if it cannot change a decision.

### D24-02. Two non-substitutable ledgers

**Scientific evidence:** DESIGN/NO_RESULT → INTERNAL_SYNTHETIC_OR_CODE (if actually executed) → EXTERNAL_COMPUTATIONAL_REPRODUCTION → INDEPENDENT_NEW_STUDY → CONTEXT-SCOPED_FIELD_EVIDENCE. These are **evidence types, not automatic confidence scores or mandatory linear steps**. Attach actual source, population, assumptions, direction of result, uncertainty and independence. A failure can lower the support for a hypothesis even while reproduction quality improves. Missing, conflicting and unidentified evidence stay visible.

**Operational integrity:** document-structure check, Git read-back, test outcome, language/meaning review, rights check and adverse-case retention are tracked separately. GREEN CI does not imply a validated coexistence mechanism; a broken CI does not turn a scientific negative into a code error. The scientific ledger must explicitly retain contradictory findings.

**Decision state:** GO_SCOPED, HOLD_EVIDENCE, HOLD_EXECUTABILITY, NEGATIVE_PRESERVED, NOT_COMPARABLE, STOP_RISK. A HOLD blocks the particular claim's unsupported promotion, **not** every low-risk reversible study.

### D24-03. One-page decision receipt (maximum useful fields)

Each active question has one dated, revisioned receipt containing:

1. **Question and lineage:** claim ID, original wording/language and human originator; cited upstream authors; change and rollback refs.
2. **Unique discriminant:** a prediction that differs between PI's proposed mechanism and at least one strongest competing explanation, plus a simple baseline.
3. **Identification scope:** observable variables, unobserved confounders, A (conditionally identifiable) / B (partially identifiable) / C (presently unidentified), and source-to-target assumptions. This grade is a proposed local classification, never proof of causality.
4. **Pre-result contract:** frozen cases/seeds, rules, primary and adverse outcomes, denominator, stop condition, meaningful comparison, deviations and whether this is exploratory.
5. **Independent evidence:** original record, actual execution receipt, code/data lineage, independent reviewer or explicit NONE, and both supportive and unfavorable metrics.
6. **Affected parties and resources:** voice/veto, practically usable exit, position reversal, third-party harm, recoverability; per-party time, money and imposed audit labor (UNKNOWN, not zero, when unmeasured).
7. **Decision:** exactly one of the states in D24-02, one next smallest reversible action, owner only if voluntarily assigned, expiry/reopen trigger and a testable reason.

If no new observation could discriminate mechanisms, **HOLD_EVIDENCE** rather than increasing simulated complexity or claiming convergence. No single favorable aggregate KPI may silently cancel severe individual harm or lost exit rights. Proportional safety intervention remains a live competing explanation, not a forbidden outcome.

### D24-04. Six-stage interface and ordered bottlenecks

The six existing stages are unchanged. Use one decision receipt across them: **S1** formulate one falsifiable question; **S2** check original prior art and nonwinners; **S3** log bounded coverage, contrary search and unsaturated unknowns; **S4** compare causal identifiability, simplest rival and power reversal; **S5** retain contributor lineage, permissions and burden; **S6** freeze and execute a fair comparison, record negatives and rollback.

**P0 scientific truth:** No automatic advancement from a checklist. Preserve E008 as unexecuted and E009 as an unfavorable mixed-result benchmark. Separately address any main-branch CI/publishing regressions; PR-only green checks do not establish main-branch health.

**P1 smallest blockers:** For E008, fill missing action-level utilities, uncertainty, common horizon/tie rules, **five baseline algorithms**, independent adjudication and participant-specific effects **before** computing the predeclared comparison. For E007 or another chosen mechanism, require an independently specified simple challenger and a blinded check when feasible; availability of an independent evaluator is not assumed.

**P2 diagnostic experiment:** Compare one ICM/voluntary-exit hypothesis with an equally informed simple alternative under high/low power, real/impossible exit, voluntary/strategic agreement and reversal. Predefine one outcome whose observation could disconfirm the claimed incremental value. If A/B/C identification fails, report partial bounds or C/UNKNOWN, not a causal victory.

**P3 external:** Permit narrow promotion only on independently sourced evidence with a stated context. Field interventions affecting people require a separate rights/ethics review; observational or safe synthetic alternatives remain available.

Order is a dependency proposal, not a promise of calendar completion. When budget or access is unavailable, retain a clearly dated HOLD checkpoint; never mistake a resource pause for literature saturation.

### D24-05. Frozen decision examples (not new results)

| Case | Observed record | Permitted decision | Disallowed inference |
|---|---|---|---|
| [E008 executability audit](../experiments/e008/EXECUTABILITY_AUDIT.json) | 16 cases; **0** full five-policy comparison-ready cases; missing quantitative/method inputs | HOLD_EXECUTABILITY. Complete specification and freeze before first valid comparison | E008 shows policy superiority, inferiority or null effect |
| [E009 frozen result](../experiments/e009/RESULT_KO.md) | Internal designer-made synthetic benchmark: PROJECT_V3 mean regret **42.35% worse** than best simple baseline; **failed 3/4 preregistered survival criteria**. Competitive-loss metric favored V3, so outcomes are mixed across metrics | NEGATIVE_PRESERVED for claimed overall V3 benefit. Keep TWO_RULE_SIMPLE and MINIMAL_4VAR; seek independent comparison [per existing gate](E009_INDEPENDENT_DECISION_GATE_EN.md) | All metrics failed; real-world harm proven; independent validation completed; post-hoc retuning erases the original negative result |

Original E009 result, including recovery, severe harm and all denominators, remains in its source files; no metric is replaced by this summary. For E008, a zero-result status is **not** a negative estimate.

### D24-06. Test the roadmap amendment itself and allow reversal

**Control B0:** v0.2.3 decision workflow; **intervention B1:** the same frozen records + D24 decision receipt. On E008, E009 and further independently sampled existing issues (if available), compare: unsupported promotions, important negative evidence missed, correct abstentions, contradictions between SCIENCE and CI state, reviewer correction minutes, added fields and review cost. Freeze sampling/scoring before comparing B0/B1, disclose missing cases and all unfavorable outcomes. This document has **not** executed that test.

**Keep** only decision-changing fields with proportionate cost. **Simplify or disable** burdensome extra checks if they add no observable discrimination, preserving critical rights, source and adverse-evidence safeguards. Do not require more unpaid founder labor, private data, a paid API or an invented independent reviewer. Record provenance and reason for every change.

---

## 원본2 — 한국어 (동등한 전문)

### D24-01. 선행 모범사례 교차표와 이식 한계

| 독립 선행사례 | 추출할 최소 방법 | 적용 경계·반례 |
|---|---|---|
| [DARPA 하일마이어 질문](https://www.darpa.mil/about/heilmeier-catechism) | 연구마다 쉬운 목표, 현재 대안, 차별성, 편익, 위험, 비용·기간, 중간·최종 시험을 명시 | 설득력 있는 연구 설명 자체는 작동 근거가 아님 |
| [OSF 사전등록](https://help.osf.io/article/330-welcome-to-registrations) | 결과를 보기 전에 가설·기준선·제외·결과지표·판정선을 시점 고정하고 이탈 이력을 공개 | 실행 불가능한 사전등록은 여전히 무결과 |
| [NIST AI RMF 플레이북](https://airc.nist.gov/airmf-resources/playbook/) | 거버넌스·맥락·측정·대응을 구분하고 제한적 진행·보류·중단 결정을 기록 | 자발적 위험관리 지침이지 과학실험도 의무 검사목록도 아님 |
| [NASEM 재현·반복 연구 구분](https://nap.nationalacademies.org/resource/25303/R%26R.pdf) | 동일 코드·입력 재실행과 새 자료로 수행한 독립 연구를 구분 | 같은 코드 재실행, 다른 AI의 동의는 독립 과학검증이 아님 |
| [NASA 기술준비도 평가](https://science.nasa.gov/wp-content/uploads/2023/11/tra-tech-showcase-2023-beauchamp-copy.pdf) | 단계 승격 전에 요구 성능·증거·환경·통과 기준을 명시 | NASA TRL 1~9는 기술성숙도이며 PI 사회가설에 점수처럼 대입 금지 |

**이식 검증:** 선행 아이디어와 공로는 원저자에게 귀속한다. PI에 효과가 있다는 주장은 아직 가설이다. v0.2.3 대비 부정근거 누락·거짓 승격·사람의 부담을 비교하고, 결정에 영향이 없는 필드는 폐기한다.

### D24-02. 서로 대체할 수 없는 두 장부

**과학적 증거:** 설계·무결과 → 내부 합성/코드 결과(실행한 경우) → 외부 계산 재현 → 독립 신규 연구 → 맥락 한정 현장 증거. 이는 **증거 종류이며 자동 신뢰점수나 필수 직선 단계가 아니다.** 출처·대상·가정·결과 방향·불확실성·독립성을 표시한다. 재현성이 좋아져도 가설 지지는 부정결과로 낮아질 수 있다. 결측·상충·미식별 증거를 숨기지 않는다.

**운영 무결성:** 문서 구조 검사, Git 재조회, 코드 검사, 영한 의미 검토, 권리 검사, 부정사례 보존은 별도 기록한다. CI 성공은 공존 기제 검증이 아니며 CI 실패가 과학적 부정결과를 코드 오류로 바꾸지도 않는다.

**판정 상태:** GO_SCOPED, HOLD_EVIDENCE, HOLD_EXECUTABILITY, NEGATIVE_PRESERVED, NOT_COMPARABLE, STOP_RISK. 보류는 해당 주장의 무근거 승격을 막으며 **가역적 저위험 연구 전체를 금지하지 않는다.**

### D24-03. 연구 질문별 1장 결정 영수증

활성 질문마다 날짜와 개정 이력을 갖춘 영수증 하나로 통합한다.

1. **질문·계보:** 주장 ID, 원문·원안 언어·인간 발안자, 선행 저자, 변경·복구 참조.
2. **식별 가능한 차이:** PI 가설과 강력한 경쟁가설의 예측이 갈리는 지점, 단순 기준선.
3. **인과 식별 범위:** 관측변수·미관측 교란·A(조건부 식별)/B(부분식별)/C(현재 미식별), 출처에서 적용 대상으로 옮길 때 필요한 가정. 이 구분은 실무 분류안이지 인과성의 증명이 아님.
4. **결과 전 계약:** 사례·난수·규칙·1차/불리한 지표·분모·중단 기준·유효 비교·이탈 기록·탐색 여부.
5. **독립 근거:** 최초 자료, 실제 실행 기록, 코드·자료 계보, 독립검토자 또는 NONE, 유리·불리한 지표 모두.
6. **영향 당사자·자원:** 발언·거부권, 실효 이탈권, 입장반전, 제3자 피해, 복구 가능성, 당사자별 시간·돈·강제된 심사노동(미측정은 UNKNOWN, 0 아님).
7. **결정:** D24-02의 단일 상태, 다음의 최소 가역 행동, 자발적으로 맡은 경우에만 담당자, 만료·재검토 조건과 반증 가능한 이유.

새 관측으로 경쟁 기제를 구별할 수 없다면 **HOLD_EVIDENCE**를 기록한다. 합성모형을 복잡하게 만들거나 수렴을 선언하지 않는다. 한 가지 유리한 집계지표가 개별 중대 피해·이탈권 손실을 상쇄했다고 숨기지 않는다. 비례적인 안전 개입도 경쟁설명으로 유지한다.

### D24-04. 기존 6단계 접속과 병목 우선순위

6단계는 변경하지 않는다. 한 영수증으로 **S1** 반증 질문 명시 → **S2** 선행 원저·실패사례 확인 → **S3** 범위가 한정된 탐색·반대근거·미포화 기록 → **S4** 인과 식별·최소 대안·권력역전 비교 → **S5** 기여자·권한·비용 보존 → **S6** 사전 고정 비교·부정결과·복구를 연결한다.

**P0 과학적 진실성:** 검사 통과만으로 승격 금지. E008은 미실행, E009는 불리한 상충 결과로 유지. 별도의 main CI·공개 안정성 결함을 점검하고 PR 검사 성공을 main 상태로 오인하지 않는다.

**P1 가장 작은 병목:** E008에서 행위별 효용·불확실성·공통 기간·동점 규칙·**5개 기준선 알고리즘**·독립 판정·당사자별 영향을 채운 후 최초 비교 전에 동결한다. E007 또는 선정된 한 기제는 가능한 경우 독립적으로 사양을 고정한 단순 경쟁모형·맹검검사를 준비한다. 독립 평가자의 존재를 가정하지 않는다.

**P2 진단 실험:** ICM·자발적 이탈 가설 하나를 동일 정보의 단순 대안과 비교한다. 강약 권력, 실효/불능 이탈, 자발/전략적 동의, 입장반전을 사전 지정한다. 추가 설명력이 부정될 관측값 하나를 미리 정한다. A/B/C 식별 조건이 성립하지 않으면 부분 경계 또는 C/UNKNOWN으로 기록한다.

**P3 외부 검증:** 출처 독립성과 대상 범위가 확인된 증거에만 한정 승격한다. 사람에게 실제 영향을 주는 현장 개입은 별도 권리·윤리 검토가 필요하며 관찰연구·안전한 합성 대안은 유지한다.

이 순서는 의존관계 제안이지 완료 날짜의 약속이 아니다. 예산·접근권 부족은 날짜 있는 HOLD로 남긴다. 자원 부족을 문헌 포화라고 부르지 않는다.

### D24-05. 동결 증거를 이용한 판단 예시 (신규 실험 아님)

| 사례 | 실제 기록 | 허용 판정 | 금지되는 추론 |
|---|---|---|---|
| [E008 실행가능성 감사](../experiments/e008/EXECUTABILITY_AUDIT.json) | 16사례 중 5정책 전체 비교 가능한 사례 **0개**; 수량·방법 지정 부족 | HOLD_EXECUTABILITY. 사양 완성 후 최초 비교 전 동결 | E008이 정책 우월·열등 또는 무효를 입증 |
| [E009 동결 결과](../experiments/e009/RESULT_KO.md) | 연구자가 설계한 내부 합성시험에서 PROJECT_V3의 평균 regret은 최선 단순 기준보다 **42.35% 악화**, 사전등록 존속 기준 **4개 중 3개 실패**. 경쟁손실 지표는 V3에 유리하여 지표별 상충 존재 | V3의 전체 우월 주장에 NEGATIVE_PRESERVED. TWO_RULE_SIMPLE·MINIMAL_4VAR 유지; [기존 외부검토 경로](E009_INDEPENDENT_DECISION_GATE_KO.md) 사용 | 모든 지표 실패, 현실 피해 입증, 독립검증 완료, 사후 튜닝으로 기존 부정결과 삭제 |

복구·중대피해·전체 분모 등 E009 원자료 지표는 원본 파일에 그대로 둔다. E008 무결과는 음의 효과 추정치가 아니다.

### D24-06. 로드맵 수정안 자체의 반증·복구

**B0:** v0.2.3 기존 판단 과정. **B1:** 같은 동결 기록에 D24 영수증을 적용. E008·E009 및 확보 가능한 독립 선정 과거 이슈에서 무근거 승격, 중대 부정근거 누락, 적절한 보류, 과학·CI 상태의 충돌, 사람의 수정 시간, 증가한 기록·검수 비용을 비교한다. 사례 선정·평가기준은 결과를 보기 전에 고정하고 누락과 불리한 결과도 보고한다. **이 시험은 아직 실행하지 않았다.**

결정에 실질 영향을 주고 비용이 비례하는 필드만 **유지**한다. 도움이 없는 추가 검사 부담은 **단순화·비활성화**하되 권리·원출처·부정근거 보호는 보존한다. 창시자의 추가 무급노동·비공개 정보·유료 API·가상의 독립검토자를 요구하지 않는다. 변경마다 출처와 복구 이유를 남긴다.

---

**Change receipt / 변경 영수증:** v0.2.4 additive research-method proposal only. No six-stage replacement, experimental run, baseline overwrite, rights adjudication, independent review or main-branch merge. / 기존 정본·6단계·부정결과·원기여를 유지한 방법 보충 제안. 과학적 성과나 외부 독립검증을 주장하지 않음.

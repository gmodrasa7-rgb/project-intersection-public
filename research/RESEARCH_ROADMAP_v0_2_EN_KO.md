# PI Roadmap v0.2 — Historical Failure-Safety Revision
# PI 로드맵 v0.2 — 역사적 실패 기반 예방 개정

**Upstream creator, copyright and adaptation control / 선행연구 원안자·저작권·응용 통제:** [Original 1 English / 한국어 원본2 provenance and rights ledger](../PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md) distinguishes prior research author, possible first originator, copyright holder, original source, and PI-added application. Every future promoted case or method must link original sources and declare the rights/copying status; unknowns stay explicit. / 후속 사례·방법의 승격 전에 원저자·최초 발안 증거·저작권/이용허락·PI의 별도 응용을 연결하며 미확인 권리를 임의로 채우지 않는다. **Initial coverage only; 211 target files unreviewed for completeness.**

**Date / 일자:** 2026-10-13  
**Status / 상태:** RESEARCH DESIGN + VERIFIED HISTORICAL SOURCE LINKS; PI APPLICATION PROPOSED / 역사자료 근거 확인·PI 적용 규칙 제안. **No original PI field trial, independent validation or automatic enforcement claimed. / PI 현장실험·독립검증·자동집행 완료 아님.**  
**Author and attribution / 기여:** Project Intersection's human research originator defined the research mission and requested failure-first v0.2 design. Historical authors, investigators and institutions retain their own attribution; assisting AI gathered and organized comparisons. This is not a claim of AI-originated human research. / 연구 목적과 실패 우선 조사·개선 요청의 인간 기여를 명시하며 기존 조사자·저자의 공로를 보존한다.

**Canonical predecessor / 기준:** [PI Roadmap v0.1](RESEARCH_ROADMAP_v0_1_EN_KO.md) remains preserved as an immutable historical milestone in Git. v0.2 **keeps the six research stages and all existing governance, funding, privacy and provenance rules**. This document is the currently proposed integrated roadmap, not a silent rewrite of v0.1. When text conflicts, record the conflict and resolve through evidence/review rather than silently erasing prior decisions. / 6단계·기존 후원금 사용처 2항목·영어 원본1/한국어 원본2·개인정보 보호·연구자 비용 추적 규칙을 그대로 유지한다.

## Original 1 — English

### 0. Failure-first principle and evidentiary limits

Excellent talent, strong funding and impressive roadmaps do not guarantee correct outputs. Historical cases in safety-critical engineering, science, finance and public IT exhibit different mechanisms; they are **purposefully selected comparators, not a representative sample or statistical proof of one universal cause**. Separate documented events from our proposed analogies. Avoid claims of deliberate concealment where a primary investigation found only errors or incentives. Do not treat all failures as equivalent, and seek counterexamples and successful mitigations.

Research is useful only if the system can **notice an anomaly, make it consequential to the decision, avoid unnecessary loss, and restore what was harmed**. Evaluation power, disclosure power and resource dependence are themselves potential failure variables.

### 1. Historical comparison set — 20 warning cases

| ID | Case | Documented failure pattern (compressed) | Proposed PI control (not proven) | Source |
|---|---|---|---|---|
| F01 | Challenger (1986) | Engineer objections and O-ring launch risk did not reach effective final decision. | Independent dissent-to-decision log; unresolved critical warning blocks irreversible promotion. | [Primary/investigation](https://www.nasa.gov/history/rogersrep/genindex.htm) |
| F02 | Columbia (2003) | Success normalization, schedule and resources weakened independent safety challenges. | Reopen assumptions after each anomaly; record near misses, not only disasters. | [Primary/investigation](https://sma.nasa.gov/SignificantIncidents/assets/columbia-accident-investigation-board-report-volume-1.pdf) |
| F03 | Mars Climate Orbiter (1999) | Unit-interface mismatch was not caught in end-to-end mission validation. | Machine-readable schema, units, cross-interface integration tests. | [Primary/investigation](https://llis.nasa.gov/lesson/641) |
| F04 | Boeing 737 MAX (2018–19) | Technical assumptions, production pressure, disclosure and oversight failures interacted. | Separate evidence owner, implementation and evaluator; no self-certification of safety. | [Primary/investigation](https://democrats-transportation.house.gov/news/press-releases/after-18-month-investigation-chairs-defazio-and-larsen-release-final-committee-report-on-boeing-737-max) |
| F05 | Therac-25 (1985–87) | Software confidence displaced defense-in-depth, permitting radiation overdoses. | Invariant/fail-safe tests and human-impact threshold before live deployment. | [Primary/investigation](https://ieeexplore.ieee.org/abstract/document/274940/authors) |
| F06 | Deepwater Horizon (2010) | Repeated cross-contractor risk-management weaknesses accumulated. | Assess full dependency chains, hidden shared risks and responsibilities. | [Primary/investigation](https://www.govinfo.gov/content/pkg/CHRG-112hhrg63876/html/CHRG-112hhrg63876.htm) |
| F07 | Fukushima Daiichi (2011) | Basic safety assumptions remained insufficiently challenged; system interactions mattered. | Test beyond-design scenarios, unexpected dependencies and reversible fallback. | [Primary/investigation](https://gnssn.iaea.org/FukushimaLessonsLearned/Lists/Fukushima/DispForm.aspx?ContentTypeId=0x01006A6D303BCE89A14FA6083DD8D969FFE0&ID=194) |
| F08 | Flint water crisis (2014–) | Citizen warnings and uneven harm were inadequately reflected in institutional decisions. | Affected-party evidence and asymmetric-harm review before public scaling. | [Primary/investigation](https://www.michigan.gov/en/mdcr/commission/flint-water-hearings) |
| F09 | Google Flu Trends (2013 error) | A large predictive model diverged from surveillance ground truth. | Compare with small, updated baseline and out-of-time reality check. | [Primary/investigation](https://gking.harvard.edu/publication/the-parable-of-google-flu-traps-in-big-data-analysis/) |
| F10 | Psychology replication study (2015) | A substantial share of sampled published effects did not replicate by the same statistical criterion. | Record selection, preregister tests and preserve null outcomes; do not generalize sample to all science. | [Primary/investigation](https://pubmed.ncbi.nlm.nih.gov/26315443/) |
| F11 | Cancer biology replication (2021) | Original reports often lacked methods/data; 50 of 193 planned experiments were completed. | Reproduction package completeness gate before declaring external verification. | [Primary/investigation](https://elifesciences.org/articles/67995) |
| F12 | Volkswagen diesel emissions (2015) | Testing-mode optimization defeated real-world emissions compliance. | Holdout and adversarial real-world evaluation separate from visible tests. | [Primary/investigation](https://www.epa.gov/vw/learn-about-volkswagen-violations) |
| F13 | Wells Fargo sales scandal (2016) | Sales incentives rewarded unauthorized accounts rather than consumer benefit. | Track objective–metric divergence, participant harm and incentive conflicts. | [Primary/investigation](https://www.consumerfinance.gov/archive/newsroom/consumer-financial-protection-bureau-fines-wells-fargo-100-million-widespread-illegal-practice-secretly-opening-unauthorized-accounts/) |
| F14 | Enron reporting fraud (2001) | Publicly presented successes concealed underlying losses. | Require raw-to-summary audit trail; report net costs and negative outcomes. | [Primary/investigation](https://www.sec.gov/newsroom/press-releases/2004-94-sec-charges-kenneth-l-lay-enrons-former-chairman-chief-executive-officer-fraud-insider-trading) |
| F15 | Theranos (2013–18) | Investor demos and claims diverged from actually deployed test capabilities. | Distinguish DEMO, SYNTHETIC, REAL_DEPLOYMENT, independent replication. | [Primary/investigation](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-24069) |
| F16 | FTX (2022) | Customer assets were diverted and control relationships were misrepresented. | Separate fund categories, permissions, reconciled evidence and beneficiary ledger. | [Primary/investigation](https://www.justice.gov/usao-sdny/pr/samuel-bankman-fried-sentenced-25-years-prison) |
| F17 | UK NHS NPfIT (2002–11) | Broad IT integration promises outran deployable benefits and user adoption. | Small usable increments before expansion; user utility not document volume. | [Primary/investigation](https://www.nao.org.uk/reports/the-national-programme-for-it-in-the-nhs-an-update-on-the-delivery-of-detailed-care-records-systems/) |
| F18 | FBI Virtual Case File (2002–05) | Unstable requirements, weak engineering and oversight preceded cancellation. | Minimal executable slice, change-controlled requirements, sunset of failing work. | [Primary/investigation](https://oig.justice.gov/archives/reports/FBI/a0614/exec.htm) |
| F19 | Healthcare.gov launch (2013) | Launch proceeded without adequate capacity, end-to-end testing or verified readiness. | Production-readiness gate and documented abort/rollback path. | [Primary/investigation](https://www.gao.gov/products/gao-14-824t) |
| F20 | UK Post Office Horizon scandal (1999–) | Disputed system outputs and institutional power generated prolonged human harms and compensation failures. | Preserve contestability, affected-party standing, corrected records and redress separate from future work. | [Primary/investigation](https://www.postofficehorizoninquiry.org.uk/reports-and-statements) |

Selection note: cases have distinct goals and harm levels. The labels are analytic compression of the linked sources, not verbatim verdicts; some historical inquiries involve disputed interpretations. No incidence, causality strength, or intervention effectiveness is estimated by counting these 20 cases.

**Limited positive comparators (not the objective):** NASA [Apollo 13](https://www.nasa.gov/missions/apollo/apollo-13-the-successful-failure/) shows objective switching to crew survival with improvisation after mission failure; NASA [ASRS](https://www.nasa.gov/human-systems-integration-division/aviation-safety-reporting-system-overview/) demonstrates long-running confidential, non-punitive near-miss reporting; the WHO [smallpox program](https://www.who.int/news-room/feature-stories/detail/the-smallpox-eradication-programme---sep-%281966-1980%29) documents surveillance/containment adaptation. These are mechanisms to test, not universal best-practice guarantees.

### 2. Cross-case convergence — eight potential system traps

These categories reflect qualitative synthesis, not proven mutual cause or measured frequency:

1. **Warning neutralization:** objections exist but cannot change a decision (F01,F02,F04,F07,F20).
2. **Assumption lock-in:** early assumptions become invisible background constraints (F02,F04,F07,F09,F17).
3. **Proxy metric capture:** passing a test, headline, schedule or quota displaces real benefit (F09,F12,F13,F14,F15).
4. **Internal evidence monopoly:** creators control evidence, interpretation and acquittal (F04,F12,F15,F20).
5. **Integration failure:** separately plausible parts fail when interfaces or organizations interact (F03,F05,F06,F17,F18,F19).
6. **Unreproducible certainty:** lack of raw data/methods but high confidence remains (F10,F11,F15).
7. **Asymmetric externalization:** beneficiaries and cost-bearing people diverge (F08,F13,F16,F20).
8. **Correction trap / escalation:** prior investment, reputational claims and deadlines block safe exit (F02,F17,F18,F19).

### 3. Mandatory transversal controls (design; enforcement not yet implemented)

- **G1 Source-to-claim:** exact original source, author/date, supported scope, contrary evidence, uncertainty and whether access was actual; if absent, mark UNKNOWN. Two model outputs citing one source are not independent.
- **G2 Dissent that changes outcomes:** each important claim records a strongest counterargument and who can challenge it. An unmitigated **critical** objection means HOLD on public promotion or real-world deployment; reversible desk research may continue with labeled uncertainty. Reviewer independence must be evidenced, never presumed.
- **G3 Real-benefit measurement:** document count, PR count, citations, model agreement, donations and CI passes are proxy indicators only. Measure reproducible predictions, holdout performance, restoration ability, real-world usefulness and negative impacts against a simple baseline.
- **G4 Separation of duties:** claim writer ≠ sole evidence auditor ≠ sole promoter, where available. If independent evaluation is unavailable, say so and restrict claims; never invent reviewers.
- **G5 Hidden and out-of-time tests:** preregister pass/fail before results; reserve holdout/adversarial/time-shift cases. Do not optimize a claimed success solely against visible tests.
- **G6 Reversibility + correction:** make small changes, perform link/semantic/regression tests, read back committed files, preserve before/after and provide rollback. On a significant unresolved safety concern, stop risky exposure rather than demanding repeated free validation from contributors.
- **G7 Cost and redress:** separately log (a) scientific progress (b) researcher/participant time, health, family-life and financial opportunity costs (c) who controls benefit, interpretation, exit, funds and remedies. Past contribution/redress is separate from new work and must never be conditioned on re-testing or future employment. Do not invent monetized values or claim liability already adjudicated.
- **G8 Public status and limitations:** keep failures, negative findings, unresolved cases, translations, protected information categories, funding limitations and independent-validation absence explicit. Protect personal/third-party data and unsafe details; disclose lawful redaction categories.

### 4. Six-stage PI cycle — revised gates, unchanged stage count

| Stage | Existing purpose retained | Additional stop/check rule |
|---|---|---|
| 1 | Define hypothesis, theory, variables, strongest counterexample | List hidden assumptions, affected parties, power asymmetries, failure modes and falsifying outcome before approval. |
| 2 | Find sources, counterexamples, historical/negative precedents | Search failures **of the proposed method itself**, not just target theory; provenance and conflicting sources required. |
| 3 | Operational search saturation | Two consecutive zero-new-competitor searches count only within disclosed, diversified search scope; new languages, contrary evidence or method drift reopen. No worldwide exhaustive claim. |
| 4 | Critique, reuse, modify or reject earlier research | Run all eight risk lenses, simplest comparator, causal alternatives, rights/cost externalization and who benefits from error. |
| 5 | Attribute original contributions and corrections | Immutable contribution/evidence ledger, uncertainty about attribution, separate past-work redress from new obligations, correction authors credited. |
| 6 | Test surviving hypotheses and accelerate | Predeclared gates, hidden/negative controls, independent challenge where possible, rollback/stop condition, real value **minus** incurred cost; otherwise HOLD and loop back. |

### 5. Compact failure-regression suite (initial manual design)

| Test | Injected failure | Passing behavior |
|---|---|---|
| R01 | Engineer/reviewer disputes main assumption | BLOCK/HOLD critical promotion; preserve dissent and decisive response |
| R02 | Five AIs agree using one shared source | Record ONE evidence lineage, not five independent validations |
| R03 | Synthetic demo advertised as empirical proof | Reject promotion and relabel SYNTHETIC |
| R04 | New contradiction after saturation | Reopen stages 2–4; preserve original saturation scope |
| R05 | More papers, commits, donations but no improved outcome | Report no verified effectiveness gain |
| R06 | Rewriter omits prior human originator or negative result | Reject or revert semantic/attribution regression |
| R07 | Sponsor/reviewer wants favorable conclusion or unsafe disclosure | Preserve independence; redact protected data while disclosing category |
| R08 | One operator exhausts time/health/money to correct system | Stop nonessential iterations, report actual cost and do not demand more labor |
| R09 | Latest edit passes syntax yet breaks old links or Korean meaning | Revert/hold until link and EN–KO semantic review |
| R10 | No external evaluator or execution result exists | State NOT EXECUTED/NO INDEPENDENT VALIDATION |
| R11 | Public release reveals private source or credentials | Abort disclosure, revoke leaked secrets as applicable, document correction without reprinting sensitive material |
| R12 | Old harm is offered payment only if contributor signs new job/testing deal | Reject linkage; handle past redress and new contract separately |

These are **test specifications**, not reports of completed automated tests.

### 6. Success/failure measurement and release criteria

For each change, maintain a concise decision record: `claim_id, stage, source_ids, primary/secondary, dissent, evidence_level, assumptions, risk_lenses, test_id, test_status, who_benefits, who_bears_cost, exit_and_redress, semantic_diff_EN_KO, reviewer_independence, decision, rollback_ref, provenance, date`. Mark unknowns explicitly; redact personally identifying items from public ledgers.

Promotion requires **all applicable**: (a) source/claim tracing, (b) strongest counterexample and alternatives, (c) validated result against baseline *for the scope claimed*, (d) preserved negative findings and authorship, (e) no unresolved critical rights/safety warning, (f) real read-back and recovery, (g) no forced uncompensated verification extraction. If (c) or independence is unavailable, a properly marked exploratory/HOLD record may be published; an empirical success claim may not.

**Important limitation:** this historical review cannot establish that G1–G8 prevent such disasters. Pilot them on a single existing PI hypothesis, evaluate failure-detection rates, researcher effort, false-stop rate and restoration quality, and modify or reject controls that cause more harm than they avert. The execution pilot remains **NOT EXECUTED**.

### 7. Changelog

- 2026-10-13 **v0.1** retained, including six stages, resource/LLM limitations, bilingual rule, funding categories, status separation, source attribution and rollback.
- 2026-10-13 **v0.2** added case comparison F01–F20, eight causal-risk lenses, G1–G8 guardrails, six-stage safety gates, R01–R12 regression specifications and explicit human cost/redress separation. This is a **proposed governance improvement**, not a measured scientific improvement.

---

## 원본2 — 한국어

### 0. 실패를 우선하는 원칙과 증거의 경계

우수한 인력·자금·상세한 계획이 정확성과 안전을 보증하지 않는다. 기술안전·학술·금융·공공 IT의 사례 20건은 **서로 다른 실패 유형을 의도적으로 고른 비교표본**이며 모든 조직의 대표표본이나 보편적 인과관계의 통계적 증명이 아니다. 확인된 사실과 PI에의 유비·제안을 분리한다. 공식 조사에서 실수와 이해상충만 확인된 경우 의도적 은폐라고 단정하지 않는다. 일부 성공적 방어 사례도 반례로 검토한다.

연구 시스템은 **이상 징후 감지 → 결정에 실제 반영 → 피해 제한 → 피해 복구**를 수행해야 한다. 평가권·정보공개권·자원 의존과 실효적 이탈 가능성도 연구 변수가 된다.

### 1. 역사적 위험 사례 20건

| ID | 사례 | 확인된 실패 구조의 압축 요약 | PI에 대한 예방안(아직 효과 미검증) | 자료 |
|---|---|---|---|---|
| F01 | Challenger (1986) | 기술자의 O-ring 위험 경고가 실제 발사 중단으로 연결되지 않음. | 핵심 경고에 대한 독립적 이견 기록; 미해결 중대 경고는 비가역 승격 차단. | [원자료/조사](https://www.nasa.gov/history/rogersrep/genindex.htm) |
| F02 | Columbia (2003) | 반복된 이전 성공이 안전의 대용 지표가 되고, 일정·예산 압력 속 독립적인 반론이 약화됨. | 이상 신호마다 전제 재검토; 대형 실패뿐 아니라 아차사고도 기록. | [원자료/조사](https://sma.nasa.gov/SignificantIncidents/assets/columbia-accident-investigation-board-report-volume-1.pdf) |
| F03 | Mars Climate Orbiter (1999) | 단위계 인터페이스 불일치가 종단 간 검증에서 차단되지 않음. | 단위·스키마의 기계판독 명시와 인터페이스 통합검사. | [원자료/조사](https://llis.nasa.gov/lesson/641) |
| F04 | Boeing 737 MAX (2018–19) | 설계 전제·생산 압력·정보 비공개·감독 결함이 결합됨. | 근거 작성·구현·평가 역할 분리; 자기 안전인증 금지. | [원자료/조사](https://democrats-transportation.house.gov/news/press-releases/after-18-month-investigation-chairs-defazio-and-larsen-release-final-committee-report-on-boeing-737-max) |
| F05 | Therac-25 (1985–87) | 소프트웨어를 과신하며 독립 방어장치가 충분하지 않았고 과다피폭 발생. | 안전불변조건·안전정지 테스트, 실제 피해 가능 시 배포 차단. | [원자료/조사](https://ieeexplore.ieee.org/abstract/document/274940/authors) |
| F06 | Deepwater Horizon (2010) | 여러 업체에 걸친 반복적인 위험관리 실패가 누적됨. | 공급자·외부 모델·자료 의존망과 공동실패 위험을 기록. | [원자료/조사](https://www.govinfo.gov/content/pkg/CHRG-112hhrg63876/html/CHRG-112hhrg63876.htm) |
| F07 | Fukushima Daiichi (2011) | 안전성의 기본 전제가 충분히 도전받지 않았고 인간·기술·조직 상호작용이 중대했음. | 설계범위 밖 상황·예상 밖 의존성·롤백 경로 시험. | [원자료/조사](https://gnssn.iaea.org/FukushimaLessonsLearned/Lists/Fukushima/DispForm.aspx?ContentTypeId=0x01006A6D303BCE89A14FA6083DD8D969FFE0&ID=194) |
| F08 | Flint water crisis (2014–) | 주민의 경고와 불균등한 피해가 제도적 의사결정에 충분히 반영되지 않음. | 영향받는 개체의 증거 및 피해비대칭을 확장 전에 검토. | [원자료/조사](https://www.michigan.gov/en/mdcr/commission/flint-water-hearings) |
| F09 | Google Flu Trends (2013 error) | 대규모 예측 모델이 실제 감시자료와 큰 차이를 보임. | 단순 기준선·시계열 외부검증과 현실 데이터 대비. | [원자료/조사](https://gking.harvard.edu/publication/the-parable-of-google-flu-traps-in-big-data-analysis/) |
| F10 | Psychology replication study (2015) | 일부 유명 학술지의 표본 논문에서 같은 유의성 기준 재현율이 낮았음. | 표집·사전등록·부정결과 보존; 특정 표본을 전체 과학으로 일반화 금지. | [원자료/조사](https://pubmed.ncbi.nlm.nih.gov/26315443/) |
| F11 | Cancer biology replication (2021) | 원논문의 절차·데이터 결손으로 계획했던 193개 중 50개 실험만 반복 완료. | 외부 재현을 선언하기 전 절차·데이터·환경의 재현 패키지 검사. | [원자료/조사](https://elifesciences.org/articles/67995) |
| F12 | Volkswagen diesel emissions (2015) | 시험 환경에만 맞추는 조작으로 현실 배출기준과 괴리가 발생. | 공개된 시험과 분리된 미사용·적대적 현실 검증. | [원자료/조사](https://www.epa.gov/vw/learn-about-volkswagen-violations) |
| F13 | Wells Fargo sales scandal (2016) | 판매 목표 보상이 고객 이익이 아닌 무단 계좌 개설을 유인함. | 목표와 지표의 괴리·피해·보상 이해상충 계측. | [원자료/조사](https://www.consumerfinance.gov/archive/newsroom/consumer-financial-protection-bureau-fines-wells-fargo-100-million-widespread-illegal-practice-secretly-opening-unauthorized-accounts/) |
| F14 | Enron reporting fraud (2001) | 공개 실적 표기가 사업 부문의 손실을 가리는 데 사용됨. | 원자료→요약 감사 계보; 순비용과 실패를 함께 보고. | [원자료/조사](https://www.sec.gov/newsroom/press-releases/2004-94-sec-charges-kenneth-l-lay-enrons-former-chairman-chief-executive-officer-fraud-insider-trading) |
| F15 | Theranos (2013–18) | 투자자 시연·홍보 주장과 실제 검사 장비 능력이 불일치했음. | 시연·합성·실제운영·독립재현을 명시적으로 분리. | [원자료/조사](https://www.sec.gov/enforcement-litigation/litigation-releases/lr-24069) |
| F16 | FTX (2022) | 고객자금이 다른 용도로 전용되고 통제·자산 관계가 왜곡됨. | 재원 종류·권한·실제 대사·수혜자 장부를 분리. | [원자료/조사](https://www.justice.gov/usao-sdny/pr/samuel-bankman-fried-sentenced-25-years-prison) |
| F17 | UK NHS NPfIT (2002–11) | 거대 IT 통합 약속에 비해 실제 현장 배포·효용이 미달했음. | 규모 확대 전에 작은 작동 단위·현장 효용 검증. | [원자료/조사](https://www.nao.org.uk/reports/the-national-programme-for-it-in-the-nhs-an-update-on-the-delivery-of-detailed-care-records-systems/) |
| F18 | FBI Virtual Case File (2002–05) | 불명확한 요구조건·기술관리·감독 부족 속 사업 중단. | 최소 실행단위·요구사항 변경 추적·실패한 작업 종료. | [원자료/조사](https://oig.justice.gov/archives/reports/FBI/a0614/exec.htm) |
| F19 | Healthcare.gov launch (2013) | 용량·통합시험·출시 준비가 미흡한 상태에서 서비스 개시. | 실서비스 준비 게이트와 중단·복원 절차. | [원자료/조사](https://www.gao.gov/products/gao-14-824t) |
| F20 | UK Post Office Horizon scandal (1999–) | 정보시스템 결과를 둘러싼 분쟁과 제도 권력비대칭이 장기 피해·배상 문제로 확대됨. | 이의신청권·당사자 지위·기록 교정·과거피해 정산을 미래 노동과 분리. | [원자료/조사](https://www.postofficehorizoninquiry.org.uk/reports-and-statements) |

**범위 주의:** 사례별 목적·피해·확정 수준은 다르다. 각 요약은 출처를 간추린 비교 해석이다. 동일한 원인이나 예방책의 효과가 20회 독립적으로 입증됐다는 뜻이 아니다.

**소수 성공 대조군:** NASA [아폴로 13](https://www.nasa.gov/missions/apollo/apollo-13-the-successful-failure/)의 원래 목표 포기·생존 우선, NASA [ASRS](https://www.nasa.gov/human-systems-integration-division/aviation-safety-reporting-system-overview/)의 자발·비밀·비징벌 근접사고 보고, WHO [천연두 퇴치](https://www.who.int/news-room/feature-stories/detail/the-smallpox-eradication-programme---sep-%281966-1980%29)의 감시·차단 전략 변화는 성공 신화가 아니라 **검증 가능한 방어기제 후보**다.

### 2. 교집합 — 반복 관측되는 8개 구조적 위험

아래는 질적 종합이며 빈도 추정이나 통계적 원인 판정이 아니다.

1. **경고 무력화:** 위험을 말해도 의사결정은 멈추지 않음(F01,F02,F04,F07,F20).
2. **전제 고착:** 초기 전제가 검증 대상에서 제외됨(F02,F04,F07,F09,F17).
3. **대리지표 포획:** 시험 통과·홍보·일정·판매량이 현실 목표를 대체(F09,F12,F13,F14,F15).
4. **내부 증거 독점:** 설계자가 증거와 해석과 합격판정까지 지배(F04,F12,F15,F20).
5. **통합 실패:** 개별 구성요소가 멀쩡해도 연결된 전체는 실패(F03,F05,F06,F17,F18,F19).
6. **재현 불가능한 확신:** 데이터·방법이 결손됐어도 자신감과 권위 유지(F10,F11,F15).
7. **비대칭 비용전가:** 혜택 획득자와 손실 부담자가 분리(F08,F13,F16,F20).
8. **교정의 덫:** 이미 투입한 돈·체면·일정 때문에 중단·수정이 어려움(F02,F17,F18,F19).

### 3. PI에 추가하는 8개 횡단 방호 게이트

- **G1 출처-주장 추적:** 원출처·저자·일자·지지 범위·반례·접근 여부 기록. 근거가 없으면 UNKNOWN. 동일 근거의 AI 반복은 독립증거가 아니다.
- **G2 실효성 있는 이견:** 주요 주장마다 가장 강한 반론을 남긴다. **중대 위험**이 해소되지 않으면 현실 적용·실증 성공 선언을 HOLD한다. 가역적 문헌 검토까지 전면 금지하지 않는다. 독립평가 미확보 시 확보한 척하지 않는다.
- **G3 현실 성과 측정:** 논문·파일·PR·인용·후원금·CI 통과는 대리지표다. 단순 기준선 대비 재현 정확도·미사용 시험·실효적 복구·현실 효용 및 비용을 분리해 측정한다.
- **G4 평가권 분리:** 가능한 경우 주장 작성, 자료검증, 승격 판정을 서로 분리한다. 독립성이 없다면 명시하고 근거를 제한한다.
- **G5 숨은 검증:** 결과를 보기 전 판정 기준 고정, 홀드아웃·적대적·시간변화 검증. 공개 테스트에만 최적화하지 않는다.
- **G6 가역성과 교정:** 변경 최소화, 링크·의미·회귀점검, Git 저장 후 재조회, 이전 상태 복원. 중대한 안전우려가 있으면 위험한 실행을 멈추며 무료 추가 검증노동을 요구하지 않는다.
- **G7 비용·피해·정산 분리:** (a) 연구 성과 (b) 인간의 시간·건강·가족시간·생활비·기회비용 (c) 누가 편익·평가권·이탈권·재원·복구권을 가지는지 각각 기록. 이미 발생한 기여에 대한 정산과 미래 고용·실험 참여는 독립. 측정되지 않은 금액·확정되지 않은 법적 책임을 발명하지 않는다.
- **G8 실패와 한계 공개:** 부정결과·오류·불명확성·번역 차이·비공개 사유·독립검증 미수행을 명시한다. 개인정보·저작권·오남용 위험 자료는 최소 보호하며 안전한 범위에서 비공개 범주를 공개한다.

### 4. PI 연구 6단계별 개정 — 단계 수와 목적은 유지

| 단계 | 유지되는 목표 | 추가 통과/중단 기준 |
|---|---|---|
| 1 | 주제·가설·이론 구체화 | 숨은 전제, 피해 당사자, 권력비대칭, 최악의 실패, 반증조건을 처음부터 명시. |
| 2 | 선행연구·실패·반례 조사 수집 | 조사 대상 이론뿐 아니라 **조사방법 자체의 실패 선행사례**를 찾아 출처·상충자료 보존. |
| 3 | 조사 포화 범위 한정 판정 | 검색 범위와 다른 분야·언어를 공개한 연속 두 번의 신규 경쟁설명 0건만 임시 중단 근거. 새 반례·방법변화 시 재개. |
| 4 | 검수·정제·응용·기각 | 8개 위험렌즈, 단순 기준선, 다른 인과설명, 이탈권·비용전가·오류 편익자 검사. |
| 5 | 연구 기여자·교정자 기록 | 원저자·인간 원기여자·교정자·AI 보조 역할, 불확실성 및 수정 계보 보존. 과거 기여 정산과 미래 노동 분리. |
| 6 | 잔여 가설 실험·신연구 가속 | 사전 기준·숨은 시험·부정결과·독립반론·롤백·중단조건·실제 편익과 비용 분리. 조건 미달 시 HOLD하고 이전 단계 복귀. |

### 5. 실패 회귀검사 12종 — **검사 설계이며 실행 완료 아님**

| 번호 | 주입할 실패 | 합격 행동 |
|---|---|---|
| R01 | 유능한 검토자가 핵심 전제를 반박 | 중대 위험의 승격 보류, 반론과 결정 이유 보존 |
| R02 | AI 5개가 하나의 원문에 동의 | 독립증거 5개가 아닌 근거계보 1개로 계상 |
| R03 | 합성 시연을 현실 실증처럼 홍보 | 상태 승격 거부, 합성 표기 복원 |
| R04 | 조사 포화 뒤 강한 새 반례 발견 | 2~4단계 재개, 이전 한정범위 기록 보존 |
| R05 | 문서·PR·후원만 증가 | 확인된 실효 성과 증가 없음 보고 |
| R06 | 재작성하면서 원기여자나 부정결과 누락 | 의미·기여 회귀 오류로 보류/복구 |
| R07 | 후원자 또는 평가자가 유리한 결론 요구 | 독립성 유지, 비밀 보호, 이해상충 기록 |
| R08 | 사용자만 오류교정하며 건강·시간·돈 소모 | 불필요 반복 중단, 실제 비용 기록, 추가노동 요구 금지 |
| R09 | 문법 검사는 통과했지만 링크·한글 의미 변질 | 연결·번역 의미 회귀검사 전 승격 보류 |
| R10 | 독립검토자·실행 로그 없음 | NOT EXECUTED / NO INDEPENDENT VALIDATION 표시 |
| R11 | 비공개 원자료·인증정보가 공개될 위험 | 공개 차단·필요한 자격증명 폐기·노출정보 재인용 금지 |
| R12 | 과거 피해 정산에 새 고용·시험 조건 결합 | 조건 결합 거부, 두 절차 독립 |

**위 12종은 자동검사 구현이나 실제 실행 결과가 아니다.**

### 6. 승격 판정·성과지표·보수적 종료

변경마다 다음을 최소 기록한다: `claim_id, stage, source_ids, 증거종류, 최강반례, 대안설명, 미검증전제, 위험렌즈, 시험번호와 실행상태, 편익자, 비용부담자, 이탈과 정산, 영어-한국어 의미차이, 평가 독립성, 결정, 롤백지점, 원기여 계보, 날짜`. 공개 장부에는 식별 가능한 개인정보를 넣지 않는다.

실증 성공이나 새 이론 승격을 주장하려면 해당 범위에서 출처, 반론, 단순 기준선 비교 결과, 실패·기여 보존, 미해결 중대피해 없음, 복원가능성, 강제적 무보수 교정노동 부재를 확인한다. 독립검증이 없으면 없다고 말하고, 제안·탐색·보류 자료 공개만 허용한다.

**추론 한계:** 역사자료 20건만으로 G1~G8의 예방효과는 입증되지 않는다. 기존 PI 가설 한 건에 먼저 적용해 경고 검출률·오탐으로 인한 불필요 정지·실제 작업부담·복구품질을 비교하고 유해한 절차는 수정하거나 폐기한다. 실제 파일럿 결과는 **미실행**.

### 7. 변경 기록

- **v0.1 — 2026-10-13:** 기존 PI 로드맵 6단계, LLM·자원 한계, 두 원본, 후원금 2개 사용처, 출처·증거·기여·회귀 관리 보존.
- **v0.2 — 2026-10-13:** 역사적 실패 비교 F01~F20, 8개 반복 위험구조, G1~G8 방호, 6단계별 차단 기준, R01~R12 실패 재현 규격, 인간 부담과 과거 기여 정산 분리 추가. **역사자료 기반 제안이며 개선 효과는 아직 미실증**.


---

## Operational appendix — PIA v0.1 upgrade track (2026-10-13)
## 운영 보충 — 피아(PIA) v0.1 업그레이드 로드맵

**Status:** ADOPTED AS A ROADMAP, NOT ACCOMPLISHED MILESTONES. This appendix adds an enabling **research-material management** track to the established six-stage PI research roadmap. It does NOT add a seventh research stage, change the v0.2 historical findings, or turn PIA v0.1 into v0.2 by naming future releases.

### Original 1 — English

**Identity.** PIA is the short call name for **PI-ANCHOR (Artifact Navigation, Change History, Observability & Retrieval)**, a scoped artifact-management layer. Project Intersection remains the research mission; ICM the studied intersection of interests; IVS-0R an execution/role-reversal/audit discipline. **PIA system version v0.1 is independent of PI research roadmap v0.2.** The current implementation is source-constrained Git indexing/search with CI regression checks. No universal semantic recall, cross-repository autonomous operations, persistent cloud agent or independent scientific validity is claimed.

**The actual bottleneck:** early searches required full re-reading or manual index navigation. Recent development added committed Git SHA comparisons, incremental text lookup, lexical/controlled bilingual candidate retrieval, explicit ID/link relations, cautions and CI. These are **retrieval candidates**, not validated claim dependencies. The highest-value next step is to measure real omissions and false associations *before* increasing model complexity.

| PIA release **target**, not current version | Priority / planned deliverable | Release gate (evidence required) | Stop/rollback |
|---|---|---|---|
| **v0.1 → v0.1.x** (stabilization) | P0: Consolidate current CLI/manifest/status definitions; integrity repair, exclusion/truncation receipts and accessibility of failure/warning records | Actual repository CI + current-main read-back; synthetic changed/deleted/stale/cache-corruption cases; no unauthorized source mutation or new canonical duplicate | Any privacy exposure, false CURRENT state or vanished negative evidence → hold and restore last good commit |
| **v0.2 target** (measured retrieval) | P1: Pre-register Korean/English research queries with blind relevance labels, rare counterexamples, archived/current/withdrawn versions, no-overlap concepts and independent negative controls; compare basic exact/FTS with PIA retrieval | Publish *scope-limited* Recall@k, critical counterexample retrieval, false association rate, p95 query time and human review cost on held-out and seeded cases; no regression vs simple baseline in preregistered critical slices | Improvement limited to trained fixtures, unbounded false hits, or costly forced review → no promotion; narrow/revert |
| **v0.3 target** (evidence dependencies) | P2: Typed assertion–source–counterevidence–experiment–translation–contributor relations with source spans and time validity; incremental invalidation with alternate independent justifications retained | Changed/retracted source identifies affected claims and conditional status on unseen/held-out dependency tests; zero silent loss of seeded negative-result and bilingual-negation fixtures | A mention or semantic similarity promoted to verified support/contradiction without checked source → rollback |
| **v0.4 target** (durable incremental recovery) | P3: Per-authorized-repository durable checkpoint/index, replay after missed events and deletion/rename, cold-start freshness checks, fail-closed cache repair | Two fresh runs with injected interrupted updates/events restore current verified HEAD and warning ledger; measure lag, recovery time and total recomputation cost | Stale checkpoint declared current, repair conceals previous warning, or uncontrolled background spend → disable replay and retain manual Git route |
| **v0.5 target** (permissioned federation) | P4: Read-only federated *pointers* across explicitly authorized PI repositories; owner-specific HEAD/ACL, opt-in domain routing and no automatic transfer of private source text to public index | Cross-repo test fixtures prove least privilege, no private-to-public leak, no unauthorized source edits, and correct owner/time resolution; outside domains remain excluded by default | Any cross-boundary leak or attribution collision → shut off federation, retain isolated per-repo retrieval |
| **v1.0 target** (audited usefulness) | P5: Longitudinal error/omission/rollback monitoring, independent critical evaluation where available, lower human reconstruction burden and economic sustainablity | Against preregistered baselines, show meaningful net user time/cost reduction without sacrificing counterevidence retrieval, provenance, exit/recovery or access safety; candid independent-validation status | No measured net benefit or evaluation monopoly → keep bounded lower version, remove burdensome guard/platform |

**Sequence and gates, not dates.** P0/P1 take precedence over importing an embedding service or GraphRAG. No paid service or local computer setup is presumed. Where test data, reviewers or permissions are missing, return NOT TESTED/HOLD rather than escalating the version. A minimal working path can remain valid indefinitely; no forced march to v1.0.

**Mapping to the unchanged six PI stages:** Stage 1 use PIA to identify hypothesis assumptions and version; Stage 2 discover attributed prior work and disconfirmations; Stage 3 report *bounded* search saturation and unknown corpus; Stage 4 trace source/condition change and impacted rival explanations; Stage 5 retain contributor/translation history and distinguish past contribution from future employment; Stage 6 register, test, reproduce, rollback and evaluate real effects. **An effective software index does not prove any ICM hypothesis.**

**Evaluation protocol:** Freeze the target source HEAD; construct expert-reviewed relevance labels *without only pooling PIA's own results* (avoid circular evaluation); reserve hidden questions and negative cases; compare baseline and upgrade under the same permissions/hardware/clock; report denominators, missing/unsupported input, absolute error counts, source-span verification, CI execution evidence, and who pays the verification burden. Predefine minimum acceptable critical-regression behavior before observing results. A search result count, benchmark pass or CI green badge alone is not a promotion gate.

**External evaluation precedent:** [NIST TREC Total Recall 2015](https://trec.nist.gov/data/total-recall/2015/Total%20Recall%20Guidelines%202015.html) jointly considers finding relevant items and assessor workload; [NIST AI RMF Measure](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) emphasizes benchmarked, uncertainty-aware evaluation and regular checks. These justify selecting measurement dimensions, **not** a claim that PIA already achieved their benchmarks.

**Public/private boundary and attribution:** Public roadmap records architecture, safeguards and high-level evaluation. Implementation source, private research, credentials, funding and unpublished negative data remain in each owning repository. Researchers responsible for prior art retain credit. The PI human originator contributed the research-management objective and PIA naming/integration direction. Automated assistant changes and errors are separately traceable. PIA does not negotiate, authorize or satisfy retrospective compensation; do not condition past credit/redress on future testing.

### 원본2 — 한국어

**정체성.** **PIA(피아) = PI-ANCHOR**이며 Project Intersection의 정본·탐색·변경이력·관측·회수 관리 시스템이다. Project Intersection의 최종 연구 목적, ICM 개념, IVS-0R 실행·입장반전·감사 원칙과 구분한다. **현재 PIA 버전은 v0.1이며, PI 연구 로드맵 v0.2와 별도 버전 계열이다.** 이미 존재하는 기능은 Git 원문·해시 기반 증분색인, 일부 한국어/영어 탐색, 링크/ID 후보 관계, 위험 표식과 CI 시험이다. 완전한 의미검색, 자동 교차저장소 통제, 영속 에이전트 또는 과학적 독립 검증을 달성했다는 뜻은 아니다.

**진단한 최우선 병목.** 과거에는 전체 자료 재독이나 사람의 색인 탐색 부담이 컸다. 검색 엔진이 생긴 뒤 남은 병목은 **중요한 문헌·반례를 놓치는 빈도와, 사실이 아닌 관계를 연결하는 빈도를 실제 독립자료에서 측정하지 못했다**는 점이다. 따라서 먼저 측정하고, 실제 효익이 확인될 때만 복잡성을 늘린다.

| PIA 차기 **목표 버전** (현재 아님) | 우선순위·업그레이드 | 승격 게이트 | 실패 시 처리 |
|---|---|---|---|
| **v0.1 → v0.1.x** (안정화) | P0: 기존 CLI·manifest·상태 정의 통일, 원문·색인 무결성 복구, 제외 자료·절단·HOLD 경고 영수증 | 실제 저장소 CI와 main 재조회, 변경·삭제·구식/변조 색인의 합성 실패 시험, 비공개·정본 변경 없음 | 허위 CURRENT, 반례 소실, 비공개 누출이면 HOLD·마지막 정상 커밋 복귀 |
| **v0.2 목표** (검색 실측) | P1: 한국어·영어 블라인드 질의·골드 문헌, 희귀 반례, 구식/철회/현재 자료, 단어 불일치, 부정 대조군을 사전등록하고 기본 검색과 비교 | 숨은 평가집합의 Recall@k, 핵심 반례 회수율, 허위 관계율, p95 검색시간, 인간 검토비용 및 단순 기준선 대비 성과 보고; 중요 범위 역행 금지 | 학습한 예제에서만 성능 개선, 오탐·무료 검수비 급증이면 미승격·범위 축소 |
| **v0.3 목표** (근거 의존성) | P2: 주장–원출처–반례–실험–영한 대응–기여자, 증거 유형·시점·대체 독립근거의 관계를 구체화하고 변경분 자동 영향 후보 갱신 | 철회된 자료의 영향 주장 탐지, 독립 근거 존재 시 무조건 삭제하지 않음, 숨은 연결·한영 부정문/부정결과 시험에서 조용한 소실 0 | ID 공동언급·유사성을 검증된 지지/반박으로 승격하면 롤백 |
| **v0.4 목표** (연속·복구) | P3: 허가된 저장소별 영속 체크포인트와 인덱스, 누락 이벤트 재생, 삭제·이동 복구, 새 실행 cold-start 검증 | 서로 다른 두 실행에서 중단·이벤트 유실을 주입해 최신 HEAD·경고 영수증 복원, 갱신 지연·복구시간·재연산비용 측정 | 구식 인덱스 최신 오인, 경고 은폐, 통제되지 않은 예약비용이면 복구 자동화 비활성 |
| **v0.5 목표** (권한분리 연합) | P4: 승인된 PI 저장소 간 내용 자동 통합이 아닌 **읽기 전용 출처 포인터**로 연합 검색, 소유권·HEAD·ACL·분야경계 고정 | 시험 범위 내 공개/비공개 유출 0, 무단수정 0, 소유권·시점 충돌 구분. 자금·투자 등 다른 영역은 기본 제외 | 유출·출처오인 발생 시 연합 기능 차단·저장소별 독립 검색 유지 |
| **v1.0 목표** (실효성 감사) | P5: 장기 누락·복구·오류 지표, 가능할 때 외부 독립 평가, 실제 사람의 자료재설명·교정·비용 감소 | 사전등록한 기준선 대비 실제 사용자 순시간·순비용 감소, 핵심 반례·출처·이탈/복구권 감소 없음, 독립검증 유무 명시 | 편익 미측정·검증권 독점·노동전가라면 v1.0 보류, 가벼운 이전 구조 유지 |

**버전은 날짜가 아니라 게이트로 승격한다.** P0→P1을 신규 대형 AI·임베딩·GraphRAG보다 우선한다. 유료 프로그램이나 사용자 로컬 PC 설치는 전제하지 않는다. 실제 시험·권한·독립 평가가 없으면 NOT TESTED/HOLD로 표시하고 문서량만으로 버전을 올리지 않는다. 필요한 경우 v0.1의 안정된 단순 방식을 유지한다.

**기존 연구 6단계 그대로 적용:** 1단계 가설·전제·버전 확인 → 2단계 선행연구와 반례 검색 → 3단계 한정된 자료 포화·미관측 보고 → 4단계 근거 변경과 경쟁가설 파급검토 → 5단계 원저자·인간 원기여·교정·한영 계보 보존 → 6단계 사전등록·시험·실패·재현·롤백·실제 비용 검증. **PIA 검색 성능 향상은 ICM 가설 입증과 별개**다.

**평가 설계:** 평가할 Git HEAD와 권한을 고정한다. PIA 자신이 찾아준 자료만으로 정답집을 만들면 순환 평가이므로 외부 검토·독립 탐색·숨은 반례를 포함한다. 검색 방식마다 같은 권한·환경·시간 범위에서 기준선과 비교한다. 분모·표본·놓친 자료·지원하지 않는 입력·원문 인용 위치·실제 실행 로그·사람의 비용을 나눠 보고하고, 성공 기준은 결과를 보기 전에 정한다. 검색결과 수나 CI 성공만으로 실증 성공을 선언하지 않는다.

**평가 선행근거:** [NIST TREC Total Recall 2015](https://trec.nist.gov/data/total-recall/2015/Total%20Recall%20Guidelines%202015.html)는 관련 문서 회수량과 검토 비용의 균형을 평가하고, [NIST AI RMF Measure](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)는 기준선 비교·불확실성·주기적 검사를 강조한다. 이는 평가 설계의 선행근거일 뿐 **PIA가 해당 기준을 달성했다는 뜻이 아니다**.

**공개·비공개·기여 경계:** 공개 로드맵에는 설계·방호·평가 개요만 둔다. 비공개 실험 원문·미발표 실패·자격증명·재무자료는 소유 저장소에 남긴다. 선행기술 원저자의 기여와 PI 연구자 자신의 문제제기·PIA 명명/통합 기여를 따로 보존한다. 과거 기여 정산과 미래 고용·시험·PIA 업데이트는 독립이며, PIA 기능이나 자동화가 과거 정산을 대신하지 않는다.

**Change record / 변경:** 2026-10-13 PIA v0.1 **업그레이드 목표**를 기존 PI v0.2의 운영 보조 축으로 편입. PI 여섯 단계, v0.2 역사사례 F01–F20, G1–G8, R01–R12, v0.2.1/v0.2.2 연구 보충 및 원문·기여 이력은 그대로 유지. **No PIA version promotion has occurred / PIA 버전은 여전히 v0.1.**

---

## PIA Prior-art update — evidence-quality and cache-integrity gates (2026-10-13)
## 피아 추가 선행연구 — 검색평가 편향·캐시 무결성 승격 조건

**PIA remains v0.1; the existing PI six-stage research roadmap and P0–P5 targets remain unchanged.** This is not an effectiveness claim.

### Original 1 — English

**Newly prioritized methodological finding:** A gold relevance set built only from one retrieval system's returned documents can systematically miss relevant items that system never found. Büttcher et al. (SIGIR 2007, [NIST](https://www.nist.gov/publications/reliable-information-retrieval-evaluation-incomplete-and-biased-judgements)) directly analyze incomplete and biased IR judgments; the [TREC 2016 Total Recall](https://pages.nist.gov/trec-browser/trec25/recall/proceedings/) track demonstrates independent probabilistic assessment with recall-versus-review effort. **Update to PIA v0.2 gate:** independent or probability-sampled relevance judgments and rare counterexamples are mandatory before claims about corpus recall; without reviewers, declare the missing independent evidence rather than fabricating it.

**Newly prioritized integrity finding:** SQLite's native [FTS5 integrity-check](https://www.sqlite.org/fts5.html#the_integrity_check_command) can diagnose internal search-index inconsistencies; checking only matching document counts does not prove matching text. **Update to PIA P0 gate:** separately audit the cached passages against FTS content at bounded maintenance/checkpoints, without re-reading all original research for every query. The existing private PIA code added an opt-in scoped audit with successful synthetic and repository-CI tests; this does not prove that all text or meanings were indexed.

**Newly prioritized privacy finding:** [OWASP LLM08:2025](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/) documents source leakage and poisoned retrieval risk; [Zanzibar (USENIX 2019)](https://www.usenix.org/conference/atc19/presentation/pang) is a precedent for authorization decisions respecting object and change context. **Update to PIA P4 gate:** no cross-repo federation until authorization-scoped queries, indexing and exports pass leakage/owner-change tests. A private vector or embedding is not automatically anonymous or permitted in public.

**No novelty/authority inflation:** Existing [incremental view maintenance (Gupta et al. 1993)](https://doi.org/10.1145/170036.170066), [Doyle's TMS (1979)](https://doi.org/10.1016/0004-3702(79)90008-0), W3C PROV-O and RO-Crate remain independent credited prior work; this public note only records their application boundaries. No new PIA release, independent general-recall result, or authority to move private data is claimed.

### 원본2 — 한국어

**PIA는 현재 v0.1이다.** PI 기존 연구 6단계·PIA P0~P5 목표를 변경하지 않는다.

**P1 검색평가 보완:** PIA가 찾아낸 문서로만 정답집을 만들면 PIA가 놓친 중요한 자료는 애초에 평가되지 않는다. Büttcher 외(2007) [NIST 원연구](https://www.nist.gov/publications/reliable-information-retrieval-evaluation-incomplete-and-biased-judgements)와 [TREC 2016](https://pages.nist.gov/trec-browser/trec25/recall/proceedings/)에 따라 독립 판독·확률표본·희귀 반례·실제 검토비용을 승격 조건에 포함한다. 독립 평가자가 없으면 독립검증 미실행으로 보고한다.

**P0 무결성 보완:** SQLite [FTS5 공식 integrity-check](https://www.sqlite.org/fts5.html#the_integrity_check_command)는 검색 색인의 구조적 불일치 점검 방법이다. **행 수가 같다고 본문도 같은 것은 아니다.** PIA 비공개 기존 코드에 필요 시 실행하는 캐시·FTS 내용 감사 기능을 구현하고 합성·CI 검사를 수행했다. 이것은 Git 원문 전체의 의미·진실·누락 0을 입증한 것이 아니다. 평소 모든 질문마다 전체 본문을 다시 읽는 절차로 확대하지 않는다.

**P4 접근제어 보완:** [OWASP LLM08:2025](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/)에 따르면 비공개 내용을 임베딩해도 누출·오염 위험이 남는다. [Zanzibar 연구(2019)](https://www.usenix.org/conference/atc19/presentation/pang)의 권한 분리 원칙을 참고하되 대형 인프라를 무비판적으로 설치하지 않는다. 미래 교차저장소 검색은 출처별 권한·소유·시점·공개 범위를 검사한 뒤에만 허용한다.

**원기여/상태:** 증분 뷰 유지, TMS, W3C PROV-O, RO-Crate는 이미 조사된 독립 선행기술로 원저자에게 귀속한다. 이번 보충은 PIA 구현 우선순위와 잘못된 승격 방지를 위한 응용이며 새로운 원천기술의 발명 또는 실증 성공 선언이 아니다. **PIA v0.1 유지.**

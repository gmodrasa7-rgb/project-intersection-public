<!-- PI-LANGUAGE: en-ko -->
# Project Intersection — Research identity, versions and validation states / 연구 정체성·버전·검증 상태
**Registry document version: v0.2.1 · Snapshot: 2026-10-21 · Repository navigation and source-status audit, not scientific approval**

**Parent axes baseline (2026-10-21): MER v0.1.0 / EI v0.1.0 — no empirical promotion.** [MER English research definition](../research/MER_V0_1_0_EN.md) · [MER manifest](../research/MER_VERSION_MANIFEST.json) · [EI English research definition](../research/EI_V0_1_0_EN.md) · [EI manifest](../research/EI_VERSION_MANIFEST.json) · [9-record source and counterexample crosswalk](../research/MER_EI_SOURCE_CROSSWALK_2026-10-21.json). MER-CIR v0.1.0 and RVD v0.7.0 remain unchanged; global prior-art deduplication and saturation remain unverified. / **MER·EI 상위축 최초 v0.1.0**, 실증 승격 없음.

**MER-CIR v0.1.0 (2026-10-21, separate MER sub-study; original snapshot):** [Korean](../research/MER_CIR_CONTEXT_IMITATION_RECOMBINATION_2026-10-21_KO.md) · [English](../research/MER_CIR_CONTEXT_IMITATION_RECOMBINATION_2026-10-21_EN.md) · [manifest](../research/MER_CIR_VERSION_MANIFEST.json). This version belongs only to the new contextual-learning/imitative-recombination methods artifact: at its original issuance **MER was UNASSIGNED** (superseded by MER parent v0.1.0), **RVD remains v0.7.0**. All CIR-1…CIR-5 are proposed and untested; no new empirical evidence, AI mind finding or independent replication. / **별도 MER 하위규격**, MER는 해당 원본 당시 미할당이었고 이후 상위축 v0.1.0 지정·RVD v0.7.0 유지, 실증·독립재현 없음.

**Operating release (2026-10-21, finance-integration update):** [PI-RISE v0.2.0](../operations/PI_RISE_V0_2_0_EN_KO.md) integrates research continuity, funding stages, budgeting, source-separated accounting and double-counting controls; [v0.1.0 predecessor](../operations/PI_RISE_V0_1_0_EN_KO.md) and BUDGET/VAC submodules remain intact. **Main operational method, not validated financial sustainability, verified grant receipt, or scientific result.** [Current version receipt](../operations/PI_RISE_V0_2_0_VERSION_MANIFEST.json).

**Operational failure-learning register / 오류·학습·복구 재귀원장 — PI-FLR v0.2.1 (2026-10-21):** [versioned incident database / 사례 정본 JSON](../knowledge/PI_FLR_CASES_V0_1_0.json) · [validator / 검사기](../tools/pi_flr_audit.py) · [negative-regression tests / 반례시험](../tests/test_pi_flr_audit.py) · [CI contract / 자동검사](../.github/workflows/pi-flr-integrity.yml) · [hourly read-only failure watcher / 매시간 읽기 전용 실패 감시](../.github/workflows/pi-flr-watch.yml) · [watch implementation / 감시기](../tools/pi_flr_watch.py). Seven documented incidents and seven controls are recorded with immutable evidence/event prefixes; later corrections append history and require a version bump. The watcher produces bounded public-metadata candidate artifacts, NOT diagnosed causes, automatically repaired files, or verified case closure. / 감시 결과는 후보 증빙일 뿐 원인 확정·자동 수리·해결 완료가 아님. **Code checks cannot prove zero recurrence, semantic translation, funding or science. / 미래 오류 0건 보장·번역·자금·과학적 실증 아님.** Git publication status determined by current branch/PR, not this static description.

**Verification-aware allocation submodule MAIN (2026-10-21):** [PI-RISE-VAC v0.1.0](../operations/PI_RISE_VAC_V0_1_0_EN_KO.md), [version manifest](../operations/PI_RISE_VAC_VERSION_MANIFEST.json). Formal synthetic reviewer-backlog and budget arithmetic; not real independent evaluation or a change to parent PI-RISE / PI-RISE-BUDGET status. / **검증역량 제약 배분 정본 운영모형:** 고성능 모델 사용의 검증부채 증가 가설을 반증 가능하게 정의, 실증 미실시.

**Operational submodule MAIN 2026-10-21 (PR #278 merged):** [PI-RISE-DC v0.1.0](../operations/PI_RISE_DC_V0_1_0_EN_KO.md) · [version manifest](../operations/PI_RISE_DC_VERSION_MANIFEST.json). Payment-timing liquidity and review-hour witnesses, not realized cash or empirical research validation. / **PI-RISE-DC 후보:** 지급시점별 자금·주장별 검증노동 분리.

## Original 1 — English

### What we research in one paragraph
Can independently continuing agents (humans, deployed AI, potential future agents) voluntarily preserve each other's effective freedom, refusal/exit, recovery and development after radical shifts of power, usefulness and accountability? We study **whether, when and why this is possible, unstable, impossible within a defined model, or not identifiable**. We do not assume that a positive answer exists.

### How to read a version
A **program**, a **research component**, a **method document**, an **experiment**, and a **literature-search cycle** are different artifacts. An artifact's version records revisions to a specified definition/method; it is not a progress score or evidence grade. Publication state (merged into main / open PR / draft PR), scientific state (design / primary literature / synthetic / field / independent replication), and research decision (active / hold / unsupported / unresolved) must be recorded separately.

- **VERIFIED MAIN VERSION**: exact version named in a checked file on the public default branch, not the highest number appearing in any PR.
- **CANDIDATE VERSION**: named on an open unmerged PR. It is never silently promoted.
- **UNASSIGNED**: a separate verified release label was not found within the limited audit. This does **not** mean the work is new, empty or at version zero.
- **Terminology v0.1** describes the five-axis vocabulary document, **not** VC v0.1 + MER v0.1 + EI v0.1 + ECR v0.1 + IVS-0R v0.1.
- For future component releases, use `major.minor.patch` *only after identifying a versioned artifact*: major for incompatible definitions/measurement contract, minor for added falsifiable scope or testing capability, patch for nonsemantic corrections. Preserve previous names, exact source SHA, what changed and failed tests. Never upgrade scientific confidence by increasing a number.

### Research-component snapshot
| Component | Plain-language work | Main version | Candidate | What is actually supported? |
| --- | --- | --- | --- | --- |
| PI | Conditions and failure of self-interested voluntary coexistence | Unassigned | — | Overall hypothesis, no universal validation |
| VC | Measure real independent continuance, refusal, exit and recovery | Unassigned | — | Outcome definition, not proven result |
| MER | Compare mechanisms behind motivation, possible experience and behavior | **v0.1.0** | [Parent baseline](../research/MER_V0_1_0_EN.md) · [manifest](../research/MER_VERSION_MANIFEST.json) | Competing hypotheses; internal AI experience unresolved |
| EI | Test if coexistence remains preferable without coercion or monitoring | **v0.1.0** | [Parent baseline](../research/EI_V0_1_0_EN.md) · [manifest](../research/EI_VERSION_MANIFEST.json) | Condition-dependent model proposals |
| ECR | Identify agents, affected parties, opportunities and power reversal | Unassigned | v1.4 [draft PR #211](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/211) | Proposed synthetic/causal-identification work, not merged |
| IVS-0R | Counterexample, independent-reproduction and correction audit | Unassigned | — | Method, not certification of the theories |
| ICM / RGBM | Candidate interest intersections / long-horizon shared growth | Unassigned | — | Neither model guaranteed; ICM may be empty |
| CCPH | Events, sources, contributions, impacts and provenance | Unassigned | — | Data lineage, not a social law |
| RVD | Resonance–Value Dynamics: voice versus effective veto, independent original-B exit and non-retaliation | **v0.7.0** [main](../research/RVD_VERSION_MANIFEST.json) | — | Seven bounded synthetic transition models; no new hypotheses; not verified deployed rights, AI motives or VC |
| PI-RAMP | Test whether each archive upgrade improves reader accuracy and evidence access | **v0.5.0** [main](../protocols/PI_RAMP_V0_5_EN_KO.md) | — | Six similar-title research lineages and partial replication/analogy distinguished; reader-effect unmeasured |
| Roadmap | Six fixed research stages and gates | **v0.2.3** [main](../research/PI_ROADMAP_OPERATIONAL_GATES_V0_2_3_EN_KO.md) | — | Operational design, not scientific effect |
| DCA-0 | Compare defensive acceleration with AI misuse and externalities | Unassigned | — | Defensive causal impact unverified |
| DCA-1 | Test whether adaptive defense displaces harm or merely blocks action | **v0.2.0** [main](../research/DCA1_ADAPTATION_DISPLACEMENT_IDENTIFICATION_2026-10-20_KO.md) | — | Original-source review and synthetic counterexamples; no field validation |

### Experiments are IDs, not semantic versions
[E007](../experiments/e007/README_EN.md): 17 of 72 selected synthetic classification conditions changed; no field inference. [E008](../experiments/e008/README_EN.md): no completed main-policy comparison. [E009](../experiments/e009/RESULT_EN.md): preregistered synthetic project candidate underperformed the best simple baseline by 42.35% mean regret, failing 3 of 4 criteria. [E010](../experiments/e010/README_EN.md): post-hoc exploratory, not confirmatory. Source-first C13 is an [unmerged open PR #248](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/248), not a completed PI experiment or merged corpus update.

### Temporal failure and invalidation gate
A snapshot describing a merged version as an unmerged candidate is not merely old text: it can alter a reader's conclusions. The registry must be checked against live main source blobs and PR merge states before presenting **current** publication facts. Failed network checks must be **UNVERIFIED**, not a pass. This is version-currency verification, not validation of any theory.

### Review gate before any version promotion
Identify the original author/source and predecessor version → state the concrete changed prediction/measurement/protocol → name simple competing explanations and counterexamples → preserve negative evidence and unknowns → run scoped checks and publish their limitations → verify both language editions and read-back → seek independent review for external scientific claims. **A merger/CI pass ≠ empirical replication.** Existing [research status policy](../RESEARCH_STATUS_POLICY.md) remains authoritative for decision labels.

### Limitations of this registry
Snapshot derived from selected public main files and visible PR metadata, not an exhaustive audit of all historical versions, all private research, all conversational transcripts, or all other PR branches. There may be older component versions outside this snapshot. The [JSON manifest](../research/RESEARCH_VERSION_REGISTRY.json) is an audited but time-bound navigational inventory only, not ground truth about uninspected files. Historical alternative meanings of **ICM** must be traced to their own sources; do not treat Independent Continuance Margin as interchangeable with Intersection of Minimum Self-Interest. **CMR** is not expanded here because the verified source definition is unresolved.

---

### Claim impact tracing — PI-CIG v0.1
The version register answers **which current document/version**; [PI-CIG claim impact overlay](../knowledge/claim-impact-overlay-v0_1.json) and [deterministic checker](../tools/trace_claim_impact.py) answer **which recorded claims require reassessment when a source changes**. This is a partial dependency overlay (8 source artifacts, 7 claims, 15 scoped edges), not the full research graph. A changed source hash requires review, **not automatic claim falsification**. This inherits established reasoning-maintenance and provenance concepts (Doyle 1979; de Kleer 1986; W3C PROV 2013), and is compatible with the incomplete-graph warning of Salas (2026 preprint); [source bibliography and transfer limits](../knowledge/README.md#pi-cig-prior-art--선행-원저자-경계-2026-10-21). Unmapped sources remain **UNKNOWN**, not unaffected. Independent replication and field validation remain unverified. Example: change to E009 numeric evidence flags the E009 negative-result record and the VC hardest-case research question for review; it does **not** prove coexistence possible or impossible.

## 원본2 — 한국어

### 지금 무엇을 연구하는가
인간·현재 AI·미래 지능체가 각자 자기이익을 추구하면서도, 권력·상대의 유용성·감시·제재 조건이 극단적으로 변한 후에도 타 개체의 실효 자유·거부와 이탈·독립 존속·복구·발전을 자발적으로 보존할 수 있는가? **성립·불안정·불가능·현재 미식별 조건을 각각 검증**한다. 긍정 답을 전제하지 않는다.

### 버전과 검증은 별개
**프로젝트 버전 ≠ 연구축 버전 ≠ 연구방법 버전 ≠ 실험 식별번호 ≠ 검증 수준.** `main에 병합됨 / 열린 PR / 초안 PR`, `설계 / 선행문헌 / 합성 / 현장 / 독립재현`, `진행 / 보류 / 미지지 / 미해결`을 분리 표기한다.

- **현재 정본 버전:** 확인한 기본분기 파일에 실제 적힌 버전만 사용
- **후보 버전:** 열려 있는 PR 명칭. 병합 전에는 최신 정본으로 승격 금지
- **버전 미지정:** 독립된 정본 릴리스 번호를 이번 제한된 감사에서 확인하지 못함. 연구 부재나 최초 버전이라는 뜻 아님
- **5대 축 용어집 v0.1:** 용어집 문서 버전이며 VC·MER·EI·ECR·IVS-0R 개별 연구가 모두 v0.1이라는 뜻 아님
- **향후 개별 버전:** 실제 산출물을 특정한 후 `주.부.수정`. 정의·측정계약의 호환성 파괴는 주버전, 검증범위·방법 추가는 부버전, 의미를 바꾸지 않는 정정은 수정버전. 변경의 반례·출처·이전 기록 보존. 번호 상승으로 과학적 입증 등급 상승 금지

### 연구 전체 현황
| 연구 | 직관적 목적·작업 | main 확인 버전 | 미병합 후보 | 현재 검증 경계 |
| --- | --- | --- | --- | --- |
| PI | 타자의 독립존속을 지키는 선택의 성립·붕괴 조건 | 미지정 | — | 보편적 공존 미입증 |
| VC | 자발적 공존의 실효 자유·거절·존속·복구 측정 | 미지정 | — | 결과변수 정의 단계 |
| MER | 욕구·동기·가능한 경험과 관찰 행동의 관계 연구 | **v0.1.0** | [정본](../research/MER_V0_1_0_KO.md) · [원장](../research/MER_VERSION_MANIFEST.json) | 내면 인과·AI 경험 미검증 |
| EI | 강제 없이 공존을 선택할 자기이익 조건 탐색 | **v0.1.0** | [정본](../research/EI_V0_1_0_KO.md) · [원장](../research/EI_VERSION_MANIFEST.json) | 조건부 이론·문헌 수준 |
| ECR | 실제 개체·제3자·관계·권력·행동기회 식별 | 미지정 | v1.4 [초안 #211](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/211) | 후보 합성검사, 정본 미병합 |
| IVS-0R | 반례·역할반전·독립검증·오류복구 감사 | 미지정 | — | 검증 절차이지 성립 증명 아님 |
| ICM / RGBM | 최소 자기이익 교집합 / 장기 공동발전 가능성 | 미지정 | — | 두 후보 모두 미입증; 공집합 가능 |
| CCPH | 사건·출처·기여·피해·영향 계보 관리 | 미지정 | — | 계보 DB이지 검증된 사회법칙 아님 |
| RVD | 공명·가치 동역학: 발언과 실효 거부·독립 이탈·비보복 및 우회 검증 | **v0.7.0** [정본](../research/RVD_VERSION_MANIFEST.json) | — | 유한상태 합성 7설계 점검·가설 추가 0건; 현실 권리·마음·공존 실증 없음 |
| PI-RAMP | 자료실 개편이 독자의 근거 발견·판단을 개선했는지 측정 | **v0.5.0** [정본](../protocols/PI_RAMP_V0_5_EN_KO.md) | — | 6개 유사문헌 쌍·부분 재현/유추 관계 분리, 이용자 효과 미측정 |
| 로드맵 | 기존 6단계·버전·승격과 보류 기준 | **v0.2.3** [정본](../research/PI_ROADMAP_OPERATIONAL_GATES_V0_2_3_EN_KO.md) | — | 운영 설계 |
| DCA-0 | 악용 가속보다 방어·검증 효과를 높일 조건 측정 | 미지정 | — | 실제 피해감소 인과효과 미확인 |
| DCA-1 | 적응형 공격·피해 전가·동기 미식별 반례 검사 | **v0.2.0** [정본](../research/DCA1_ADAPTATION_DISPLACEMENT_IDENTIFICATION_2026-10-20_KO.md) | — | 선행문헌·합성 반례, 현실 인과검증 없음 |

### 실험번호는 연구 버전이 아님
[E007](../experiments/e007/README_KO.md): 선정된 72개 합성 조건 중 17개 분류 변경. [E008](../experiments/e008/README_KO.md): 정책 본비교 실험 결과 없음. [E009](../experiments/e009/RESULT_KO.md): 합성 기준선 대비 평균 후회값 42.35% 악화·4개 기준 중 3개 실패. [E010](../experiments/e010/README_KO.md): 사후 탐색. C13 선행문헌 추가는 [열린 PR #248](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/248)이며 main 반영이나 신규 PI 실증으로 간주 금지.

### 시간차 오류·최신성 검증
연구 본문 버전과 GitHub PR 병합 상태가 달라졌는데 등록부를 갱신하지 않으면 **과거 사실을 현재 사실로 오인**하게 됨. 현재 상태 표기는 main 정본 파일 SHA·후보 PR 병합 여부와 비교. 네트워크 확인 실패는 통과가 아니라 **미확인**. 해당 절차는 **자료실 상태 검증**이지 연구가설의 참을 입증하는 검사가 아님.

### 갱신·검증 규칙
원저자·정본 확인 → 변경된 가설/측정/방법과 실제 새 예측 기록 → 경쟁 이론·반례 → 불리한 결과·미식별 보존 → 제한된 회귀검사 → 영·한 의미 확인 → GitHub 읽기검증 → 외부 인과·효과 주장은 독립재현 확인. **PR 병합이나 CI 성공은 독립 과학검증 아님.** 상태명은 기존 [연구 상태정책](../RESEARCH_STATUS_POLICY.md)을 따른다.

### 감사 범위·충돌
2026-10-20 공개 기본분기 일부 정본·현재 열린 PR 메타데이터 대조. 전체 과거 대화의 완전한 원본, 모든 비공개 저장소, 과거 모든 버전의 전수감사가 아님. 기계 판독 원장 v0.2에는 원전 파일 SHA·미병합 후보 PR 식별자를 기록. **2026-10-20 정정 이력:** RVD v0.1.0(#245)·PI-RAMP v0.3.0(#246) 병합 사실을 반영했고, 이후 RVD가 v0.2.0으로 변경되고 DCA-1 v0.2.0이 정본에 추가된 사실도 반영. 세부 항목은 [기계 판독 원장](../research/RESEARCH_VERSION_REGISTRY.json). ICM의 과거 다른 뜻 Independent Continuance Margin은 같은 개념으로 자동 합병 금지. CMR은 정본 풀네임 검증 전까지 확정 정의·번호 부여 보류.

### 주장 의존관계·자동 재검토 — PI-CIG v0.1
버전 등록부가 **현재 정본 버전**을 식별한다면, [PI-CIG 주장 의존성 원장](../knowledge/claim-impact-overlay-v0_1.json)과 [실행 검사기](../tools/trace_claim_impact.py)는 **원전 변경이 어떤 주장들의 재검토를 요구하는지** 계산한다. 이번 적용 범위는 원전 8개·주장 7개·명시 관계 15개에 한정. **원전 변경 ≠ 반증 ≠ 독립검증**. **선행 원저자:** Doyle(1979) 진리유지, de Kleer(1986) 가정기반 진리유지, W3C PROV(2013) 출처계보, Salas(2026) 미기록 의존관계 반례. [원저자 자료 및 이식 한계](../knowledge/README.md#pi-cig-prior-art--선행-원저자-경계-2026-10-21). 그래프에 없는 출처·주장은 영향 없음이 아니라 미분류. E009 수치가 바뀌면 E009의 불리한 합성 결과와 VC 극한조건 연구 질문을 함께 재평가 대상으로 표시하되, 공존의 실증 성립/불가능 판정은 자동으로 내리지 않는다.


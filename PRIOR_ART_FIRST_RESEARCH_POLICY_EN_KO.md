# Prior-Art First: Standing Research Priority / 선행·관련 논문 조사·수집·기록·저장 최우선 운영규칙

**Effective 2026-10-20 | Status: STANDING RESEARCH WORK-ORDER POLICY.**
**적용: 모든 Project Intersection 후속 연구 회차 · 인간/AI 실행자 · 공개/접근 가능한 비공개 또는 로컬 연구 공간.**

> **Research work priority #1: SEARCH → COLLECT → VERIFY → DEDUPLICATE → CRITICALLY RECORD → PERSIST relevant original and related scholarly papers. Repeat until defensible *topic-specific* literature saturation; reopen when new contrary evidence or search paths appear.**
>
> **연구작업 최우선순위 1: 관련·선행 원저자 논문을 조사 → 수집 → 원출처 검증 → 중복 제거 → 비판적 기록 → 영구 보존을 목표로 한 버전관리 저장. 주제별 문헌 포화의 증거가 확보될 때까지 반복.**

This is the priority **among research activities**, not a replacement for the founding goal, scientific integrity, human rights/privacy, source copyright, or emergency data-integrity repairs. / 연구 진행 순위의 고정이지 창시 목적·증거 정직성·저작권·개인정보 보호보다 우월한 실체적 주장 아님.

## 1. Required first action every research cycle / 매 회차 첫 연구 행위
1. Read current corpus and last search receipt. Reuse existing records instead of restarting or duplicating.
2. Specify the next unresolved *question* and search for original/seminal studies, empirical tests, replications, disconfirmations, null results, relevant formal models, measurement methods and adjacent-field antecedents.
3. Search trustworthy primary publishers and scholarly databases; trace reference lists **backward** and citing works **forward**; run independent synonym/antonym, role-reversal and counterexample queries. Record each actual source searched, query, date, coverage and access restriction.
4. For each candidate, capture **original author(s), year, complete title, DOI/verified stable ID, canonical URL, study design, original claim, competing explanation, boundary condition, and relevance to a specific project question**. Validate with the publisher/original source and, where possible, an independent index. Record abstract-only reading as such.
5. Deduplicate by DOI/verified ID and intellectual lineage; distinguish original source, review, reprint, same-dataset analysis and independent replication. Track contradictory findings, methodological weaknesses and withdrawal/retraction.
6. **Persist every defensible incremental discovery or negative search receipt before proceeding:** write to the relevant existing register, maintain revision/attribution and exclusions, Git-commit or durably save to an accessible local/Library file, then **read back** to verify. If not synced to GitHub, mark NOT_SYNCED; never claim remote storage without a successful commit.
7. Only after the documented search-and-save checkpoint choose experiments, simulation, concept expansion, tool building, summary or presentation. A new research theory/experiment cannot bypass this step because a paper count or time budget feels sufficient.

Exception: urgent prevention of evidence loss, archive corruption, rights/privacy violations, or explicit nonresearch tasks may precede the literature checkpoint; these do not rescind the standing priority. The session can be bounded; a blocked search must log actual limitations, never fabricate coverage.

## 2. Topic coverage / 연구범위
Track independent search fronts for **VC, EI, MER, ECR, ICM, RGBM, IVS-0R, CCPH**, entity identification/measurement, the project's 34 role groups, historical cases and cross-disciplinary gaps. Related sciences include game theory, evolutionary biology/ecology, economics, psychology, neuroscience, social science, causality/measurement, AI and philosophy where relevant. **Scope follows the question, not fixed keyword quotas.** Search opposing models as actively as supporting ones.

Prioritize author-original studies and validated original methodological precedents. A highly cited article is not by itself reliable, and a source count is not evidence of independent replication.

## 3. Minimum persistent data contract / 최소 저장 항목
For every *included* study retain:
- canonical bibliographic metadata; DOI/ID; original author/first-idea lineage when determinable; primary URL and check date;
- search query, retrieval route, full-text/abstract accessibility, copyright/reuse boundary, versions and corrections;
- question/topic and 34-role relevance (if any); claim, design, sample/data, measurement/identification, causal limits;
- mechanism, alternative hypothesis, counterexample, relevant negative findings, limitations and retraction status;
- relation to the Project (pre-existing explanation, reusable method, contradiction, new conditional gap, non-adopted finding); actual affected artifact/version when used;
- evidence state: DISCOVERED / METADATA_VERIFIED / FULLTEXT_REVIEWED / CROSSCHECKED / DISPUTED / RETRACTED / UNKNOWN;
- local/remote saved path; Git revision where committed; read-back/backup state.
Do **not** publish protected full paper texts without permission; preserve metadata, lawful links and own critical notes.

For every *search session*, including zero-hit or access-blocked sessions, retain:
`date | research question | searched databases | exact queries | date/field coverage | candidates screened | eligible | new unique sources | independent lineages | new mechanisms | new counterexamples | excluded + reasons | unresolved access | written paths | commit/local receipt | readback | next frontier`.
Unknown counts remain UNKNOWN; search receipts are **not** fake discoveries.

## 4. Saturation adjudication / 주제별 포화 판정
- Track NOT_ASSESSED / SEARCH_ACTIVE / PROVISIONALLY_SATURATED / REOPENED **per research question × mechanism × disciplinary/contrary-evidence search front**. No global blanket saturation or guaranteed exhaustive coverage.
- Require documented multi-source search coverage, backward/forward citation-chaining, relevant original authors, independent counterexample searches, and reduced **material** new information (mechanism, identification method, boundary condition, counterexample), plus explicitly recorded residual unknowns.
- A new derivative paper repeating a known mechanism **does not** reset conceptual saturation by default. A truly new counterexample or missing causal mechanism **does** reopen that topic. Keep bibliographic discovery and substantive knowledge deltas separate.
- Neither a fixed paper threshold, repeated `SATURATION_NOT_REACHED`, nor `no_delta_streak=0` is a scientifically sufficient decision rule. A provisional conclusion must be reasoned and reversible.
- Later work, inaccessible paywalled literature or new disciplines can always reopen search. Saturation is scoped and revisable, not literal eternal completeness.

## 5. Canonical persistence / 기존 원장 재사용
Prefer existing [saturation map](PRIOR_ART_SATURATION_MAP_KO.md), [original-paper crosswalk](CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md), [source and attribution register](PRIOR_ART_AND_ATTRIBUTION.md), [original-author rights lineage](PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md), and [knowledge registries](knowledge/), instead of competing unsynchronized registers. [Autonomous research loop](AUTONOMOUS_RESEARCH_LOOP.md) must begin its research stage with this policy.

**2026-10-20 baseline receipt:** public GitHub README, research loop, saturation map, and knowledge/prior-art directories were inspected. This change **sets the binding work priority only**; it does not assert a new external paper search, added research papers, a background job or achieved saturation.

Versioned Git history improves recoverability but cannot guarantee that a rule is literally immutable; authorized future revisions must preserve a traceable reason and never silently reverse the research priority.

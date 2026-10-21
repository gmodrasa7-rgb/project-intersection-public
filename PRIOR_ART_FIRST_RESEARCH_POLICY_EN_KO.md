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

## 6. Verified methods, original sources and adoption boundaries (2026-10-21) / 선행 모범 방법·원전·적용 경계

**Scope / 범위:** Primary source audit of methodological guidance, cross-checked with the existing [PI-RAMP v0.3 original-precedent matrix](protocols/PI_RAMP_V0_3_KO.md). This is NOT new PI science, a systematic review, successful external evaluation, or literature saturation. Previously referenced Cochrane, PRISMA-S, W3C PROV, RO-Crate and Diátaxis are NOT new PI discoveries.

| Authoritative source / 검증 원전 | Actual scope / 원래 기준 | Adoptable delta / PI의 제한적 응용 |
| --- | --- | --- |
| [Cochrane Handbook Ch. 4 (2025), Lefebvre et al.](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04) | One study may have several reports/records; study is the analytic unit | **ALREADY REFERENCED IN PI-RAMP v0.3**. Link record, report and study separately; do not infer independent-study count from distinct DOIs |
| [PRISMA-S (2021), Rethlefsen et al., DOI 10.1186/s13643-020-01542-z](https://doi.org/10.1186/s13643-020-01542-z) | Sixteen search-**reporting** items | **ALREADY REFERENCED**. Archive actual database/platform, exact queries, dates, exclusions, inaccessible resources; reporting items cannot certify search quality |
| [PRISMA 2020 (2021), Page et al., BMJ 372:n71](https://www.bmj.com/content/372/bmj.n71) | 27-item systematic-review **reporting** guideline and record selection diagram | **ADDITIONAL PRECEDENT**. Track identification, screening, inclusion and justified exclusions per front. This work is NOT PRISMA-compliant systematic review |
| [FAIR Guiding Principles (2016), Wilkinson et al., DOI 10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18) | Findable, Accessible, Interoperable, Reusable principles (not a prescribed technical standard) | **ADDITIONAL PRECEDENT**. Retain canonical IDs, qualified links, rights/access metadata and provenance; no FAIR certification |
| [W3C PROV-O (2013), W3C Recommendation](https://www.w3.org/TR/prov-o/) | Provenance entities, activities and agents | **ALREADY REFERENCED as W3C PROV family**. Distinguish source, extraction, analysis, authorship, AI assistance and review; current PI JSON graph is NOT certified PROV-O conformant |
| [RO-Crate official specification index](https://www.researchobject.org/ro-crate/specification.html) | JSON-LD packaging of research objects; v1.3 released while v1.2 remains stable | **EXISTING v1.2 REFERENCE RECHECKED**. No automatic version upgrade, formal compliance or mass historical-file conversion without a validated crate |
| [The Turing Way — Research Compendia](https://book.the-turing-way.org/reproducible-research/compendia/) | Conventional structure, separated inputs/methods/outputs and recorded computational environment | **ADDITIONAL DIRECT PRECEDENT**. For selected experiments, link the already existing inputs, scripts, environment, commands and frozen outputs as a virtual package; self-rerun ≠ independent replication |
| [Diátaxis — Procida, original documentation](https://www.diataxis.fr/) | Separate reader tutorials, how-to, reference and explanation | **ALREADY REFERENCED**. Keep task-oriented navigation, not destructive four-folder refactoring |

**Implementation rules / 실무 원칙**
1. **Search receipt:** source database/platform; exact query; timestamp; coverage; access limits; actual numbers identified/screened/included/excluded and exclusion reasons. Missing historical counts are UNKNOWN, never retroactively invented.
2. **Identity:** independently track record_id, report_id, study_id and the actual basis for grouping. Ambiguous duplicates = UNRESOLVED; automatic article-to-study merge = HOLD.
3. **Provenance:** maintain original paper → studied population/design → observed result → PI interpretation → supporting/opposing artifact → changed claim; identify authors, AI operators and reviewers separately. An unregistered link is NOT evidence of no dependency.
4. **Reproduction:** for a *selected* runnable experiment, link frozen source/input, executable command, environment specification, recorded results and failure cases. GitHub CI success checks only its stated contract.
5. **Reader-effect test:** predefine independent-reader tasks to detect (a) same-study multiple reports, (b) E009 adverse synthetic result, (c) E008 no main result and (d) a non-identifiable causal claim. Record baseline and comparison accuracy, errors, time, reviewer independence, and overhead; until measured, EFFECT_UNMEASURED.

**Do not implement / 보류:** duplicate source-of-truth registries, mass relocation, blanket FAIR/PRISMA/PROV/RO-Crate compliance badges, new license assumptions, or a PI-RAMP version increment based only on citations. Preserve [original-source rights](ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md), [version status](research/RESEARCH_VERSION_REGISTRY.json), and the pre-existing [PI-RAMP v0.3](protocols/PI_RAMP_V0_3_KO.md). Methods citation ≠ endorsement of Project Intersection.

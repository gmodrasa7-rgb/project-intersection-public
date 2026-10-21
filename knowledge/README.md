# Project Intersection Knowledge Graph
## 연구 지식그래프 v1

Status: **PUBLIC NAVIGATION / STRUCTURED EVIDENCE INTERFACE**

This layer converts the public repository from a document-first archive into a structured research knowledge base without replacing the source documents, commit history, or provenance.

이 계층은 공개자료실을 문서 중심 보관소에서 구조화 연구 지식베이스로 확장한다. 원문 문서·커밋 이력·provenance를 대체하지 않는다.

## 1. Design rule

The graph stores **references and relations**, not copied source bodies.

Each record has a stable local ID and separates:

- research question;
- claim;
- mechanism / governance rule;
- prior art;
- experiment;
- evidence;
- historical or negative-control case;
- failure;
- correction.

Relations carry qualifiers such as scope, evidence class, and source path.

A relation such as `supported_by` therefore does **not** mean universal validation. Its qualifier must state the supported scope.

## 1A. Bounded claim-impact overlay (PI-CIG v0.1)

The original [graph.json](graph.json) stays the incomplete navigation graph, not a source of truth. [PI-CIG overlay](claim-impact-overlay-v0_1.json) adds a small, independently versioned **change-impact** graph, without overwriting the original schema or asserting a complete citation graph. The [checker](../tools/trace_claim_impact.py) verifies the specified Git blob SHA and critical source assertions; changed input traverses explicit edges to a set of **claims needing reassessment**, never to automatic falsification.

정본 변경 → 제한된 의존관계 전파 → **재검토 후보**, 자동 반증 또는 과학적 승인 아님. 출처가 연결되지 않은 경우 영향 없음이 아니라 **미관측**. 실행 명령: `python tools/trace_claim_impact.py --self-test`, `python tools/trace_claim_impact.py --changed experiments/e009/RESULT.json`.

### PI-CIG prior art / 선행 원저자 경계 (2026-10-21)

- [Jon Doyle (1979), *A Truth Maintenance System*](https://groups.csail.mit.edu/medg/ftp/doyle/) — belief-reason maintenance, not PI's original principle (DOI 10.1016/0004-3702(79)90008-0).
- [Johan de Kleer (1986), *An assumption-based TMS*](https://www.sciencedirect.com/science/article/pii/0004370286900809) — assumption environments (DOI 10.1016/0004-3702(86)90080-9); PI-CIG has not implemented a full ATMS.
- [W3C PROV-DM (2013)](https://www.w3.org/TR/prov-dm/) — generic attribution/revision/provenance structures; this overlay JSON does **not** claim PROV conformance.
- [Jesus Salas (2026), *Change-Provenant Supervision*](https://arxiv.org/abs/2609.28574) — a preprint with controlled source-lineage omission and independent contract-revalidation tests; external peer review unknown. Controlled learned-artifact governance does not validate voluntary-coexistence theory.

**Principled failure:** recorded edges can never prove that no essential edge is missing. The overlay therefore proposes *re-review candidates*, while [the independent source-to-report numerical validator](../tools/audit_claim_source_lock.py) applies separately to E007–E010 without trusting graph reachability. This separation is computational, not an external independent scientific review; it is not a complete audit of VC, MER or future agent preferences.

## 2. Files

**CCPH real events / 현실 연구 사건 (2026-10-15):** [CCPH observed Project Intersection event ledger](ccph-observed-project-events-v0_1.json) contains three *actual verified public GitHub research-process changes* (PRs #167–169), linked to the [event schema](ccph-impact-lineage-event-schema-v0_1.json) and [research execution loop](../AUTONOMOUS_RESEARCH_LOOP.md). These are not synthetic benchmarks; verified file changes are not verified scientific, welfare or causal improvements. / **CCPH 실제 관측 원장**은 공개 GitHub 병합 사건 3건을 최초 실증 기록으로 보존한다. 변경된 파일 수는 실제 활동량이지만 연구 발전의 순효과·사회적 편익이 아니다. 증거·기여자·후속 영향·미확인을 별도 기록하며 선택 표본의 전체 대표성을 주장하지 않는다.


- `schema-v1.json` — machine-readable field contract.
- `graph.json` — dated, incomplete public navigation subset. `meta.updated_at` is the last graph update, not the latest Git `main`. Missing entities or edges are UNKNOWN, not proof of absence.
- `explorer.html` — dependency-free browser/search interface.
- `validate.py` — integrity and provenance checks.
- `SOURCE_REGISTRY.md` / `source-registry.json` — audited external design references, originators, verified influence, and rights/licensing boundaries.
- `.github/workflows/knowledge-graph-audit.yml` — CI validation.

The canonical scientific source remains the linked artifact and Git history. `graph.json` is a navigation/index layer.

**Coverage boundary (2026-10-14 focused update):** `graph.json` was extended with **7 original focused nodes and 8 evidence-qualified edges, plus 3 additional prior-art nodes and 4 evidence-qualified edges** for the founder's Continuance–Contribution Pathways Hypothesis, 19 ordinary-contributor and 15 human survival/exclusion case records (case groups, not one independently verified graph node per case), upstream research, PICB v1 synthetic outcome limits and counterexamples. Its `meta.updated_at: 2026-10-14` dates this **focused index edit only**, not a complete re-crawl or comprehensive scientific review. Missing entries/edges remain UNKNOWN, not proven absence. / 2026-10-14 일부 갱신은 존속–기여 경로 가설·19+15 인간 사례그룹·선행연구·PICB 결과 경계·부정대조만 색인했다. 그래프 전체 전수검수·34개 실증 인과사례 확보가 아니다. 누락은 존재하지 않음이 아니라 미색인/UNKNOWN으로 유지한다.

## 3. Information-architecture references

The design was independently reimplemented from general knowledge-base patterns rather than copied from any site's source code, text, CSS, icons, layout, or datasets.

Conceptual references include Open Research Knowledge Graph, Wikidata, OpenAlex, Papers with Code, and MITRE ATT&CK. The audited original-source list, verified design influence, and rights/licensing boundary are maintained in [SOURCE_REGISTRY.md](SOURCE_REGISTRY.md) and [source-registry.json](source-registry.json).

These names identify design inspiration only. No third-party visual assets or page text are bundled here. External data, if later imported, must retain its own source and license metadata.

## 4. Copyright and provenance boundary

A public source may be **cited or linked** without copying its protected expression.

For every external record, preserve where applicable:

- original author / organization;
- title;
- year;
- DOI or canonical URL;
- external identifier;
- license or rights note;
- Project-specific interpretation;
- novelty/overlap boundary.

Do not paste article bodies, diagrams, tables, CSS, icons, or proprietary datasets into this layer merely because they are publicly accessible.

No new repository-wide license is granted by this file. Existing scoped license decisions remain unchanged.

## 5. Status discipline

Structured records may use evidence/status labels such as:

`CONCEPT`, `HYPOTHESIS`, `GOVERNANCE_CANDIDATE`, `SYNTHETIC_RESULT`, `PROJECT_RERUN`, `CASE_LEVEL_SUPPORT`, `MODIFY`, `HOLD`, `REJECTED`, `UNRESOLVED`.

The graph must not convert:

- unobserved -> false;
- citation -> validation;
- project rerun -> independent replication;
- AI assistance -> external validation;
- renamed prior art -> novelty.

## 6. External-review use

A reviewer should be able to start from a question or claim and traverse:

`Question -> Claim -> Experiment -> Evidence -> Failure -> Correction -> Current status`

and separately:

`Claim -> Prior art -> overlap boundary -> residual Project claim`.

This lowers review cost while leaving the original evidence untouched.

## 7. Contribution path

External reviewers can report an independent rerun, independent implementation, contradiction, stronger prior art, or negative result using the repository issue template.

A negative result that narrows a claim is a valid contribution.

## 8. Governance

The structured layer fails if it becomes a superior truth source over the original artifacts.

When graph data conflicts with a source artifact or commit history:

`SOURCE_ARTIFACT / COMMIT_HISTORY > GRAPH_INDEX`

The graph must then be corrected.

## 9. Methodological provenance crosswalk (2026-10-21)

Use the [verified original-method references and adoption limits](../PRIOR_ART_FIRST_RESEARCH_POLICY_EN_KO.md) before adding a new graph schema or export. Cochrane separates records, reports and actual underlying studies; PRISMA 2020/PRISMA-S guide reporting of searches and exclusions; FAIR provides discoverability and qualified-reference principles; W3C PROV-O and RO-Crate provide optional interoperability targets; The Turing Way specifies reproducible research bundles; Diátaxis informs reader-facing routes. Existing [PI-RAMP v0.3](../protocols/PI_RAMP_V0_3_KO.md) already references several of these, so no new discovery or novelty is claimed.

**Scope:** Existing graph and claim-impact overlay are *not* asserted FAIR-, PROV-O-, RO-Crate- or PRISMA-compliant. Source documents and Git history remain superior to the graph. An independent reader should be able to follow one bounded claim to an original study, negative or competing result, exact synthetic calculation where applicable, and explicit unknowns. No such reader-effect study has yet been performed.

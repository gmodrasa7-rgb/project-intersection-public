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

## 2. Files

- `schema-v1.json` — machine-readable field contract.
- `graph.json` — current public structured dataset.
- `explorer.html` — dependency-free browser/search interface.
- `validate.py` — integrity and provenance checks.
- `.github/workflows/knowledge-graph-audit.yml` — CI validation.

The canonical scientific source remains the linked artifact and Git history. `graph.json` is a navigation/index layer.

## 3. Information-architecture references

The design was independently reimplemented from general knowledge-base patterns rather than copied from any site's source code, text, CSS, icons, layout, or datasets.

Conceptual references include:

- Open Research Knowledge Graph — research questions/contributions/comparisons;
- Wikidata — entity–relation statements with qualifiers and references;
- OpenAlex — stable typed entities connected by IDs;
- Papers with Code — task/method/dataset/result/code linkage;
- MITRE ATT&CK — matrix-style traversal of structured techniques/failures.

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

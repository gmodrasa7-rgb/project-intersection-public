# External Design Source Registry
## 외부 설계 출처·라이선스 레지스트리

Review date / 조사일: **2026-10-06**

Purpose: record the original/official sources used to inform the Project Intersection structured knowledge layer, what was actually learned from each source, and what copyright/license/trademark boundary applies.

이 문서는 “어디를 참고했는지”뿐 아니라 **무엇을 참고했고 무엇을 복사하지 않았는지**를 보존한다.

Machine-readable record: [source-registry.json](source-registry.json)

---

## 1. Open Research Knowledge Graph (ORKG)

**Original organization / project:** TIB – Leibniz Information Centre for Science and Technology / ORKG.

### Verified design features

Official ORKG materials describe:

- structured descriptions of scholarly contributions;
- research-question-centered **Comparisons** that place multiple contributions into a comparable tabular structure;
- **Templates** that specify a common structure for contributions addressing the same problem;
- machine-actionable / FAIR scientific information.

Primary references:

1. ORKG About — https://orkg.org/about
2. ORKG Academy, Template Course — https://academy.orkg.org/courses/template-course.html
3. Stocker et al. (2023), *FAIR scientific information with the Open Research Knowledge Graph*, DOI: **10.3233/FC-221513**
4. Auer et al. (2020), *Improving Access to Scientific Literature with Knowledge Graphs*, DOI: **10.1515/bfp-2020-2042**

### Rights boundary

The 2023 FAIR Connect article is CC BY 4.0. A 2025 Scientific Data article describing ORKG states that its referenced ORKG data are published under **CC0 1.0 Universal** and ORKG software/components are open source under the **MIT license**. The official TIB ORKG backend repository also identifies an MIT software license.

**Project decision:** architecture inspiration only. No ORKG page text, CSS, source code, figures, icons, or dataset has been copied into Project Intersection.

If ORKG data are imported in the future, current license and dataset-specific provenance must be rechecked at import time.

---

## 2. Wikidata

**Original project:** Wikidata / Wikimedia Foundation and community.

### Verified design features

Official Wikidata documentation defines:

- entities/items;
- statement structure centered on property-value relations;
- subject–predicate–object-like linked data;
- qualifiers that refine or restrict a statement;
- references and ranks attached to statements.

Primary references:

1. Wikidata Data model — https://www.wikidata.org/wiki/Wikidata:Data_model
2. Help:Statements — https://www.wikidata.org/wiki/Help:Statements/en
3. Wikidata Licensing — https://www.wikidata.org/wiki/Wikidata:Licensing

### Rights boundary

Wikidata states that structured data in the main/Property/Lexeme/EntitySchema namespaces is **CC0**. Text in other namespaces is **CC BY-SA 4.0**.

**Project decision:** no Wikidata dump or page text was imported. Project relation qualifiers were independently implemented for evidence scope, evidence class, and source path.

---

## 3. OpenAlex

**Original organization:** OurResearch.

### Verified design features

Official OpenAlex documentation models scholarly information as connected typed entities including works, authors, sources, institutions, publishers, funders, and topics. OpenAlex uses stable IDs and links records to external identifiers including DOI, ORCID, ROR, ISSN, and Wikidata identifiers.

Primary references:

1. OpenAlex Data reference — https://help.openalex.org/data/
2. OpenAlex API reference — https://help.openalex.org/api/

### Rights boundary

OpenAlex's official API documentation states that **all OpenAlex data is CC0**.

**Project decision:** stable typed-ID architecture is a conceptual reference. No OpenAlex record dump is bundled in the current Project graph.

---

## 4. Papers with Code

**Original project:** Papers with Code; community project supported by Meta AI Research.

### Verified design features

Its official About page describes a resource connecting:

- papers;
- code;
- datasets;
- methods;
- evaluation tables / benchmark results.

This is the design precedent for keeping research objects navigable by role rather than embedding everything into one prose document.

Primary references:

1. About Papers With Code — https://paperswithcode.com/about
2. Dataset Licensing Guide — https://paperswithcode.com/datasets/license

### Rights boundary

Papers with Code states that its website content/data is **CC BY-SA**. It also explicitly warns that licenses for indexed datasets, code, annotations, and underlying assets may differ and must be checked independently.

**Project decision:** no Papers with Code data, tables, text, CSS, or visual layout was copied. This avoids importing CC BY-SA content into the v1 knowledge layer.

---

## 5. MITRE ATT&CK®

**Original organization:** The MITRE Corporation.

### Verified design features

MITRE's official documentation describes ATT&CK as a structured knowledge base of adversary behavior using hierarchical concepts including:

- tactics — why;
- techniques — how;
- sub-techniques — more specific behaviors;
- procedures — observed/specific implementations.

This informed the idea of matrix/taxonomy navigation from abstract failure mechanisms to concrete cases. Project Intersection does **not** adopt ATT&CK's cyber taxonomy.

Primary references:

1. Get Started — https://attack.mitre.org/resources/
2. Terms of Use — https://attack.mitre.org/resources/terms-of-use/
3. Legal & Branding — https://attack.mitre.org/resources/legal-and-branding/

### Rights / trademark boundary

MITRE grants a non-exclusive, royalty-free license to use ATT&CK for research, development, and commercial purposes, with required copyright/license notice for copies. MITRE also states that MITRE ATT&CK® / ATT&CK® are registered trademarks and their use must not imply endorsement.

**Project decision:** no ATT&CK content, matrix, technique text, IDs, logo, or code was copied. MITRE ATT&CK is named only as a design reference.

---

## 6. What Project Intersection actually reused

The Project reused **abstract information-architecture ideas**, not protected site expression:

| Project feature | External precedents | Project-specific implementation |
|---|---|---|
| Question → Claim → Experiment → Evidence | ORKG, Papers with Code | Adds evidence class, failure/correction lineage, claim-state boundary |
| Typed entities with stable IDs | OpenAlex, Wikidata | Local IDs: RQ / CL / GR / PA / EX / EV / HC / NC / FR / CR |
| Qualified relations | Wikidata | `scope + evidence_class + source_path` are mandatory |
| Failure/mechanism traversal | MITRE ATT&CK | Research/governance failures, not cyber techniques |
| Comparison-oriented review | ORKG | Claim/prior-art/evidence/counterexample comparison |

This combination is not claimed as a new scientific discovery merely because the components are recombined.

---

## 7. Import rule

Future external-data ingestion requires, per imported source:

`original creator / organization`  
`canonical URL or DOI`  
`retrieval date`  
`external ID`  
`license / rights status`  
`what was copied vs merely linked`  
`Project interpretation`  
`novelty boundary`

If rights are unclear, use **link/citation only** until resolved.

If source material conflicts with the Project's structured summary:

`ORIGINAL SOURCE > PROJECT SOURCE REGISTRY > GRAPH INDEX`

The registry itself does not validate Project scientific claims.

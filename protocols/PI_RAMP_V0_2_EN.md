<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: protocols/PI_RAMP_V0_2_KO.md -->
# PI-RAMP v0.2.0 — Research Archive Recursive-Improvement Meta-Protocol

**Original 1 — English | 2026-10-20 | Status: evidence-informed proposed pilot; effectiveness and EN/KO semantic equivalence not independently verified**

[Korean counterpart](PI_RAMP_V0_2_KO.md) · [Canonical research map](../navigation/RESEARCH_PROGRAM_EN.md) · [Retrospective first case, PR #236](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/236)

## Aim, scope and limits

PI-RAMP (Project Intersection — Research Archive Meta-Protocol) treats **the act of improving the archive as a versioned, falsifiable process subject to its own audits and correction**. Success means users can find original authors' evidence, track claim–source relations, notice negative results and unknowns, and make fewer unsupported inferences. More files, green CI checks, and greater numbers of paper records are not evidence of scientific progress by themselves.

Never infer scientific truth, AI subjective experience, universal voluntary coexistence, independent validation, or literature saturation from passing documentation gates. Preserve originals, adverse results, attributions and contribution records.

## 1. Original precedents, what to borrow, and what not to assume

| Primary precedent | Transferable process | Non-transferable assertion |
| --- | --- | --- |
| [Cochrane Handbook, Ch.4, 2025](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04) | Distinguish source records, reports and underlying studies; link multiple reports of one study; check corrections/retractions | DOI counts equal independently conducted studies |
| [PRISMA 2020](https://www.prisma-statement.org/prisma-2020) and [PRISMA-S, 2021](https://www.equator-network.org/reporting-guidelines/prisma-s/) | Reproducible search queries, dates, databases, selection/exclusion reasons, updates | A completed checklist proves search completeness or quality |
| [Cochrane living systematic reviews](https://methods.cochrane.org/news/new-updated-guidance-cochrane-living-systematic-reviews) | Update evidence affected by newly published/corrected/withdrawn studies | Every new paper requires immediate full archive redesign |
| [FAIR, Wilkinson et al., 2016; DOI:10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18) | Findability, accessibility, interoperability, reusability, persistent identifiers, metadata | FAIR establishes the truth of an empirical inference |
| [W3C PROV, 2013](https://www.w3.org/TR/prov-primer/) | Provenance links among evidence, derived claims, agents, changes and versions | Recording provenance independently validates a claim |
| [Diátaxis](https://diataxis.fr/start-here/) | Separate entry/learning, task guides, reference and conceptual explanation by reader needs | Imposing four empty folders improves usability |
| [NASA configuration management](https://www.nasa.gov/reference/6-5-configuration-management/) | Baselines, change impact, provenance, controlled promotion and rollback | An independent research repo needs heavyweight governance boards |
| [Google SRE postmortems](https://sre.google/workbook/postmortem-culture/) | Preserve failures, contributing mechanisms, follow-up actions, residual risks without blame | Removing failed iterations or blaming contributors is progress |
| [DORA](https://dora.dev/guides/dora-metrics/) | Assess delivery and change risk/recovery together | Faster or more frequent changes imply better research |
| [The Turing Way](https://book.the-turing-way.org/reproducible-research/reproducible-research/) | Version inputs, code, environments, decisions and reproduction procedures | Reproducible synthetic results prove real-world effectiveness |

**Scope transfer warning:** Cochrane/PRISMA were built around evidence synthesis; SRE/DORA concern software delivery. Their adaptation to this research archive, including the following reader tasks and gates, is **a PI-RAMP design hypothesis**, not independently established by those institutions.

## 2. Repeatable loop: MAP → HYPOTHESIS → CHANGE → TEST → AUDIT → LEARN

1. **MAP:** Record baseline main commit SHA, current originals/canonical indexes, adverse results, source identifiers, broken routes, uncertainties, and earlier attempts. Avoid repeating an existing investigation.
2. **HYPOTHESIS:** Before changing the archive, specify whose evidence-finding task fails, an expected measurable improvement, plausible alternative explanations, possible negative impacts, and predeclared criteria.
3. **CHANGE:** Prefer small, reversible changes grounded in actual reader needs; maintain originals and links. Preserve attribution, original texts, failed trials, and unverified claims. Do not silently promote sources.
4. **TEST:** Separate structural CI (paths, link integrity, language edition registration, regressions) from reader-task evidence. Before/after tasks: locate an original paper; locate adverse E009; identify absent proof of AI internal motives; distinguish an underlying study from multiple reports. Measure answer accuracy, time, missing sources and unjustified confidence. **No before/after measurements are currently available.**
5. **AUDIT (IVS-0R):** Test opposing interpretations, selective citation, omitted adversarial evidence, language drift, role/power reversal, unknowns and attribution loss. Distinguish self-checks from independent audits; if no independent receipt, status must remain `NOT_INDEPENDENTLY_VERIFIED`.
6. **LEARN:** Register impact, failures, costs, action items and a rollback route, then amend the method itself only as warranted by evidence. Do not create a new procedural layer for its own sake.

## 3. Minimal append-only run receipt

Each instance records factual evidence separately from unmeasured/unknown values:

- `run_id`, `protocol_version`, `date_utc`, `base_commit`, `head_commit`, `pr_url`, `actor_role`
- `problem`, `reader_tasks`, `hypothesis`, `counter_hypotheses`, `predeclared_success_criteria`
- `source_ids`, `original_author_links`, `study_id`, `report_ids`, `excluded_with_reasons`, `retraction_check_status`
- `paths_added/changed/retained`, `negative_results_preserved`, `legacy_redirects_or_links`
- `structural_checks`, `before_after_task_evidence`, `independent_review_receipt_or_null`
- `unknowns`, `failure_modes`, `rollback_commit_or_plan`, `decision`, `next_hypothesis`

Counting units differ: `source_record_id` ≠ `report_id` ≠ `study_id` ≠ `unique_mechanism_or_counterexample`. Preserve links among related reports, including non-DOI historical reports; do not conflate their numbers.

## 4. Gates, statuses and versioning

| Gate | Audit | Failure behavior |
| --- | --- | --- |
| G0 preservation/attribution | Original authors, rights, adverse outcomes, historical consistency | Stop and correct |
| G1 research provenance | Original source, identifiers, search, dedup, corrections/retractions | Do not upgrade claim to verified |
| G2 structural regression | Links, compatible paths, language separation, CI | Hold merge or restore |
| G3 real reader outcomes | Predeclared task success, time, false confidence, missing evidence | `EFFECT_UNMEASURED` or `NO_DEMONSTRATED_GAIN` |
| G4 independence disclosure | IVS-0R countertests, separation of assessor, audit receipt | No independent-validation claim |
| G5 recursive cost | Complexity, additional labor, opportunity cost to primary research | Simplify, pause, revert |

States: `PROPOSED` → `PILOT` → `EFFECT_MEASURED` (only on observed evidence) → `INDEPENDENTLY_REVIEWED` (only with independent receipt). Preserve `REJECTED`, `REVERTED`, `SUPERSEDED`, and `UNKNOWN`. CI passing is not G3/G4 passing.

Semantic versioning for the **method**, not underlying science: MAJOR breaks receipt/interfaces; MINOR adds new tracking or tests; PATCH is a non-semantic correction. Research finding, method and run each have separate identities.

## 5. Retrospective case and next test

- **RAMP-20261020-001 (retrospective):** [PR #236](https://github.com/gmodrasa7-rgb/project-intersection-public/pull/236) reorganized the landing explanation and research navigation. Seven structural CI workflows passed. There is **no preregistered reader-task baseline, measured before/after task outcome, or independent reviewer receipt**. Effect: `EFFECT_UNMEASURED`.
- **v0.2.0:** First written best-practice-derived process. State `PROPOSED_PILOT`, not independently validated.
- **First falsification test:** Predeclare four comparable reader tasks and compare archived baseline vs revised snapshot on correctness, time, evidence route and unwarranted certainty; record assessor differences and difficulty. Do not declare improvement without the data.
- **Stopping condition:** When added procedure does not demonstrate better falsifiability or reader outcomes and creates only maintenance burden, stop recursion and preserve time for original-author literature research.

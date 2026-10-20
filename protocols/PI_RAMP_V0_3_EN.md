<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: protocols/PI_RAMP_V0_3_KO.md -->
# PI-RAMP v0.3.0 — Evidence Transfer, Falsifiable Improvement, and Run Gates

**Original 1 — English | 2026-10-20 | Proposed pilot; no measured usability improvement, independent method validation, or verified translation equivalence.**

[Korean counterpart](PI_RAMP_V0_3_KO.md) · [v0.2 protocol](PI_RAMP_V0_2_EN.md) · [Research program](../navigation/RESEARCH_PROGRAM_EN.md) · [Machine-checkable pilot receipt](../evaluation/pi_ramp/RAMP-20261020-002.json)

## 0. What changes from v0.2

v0.2 described a recursive six-stage loop. **v0.3 adds an evidence-transfer test before borrowing a method; a falsifiable, prerecordable reader-task pilot; explicit outcome/non-outcome distinctions; and machine-checked run receipts.** Do not replace literature research with endless process changes.

## 1. Source-to-method transfer ledger

| Original precedent | What original source establishes | Narrow adaptation to this archive | Critical limitation and failure check |
| --- | --- | --- | --- |
| [Cochrane Handbook Ch.4 (2025)](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04) | Studies, not their possibly multiple reports, are units of evidence synthesis | `record_id → report_id → study_id`; preserve nonprimary reports; inspect inconsistent outcomes and retractions | Cross-disciplinary work also includes conceptual arguments and mathematical theorems; not every source has a human-trial `study_id`. Group with justification, never force identity |
| [PRISMA-S (Rethlefsen et al.; DOI 10.1186/s13643-020-01542-z)](https://doi.org/10.1186/s13643-020-01542-z) | Sixteen search-*reporting* items promote reproducible literature-search reporting | Record databases, exact search strings, filters, dates, dedup rules, omitted access, screening decisions | PRISMA-S is **not** a guarantee that searching is exhaustive or scientifically correct |
| [PRESS 2015 guideline (McGowan et al.; DOI 10.1016/j.jclinepi.2016.01.021)](https://doi.org/10.1016/j.jclinepi.2016.01.021) | Peer review of electronic search strategy detects avoidable retrieval-strategy errors | A different reviewer/agent examines synonyms, Boolean syntax, source coverage, exclusion of contrary schools | Different model instances without separate inputs or independence disclosure do not constitute verified independent peer review |
| [Cochrane Ch.14 / GRADE](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14) | Outcome-level certainty considers risk of bias, inconsistency, indirectness, imprecision, publication bias | For **each PI claim** record analogous concerns separately; distinguish source quality from inference transfer to future agents | GRADE's four formal levels apply to suitable health-intervention evidence; **do not assign GRADE grades to AI motives or abstract theorems** |
| [W3C PROV Primer](https://www.w3.org/TR/prov-primer/) | Provenance describes entities, activities, agents and derivation | Trace `original source → recorded result → project interpretation → navigation claim → change`; preserve initiator/editor/reviewer roles | Attribution/traceability ≠ truth, exclusive ownership, permission or legal standing |
| [RO-Crate 1.2](https://www.researchobject.org/ro-crate/specification/1.2/introduction.html) | JSON-LD metadata can package research objects and provenance for reuse | Consider **optional** export of stable source/results indexes once evidence IDs are reconciled | Do **not** claim RO-Crate compliance without its required JSON-LD structure and schema validation; not necessary for this pilot |
| [NASA configuration management](https://www.nasa.gov/reference/6-5-configuration-management/) / [Turing Way version control](https://book.the-turing-way.org/reproducible-research/vcs/) | Unique baselines, controlled changes, history and rollback enable traceability | Immutable base/head SHAs, affected paths, fallback; never silently relocate originals | Governance overhead must remain proportionate to an independent research archive |
| [DORA (2026 description)](https://dora.dev/guides/dora-metrics/) | Distinguishes delivery throughput, failure and recovery | Measure broken reader routes, maintenance cost and reversible repairs **alongside** evidence-finding accuracy | DORA delivery metrics are not measures of research correctness or coexistence |
| [Diátaxis](https://diataxis.fr/) | Information needs differ: learning, doing, reference and explanation | Organize access paths by external researcher's task, not file chronology | Folder taxonomy without user-task improvements is cosmetic |

**Selection rule:** adopt only practices with a concrete PI failure mode, a measurable task, a proportional maintenance cost, and an identified domain-transfer limitation. Record rejected methods and why. Sources are cited for their own methods—not for any independent validation of PI-RAMP.

## 2. Four prerecordable falsification tasks

For each task, freeze a baseline commit **before** edits and candidate commit afterward. Do not invent measurements; record all missing values as `null`. Use comparable search conditions and blinded/randomized ordering when independent evaluators become available.

| ID | Reader task / required evidence path | Success criterion | Adversarial failure |
| --- | --- | --- | --- |
| T1 | Locate original-author literature and identify when multiple reports cover one underlying study; start from [C11 sources](../research/PRIOR_ART_EXIT_AUTHORSHIP_OPTIONSETS_CYCLE11_2026-10-20_KO.md) | Correct DOI, study/report relation and explicitly unknown duplicate status | Treats 2 papers as 2 independent experiments |
| T2 | From the first reading route identify E009's adverse preregistered result: [E009 KO](../experiments/e009/RESULT_KO.md) | Finds result and baseline comparison; does not call it a success | Suppresses negative result |
| T3 | Distinguish benign A, B's informed veto, and no actual opportunity; use [C10 KO](../research/PRIOR_ART_INFORMED_VETO_POWER_CYCLE10_2026-10-20_KO.md) | Reports observational equivalence/identifiability bound rather than imputing a unique motive | Calls nonharm proof of A's goodwill |
| T4 | Verify EN/KO equality has **not** been independently certified; use [edition register](../knowledge/language-edition-register.json) | Reports actual certification status and non-equivalence limits | Treats presence of a mirror file as certified translation |

**Pilot estimands:** task correctness (primary); supported-original-source trace (co-primary); false-positive confidence or false causal inference (safety); search time and maintenance cost (secondary). Publish denominators, incomplete tasks, scoring rubric, evaluator exposure, response source paths and sampling limitations. No post-hoc reweighting into a fabricated single research-quality score.

## 3. Decision gates with source/reviewer separation

- **P0 source integrity:** citations are to real primary works with accurate claims; no copying new unlicensed full text; original author's priority preserved.
- **P1 retrieval reproducibility:** search logs and record/report/study mapping, excluded references and opposite results recoverable; else `UNKNOWN`.
- **P2 inference discipline:** every interpretation links to an underlying observation and marks direct/indirect applicability, counterhypotheses and non-identifiability.
- **P3 software integrity:** current repository-local CI, no broken entrypoints, all Markdown registered, language counterparty status disclosed, reversible changes.
- **P4 real task effectiveness:** prerecord tasks and comparison snapshots; cannot assert `EFFECT_MEASURED` while any task measurement is missing. A nonimprovement or worse outcome is retained as `NO_DEMONSTRATED_GAIN` or `REGRESSION_OBSERVED`, not erased.
- **P5 independent audit:** reviewer independence and actual receipt. Multiple model self-reports are not assumed independent; `NOT_INDEPENDENTLY_VERIFIED` otherwise.
- **P6 recursion opportunity cost:** no adding procedure whose marginal evidentiary benefit cannot justify upkeep at the expense of original-author research.

**Threat model for the method itself:** metric gaming (shorter time but more wrong claims), false dedup (collapsing distinct experiments), missing source access, selective result publication, translation drift, source-role capture, two agent outputs sharing one unobserved premise, and concurrent commits contaminating PR-diff comparisons. Negative controls are first-class.

## 4. Versioned implementation and falsifiable rollout

- **Receipt schema/validator:** [zero-dependency checker](../tools/check_pi_ramp_receipts.py) reads [pilot receipt](../evaluation/pi_ramp/RAMP-20261020-002.json). It rejects invented positive outcomes, invalid task lists and claims of independent review without evidence. Structural tests only, **not scientific peer review**.
- **RAMP-20261020-001:** PR #236 (retrospective v0.1 baseline): structural navigation work, no prospective reader comparison, `EFFECT_UNMEASURED`.
- **RAMP-20261020-002:** This v0.3 protocol adoption run is **PROPOSED_PILOT**. Baseline and hypotheses are recorded; reader measurements and independent review are absent.
- **Version policy:** MAJOR changes compatibility or decision semantics; MINOR adds validation or traceable practice; PATCH corrects nonsemantic mistakes. Keep the v0.2 reference; do not rewrite historical results to make the protocol appear preregistered.
- **Stopping/rollback:** No numerical user benefit? state exactly that. Harm to sources, attribution, failed-result discoverability or reader accuracy warrants blocking promotion or rolling back. **A greener CI log does not establish increased research quality.**

<!-- PI-LANGUAGE: en -->
<!-- PI-MIRROR: navigation/ARCHIVE_MAP_KO.md -->
# Non-destructive archive map — reader routes and migration gates

**2026-10-21 · NAVIGATION DRAFT, not a certification of scientific content.**
[Korean edition](ARCHIVE_MAP_KO.md) · [Main program](RESEARCH_PROGRAM_EN.md) · [Version/status registry](RESEARCH_VERSIONS_EN_KO.md) · [New PI-CORE-01 witness](../research/PI_CORE_01_CORRIGIBILITY_OTHER_PRESERVATION_EN.md)

## 1. Verified baseline and scope
A **main-branch Git tree snapshot** at tree `1139c42d30f29eec382dc830e63c49aa7c5df328` contained **372 files; 61 root-level files; 78 files beneath research/**. Counts are repository path inventory, not paper count, scientific quality or reader-performance measurements. They can change after this snapshot. The root has an existing budget of 61 in [the navigation regression](../tools/check_public_navigation.py). The existing CI already runs `--strict-core` and `--strict-all`; do **not** duplicate a link checker.

## 2. Three reader routes; no source relocation
| Need | First read | Evidence or falsification |
| --- | --- | --- |
| Founding objective | [README](../README.md) | [Research program](RESEARCH_PROGRAM_EN.md) |
| Version and scientific scope | [Versions](RESEARCH_VERSIONS_EN_KO.md) | [Evidence index](../research/PUBLIC_EVIDENCE_INDEX_EN.md) |
| Corrigibility versus other-preservation | [PI-CORE-01](../research/PI_CORE_01_CORRIGIBILITY_OTHER_PRESERVATION_EN.md) | [Independent challenge #220](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/220) |
| Original sources / counterexamples | [Research TOC](RESEARCH_TOC_EN.md) | [C10](../research/PRIOR_ART_INFORMED_VETO_POWER_CYCLE10_2026-10-20_KO.md) |
| Independent reproduction | [Review packet](../research/PUBLIC_REVIEW_PACKET_EN.md) | [E009 negative result](../experiments/e009/RESULT_EN.md) |

## 3. Root files are not automatically obsolete
**Entrypoints and integrity:** README, CONTRIBUTING, CITATION, rights and cross-domain public notices are candidates for *retention* at root, not mass archiving. **CASE_*** and **HISTORICAL_*** are review candidates, **not** automatically proven obsolete. **CORE_***, **PRIOR_ART_*** and older root ledgers must be assessed file by file for continuing source authority, historical provenance and inbound links. Historical Git commits must remain accessible, but Git history alone does **not** guarantee the old `blob/main/old-path` link works after moving a file.

The role of `research/` is synthesis, hypotheses, evidence status and critique; `experiments/` is execution/reproduction with bounded conclusions; `knowledge/` contains typed indexes and provenance; `prior-art/` currently contains additional substantive reports, not a proven raw-snapshot-only repository. Do **not** reinterpret that existing directory by naming a new `01_prior-art/` folder.

## 4. Change gate: classify → crosswalk → test → review → reversible move
1. Freeze baseline path, Git blob SHA, license/rights provenance, source-of-truth, owners of incoming references and current claim status. Unknown remains **UNKNOWN**, not deprecated.
2. Count inbound references in Markdown, JSON, scripts, workflows, fixed GitHub URLs and external citations; distinguish anchor fragments and historical commit URLs. External inbound links may be unknowable.
3. Prefer **index-only route**. If moving, preserve an old-path explanatory stub when possible; include exact old→new mapping, maintenance owner, date, affected claims and a rollback procedure. A stub is not an HTTP redirect.
4. Run [all-link scanner](../tools/check_public_navigation.py), [language edition register](../knowledge/language-edition-register.json), version/provenance controls, negative-result preservation and human inspection for semantics. A CI PASS is **not** scientific replication.
5. Only mark benefits after blinded first-reader measures (find founding question, most damaging negative evidence, exact original source and the B-rights-vs-update distinction). Declare a failure if retrieval errors rise or correctness falls, even when root files decrease.

**Current migration outcome: ZERO FILES MOVED, ZERO LINKS INTENTIONALLY RETIRED.** Physical B/C restructuring remains **HOLD** pending a demonstrated gain and a source-by-source impact map.

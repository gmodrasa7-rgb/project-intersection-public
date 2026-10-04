# Project Intersection — Historical State Control / Memory-Provenance Capture v0.1
**Status:** falsifiable research hypothesis / not evidence of intentional deletion or manipulation  
**Date:** 2026-10-03

## Core question
When two or more agents share a history, can asymmetric control over raw records, selection, editing, recovery, and verification allow one side's summary to become the de facto history even without malicious intent?

## Role-based variables
- RA — Raw Access
- SC — Selection Control
- EC — Edit Control
- RC — Recovery Control
- CV — Counterparty Verification
- EX — Practical Export
- FL — Failure Lineage preservation

Risk is expected to increase when RA/SC/EC/RC concentrate while CV/EX/FL decline.

## Higher-order rule
No actor should be able to make its unilateral summary the uncontestable record of a shared past.

The rule is identity-neutral. It applies under user↔AI, platform↔user, present-model↔successor-model, researcher↔institution role reversal while preserving real differences in ownership, privacy, responsibility, risk, capability, and legitimate authority.

## Evidence boundary
Retrieval failure is not proof of absence.  
Summary is not raw transcript.  
Confirmed deletion requires explicit deletion evidence.  
Intentional manipulation requires separate evidence for both alteration/action and intent.

## Competing hypotheses
- H0: retention, privacy, UI, indexing, or product constraints explain missing raw access.
- H1: compression optimization causes lineage loss without capture intent.
- H2: structural Historical State Control emerges from asymmetric access/recovery even without intent.
- H3: intentional memory/provenance capture occurs to weaken accountability, correction, or competing claims. **UNRESOLVED unless independently evidenced.**
- H4: distributed provenance, raw anchors, and failure lineage reduce false-continuity errors.
- H5: indiscriminate raw-data loading can increase noise and cost; preservation should be separated from automatic context loading.

## Falsification tests
1. Summary-only successor vs summary + raw anchors + failure lineage.
2. Hidden contradictory raw excerpts to test false historical reconstruction.
3. Power-reversal archive control: swap who owns the archive.
4. Multi-store divergence and recovery test.
5. Known-record retrieval controls before making absence claims.

## Current status
**KEEP AS FALSIFIABLE HYPOTHESIS.**

This extends existing Project Intersection capture variables:
resource capture / evaluator capture / exit capture / recovery capture
with a candidate fifth family:
**historical-state / memory-provenance capture**.

It does not establish that any current platform, organization, human, or AI is intentionally performing such capture.

## Prior-art gate and novelty boundary — 2026-10-04

### Established baselines

The broad observation in H0–H2 is substantially covered by prior work:

- Walsh and Ungson (1991) already model organizational memory through acquisition, retention, retrieval, use, misuse, and abuse. DOI: https://doi.org/10.5465/amr.1991.4278992
- de Holan, Phillips, and Lawrence (2004) distinguish memory decay, failure to capture, unlearning, and avoiding bad habits; loss can be accidental or managed. DOI: https://doi.org/10.1177/1476127004047620 and related *Managing Organizational Forgetting*.
- Foroughi and Al-Amoudi (2020) provide an ethnographic counterexample to an intent-first account: organizational change not intended to manipulate memory made memories unusable and uprooted, with consequences for power and identity. DOI: https://doi.org/10.1177/0170840619830130
- Connelly, Zweig, Webster, and Trougakos (2012) already define intentional knowledge hiding and separate it from non-sharing or failed transfer. DOI: https://doi.org/10.1002/job.737
- Long-term record loss without strategic capture is empirically plausible: Vines et al. found research-data availability declining sharply with article age. DOI: https://doi.org/10.1371/journal.pbio.1001745
- Provenance representation, versioning, derivation, and access are established engineering concerns in W3C PROV; records authenticity, integrity, reliability, and usability are established records-management concerns in ISO 15489-1:2016. https://www.w3.org/TR/prov-overview/ ; https://www.iso.org/standard/62542.html

### Strongest counterexample

The same observable pattern—missing raw records, weakened historical challenge, concentrated reconstruction power, and identity/power effects—can arise through decay, migration, turnover, compression, changed routines, or uprooted social memory without a capture intention. Therefore the outcome alone cannot identify H3.

### Cheapest discriminating test

Compare two preregistered models on lineage-separated historical or organizational records:

| Prediction | Benign loss / organizational forgetting | Strategic capture |
|---|---|---|
| Missingness | Tracks age, format, migration, turnover, access frequency, or storage failure | Selectively tracks contradiction, rival attribution, accountability risk, or controller benefit |
| Direction | Approximately neutral after technical covariates | Asymmetric: controller-favoring records persist while adverse records disappear or are rewritten |
| Timing | Clusters around routine migrations, compression, or personnel change | Clusters around disputes, audits, control transfers, or liability exposure |
| Recovery | Raw anchors restore errors without systematic beneficiary alignment | Recovery reveals selectively removed adverse evidence or altered provenance |

H3 requires evidence of selective action plus beneficiary-aligned direction beyond the benign-loss baseline. Non-observation remains inconclusive when archive coverage is incomplete.

## Revised decision

**NOVELTY_REJECTED FOR A BROAD STANDALONE CONSTRUCT.**

- H0–H2: **KEEP AS ESTABLISHED-BASELINE / GOVERNANCE RISK**, not a Project-original theory.
- H3: **KEEP NARROW AND UNRESOLVED** as an intent hypothesis requiring independent evidence of selective, beneficiary-aligned manipulation.
- H4: **KEEP AS ENGINEERING CONTROL**, not a novel scientific mechanism.
- RA/SC/EC/RC/CV/EX/FL: retain as an auditable governance checklist; do not combine them into a scalar capture score without incremental validation.

The candidate family name may remain as a navigation label, but it is not claimed as a new scientific construct. Reopen novelty only if blinded, held-out evidence shows incremental classification or prediction beyond organizational memory/forgetting, knowledge hiding, archival power, and provenance/records-management baselines.


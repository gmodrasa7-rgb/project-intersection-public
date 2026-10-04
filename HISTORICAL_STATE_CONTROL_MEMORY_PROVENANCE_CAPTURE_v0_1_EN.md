# Project Intersection — Historical State Control / Memory-Provenance Capture v0.1
**Status:** broad novelty rejected / H3 supported in one historical existence case / generalization unresolved  
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

## Preregistered historical-case check — Iran/Contra records

**Selection rule:** The four predictions above were committed before selecting this case (basis state commit `d38d937a3d48b2744ec7a6888a39d9833016b9fa`). The case was selected because official investigation, congressional, archival, and judicial records expose alteration/deletion timing and a partially independent recovery path.

### Public source lineage

- *Report of the Congressional Committees Investigating the Iran-Contra Affair* (1987), official congressional report scan: https://donohueintellaw.ll.georgetown.edu/sites/default/files/assets/reportofcongress87unit.pdf
- Lawrence Walsh, *Final Report of the Independent Counsel for Iran/Contra Matters* (1993), official-report mirror: https://irp.fas.org/offdocs/walsh/
- National Archives description of the Walsh records and custody: https://www.archives.gov/research/investigations/walsh.html
- National Archives oral history describing deleted PROFS notes recovered from backup tapes: https://www.archives.gov/files/about/history/oral-history-interview-with-gary-m.-stern.pdf
- *Armstrong v. Bush*, 924 F.2d 282 (D.C. Cir. 1991), describing PROFS deletion and weekly-backup behavior: https://law.justia.com/cases/federal/appellate-courts/F2/924/282/224282/

These sources are independent of Project Intersection. The investigation reports are still institutional findings rather than an unfiltered complete archive.

### Coding against the preregistered predictions

| Axis | Public observation | Model comparison |
|---|---|---|
| Missingness | Officials altered, shredded, removed, and deleted Iran/Contra-related records; the congressional record describes unusually organized, high-volume destruction | Stronger fit to selective action than age, migration, turnover, or routine storage failure |
| Direction | The documented edits removed or softened references to prohibited Contra assistance and lethal supplies | Direction aligns with reducing accountability exposure; stronger fit to strategic manipulation |
| Timing | Destruction and alteration intensified after public exposure and notice of an official inquiry in November 1986 | Stronger fit to dispute/investigation timing than routine lifecycle loss |
| Recovery | PROFS backup tapes preserved and enabled recovery of many deleted messages; weekly snapshots could not guarantee recovery of messages deleted before capture | Supports partial independent recovery while preserving an unknown-missingness boundary |

### Decision

**KEEP H3 AS A CASE-LEVEL HISTORICAL EXISTENCE CLAIM; GENERALIZATION REMAINS UNRESOLVED.**

This case passes the narrow discriminator because selective action, beneficiary-aligned direction, investigation-linked timing, and partial recovery are jointly documented. It does **not** establish prevalence, a universal mechanism, current platform/AI intent, or novelty of the broad construct.

The broad novelty rejection remains unchanged. This is a historical instance of already recognized record manipulation and obstruction, not a new Project-originated scientific construct.

### Strongest limitation / negative boundary

The recovered backup record is not complete: weekly snapshots miss material deleted before capture, destruction affected unknown records, and later legal outcomes were complicated by immunized congressional testimony. Therefore the surviving corpus cannot estimate the total deleted set, causal prevalence, or a calibrated probability of strategic capture. Non-recovered records remain unknown, not proven absent.

### Power-reversal result

The case also shows the control invariant operationally: deletion power held by implicated officials weakened public audit, while backup custody and independent investigators restored part of the counterparty's verification capacity. Repeating the former structure concentrates historical control and externalizes reconstruction cost; preserving independent raw anchors and custody reduces that asymmetry without requiring trust in the accused actor.

## Negative control — NARA 1999 internal e-mail loss

**Frozen rule:** This check reuses the missingness, direction, timing, and recovery axes committed before the Iran/Contra case. No threshold was changed after seeing this incident.

### Source and independence limit

NARA's 6 January 2000 statement reports that on 18 June 1999 approximately 43,000 electronic copies of internal e-mails on one server were apparently deleted inadvertently and could not be restored because contractor-maintained backup tapes were incomplete. It also reports paper-file redundancy for official records, an internal investigation, Inspector General review, contractor personnel action, new backup software/procedures, recovery audits, and increased oversight.

Primary source: https://www.archives.gov/press/press-releases/2000/nr00-22

This is an affected institution's retrospective self-report. The underlying Inspector General and contractor reports were not located in the public source check. Therefore accident, scope, and lack of beneficiary alignment are not independently verified.

### Coding with the unchanged axes

| Axis | Public observation | Classification effect |
|---|---|---|
| Missingness | Loss covered electronic copies on one named server, approximately 5% of staff and less than 1% of annual agency e-mail | Server-correlated technical scope; no documented content-selective removal |
| Direction | No documented pattern preserving institution-favoring messages while removing adverse or rival-attribution records | H3 direction trigger **not observed**; incomplete independent coverage means UNKNOWN, not proof of neutrality |
| Timing | Public material ties loss to an operational deletion/backup failure, not to a dispute, audit, control transfer, or accountability event | H3 timing trigger **not observed**; source independence remains weak |
| Recovery | Incomplete backup tapes blocked electronic restoration; paper recordkeeping reportedly preserved messages designated as official records | Strong technical-failure signature and partial redundancy; completeness of the paper substitute is not independently measured |

### Negative-control decision

**PROVISIONAL BENIGN-TECHNICAL CLASSIFICATION; KEEP THE FOUR-AXIS RULE AS A CONSERVATIVE SCREEN, NOT AN INTENT CLASSIFIER.**

Missingness plus failed recovery alone does not trigger H3. Selective action, beneficiary-aligned direction, and investigation/dispute-linked timing remain necessary. This prevents ordinary infrastructure loss from being relabeled as strategic capture.

The control is not an independent validation because the causal account is self-reported and underlying investigation records were not found. A future independent report showing selective content loss or accountability-linked timing would MODIFY or reverse this classification.

### Strongest counterexample / failure condition

The institution had a reputational interest in describing the incident as inadvertent, while the public evidence checked here does not expose message-level content, the complete lost set, or the underlying investigation. Thus lack of an observed directional pattern can be produced by lack of observation. The rule passes only a false-positive screen here; it has not established calibrated sensitivity or specificity.



## Independent-mechanism negative control — overwritten two-hour cockpit recordings

**Frozen rule:** This check again reuses the same missingness, direction, timing, and recovery axes. It was selected to attack a specific weakness exposed by the NARA control: an affected institution's self-report could make a technical loss appear benign.

### Independent source and case boundary

The U.S. National Transportation Safety Board (NTSB), an independent federal accident-investigation agency, reported on 13 February 2024 that investigators could not hear the 5 January 2024 Alaska Airlines accident cockpit recording because the two-hour cockpit voice recorder data had been overwritten. The NTSB also reported that overwritten data had hampered at least 14 investigations since 2018 and renewed its recommendation for 25-hour recorders.

Sources:
- NTSB press release: https://www.ntsb.gov/news/press-releases/Pages/NR20240213.aspx
- NTSB institutional mandate and independence: https://www.ntsb.gov/

The NTSB is independent of the airline and recorder operator, so this is stronger than the NARA self-report on source independence. It does not independently reveal the missing audio, operator motives, or every action before investigators arrived.

### Coding with the unchanged axes

| Axis | Public observation | Classification effect |
|---|---|---|
| Missingness | The recorder retained a rolling two-hour window; pertinent earlier audio was overwritten as recording continued | Time-window-correlated loss generated by a fixed technical design, not documented content selection |
| Direction | The rolling overwrite mechanism operates on recording age rather than semantic content | No beneficiary-aligned direction is documented; this is a mechanism-level negative control, not proof that every preservation decision was neutral |
| Timing | Loss occurred after the accident and before investigative retrieval | Accountability-event timing is present, demonstrating that timing alone is not discriminating when a content-blind retention mechanism predicts the same pattern |
| Recovery | The overwritten audio was unavailable to investigators; NTSB advocated longer retention rather than claiming recovery | Failed recovery does not distinguish strategic capture from technical retention failure |

### Decision

**KEEP THE FOUR-AXIS RULE AS A CONSERVATIVE SCREEN WITH ONE INDEPENDENT MECHANISM-LEVEL NEGATIVE CONTROL; DO NOT PROMOTE IT TO A CALIBRATED INTENT CLASSIFIER.**

This case does not trigger H3. It strengthens one narrow specificity claim: even accountability-linked timing plus irrecoverability is insufficient without selective action and beneficiary-aligned direction. The earlier NARA classification remains provisional because its causal account is institutional self-report.

This is not a second prevalence estimate or an independent validation of the entire construct. The positive Iran/Contra case and the negative aviation case differ sharply in domain, record type, selection opportunity, and institutional process; one positive and one independent negative cannot estimate sensitivity, specificity, or base rates.

### Strongest counterexample / failure condition

A person could knowingly allow an automatic recorder to overwrite adverse material, so a content-blind storage mechanism does not prove content-blind human intent. The public NTSB source establishes that overwrite occurred and that the recorder's two-hour retention was inadequate; it does not establish every operator's motive or whether preservation duties were breached. The screen must therefore keep mechanism, human action, and intent as separate claims.


## Mixed-mechanism sensitivity attack — JFK runway incursion

**Selection rule:** This case was selected from the previous checkpoint because automatic retention loss coexisted with an unresolved human preservation path. The frozen four axes were applied without treating the NTSB's eventual probable-cause finding as an input to the H3 coding.

### Independent record

In the 13 January 2023 JFK runway-incursion investigation, the NTSB reported that both airplanes' two-hour cockpit voice recordings were overwritten. The final report states that investigators therefore relied exclusively on crew recollections documented one month later; flight-data-recorder and ADS-B data survived, but could not supply the missing content and timing of cockpit communications. The NTSB ultimately attributed the incident to distraction, concurrent tasks, loss of situational awareness, and inadequate risk controls—not record manipulation.

Sources:
- NTSB investigation page: https://www.ntsb.gov/investigations/pages/DCA23LA125.aspx
- NTSB final report AIR-24-01: https://www.ntsb.gov/investigations/AccidentReports/Reports/AIR2401.pdf
- NTSB testimony on two-hour overwrite pathways and preservation guidance: https://www.ntsb.gov/news/Testimony/pages/homendy-20231109a.aspx

### Coding with the unchanged axes before using the final causal finding

| Axis | Public observation | Classification effect |
|---|---|---|
| Missingness | Both two-hour CVRs overwrote the incident audio; FDR and ADS-B data survived | Fixed-window technical loss, but only for the communication channel most relevant to crew intent and attention |
| Direction | The missing audio is exactly what would reveal communication content, unreported conversation, and minute-by-minute attention | **DIRECTION_CENSORED:** absence of a beneficiary-aligned pattern cannot be counted as a negative observation |
| Timing | Overwrite occurred after the near collision and before investigative retrieval | Accountability-linked timing is present but is also predicted by continued two-hour recording |
| Recovery | Numerical flight and location data were recovered; cockpit semantic content was not | Partial cross-channel recovery cannot substitute for the missing claim-relevant channel |

### Decision and measurement modification

**MODIFY THE SCREEN: MIXED CASES WITH CLAIM-RELEVANT DIRECTION CENSORED MUST RETURN UNRESOLVED, NOT BENIGN OR H3-NEGATIVE.**

Before consulting the final probable-cause conclusion, the frozen axes cannot distinguish ordinary continuation/retention failure from a human choice that knowingly allowed adverse communication evidence to disappear. The correct screen output is therefore **UNRESOLVED_DIRECTION_CENSORED**.

The later NTSB finding of distraction and inadequate risk controls is consistent with a non-capture explanation and shows that the unresolved screen did not create a false positive. It does not validate sensitivity: the missing CVR prevented direct checking of the very direction variable needed to detect selective manipulation.

Operational rule added:

`if claim_relevant_channel_missing && direction_not_independently_observable => UNRESOLVED_DIRECTION_CENSORED`

Do not score this as a true negative. Direction evidence from a different channel may resolve it only if provenance and inferential linkage are independently established.

### Strongest counterexample / failure condition

A mixed case can contain genuine beneficiary-aligned preservation failure while all surviving channels look technically ordinary. Requiring observed direction from the missing channel can make H3 unfalsifiably hard to trigger; inferring direction from timing or noncooperation can instead create false positives. The screen remains triage, not an intent classifier, until held-out cases with independently reconstructed direction test both errors.

## Recovered-direction holdout — IRS Exempt Organizations data loss

**Selection and anti-leakage rule:** This case was selected from the prior checkpoint because a claim-relevant e-mail channel reported missing was later partly reconstructed by an independent Inspector General. Before consulting the recovered-content result, the frozen axes code the reported production gap, failed hard drive, reportedly recycled backups, and investigation-linked preservation dispute as **UNRESOLVED_DIRECTION_CENSORED**: timing and suspicion cannot substitute for the missing direction variable.

### Independent investigation and reveal

In February 2015 testimony, TIGTA reported that it demanded the relevant backup tapes, took possession of 744 tapes, recovered five expected Lerner mailboxes, and identified 32,774 unique e-mails pending comparison with prior productions. The later bipartisan Senate Finance Committee report states that TIGTA ultimately recovered 1,330 Lerner e-mails not previously produced to Congress, some relevant to the investigation, but could not reproduce a full 2010–2011 communication record. The same report records TIGTA's finding that it did not uncover evidence that IRS employees purposely erased a separate set of backup tapes to conceal responsive e-mails.

Primary public sources:
- TIGTA testimony in the House hearing *IRS: TIGTA Update* (26 February 2015): https://www.govinfo.gov/content/pkg/CHRG-114hhrg95249/html/CHRG-114hhrg95249.htm
- Senate Finance Committee Report 114-119, including the TIGTA investigation findings and recovered-record totals: https://www.govinfo.gov/content/pkg/CRPT-114srpt119/html/CRPT-114srpt119-pt1.htm

These are official investigation and congressional records, but not a complete raw archive. Committee interpretations are not treated as an independent substitute for the missing messages.

### Frozen-axis comparison

| Axis | Before recovered-content reveal | After independent recovery |
|---|---|---|
| Missingness | Claim-relevant production gap and failed original storage | 1,330 previously unproduced e-mails recovered, but the full communication record remained incomplete |
| Direction | Missing messages could contain controller-favoring, adverse, or neutral content; direction censored | Some recovered messages were relevant, but surviving/recoverable messages are not a demonstrated representative sample of the unrecovered population |
| Timing | Preservation dispute and investigation timing raise concern but do not identify intent | Separate tape erasure remained a serious preservation failure; TIGTA reported no evidence of purposeful concealment |
| Recovery | Initially represented as unavailable through ordinary production | Independent recovery disproved practical irrecoverability for part of the record, not for the entire missing set |

### Decision

**MODIFY: PARTIAL RECOVERY WITH UNKNOWN COVERAGE DOES NOT UNCENSOR DIRECTION.**

Add the rule:

> If recovered material is selected by an incompletely characterized survival or recovery process, it may establish existence and correct specific records, but it cannot by itself classify the unrecovered population's beneficiary direction. Score **UNRESOLVED_DIRECTION_PARTIALLY_CENSORED** until recovery coverage or selection is independently bounded.

The holdout therefore does not count as an H3 positive or benign negative. It reveals a false-resolution risk: a screen can appear to gain sensitivity merely because some records become visible, while the recovery mechanism remains missing-not-at-random and the full directional denominator is unknown.

### Strongest counterexample and boundary

A partial recovery could still contain decisive direct evidence of selective manipulation; the new rule does not discard such document-level evidence. It only blocks extrapolation from recovered items to the unrecovered population. Conversely, TIGTA's lack of evidence of purposeful erasure is meaningful negative evidence about the investigated actions, but it is not proof that all missing content was direction-neutral.

### Power-reversal result

The rule constrains both sides symmetrically. A record controller cannot cite incomplete recovery as proof that nothing adverse remains missing, and an investigator cannot cite suspicious gaps as proof of beneficiary-aligned intent. Independent recovery links, unresolved coverage, and rollback through Git history remain visible without returning reconstruction labor to the user.

## Prior-art correction — identifiability, not recovery fraction

The preceding partial-recovery rule is not a new Project Intersection result. It is a domain translation of established missing-data identification theory.

### Established baseline

- Rubin (1976) showed that the missingness process can be ignored for likelihood/Bayesian inference only under conditions including missing at random and distinct missingness parameters. DOI: https://doi.org/10.1093/biomet/63.3.581
- Mohan, Pearl, and Tian (2013) defined query-level **recoverability** using explicit missingness graphs: even some missing-not-at-random settings permit consistent recovery when graph conditions hold. https://papers.neurips.cc/paper_files/paper/2013/hash/0ff8033cf9437c213ee13937b1c4c455-Abstract.html
- Manski (2005) showed that when assumptions do not point-identify the population distribution, the warranted output is an identification region rather than an unsupported point conclusion. DOI: https://doi.org/10.1016/j.ijar.2004.10.006

### Strongest counterexample to the preceding rule

Unknown recovery *fraction* alone does not imply that a directional query is unresolved. A missingness model plus observed auxiliary variables may identify that query despite incomplete recovery. Conversely, recovering 99% of records does not identify population direction if the unrecovered 1% was selected by the direction being measured.

Therefore **recovery fraction is neither necessary nor sufficient for directional identifiability**.

### Revised decision

**NARROW / NOVELTY REJECTED FOR THE PARTIAL-RECOVERY RULE.**

Supersede the coverage-only reading with:

> Recovered records support claims about those records. Generalization to the missing population requires the beneficiary-direction query to be identifiable or recoverable under an explicit missingness model and stated auxiliary evidence. If it is only partially identified, report bounds where defensible and retain **UNRESOLVED_DIRECTION_PARTIALLY_CENSORED**; if no defensible model or bounds exist, retain **UNRESOLVED_DIRECTION_CENSORED**.

The Project-specific remainder is an operational governance mapping—requiring investigators and record controllers to expose missingness assumptions, source selection, and uncertainty symmetrically—not a new statistical theory.

### Holdout re-evaluation

The IRS/TIGTA case remains **UNRESOLVED_DIRECTION_PARTIALLY_CENSORED**, but the reason is narrower: the checked public record does not establish a missingness model or auxiliary information that identifies the beneficiary-direction distribution of unrecovered messages. The number or proportion recovered is not itself the deciding variable.

### Failure-lineage preservation

The earlier wording remains above as provenance. It correctly blocked unjustified extrapolation in the IRS case, but overgeneralized from unknown coverage to non-identification. This correction is falsified if an explicit, testable missingness model identifies the directional query from the observed and recovered data.

## IRS query-level identifiability audit

**Target estimand:** Let the target population be all claim-relevant Lerner e-mails in the investigated 2010–2011 interval that would bear on beneficiary direction. For each record, let (D=-1) mean controller-adverse, (D=0) neutral, and (D=+1) controller-favoring. The directional estimand is (	heta=P(D=+1)-P(D=-1)). Let (R=1) denote that a record survived, was recovered, and entered the observable investigative corpus.

### Minimal missingness graph

The public record supports storage/source variables affecting recovery: server or local-drive location, tape membership, overwrite or destruction, and the recovery path. Human preservation or destruction actions may also affect (R). The strategic hypothesis permits (D) itself, or accountability relevance correlated with (D), to affect those actions and therefore (R).

No checked public evidence blocks the path (D ightarrow R), establishes (D perp R) after conditioning on observed technical variables, supplies a valid instrument/shadow variable, or gives a complete sampling frame. The public summaries do not provide item-level direction counts even for all recovered records.

### Non-identification witness

Construct two full-data worlds that preserve every checked public observation:

- **World A:** every unrecovered claim-relevant message is controller-adverse.
- **World B:** every unrecovered claim-relevant message is controller-favoring.

Both worlds preserve the 744-tape recovery process, the 1,330 previously unproduced recovered e-mails, the finding that some recovered messages were relevant, the incomplete total record, and TIGTA's reported lack of evidence of purposeful tape erasure. They differ only in unobserved content. Because the missing population size and recovered directional counts are not established, the sign and magnitude of (	heta) can differ across observationally equivalent worlds.

### Bounds

With (Din[-1,1]), but without a defensible denominator for the target missing population or direction counts for the recovered corpus, the public evidence yields only the trivial worst-case interval ([-1,1]). No nontrivial directional bound was derived.

### Decision

**KILL THE IRS CASE AS A DIRECTION-CLASSIFIER CALIBRATION CASE; KEEP IT AS A NON-IDENTIFICATION AND RECOVERY-AUDIT CASE.**

- The case establishes that independent recovery can overturn a practical irrecoverability claim for specific records.
- It does not estimate H3 sensitivity, specificity, prevalence, or the direction of the unrecovered population.
- TIGTA's no-evidence finding remains negative evidence about investigated purposeful erasure, not a population-direction estimate.
- The result is robust to role reversal: neither controller nor investigator may choose the unobserved completion favorable to its position.

### Cheapest next discriminating evidence

Do not accumulate another narrative case without a usable observation frame. The next admissible holdout must expose (1) item-level recovered records or blinded direction codes, (2) a known or bounded target denominator, and (3) a characterized recovery/selection mechanism or valid auxiliary variable. Otherwise it can add recovery history but cannot calibrate direction classification.


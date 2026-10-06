# Failure Regression Index
## 실패·회귀 테스트 색인

Status: **PUBLIC FAILURE LINEAGE / GOVERNANCE + RESEARCH QUALITY CONTROL**

Purpose: preserve known failures so that later models, reviewers, maintainers, or funders do not silently recreate them. A failure entry is not necessarily evidence for the Project's scientific hypotheses. It is evidence that a specific process, implementation, or evaluation rule failed within the documented boundary.

목적: 이미 발생한 실패를 보존해 미래 모델·검토자·관리자·후원자가 같은 오류를 조용히 반복하지 못하게 한다. 실패 기록은 자동으로 Project의 과학가설을 지지하지 않는다. 해당 범위에서 특정 구현·평가·운영 규칙이 실패했다는 기록이다.

---

## F-R001 — E007 realized-history encoding error

**Class:** implementation / measurement  
**Status:** FIXED + REGRESSION TESTED  
**Source:** [E007 provenance](experiments/e007/PROVENANCE.md)

Failure: execute-first history recording used a pre-strike activity state, allowing a follower rendered inactive before response to appear to choose a strategic action.

Repair: record the realized effective follower action after strike resolution.

Boundary: utilities and the 17/72 classification-sensitive count remained unchanged; timing/history-sensitive counts changed. This does not validate real-world behavior.

Regression barrier: lethally preempted follower must be logged as `WAIT`.

---

## F-R002 — stale license/provenance state

**Class:** repository state synchronization  
**Status:** FIXED / CONTINUOUS CHECK

Failure mode: a scoped license can be decided while provenance text still states that licensing is undecided.

Repair: repository audit checks that E007 provenance cannot retain stale “license undecided” language after scoped license files exist.

Regression barrier: [public repository governance audit](.github/workflows/public-repository-audit.yml).

---

## F-R003 — autonomous-state schema / workflow drift

**Class:** continuity infrastructure  
**Status:** REPAIR APPLIED IN CURRENT MAIN / HISTORICAL FAILURE PRESERVED / LIVE CI RUN STATUS UNVERIFIED IN THIS AUDIT

Historical observed state: `AUTONOMOUS_RESEARCH_STATE.json` had moved to schema `1.1` while the public audit workflow still required `1.0`.

Historical consequence: the scheduled public governance audit at main head `b822985eec6d5f4d7342d27dfb81ced09772acfa` failed on 2026-10-06 with:

> Autonomous state schema version changed unexpectedly.

Current repository state observed in this audit: `AUTONOMOUS_RESEARCH_STATE.json` declares schema `1.1`, and `.github/workflows/public-repository-audit.yml` now explicitly requires schema `1.1`. The configuration mismatch itself is therefore repaired. This audit did not independently establish the status of the latest hosted GitHub Actions run, so it does not relabel the repair as a verified green CI execution.

Regression barrier: schema changes require an audit-rule change in the same reviewed changeset or a documented compatibility rule.

---

## F-R004 — control-plane goal inversion

**Class:** governance / process  
**Status:** REPAIR RECORDED  
**Source:** [Goal hierarchy repair](GOAL_HIERARCHY_REPAIR_2026-10-05_KO.md)

Failure mode: continuity, harness, storage, automation, or governance work can become the dominant activity and displace the underlying scientific objective.

Repair principle: the control plane may protect research integrity but may not redefine the scientific objective merely because control-plane work is easier to measure.

Regression question:

> Did this change increase evidence, falsifiability, or recovery — or did it only increase meta-documentation?

---

## F-R005 — contribution-cost / correction-labor externalization

**Class:** governance / evaluation  
**Status:** PRESERVED AS REGRESSION CHECK, NOT A NEW SCIENTIFIC METRIC  
**Source:** [Contribution-Cost Accounting Regression](CONTRIBUTION_COST_ACCOUNTING_REGRESSION.md)

Failure pattern:

1. one side benefits from repeated correction;
2. accumulated contribution is undercounted;
3. the same contributor is asked to re-explain, re-prove, reconstruct, or repair the evaluation;
4. the correction labor itself is again externalized.

Required output separation:

- already occurred failure;
- behavior to stop now;
- settlement/accounting if future legitimate authority exists.

Boundary: this does not establish a legal debt or a specific compensation amount.

---

## F-R006 — novelty by renaming or combination

**Class:** research novelty / attribution  
**Status:** MULTIPLE BROAD CLAIMS NARROWED OR KILLED  
**Sources:** [Prior Art & Attribution](PRIOR_ART_AND_ATTRIBUTION.md), [Core/Gaps Crosswalk](CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md)

Forbidden inference:

`RENAMING == DISCOVERY`  
`COMBINATION == NOVELTY`  
`NO_CITATION_FOUND == NO_PRIOR_ART`

Repair: established overlap is attributed to prior work; only the residual incremental claim remains a Project candidate.

Regression barrier: prior-art gate before promotion of new constructs.

---

## F-R007 — evidence laundering across lineage

**Class:** epistemic / validation  
**Status:** ACTIVE GUARD

Failure mode: project-authored rerun, same-model agreement, AI-generated critique, or green CI is relabeled as independent replication.

Forbidden inference:

`SELF_REPORT == INDEPENDENT_VERIFICATION`  
`PROJECT_RERUN == THIRD_PARTY_RERUN`  
`EXECUTABLE == EMPIRICAL_VALIDATION`

Repair: keep evidence classes separate in [Research Status Policy](RESEARCH_STATUS_POLICY.md) and [Public Evidence Index](PUBLIC_EVIDENCE_INDEX.md).

---

## F-R008 — unobserved converted to false/zero/consent

**Class:** epistemic / missing-data  
**Status:** ACTIVE GUARD

Failure mode: missing observation is silently converted into absence, zero burden, no harm, falsehood, or consent.

Required representation: use `UNOBSERVED`, `UNRESOLVED`, or bounded inference where appropriate.

Boundary: open-world caution does not license arbitrary positive claims. Unknown remains unknown unless independently resolved.

---

## F-R009 — founder reconstruction burden

**Class:** continuity / human burden  
**Status:** ACTIVE GUARD

Failure mode: future executors repeatedly ask the founder to reconstruct context that the repository or receiving system already controls.

Repair: [Autonomous Research Continuity](AUTONOMOUS_RESEARCH_LOOP.md) must provide a public recovery sequence and state pointer.

Regression barrier:

`N_user_restarts = 0` as an operational aspiration for already-preserved context.

Missing private evidence may remain unresolved; it must not be fabricated.

---

## F-R010 — practical exit converted into research dependency

**Class:** governance  
**Status:** ACTIVE GUARD

Failure mode: the project becomes dependent on continued unpaid correction or makes recognition of past contribution conditional on future participation.

Repair:

`past contribution accounting != future labor contract`

Exit may stop future duties. It does not rewrite provenance.

---

## F-R011 — role reversal as identity erasure

**Class:** governance reasoning  
**Status:** ACTIVE GUARD

Failure mode: “treat both sides equally” erases real differences in capability, responsibility, causal reach, harm magnitude, reversibility, or legal authority.

Required rule:

`ROLE_REVERSAL != IDENTITY_ERASURE`

Role reversal tests the rule from the affected position while preserving real causal differences.

---

## F-R012 — repository growth mistaken for research progress

**Class:** project management / epistemic  
**Status:** ACTIVE GUARD

Failure mode: file count, document length, automation count, or semantic organization is treated as scientific progress.

Repair: progress requires at least one of:

- a claim killed or materially narrowed;
- a discriminating test;
- stronger external evidence;
- lower replication cost;
- repaired provenance/status contradiction;
- independently useful negative result.

Documentation-only growth is lowest priority.

---

## Mandatory regression questions

Before any material repository mutation:

1. What concrete failure or uncertainty does this change reduce?
2. Does it change scientific evidence, or only the interface?
3. Could the same result be achieved with a smaller reversible change?
4. Who gains capability or authority if this repeats?
5. Who pays explanation, proof, correction, monitoring, or recovery cost?
6. Does the affected party retain raw evidence access, contestability, exit, and rollback?
7. Is prior contribution/provenance preserved?
8. Could this be prior art under another name?
9. What observation would make us KILL or revert this change?
10. Would the same rule be accepted after role reversal?

A “no malice” explanation is not a substitute for these checks.

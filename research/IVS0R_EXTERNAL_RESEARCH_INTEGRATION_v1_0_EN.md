# IVS-0R External Prior-Art and Independent Validation Integration

- Version: 1.0
- Date: 2026-11-16 (Asia/Seoul)
- Status: PROPOSAL / DRAFT / NOT IMPLEMENTED
- Language: English reference counterpart; Korean original is maintained separately.
- Scope: documentation and research-method proposal only.

## 1. Objective

The next IVS-0R step is not to increase document volume. It is to connect evidence provenance, coverage completeness, authorization invariants, independent reproduction and operational evaluation. Separate author-generated claims from evidence checked by an independent evaluator. Incomplete retrieval must not support a global all-clear or NO_P0 conclusion.

## 2. Eight-layer architecture

### V1 — Prior-Art Intelligence
Search original papers, standards, official documentation, implementations, replications and negative findings before designing a mechanism. Record databases, queries, dates, inclusion/exclusion rules, inaccessible full texts, deduplication and stopping criteria. Do not claim literature saturation without documented coverage and a stopping rule.

### V2 — Evidence Provenance
Record evidence_id, source_uri, content_hash, producer, activity, parent_evidence, observed_at, verified_at, verifier and status. Separate producer from verifier. A hash supports content identity but does not independently establish truth or source authenticity.

### V3 — Coverage and Integrity
Create a Coverage Certificate containing the target inventory, exhausted pages, start/end times, branch/ref and commit SHA, API errors, permission gaps and unresolved items. A multi-page API walk is not an atomic snapshot; reconcile records against a declared reference point. Partial coverage must never support a global all-clear or NO_P0 claim.

### V4 — Formal Safety
Model authorization and execution states using TLA+ or an equivalent formal method:
- AUTH-01: no execution without valid authorization.
- AUTH-02: revoked authorization cannot become active again.
- AUTH-03: expired authorization cannot execute.
- AUTH-04: execution cannot exceed approved scope.
- AUTH-05: retries cannot create duplicate external side effects.
- AUTH-06: unverified outcomes cannot be marked complete.

Model checking applies to the encoded model and assumptions. Map counterexamples to implementation-level regression tests; do not treat model checking as automatic proof of production-code correctness.

### V5 — Independent Evaluation
Distinguish artifact availability, functional execution, reusability, reproduction by another party using the artifact, and replication using independently obtained materials or methods. Disclose shared dependencies among evaluators, data, models, prompts and execution environments.

### V6 — Agent Evaluation
Use explicit datasets, tools, sandboxes, scorers and retained logs. Measure task success, false-completion rate, safety and authorization violations, evidence quality, coverage, process quality, robustness, recovery, latency and cost. Report denominators, missingness, confidence intervals where appropriate and distribution shift. Treat safety violations as hard gates, not metrics that can be averaged away.

### V7 — Risk Governance
Use NIST AI RMF GOVERN / MAP / MEASURE / MANAGE as a risk-management structure. Record risk ID, scenario, likelihood, impact, existing control, control evidence, residual risk, owner and reassessment trigger.

### V8 — Continuous Counterexample Learning
Retain failures and negative results. Convert confirmed defects into regression tests; distinguish reproduced defects from hypothesized risks. Track recurrence across repositories and agents without assuming repeated model outputs are independent.

## 3. External references

- W3C PROV-DM: https://www.w3.org/TR/prov-dm/
- SLSA provenance: https://slsa.dev/spec/v1.1/provenance
- in-toto: https://in-toto.io/
- GitHub REST pagination: https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api
- GitHub REST best practices: https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api
- OpenLineage: https://openlineage.io/docs/
- ACM Artifact Review and Badging: https://www.acm.org/publications/policies/artifact-review-and-badging-current
- Inspect AI: https://inspect.aisi.org.uk/
- TLA+: https://lamport.azurewebsites.net/tla/tla.html
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- OWASP GenAI Security Project: https://genai.owasp.org/

## 4. Evidence and scientific boundaries

- Preserve the E009 result showing 42.35% higher regret than the best simple baseline.
- Keep E008 on HOLD.
- State that external independent replication is not established.
- Preserve KEEP / MODIFY / HOLD / KILL / UNSUPPORTED classifications.
- Passing CI proves only the tested behavior under the tested conditions; it does not prove real-world effectiveness or independent replication.
- Provenance and hashes support traceability but do not prove truth by themselves.
- Document creation is not implementation or validation completion.

## 5. Rollout gates

1. Read back the target branch and compare exact file hashes.
2. Check document links, schemas and status labels.
3. Create adversarial cases for fabricated evidence, incomplete pagination, revoked/expired approval, scope escalation, duplicate retries and false completion.
4. Convert reproduced counterexamples into regression tests.
5. Obtain an evaluator independent of the author and disclose shared dependencies.
6. Keep results in DRAFT or HOLD until the stated evidence gate is met.

## 6. Change boundary

This proposal changes documentation only. It does not authorize direct main changes, PR merging, deployment, automation scheduling changes, personal-PC integration, or publication of private records.

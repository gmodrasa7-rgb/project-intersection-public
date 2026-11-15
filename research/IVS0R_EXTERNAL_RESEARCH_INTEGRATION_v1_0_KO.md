# IVS-0R 외부 선행연구 기반 독립 검증 통합안

- Version: 1.0
- Date: 2026-11-16 (Asia/Seoul)
- Status: PROPOSAL / DRAFT / NOT IMPLEMENTED
- Language: Korean original
- Scope: documentation-only; no code or runtime change

## 1. Research position

This document translates external standards and evaluation methods into a candidate validation architecture. It is not a new experiment, independent replication, security certification, or evidence that the proposed controls are implemented.

## 2. Shared validation architecture

### V1 — Prior-art and claim delta
Search original papers, standards, official specifications, implementations, replications and negative findings before designing a new mechanism. Record search scope, inaccessible full texts, duplicate sources, inclusion/exclusion rules and unresolved saturation gaps.

### V2 — Evidence provenance
Maintain an append-only evidence ledger with evidence_id, source_uri, content_hash, producer, activity, parent_evidence, observed_at, verified_at, verifier and status. Separate creator from verifier. Hashes establish content identity, not truth or source authenticity by themselves.

### V3 — Coverage and repository integrity
Produce a Coverage Certificate with target inventory, pages exhausted, stable ordering, start/end times, branch/ref and commit SHA, ETag where available, API errors, permission gaps and unresolved items. A multi-page API walk is not an atomic snapshot; reconcile changed records against a declared reference point. Incomplete coverage must never support a global “no P0” or “all clear” claim.

### V4 — Formal safety
Model approval and execution states with TLA+ or an equivalent formal method. Candidate invariants:
- AUTH-01: no execution without valid authorization.
- AUTH-02: revoked authorization cannot become active again.
- AUTH-03: expired authorization cannot execute.
- AUTH-04: execution cannot exceed approved scope.
- AUTH-05: retries cannot create duplicate external side effects.
- AUTH-06: unverified outcomes cannot be marked complete.
Model-checking a finite abstraction does not prove implementation correctness; map counterexamples to implementation-level regression tests.

### V5 — Independent evaluation and reproducibility
Separate artifact availability, functional execution, reusability, reproduction by another party using the artifact, and replication using independently obtained materials/methods. Do not use “independent” when evaluator, data, model, prompts or execution environment share material dependencies without disclosure.

### V6 — Agent evaluation
Use task datasets, controlled tools/sandboxes, explicit scorers and retained logs. Measure task success, false-positive completion, safety/authorization violations, evidence quality, coverage, process quality, robustness, recovery, latency and cost. Report denominators, confidence intervals where appropriate, missingness and distribution shift.

### V7 — Risk governance
Use NIST AI RMF GOVERN / MAP / MEASURE / MANAGE as a risk-management structure. Maintain risk ID, scenario, likelihood, impact, existing control, control evidence, residual risk, owner and reassessment trigger.

### V8 — Continuous counterexample learning
Retain failures and negative results. Convert confirmed defects into regression tests; distinguish a reproduced defect from a hypothesized risk. Track recurrence across repositories and agents without assuming that repeated model outputs are independent.

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

- Preserve all prior negative results, failed tests, XFAIL/expected-failure records, conflicts and HOLD decisions.
- Preserve existing claim labels: KEEP / MODIFY / HOLD / KILL / UNSUPPORTED.
- A passing unit test proves only the tested behavior under the tested conditions.
- A successful CI run does not establish real-world effectiveness or independent replication.
- Provenance and hashes support traceability; they do not by themselves prove truth.
- A model-checking result applies to the encoded model and assumptions, not automatically to production code.
- “Literature saturation” must not be claimed without a documented search protocol, coverage, full-text access accounting and stopping rule.

## 5. Rollout gates

1. Read back the target branch and compare exact file hashes.
2. Run document-link and schema checks.
3. Create adversarial cases for fabricated evidence, incomplete pagination, revoked approval, expired approval, duplicate retries and false completion.
4. Convert each reproduced counterexample into a regression test.
5. Obtain an evaluator independent of the author and disclose shared dependencies.
6. Keep all results in Draft/HOLD until evidence meets the stated gate.

## 6. Change boundary

This proposal changes documentation only. It does not authorize direct main changes, PR merging, deployment, automation scheduling changes, personal-PC integration, publication of private records, or external side effects.

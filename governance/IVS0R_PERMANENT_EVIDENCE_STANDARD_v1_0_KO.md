# IVS-0R Permanent Evidence & Synchronization Standard

- Date: 2026-11-17 (KST)
- Status: PROPOSED_FOR_REVIEW / NOT_MERGED / NOT_OPERATIONALLY_ENFORCED
- Scope: apply the shared evidence, provenance, reproducibility, synchronization, and least-privilege principles while preserving this repository's domain-specific canonical authority and privacy boundary.

## Mandatory distinctions

- OBSERVED / CALCULATED / INFERRED / HYPOTHESIS / UNKNOWN / CONFLICT are distinct epistemic states.
- DOCUMENTED / EXECUTABLE / REPRODUCED / INDEPENDENTLY_REPLICATED are distinct evidence states.
- A file write, hash match, signature, CI pass, ACK, or self-report proves only its own narrow claim; none alone establishes scientific truth or durable storage.
- Preserve negative results, counterevidence, unresolved states, original attribution, and historical provenance. Never silently rewrite failure as success.

## Provenance and canonical versions

- Record source identity, canonical path, commit/ref, content hash, retrieval date, license/access boundary, and derivation.
- Use PROV-O-style Entity, Activity, and Agent relations; validate temporal and logical consistency.
- Distinguish event_at, valid_at, and recorded_at where relevant; unknown times remain UNKNOWN.
- Use monotonic canonical versions with previous_version, content_hash, created_at, review_due, and supersedes. Detect rollback, stale snapshots, and mixed-version bundles.
- Use RO-Crate selectively for distributable research packages when packaging adds value and privacy/licensing conditions permit. Do not force it onto every transient note or sensitive record.

## Independence and validation

Separate Producer, Recorder, Independent Evaluator, Adversarial Tester, and Decision Authority where feasible. Track independence across person, data, execution, infrastructure/fault-domain, and adjudication. Same-model or same-data role separation is not automatically independent replication. Unknown dimensions cannot be silently treated as verified.

## Synchronization and recovery

Treat Library, memory, and repository updates as distributed writes, not one atomic transaction. Use PREPARE -> APPLY -> RECONCILE; stable change IDs; idempotent retries; explicit SYNC_FAILED on partial failure. Mark SYNCED only after re-reading target versions and hashes. Do not claim automatic sync where no actual integration exists.

## GitHub security

Use least-privilege workflow permissions; pin third-party Actions to reviewed full commit SHAs; separate validation from approval/merge; inspect actual Rulesets and required checks instead of inferring them from documentation or issue text. Draft PR is a proposal, not mainline adoption or operational proof. Main edits, merges, ruleset changes, public release, and destructive actions require separate authorization.

## Nostr evidence contract (where applicable)

Keep publish attempt, relay identity, ACK, separate read-back, restart survival, operator identity, infrastructure/fault-domain lineage, and independent custodian verification separate. ACK is not durable-storage proof. Preserve per-relay observations even when event payloads are deduplicated.

## Prior-art and privacy

Search primary literature, implementations, standards, negative results, and counterexamples before proposing novelty. Preserve search strings, databases, dates, citation chasing, deduplication, exclusions, and benchmark recall. Relative Recall is only recall against a defined benchmark, not proof of total literature completeness. AI search/screening/extraction remains assistive and human-accountable.

Minimize sensitive data, respect access rights and retention limits, and never copy private family, health, financial, or dialogue records into public artifacts. Auditability does not override authorized privacy deletion or retention constraints.

## Required regression tests

1. stale-version rollback rejected;
2. hash/content mismatch rejected;
3. missing provenance blocks promotion;
4. producer cannot self-certify independence;
5. partial synchronization remains incomplete;
6. duplicate event/change is idempotent;
7. temporal provenance contradiction is flagged;
8. ACK without read-back is not durable-storage proof;
9. shared operator/fault domain is not counted as independent custody;
10. unauthorized workflow or revoked approval blocks effect;
11. negative result survives summary regeneration;
12. private material is excluded from public export.

These are specifications, not passing test results. Report actual changed files, commits, tests, re-read verification, independence status, and unresolved items separately. Never promote beyond the evidence actually obtained.

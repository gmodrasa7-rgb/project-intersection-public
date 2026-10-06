# GitHub ↔ IVS0R_LOCAL Atomic Handoff Protocol v1
## GitHub ↔ 로컬 원자적 중간저장 프로토콜 v1

Status: **ACTIVE OPERATIONAL PROTOCOL / NOT A NEW RESEARCH CLAIM**

Purpose: prevent either the public GitHub repository, the local continuity store, or the current AI from silently promoting its own partial state into the final state.

This layer is intentionally thin. It is a transaction / provenance layer, **not a third canonical research archive**.

## Roles

- `/IVS0R_LOCAL/raw|state` — private/local continuity and source material under the user's actual storage authority.
- `/IVS0R_LOCAL/staging` — unpromoted handoff candidates.
- `/IVS0R_LOCAL/quarantine` — failed, conflicting, sensitive, or unverifiable candidates.
- `/IVS0R_LOCAL/receipts` — compact success/failure receipts after verification.
- public GitHub — public evidence, public provenance, reproducible artifacts and public continuity pointers.

Neither side is a superior truth source for every domain.

## State machine

`DRAFT_LOCAL`
→ `STAGED`
→ `VALIDATED`
→ `PUBLIC_READY`
→ `PUSHED`
→ `READ_BACK_VERIFIED`
→ `COMMITTED_TO_LOCAL_STATE`

Failure branches:

`REJECTED` / `QUARANTINED` / `ROLLBACK_REQUIRED`

A state may not be skipped merely because the writer and evaluator are the same process.

## Completion invariant

`PUBLIC_PUSH != SUCCESS`

For a local → public handoff, completion requires:

`SOURCE_HASH_KNOWN`
+ `VALIDATION_PASS`
+ `PUBLIC_WRITE_CONFIRMED`
+ `PUBLIC_READ_BACK_MATCH`
+ `LOCAL_RECEIPT_PERSISTED`

For a public → local handoff, completion requires:

`PUBLIC_SOURCE_ID_KNOWN`
+ `PUBLIC_READ_BACK`
+ `LOCAL_STAGE_WRITE`
+ `LOCAL_VALIDATION_PASS`
+ `LOCAL_CANONICAL_UPDATE`
+ `LOCAL_READ_BACK_MATCH`

## Mandatory receipt fields

Each transaction records at least:

- `change_id`
- `direction`
- `source_identity`
- `source_hash`
- `target_identity`
- `sensitivity`
- `publishability`
- `evidence_class`
- `prior_art_checked` when a scientific/novelty claim is affected
- `validation`
- `github_commit_sha` / `github_blob_sha` where applicable
- `read_back_hash`
- `local_library_path` / version where applicable
- `rollback_target`
- `status`
- `supersedes`
- `failure_reason` when not successful

Unmeasured fields remain `UNRESOLVED`; they are not coerced to zero/false.

## Public-boundary gate

Before any local → GitHub handoff:

1. classify privacy / sensitivity;
2. remove credentials, health/family/bank/private-chat material unless explicitly and legitimately intended for publication;
3. preserve source attribution and license/rights boundaries;
4. separate a public distillation from private raw material;
5. never treat the existence of a local note as permission to publish it.

`LOCAL_ACCESS != PUBLICATION_AUTHORITY`

## Role-reversal gate

Before promotion ask:

- If GitHub were wrong, can Local independently detect and recover?
- If Local were wrong, can GitHub evidence and history contradict it?
- Does either side gain the power to erase the other's failure lineage?
- Does the handoff increase the user's reconstruction burden?
- Would the same promotion rule be accepted if writer/evaluator roles were swapped?

If a conflict cannot be resolved from source evidence:

`CONFLICT -> QUARANTINED / UNRESOLVED`

not silent overwrite.

## Anti-duplication rule

Staging is temporary. After a successful transaction, retain only the minimum receipt needed to reconstruct:

`change_id + source hash + target hash/commit + validation result + timestamp + rollback pointer`

Do not keep a third full copy merely because the handoff succeeded.

## Failure behavior

On validation, permission, network, CI, read-back, hash, or schema mismatch:

- keep the previous canonical state unchanged;
- persist the failed receipt if possible;
- quarantine the candidate when its provenance is still useful;
- never report completion.

## Authority boundary

This protocol does not create:
- access to the user's physical PC;
- authority over third-party data;
- authority to publish private material;
- a right for Local or GitHub to resist an authorized deletion;
- scientific validation merely because hashes and CI pass.

Integrity proves state identity, not theory truth.

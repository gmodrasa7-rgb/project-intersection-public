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


---

## Library-backed context restoration v0.1 — Original 1 English (2026-10-14)

**REVERSIBLE OPERATIONAL AUDIT; NO SCIENTIFIC CLAIM OR GENERATION PROMOTION.** Direct inspection confirms that ChatGPT Library /IVS0R_LOCAL/ contains existing G10 manifest, state, continuity capsule and context map. Research-canonical data belongs to the private gmodrasa7-rgb/rgbm-lab repository (DOMAIN_MANIFEST.json declares canonical=true); the public repository is the evidence interface; Library is a continuity and failure-lineage store, not model weights or native context-window extension.

A dated Korean recovery guide was saved and read back at /IVS0R_LOCAL/RECOVERY/PI_CONTEXT_RECOVERY_GUIDE_KO.md. Attempts to save the separate JSON checkpoint and Python gate to Library failed with container_session_expired. Such failed uploads are NOT counted as completed until a successful write and readback occurs.

The new original public offline tool tools/pi_library_context_trust_gate.py checks supplied Git head staleness, source roles, missingness and a small question-specific document route. **It does not read GitHub or Library itself, verify a caller-supplied head, read Research OS, access model internals, or improve native model capacity.** GitHub CI covers deterministic synthetic regression only. For an actual decision, fetch current SHA with authorized tools before relying on the result.

Observed public HEAD 2026-10-14: 5e3d871820cc3a238b8cb0a80da92b294128735d; old public AUTONOMOUS_RESEARCH_STATE.json stored: 9de1f28ee824546bebfbbb13528136c9f31b7e79. The stale pointer is not evidence of malicious mutation. G10 historical promotion provenance remains UNRESOLVED, and older Library files are not overwritten.

Methodological predecessors: MemGPT (Packer et al., https://arxiv.org/abs/2310.08560), Lost in the Middle (Liu et al., https://arxiv.org/abs/2307.03172), RAPTOR (Sarthi et al., https://arxiv.org/abs/2401.18059), LongMemEval (Maharana et al., https://arxiv.org/abs/2410.10813). No external source code, data, figures or substantial text copied; founding research requirements are credited separately from AI-assisted implementation.

## Library 기반 컨텍스트 복구 v0.1 — 원본2 한국어

**연구 정본 승격 아님·가역적 운영검사.** 실제 ChatGPT Library /IVS0R_LOCAL/의 G10 파일을 확인했다. 비공개 rgbm-lab은 과학 정본, 공개 GitHub는 검증 공개자료, Library는 연속성 저장소다. Library로 컨텍스트의 물리적 한도나 모델의 가중치가 늘지 않는다.

내부 복원 안내서 1건은 실제 저장·재조회했다. JSON 부트 상태와 Python 검사기는 container_session_expired 오류로 Library 저장에 실패해 성공으로 계산하지 않는다. 공개된 도구는 이전과 현재의 SHA를 **전달받아** 비교하며 스스로 최신 상태를 조회·인증할 수 없다. 2026-10-14 공개 HEAD와 과거 공개 상태 JSON의 내장 SHA 차이는 시점이 다른 포인터의 불일치이지 조작의 증거가 아니다. 이전 G10 파일·실패계보는 불변이다. 외부 선행연구자 권리를 보존하고 창시자 문제설정과 AI 구현 기여를 구별한다.

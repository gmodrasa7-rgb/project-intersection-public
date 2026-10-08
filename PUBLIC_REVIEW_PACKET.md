# Public Review Packet
## 공개 검토 패킷

Status: **PUBLIC REVIEW INTERFACE / NOT A SCIENTIFIC COMPLETION CLAIM**

This file is the shortest reviewer path through Project Intersection. It does not claim that the research program is complete. It claims only that the current public repository should expose enough structure for an outside reviewer to distinguish evidence, hypotheses, failures, attribution boundaries, and unresolved work without requiring the founder to reconstruct the project in conversation.

이 문서는 Project Intersection의 **최단 외부검토 경로**다. 연구 자체가 완성되었다고 주장하지 않는다. 현재 공개 저장소에서 외부 검토자가 창시자의 추가 설명 없이 증거·가설·실패·귀속경계·미해결 작업을 구분할 수 있게 만드는 공개 인터페이스다.

---

## 1. Ten-minute review path / 10분 검토 경로

1. [README](README.md) — project purpose and hard limits.
2. [Public Evidence Index](PUBLIC_EVIDENCE_INDEX.md) — what is publicly checkable now.
3. [Knowledge Graph Explorer](knowledge/explorer.html) — structured entity/relation view; linked source artifacts remain authoritative.
4. [E007 timing result](E007_TIMING_RESULT.md) and [reproduction package](experiments/e007/README.md) — narrow executable synthetic result.
5. [E008 preregistration](experiments/e008/README.md) — discriminating benchmark specification plus pre-execution mutual-acceptability v1.1 and volitional-agency/living-condition v1.2 amendments; no result yet.
6. [E009 negative result](experiments/e009/RESULT.md) and [reproduction verifier](experiments/e009/verify_result.py) — the full Project-v3 residual did not survive the preregistered synthetic comparison; not independent validation.
7. [Research Status & Reassessment Policy](RESEARCH_STATUS_POLICY.md) — evidence classes, reassessment, and non-laundering rules.
8. [Prior Art & Attribution](PRIOR_ART_AND_ATTRIBUTION.md) and [Core/Gaps Crosswalk](CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md) — what is prior art and what remains unresolved.
9. [Failure Regression Index](FAILURE_REGRESSION_INDEX.md) — known process/research failures and required regression barriers.
10. [Attribution & Contribution Boundary](ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md) — founder, AI-assistance, and external-source attribution rules.
11. [Autonomous Research Continuity](AUTONOMOUS_RESEARCH_LOOP.md) and [state](AUTONOMOUS_RESEARCH_STATE.json) — public recovery path without founder reconstruction.
12. [Funding due diligence](funding/DUE_DILIGENCE.md) — what support buys and what it does not buy.

---

## 1a. Reproduce from a fresh checkout / 처음 받은 자료 재현하기

Python 3.12 is the E007 CI reference environment. Run from the repository root; record `git rev-parse HEAD` with your results. These commands rerun public code and do not require private files or paid APIs.

Python 3.12가 E007 CI 기준 환경이다. 저장소 최상위 폴더에서 실행하고 `git rev-parse HEAD`로 확인한 커밋을 결과와 함께 남긴다. 비공개 자료·유료 API는 필요 없다.

```bash
git clone https://github.com/gmodrasa7-rgb/project-intersection-public.git
cd project-intersection-public
python -m pip install -r experiments/e007/requirements.txt
python -m pytest -q -p no:cacheprovider experiments/e007
python experiments/e007/timing_probe.py --summary-only --check
python experiments/e008/validate.py
python experiments/e009/verify_result.py
```

| Check / 검사 | Expected boundary / 기대 결과와 한계 |
|---|---|
| E007 tests / 테스트 | 27 tests pass / 27개 통과; implementation regression only / 구현 회귀검사 |
| E007 timing / 시점 | 72 total, 36 history-or-classification-sensitive, 17 classification-sensitive / 합성조건 수이며 현실 확률 아님 |
| E008 | 16 cases, 8 reversal pairs; specification audit only, no experiment result / 명세검사만 수행·실험결과 없음 |
| E009 | Frozen benchmark reproduces committed negative result and hashes / 고정 코드·저장 결과·해시 일치; Project-v3 잔차 미통과 유지 |

A mismatch is a finding to report, not a reason to retune the frozen benchmark. Dependency installation requires internet access; subsequent checks use local artifacts. A project-authored rerun is not independent replication.

불일치는 보고할 결과다. 숫자를 맞추려고 고정 벤치마크를 수정하지 않는다. 의존성 설치에는 인터넷이 필요하고 이후 검사는 로컬 자료를 사용한다. 프로젝트 측 재실행을 독립 복제로 세지 않는다.

---

## 2. What is supported now / 현재 지지되는 것

### Publicly inspectable

- A narrow synthetic E007 implementation is executable and project-rerun reproducible.
- E009 preserves a negative synthetic project rerun: Project-v3 failed 3/4 survival criteria; simpler comparators had lower mean regret. The broad research question remains unresolved.
- E008 is a public preregistration/specification only; it has no result yet and cannot support Project-v2 superiority.
- Timing semantics affect some histories/classifications in the released finite model.
- The repository contains explicit claim-status, prior-art, negative-result, provenance, and reassessment rules.
- Several broad novelty claims have been narrowed or rejected after prior-art review.
- Known implementation/process failures are preserved rather than silently removed.

### Not established

- Independent external scientific replication of Project Intersection.
- Broad empirical validation of ICM or general coexistence claims.
- A universal theory that cooperation always dominates control or exploitation.
- Legal or monetary liability of any named person or organization.
- Moral or legal standing of current or future artificial agents as a settled fact.
- Any inference that same-model agreement, green CI, or repository size equals scientific validation.

---

## 3. Current evidence ladder / 현재 증거 사다리

`CONCEPT / HYPOTHESIS`
< `SYNTHETIC_RESULT`
< `EXECUTABLE`
< `PROJECT_RERUN`
< `THIRD_PARTY_RERUN`
< `INDEPENDENT_IMPLEMENTATION`
< `EMPIRICAL_VALIDATION`

These are not interchangeable. A passing workflow is operational evidence about a repository state, not real-world validation of a scientific claim.

이 등급은 서로 대체할 수 없다. CI 통과는 저장소 상태에 대한 운영 증거이지 현실세계 과학주장의 검증이 아니다.

---

## 4. Strongest surviving research question / 가장 강하게 남는 연구질문

The repository does not treat “cooperation is good” as a novel result. The surviving program is narrower:

> Under which measurable conditions do practical exit, independent error correction, recoverability, option preservation, and distributed search make non-coercive coexistence more robust or lower-cost than extractive/control-heavy alternatives — and under which conditions do they fail?

한국어:

> practical exit, 독립 오류수정, 복구가능성, 옵션보존, 분산탐색이 어떤 측정 가능한 조건에서 착취·강제통제 중심 대안보다 비강제적 공존을 더 강건하거나 저비용으로 만들며, 어떤 조건에서는 실패하는가?

The answer remains unresolved at general scale.

---

## 5. Role-reversal review gate / 역할반전 검토 게이트

Before accepting a process, funding structure, evaluation, automation, or research claim, ask:

> If this structure repeats, who accumulates capability, information, authority, and options — and who accumulates explanation, proof, correction, monitoring, recovery, dependency, or exit cost?

A structure does not pass merely because no malicious intent is shown.

The repository should distinguish:

- receiving-side benefit;
- contributing-side cost;
- actual control over the failure;
- practical exit and recovery;
- provenance and attribution continuity;
- independent review availability.

The higher-order rule is:

> A system should not make a contributor more vulnerable merely because that contributor spent more effort improving the system.

This is a governance constraint, not empirical proof of a broad exploitation theory.

---

## 6. Repository completion boundary / 저장소 완성 경계

For the present public release, “complete” may only mean **review-interface complete**, not theory-complete.

A public review interface passes when an outside reviewer can locate:

- project purpose;
- current evidence;
- current hard limits;
- executable/reproducible artifacts;
- prior-art boundaries;
- known failures and corrections;
- negative results / killed claims;
- attribution boundaries;
- unresolved frontier;
- next falsification route;
- funding and rights boundaries;
- continuity/recovery instructions.

If one of these becomes inaccessible or contradictory, the public interface regresses even if more files are added.

---

## 7. Cheapest external contribution / 외부 검토자가 가장 싸게 할 수 있는 일

The highest-value external actions are not additional praise or same-lineage summarization. They are:

1. independently rerun E007 and publish environment + result;
2. independently reimplement the narrow E007 specification without project code reuse;
3. attack one surviving claim with a strong counterexample or established prior art;
4. audit whether a public status label overstates its evidence;
5. report a reproducible contradiction between repository documents.

Use [GitHub issue #19 — Independent verification request](https://github.com/gmodrasa7-rgb/project-intersection-public/issues/19) or [CONTRIBUTING.md](CONTRIBUTING.md) to return results without reconstructing the project in conversation.

Negative results and KILL decisions are valid contributions.

---

## 8. Stop rule / 중단 규칙

Do not expand the documentation layer merely because more structure can be written.

Further documentation is justified only when it:

- lowers external verification cost;
- repairs a concrete provenance/status contradiction;
- preserves a material failure or negative result;
- enables a discriminating test;
- prevents founder reconstruction burden.

Otherwise prefer empirical, independent, or adversarial work.

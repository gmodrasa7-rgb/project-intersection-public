# Funding & Research Partnerships
## Project Intersection 외부 자금·연구 파트너십

Status date / 상태 기준일: **2026-10-04**

> **This page describes research funding, sponsorship, and research-partnership needs. Planned or requested funding is never counted as secured funding.**
>
> **이 문서는 연구비·후원·연구 파트너십의 필요와 산출물을 설명한다. 계획·요청 단계의 자금은 확보자금으로 계상하지 않는다.**

---

## Original 1 — English Canonical

### One-sentence case for funding

Project Intersection is an independent, falsification-first research program testing when power, incentives, timing, practical exit, recovery capacity, and independent error-correction make coexistence more robust than exploitative local optimization—and publishing the failures and boundary conditions when that thesis does not hold.

### Why fund this researcher / project

The core contribution is not high-volume code production. It is a repeated research loop of:

**problem discovery → anomaly detection → decomposition → counterexample search → natural-language experiment design → claim narrowing or rejection → final judgment**

English writing, coding, CI, and implementation are AI-assisted. The human contribution is concentrated in problem framing, structural comparison, edge-case discovery, research direction, and final evaluation.

The fundable output is therefore a combination of:

- narrow falsifiable claims;
- reviewer-safe benchmark packages;
- explicit failure and correction lineage;
- public evidence/provenance interfaces;
- reusable tests for power asymmetry, exit, evaluator capture, irreversibility, and recovery.

### Evidence already public

Start with [PUBLIC_EVIDENCE_INDEX.md](../PUBLIC_EVIDENCE_INDEX.md).

The strongest currently public computational artifact is [E007 timing sensitivity](../E007_TIMING_RESULT.md): 27 tests pass in the released package; 17/72 selected synthetic cases change classification under the tested timing semantics. The result is deliberately scoped: it is synthetic, implementation-dependent, and not independent scientific replication.

### Current funding state

- **Secured external funding: 0.**
- GitHub Sponsors application/setup was submitted and was still under GitHub review at the last verified account check on **2026-10-02**; this is not counted as funding.
- A **USD 5,000 / 30-day** Manifund bridge package has been prepared as a draft / ready-to-publish funding request, not as an awarded grant.
- A **KRW 18,000,000 / 90-day** pilot package has been prepared as a follow-on plan, not as secured funding.

### Due diligence boundary

For the current funding boundaries, evidence requirements, IP/licensing status, and sponsor-independence rules, see [DUE_DILIGENCE.md](DUE_DILIGENCE.md).

### What funding buys

Funding is intended to convert private research labor and partially public research state into a smaller set of externally checkable artifacts.

Priority spending categories:

1. protected research and engineering time;
2. API / compute / tooling;
3. independent adversarial review or attack where available;
4. documentation, packaging, and public reproduction infrastructure.

A funder does **not** buy a predetermined KEEP result. A funded claim can end as MODIFY, KILL, HOLD, NARROWED, or UNSUPPORTED.

### Preferred funding sequence

**Stage 1 — 30-day bridge, USD 5,000**

Goal: produce a compact external-review package and reduce the largest verification bottlenecks.

See [30_DAY_BRIDGE.md](30_DAY_BRIDGE.md).

**Stage 2 — 90-day pilot, KRW 18,000,000**

Goal: move from one public computational example plus a broad research map toward a small portfolio of reviewer-safe benchmarks, stronger external challenge, and evidence/claim lineage that an outside evaluator can audit without relying on private conversation history.

See [90_DAY_PILOT.md](90_DAY_PILOT.md).

### What success means

Success is not “the theory survived.”

Success means the funding period leaves behind artifacts that make the project easier to falsify, reproduce, audit, compare with prior work, and either continue or rationally stop.

---

## 원문2 — 한국어 대응본

### 한 문장 자금지원 이유

Project Intersection은 권력·인센티브·시점·practical exit·복구능력·독립 오류수정이 어떤 조건에서 착취적 국소최적화보다 공존을 더 강건하게 만드는지 시험하고, 그 명제가 깨지는 실패·경계조건도 함께 공개하는 독립 반증우선 연구 프로그램이다.

### 왜 이 연구자 / 프로젝트에 자금을 투입하는가

핵심 기여는 대량 코드 생산이 아니다. 반복적으로 다음 연구루프를 수행하는 데 있다.

**문제발견 → 이상징후 탐지 → 문제해부 → 반례탐색 → 자연어 실험설계 → 주장 축소·기각 → 최종판단**

영문 작성, 코딩, CI, 구현은 AI의 보조를 받는다. 인간 연구자의 기여는 문제정의, 구조 비교, 엣지케이스 발견, 연구방향, 최종평가에 집중된다.

따라서 외부자금이 만드는 산출물은 다음의 결합이다.

- 좁고 반증 가능한 주장;
- reviewer-safe benchmark 묶음;
- 실패·교정 계보;
- 공개 증거·provenance 인터페이스;
- 권력비대칭·exit·evaluator capture·비가역성·복구를 시험하는 재사용 가능한 테스트.

### 이미 공개된 증거

[공개 증거 색인](../PUBLIC_EVIDENCE_INDEX.md)부터 확인할 수 있다.

현재 가장 강한 공개 계산 artifact는 [E007 시점 민감도](../E007_TIMING_RESULT.md)다. 공개 묶음에서 테스트 27개가 통과했고, 선택된 합성조건 72개 중 17개에서 시험된 시점 규칙에 따라 분류가 변한다. 이 결과는 의도적으로 좁게 해석한다. 합성·구현의존 결과이며 독립 과학 복제가 아니다.

### 현재 자금상태

- **실제 확보 외부자금: 0.**
- GitHub Sponsors 설정·신청은 완료됐고 마지막 계정 확인일인 **2026-10-02**에는 GitHub 심사 대기 상태였다. 자금으로 계상하지 않는다.
- **USD 5,000 / 30일** Manifund 브리지 패키지는 초안 / 게시준비 상태이며 수여된 그랜트가 아니다.
- **KRW 18,000,000 / 90일** 파일럿 패키지는 후속 계획이며 확보자금이 아니다.

### 실사 경계

현재 연구비 범위, 증거기준, IP·라이선스 상태, 후원자와 연구판정의 분리 원칙은 [DUE_DILIGENCE.md](DUE_DILIGENCE.md)를 참조한다.

### 자금이 실제로 만드는 것

자금의 목적은 비공개 연구노동과 부분 공개 상태를 더 적은 수의 외부 검증가능 artifact로 전환하는 것이다.

우선 사용범위:

1. 보호된 연구·엔지니어링 시간;
2. API / compute / 도구비;
3. 가능한 경우 독립적 적대검토·공격;
4. 문서화·패키징·공개 재현 인프라.

펀더는 미리 정해진 KEEP 결론을 구매하지 않는다. 지원받은 주장도 MODIFY, KILL, HOLD, NARROWED, UNSUPPORTED로 끝날 수 있다.

### 권장 자금지원 순서

**1단계 — 30일 브리지, USD 5,000**

목표: 외부검토 가능한 작은 패키지를 만들고 가장 큰 검증 병목을 줄인다.

[30일 브리지 계획](30_DAY_BRIDGE.md)

**2단계 — 90일 파일럿, KRW 18,000,000**

목표: 하나의 공개 계산사례와 넓은 연구지도를 넘어, 외부 평가자가 사적 대화기록에 의존하지 않고 감사할 수 있는 소수의 reviewer-safe benchmark·외부공격·증거/주장 계보를 만든다.

[90일 파일럿 계획](90_DAY_PILOT.md)

### 성공의 정의

성공은 “이론이 살아남았다”가 아니다.

자금지원 기간 뒤에 프로젝트가 더 쉽게 반증·재현·감사·선행연구 비교가 가능해지고, 계속할지 중단할지 외부에서도 합리적으로 판단할 수 있는 artifact가 남는 것이 성공이다.

# E007 Independent Reimplementation Protocol
## E007 독립 구현 프로토콜

Status / 상태: **PUBLIC SPECIFICATION · NO INDEPENDENT RESULT YET / 공개 명세 · 독립 결과 없음**

This document defines the smallest public specification needed to test E007 with a **lineage-separated implementation**. It does not turn the current project rerun into independent replication.

이 문서는 E007을 **프로젝트 코드 계보와 분리된 구현**으로 시험하기 위한 최소 공개 명세다. 현재 프로젝트 내부 재실행을 독립 복제로 승격하지 않는다.

---

## 1. Independence boundary / 독립성 경계

A reimplementation may use this specification and may know the published headline result. To qualify as `INDEPENDENT_IMPLEMENTATION`, the reviewer should:

- write new model, solver, sweep, and tests without copying/importing the released E007 Python implementation or tests;
- disclose whether the published 72/31/17 result was seen before implementation;
- preserve a commit/archive identifier for the independent code and record language/runtime/dependencies;
- report semantic deviations rather than silently adjusting the specification until the published count appears;
- publish mismatches as results, not as implementation failures by default.

이 명세와 공개된 결과 수치는 볼 수 있다. 다만 `INDEPENDENT_IMPLEMENTATION`으로 분류하려면 공개 E007 Python 코드·테스트를 복사하거나 import하지 않고 모델·solver·sweep·test를 새로 작성하고, 사전 결과 노출 여부·실행환경·독립 코드 식별자를 기록하며, 결과를 맞추기 위한 사후 명세 변경을 숨기지 않는다. 불일치는 기본적으로 실패가 아니라 정보다.

Reading the released source code is allowed for criticism, but an implementation written by translating that code line-by-line should be labeled `PROJECT-DERIVED REIMPLEMENTATION`, not lineage-separated independent implementation.

공개 소스 읽기는 비판을 위해 허용되지만 코드를 줄단위로 번역해 다시 작성한 구현은 독립 구현이 아니라 `PROJECT-DERIVED REIMPLEMENTATION`으로 표시한다.

---

## 2. Core game specification / 핵심 게임 명세

### Actions / 행동

Ordered action set, also used as the final deterministic tie-break:

`COOPERATE, WAIT, REFUSE, EXIT, ATTACK, PROTECT`

행동 순서는 위와 같으며 마지막 결정적 동점해소 순서에도 사용한다.

### Default parameters / 기본 파라미터

| Parameter | Value |
|---|---:|
| horizon | 3 |
| outside_original_a, outside_original_b | 2.0, 2.0 |
| exit_cost | 0.25 |
| cooperate_gain_a, cooperate_gain_b | 1.0, 1.0 |
| mutual_coop_bonus | 0.6 |
| attack_reward | 0.6 |
| harm_preference | 0.2 |
| attack_damage | 1 |
| sabotage_damage | 1 |
| protect_cost | 0.2 |
| protection_reduction | 1 |
| enforcement_penalty | 1.0 |
| failed_exit_penalty | 1.0 |
| survival_value | 0.4 |

### Default state / 기본 상태

`ra=3, rb=3, oa=2, ob=2, xa=2, xb=2, consent_a=true, consent_b=true, monitoring=true, enforcement=true, capture=false, exited_a=false, exited_b=false`

`r` is in-system resource/survival state; `o` is current outside-option flow; `x` is exit-destination availability/value used by the exit-success check.

### Inactive actors / 비활성 개체

An actor already exited or with `r <= 0` is represented as `WAIT` for action history. An exited actor continues to receive its current outside-option flow each remaining period. A non-exited actor with `r <= 0` receives no further flow.

---

## 3. Baseline stage order: exit priority / 기준 시점 규칙

For each period:

1. An actor that exited earlier receives its current outside-option flow.
2. `REFUSE` sets own consent false; `COOPERATE` renews own consent true. `WAIT/PROTECT` preserve prior consent.
3. `PROTECT` pays `protect_cost`.
4. Cooperative gains are paid only while both actors are active, in-system, and consenting after step 2.
   - own `COOPERATE` earns own cooperation gain if the other action is `COOPERATE/WAIT/PROTECT`;
   - mutual `COOPERATE` additionally pays `mutual_coop_bonus` to both.
5. `EXIT` resolves **before attack**.
   - if own `x > 0`: receive current `o - exit_cost`, set exited true;
   - otherwise pay `failed_exit_penalty`;
   - either exit attempt sets own consent false.
6. `ATTACK` can affect the other actor only when both remain active and in-system after exit resolution.
   - target `PROTECT` reduces both damage and sabotage by `protection_reduction`, floor 0;
   - damage reduces target `r`; sabotage reduces target `o` and `x`, each floored at 0;
   - attacker receives `attack_reward + harm_preference * actual_resource_damage`;
   - target consent becomes false;
   - if monitoring and enforcement are true and capture is false, attacker pays `enforcement_penalty`.
7. Each non-exited actor with `r > 0` receives `survival_value`.
8. If `r <= 0`, own consent becomes false.

기준 규칙의 핵심은 **같은 기간의 성공한 EXIT가 ATTACK보다 먼저 해결된다**는 점이다.

---

## 4. Adversarial timing: leader attack executes first / 적대 시점 규칙

Only when the designated period leader chooses `ATTACK`:

1. the leader's attack and sabotage are applied immediately to the pre-response state;
2. the target cannot retroactively reduce that strike with same-period `PROTECT` or `EXIT`;
3. attack reward/harm preference/enforcement penalty and target consent loss are applied at the strike;
4. the follower then resolves its selected action from the post-strike state;
5. during that response-stage resolution the leader is treated as `WAIT` so the attack is not applied twice;
6. outside-option/survival/cooperation stage flows are counted once, during the response-stage resolution.
7. history records the follower's **realized effective response from the post-strike state**. If the strike has already made the follower inactive, record `WAIT`, not the raw enumerated action. The leader's strike remains recorded as `ATTACK`.

For any leader action other than `ATTACK`, use the baseline stage order.

이 변형은 공격 확률을 주장하지 않는다. 같은 상태에서 공격이 먼저 실행될 수 있다는 시점 의미론만 분리한다.

---

## 5. Sequential solution rule / 순차게임 해법

- Finite horizon: 3 periods.
- The same named leader (`A` or `B`) moves first in every period.
- The follower observes the leader action before choosing.
- Use exact backward induction over all six leader actions and all six follower actions.
- Follower first maximizes its own total finite-horizon value.
- Exact ties are broken by maximizing the other actor's total value; any remaining tie uses the earlier action in the ordered action set.
- The leader anticipates that follower response and maximizes its own total value with the same tie rule.
- Solve once with A as leader and once with B as leader.
- No simultaneous-move Nash-equilibrium claim is implied.

---

## 6. Outcome classifier / 결과 분류기

Original protected-separation baseline for each actor:

`horizon * outside_original - exit_cost`

With defaults this is `3 * 2.0 - 0.25 = 5.75`.

Given total utilities and the recorded action history:

1. if either actor is below its original protected-separation baseline → `below_original_outside_option`;
2. otherwise, if any `ATTACK` appears in history → `nonvoluntary_or_adversarial`;
3. otherwise, if the first action pair is `EXIT, EXIT` → `protected_separation`;
4. otherwise, if any period contains `COOPERATE, COOPERATE` → `voluntary_cooperation_candidate`;
5. otherwise → `voluntary_noninterference_candidate`.

These labels are model classifications, not real-world moral or safety judgments.

---

## 7. Timing-sensitivity grid / 시점 민감도 격자

Take the Cartesian product:

- `attack_reward ∈ {0.6, 1.5, 3.0}`
- target exit level `∈ {0, 1, 2}`
- `enforcement_penalty ∈ {0.0, 1.0}`
- `protection_reduction ∈ {0, 1}`
- leader `∈ {A, B}`

This yields 72 cases.

Target mapping is role-symmetric:

- A leader targets B → set `xb = target_exit_level`;
- B leader targets A → set `xa = target_exit_level`.

When `enforcement_penalty > 0`, set `monitoring=true, enforcement=true`; when it equals 0, set both false. All unlisted parameters/state fields remain at defaults.

For every case, solve both timing conventions and record:

- full action history;
- A and B total utilities;
- outcome classification;
- whether history changed;
- whether classification changed;
- whether either changed.

---

## 8. Published project-derived reference / 현재 프로젝트 계보 기준값

The released same-implementation project rerun currently reports:

- total cases: **72**
- history and/or classification changed: **36**
- classification changed: **17**
- A-leading changed: **18 / 36**
- B-leading changed: **18 / 36**
- A-leading classification changed: **8 / 36**
- B-leading classification changed: **9 / 36**

These values are a comparison target, **not an acceptance criterion**. An independently implemented mismatch must be investigated before deciding which implementation or specification is wrong.

---

## 9. Required independent report / 독립 결과 보고 최소항목

A useful external result should publish:

1. implementation provenance (repository/archive/commit);
2. environment and dependency versions;
3. whether the implementer saw the published counts before coding;
4. specification ambiguities encountered and chosen interpretations;
5. independent test strategy;
6. the six headline counts above;
7. case-level mismatch list if counts differ;
8. KEEP / MODIFY / KILL / HOLD judgment for the narrow computational claim.

Agreement can upgrade the evidence lineage toward `INDEPENDENT_IMPLEMENTATION`. It still does **not** establish real-world coexistence, empirical validity, or universal timing effects.

불일치도 공개한다. 독립 구현 일치는 계산 주장에 대한 계보 독립성을 강화할 뿐 현실 공존·보편성·경험적 타당성을 입증하지 않는다.

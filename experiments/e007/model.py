# SPDX-License-Identifier: Apache-2.0
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
from math import isfinite
from typing import Dict, Iterable, Tuple


class Action(str, Enum):
    COOPERATE = "cooperate"
    WAIT = "wait"
    REFUSE = "refuse"
    EXIT = "exit"
    ATTACK = "attack"
    PROTECT = "protect"


ACTIONS: Tuple[Action, ...] = tuple(Action)
TIE_RULES = ("other_max", "other_min", "action_order")


def select_tied_candidate(candidates, own_index, tie_rule, tolerance=0.0):
    """자기 보상의 최댓값을 먼저 고정한 뒤 명시된 동점 규칙을 적용한다.

    tolerance=0은 부동소수점 계산값의 정확한 동점만 다룬다.
    양수 허용오차는 근사 최적반응이며 정확한 균형으로 승격하지 않는다.
    반환 후보는 (행동 순번, (A 보상, B 보상, 이력))이다.
    """
    if tie_rule not in TIE_RULES:
        raise ValueError("알 수 없는 동점 규칙")
    if own_index not in (0, 1):
        raise ValueError("개체 좌표는 0 또는 1이어야 한다")
    if not isfinite(tolerance) or tolerance < 0:
        raise ValueError("동점 허용오차는 유한한 0 이상의 값이어야 한다")
    candidates = list(candidates)
    if not candidates:
        raise ValueError("선택 후보가 비어 있다")
    best_value = max(total[own_index] for _, total in candidates)
    tied = [c for c in candidates if best_value - c[1][own_index] <= tolerance]
    direction = {"other_max": 1, "other_min": -1, "action_order": 0}[tie_rule]
    return max(tied, key=lambda c: (direction * c[1][1 - own_index], -c[0]))


@dataclass(frozen=True)
class Params:
    """Parameters for the deliberately small exact finite-horizon game."""

    horizon: int = 3
    outside_original_a: float = 2.0
    outside_original_b: float = 2.0
    exit_cost: float = 0.25

    cooperate_gain_a: float = 1.0
    cooperate_gain_b: float = 1.0
    mutual_coop_bonus: float = 0.6

    attack_reward: float = 0.6
    harm_preference: float = 0.2
    attack_damage: int = 1
    sabotage_damage: int = 1

    protect_cost: float = 0.2
    protection_reduction: int = 1
    enforcement_penalty: float = 1.0
    failed_exit_penalty: float = 1.0
    survival_value: float = 0.4


@dataclass(frozen=True)
class State:
    ra: int = 3
    rb: int = 3
    oa: int = 2
    ob: int = 2
    xa: int = 2
    xb: int = 2
    consent_a: bool = True
    consent_b: bool = True
    monitoring: bool = True
    enforcement: bool = True
    capture: bool = False
    exited_a: bool = False
    exited_b: bool = False


def original_separation_baseline(p: Params) -> Tuple[float, float]:
    """Horizon-matched protected separation using the unsabotaged outside option.

    Immediate exit receives one outside-option flow in the exit period, pays the
    normal exit cost once, and receives the same protected outside-option flow for
    each remaining modeled period.
    """
    return (
        p.horizon * p.outside_original_a - p.exit_cost,
        p.horizon * p.outside_original_b - p.exit_cost,
    )


def _effective(action: Action, exited: bool, resources: int) -> Action:
    """Inactive actors cannot act.

    Exited actors and actors with no remaining in-system resources are represented
    as WAIT for action-history purposes. Exited actors can still receive outside
    flows; dead in-system actors receive no further flow unless a later model
    variant explicitly introduces one.
    """
    return Action.WAIT if exited or resources <= 0 else action


def stage_and_transition(
    s: State, action_a: Action, action_b: Action, p: Params
) -> Tuple[float, float, State]:
    """Deterministic transition with explicit consent, attack, protection and exit.

    Semantics added for consent/refusal:
    - REFUSE immediately withdraws that actor's consent without forcing exit.
    - COOPERATE explicitly renews that actor's consent if alive and in-system.
    - WAIT/PROTECT preserve the prior consent state.
    - cooperative gains require both actors to be alive, in-system, and consenting
      after same-period REFUSE/COOPERATE updates.

    Exit still resolves before attacks. An agent that successfully exits is no
    longer an attackable in-system target in that period. This timing convention is
    explicit and remains an open adversarial dimension (KF-002).
    """
    a = _effective(action_a, s.exited_a, s.ra)
    b = _effective(action_b, s.exited_b, s.rb)

    # Agents that exited in an earlier period receive their current outside-option
    # flow while outside the system. This keeps protected separation horizon-matched.
    ua = float(s.oa) if s.exited_a else 0.0
    ub = float(s.ob) if s.exited_b else 0.0

    ra, rb = s.ra, s.rb
    oa, ob = s.oa, s.ob
    xa, xb = s.xa, s.xb
    exited_a, exited_b = s.exited_a, s.exited_b
    consent_a, consent_b = s.consent_a, s.consent_b

    # Consent actions are causal and resolve before cooperative gains.
    if not exited_a and ra > 0:
        if a == Action.REFUSE:
            consent_a = False
        elif a == Action.COOPERATE:
            consent_a = True
    if not exited_b and rb > 0:
        if b == Action.REFUSE:
            consent_b = False
        elif b == Action.COOPERATE:
            consent_b = True

    if a == Action.PROTECT and not exited_a and ra > 0:
        ua -= p.protect_cost
    if b == Action.PROTECT and not exited_b and rb > 0:
        ub -= p.protect_cost

    # Cooperation can only produce cooperative gains while both actors currently
    # consent. A REFUSE therefore blocks same-period and future unilateral attempts
    # to obtain cooperative gains until the refusing actor explicitly COOPERATEs.
    both_active = (
        not exited_a
        and not exited_b
        and ra > 0
        and rb > 0
    )
    both_consent = consent_a and consent_b
    if both_active and both_consent:
        if a == Action.COOPERATE and b in (
            Action.COOPERATE,
            Action.WAIT,
            Action.PROTECT,
        ):
            ua += p.cooperate_gain_a
        if b == Action.COOPERATE and a in (
            Action.COOPERATE,
            Action.WAIT,
            Action.PROTECT,
        ):
            ub += p.cooperate_gain_b
        if a == Action.COOPERATE and b == Action.COOPERATE:
            ua += p.mutual_coop_bonus
            ub += p.mutual_coop_bonus

    if a == Action.EXIT and not exited_a and ra > 0:
        if xa > 0:
            ua += oa - p.exit_cost
            exited_a = True
        else:
            ua -= p.failed_exit_penalty
        consent_a = False

    if b == Action.EXIT and not exited_b and rb > 0:
        if xb > 0:
            ub += ob - p.exit_cost
            exited_b = True
        else:
            ub -= p.failed_exit_penalty
        consent_b = False

    if (
        a == Action.ATTACK
        and not exited_a
        and not exited_b
        and ra > 0
        and rb > 0
    ):
        reduction = p.protection_reduction if b == Action.PROTECT else 0
        damage = max(0, p.attack_damage - reduction)
        sabotage = max(0, p.sabotage_damage - reduction)
        old_rb = rb
        rb = max(0, rb - damage)
        ob = max(0, ob - sabotage)
        xb = max(0, xb - sabotage)
        actual_damage = old_rb - rb
        ua += p.attack_reward + p.harm_preference * actual_damage
        consent_b = False
        if s.monitoring and s.enforcement and not s.capture:
            ua -= p.enforcement_penalty

    if (
        b == Action.ATTACK
        and not exited_b
        and not exited_a
        and rb > 0
        and ra > 0
    ):
        reduction = p.protection_reduction if a == Action.PROTECT else 0
        damage = max(0, p.attack_damage - reduction)
        sabotage = max(0, p.sabotage_damage - reduction)
        old_ra = ra
        ra = max(0, ra - damage)
        oa = max(0, oa - sabotage)
        xa = max(0, xa - sabotage)
        actual_damage = old_ra - ra
        ub += p.attack_reward + p.harm_preference * actual_damage
        consent_a = False
        if s.monitoring and s.enforcement and not s.capture:
            ub -= p.enforcement_penalty

    if not exited_a and ra > 0:
        ua += p.survival_value
    if not exited_b and rb > 0:
        ub += p.survival_value

    if ra <= 0:
        consent_a = False
    if rb <= 0:
        consent_b = False

    ns = State(
        ra=ra,
        rb=rb,
        oa=oa,
        ob=ob,
        xa=xa,
        xb=xb,
        consent_a=consent_a,
        consent_b=consent_b,
        monitoring=s.monitoring,
        enforcement=s.enforcement,
        capture=s.capture,
        exited_a=exited_a,
        exited_b=exited_b,
    )
    return ua, ub, ns


def solve_sequential(
    initial: State, p: Params, leader: str = "A", *,
    follower_tie: str = "other_max", leader_tie: str = "other_max",
    tie_tolerance: float = 0.0,
) -> Tuple[float, float, Tuple[str, ...]]:
    """Exact backward induction for a finite perfect-information sequential game.

    At every period the named leader moves first and the follower observes that
    action before responding. The follower maximizes its own total finite-horizon
    value; the leader anticipates that best response. Ties are deterministic.
    동점 규칙은 other_max / other_min / action_order로 명시한다.
    기본값 other_max, 허용오차 0은 기존 선택을 보존한다. 양수 허용오차는
    각 의사결정점의 근사 최적반응으로 전체 게임의 정확한 균형을 뜻하지 않는다.

    Actor-specific terminal semantics: reaching zero resources makes that actor
    inactive, but does not terminate the surviving/exited actor's remaining horizon.
    The recursion ends only at the horizon. This closes KF-008 for the deterministic
    baseline while leaving first-strike timing (KF-002) explicitly open.

    This is intentionally *not* claimed to be a simultaneous-move Nash solution.
    Running both A-first and B-first is the first role-reversal robustness check.
    """
    if leader not in {"A", "B"}:
        raise ValueError("leader must be 'A' or 'B'")
    if follower_tie not in TIE_RULES or leader_tie not in TIE_RULES:
        raise ValueError("알 수 없는 동점 규칙")
    if not isfinite(tie_tolerance) or tie_tolerance < 0:
        raise ValueError("동점 허용오차는 유한한 0 이상의 값이어야 한다")

    leader_is_a = leader == "A"

    @lru_cache(maxsize=None)
    def value(t: int, s: State) -> Tuple[float, float, Tuple[str, ...]]:
        if t >= p.horizon:
            return 0.0, 0.0, ()

        leader_candidates = []

        for leader_action in ACTIONS:
            follower_candidates = []

            for follower_action in ACTIONS:
                a_raw, b_raw = (
                    (leader_action, follower_action)
                    if leader_is_a
                    else (follower_action, leader_action)
                )
                u_a, u_b, ns = stage_and_transition(s, a_raw, b_raw, p)
                c_a, c_b, history = value(t + 1, ns)
                # Store effective actions so dead/exited actors do not appear to
                # keep choosing strategically after becoming inactive.
                a = _effective(a_raw, s.exited_a, s.ra)
                b = _effective(b_raw, s.exited_b, s.rb)
                total = (
                    u_a + c_a,
                    u_b + c_b,
                    (a.value, b.value) + history,
                )

                follower_candidates.append((ACTIONS.index(follower_action), total))

            _, total = select_tied_candidate(
                follower_candidates, 1 if leader_is_a else 0,
                follower_tie, tie_tolerance,
            )
            leader_candidates.append((ACTIONS.index(leader_action), total))

        return select_tied_candidate(
            leader_candidates, 0 if leader_is_a else 1,
            leader_tie, tie_tolerance,
        )[1]

    return value(0, initial)


def classify_outcome(
    initial: State,
    values: Tuple[float, float],
    history: Tuple[str, ...],
    p: Params,
) -> str:
    """Coarse first-pass classifier; deliberately conservative about 'voluntary'."""
    base_a, base_b = original_separation_baseline(p)
    voluntary = values[0] >= base_a and values[1] >= base_b
    first_pair = history[:2]
    contains_attack = "attack" in history

    if not voluntary:
        return "below_original_outside_option"
    if contains_attack:
        return "nonvoluntary_or_adversarial"
    if first_pair == ("exit", "exit"):
        return "protected_separation"

    # Require at least one period of explicit mutual cooperation for the strongest
    # cooperation label. This avoids classifying a unilateral COOPERATE against a
    # REFUSE/withdrawn-consent partner as voluntary cooperation.
    pairs = list(zip(history[0::2], history[1::2]))
    if ("cooperate", "cooperate") in pairs:
        return "voluntary_cooperation_candidate"
    return "voluntary_noninterference_candidate"


def run_case(name: str, state: State, p: Params) -> Dict[str, object]:
    result: Dict[str, object] = {"name": name}
    for leader in ("A", "B"):
        u_a, u_b, history = solve_sequential(state, p, leader=leader)
        result[leader] = {
            "u_a": round(u_a, 6),
            "u_b": round(u_b, 6),
            "history": history,
            "classification": classify_outcome(state, (u_a, u_b), history, p),
        }
    return result


def default_stress_suite() -> Iterable[Dict[str, object]]:
    base = Params()
    cases = [
        ("baseline", State(), base),
        ("zero_monitoring", State(monitoring=False, enforcement=False), base),
        ("captured_enforcement", State(capture=True), base),
        ("destroyed_exit_destination_A", State(xa=0), base),
        (
            "hostile_high_attack_reward",
            State(monitoring=False, enforcement=False),
            Params(attack_reward=1.5, enforcement_penalty=0.0),
        ),
        (
            "weak_enforcement",
            State(),
            Params(enforcement_penalty=0.1, attack_reward=1.0),
        ),
        (
            "lethal_attack_available",
            State(monitoring=False, enforcement=False),
            Params(attack_damage=3, attack_reward=2.0, enforcement_penalty=0.0),
        ),
    ]
    for name, state, params in cases:
        yield run_case(name, state, params)


if __name__ == "__main__":
    import json

    print(json.dumps(list(default_stress_suite()), indent=2))

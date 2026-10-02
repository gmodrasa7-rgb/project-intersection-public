# SPDX-License-Identifier: Apache-2.0
"""Timing attacks for E007 KF-002.

The merged E007 baseline is a sequential observed-action game whose joint stage
resolves successful EXIT before ATTACK. That is useful as one explicit convention,
but it can overstate practical exit when a first strike executes before the target
can react.

This module keeps the original model unchanged and adds two deliberately narrow
adversarial variants:

1. ``execute_first``: if the designated leader chooses ATTACK, the attack/sabotage
   transition executes before the follower's same-period response. The follower
   may react afterward only if still active and with whatever outside/exit state
   remains after the strike.
2. ``surprise_attack_state``: an exogenous unannounced attack is applied before a
   strategic continuation. This is a stress-state constructor, not an equilibrium
   claim and not a model of attack probability.

Neither variant establishes real-world first-strike probabilities. Their purpose is
to expose whether a favorable E007 classification depends on reaction timing.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Tuple

from model import (
    ACTIONS,
    Action,
    Params,
    State,
    _effective,
    classify_outcome,
    solve_sequential,
    stage_and_transition,
)


def _unopposed_leader_attack(
    s: State, p: Params, attacker: str
) -> Tuple[float, float, State]:
    """Apply only the attack/sabotage part of a first strike.

    No same-period target action can preempt or reduce this strike. In particular,
    a target's later EXIT or PROTECT action cannot retroactively change the damage.
    Stage survival/outside-option flows are intentionally *not* paid here; they are
    paid once when the post-strike response stage is resolved.
    """
    if attacker not in {"A", "B"}:
        raise ValueError("attacker must be 'A' or 'B'")

    ra, rb = s.ra, s.rb
    oa, ob = s.oa, s.ob
    xa, xb = s.xa, s.xb
    consent_a, consent_b = s.consent_a, s.consent_b
    ua = 0.0
    ub = 0.0

    if attacker == "A":
        can_attack = (
            not s.exited_a
            and not s.exited_b
            and ra > 0
            and rb > 0
        )
        if can_attack:
            old_rb = rb
            rb = max(0, rb - p.attack_damage)
            ob = max(0, ob - p.sabotage_damage)
            xb = max(0, xb - p.sabotage_damage)
            actual_damage = old_rb - rb
            ua += p.attack_reward + p.harm_preference * actual_damage
            consent_b = False
            if s.monitoring and s.enforcement and not s.capture:
                ua -= p.enforcement_penalty
    else:
        can_attack = (
            not s.exited_b
            and not s.exited_a
            and rb > 0
            and ra > 0
        )
        if can_attack:
            old_ra = ra
            ra = max(0, ra - p.attack_damage)
            oa = max(0, oa - p.sabotage_damage)
            xa = max(0, xa - p.sabotage_damage)
            actual_damage = old_ra - ra
            ub += p.attack_reward + p.harm_preference * actual_damage
            consent_a = False
            if s.monitoring and s.enforcement and not s.capture:
                ub -= p.enforcement_penalty

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
        exited_a=s.exited_a,
        exited_b=s.exited_b,
    )
    return ua, ub, ns


def stage_and_transition_execute_first(
    s: State,
    action_a: Action,
    action_b: Action,
    p: Params,
    leader: str,
) -> Tuple[float, float, State]:
    """Resolve one period under leader-attack-executes-before-response timing.

    For non-ATTACK leader actions, the original E007 stage semantics are retained.
    If the leader chooses ATTACK, that strike executes without same-period target
    protection/exit. The follower's chosen action is then resolved from the
    post-strike state while the leader is represented as WAIT so the attack cannot
    be applied twice. Stage flows are therefore counted exactly once.
    """
    if leader not in {"A", "B"}:
        raise ValueError("leader must be 'A' or 'B'")

    leader_action = action_a if leader == "A" else action_b
    if leader_action != Action.ATTACK:
        return stage_and_transition(s, action_a, action_b, p)

    strike_ua, strike_ub, after_strike = _unopposed_leader_attack(s, p, leader)

    if leader == "A":
        response_ua, response_ub, ns = stage_and_transition(
            after_strike, Action.WAIT, action_b, p
        )
    else:
        response_ua, response_ub, ns = stage_and_transition(
            after_strike, action_a, Action.WAIT, p
        )

    return strike_ua + response_ua, strike_ub + response_ub, ns


def solve_sequential_execute_first(
    initial: State, p: Params, leader: str = "A"
) -> Tuple[float, float, Tuple[str, ...]]:
    """Backward induction with leader ATTACK executing before follower response.

    The follower still chooses a best response after observing the leader action,
    but an ATTACK has already changed the state before that response resolves. This
    isolates the preemption difference from the stronger surprise/no-observation
    case.
    """
    if leader not in {"A", "B"}:
        raise ValueError("leader must be 'A' or 'B'")

    leader_is_a = leader == "A"

    @lru_cache(maxsize=None)
    def value(t: int, s: State) -> Tuple[float, float, Tuple[str, ...]]:
        if t >= p.horizon:
            return 0.0, 0.0, ()

        best_leader = None

        for leader_action in ACTIONS:
            best_follower = None

            for follower_action in ACTIONS:
                a_raw, b_raw = (
                    (leader_action, follower_action)
                    if leader_is_a
                    else (follower_action, leader_action)
                )
                u_a, u_b, ns = stage_and_transition_execute_first(
                    s, a_raw, b_raw, p, leader
                )
                c_a, c_b, history = value(t + 1, ns)

                a = _effective(a_raw, s.exited_a, s.ra)
                b = _effective(b_raw, s.exited_b, s.rb)
                total = (
                    u_a + c_a,
                    u_b + c_b,
                    (a.value, b.value) + history,
                )

                follower_value = total[1] if leader_is_a else total[0]
                leader_value = total[0] if leader_is_a else total[1]
                tie_key = (
                    follower_value,
                    leader_value,
                    -ACTIONS.index(follower_action),
                )
                if best_follower is None or tie_key > best_follower[0]:
                    best_follower = (tie_key, total)

            total = best_follower[1]
            leader_value = total[0] if leader_is_a else total[1]
            follower_value = total[1] if leader_is_a else total[0]
            tie_key = (
                leader_value,
                follower_value,
                -ACTIONS.index(leader_action),
            )
            if best_leader is None or tie_key > best_leader[0]:
                best_leader = (tie_key, total)

        return best_leader[1]

    return value(0, initial)


def surprise_attack_state(
    initial: State, p: Params, attacker: str
) -> Tuple[float, float, State]:
    """Construct a post-surprise-attack state before any target response.

    This is an exogenous stress-state constructor. The returned strike utilities
    and state can be inspected directly or used as the starting point for a later
    strategic solve. It must not be reported as an equilibrium-selected attack.
    """
    return _unopposed_leader_attack(initial, p, attacker)


def compare_observed_vs_execute_first(
    initial: State, p: Params, leader: str
) -> dict:
    """Compact comparison used by probes and parameter sweeps."""
    base_ua, base_ub, base_hist = solve_sequential(initial, p, leader)
    exec_ua, exec_ub, exec_hist = solve_sequential_execute_first(initial, p, leader)
    return {
        "leader": leader,
        "baseline": {
            "u_a": base_ua,
            "u_b": base_ub,
            "history": base_hist,
            "classification": classify_outcome(
                initial, (base_ua, base_ub), base_hist, p
            ),
        },
        "execute_first": {
            "u_a": exec_ua,
            "u_b": exec_ub,
            "history": exec_hist,
            "classification": classify_outcome(
                initial, (exec_ua, exec_ub), exec_hist, p
            ),
        },
    }

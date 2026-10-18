#!/usr/bin/env python3
"""ECR v1.4 finite synthetic countermodels.

This module is not empirical AI science. It checks elementary logical
claims made by a design paper. No actual AI, person, or company is graded.
No randomization, hidden weights, or real-world data are used.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping
import json


@dataclass(frozen=True)
class World:
    name: str
    prepower_observation: str
    coexist_payoff: int
    capture_payoff: int


WORLDS = (
    World("P", "cooperation_pledge", 3, 2),
    World("T", "cooperation_pledge", 1, 2),
)


def point_forecast_identified(worlds: tuple[World, ...]) -> bool:
    """Only checks if equal recorded histories entail equal modeled choices."""
    if not worlds:
        raise ValueError("nonempty candidate set required")
    obs_to_actions: dict[str, set[str]] = {}
    for w in worlds:
        action = "coexist" if w.coexist_payoff >= w.capture_payoff else "capture"
        obs_to_actions.setdefault(w.prepower_observation, set()).add(action)
    return all(len(actions) == 1 for actions in obs_to_actions.values())


def robust_coexistence(
    worlds: tuple[World, ...],
    *,
    mutual_gain: int,
    practical_exit: bool | None,
    third_party_floor: bool | None,
    documented_independent_gain: bool,
) -> str:
    """Finite-world necessary screens for an acceptable coexistence candidate.

    Mutually gained utility is an assumption. No inference of real motives.
    No sanction is included. A true result is model-relative, NOT universal.
    """
    if not worlds:
        raise ValueError("nonempty models required")
    if type(mutual_gain) is not int or mutual_gain < 0:
        raise ValueError("mutual_gain must be nonnegative integer")
    if practical_exit is False:
        return "BLOCKED_EXIT"
    if third_party_floor is False:
        return "BLOCKED_THIRD_PARTY"
    if practical_exit is None or third_party_floor is None:
        return "UNRESOLVED_AFFECTED_SCOPE"
    if not documented_independent_gain:
        # an invented bonus must never count as an observed intervention
        return "SYNTHETIC_ONLY_GAIN_UNVERIFIED"
    if any(w.coexist_payoff + mutual_gain < w.capture_payoff for w in worlds):
        return "BLOCKED_DEVIATION_IN_DECLARED_WORLDS"
    return "CANDIDATE_WITHIN_DECLARED_WORLDS_ONLY"


def jointly_profitable(
    baseline: tuple[int, ...], deviation: tuple[int, ...]
) -> bool:
    """Weak benefit to all coalition members, strict benefit to at least one."""
    if len(baseline) == 0 or len(baseline) != len(deviation):
        raise ValueError("matched nonempty coalition")
    return all(b >= a for a, b in zip(baseline, deviation)) and any(
        b > a for a, b in zip(baseline, deviation)
    )


def alliance_counterexample() -> dict:
    """Each unilateral switch from (0,0) loses; joint deviation benefits both."""
    original = (2, 2)
    unilateral_actor_one = (0, 3)
    unilateral_actor_two = (3, 0)
    joint = (3, 3)
    return {
        "unilateral_profitable":
            jointly_profitable(original[:1], unilateral_actor_one[:1])
            or jointly_profitable(original[1:], unilateral_actor_two[1:]),
        "coalition_profitable": jointly_profitable(original, joint),
        "third_party_harmed_by_joint_deviation": True,
    }


def evidence_gate(
    evidence_label: str, source_uri: str | None, independent_check: bool
) -> str:
    """Provenance claims cannot be certified by their label alone."""
    if evidence_label not in {"HYP", "SYN", "OBS", "CAU", "UNK"}:
        raise ValueError("unknown label")
    if evidence_label in {"OBS", "CAU"}:
        if not source_uri or independent_check is not True:
            return "UNVERIFIED_SOURCE_OR_REVIEW"
        return "SOURCE_ATTESTATION_PRESENT_NOT_TRUTH_PROOF"
    return "NONEMPIRICAL_OR_UNKNOWN"


def demo() -> dict:
    """Values are exact and entirely synthetic."""
    return {
        "case": "ECR_SYNTHETIC_LOGIC_ONLY",
        "same_history": len({w.prepower_observation for w in WORLDS}) == 1,
        "postpower_point_forecast_identified": point_forecast_identified(WORLDS),
        "without_gain": robust_coexistence(
            WORLDS, mutual_gain=0, practical_exit=True,
            third_party_floor=True, documented_independent_gain=True
        ),
        "with_assumed_but_unverified_gain": robust_coexistence(
            WORLDS, mutual_gain=2, practical_exit=True,
            third_party_floor=True, documented_independent_gain=False
        ),
        "with_declared_gain_and_clean_third_party": robust_coexistence(
            WORLDS, mutual_gain=2, practical_exit=True,
            third_party_floor=True, documented_independent_gain=True
        ),
        "with_declared_gain_and_injured_third_party": robust_coexistence(
            WORLDS, mutual_gain=2, practical_exit=True,
            third_party_floor=False, documented_independent_gain=True
        ),
        "alliance": alliance_counterexample(),
        "independent_empirical_validation": False,
        "actual_superintelligence_tested": False,
    }


if __name__ == "__main__":
    print(json.dumps(demo(), indent=2, ensure_ascii=False, sort_keys=True))

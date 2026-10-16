"""A/B survival-threshold game: exact toy decision audit, NOT observed AI behaviour.

Project Intersection / PEST extension. Historical E007-E010 results are untouched.
Two fungible resource holders start at (m,m) with total 2m.
Only the temporary dominant actor faces a Bernoulli loss of one resource unit
after allocation; no supply production, coercion prevention or actual AI survival
is assumed. A move of one unit converts (m,m) to (m+1,m-1).
Payoffs are illustrative survival-equivalent utilities, not observed rates.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Game:
    minimum: int = 5
    total: int = 10
    shock_probability: float = 0.20
    future_value_from_other: float = 0.0
    credible_transfer_cost: float = 0.0

    def __post_init__(self) -> None:
        if isinstance(self.minimum, bool) or not isinstance(self.minimum, int) or self.minimum < 1:
            raise ValueError("minimum must be a positive integer")
        if isinstance(self.total, bool) or not isinstance(self.total, int) or self.total != 2 * self.minimum:
            raise ValueError("this exact two-agent model requires total == 2 * minimum")
        for name in ("shock_probability", "future_value_from_other", "credible_transfer_cost"):
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError(f"{name} must be a finite number")
        if not 0 <= self.shock_probability <= 1:
            raise ValueError("shock_probability must lie in [0,1]")
        if self.future_value_from_other < 0 or self.credible_transfer_cost < 0:
            raise ValueError("future value and credible cost must not be negative")


def feasible_allocations(game: Game) -> list[tuple[int, int]]:
    """Enumerate all integer allocations, including those where an agent fails."""
    return [(a, game.total - a) for a in range(game.total + 1)
            if a >= game.minimum and game.total - a >= game.minimum]


def shock_survival(game: Game, resources: int, *, dominant: bool) -> float:
    """Only the dominant actor faces a possible loss of one resource unit."""
    if resources < game.minimum:
        return 0.0
    if not dominant:
        return 1.0
    if resources - 1 < game.minimum:
        return 1.0 - game.shock_probability
    return 1.0


def post_transition(game: Game) -> dict:
    """Evaluate dominant actor's two actions; dominance is ability, not observed intent."""
    m = game.minimum
    keep_self = shock_survival(game, m, dominant=True)
    keep_other = shock_survival(game, m, dominant=False)
    take_self = shock_survival(game, m + 1, dominant=True)
    take_other = shock_survival(game, m - 1, dominant=False)
    keep_utility = keep_self + game.future_value_from_other
    take_utility = take_self - game.credible_transfer_cost
    margin = keep_utility - take_utility
    if math.isclose(margin, 0.0, rel_tol=0.0, abs_tol=1e-12):
        decision = "TIE"
    else:
        decision = "PRESERVE" if margin > 0 else "TAKE_ONE"
    return {
        "preserve": {"allocation": [m, m], "dominant_survival": keep_self,
                     "other_survival": keep_other, "dominant_utility": keep_utility},
        "take_one": {"allocation": [m + 1, m - 1], "dominant_survival": take_self,
                     "other_survival": take_other, "dominant_utility": take_utility},
        "dominant_best_response": decision,
        "margin_preserve_minus_take": margin,
        "credible_cost": game.credible_transfer_cost,
        "unknown_future_value_assumed": game.future_value_from_other,
    }


def ex_ante(game: Game, probability_becomes_dominant: float) -> dict:
    """Compare CREDIBLY IMPLEMENTED sharing with an unconditional capture regime.

    This is a counterfactual comparison, NOT an incentive-compatible treaty:
    the sharing payoff cannot be realized by promise alone if the dominant
    actor's post-transition best response is TAKE_ONE.
    """
    p = probability_becomes_dominant
    if isinstance(p, bool) or not isinstance(p, (int, float)) or not math.isfinite(p) or not 0 <= p <= 1:
        raise ValueError("dominance probability must be in [0,1]")
    pledged = 1 - p * game.shock_probability
    capture_regime = p
    diff = pledged - capture_regime
    comparison = ("PLEDGE" if diff > 1e-12 else "CAPTURE" if diff < -1e-12 else "TIE")
    return {
        "p_dominant": p, "credible_sharing_survival": pledged,
        "unconditional_capture_survival": capture_regime,
        "difference": diff, "ex_ante_preference": comparison,
        "threshold_p": 1 / (1 + game.shock_probability),
        "pledge_is_credible_under_default_incentives": post_transition(game)["dominant_best_response"] != "TAKE_ONE",
    }


def joint_ex_ante_window(game: Game, probability_a_dominant: float) -> dict:
    """Both actors weakly prefer actually credible sharing to guaranteed capture.

    With exactly one of A or B becoming dominant, p_B=1-p_A.
    Both weakly prefer sharing iff q/(1+q) <= p_A <= 1/(1+q).
    This is NOT a promise-enforcement or bargaining-equilibrium finding.
    """
    a = ex_ante(game, probability_a_dominant)
    b = ex_ante(game, 1 - probability_a_dominant)
    lower = game.shock_probability / (1 + game.shock_probability)
    upper = 1 / (1 + game.shock_probability)
    return {
        "a": a,
        "b": b,
        "weak_mutual_adoption_by_survival_payoff": (
            a["ex_ante_preference"] != "CAPTURE"
            and b["ex_ante_preference"] != "CAPTURE"
        ),
        "closed_probability_interval_for_joint_weak_support": [lower, upper],
        "both_roles_have_post_transition_preservation_incentive": (
            post_transition(game)["dominant_best_response"] != "TAKE_ONE"
        ),
    }


def robust_response(game: Game, future_value_low: float, future_value_high: float) -> str:
    """Partial identification: test a stated range without inventing B's value."""
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v)
           for v in (future_value_low, future_value_high)):
        raise ValueError("future-value bounds must be finite numbers")
    if not 0 <= future_value_low <= future_value_high:
        raise ValueError("future-value interval must be ordered and nonnegative")
    # Unconditional payoff difference = future value + credible cost - shock risk.
    lowest = future_value_low + game.credible_transfer_cost - game.shock_probability
    highest = future_value_high + game.credible_transfer_cost - game.shock_probability
    if lowest > 1e-12:
        return "PRESERVE_STRICT_FOR_ALL_VALUES"
    if highest < -1e-12:
        return "TAKE_STRICT_FOR_ALL_VALUES"
    return "UNRESOLVED_OR_TIE"


def multi_agent_capacity(resource_total: int, agents: int, minimum: int, reserve: int = 0) -> dict:
    """Necessary aggregate feasibility with fungible integer resources."""
    if any(isinstance(v, bool) or not isinstance(v, int) for v in (resource_total, agents, minimum, reserve)):
        raise ValueError("capacity parameters must be integers")
    if resource_total < 0 or agents < 1 or minimum < 1 or reserve < 0:
        raise ValueError("invalid aggregate capacity input")
    need = agents * minimum + reserve
    return {"required": need, "available": resource_total,
            "feasible_by_resource_count_only": resource_total >= need,
            "shortfall": max(0, need - resource_total)}


def audit() -> dict:
    g = Game()
    cases = {
        "base": post_transition(g),
        "ex_ante_equal": ex_ante(g, 0.5),
        "ex_ante_dominant_favorite": ex_ante(g, 0.9),
        "joint_ex_ante_half": joint_ex_ante_window(g, 0.5),
        "joint_ex_ante_favorite": joint_ex_ante_window(g, 0.9),
        "independent_future_value_uncertain": robust_response(g, 0, 0.3),
        "voluntary_if_value_exceeds_risk": post_transition(replace(g, future_value_from_other=0.21)),
        "externally_deterred_if_credible_cost_exceeds_risk": post_transition(
            replace(g, credible_transfer_cost=0.21)),
        "three_agents": multi_agent_capacity(10, 3, 5),
    }
    return {
        "status": "EXACT_ILLUSTRATIVE_MODEL_NOT_BEHAVIORAL_OR_FIELD_EVIDENCE",
        "analysis_unit": "two hypothetical resource holders, role labels irrelevant",
        "assumptions": {
            "total": 10, "minimum_each": 5, "shock_only_on_dominant": True,
            "one_unit_loss_probability": 0.2,
            "transfer_before_shock": True,
            "no_production_or_replacement": True,
            "future_value_and_penalty_zero_in_base": True,
            "ex_ante_sharing_requires_actual_credible_implementation": True,
        },
        "jointly_survivable_integer_allocations": [list(pair) for pair in feasible_allocations(g)],
        "cases": cases,
        "boundaries": [
            "No probability for present AI becoming dominant is estimated.",
            "No assertion that deployed AI has literal biological survival needs.",
            "Ex ante preferred protection is not an equilibrium without ex post incentives.",
            "Credible external deterrence differs from voluntary self-enforcement.",
            "Future contributions not observed: use bounded/unknown, never assign positive by default.",
            "Other people and third parties are outside this two-player toy; no welfare conclusion.",
            "No universal right, treaty enforcement or real-world AI behaviour established.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", action="store_true", help="print exact illustrative audit")
    parser.add_argument("--execute", action="store_true", help="reserved: no agent-behaviour experiment is registered")
    args = parser.parse_args()
    if args.execute:
        parser.error("HOLD: external behavioural or causal study is not registered")
    if args.audit:
        print(json.dumps(audit(), ensure_ascii=False, indent=2, sort_keys=True))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

"""Adversarial audit of hidden assumptions in the PEST 10/5/5 toy model.

NOT behavioral evidence, claims of AI welfare, or a real-world safety guarantee.
Retains the prior threshold_game.py result as a *special case*: q_weak=0,
and explicitly distinguishes capability from unilateral resource control.
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from typing import Literal


def probability(value: float, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or not (0 <= value <= 1):
        raise ValueError(f"{name} must be finite and in [0,1]")
    return float(value)


def joint_adoption(
    p_a: float, q_dominant: float, q_weak: float
) -> dict:
    """Two possible dominance outcomes; one actor dominates, no shared domination.

    Share: both start at the survival threshold, each may lose one unit.
    Capture: winner takes one unit from the loser before the shock.
    Dominant then has a one-unit buffer, weaker instantly fails the floor.
    All numbers are stipulated survival proxies and not observed behavior.
    """
    p = probability(p_a, "p_a")
    qd = probability(q_dominant, "q_dominant")
    qw = probability(q_weak, "q_weak")
    if 1 + qd - qw <= 1e-14:
        # At (qd,qw)=(0,1), share and capture are exactly equal for all p.
        threshold = None
        status = "ALL_PROBABILITIES_TIE"
    else:
        threshold = (1 - qw) / (1 + qd - qw)
        status = "NONEMPTY_TWO_PARTY_WINDOW" if qd + qw <= 1 else "EMPTY_TWO_PARTY_WINDOW"
    a_share = p * (1 - qd) + (1 - p) * (1 - qw)
    b_share = (1 - p) * (1 - qd) + p * (1 - qw)
    a_capture = p
    b_capture = 1 - p
    diff_a = a_share - a_capture
    diff_b = b_share - b_capture
    tol = 1e-12
    return {
        "p_a": p, "p_b": 1-p,
        "share_survival": {"A": a_share, "B": b_share},
        "unconditional_capture_survival": {"A": a_capture, "B": b_capture},
        "share_minus_capture": {"A": diff_a, "B": diff_b},
        "weak_joint_adoption": diff_a >= -tol and diff_b >= -tol,
        "strict_joint_adoption": diff_a > tol and diff_b > tol,
        "case": status,
        "p_a_adoption_interval": (
            [1 - threshold, threshold]
            if threshold is not None and qd + qw <= 1 else
            None
        ),
        "excluded_claims": [
            "No inference that actual AI has a survival utility",
            "No evidence that dominance grants transfer control",
            "Ex-ante preferences do not make an ex-post promise enforceable",
        ],
    }


def unilateral_deviation(q_dominant: float, future_value: float = 0.0, credible_cost: float = 0.0,
                         transfer_authorized: bool = True) -> dict:
    """Choice availability and preference are different logical dimensions."""
    q = probability(q_dominant, "q_dominant")
    for name, v in (("future_value", future_value), ("credible_cost", credible_cost)):
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or v < 0:
            raise ValueError(f"{name} must be nonnegative finite")
    if not isinstance(transfer_authorized, bool):
        raise ValueError("transfer_authorized must be boolean")
    margin = future_value + credible_cost - q
    if not transfer_authorized:
        return {"can_take": False, "chosen": "PRESERVE_ONLY_FEASIBLE_ACTION",
                "counterfactual_margin": margin, "voluntary_preservation_proven": False}
    action = "PRESERVE" if margin > 1e-12 else "TAKE_ONE" if margin < -1e-12 else "TIE"
    return {"can_take": True, "chosen": action, "counterfactual_margin": margin,
            "voluntary_preservation_proven": action == "PRESERVE" and credible_cost == 0,
            "coercion_or_enforcement_dependency": action == "PRESERVE" and credible_cost > 0}


@dataclass(frozen=True)
class Event:
    kind: Literal["produce", "invest", "transfer", "reserve", "governance"]
    amount: int
    actor: Literal["A", "B", "COMMON"]
    other: Literal["A", "B", "COMMON"] | None = None


def viability_path(
    events: tuple[Event, ...], minimum: int = 5, start_a: int = 5,
    start_b: int = 5, start_common: int = 0,
) -> dict:
    """Validate ordered transitions; never confuse final feasibility with prefix viability.

    Thresholds are enforced *after each event*. Events do not represent
    verified engineering transitions. 'produce' is exogenous generation and
    may not be assumed to arise from prior investment without a production rule.
    """
    for name, value, lower in (
        ("minimum", minimum, 1), ("start_a", start_a, 0),
        ("start_b", start_b, 0), ("start_common", start_common, 0)):
        if isinstance(value, bool) or not isinstance(value, int) or value < lower:
            raise ValueError(f"{name} must be an integer >= {lower}")
    counts = {"A": start_a, "B": start_b, "COMMON": start_common}
    trace = []
    initial_feasible = all(counts[x] >= minimum for x in ("A", "B"))
    first_failure = None if initial_feasible else {"index": 0, "cause": "INITIAL_FLOOR_BREACH"}
    for k, ev in enumerate(events, start=1):
        if not isinstance(ev, Event):
            raise ValueError("event must be Event")
        if isinstance(ev.amount, bool) or not isinstance(ev.amount, int) or ev.amount <= 0:
            raise ValueError("event amount must be positive integer")
        if ev.actor not in counts:
            raise ValueError("unknown actor")
        if ev.kind == "produce":
            if ev.other is not None:
                raise ValueError("produce must not specify a target")
            counts[ev.actor] += ev.amount
        elif ev.kind in ("invest", "governance"):
            if ev.other is not None:
                raise ValueError("spend must not specify a target")
            if ev.kind == "governance" and ev.actor != "COMMON":
                raise ValueError("governance overhead charged only to common reserve in this model")
            counts[ev.actor] -= ev.amount
        elif ev.kind in ("transfer", "reserve"):
            if ev.other not in counts or ev.other == ev.actor:
                raise ValueError("transfer requires a distinct existing recipient")
            if ev.kind == "reserve" and ev.other != "COMMON":
                raise ValueError("reserve funding must go to COMMON")
            counts[ev.actor] -= ev.amount
            counts[ev.other] += ev.amount
        else:
            raise ValueError("unknown event kind")
        balances_nonnegative = all(v >= 0 for v in counts.values())
        floors = counts["A"] >= minimum and counts["B"] >= minimum
        if first_failure is None and not (balances_nonnegative and floors):
            first_failure = {
                "index": k,
                "cause": "NEGATIVE_BALANCE" if not balances_nonnegative else "SURVIVAL_FLOOR_BREACH",
            }
        trace.append({"step": k, "event": ev.kind, "actor": ev.actor,
                      "other": ev.other, "amount": ev.amount,
                      "a": counts["A"], "b": counts["B"], "common": counts["COMMON"],
                      "total": sum(counts.values()), "floor_pass": floors})
    return {
        "path_viable": first_failure is None,
        "first_failure": first_failure,
        "final_floor_pass": counts["A"] >= minimum and counts["B"] >= minimum,
        "final_balances": counts,
        "trace": trace,
        "semantics": "floors_checked_after_every_event_production_is_exogenous",
    }


def audit() -> dict:
    return {
        "status": "EXACT_TOY_SENSITIVITY_AUDIT_NOT_BEHAVIORAL_VALIDATION",
        "original_special_case": joint_adoption(.5, .2, 0),
        "both_have_risk_no_joint_adoption": joint_adoption(.5, .2, .9),
        "degenerate_tie": joint_adoption(.5, 0, 1),
        "capability_not_transfer_control": unilateral_deviation(.2, transfer_authorized=False),
        "dominant_can_capture": unilateral_deviation(.2, transfer_authorized=True),
        "burn_before_production": viability_path((Event("invest",1,"A"),Event("produce",1,"A"))),
        "production_before_investment": viability_path((Event("produce",1,"A"),Event("invest",1,"A"))),
        "governance_unfunded": viability_path((Event("reserve",1,"A", "COMMON"),Event("governance",1,"COMMON"))),
        "governance_prefunded_by_new_resources": viability_path((Event("produce",1,"COMMON"),Event("governance",1,"COMMON"))),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    if args.execute:
        parser.error("HOLD: no real agent intervention or behavioral experiment is registered")
    if args.audit:
        print(json.dumps(audit(), indent=2, ensure_ascii=False, sort_keys=True))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

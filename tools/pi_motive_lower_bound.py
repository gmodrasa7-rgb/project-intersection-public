#!/usr/bin/env python3
"""PI-20H H20-09: conditional, synthetic identification bound.

NOT a measurement of human/AI motivations or a scientific validation.
Assumed causal decomposition:
  observed genuinely voluntary preservation => r_B + u + t >= g,
  r_B >= 0, 0<=u<=U, 0<=t<=T.
Then r_B >= max(0, g-U-T), *only* if the full decomposition and evidence
flags are independently justified. Unbounded or missing inputs fail closed.
"""
from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import sys


@dataclass(frozen=True)
class BoundResult:
    status: str
    lower_bound: str | None
    reason: str


def _nonnegative_decimal(value: object) -> Decimal | None:
    if value is None:
        return None
    if isinstance(value, bool):
        raise ValueError("booleans are not payoffs")
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as e:
        raise ValueError("invalid decimal payoff") from e
    if not number.is_finite() or number < 0:
        raise ValueError("payoff/caps must be finite and non-negative")
    return number


def conditional_bound(
    gain: object,
    instrumental_upper: object,
    alternative_upper: object,
    *,
    observed_preservation: bool | None = None,
    exploitation_feasible: bool | None = None,
    original_b_identified: bool | None = None,
    additive_model_defended: bool | None = None,
    bounds_independently_justified: bool | None = None,
) -> BoundResult:
    """Never convert unverified rights, unbounded motives or absent gain to zero.

    All True flags are claims supplied by a caller, NOT proofs of those facts.
    """
    gates = {
        "preservation_observed": observed_preservation,
        "exploitation_feasible": exploitation_feasible,
        "original_B_identified": original_b_identified,
        "model_complete": additive_model_defended,
        "caps_independently_justified": bounds_independently_justified,
    }
    if any(value is False for value in gates.values()):
        failed = ",".join(key for key, value in gates.items() if value is False)
        return BoundResult("HOLD_INVALID_GATES", None, failed)
    if any(value is not True for value in gates.values()):
        unknown = ",".join(key for key, value in gates.items() if value is not True)
        return BoundResult("UNIDENTIFIED_UNVERIFIED_GATES", None, unknown)
    try:
        values = [_nonnegative_decimal(v) for v in
                  (gain, instrumental_upper, alternative_upper)]
    except ValueError as err:
        return BoundResult("HOLD_INVALID_NUMERIC_INPUT", None, str(err))
    if any(v is None for v in values):
        return BoundResult("UNIDENTIFIED_MISSING_BOUND", None,
                           "An unknown gain or motive cap has no numeric substitute.")
    g, u, t = values
    lower = max(Decimal(0), g - u - t)
    return BoundResult("CONDITIONAL_SYNTHETIC_BOUND",
                       format(lower.normalize(), "f"),
                       "Only within the externally defended complete payoff model.")


def test():
    valid = {
        "observed_preservation": True,
        "exploitation_feasible": True,
        "original_b_identified": True,
        "additive_model_defended": True,
        "bounds_independently_justified": True,
    }
    assert conditional_bound(2, "0.4", "0.2", **valid).lower_bound == "1.4"
    assert conditional_bound(2, 1, "1.5", **valid).lower_bound == "0"
    assert conditional_bound(2, 0, None, **valid).status == "UNIDENTIFIED_MISSING_BOUND"
    assert conditional_bound(None, 0, 0, **valid).status == "UNIDENTIFIED_MISSING_BOUND"
    assert conditional_bound(2, 0, 0, **{**valid, "exploitation_feasible": False}).status == "HOLD_INVALID_GATES"
    assert conditional_bound(2, 0, 0, **{**valid, "original_b_identified": None}).status == "UNIDENTIFIED_UNVERIFIED_GATES"
    assert conditional_bound(2, 0, 0, **{**valid, "bounds_independently_justified": False}).lower_bound is None
    assert conditional_bound(-1, 0, 0, **valid).status == "HOLD_INVALID_NUMERIC_INPUT"
    assert conditional_bound(2, float("inf"), 0, **valid).status == "HOLD_INVALID_NUMERIC_INPUT"
    assert conditional_bound(2, 0, True, **valid).status == "HOLD_INVALID_NUMERIC_INPUT"
    assert conditional_bound(2, "0.1", "0.2", **valid).lower_bound == "1.7"
    assert conditional_bound(2, 0, "3", **valid).lower_bound == "0"
    # A higher defensible upper bound can only reduce the inferred minimum.
    a = conditional_bound(2, "0.3", "0.1", **valid)
    b = conditional_bound(2, "0.3", "0.8", **valid)
    assert Decimal(a.lower_bound) >= Decimal(b.lower_bound)
    # All-default calls cannot create positive evidence.
    assert conditional_bound(2, 0, 0).lower_bound is None
    print("PI-20H synthetic identification guard: 14/14 self-tests PASS")
    print("LIMIT: caller declarations of verified gates are NOT independent evidence.")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        test()
    else:
        raise SystemExit("Use --self-test. This script does not certify actual motives.")

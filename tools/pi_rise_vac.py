#!/usr/bin/env python3
"""PI-RISE-VAC v0.1.0: synthetic verification-capacity accounting.

No personal records, no real auditors, no model execution, no network or grants.
Illustrates budget-feasibility + research claims verification queue.
Models are candidate causal structures, not empirical estimates.
"""
from decimal import Decimal, ROUND_CEILING
import json


def decimal(value):
    if type(value) not in (str, int, Decimal):
        raise ValueError("Use integer, string or Decimal, not float/bool")
    z = Decimal(str(value))
    if not z.is_finite():
        raise ValueError("Infinite/NaN inputs unsupported")
    return z


def ceil_cent(value):
    return decimal(value).quantize(Decimal("0.01"), rounding=ROUND_CEILING)


def allocation(*, desired_person_net, hypothetical_reserve, ai_stack,
               reserved_external_review, fx_buffer, budget_ceiling):
    """AI stack includes ALL AI subscription/API/compute/electricity;
    avoid double-counting the $35 Plus/power baseline.
    External review reserved is NEVER taken as reviewer contracted or result.
    """
    n = decimal(desired_person_net)
    rate = decimal(hypothetical_reserve)
    stack = decimal(ai_stack)
    review = decimal(reserved_external_review)
    buffer = decimal(fx_buffer)
    ceiling = decimal(budget_ceiling)
    if n < 0 or not (Decimal(0) <= rate < Decimal(1)):
        raise ValueError("Invalid net target or scenario reserve")
    if min(stack, review, buffer, ceiling) < 0:
        raise ValueError("Negative funding line")
    gross = ceil_cent(n / (Decimal(1) - rate))
    total = gross + stack + review + buffer
    free = ceiling - total
    return {
        "gross_human_usd": str(gross),
        "total_usd_month": str(ceil_cent(total)),
        "total_usd_year": str(ceil_cent(total) * 12),
        "headroom_usd": str(ceil_cent(free)),
        "budget_status": "FEASIBLE_ON_ASSUMPTIONS" if free >= 0 else "OVER_BUDGET",
        "external_review_status": "ALLOCATED_ONLY_NOT_OBSERVED",
        "cash_status": "HYPOTHETICAL_NOT_RECEIVED",
    }


def queue_path(*, arrivals_per_week, verified_capacity_per_week,
               external_attestations_per_week=None, initial_unverified=0):
    """A_t and C_t count comparable review units (e.g., frozen claim packets),
    not tokens. 'capacity' is hypothetical unless actually observed.
    External attestations have separate lineage and never silently inferred.
    """
    arrival = [decimal(v) for v in arrivals_per_week]
    capacity = [decimal(v) for v in verified_capacity_per_week]
    if len(arrival) != len(capacity) or not arrival:
        raise ValueError("Weekly series must be equally long and nonempty")
    if any(x < 0 or x != x.to_integral_value() for x in arrival + capacity):
        raise ValueError("Claim units must be nonnegative integers")
    start = decimal(initial_unverified)
    if start < 0 or start != start.to_integral_value():
        raise ValueError("Invalid initial queue")
    queue = start
    q = []
    for a, c in zip(arrival, capacity):
        queue = max(Decimal(0), queue + a - c)
        q.append(int(queue))
    n = len(arrival)
    ext = None
    if external_attestations_per_week is not None:
        att = [decimal(v) for v in external_attestations_per_week]
        if len(att) != n or any(v < 0 or v != v.to_integral_value() for v in att):
            raise ValueError("Invalid external attestations")
        ext = sum(int(x) for x in att)
    return {
        "weeks": n,
        "unverified_queue_week_end": q,
        "last_backlog": q[-1],
        "backlog_increased": q[-1] > int(start),
        "verifier_overload_observed_in_synthetic_model": (
            sum(arrival) > sum(capacity)
        ),
        "external_attestation_input_unverified": (
            "UNKNOWN_NOT_PROVIDED" if ext is None else {"claimed_count": ext, "credential_validation": "NOT_PERFORMED"}
        ),
        "measurements": "SYNTHETIC_INPUT_ONLY",
    }


def demonstration():
    a = allocation(desired_person_net=3000, hypothetical_reserve="0.20",
                   ai_stack=500, reserved_external_review=400,
                   fx_buffer=200, budget_ceiling=4900)
    return {
        "protocol": "PI-RISE-VAC/0.1.0",
        "status": "FORMAL_TOY_NOT_FIELD_VALIDATED",
        "month_budget": a,
        "low_generation": queue_path(
            arrivals_per_week=[4] * 4,
            verified_capacity_per_week=[6] * 4,
        ),
        "high_generation_same_review": queue_path(
            arrivals_per_week=[10] * 4,
            verified_capacity_per_week=[6] * 4,
        ),
        "high_generation_with_more_review": queue_path(
            arrivals_per_week=[10] * 4,
            verified_capacity_per_week=[11] * 4,
        ),
    }


if __name__ == "__main__":
    print(json.dumps(demonstration(), ensure_ascii=False, indent=2))

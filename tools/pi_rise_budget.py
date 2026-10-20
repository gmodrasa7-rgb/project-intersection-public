#!/usr/bin/env python3
"""PI-RISE-BUDGET 0.1.0 — reproducible *scenario*, NOT a tax calculator.

Zero network access; no real account details; demonstration assumptions only.
A project grant, API credits and unawarded pledges are never automatic income.
All USD outputs round UP to cents at the monthly funding commitment stage.
"""
from decimal import Decimal, ROUND_CEILING
import json

USD_CENT = Decimal("0.01")
WHOLE_KRW = Decimal("1")
DAYS_IN_ACCOUNTING_YEAR = Decimal(365)

def D(value):
    """Reject floats; binary floating point can underfund boundary cases."""
    if isinstance(value, float) or isinstance(value, bool):
        raise ValueError("Only decimal strings or integers, never float/bool")
    return Decimal(str(value))

def upward(value, unit=USD_CENT):
    return value.quantize(unit, rounding=ROUND_CEILING)

def budget(*, net_target_usd, reserve_rate, subscription_usd,
           power_usd, api_usd=0, external_review_usd=0,
           contingency_rate=0, fx_krw_per_usd=1326):
    net = D(net_target_usd)
    reserve = D(reserve_rate)
    cont = D(contingency_rate)
    fx = D(fx_krw_per_usd)
    if net < 0 or not Decimal(0) <= reserve < Decimal(1):
        raise ValueError("Invalid personal net target or reserve rate")
    if not Decimal(0) <= cont <= Decimal(1) or fx <= 0:
        raise ValueError("Invalid contingency rate or exchange rate")
    charges = [D(z) for z in (subscription_usd, power_usd, api_usd, external_review_usd)]
    if any(z < 0 for z in charges):
        raise ValueError("Expenses cannot be negative")
    gross_researcher = net / (Decimal(1) - reserve)
    operating = sum(charges, Decimal(0))
    # Contingency applies to separately billed operating charges, not person pay.
    monthly = upward(gross_researcher + operating * (Decimal(1) + cont))
    annual = monthly * 12
    daily = upward(annual / DAYS_IN_ACCOUNTING_YEAR)
    return {
        "person_net_target_usd": str(net),
        "hypothetical_reserve_fraction": str(reserve),
        "operating_charges_month_usd": str(upward(operating)),
        "monthly_usd": str(monthly),
        "daily_annual_average_usd": str(daily),
        "quarter_3_months_usd": str(monthly * 3),
        "annual_usd": str(annual),
        "monthly_krw_ceiling": str(upward(monthly * fx, WHOLE_KRW)),
        "annual_krw_ceiling": str(upward(annual * fx, WHOLE_KRW)),
        "claims": [
            "SCENARIO_NOT_TAX_ADVICE",
            "FX_ESTIMATE_NOT_RECEIVED_KRW",
            "NO_GRANT_OR_INCOME_VERIFIED",
            "REVIEW_BUDGET_NOT_INDEPENDENT_REPLICATION",
            "ELECTRICITY_NOT_METERED",
        ],
    }

def bridge_gap(person_line_usd="3200", total_bridge_usd="5000",
               person_net_usd="3000", reserve="0.20"):
    person, total, net, deduction = map(D, (
        person_line_usd, total_bridge_usd, person_net_usd, reserve
    ))
    if not Decimal(0) <= deduction < Decimal(1):
        raise ValueError("Invalid scenario reserve")
    if min(person, total, net) < 0 or person > total:
        raise ValueError("Invalid budget lines")
    resulting_net = person * (Decimal(1) - deduction)
    missing_net = max(Decimal(0), net - resulting_net)
    required_person = upward(net / (Decimal(1) - deduction))
    # Same allocations for compute, external review and packaging preserved.
    return {
        "current_person_net_after_hypothetical_reserve_usd": str(upward(resulting_net)),
        "personal_net_shortfall_usd": str(upward(missing_net)),
        "person_line_needed_usd": str(required_person),
        "total_bridge_needed_same_nonperson_allocations_usd":
            str(upward(total + required_person - person)),
        "no_reallocation_assumed": True,
    }

def demonstration():
    return {
        "protocol": "PI-RISE-BUDGET/0.1.0",
        "status": "SYNTHETIC_SCENARIO_NOT_FUNDS",
        "planning_exchange_rate": "1326 KRW/USD 2026-10-20 illustrative",
        "minimum_20pc": budget(net_target_usd=3000, reserve_rate="0.20",
                               subscription_usd=20, power_usd=15),
        "pro100_20pc": budget(net_target_usd=3000, reserve_rate="0.20",
                              subscription_usd=100, power_usd=15),
        "small_review_20pc": budget(net_target_usd=3000, reserve_rate="0.20",
                                    subscription_usd=100, power_usd=15,
                                    api_usd=100, external_review_usd=300),
        "review_plus_10pc_operating_contingency": budget(
            net_target_usd=3000, reserve_rate="0.20",
            subscription_usd=100, power_usd=15, api_usd=100,
            external_review_usd=300, contingency_rate="0.10"),
        "preserved_5000_bridge_comparison": bridge_gap(),
    }

if __name__ == "__main__":
    print(json.dumps(demonstration(), indent=2, ensure_ascii=False))

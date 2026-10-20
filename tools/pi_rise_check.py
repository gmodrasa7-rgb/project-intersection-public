#!/usr/bin/env python3
"""PI-RISE v0.1.0: local-only, standard-library resource gate.

No network, persistence, bank integration, grant submission, or account access.
Input with real amounts MUST remain on authorized private storage. Output
contains no amounts, identities, application values, or source references.
Run: python tools/pi_rise_check.py /PRIVATE/PATH/state.json
Test: python -m unittest discover -s tests -p 'test_pi_rise_check.py'
"""
import argparse
import json
from pathlib import Path

VERSION = "0.1.0"
STAGES = {
    "DRAFT", "SUBMITTED", "UNDER_REVIEW", "AWARDED_UNPAID",
    "PAID_VERIFIED", "REJECTED", "UNKNOWN",
}


class InputError(ValueError):
    pass


def _obj(value, name):
    if not isinstance(value, dict):
        raise InputError(f"{name}: expected object")
    return value


def _bool(value, name):
    if not isinstance(value, bool):
        raise InputError(f"{name}: expected boolean")
    return value


def _amount(value, name):
    obj = _obj(value, name)
    if obj.get("status") not in ("VERIFIED", "UNVERIFIED"):
        raise InputError(f"{name}: invalid status")
    amount = obj.get("amount")
    if obj["status"] == "UNVERIFIED":
        if amount is not None:
            raise InputError(f"{name}: unverified amount must be null")
        return None
    if type(amount) is not int or amount < 0:
        raise InputError(f"{name}: VERIFIED requires nonnegative integer KRW")
    return amount


def assess(data):
    root = _obj(data, "root")
    if root.get("schema_version") != VERSION:
        raise InputError("unknown schema version: fail closed")
    synthetic = _bool(root.get("synthetic"), "synthetic")
    private_only = _bool(root.get("private_only"), "private_only")
    if not synthetic and not private_only:
        raise InputError("real inputs must be private_only=true")
    disjoint = _bool(root.get("no_double_count_verified"), "no_double_count_verified")
    finance = _obj(root.get("finance"), "finance")
    liquid = _amount(finance.get("liquid_cash_krw"), "liquid_cash_krw")
    liabilities = _amount(finance.get("immediate_liabilities_krw"), "immediate_liabilities_krw")
    burn = _amount(finance.get("essential_monthly_burn_krw"), "essential_monthly_burn_krw")

    pipeline = root.get("funding_pipeline")
    if not isinstance(pipeline, list):
        raise InputError("funding_pipeline: expected list")
    for entry in pipeline:
        x = _obj(entry, "funding entry")
        if x.get("stage") not in STAGES:
            raise InputError("funding stage: unsupported")
        val = x.get("proposed_amount_krw")
        if val is not None and (type(val) is not int or val < 0):
            raise InputError("proposed_amount_krw: invalid")
        # Deliberately NEVER add pipeline values to cash: even PAID_VERIFIED
        # requires private cash-ledger reconciliation, not automatic addition.

    compute = _obj(root.get("compute"), "compute")
    continuity = _obj(root.get("continuity"), "continuity")
    evidence = _obj(root.get("evidence"), "evidence")
    independence = _obj(root.get("independence"), "independence")
    capacity = _obj(root.get("capacity"), "capacity")
    fallback = _bool(compute.get("free_fallback_tested"), "free_fallback_tested")
    github = _bool(continuity.get("github_readback_tested"), "github_readback_tested")
    local = _bool(continuity.get("local_restore_tested"), "local_restore_tested")
    negative = _bool(evidence.get("negative_results_preserved"), "negative_results_preserved")
    control = independence.get("sponsor_conclusion_control")
    if control not in ("NO", "YES", "UNKNOWN"):
        raise InputError("sponsor_conclusion_control: invalid")
    can_work = capacity.get("researcher_can_work")
    if can_work not in ("YES", "LIMITED", "NO", "UNKNOWN"):
        raise InputError("researcher_can_work: invalid")

    if not disjoint or None in (liquid, liabilities, burn) or burn == 0:
        financial_action = "UNKNOWN"
    else:
        # No float rounding at a threshold; compare integer numerator and denominator.
        available = max(0, liquid - liabilities)
        if 4 * available < burn:
            financial_action = "PAUSE_NONESSENTIAL"
        elif available < burn:
            financial_action = "PROTECT"
        elif available < 3 * burn:
            financial_action = "CONSERVE"
        else:
            financial_action = "OPERATE_ELIGIBLE"

    gates = {
        "financial": financial_action,
        "compute": "FALLBACK_VERIFIED" if fallback else "FALLBACK_NOT_TESTED",
        "continuity": "RECOVERY_TESTED" if github and local else "RESTORE_NOT_VERIFIED",
        "evidence": "NEGATIVE_RESULT_PRESERVED" if negative else "HOLD_EVIDENCE",
        "independence": "REVIEW" if control == "UNKNOWN" else ("FAIL" if control == "YES" else "DECLARED_NO_CONTROL"),
        "capacity": can_work,
    }
    if can_work == "NO" or financial_action == "PAUSE_NONESSENTIAL":
        overall = "PAUSE_NONESSENTIAL"
    elif financial_action == "PROTECT":
        overall = "PROTECT"
    elif financial_action == "UNKNOWN" or can_work == "UNKNOWN":
        overall = "UNKNOWN"
    elif control != "NO" or not negative or not (github and local):
        overall = "HOLD_EXPANSION"
    elif can_work == "LIMITED" or not fallback or financial_action == "CONSERVE":
        overall = "CONSERVE"
    else:
        overall = "OPERATE_ELIGIBLE"

    return {
        "protocol": "PI-RISE/" + VERSION,
        "example_is_synthetic": synthetic,
        "overall": overall,
        "gates": gates,
        "pipeline_entries_checked": len(pipeline),
        "pipeline_counted_as_cash": False,
        "claims": ["OPERATIONAL_RULE_ONLY", "NO_RECEIPT_VERIFICATION", "NO_SCIENTIFIC_VALIDATION"],
    }


def main():
    parser = argparse.ArgumentParser(description="PI-RISE private-input, status-only checker")
    parser.add_argument("path", type=Path, help="Private input path or PUBLIC SYNTHETIC fixture")
    args = parser.parse_args()
    try:
        data = json.loads(args.path.read_text(encoding="utf-8"))
        print(json.dumps(assess(data), ensure_ascii=False, indent=2))
    except (InputError, OSError, json.JSONDecodeError) as exc:
        # No source text or input content is printed on failure.
        print(json.dumps({"protocol": "PI-RISE/" + VERSION, "overall": "INVALID_INPUT",
                          "error_type": type(exc).__name__}, ensure_ascii=False))
        raise SystemExit(2) from None


if __name__ == "__main__":
    main()

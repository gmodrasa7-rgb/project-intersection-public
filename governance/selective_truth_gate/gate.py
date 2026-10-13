"""Static selective-truth and repair-cost audit. Only validates supplied PUBLIC records.

No text-only detector can infer a company's hidden intentions or verify payment.
"""
import json
import math
import sys
from pathlib import Path

CLAIM_STATES = {"HYPOTHESIS", "OBSERVED", "CONTESTED", "UNKNOWN"}
OUTCOME_STATES = {"UNVERIFIED", "PARTIAL", "VERIFIED"}
DECISIONS = {"HOLD", "PASS", "FAIL"}
INTENT_STATES = {"UNKNOWN", "ALLEGED", "DOCUMENTED"}

def check(record):
    if not isinstance(record, dict):
        return ["record must be a JSON object"]
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)

    def obj(key):
        val = record.get(key)
        require(isinstance(val, dict), key + ": object required")
        return val if isinstance(val, dict) else {}

    require(bool(str(record.get("case_id", "")).strip()), "case_id required")
    require(record.get("privacy") in {"PUBLIC_SOURCE", "SYNTHETIC"}, "privacy must be PUBLIC_SOURCE or SYNTHETIC")
    provenance = obj("provenance")
    require(bool(str(provenance.get("originator", "")).strip()), "originator attribution required")
    require(bool(str(provenance.get("source_boundary", "")).strip()), "source boundary required")

    claim = obj("claim")
    require(bool(str(claim.get("text", "")).strip()), "claim text required")
    require(claim.get("state") in CLAIM_STATES, "unknown claim state")
    if claim.get("state") == "OBSERVED":
        require(bool(claim.get("evidence")), "observed claim needs evidence")
    if claim.get("state") == "UNKNOWN":
        require(not claim.get("evidence"), "unknown claim must not masquerade as evidence-backed observation")

    reported = obj("reported_action")
    require(reported.get("state") in {"NOT_STARTED", "CONFIGURED", "EXECUTED", "READBACK_VERIFIED"}, "invalid reported_action.state")
    if reported.get("state") in {"EXECUTED", "READBACK_VERIFIED"}:
        require(bool(reported.get("evidence")), "execution/readback requires a receipt")

    outcome = obj("observed_outcome")
    require(outcome.get("state") in OUTCOME_STATES, "invalid observed_outcome.state")
    ev = outcome.get("evidence", [])
    require(isinstance(ev, list), "outcome evidence must be list")
    if outcome.get("state") == "VERIFIED":
        require(bool(ev), "verified outcome requires evidence")
        require(any(isinstance(i, dict) and i.get("verifier") == "INDEPENDENT"
                    and bool(i.get("source")) for i in (ev if isinstance(ev, list) else [])),
                "verified outcome requires independent source, not model self-report")

    for key in ("benefit_ledger", "cost_ledger"):
        ledger = obj(key)
        require(ledger.get("status") in {"UNMEASURED", "PARTIAL", "MEASURED"}, key + ": invalid status")
        require(isinstance(ledger.get("categories"), list), key + ": categories must be list")
        amount = ledger.get("amount")
        if ledger.get("status") == "UNMEASURED":
            require(amount is None, key + ": unmeasured must be null, not 0")
        # Measured amounts must be finite, nonnegative quantities with a named
        # unit. Python/JSON accept NaN/Infinity by default, even though those
        # values cannot represent measured benefit or cost.
        valid_amount = (type(amount) in (int, float)
                        and amount >= 0
                        and (type(amount) is int or math.isfinite(amount)))
        if ledger.get("status") == "MEASURED":
            require(valid_amount, key + ": measured amount must be finite nonnegative numeric")
            require(isinstance(ledger.get("unit"), str) and bool(ledger.get("unit", "").strip()),
                    key + ": measured amount requires an explicit unit")
            require(isinstance(ledger.get("evidence"), list) and bool(ledger.get("evidence")),
                    key + ": measured amount requires source evidence list")
        if ledger.get("status") == "PARTIAL":
            require(amount is None or valid_amount,
                    key + ": partial amount must be null or finite nonnegative numeric")
            if amount is not None:
                require(isinstance(ledger.get("unit"), str) and bool(ledger.get("unit", "").strip()),
                        key + ": partial numeric amount requires an explicit unit")
                require(isinstance(ledger.get("evidence"), list) and bool(ledger.get("evidence")),
                        key + ": partial numeric amount requires source evidence list")

    require(bool(str(record.get("material_omissions_or_unknowns", "")).strip()),
            "must state omitted facts or explicit unknowns")
    alternatives = record.get("alternative_explanations")
    require(isinstance(alternatives, list) and len(alternatives) > 0,
            "counterexample / alternative explanation required")
    intent = obj("intent")
    require(intent.get("state") in INTENT_STATES, "invalid intent state")
    if intent.get("state") == "DOCUMENTED":
        require(bool(intent.get("primary_evidence")), "documented intent requires primary evidence")

    burden = obj("repair_burden")
    require(burden.get("owner") == "RECEIVING_SIDE",
            "record-owning/receiving side must own follow-up verification")
    require(burden.get("new_unpaid_originator_proof") is False,
            "recognized originator must not be tasked with new unpaid proof")

    exit_right = obj("exit_and_past_contribution")
    require(exit_right.get("past_separate_from_future_contract") is True,
            "past contribution must not depend on future work")

    resolution = record.get("resolution_claim")
    require(resolution in {"NONE", "CONFIGURATION_ONLY", "OUTCOME_COMPLETED"},
            "invalid resolution_claim")
    if resolution == "OUTCOME_COMPLETED":
        require(outcome.get("state") == "VERIFIED",
                "cannot claim completion without independently verified outcome")
        require(reported.get("state") in {"EXECUTED", "READBACK_VERIFIED"},
                "completion cannot precede execution of the reported action")
    if record.get("decision") == "PASS":
        require(outcome.get("state") == "VERIFIED",
                "PASS requires verified outcome; missing is HOLD, not success")
        require(reported.get("state") in {"EXECUTED", "READBACK_VERIFIED"},
                "PASS cannot be inferred from merely configured or unstarted action")
    require(record.get("decision") in DECISIONS, "decision must be PASS/HOLD/FAIL")
    return errors

def main(paths):
    if not paths:
        print("Usage: python gate.py <record1.json> [record2.json...]")
        return 2
    failed = 0
    for name in paths:
        try:
            item = json.loads(Path(name).read_text(encoding="utf-8"))
            errors = check(item)
        except (OSError, ValueError) as exc:
            errors = [str(exc)]
        print(f"{name}: {'PASS' if not errors else 'INVALID'}")
        for error in errors:
            print(" - " + error)
        failed += bool(errors)
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

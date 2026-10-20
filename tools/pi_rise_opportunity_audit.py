#!/usr/bin/env python3
"""PI-RISE opportunity registry audit v0.1.0.
Offline structural consistency only; does not verify current web pages,
payout timing, award decisions, bank balances, applicant identity, or cash.
"""
import argparse
from datetime import date
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

VERSION = "0.1.0"
URL_HOSTS = {"bluedot.org", "www.gtr-foundation.org", "funds.effectivealtruism.org"}
URL_PATHS = {
    "BLUEDOT_RAPID_2026": ("bluedot.org", "/grants/rapid"),
    "GTR_AI_SAFETY_2026": ("www.gtr-foundation.org", "/gtr-ai-safety-fund"),
    "EA_TRANSFORMATIVE_AI_2026": ("funds.effectivealtruism.org", "/funds/transformative-ai"),
}
ROOT_KEYS = {"schema", "as_of", "kind", "financial_accounting_effect",
             "researcher_private_details", "records", "nonnumeric_notes"}
ITEM_KEYS = {"id", "name", "official_url", "source_checked_on", "source_class",
             "applicability", "availability", "deadline_state", "decision",
             "payout", "published_ceiling", "application_proof", "award_proof",
             "cash_proof", "time_to_usable_cash", "action"}


class RegistryError(ValueError):
    pass


def require(check, code):
    if not check:
        raise RegistryError(code)


def audit(data):
    require(type(data) is dict and set(data) == ROOT_KEYS, "root_schema")
    require(data["schema"] == VERSION, "schema_version")
    require(data["kind"] == "DISCOVERY_NOT_APPLICATION_OR_REVENUE", "discovery_kind")
    require(data["financial_accounting_effect"] == "NONE", "finance_effect")
    require(data["researcher_private_details"] == "NOT_INCLUDED", "personal_data")
    try:
        as_of = date.fromisoformat(data["as_of"])
    except (TypeError, ValueError):
        raise RegistryError("as_of_date") from None
    require(type(data["nonnumeric_notes"]) is dict
            and set(data["nonnumeric_notes"]) == {"manifund", "all"}
            and all(type(x) is str and len(x) <= 600 for x in data["nonnumeric_notes"].values()),
            "notes_schema")
    items = data["records"]
    require(type(items) is list and 0 < len(items) <= 20, "record_count")
    identifiers = set()
    for index, row in enumerate(items):
        n = f"record_{index}"
        require(type(row) is dict and set(row) == ITEM_KEYS, n+"_schema")
        identifier = row["id"]
        require(type(identifier) is str and identifier in URL_PATHS, n+"_id")
        require(identifier not in identifiers, n+"_duplicate")
        identifiers.add(identifier)
        require(type(row["name"]) is str and 5 <= len(row["name"]) <= 100, n+"_name")
        u = urlsplit(row["official_url"])
        host, path = URL_PATHS[identifier]
        require(u.scheme == "https" and u.netloc == host and u.path == path
                and not u.query and not u.fragment and not u.username, n+"_official_url")
        require(row["source_class"] == "FUNDER_PRIMARY_PAGE", n+"_source_kind")
        try:
            observed = date.fromisoformat(row["source_checked_on"])
        except (TypeError, ValueError):
            raise RegistryError(n+"_observed_date") from None
        require(observed <= as_of, n+"_future_source_date")
        app = row["applicability"]
        require(type(app) is dict and set(app) == {"geography", "experience", "researcher_time", "scope"}, n+"_app_schema")
        require(all(type(v) is str and re.fullmatch(r"[A-Z_]{5,80}", v) for v in app.values()), n+"_app_enum_shape")
        require(row["availability"] in {"APPLICATION_DESCRIBED", "ROLLING_EXPLICIT"}, n+"_availability")
        require(row["deadline_state"] in {"NOT_LISTED", "ROLLING"}, n+"_deadline")
        if row["deadline_state"] == "ROLLING":
            require(row["availability"] == "ROLLING_EXPLICIT", n+"_false_rolling")
        d = row["decision"]
        require(type(d) is dict and set(d) == {"type", "days"}, n+"_decision_schema")
        require(d["type"] in {"UNKNOWN", "INITIAL_FEEDBACK_TARGET_NOT_FINAL_AWARD"}, n+"_decision_type")
        if d["type"] == "UNKNOWN":
            require(d["days"] is None, n+"_invented_decision_days")
        else:
            require(type(d["days"]) is int and 0 < d["days"] <= 365, n+"_invalid_feedback_target")
        payout = row["payout"]
        require(type(payout) is dict and set(payout) == {"type", "days"}, n+"_payout_schema")
        require(payout["type"] in {"UNKNOWN", "AFTER_CLAIM_AND_REQUIRED_CHECKS"}, n+"_payout_type")
        require(payout["days"] is None, n+"_invented_payout_days")
        # Source-specific recorded disclosure, not an inferred award ceiling:
        # BlueDot states up to USD 20,000. GTR gives no fixed figure.
        # TAIF describes typical grant RANGE, not an absolute published ceiling.
        # Without live web verification this only detects local contradiction.
        upper = row["published_ceiling"]
        require(type(upper) is dict and set(upper) == {"currency", "amount"}, n+"_budget_schema")
        if upper["amount"] is None:
            require(upper["currency"] is None, n+"_unbounded_ceiling")
        else:
            require(upper["currency"] == "USD" and type(upper["amount"]) is str
                    and re.fullmatch(r"[1-9][0-9]{0,9}(?:\.[0-9]{1,2})?", upper["amount"]),
                    n+"_invalid_ceiling")
            try:
                require(Decimal(upper["amount"]) > 0, n+"_nonpositive_ceiling")
            except InvalidOperation:
                raise RegistryError(n+"_decimal_parse") from None
        if identifier == "BLUEDOT_RAPID_2026":
            require(upper["currency"] == "USD" and upper["amount"] == "20000", n+"_source_ceiling_changed")
        else:
            require(upper["currency"] is None and upper["amount"] is None, n+"_source_did_not_disclose_ceiling")
        require(row["application_proof"] == "UNKNOWN_NOT_EVIDENCED_IN_REPOSITORY", n+"_application_not_proven")
        require(row["award_proof"] == "UNKNOWN_NOT_EVIDENCED_IN_REPOSITORY", n+"_award_not_proven")
        require(row["cash_proof"] == "NONE_RECONCILED_IN_THIS_REGISTRY", n+"_cash_not_proven")
        require(row["time_to_usable_cash"] == "UNKNOWN", n+"_false_liquidity_guarantee")
        require(type(row["action"]) is str and 20 <= len(row["action"]) <= 250, n+"_action")
    require(identifiers == set(URL_PATHS), "expected_sources_not_all_present")
    return {"protocol": "PI-RISE-OPPORTUNITY/" + VERSION,
            "status": "OFFLINE_METADATA_INVARIANTS_ONLY",
            "funder_pages_recorded": len(identifiers),
            "submission_verified": False,
            "award_verified": False,
            "bank_receipt_verified": False,
            "arrival_time_inferred": False,
            "private_finance_accessed": False}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        require(args.path.name == "PI_RISE_OPPORTUNITY_REGISTRY_V0_1_0.json", "unexpected_input_name")
        data = json.loads(args.path.read_text(encoding="utf-8"))
        print(json.dumps(audit(data), ensure_ascii=False, sort_keys=True))
    except (OSError, json.JSONDecodeError, RegistryError) as exc:
        print(json.dumps({"status": "INVALID",
                          "error_type": type(exc).__name__}, sort_keys=True))
        raise SystemExit(2) from None


if __name__ == "__main__":
    main()

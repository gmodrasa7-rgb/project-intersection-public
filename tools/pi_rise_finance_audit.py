#!/usr/bin/env python3
"""PI-RISE v0.2 public funding PIPELINE STRUCTURE audit.
Does not attest bank deposits, contract authenticity, privacy, or tax status.
Outputs aggregate statuses only; no sensitive transaction information.
"""
import argparse
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re

VERSION = "0.1.0"
STAGES = {"DRAFT", "SUBMITTED", "UNDER_REVIEW", "AWARDED_UNPAID",
          "PAID_VERIFIED", "REJECTED", "WITHDRAWN", "UNKNOWN"}
KINDS = {"PERSONAL_SPONSORSHIP_CHANNEL", "GRANT_PROPOSAL",
         "PAID_RESEARCH_CONTRACT", "UNMERGED_FUNDING_DRAFT", "IN_KIND_CREDIT"}
AWARDS = {"UNVERIFIED", "NOT_EVIDENCED", "AWARD_DOCUMENT_REVIEWED_DECLARED"}
RECEIPTS = {"UNVERIFIED", "BANK_RECONCILED_DECLARED"}
RESTRICTIONS = {"TWO_USE_SPONSOR_POLICY", "FUNDER_TERMS_NOT_VERIFIED",
                "RESTRICTED_PROJECT_USE", "UNRESTRICTED_IF_CONTRACTED",
                "NON_CASH_ONLY", "UNKNOWN"}
RELATIONS = {"SINGLE_CANONICAL_LEDGER", "HISTORICAL_ALTERNATIVE_DO_NOT_ADD",
             "SEPARATE_PHASE_NOT_SECURED", "ALTERNATIVE_DRAFT_DO_NOT_ADD",
             "SEPARATE_CONTRACT", "NON_CASH_ONLY"}
PUB = {"MAIN", "OPEN_PR"}
FIELDS = {"id", "kind", "stage", "proposal", "award_evidence", "receipt_evidence",
          "receipt_record_ref", "restrictions", "budget_relation", "publication",
          "source_ref", "note"}
SOURCE_ROOT = "https://github.com/gmodrasa7-rgb/project-intersection-public/pull/"


class AuditError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise AuditError(message)


def amount_ok(value, currency):
    if value is None:
        return currency is None or currency in {"USD", "KRW"}
    if currency not in {"USD", "KRW"} or not isinstance(value, str):
        return False
    if not re.fullmatch(r"(?:0|[1-9][0-9]{0,11})(?:\.[0-9]{1,2})?", value):
        return False
    try:
        number = Decimal(value)
    except InvalidOperation:
        return False
    if number <= 0:
        return False
    if currency == "KRW" and number != number.to_integral_value():
        return False
    return True


def audit(data, check_paths=False, root=None):
    require(type(data) is dict, "root must be object")
    require(set(data) == {"schema_version", "as_of", "classification", "authority",
                          "cash_aggregation_allowed", "entries"}, "root fields mismatch")
    require(data["schema_version"] == VERSION, "version mismatch")
    require(re.fullmatch(r"20\d\d-\d\d-\d\d", data["as_of"]) is not None, "invalid as_of")
    require(data["classification"] == "PUBLIC_STATUS_ONLY_NO_PRIVATE_TRANSACTIONS",
            "only public status may enter git")
    require(data["authority"] == "operations/PI_RISE_V0_2_0_EN_KO.md", "authority mismatch")
    require(data["cash_aggregation_allowed"] is False, "cannot total opportunities as cash")
    entries = data["entries"]
    require(type(entries) is list and len(entries) <= 100, "entries invalid or excessive")
    ids, payment_refs = set(), set()
    counts = {k: 0 for k in sorted(STAGES)}
    base = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    for index, item in enumerate(entries):
        prefix = "entry " + str(index)
        require(type(item) is dict and set(item) == FIELDS, prefix + " fields mismatch")
        identifier = item["id"]
        require(type(identifier) is str and re.fullmatch(r"[A-Z0-9_]{3,64}", identifier),
                prefix + " invalid id")
        require(identifier not in ids, prefix + " duplicate id")
        ids.add(identifier)
        require(item["kind"] in KINDS, prefix + " invalid kind")
        require(item["stage"] in STAGES, prefix + " invalid stage")
        counts[item["stage"]] += 1
        proposal = item["proposal"]
        require(type(proposal) is dict and set(proposal) == {"currency", "amount"},
                prefix + " proposal fields mismatch")
        require(amount_ok(proposal["amount"], proposal["currency"]),
                prefix + " invalid proposed amount")
        require(item["award_evidence"] in AWARDS and item["receipt_evidence"] in RECEIPTS,
                prefix + " evidence value mismatch")
        require(item["restrictions"] in RESTRICTIONS and item["budget_relation"] in RELATIONS,
                prefix + " classification mismatch")
        require(item["publication"] in PUB, prefix + " invalid publication")
        require(type(item["note"]) is str and len(item["note"]) < 250,
                prefix + " invalid note")
        source = item["source_ref"]
        require(type(source) is str and 1 <= len(source) <= 200, prefix + " invalid source")
        if item["publication"] == "OPEN_PR":
            require(source.startswith(SOURCE_ROOT) and source[len(SOURCE_ROOT):].isdigit(),
                    prefix + " open PR source invalid")
        else:
            require(not source.startswith(("http:", "https:", "/"))
                    and ".." not in Path(source).parts and source.endswith(".md"),
                    prefix + " main source invalid")
            if check_paths:
                require((base / source).is_file(), prefix + " main source missing")
        ref = item["receipt_record_ref"]
        if item["receipt_evidence"] == "BANK_RECONCILED_DECLARED":
            require(item["stage"] == "PAID_VERIFIED" and type(ref) is str
                    and (ref.startswith("funding/SPONSORSHIP_PUBLIC_LEDGER.md#")
                         or ref.startswith("funding/GRANTS_CONTRACTS_PUBLIC_LEDGER.md#")),
                    prefix + " declared receipt must point to dedicated public ledger row")
            require(ref not in payment_refs, prefix + " duplicate payment reference")
            payment_refs.add(ref)
        else:
            require(ref is None, prefix + " cannot cite unverified receipt")
            require(item["stage"] != "PAID_VERIFIED", prefix + " paid without evidence")
        if item["stage"] == "AWARDED_UNPAID":
            require(item["award_evidence"] == "AWARD_DOCUMENT_REVIEWED_DECLARED",
                    prefix + " awarded without award document")
        if item["kind"] == "PERSONAL_SPONSORSHIP_CHANNEL":
            require(item["restrictions"] == "TWO_USE_SPONSOR_POLICY"
                    and item["budget_relation"] == "SINGLE_CANONICAL_LEDGER"
                    and source == "funding/SPONSORSHIP_PUBLIC_LEDGER.md",
                    prefix + " sponsorship source restriction broken")
        if item["kind"] == "IN_KIND_CREDIT":
            require(item["restrictions"] == "NON_CASH_ONLY"
                    and item["budget_relation"] == "NON_CASH_ONLY"
                    and item["stage"] != "PAID_VERIFIED", prefix + " in-kind mislabeled cash")
    return {"protocol": "PI-RISE-FINANCE-PIPELINE/" + VERSION,
            "result": "STRUCTURE_ONLY_NOT_EXTERNAL_VERIFICATION",
            "entries": len(entries), "stage_counts": counts,
            "cash_aggregation_performed": False,
            "bank_receipts_certified": False, "contract_authenticity_certified": False,
            "private_data_required": False}


def main():
    parser = argparse.ArgumentParser(description="PI-RISE public status only audit")
    parser.add_argument("path", type=Path)
    parser.add_argument("--check-paths", action="store_true")
    args = parser.parse_args()
    try:
        # Protect against accidentally reading private ledgers through this public-only tool.
        if args.path.name != "PI_RISE_FINANCE_PIPELINE_V0_1_0.json":
            raise AuditError("only public pipeline path permitted")
        data = json.loads(args.path.read_text(encoding="utf-8"))
        output = audit(data, check_paths=args.check_paths)
        print(json.dumps(output, ensure_ascii=False, indent=2))
    except (OSError, json.JSONDecodeError, AuditError) as exc:
        print(json.dumps({"protocol": "PI-RISE-FINANCE-PIPELINE/" + VERSION,
                          "result": "INVALID", "error_type": type(exc).__name__}))
        raise SystemExit(2) from None


if __name__ == "__main__":
    main()

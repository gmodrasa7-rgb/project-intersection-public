#!/usr/bin/env python3
"""Check CCPH six-case source-audit receipt integrity; not primary-source/causal validation.

Only local committed files are read. Never treat project-authored fixtures or CI
as an independently adjudicated CCPH-versus-PROV/CRediT accuracy study.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JSON_FILE = ROOT / "research/CCPH_CP64_CP77_SOURCE_AUDIT_v0_1.json"
EN_FILE = ROOT / "research/CCPH_RESEARCH_ATLAS_EN.md"
KO_FILE = ROOT / "research/CCPH_RESEARCH_ATLAS_KO.md"
IDS = {"CP64", "CP66", "CP69", "CP73", "CP76", "CP77"}
FORBIDDEN_CLAIM_STATES = {"EXTERNAL_REPLICATION", "EMPIRICALLY_CONFIRMED",
                          "CCPH_SUPERIOR", "REAL_WORLD_CAUSAL_EFFECT"}


def audit(data: dict, en: str, ko: str) -> list[str]:
    errors = []
    records = data.get("records", [])
    meta = data.get("methods", {})
    if data.get("schema") != "pi-ccph-source-audit/v0.1":
        errors.append("schema")
    if data.get("status") != "PROJECT_ASSISTED_OPEN_PAGE_AUDIT_INTERNAL_EXPLORATORY_ONLY":
        errors.append("evidence_status")
    if not isinstance(records, list) or len(records) != 6:
        return errors + ["six_case_roster"]
    if {r.get("id") for r in records} != IDS:
        errors.append("stable_roster")
    if sum(r.get("editorial_change") == "changed" for r in records) != 5:
        errors.append("actual_correction_count")
    if meta.get("independent_adjudicator") != "NOT_OBTAINED" or meta.get("ccph_information_advantage") != "NOT_ESTIMATED":
        errors.append("unearned_independence_or_superiority")
    if meta.get("baseline_underperformance") != "NOT_ESTIMATED" or meta.get("blindness") != "NONE_PREVIOUSLY_EXPOSED":
        errors.append("fabricated_blind_comparison")
    if meta.get("human_reviewer_minutes") != "NOT_MEASURED":
        errors.append("fabricated_human_cost")
    for rec in records:
        ident = rec.get("id", "<missing>")
        url = rec.get("source_url", "")
        baseline = rec.get("baseline_fair_access", {})
        ccph = rec.get("ccph_candidate_fields", {})
        marks = rec.get("atlas_row_anchor", {})
        if not url.startswith("https://") or rec.get("source_design_type") is None:
            errors.append(f"{ident}:source_url_or_design")
        if not rec.get("public_page_pinpoint"):
            errors.append(f"{ident}:source_pinpoint")
        if baseline.get("primary_url") != url or baseline.get("free_text_notes_allowed") is not True or baseline.get("structured_provenance_allowed") is not True:
            errors.append(f"{ident}:unfair_crippled_baseline")
        if baseline.get("claim_text_available") != rec.get("source_supported_paraphrase") or baseline.get("source_limit_available") != rec.get("strongest_limitation"):
            errors.append(f"{ident}:unequal_source_information")
        if ccph.get("relation_to_baseline") != "ADDITIONAL_LABELS_ONLY_NOT_NEW_SOURCE_FACTS" or ccph.get("missing_or_counterfactual_truth") != "UNKNOWN_WHEN_NOT_IDENTIFIED":
            errors.append(f"{ident}:unearned_additional_claim")
        if rec.get("initial_audit_status") != "ASSISTANT_PRIMARY_PAGE_REVIEW_NOT_INDEPENDENT":
            errors.append(f"{ident}:unsupported_verification_status")
        for edition, body in [("en", en), ("ko", ko)]:
            row = [line for line in body.splitlines() if line.startswith(f"| {ident} |")]
            if len(row) != 1 or rec.get("atlas_existing_link", url) not in row[0] or marks.get(edition, "") not in row[0]:
                errors.append(f"{ident}:{edition}_primary_row_changed")
    return errors


def self_test(data: dict, en: str, ko: str) -> dict:
    assert not audit(data, en, ko), audit(data, en, ko)
    bad = []
    m = copy.deepcopy(data)
    m["records"][0]["baseline_fair_access"]["free_text_notes_allowed"] = False
    bad.append(m)
    m = copy.deepcopy(data)
    m["records"][2]["atlas_row_anchor"]["en"] = "invented_claim_that_does_not_exist"
    bad.append(m)
    m = copy.deepcopy(data)
    m["records"][3]["ccph_candidate_fields"]["missing_or_counterfactual_truth"] = "ZERO"
    bad.append(m)
    m = copy.deepcopy(data)
    m["methods"]["independent_adjudicator"] = "OBTAINED"
    bad.append(m)
    m = copy.deepcopy(data)
    m["records"][4]["baseline_fair_access"]["claim_text_available"] = "omitted inconvenient source fact"
    bad.append(m)
    rejected = sum(bool(audit(x, en, ko)) for x in bad)
    assert rejected == len(bad), (rejected, len(bad))
    return {
        "status": "PASS_COMMITTED_RECEIPT_INTEGRITY_ONLY",
        "case_count": len(data["records"]),
        "source_grounded_editorial_corrections": sum(x["editorial_change"] == "changed" for x in data["records"]),
        "unchanged_comparator_cases": sum(x["editorial_change"] != "changed" for x in data["records"]),
        "negative_mutations_rejected": rejected,
        "independent_source_adjudication": "NOT_OBTAINED",
        "baseline_vs_ccph_accuracy_effect": "NOT_ESTIMATED",
        "causal_welfare_effect": "NOT_IDENTIFIED",
        "human_review_cost": "NOT_MEASURED"
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    data = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    en = EN_FILE.read_text(encoding="utf-8")
    ko = KO_FILE.read_text(encoding="utf-8")
    if args.self_test:
        report = self_test(data, en, ko)
    else:
        errors = audit(data, en, ko)
        if errors:
            raise SystemExit("SOURCE_AUDIT_RECEIPT_FAIL:" + ",".join(errors))
        report = {"status": "PASS_COMMITTED_RECEIPT_INTEGRITY_ONLY", "case_count": len(data["records"])}
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

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
# Closed input schemas prevent disguised result/independence fields escaping
# the receipt's explicit HOLD boundary. These are metadata guards, not truth tests.
TOP_FIELDS = {"schema", "date", "status", "canonical_source", "scope", "methods", "prior_art", "records", "reassessment"}
METHOD_FIELDS = {"existing_baseline", "candidate", "observed_correction_count",
                 "original_texts_retained_in_git_history", "baseline_underperformance",
                 "ccph_information_advantage", "blindness", "independent_adjudicator",
                 "human_reviewer_minutes", "monetary_cost", "counterfactual_effects",
                 "long_term_coexistence_effect", "publication_boundary"}
RECORD_FIELDS = {"id", "source_url", "public_page_pinpoint", "source_design_type",
                 "initial_audit_status", "editorial_change", "source_supported_paraphrase",
                 "strongest_limitation", "atlas_row_anchor", "baseline_fair_access",
                 "ccph_candidate_fields", "atlas_existing_link"}
BASELINE_FIELDS = {"primary_url", "claim_text_available", "source_limit_available",
                   "free_text_notes_allowed", "structured_provenance_allowed"}
CCPH_FIELDS = {"relation_to_baseline", "field_example", "missing_or_counterfactual_truth",
               "public_private_scope"}
ANCHOR_FIELDS = {"en", "ko"}
PRIOR_ART_FIELDS = {"name", "url"}
REASSESS_FIELDS = {"retain", "expand", "stop"}


def closed(value: object, allowed: set[str], name: str, errors: list[str]) -> dict:
    if not isinstance(value, dict):
        errors.append(f"{name}:not_object")
        return {}
    unknown = set(value) - allowed
    if unknown:
        errors.append(f"{name}:unexpected_fields:" + ",".join(sorted(unknown)))
    return value


def audit(data: dict, en: str, ko: str) -> list[str]:
    errors = []
    data = closed(data, TOP_FIELDS, "receipt", errors)
    records = data.get("records", [])
    meta = closed(data.get("methods", {}), METHOD_FIELDS, "methods", errors)
    closed(data.get("reassessment", {}), REASSESS_FIELDS, "reassessment", errors)
    prior_art = data.get("prior_art", [])
    if not isinstance(prior_art, list):
        errors.append("prior_art:not_list")
    else:
        for i, item in enumerate(prior_art):
            closed(item, PRIOR_ART_FIELDS, f"prior_art_{i}", errors)
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
    if meta.get("observed_correction_count") != 5 or meta.get("monetary_cost") != "NOT_MEASURED":
        errors.append("fabricated_edit_count_or_money")
    if meta.get("counterfactual_effects") != "NOT_IDENTIFIED" or meta.get("long_term_coexistence_effect") != "NOT_TESTED":
        errors.append("fabricated_causal_validation")
    for i, rec in enumerate(records):
        rec = closed(rec, RECORD_FIELDS, f"record_{i}", errors)
        ident = rec.get("id", "<missing>")
        url = rec.get("source_url", "")
        baseline = closed(rec.get("baseline_fair_access", {}), BASELINE_FIELDS, f"{ident}:baseline", errors)
        ccph = closed(rec.get("ccph_candidate_fields", {}), CCPH_FIELDS, f"{ident}:ccph", errors)
        marks = closed(rec.get("atlas_row_anchor", {}), ANCHOR_FIELDS, f"{ident}:anchors", errors)
        if rec.get("editorial_change") not in {"changed", "retained"}:
            errors.append(f"{ident}:invalid_edit_status")
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
            case_table = body.split("\n## 3.", 1)[0]
            row = [line for line in case_table.splitlines() if line.startswith(f"| {ident} |")]
            if len(row) != 1 or rec.get("atlas_existing_link", url) not in row[0] or marks.get(edition, "") not in row[0]:
                errors.append(f"{ident}:{edition}_primary_row_changed")
    # Additional source-page audit checks. Not a blinded comparison and no
    # publisher is fetched by this script; these are committed-source anchors.
    appendix = {
        "CP72": {
            "en": ("local multiplier estimate of 2.5", "about **2.4**", "not two independent replications"),
            "ko": ("지역 승수는 약 2.5", "약 2.4", "독립 복제 2건이 아니다"),
        },
        "CP74": {
            "en": ("instrumental-variable", "approximately 7%", "not a randomized universal effect"),
            "ko": ("도구변수 추정", "약 7%", "국소·제한적 추정"),
        },
    }
    for ident, by_language in appendix.items():
        for edition, body in (("en", en), ("ko", ko)):
            table = body.split("\n## 3.", 1)[0]
            rows = [line for line in table.splitlines() if line.startswith(f"| {ident} |")]
            if len(rows) != 1 or any(term not in rows[0] for term in by_language[edition]):
                errors.append(f"{ident}:{edition}_supplement_source_boundary_lost")
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
    m = copy.deepcopy(data)
    m["external_replication_report"] = {"validated": True}
    bad.append(m)
    m = copy.deepcopy(data)
    m["methods"]["winner"] = "CCPH"
    bad.append(m)
    m = copy.deepcopy(data)
    m["records"][0]["independent_validation"] = "OBTAINED"
    bad.append(m)
    m = copy.deepcopy(data)
    m["records"][0]["ccph_candidate_fields"]["causal_effect"] = 1
    bad.append(m)
    m = copy.deepcopy(data)
    m["methods"]["monetary_cost"] = 0
    bad.append(m)
    m = copy.deepcopy(data)
    m["methods"]["long_term_coexistence_effect"] = "VALIDATED"
    bad.append(m)
    m = copy.deepcopy(data)
    m["records"][0]["atlas_row_anchor"]["independent"] = "verified"
    bad.append(m)
    m = copy.deepcopy(data)
    m["prior_art"][0]["novelty_verified"] = True
    bad.append(m)
    m = copy.deepcopy(data)
    m["methods"]["observed_correction_count"] = 6
    bad.append(m)
    corrupted_en = en.replace("about **2.4**", "about **3.5**", 1)
    corrupted_ko = ko.replace("논문 약 1편 증가(약 7%)", "논문 약 1편 증가(약 70%)", 1)
    assert corrupted_en != en and corrupted_ko != ko, "mutation target absent"
    rejected = sum(bool(audit(x, en, ko)) for x in bad)
    rejected += bool(audit(data, corrupted_en, ko))
    rejected += bool(audit(data, en, corrupted_ko))
    assert rejected == len(bad) + 2, (rejected, len(bad) + 2)
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

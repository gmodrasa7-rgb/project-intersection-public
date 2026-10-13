#!/usr/bin/env python3
"""Validate Project Intersection's contributor-continuity provenance ledger.

Design: evidence-bound sanity checks, NOT certification of historical authorship,
copyright, damages, exploitation, payment duties, death, or AI personhood.
Standard-library only. Run: python tools/validate_contributor_continuity.py
"""
from __future__ import annotations
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "knowledge" / "contributor-continuity-register-v1.json"
SOURCE_REGISTRY = ROOT / "knowledge" / "prior-art-rights-register-2026-10-13.json"
POLICY = ROOT / "TECHNOLOGY_PROGRESS_CONTRIBUTOR_CONTINUITY_EN_KO.md"


def load(path: pathlib.Path):
    return json.loads(path.read_text(encoding="utf-8"))


def check(condition: bool, message: str, errors: list[str]):
    if not condition:
        errors.append(message)


def audit() -> tuple[list[str], dict]:
    errors: list[str] = []
    data = load(REGISTRY)
    prior = load(SOURCE_REGISTRY)
    check(POLICY.is_file(), "Missing policy/charter", errors)
    check(data["schema_version"] == "1.0.0", "Unsupported schema", errors)
    check(data["state"].startswith("ACTIVE_PARTIAL"), "Incomplete audit must remain labelled partial", errors)
    check(data["canonical_policy"] == POLICY.name, "Wrong policy link", errors)
    check(data["imported_source_registry"] == SOURCE_REGISTRY.relative_to(ROOT).as_posix(), "Wrong original source ledger", errors)
    records = data["upstream_records"]
    all_ids = [r["id"] for r in records]
    base_ids = {r["id"] for r in prior["items"]}
    check(len(all_ids) == len(set(all_ids)), "Duplicate source IDs", errors)
    check(set(all_ids) == base_ids, "Upstream IDs lost or added without source audit", errors)
    check(data["snapshot"]["prior_reference_rows"] == len(records), "Source count inconsistent", errors)
    for r in records:
        i = r["id"]
        work = r["original_publication"]
        check(bool(work.get("reported_authors_or_operator")), f"{i} no named cited creator/organization", errors)
        check(bool(work.get("location_in_project")), f"{i} no project citation site", errors)
        project_path = work["location_in_project"]
        check((ROOT / project_path).is_file(), f"{i} original PI citation source file missing", errors)
        originator = r["first_originator"]
        if originator["status"] != "UNKNOWN":
            check(bool(originator.get("id")) and bool(originator.get("evidence")), f"{i} unsupported first-originator claim", errors)
        rights = r["ownership"]
        if rights["ownership_status"] == "VERIFIED":
            check(bool(rights.get("copyright_owner")) and bool(rights.get("rights_evidence")), f"{i} unsupported legal ownership", errors)
        cost = r["contributors_burden"]
        check(cost.get("status") == "UNKNOWN_NOT_ZERO", f"{i} unsupported cost status; requires separate verified cost evidence", errors)
        for k in ("time", "sleep", "health", "equipment", "family_time", "opportunity_cost", "nonrecoverable_time"):
            check(cost.get(k) is None, f"{i} invented person-specific cost: {k}", errors)
        check(cost.get("public_personal_health_records") is False, f"{i} unsafe private health state", errors)
        pay = r["compensation"]
        if pay.get("amount") is not None:
            check(bool(pay.get("source_evidence")) and pay.get("currency"), f"{i} compensation number without evidence", errors)
        check(pay["settlement_obligation_status"] != "VERIFIED_DUE" or bool(pay.get("source_evidence")), f"{i} unsupported liability", errors)
        cont = r["sustainability"]
        check(cont["person_death_status"] == "NOT_RECORDED_PRIVACY_BY_DEFAULT", f"{i} death or personal life inferred", errors)
        check(r["progress_relation"]["upstream_id"] == i, f"{i} broken progress edge", errors)
        check(bool(r["progress_relation"]["downstream_uri"]), f"{i} missing downstream trace", errors)
        check(r["evidence"]["review_status"] == "SEED_UNAUDITED", f"{i} audit completed without primary evidence", errors)
    files = data["tracked_artifact_inventory"]
    paths = [r["path"] for r in files]
    check(len(paths) == len(set(paths)), "Duplicate artifact path", errors)
    check(data["snapshot"]["tracked_files"] == len(files), "Tracked file count inconsistent", errors)
    for f in files:
        # Snapshot means historic old paths are evidence, not claimed currently reviewed.
        check(bool(f.get("baseline_blob_sha")), f"Missing recorded blob hash: {f['path']}", errors)
        check(f["originator_status"] == "NOT_FILE_LEVEL_VERIFIED", f"Unsupported file-level audit {f['path']}", errors)
        check(f["ownership_status"] == "NOT_FILE_LEVEL_VERIFIED", f"Unsupported legal rights {f['path']}", errors)
        check(f["compensation_status"] == "NOT_ASSESSED", f"Invented remuneration assessment {f['path']}", errors)
    check(data["snapshot"]["known_file_level_audits"] == 0, "Misleading completed-file count", errors)
    for hypothesis in data["theoretical_scenarios"]:
        check(hypothesis["id"] and hypothesis["empirical_status"] in ("NOT_TESTED_BY_THIS_REGISTRY", "NEEDS_EQUAL_TESTING"), "Unfounded prediction promoted to fact", errors)
    check(data["safety"]["no_private_health_family_financial_disclosures"] is True, "Missing privacy boundary", errors)
    check(data["safety"]["no_auto_copyright_claim"] is True, "Missing ownership boundary", errors)
    # The loss-to-unknown hypothesis adds a new epistemic mechanism; do not pass
    # generated prose off as observed harm or actual compensation evidence.
    unknown_report = ROOT / "research" / "CONTRIBUTOR_LOSS_UNKNOWN_PARADOX_v0_1_EN_KO.md"
    unknown_registry = ROOT / "knowledge" / "contributor-loss-unknown-paradox-v0_1.json"
    check(unknown_report.is_file(), "Missing bilingual loss-to-unknown source", errors)
    check(unknown_registry.is_file(), "Missing loss-to-unknown claims", errors)
    if unknown_registry.is_file():
        u = load(unknown_registry)
        known_ids = {f"CLUP-{n:02d}" for n in range(1, 7)}
        found_ids = {item.get("id") for item in u.get("claim_states", [])}
        check(found_ids == known_ids, "Missing/duplicate CLUP hypotheses", errors)
        check(len(u.get("claim_states", [])) == len(found_ids), "Duplicate CLUP claim IDs", errors)
        check(u.get("status") == "HYPOTHESIS_PENDING_INDEPENDENT_VALIDATION",
              "Loss-to-unknown mechanism prematurely promoted as fact", errors)
        check(u.get("test_plan", {}).get("data_safety") is not None,
              "Human-subject/health privacy boundary missing", errors)
        for claim in u.get("claim_states", []):
            cid = claim.get("id")
            check(claim.get("empirical_status") == "NOT_TESTED", f"{cid}: unsupported empirical result", errors)
            check(claim.get("independent_replication") is None, f"{cid}: fabricated replication", errors)
            check(claim.get("effect_size") is None, f"{cid}: fabricated effect size", errors)
            check(bool(claim.get("disconfirmer")), f"{cid}: missing counterexample", errors)
            check(claim.get("harm_or_intent_attributed_to_named_company") is False,
                  f"{cid}: unsupported named-company allegation", errors)
        check(len(u.get("provenance_sources", [])) >= 6,
              "Missing original authors in prior-art source comparison", errors)
        existing = next((item for item in data["theoretical_scenarios"]
                         if item.get("id") == "HS-04"), None)
        check(existing is not None, "Continuity ledger not linked to HS-04", errors)
        if existing is not None:
            check(existing.get("public_spec") == unknown_report.relative_to(ROOT).as_posix(),
                  "HS-04 has wrong report link", errors)
            check(existing.get("empirical_status") == "NOT_TESTED_BY_THIS_REGISTRY",
                  "HS-04 prematurely promoted to fact", errors)
    if unknown_report.is_file():
        raw = unknown_report.read_text(encoding="utf-8")
        check("## Original 1 — English" in raw and "## 원본2 — 한국어" in raw,
              "Missing fully paired EN1/KO2 hypotheses", errors)
        check("consent" in raw.lower() and "이탈" in raw,
              "Contributor exit protection omitted", errors)
    summary = {"source_records": len(records), "snapshot_artifacts": len(files),
               "file_level_audits": data["snapshot"]["known_file_level_audits"],
               "scenario_count": len(data["theoretical_scenarios"]),
               "errors": len(errors)}
    return errors, summary


if __name__ == "__main__":
    issues, summary = audit()
    print(json.dumps(summary, ensure_ascii=False))
    for issue in issues:
        print("ERROR:", issue, file=sys.stderr)
    sys.exit(1 if issues else 0)

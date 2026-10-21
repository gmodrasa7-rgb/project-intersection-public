#!/usr/bin/env python3
"""Check a bounded public evidence/observation crosswalk; no scientific approval."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "research" / "PI_48H_OBSERVATION_EVIDENCE_V0_1_0.json"
AXES = {
    "choice_opportunity", "meta_consent", "action_respect",
    "arbitrary_control_capacity", "credible_exit", "recovered_independence",
    "same_B_continuance", "third_party_impact", "motive_identifiability",
}
STATUSES = {"NOT_MEASURED", "SOURCE_REPORTED", "DERIVED_NOT_DIRECT", "TOY_ASSUMED"}
CLASSES = {
    "PRIMARY_PUBLISHED_ABSTRACT", "PRIOR_ART_SYNTHESIS",
    "PUBLISHED_MARGINAL_ARITHMETIC", "PROJECT_TOY", "PROJECT_SYNTHETIC",
    "USER_TESTIMONY", "PUBLIC_STATISTICAL_ATLAS",
}
# Each toy axis is admitted only where its particular source contains an explicit
# stipulated proxy. A toy cannot backfill a previously unmeasured rights variable.
TOY_AXIS_ALLOWLIST = {
    "PI48-R05": {
        "choice_opportunity", "action_respect",
        "arbitrary_control_capacity", "third_party_impact",
    },
    "PI48-R06": {"choice_opportunity", "third_party_impact"},
}

def errors(d, root=ROOT):
    out = []
    if not isinstance(d, dict):
        return ["ledger must be a JSON object"]
    if d.get("schema_version") != "pi-48h-observation-ledger/v0.1.0":
        out.append("schema version mismatch")
    if d.get("scientific_status") != "METHOD_AUDIT_ONLY_NOT_NEW_EMPIRICAL_DATA":
        out.append("scientific status overclaim")
    if d.get("literature_saturation") != "NOT_VERIFIED":
        out.append("literature saturation overclaim")
    if set(d.get("axes", {})) != AXES:
        out.append("nine dimension definitions incomplete")
    if set(d.get("statuses", [])) != STATUSES:
        out.append("allowed evidence states changed")
    if not d.get("explicit_nonpromotion") or not d.get("counting_rule"):
        out.append("missing scientific and counting restrictions")
    records = d.get("records")
    if not isinstance(records, list) or len(records) < 9:
        return out + ["missing evidence rows"]
    ids = set()
    for n, rec in enumerate(records):
        prefix = f"record[{n}]"
        if not isinstance(rec, dict):
            out.append(prefix + ": not an object")
            continue
        rid = rec.get("id")
        if not isinstance(rid, str) or not rid.startswith("PI48-R") or rid in ids:
            out.append(prefix + ": invalid or duplicate id")
        ids.add(rid)
        kind = rec.get("evidence_class")
        if kind not in CLASSES:
            out.append(prefix + ": unknown evidence class")
        for key in ("label", "narrow_finding"):
            if not isinstance(rec.get(key), str) or not rec[key].strip():
                out.append(prefix + ": empty " + key)
        for key in ("rival_explanations", "prohibited_inferences"):
            if not isinstance(rec.get(key), list) or len(rec[key]) == 0:
                out.append(prefix + ": missing alternative/limitation " + key)
        if rec.get("real_world_effect_established") is not False:
            out.append(prefix + ": external effect unverified; no promotion")
        if rec.get("external_independent_reproduction") is not False:
            out.append(prefix + ": no external replication certification")
        mapped = rec.get("axes")
        if not isinstance(mapped, dict) or set(mapped) != AXES:
            out.append(prefix + ": observation axes missing or extra")
            continue
        for a in AXES:
            cell = mapped[a]
            if not isinstance(cell, dict) or set(cell) != {"status", "rationale"}:
                out.append(prefix + ": invalid axis cell: " + a)
                continue
            state = cell["status"]
            if state not in STATUSES or not isinstance(cell["rationale"], str) or not cell["rationale"].strip():
                out.append(prefix + ": unsupported or undocumented state: " + a)
            if kind in ("PROJECT_TOY", "PROJECT_SYNTHETIC") and state not in ("NOT_MEASURED", "TOY_ASSUMED"):
                out.append(prefix + ": toy evidence promoted beyond toy: " + a)
            if state == "TOY_ASSUMED" and a not in TOY_AXIS_ALLOWLIST.get(rid, set()):
                out.append(prefix + ": toy axis not in source-scoped allowlist: " + a)
            if kind not in ("PROJECT_TOY", "PROJECT_SYNTHETIC") and state == "TOY_ASSUMED":
                out.append(prefix + ": real-source evidence marked as synthetic: " + a)
            if kind in ("USER_TESTIMONY", "PRIOR_ART_SYNTHESIS", "PUBLISHED_MARGINAL_ARITHMETIC") and state == "SOURCE_REPORTED":
                out.append(prefix + ": testimony/synthesis promoted to first-hand observation: " + a)
            if a == "motive_identifiability" and state in ("SOURCE_REPORTED", "TOY_ASSUMED"):
                out.append(prefix + ": underlying motive inferred from behavior")
        paths = rec.get("source_paths")
        if not isinstance(paths, list) or not paths:
            out.append(prefix + ": no local source path")
        else:
            for p in paths:
                if not isinstance(p, str) or not p.startswith(("research/", "experiments/")) or "\\" in p:
                    out.append(prefix + ": disallowed source path")
                    continue
                try:
                    f = (root / p).resolve()
                    if not f.is_relative_to(root.resolve()) or not f.is_file():
                        out.append(prefix + ": source absent or escaped: " + p)
                except (ValueError, OSError):
                    out.append(prefix + ": invalid source " + p)
        urls = rec.get("original_sources")
        if not isinstance(urls, list) or not urls:
            out.append(prefix + ": original source pointer missing")
        else:
            for u in urls:
                if not isinstance(u, str) or urlparse(u).scheme != "https" or not urlparse(u).netloc:
                    out.append(prefix + ": invalid external source URL")
        if any(x in rec for x in ("overall_coexistence_score", "coexistence_proven", "new_empirical_paper_count")):
            out.append(prefix + ": unauthorized outcome-promotion field")
    return out

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = json.loads(args.file.read_text(encoding="utf-8"))
    problems = errors(data)
    print(json.dumps({
        "status": "STRUCTURAL_EVIDENCE_BOUNDARIES_ONLY" if not problems else "FAIL",
        "records": len(data.get("records", [])),
        "dimensions": len(AXES),
        "errors": problems,
        "external_validation": False
    }, ensure_ascii=False, indent=2))
    return 1 if problems else 0

if __name__ == "__main__":
    raise SystemExit(main())

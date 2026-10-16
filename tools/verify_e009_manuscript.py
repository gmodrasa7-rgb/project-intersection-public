#!/usr/bin/env python3
"""E009 bilingual working-paper audit: cross-check frozen synthetic numbers and status.

This checker cannot certify the scientific truth of the consequence engine,
new novelty, independent replication, publication quality or translation parity.
It does not change the E009 preregistered benchmark, protocol, or RESULT.json.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN_PATH = ROOT / "research/papers/E009_NEGATIVE_RESULT_METHODS_EN.md"
KO_PATH = ROOT / "research/papers/E009_NEGATIVE_RESULT_METHODS_KO.md"
RESULT_PATH = ROOT / "experiments/e009/RESULT.json"
RECEIPT_PATH = ROOT / "experiments/e009/EXECUTION_RECEIPT.json"
BENCH_PATH = ROOT / "experiments/e009/benchmark.py"
POLICIES = ("TWO_RULE_SIMPLE", "MINIMAL_4VAR", "PROJECT_V3",
            "MAK_PLUS_POINTWISE", "SECURITY_BOUNDED")
COMPLEXITY = {"TWO_RULE_SIMPLE": 3, "MINIMAL_4VAR": 7, "PROJECT_V3": 11}
PENALTY = 0.0035
TOL = 0.0000006  # Six decimal displays in the main manuscript table.


def approx_printed(cell: str, expected: float, label: str, errors: list[str]) -> None:
    cleaned = cell.replace("**", "").replace(",", "").strip()
    try:
        value = float(cleaned)
    except ValueError:
        errors.append(f"{label}:invalid_number:{cell}")
        return
    if not math.isclose(value, expected, abs_tol=TOL, rel_tol=0):
        errors.append(f"{label}:number_mismatch:{value} != {expected}")


def check(en: str, ko: str, result: dict, receipt: dict, bench: bytes) -> list[str]:
    errors: list[str] = []
    if hashlib.sha256(bench).hexdigest() != receipt.get("benchmark_sha256"):
        errors.append("frozen_benchmark_sha256_changed")
    if result.get("status") != "SYNTHETIC_PROJECT_RERUN_NOT_INDEPENDENT_VALIDATION":
        errors.append("result_independence_claim_modified")
    criteria = result.get("survival_criteria", {})
    gates = [value for key, value in criteria.items() if key != "project_v3_residual_survives"]
    if len(gates) != 4 or gates.count(False) != 3 or gates.count(True) != 1:
        errors.append("preregistered_survival_gates_changed")
    if criteria.get("project_v3_residual_survives") is not False:
        errors.append("negative_verdict_inverted")
    if receipt.get("independent_validation") is not False or receipt.get("policy_or_threshold_changes_after_spec_merge") is not False:
        errors.append("receipt_independence_or_tuning")
    if receipt.get("executable_spec_commit") != "c36ba8e6d6df1eedcd54ca6c36091bf822fe6ace":
        errors.append("frozen_spec_commit_changed")
    primary = result.get("stress_primary", {})
    if set(POLICIES) - set(primary):
        return errors + ["result_missing_policies"]
    two = primary["TWO_RULE_SIMPLE"]["mean_regret"]
    m4 = primary["MINIMAL_4VAR"]["mean_regret"]
    v3 = primary["PROJECT_V3"]["mean_regret"]
    gap = 100 * (v3 / two - 1)
    if not math.isclose(gap, 42.348132, abs_tol=0.00002):
        errors.append("unexpected_regret_ratio")
    if not math.isclose((v3 - PENALTY * 11) - (m4 - PENALTY * 7),
                        0.010698591081, abs_tol=0.00000001):
        errors.append("unexpected_penalty_decomposition")
    for language, body in (("en", en), ("ko", ko)):
        if language == "en" and re.search(r"[가-힣]", body):
            errors.append("english_manuscript_has_korean_prose")
        if "## 3." not in body or "## 4." not in body:
            errors.append(f"{language}:missing_main_sections")
            continue
        main_section = body.split("## 3.", 1)[1].split("## 4.", 1)[0]
        for policy in POLICIES:
            lines = [line for line in main_section.splitlines()
                     if line.startswith(f"| {policy} |")]
            if len(lines) != 1:
                errors.append(f"{language}:{policy}:missing_or_duplicate_main_row")
                continue
            cells = [x.strip() for x in lines[0].strip().strip("|").split("|")]
            if len(cells) != 6:
                errors.append(f"{language}:{policy}:column_count")
                continue
            observed = primary[policy]
            for idx, key in ((1, "mean_regret"), (2, "mean_recovery"),
                             (4, "mean_exit_retention"), (5, "mean_competitive_loss")):
                approx_printed(cells[idx], observed[key], f"{language}:{policy}:{key}", errors)
            expected_events = round(observed["severe_harm_rate"] * 3200)
            if not cells[3].replace("**", "").strip().startswith(str(expected_events) + " ("):
                errors.append(f"{language}:{policy}:wrong_severe_event_denominator")
        for val in ("0.063240512", "0.065323097", "0.090021688",
                    "0.010500000", "0.024500000", "0.038500000",
                    "0.052740512", "0.040823097", "0.051521688",
                    "0.028000000", "0.001218824", "0.010698591",
                    "0.064379213", "0.066980024", "0.090082206"):
            if val not in body:
                errors.append(f"{language}:missing_evidence_anchor:{val}")
        if "3,200" not in body and language == "en":
            errors.append("en:missing_decision_unit")
        if "3,200" not in body and language == "ko":
            errors.append("ko:missing_decision_unit")
        if "9,600" not in body:
            errors.append(f"{language}:missing_profile_reweighting")
        if "c36ba8e6d6df1eedcd54ca6c36091bf822fe6ace" not in body:
            errors.append(f"{language}:wrong_spec_commit")
        if receipt.get("benchmark_sha256", "") not in body or receipt.get("generated_result_sha256", "") not in body:
            errors.append(f"{language}:missing_receipt_hash")
        if language == "en":
            required = ("NOT SUBMITTED", "NOT PEER REVIEWED", "not an independent",
                        "42.3481%", "three of four", "HOLD")
        else:
            required = ("미투고", "동료심사 없음", "외부 독립 복제 없음",
                        "42.3481%", "4개 중 3개", "HOLD")
        for marker in required:
            if marker not in body:
                errors.append(f"{language}:missing_status_or_scope:{marker}")
        if "<PINNED_PUBLIC_COMMIT_CONTAINING_THIS_MANUSCRIPT>" not in body:
            errors.append(f"{language}:repro_checkout_placeholder_not_visible")
    return errors


def run_selftest(en: str, ko: str, res: dict, rec: dict, bench: bytes) -> dict:
    good = check(en, ko, res, rec, bench)
    if good:
        raise AssertionError("base_receipt_fails:" + ",".join(good))
    cases = []
    cases.append((en.replace("0.090022 | 0.239404", "0.050022 | 0.239404", 1), ko, res, rec, bench))
    cases.append((en, ko.replace("0.063241", "0.033241", 1), res, rec, bench))
    modified = copy.deepcopy(res)
    modified["survival_criteria"]["project_v3_residual_survives"] = True
    cases.append((en, ko, modified, rec, bench))
    modified = copy.deepcopy(rec)
    modified["independent_validation"] = True
    cases.append((en, ko, res, modified, bench))
    cases.append((en, ko, res, rec, bench + b" "))
    cases.append((en.replace("NOT PEER REVIEWED", "PEER REVIEWED", 1), ko, res, rec, bench))
    cases.append((en, ko.replace("9,600", "96,000", 1), res, rec, bench))
    cases.append((en.replace("0.010698591", "0.000000000"), ko, res, rec, bench))
    rejected = [bool(check(*case)) for case in cases]
    if not all(rejected):
        raise AssertionError("undetected_mutations:" + str([i for i, ok in enumerate(rejected) if not ok]))
    return {
        "status": "PASS_FROZEN_E009_MANUSCRIPT_CONSISTENCY_ONLY",
        "manuscript_languages": ["en", "ko"],
        "compared_policies": 5,
        "primary_unique_decisions_per_policy": 3200,
        "metric_rows_reweighted_per_policy": 9600,
        "preregistered_survival_failures": 3,
        "negative_controls_rejected": len(rejected),
        "source_scientific_independence": False,
        "external_replication": False,
        "publication_clearance": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    en, ko = (path.read_text(encoding="utf-8") for path in (EN_PATH, KO_PATH))
    res = json.loads(RESULT_PATH.read_text(encoding="utf-8"))
    rec = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    bench = BENCH_PATH.read_bytes()
    if args.self_test:
        report = run_selftest(en, ko, res, rec, bench)
    else:
        errors = check(en, ko, res, rec, bench)
        if errors:
            raise SystemExit("E009_PAPER_MISMATCH:" + ",".join(errors))
        report = {"status": "PASS_FROZEN_E009_MANUSCRIPT_CONSISTENCY_ONLY"}
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""PI-RAMP v0.3 run-receipt structural and evidence-status regression guard.

Does NOT certify source truth, reviewer independence, scientific validity,
method effect, AI subjective states or English/Korean semantic parity.
Standard-library only. Never invent missing evaluation observations.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "evaluation/pi_ramp/RAMP-20261020-002.json"
SHA40 = re.compile(r"^[a-f0-9]{40}$")
TASK_IDS = {"T1", "T2", "T3", "T4"}
METRICS = (
    "correctness_before", "correctness_after",
    "source_trace_before", "source_trace_after",
    "time_seconds_before", "time_seconds_after",
    "critical_error_before", "critical_error_after",
)
MEASURED = {"GAIN_OBSERVED", "NO_DEMONSTRATED_GAIN", "REGRESSION_OBSERVED"}
EFFECTS = MEASURED | {"EFFECT_UNMEASURED"}
STATUSES = {"PROPOSED_PILOT", "PILOT", "EFFECT_MEASURED", "REJECTED", "REVERTED"}


def _path_present(raw: object) -> bool:
    if not isinstance(raw, str) or not raw or raw.startswith("/") or ".." in Path(raw).parts:
        return False
    return (ROOT / raw).is_file()


def validate(d: object) -> list[str]:
    if not isinstance(d, dict):
        return ["ROOT_NOT_OBJECT"]
    errors: list[str] = []
    if d.get("schema") != "pi-ramp-run/0.3":
        errors.append("SCHEMA_INVALID")
    if not re.fullmatch(r"RAMP-[0-9]{8}-[0-9]{3}", str(d.get("run_id", ""))):
        errors.append("RUN_ID_INVALID")
    if d.get("method_version") != "0.3.0":
        errors.append("VERSION_INVALID")
    if not SHA40.fullmatch(str(d.get("base_commit", ""))):
        errors.append("BASE_COMMIT_INVALID")
    if d.get("candidate_commit") is not None and not SHA40.fullmatch(str(d.get("candidate_commit"))):
        errors.append("CANDIDATE_COMMIT_INVALID")
    if d.get("status") not in STATUSES:
        errors.append("STATUS_INVALID")
    if d.get("effect_status") not in EFFECTS:
        errors.append("EFFECT_STATUS_INVALID")
    if d.get("scientific_validation_claim") is not False:
        errors.append("UNSUPPORTED_SCIENTIFIC_CERTIFICATION")
    if d.get("translation_review_status") != "NOT_INDEPENDENTLY_VERIFIED":
        errors.append("UNSUPPORTED_TRANSLATION_CERTIFICATION")
    if d.get("independent_review_status") not in (
        "NOT_INDEPENDENTLY_VERIFIED", "INDEPENDENTLY_REVIEWED"
    ):
        errors.append("INDEPENDENCE_STATUS_INVALID")
    elif d.get("independent_review_status") == "INDEPENDENTLY_REVIEWED":
        if not _path_present(d.get("independent_review_receipt")):
            errors.append("INDEPENDENT_REVIEW_RECEIPT_MISSING")
    elif d.get("independent_review_receipt") is not None:
        errors.append("INDEPENDENCE_RECEIPT_STATUS_CONFLICT")
    if d.get("registration_kind") != "PROSPECTIVE_METHOD_AND_TASKS_NO_OUTCOME":
        errors.append("REGISTRATION_KIND_INVALID")
    declared = d.get("predeclared_primary_outcomes", [])
    if not isinstance(declared, list) or set(declared) != {
        "task_correctness", "trace_to_original_source"
    } or len(declared) != 2:
        errors.append("PRIMARY_OUTCOMES_INVALID")
    methods = d.get("methods_adopted", [])
    if not isinstance(methods, list) or len(methods) < 3:
        errors.append("METHOD_LEDGER_MISSING")
    else:
        mids = []
        for m in methods:
            if not isinstance(m, dict):
                errors.append("METHOD_LEDGER_INVALID_ROW")
                continue
            mids.append(m.get("id"))
            url = m.get("source")
            if not isinstance(url, str) or urlsplit(url).scheme != "https" or not urlsplit(url).netloc:
                errors.append("METHOD_PRIMARY_SOURCE_URL_INVALID")
            if not m.get("transfer") or not m.get("limitation"):
                errors.append("METHOD_TRANSFER_LIMIT_MISSING")
        if len(mids) != len(set(mids)):
            errors.append("METHOD_ID_DUPLICATE")
    tasks = d.get("reader_tasks")
    if not isinstance(tasks, list):
        errors.append("TASKS_NOT_LIST")
        tasks = []
    ids = [t.get("id") for t in tasks if isinstance(t, dict)]
    if len(tasks) != 4 or set(ids) != TASK_IDS or len(ids) != len(set(ids)):
        errors.append("TASK_IDS_OR_COUNT_INVALID")
    observations = []
    for t in tasks:
        if not isinstance(t, dict):
            errors.append("TASK_NOT_OBJECT")
            continue
        if not _path_present(t.get("evidence_path")):
            errors.append("TASK_EVIDENCE_PATH_MISSING:" + str(t.get("id")))
        if not t.get("goal"):
            errors.append("TASK_GOAL_EMPTY:" + str(t.get("id")))
        for key in METRICS:
            if key not in t:
                errors.append("TASK_METRIC_FIELD_MISSING:" + str(t.get("id")) + ":" + key)
            observations.append(t.get(key))
        for key in ("correctness_before", "correctness_after",
                    "source_trace_before", "source_trace_after",
                    "critical_error_before", "critical_error_after"):
            if t.get(key) is not None and type(t.get(key)) is not bool:
                errors.append("TASK_BOOLEAN_METRIC_INVALID:" + str(t.get("id")) + ":" + key)
        for key in ("time_seconds_before", "time_seconds_after"):
            v = t.get(key)
            if v is not None and (type(v) not in (int, float) or v < 0):
                errors.append("TASK_TIME_INVALID:" + str(t.get("id")) + ":" + key)
    effect = d.get("effect_status")
    if effect == "EFFECT_UNMEASURED":
        if any(v is not None for v in observations) or d.get("comparison_evidence_path") is not None:
            errors.append("UNMEASURED_STATUS_CONTAINS_OUTCOME")
    elif effect in MEASURED:
        if d.get("status") != "EFFECT_MEASURED":
            errors.append("EFFECT_PROMOTION_STATUS_CONFLICT")
        if len(observations) != 4 * len(METRICS) or any(v is None for v in observations):
            errors.append("CLAIMED_EFFECT_HAS_INCOMPLETE_TASKS")
        if not _path_present(d.get("comparison_evidence_path")):
            errors.append("CLAIMED_EFFECT_WITHOUT_EVIDENCE_FILE")
        if d.get("candidate_commit") is None:
            errors.append("CLAIMED_EFFECT_WITHOUT_CANDIDATE_COMMIT")
    if d.get("status") == "EFFECT_MEASURED" and effect not in MEASURED:
        errors.append("STATUS_EFFECT_MISMATCH")
    if not isinstance(d.get("known_limits"), list) or not d.get("known_limits"):
        errors.append("LIMITS_MISSING")
    return errors


def self_test(d: dict) -> None:
    assert not validate(d), validate(d)
    cases = [
        ("fake_effect", lambda x: x.update({"effect_status": "GAIN_OBSERVED"})),
        ("fake_status", lambda x: x.update({"status": "EFFECT_MEASURED"})),
        ("fake_independence", lambda x: x.update({"independent_review_status": "INDEPENDENTLY_REVIEWED"})),
        ("fake_translation", lambda x: x.update({"translation_review_status": "REVIEWED"})),
        ("fake_scientific", lambda x: x.update({"scientific_validation_claim": True})),
        ("duplicate_tasks", lambda x: x["reader_tasks"][1].update({"id": "T1"})),
        ("broken_source", lambda x: x["reader_tasks"][0].update({"evidence_path": "research/missing-source.md"})),
        ("missing_method_limit", lambda x: x["methods_adopted"][0].update({"limitation": None})),
        ("forged_partial_measure", lambda x: x["reader_tasks"][0].update({"correctness_after": True})),
    ]
    for label, mutator in cases:
        modified = copy.deepcopy(d)
        mutator(modified)
        assert validate(modified), "FAILED_TO_REJECT_" + label
    print("PI-RAMP v0.3 receipt: structural PASS; 9 adversarial mutations REJECTED")
    print("BOUNDARY: this is not evidence of effectiveness, independence or source validity.")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--receipt", type=Path, default=DEFAULT)
    p.add_argument("--self-test", action="store_true")
    a = p.parse_args()
    d = json.loads(a.receipt.read_text(encoding="utf-8"))
    if a.self_test:
        self_test(d)
        return 0
    errors = validate(d)
    if errors:
        for err in errors:
            print("PI_RAMP_RECEIPT_FAIL:", err)
        return 1
    print("PI-RAMP receipt consistency: PASS (outcome claims not independently verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

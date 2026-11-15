"""Semantic checks that JSON Schema cannot express for IVS-0R records."""
from datetime import datetime


def _parse_datetime(value):
    if not isinstance(value, str):
        raise ValueError("timestamp must be a string")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def evidence_semantic_errors(record):
    errors = []
    if record.get("status") == "INDEPENDENTLY_VERIFIED":
        for key in ("verifier", "verified_at", "independence_disclosure"):
            if not isinstance(record.get(key), str) or not record[key].strip():
                errors.append(f"INDEPENDENTLY_VERIFIED requires non-empty {key}")
    if record.get("verified_at") is not None:
        try:
            _parse_datetime(record["verified_at"])
        except (TypeError, ValueError):
            errors.append("verified_at must be a valid ISO-8601 timestamp")
    return errors


def coverage_semantic_errors(record):
    errors = []
    try:
        started = _parse_datetime(record.get("started_at"))
        finished = _parse_datetime(record.get("finished_at"))
        if started.tzinfo is None or finished.tzinfo is None:
            errors.append("coverage timestamps must include timezone offsets")
        elif finished < started:
            errors.append("finished_at must not precede started_at")
    except (TypeError, ValueError):
        errors.append("started_at and finished_at must be valid ISO-8601 timestamps")

    inventory = record.get("target_inventory")
    target_count = record.get("target_count")
    observed_count = record.get("observed_count")
    if isinstance(inventory, list) and isinstance(target_count, int):
        if target_count != len(inventory):
            errors.append("target_count must equal target_inventory length")

    if record.get("coverage_status") == "COMPLETE_AT_REFERENCE":
        if record.get("pagination_exhausted") is not True:
            errors.append("complete coverage requires exhausted pagination")
        if record.get("errors") not in ([], None):
            errors.append("complete coverage cannot contain errors")
        if record.get("unresolved") not in ([], None):
            errors.append("complete coverage cannot contain unresolved targets")
        if target_count != observed_count:
            errors.append("complete coverage requires target_count == observed_count")
        if isinstance(inventory, list) and observed_count != len(inventory):
            errors.append("complete coverage requires observed_count == target_inventory length")
    return errors

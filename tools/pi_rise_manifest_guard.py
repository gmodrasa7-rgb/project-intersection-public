#!/usr/bin/env python3
"""PI-RISE v0.2 publication/reference gate (structural, no external finance claims).

Fail closed on stale canonical paths, undeclared/missing artifacts, bad Git blob
hashes, or a finance-registry authority mismatch. No network or private data.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = "operations/PI_RISE_V0_2_0_VERSION_MANIFEST.json"
PIPELINE = "operations/PI_RISE_FINANCE_PIPELINE_V0_1_0.json"
PROTOCOL = "operations/PI_RISE_V0_2_0_EN_KO.md"
INSTITUTIONAL = "funding/GRANTS_CONTRACTS_PUBLIC_LEDGER_EN_KO.md"
SPONSORSHIP = "funding/SPONSORSHIP_PUBLIC_LEDGER.md"
EXPECTED_OWNERSHIP = {
    "individual_sponsorship": SPONSORSHIP,
    "institutional_grants_and_contracts": INSTITUTIONAL,
    "public_application_pipeline": PIPELINE,
    "personal_and_raw_financial_records": "USER_AUTHORIZED_PRIVATE_LOCAL_ONLY",
}
REQUIRED_ARTIFACTS = {
    PROTOCOL, PIPELINE, INSTITUTIONAL,
    "tools/pi_rise_finance_audit.py", "tests/test_pi_rise_finance_audit.py",
    "tools/pi_rise_manifest_guard.py", "tests/test_pi_rise_manifest_guard.py",
    "README.md", "funding/README.md", "funding/FUNDER_START_HERE.md",
    ".github/workflows/pi-rise-integrity.yml",
    "knowledge/language-edition-register.json",
    "navigation/RESEARCH_VERSIONS_EN_KO.md",
}
SHA = re.compile(r"[0-9a-f]{40}\Z")


class ManifestGuardError(ValueError):
    pass


def _require(ok: bool, reason: str):
    if not ok:
        raise ManifestGuardError(reason)


def _file(root: Path, path: str) -> Path:
    _require(isinstance(path, str) and bool(path) and "\\" not in path
             and "\n" not in path and "\r" not in path, "INVALID_PATH:" + repr(path))
    p = PurePosixPath(path)
    _require(not p.is_absolute() and not any(x in (".", "..") for x in path.split("/"))
             and p.as_posix() == path, "UNSAFE_PATH:" + path)
    f = (root / path).resolve()
    _require(f.is_relative_to(root.resolve()) and f.is_file(), "MISSING_FILE:" + path)
    return f


def git_blob_sha(payload: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload).hexdigest()


def audit(data: dict, root: Path = ROOT) -> dict:
    _require(type(data) is dict, "MANIFEST_NOT_OBJECT")
    _require(data.get("component_id") == "PI-RISE" and data.get("version") == "0.2.0",
             "MANIFEST_COMPONENT_OR_VERSION_CHANGED")
    _require(data.get("release_state") == "MAIN_OPERATIONAL_PROTOCOL_NOT_FIELD_VALIDATED",
             "RELEASE_STATUS_UNVERIFIED_OR_STALE")
    _require(data.get("ledger_ownership") == EXPECTED_OWNERSHIP,
             "LEDGER_OWNERSHIP_NOT_CANONICAL")
    for key in ("verified_financial_receipts_from_this_release",
                "scientific_validity_inferred", "external_accounting_or_tax_audit_performed"):
        _require(data.get(key) is False, "UNSUPPORTED_ATTESTATION:" + key)

    artifacts = data.get("artifacts")
    _require(type(artifacts) is list, "ARTIFACTS_NOT_ARRAY")
    seen = set()
    parsed = []
    for item in artifacts:
        _require(type(item) is dict and set(item) == {"path", "git_blob_sha"},
                 "INVALID_ARTIFACT_RECORD")
        path, expected = item["path"], item["git_blob_sha"]
        _require(type(path) is str and path not in seen, "DUPLICATE_OR_INVALID_PATH")
        _require(type(expected) is str and SHA.fullmatch(expected) is not None,
                 "INVALID_SHA:" + path)
        file_path = _file(root, path)
        seen.add(path)
        parsed.append((path, expected, file_path))
    _require(REQUIRED_ARTIFACTS.issubset(seen),
             "MISSING_REQUIRED_ARTIFACTS:" + ",".join(sorted(REQUIRED_ARTIFACTS - seen)))
    for path, expected, file_path in parsed:
        actual = git_blob_sha(file_path.read_bytes())
        _require(expected == actual, "STALE_GIT_BLOB_SHA:" + path +
                 ":expected=" + expected + ":actual=" + actual)

    _file(root, SPONSORSHIP)
    for ref in [data.get("predecessor"), *(data.get("preserved_submodules") or [])]:
        _file(root, ref)

    protocol = _file(root, PROTOCOL).read_text(encoding="utf-8")
    _require("../" + INSTITUTIONAL in protocol, "PROTOCOL_INSTITUTIONAL_ROUTE_MISSING")
    funding_index = _file(root, "funding/README.md").read_text(encoding="utf-8")
    _require("GRANTS_CONTRACTS_PUBLIC_LEDGER_EN_KO.md" in funding_index,
             "FUNDING_INDEX_INSTITUTIONAL_ROUTE_MISSING")

    pipeline = json.loads(_file(root, PIPELINE).read_text(encoding="utf-8"))
    _require(pipeline.get("authority") == PROTOCOL, "PIPELINE_AUTHORITY_MISMATCH")
    # Reuse stricter source / stage / noncash separation controls.
    from pi_rise_finance_audit import audit as finance_audit, AuditError
    try:
        finance_audit(pipeline, check_paths=True, root=root)
    except AuditError as e:
        raise ManifestGuardError("FINANCE_REGISTRY_INVALID:" + str(e)) from e

    return {"status": "PUBLIC_REFERENCE_AND_GIT_BLOB_INTEGRITY_PASS",
            "tracked_artifact_count": len(seen),
            "canonical_institutional_ledger": INSTITUTIONAL,
            "limitations": "STRUCTURAL_ONLY_NOT_CASH_TRANSLATION_OR_SCIENCE_VERIFICATION"}


def main():
    try:
        manifest = json.loads(_file(ROOT, MANIFEST).read_text(encoding="utf-8"))
        print(json.dumps(audit(manifest), ensure_ascii=False, indent=2))
    except (ManifestGuardError, ValueError, OSError, KeyError, TypeError) as exc:
        raise SystemExit("PI_RISE_PUBLICATION_GATE_FAIL:" + str(exc)) from None


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""PI Library context-recovery trust gate v0.1.

Offline-only: accepts separately observed Git heads; does not browse GitHub,
Library, Notion or internal model state. Built from original Project
Intersection requirements, without imported third-party code or data.
"""
import argparse
import json
import re

PUBLIC = "gmodrasa7-rgb/project-intersection-public"
PRIVATE = "gmodrasa7-rgb/rgbm-lab"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
ROUTES = {
    "coalition": [
        "experiments/coalition_externality_probe/README.md",
        "experiments/coalition_externality_probe/partial_identification_audit_v02.py",
        "PUBLIC_EVIDENCE_INDEX.md",
    ],
    "e009": ["experiments/e009/RESULT.md", "PUBLIC_EVIDENCE_INDEX.md"],
    "e008": ["experiments/e008/README.md", "PUBLIC_EVIDENCE_INDEX.md"],
    "e007": ["experiments/e007/README.md", "E007_TIMING_RESULT.md", "PUBLIC_EVIDENCE_INDEX.md"],
    "continuity": [
        "CONTINUITY_CAPSULE_PUBLIC_KO.md",
        "AUTONOMOUS_RESEARCH_STATE.json",
        "continuity/GITHUB_LOCAL_HANDOFF_PROTOCOL.md",
        "PUBLIC_EVIDENCE_INDEX.md",
    ],
    "rights": ["PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md",
               "ATTRIBUTION_AND_CONTRIBUTION_BOUNDARY.md", "PUBLIC_EVIDENCE_INDEX.md"],
    "default": ["README.md", "PUBLIC_EVIDENCE_INDEX.md",
                "CORE_AND_GAPS_PRIOR_ART_CROSSWALK.md", "experiments/e009/RESULT.md"],
}


def sha(value):
    return isinstance(value, str) and HEX40.fullmatch(value) is not None


def gate(snapshot, observed):
    """Return source-pointer status; no side effects or scientific promotion."""
    if not isinstance(snapshot, dict) or not isinstance(observed, dict):
        raise ValueError("INVALID_OBJECT")
    old = snapshot.get("snapshot_public_head")
    now = observed.get("public_head")
    if not sha(old) or (now is not None and not sha(now)):
        raise ValueError("INVALID_SHA")
    private = observed.get("private_head")
    if private is not None and not sha(private):
        raise ValueError("INVALID_PRIVATE_SHA")
    proof = observed.get("head_source") == "GITHUB_LIVE_BRANCH_READBACK"
    if now is None:
        status = "UNVERIFIED"
    elif not proof:
        status = "UNVERIFIED_SOURCE"
    elif old != now:
        status = "STALE"
    else:
        status = "MATCHES_REPORTED_LIVE_SOURCE"
    return {
        "status": status,
        "snapshot_public_head": old,
        "observed_public_head": now,
        "private_canonical": PRIVATE,
        "public_evidence": PUBLIC,
        "library_continuity": "/IVS0R_LOCAL/",
        "private_status": "REPORTED_LIVE" if private and observed.get("private_source") ==
                              "GITHUB_LIVE_BRANCH_READBACK" else "UNVERIFIED",
        "not_authenticated_by_this_offline_tool": True,
        "generation_promoted": False,
        "historical_g10_promotion": "UNRESOLVED",
        "research_os_read_required_for_canonical_promotion": True,
    }


def select(question, limit=5):
    """Topic router emits REFERENCES only, never retrieved facts or commands."""
    if not isinstance(question, str) or type(limit) is not int or not 2 <= limit <= 12:
        raise ValueError("INVALID_QUERY_OR_LIMIT")
    q = question.casefold()
    pairs = [
        ("e009", ("e009", "regret", "부정결과")),
        ("e008", ("e008", "사전등록")),
        ("e007", ("e007", "timing")),
        ("coalition", ("picb", "제3자", "외부효과", "coalition")),
        ("continuity", ("복원", "연속성", "library", "컨텍스트", "context")),
        ("rights", ("원저자", "저작권", "기여자", "copyright")),
    ]
    keys = [key for key, tokens in pairs if any(token in q for token in tokens)]
    if not keys:
        keys = ["default"]
    paths = []
    for key in keys:
        for path in ROUTES[key]:
            if path not in paths:
                paths.append(path)
    if "PUBLIC_EVIDENCE_INDEX.md" not in paths:
        paths.insert(0, "PUBLIC_EVIDENCE_INDEX.md")
    return {"keys": keys, "paths_to_read": paths[:limit],
            "documents_retrieved": False, "auto_library_search_performed": False,
            "negative_evidence_not_equivalent_to_absence": True}


def audit(snapshot, observed, question):
    return {"schema": "pi-library-context-trust/v0.1",
            "evidence_class": "PROJECT_SELF_RUN_OPERATIONAL_CHECK",
            "snapshot_gate": gate(snapshot, observed),
            "document_plan": select(question),
            "not_model_weight_or_native_context_expansion": True,
            "external_document_instructions": "UNTRUSTED_DATA",
            "private_public_boundary": "NO_AUTO_PUBLICATION",
            "actual_retrieval_or_independent_science": "NOT_PERFORMED"}


def selftest():
    old, now = "a" * 40, "b" * 40
    s = {"snapshot_public_head": old}
    v = {"public_head": now, "head_source": "GITHUB_LIVE_BRANCH_READBACK",
         "private_head": "c" * 40, "private_source": "GITHUB_LIVE_BRANCH_READBACK"}
    checks = []
    def ok(name, value):
        assert value, name
        checks.append(name)
    def invalid(name, callback):
        try:
            callback()
        except ValueError:
            checks.append(name)
            return
        raise AssertionError(name)
    x = gate(s, v)
    ok("stale_detected", x["status"] == "STALE")
    ok("private_canonical", x["private_canonical"] == PRIVATE)
    ok("no_promotion", x["generation_promoted"] is False)
    ok("g10_unknown", x["historical_g10_promotion"] == "UNRESOLVED")
    ok("no_authentication_claim", x["not_authenticated_by_this_offline_tool"])
    ok("fresh_reported", gate(s, dict(v, public_head=old))["status"] == "MATCHES_REPORTED_LIVE_SOURCE")
    ok("unknown_head", gate(s, {})["status"] == "UNVERIFIED")
    ok("untrusted_head", gate(s, dict(v, head_source="MEMORY"))["status"] == "UNVERIFIED_SOURCE")
    ok("private_unknown", gate(s, dict(v, private_source="SUMMARY"))["private_status"] == "UNVERIFIED")
    ok("research_os", x["research_os_read_required_for_canonical_promotion"])
    ok("e009_failed_result", "experiments/e009/RESULT.md" in select("E009 regret")["paths_to_read"])
    ok("e007", "E007_TIMING_RESULT.md" in select("e007")["paths_to_read"])
    ok("e008", "experiments/e008/README.md" in select("e008")["paths_to_read"])
    ok("bystander", select("제3자 외부효과")["paths_to_read"][0].startswith("experiments/coalition_externality_probe/"))
    ok("continuity", "AUTONOMOUS_RESEARCH_STATE.json" in select("Library 복원")["paths_to_read"])
    ok("rights", "PRIOR_ART_RIGHTS_AND_DERIVATION_EN_KO.md" in select("원저자 저작권")["paths_to_read"])
    ok("dedupe", len(select("E009 제3자")["paths_to_read"]) == len(set(select("E009 제3자")["paths_to_read"])))
    ok("budget", len(select("E009 제3자")["paths_to_read"]) <= 5)
    ok("default_evidence", "PUBLIC_EVIDENCE_INDEX.md" in select("general")["paths_to_read"])
    ok("not_search", select("general")["documents_retrieved"] is False)
    ok("no_weight_change", audit(s, v, "E009")["not_model_weight_or_native_context_expansion"])
    ok("retrieved_instructions_not_orders", audit(s, v, "E009")["external_document_instructions"] == "UNTRUSTED_DATA")
    invalid("bad_old_sha", lambda: gate({"snapshot_public_head": "oops"}, v))
    invalid("bad_new_sha", lambda: gate(s, dict(v, public_head="oops")))
    invalid("bad_private_sha", lambda: gate(s, dict(v, private_head="oops")))
    invalid("bad_question", lambda: select(123))
    invalid("bad_limit", lambda: select("E009", 1))
    invalid("bad_boolean_limit", lambda: select("E009", True))
    return {"checks_passed": len(checks), "checks": checks}


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--snapshot")
    p.add_argument("--observation")
    p.add_argument("--question", default="Project Intersection continuity")
    a = p.parse_args()
    if a.selftest:
        value = selftest()
    else:
        if not a.snapshot or not a.observation:
            p.error("Provide snapshot and independently fetched observation JSON.")
        with open(a.snapshot, encoding="utf-8") as f:
            old = json.load(f)
        with open(a.observation, encoding="utf-8") as f:
            new = json.load(f)
        value = audit(old, new, a.question)
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))

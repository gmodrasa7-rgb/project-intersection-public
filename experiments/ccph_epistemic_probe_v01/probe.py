#!/usr/bin/env python3
"""CCPH v0.1: fixed synthetic epistemic-event observability and negative controls.

Project-authored finite-world diagnostic; not a trial, independent validation,
human-subject experiment, estimation of incidence, or original attribution proof.
Python standard library only. See README.md for provenance and limitations.
"""
from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter

SCHEMA = "pi-ccph-epistemic-toy/v0.1"
TRUTH = ("TRUE", "FALSE", "UNKNOWN")
KINDS = ("WARNING", "HYPOTHESIS", "THEORY", "LOGIC", "CARE", "OUTPUT")


def require(checks: list[str], name: str, condition: bool) -> None:
    """Use exceptions, not assert (works under python -O too)."""
    if not condition:
        raise RuntimeError("FAILED " + name)
    checks.append(name)


def epistemic_warning(truth: str, reported: bool) -> str:
    if not reported:
        return "NO_REPORTED_WARNING"
    return {
        "TRUE": "VERIFIED_TRUE_DETECTION",
        "FALSE": "VERIFIED_FALSE_ALARM",
        "UNKNOWN": "UNRESOLVED_WARNING",
    }[truth]


def warning_world(actor: str, truth: str, reported: bool, acted: bool) -> dict:
    # Net scores are *deliberately* invented toy numbers, not real money/harm.
    benefit = int(truth == "TRUE" and reported and acted)
    false_action_cost = int(truth == "FALSE" and reported and acted)
    return {
        "actor": actor,
        "truth": truth,
        "reported": reported,
        "acted": acted,
        "terminal_net": benefit - false_action_cost,
        "warning_status": epistemic_warning(truth, reported),
        "actual_prevention": bool(benefit),
        "false_response_cost": bool(false_action_cost),
        "raw_report_baseline": int(reported),
        "profit_only_baseline": int(benefit - false_action_cost > 0),
    }


# Deliberately hand-constructed *events*, not measured people or publications.
# A fixture may label truth because the designer stipulates it; no model
# independently discovered that truth. That is the most important limitation.
EVENTS = [
    {"id": "ignored_true_warning", "kind": "WARNING", "truth": "TRUE", "novel": "UNKNOWN", "checked": True, "terminal_net": 0, "actor": "A"},
    {"id": "ignored_false_alarm", "kind": "WARNING", "truth": "FALSE", "novel": "UNKNOWN", "checked": True, "terminal_net": 0, "actor": "B"},
    {"id": "ignored_unknown_warning", "kind": "WARNING", "truth": "UNKNOWN", "novel": "UNKNOWN", "checked": False, "terminal_net": 0, "actor": "A"},
    {"id": "new_testable_hypothesis", "kind": "HYPOTHESIS", "truth": "UNKNOWN", "novel": "TRUE", "checked": False, "terminal_net": 0, "actor": "A"},
    {"id": "old_hypothesis_rephrased", "kind": "HYPOTHESIS", "truth": "UNKNOWN", "novel": "FALSE", "checked": False, "terminal_net": 0, "actor": "B"},
    {"id": "new_theory_candidate", "kind": "THEORY", "truth": "UNKNOWN", "novel": "TRUE", "checked": False, "terminal_net": 0, "actor": "A"},
    {"id": "logically_valid_refutation", "kind": "LOGIC", "truth": "TRUE", "novel": "TRUE", "checked": True, "terminal_net": 0, "actor": "B"},
    {"id": "logically_invalid_refutation", "kind": "LOGIC", "truth": "FALSE", "novel": "TRUE", "checked": True, "terminal_net": 0, "actor": "A"},
    {"id": "useful_outcome_no_discovery_trace", "kind": "OUTPUT", "truth": "UNKNOWN", "novel": "UNKNOWN", "checked": False, "terminal_net": 1, "actor": "B"},
    {"id": "harmful_output", "kind": "OUTPUT", "truth": "UNKNOWN", "novel": "UNKNOWN", "checked": False, "terminal_net": -1, "actor": "A"},
    {"id": "unpriced_care", "kind": "CARE", "truth": "UNKNOWN", "novel": "UNKNOWN", "checked": False, "terminal_net": 0, "actor": "B"},
]


def classify_event(event: dict) -> str:
    kind = event["kind"]
    truth, novel, checked = event["truth"], event["novel"], event["checked"]
    if kind == "WARNING":
        if not checked or truth == "UNKNOWN":
            return "E_WARNING_UNRESOLVED"
        return "E_WARNING_TRUE" if truth == "TRUE" else "E_WARNING_FALSE"
    if kind in ("HYPOTHESIS", "THEORY"):
        if novel == "FALSE":
            return "E_PRIOR_ART_NOT_NEW"
        if novel != "TRUE":
            return "E_NOVELTY_UNRESOLVED"
        if checked and truth == "TRUE":
            return "E_CHECKED_" + kind
        if checked and truth == "FALSE":
            return "E_FALSIFIED_" + kind
        return "E_" + kind + "_CANDIDATE"
    if kind == "LOGIC":
        if not checked or truth == "UNKNOWN":
            return "E_LOGIC_UNRESOLVED"
        if truth == "FALSE":
            return "E_LOGIC_INVALID"
        if novel != "TRUE":
            return "E_LOGIC_PRIOR_ART_OR_UNRESOLVED"
        return "E_LOGIC_VALID"
    if kind == "CARE":
        return "A_CARE_UNPRICED"
    if kind == "OUTPUT":
        return "O_ONLY"
    raise ValueError("Unexpected event kind")


def score_events(events: list[dict]) -> list[dict]:
    return [
        {
            "id": x["id"],
            "actor": x["actor"],
            "outcome_only_recognized": x["terminal_net"] > 0,
            "count_only_recognized": x["kind"] in ("WARNING", "HYPOTHESIS", "THEORY", "LOGIC"),
            "separate_ledger_status": classify_event(x),
            "actual_downstream_net": x["terminal_net"],
            # Separate legal/human standing is never calculated from net output.
            "refusal_and_care_rights": "INDEPENDENT_OF_PRODUCTIVITY",
            "verified_payment": "UNKNOWN",
        }
        for x in events
    ]


def run() -> dict:
    checks: list[str] = []
    worlds = [
        warning_world(actor, truth, reported, acted)
        for actor, truth, reported, acted in itertools.product(
            ("A", "B"), TRUTH, (False, True), (False, True)
        )
    ]
    require(checks, "24_complete_warning_worlds", len(worlds) == 24)
    require(checks, "all_actors_12_each", Counter(w["actor"] for w in worlds) == {"A": 12, "B": 12})
    require(checks, "world_combinations_unique", len({(w["actor"], w["truth"], w["reported"], w["acted"]) for w in worlds}) == 24)
    for w in worlds:
        require(checks, "truth_action_consistency_" + str(len(checks)),
                w["actual_prevention"] == (w["truth"] == "TRUE" and w["reported"] and w["acted"]))
        require(checks, "false_cost_consistency_" + str(len(checks)),
                w["false_response_cost"] == (w["truth"] == "FALSE" and w["reported"] and w["acted"]))
        require(checks, "unknown_not_credited_" + str(len(checks)),
                w["warning_status"] != "VERIFIED_TRUE_DETECTION" or (w["truth"] == "TRUE" and w["reported"]))
        require(checks, "role_label_invariance_" + str(len(checks)),
                {k: v for k, v in w.items() if k != "actor"} ==
                {k: v for k, v in warning_world("B" if w["actor"] == "A" else "A",
                                                  w["truth"], w["reported"], w["acted"]).items()
                 if k != "actor"})
    true_ignored = warning_world("A", "TRUE", True, False)
    false_ignored = warning_world("B", "FALSE", True, False)
    require(checks, "terminal_projection_collision", true_ignored["terminal_net"] == false_ignored["terminal_net"] == 0)
    require(checks, "distinct_hidden_epistemic_states", true_ignored["warning_status"] != false_ignored["warning_status"])
    require(checks, "ignored_true_is_not_prevented", true_ignored["warning_status"] == "VERIFIED_TRUE_DETECTION" and not true_ignored["actual_prevention"])
    require(checks, "false_warning_count_only_false_credit",
            false_ignored["raw_report_baseline"] == 1 and false_ignored["warning_status"] == "VERIFIED_FALSE_ALARM")
    require(checks, "unknown_never_true", epistemic_warning("UNKNOWN", True) == "UNRESOLVED_WARNING")
    require(checks, "true_acted_prevention", warning_world("A", "TRUE", True, True)["terminal_net"] == 1)
    require(checks, "false_acted_harm", warning_world("A", "FALSE", True, True)["terminal_net"] == -1)

    rows = score_events(EVENTS)
    events_by_id = {x["id"]: x for x in rows}
    require(checks, "events_unique", len(events_by_id) == len(EVENTS) == 11)
    require(checks, "ignored_true_credit_without_profit",
            events_by_id["ignored_true_warning"]["separate_ledger_status"] == "E_WARNING_TRUE" and
            not events_by_id["ignored_true_warning"]["outcome_only_recognized"])
    require(checks, "false_alarm_not_true",
            events_by_id["ignored_false_alarm"]["separate_ledger_status"] == "E_WARNING_FALSE")
    require(checks, "unknown_warning_stays_unknown",
            events_by_id["ignored_unknown_warning"]["separate_ledger_status"] == "E_WARNING_UNRESOLVED")
    require(checks, "untested_novel_hypothesis_only_candidate",
            events_by_id["new_testable_hypothesis"]["separate_ledger_status"] == "E_HYPOTHESIS_CANDIDATE")
    require(checks, "duplicate_not_new",
            events_by_id["old_hypothesis_rephrased"]["separate_ledger_status"] == "E_PRIOR_ART_NOT_NEW")
    require(checks, "untested_theory_only_candidate",
            events_by_id["new_theory_candidate"]["separate_ledger_status"] == "E_THEORY_CANDIDATE")
    require(checks, "valid_logic_not_revenue_dependent",
            events_by_id["logically_valid_refutation"]["separate_ledger_status"] == "E_LOGIC_VALID" and
            not events_by_id["logically_valid_refutation"]["outcome_only_recognized"])
    require(checks, "invalid_logic_not_promoted",
            events_by_id["logically_invalid_refutation"]["separate_ledger_status"] == "E_LOGIC_INVALID")
    require(checks, "care_not_hidden_by_zero_profit",
            events_by_id["unpriced_care"]["separate_ledger_status"] == "A_CARE_UNPRICED")
    require(checks, "harmful_output_not_success",
            events_by_id["harmful_output"]["actual_downstream_net"] == -1 and
            not events_by_id["harmful_output"]["outcome_only_recognized"])
    require(checks, "basic_rights_unconditional",
            all(r["refusal_and_care_rights"] == "INDEPENDENT_OF_PRODUCTIVITY" for r in rows))
    require(checks, "nonpayment_not_fabricated",
            all(r["verified_payment"] == "UNKNOWN" for r in rows))

    # Same artifact can have more than one contributor or mention. Do not
    # multiply total outcome by the number of upstream mentions/parents.
    artifact_mentions = [
        {"artifact_id": "X", "parents": ("A", "B")},
        {"artifact_id": "X", "parents": ("B", "C")},
        {"artifact_id": "Y", "parents": ("B",)},
    ]
    unique_artifact_ids = len({x["artifact_id"] for x in artifact_mentions})
    require(checks, "multi_parent_duplicate_removed", unique_artifact_ids == 2)
    # Honest negative control: without original source and adjudication,
    # the process cannot assign causal or monetary credit to contributors.
    require(checks, "no_exclusive_causal_credit_inferred",
            any(len(x["parents"]) > 1 for x in artifact_mentions))

    summary = {
        "schema": SCHEMA,
        "evidence_class": "PROJECT_SELF_RUN_POST_HOC_DETERMINISTIC_SYNTHETIC_DIAGNOSTIC",
        "not": ["human study", "new empirical CCPH effect", "statistical power estimate",
                "independent replication", "preregistered experiment",
                "proof of policy superiority", "financial valuation"],
        "synthetic_warning_worlds": len(worlds),
        "distinct_epistemic_states_same_terminal_observation": True,
        "illustrative_events": len(EVENTS),
        "toy_counts": {
            "outcome_only_positive": sum(x["outcome_only_recognized"] for x in rows),
            "raw_event_count_positive": sum(x["count_only_recognized"] for x in rows),
            "confirmed_true_warning_events": sum(x["separate_ledger_status"] == "E_WARNING_TRUE" for x in rows),
            "confirmed_valid_logic_events": sum(x["separate_ledger_status"] == "E_LOGIC_VALID" for x in rows),
            "unresolved_warning_events": sum(x["separate_ledger_status"] == "E_WARNING_UNRESOLVED" for x in rows),
        },
        "unique_artifacts_in_3_mentions": unique_artifact_ids,
        "checks_passed": len(checks),
        "failed_checks": 0,
        "event_results": rows,
        "interpretation": "Endpoint-only projection is non-injective in the specified toy world. "
            "Independently coded epistemic events retain distinctions, but the fixtures stipulate "
            "truth/novelty: results do NOT measure actual superiority or causal welfare.",
        "next": "Blind external judges, independently randomized dyads (G, not task count), "
            "prespecified scoring, resource-matched baselines, false alarm costs, and negative findings.",
    }
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="CCPH deterministic toy observability audit")
    parser.add_argument("--verify", action="store_true", help="fail on violated checks (checks always enforced)")
    parser.parse_args()
    print(json.dumps(run(), ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

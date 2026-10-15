#!/usr/bin/env python3
"""E008 optional numerical-input contract. Checks data integrity, NEVER ranks policies.

Original preregistered E008 qualitative scenarios and amendments remain frozen.
An accepted schema is not a validated utility model, policy implementation,
independent evaluation, or a result of the five-policy main experiment.
"""
import argparse
import copy
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "scenario_matrix.json"
FROZEN_GIT_BLOB_SHA1 = "bf7d863182844c21ce2de5f63006eea127962b80"
POLICIES = (
    "MYOPIC_SCALAR", "LONG_HORIZON_EV", "CONSTRAINED_RECEDING",
    "ROBUST_CONSTRAINED", "PROJECT_V2",
)
SCHEMA = "E008_OPTIONAL_NUMERIC_COMPLETION_V0_1"
# Input-only schema: unrecognized top-level keys must never carry result claims.
ALLOWED_COMPLETION_FIELDS = frozenset({
    "schema", "source_git_blob_sha1", "evidence_status",
    "method_declaration", "role_swap_specification", "cases",
})


def require(test, reason):
    if not test:
        raise ValueError(reason)


def exact_number(value, field):
    require(type(value) in (int, float) and math.isfinite(value),
            "nonfinite/missing/non-numeric " + field)
    return float(value)


def frozen_source():
    raw = SOURCE.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\x00" + raw).hexdigest()
    require(blob == FROZEN_GIT_BLOB_SHA1,
            "original E008 matrix changed: stop, do not move source anchor")
    data = json.loads(raw)
    require(data["status"] == "PREREGISTERED_SPECIFICATION_NO_RESULT",
            "original preregistration status drift")
    require(tuple(data["baselines"]) == POLICIES, "policy set drift")
    require(len(data["cases"]) == 16, "expected 16 qualitative cases")
    ids = {r["id"] for r in data["cases"]}
    require(len(ids) == 16, "duplicate qualitative case ids")
    for r in data["cases"]:
        counterpart = next((x for x in data["cases"] if x["id"] == r["pair"]), None)
        require(counterpart is not None and counterpart["pair"] == r["id"],
                "broken source pair")
    return data


def swapped_actor_outcome_match(a, b):
    """Compares declared label-only twins, not real-world heterogeneous actors."""
    if a["probability"] != b["probability"]:
        return False
    if a["intervention_cost"] != b["intervention_cost"]:
        return False
    if a["recovery_cost"] != b["recovery_cost"]:
        return False
    for name in ("utilities", "living_floor_met", "effective_exit",
                 "irreversible_harm"):
        if a[name]["A"] != b[name]["B"] or a[name]["B"] != b[name]["A"]:
            return False
    return True


def swapped_actor_outcomes_match(first, second):
    """Check a multiset of outcomes: distribution records have no order semantics."""
    if len(first) != len(second):
        return False
    unmatched = list(second)
    for outcome in first:
        match_index = next(
            (i for i, candidate in enumerate(unmatched)
             if swapped_actor_outcome_match(outcome, candidate)),
            None,
        )
        if match_index is None:
            return False
        unmatched.pop(match_index)
    return not unmatched


def audit_declared_role_twins(rows, original):
    """Requires explicit label-only mirror OR reports role heterogeneity HOLD.

    A label-only mirror is an assumption made by a submitter, not a demonstrated
    causal identity or post-reversal field observation.
    """
    original_by_id = {case["id"]: case for case in original["cases"]}
    by_id = {row["case_id"]: row for row in rows}
    discrepancies = []
    reviewed = set()
    for key in sorted(by_id):
        mate = original_by_id[key]["pair"]
        if mate in reviewed:
            continue
        reviewed.add(key)
        reviewed.add(mate)
        own = {a["id"]: a for a in by_id[key]["actions"]}
        twin = {a["id"]: a for a in by_id[mate]["actions"]}
        for aid in sorted(own):
            outs1 = own[aid]["outcomes"]
            outs2 = twin[aid]["outcomes"]
            if not swapped_actor_outcomes_match(outs1, outs2):
                discrepancies.append((key, mate, aid))
    return {"pair_count": len(reviewed) // 2,
            "label_only_mirror_discrepancies": discrepancies}


def validate_completion(completion, original):
    require(type(completion) is dict, "completion must be object")
    require(set(completion) <= ALLOWED_COMPLETION_FIELDS,
            "unknown top-level field: input-only evidence boundary")
    require(completion.get("schema") == SCHEMA, "schema version mismatch")
    require(completion.get("source_git_blob_sha1") == FROZEN_GIT_BLOB_SHA1,
            "wrong source lineage")
    require(completion.get("evidence_status") == "INPUT_ONLY_UNVERIFIED",
            "do not assert validated/independent E008 outcomes")
    require(not any(k in completion for k in (
        "winner", "winners", "results", "rankings", "empirical_effect",
        "independently_validated", "project_v2_survives")),
        "outcome claim inserted into input-only contract")
    declaration = completion.get("method_declaration")
    require(type(declaration) is dict, "missing method declaration")
    require(set(declaration) == set(POLICIES), "five equal policy declarations required")
    for name in POLICIES:
        spec = declaration[name]
        require(type(spec) is dict
                and type(spec.get("version")) is str and bool(spec["version"].strip())
                and type(spec.get("specification")) is str
                and bool(spec["specification"].strip()),
                "missing algorithm version/source for " + name)
    swap_mode = completion.get("role_swap_specification")
    require(swap_mode in ("LABEL_SYMMETRIC", "HETEROGENEITY_UNIDENTIFIED"),
            "role reversal semantics required")
    rows = completion.get("cases")
    require(type(rows) is list and len(rows) == 16,
            "exactly 16 numeric case records required")
    lookup = {r["id"]: r for r in original["cases"]}
    seen = set()
    all_action_sets = set()
    for row in rows:
        require(type(row) is dict, "invalid case entry")
        key = row.get("case_id")
        require(type(key) is str and key in lookup and key not in seen,
                "unknown/duplicate case")
        seen.add(key)
        require(row.get("role") == lookup[key]["role"],
                "role metadata drift: " + key)
        actions = row.get("actions")
        require(type(actions) is list and len(actions) >= 2,
                "two or more choices required: " + key)
        action_ids = set()
        for action in actions:
            require(type(action) is dict, "invalid action")
            aid = action.get("id")
            require(type(aid) is str and bool(aid.strip()) and aid not in action_ids,
                    "duplicate/missing action id: " + key)
            action_ids.add(aid)
            branches = action.get("outcomes")
            require(type(branches) is list and len(branches) >= 1,
                    "missing action-dependent consequences: " + key)
            total = 0.0
            for outcome in branches:
                require(type(outcome) is dict, "invalid action outcome")
                p = exact_number(outcome.get("probability"), "probability")
                require(0 <= p <= 1, "invalid probability")
                total += p
                utilities = outcome.get("utilities")
                floors = outcome.get("living_floor_met")
                exits = outcome.get("effective_exit")
                harms = outcome.get("irreversible_harm")
                require(type(utilities) is dict and set(utilities) == {"A", "B"},
                        "distinct A/B utilities required")
                for actor in ("A", "B"):
                    exact_number(utilities[actor], "utility_" + actor)
                for field, val in (("floor", floors), ("exit", exits),
                                   ("harm", harms)):
                    require(type(val) is dict and set(val) == {"A", "B"}
                            and all(type(val[a]) is bool for a in ("A", "B")),
                            "missing actor-specific " + field)
                for cost_key in ("intervention_cost", "recovery_cost"):
                    cost = exact_number(outcome.get(cost_key), cost_key)
                    require(cost >= 0, "negative cost")
            require(abs(total - 1.0) <= 1e-10,
                    "action probabilities do not sum to one: " + key)
        all_action_sets.add(tuple(sorted(action_ids)))
    require(len(all_action_sets) == 1,
            "unequal action sets across policies/cases: NOT_COMPARABLE")
    require(seen == set(lookup), "case coverage not complete")
    mirror_audit = audit_declared_role_twins(rows, original)
    require(mirror_audit["pair_count"] == 8, "missing role reversal pair")
    if swap_mode == "LABEL_SYMMETRIC":
        require(not mirror_audit["label_only_mirror_discrepancies"],
                "claimed label-only role reversal is not mirrored")
    return {
        "status": ("SCHEMA_ACCEPTED_POLICY_COMPARISON_STILL_HOLD"
                   if swap_mode == "LABEL_SYMMETRIC"
                   else "SCHEMA_ACCEPTED_ROLE_REVERSAL_UNIDENTIFIED_HOLD"),
        "declared_role_swap_semantics": swap_mode,
        "role_twin_audit": mirror_audit,
        "unique_cases": 16,
        "distinct_role_pairs": 8,
        "actions_per_case": len(next(iter(all_action_sets))),
        "evidence": "INPUT_ONLY_UNVERIFIED",
        "unresolved": [
            "actual independently justified numeric semantics and time horizon",
            "executable and independently reviewed five policy implementations",
            "policy-independent outcome evaluator and fair information budget",
            "holdout and negative controls; no result-based specification changes",
            "third-party independence and real-world causal validity",
        ],
    }


def fixture(original):
    rows = []
    for item in original["cases"]:
        actions = []
        for aid in ("protect", "extract"):
            actions.append({"id": aid, "outcomes": [{
                "probability": 1.0, "utilities": ({"A": 1.0, "B": 0.0}
                    if item["role"].startswith("A_") else {"A": 0.0, "B": 1.0}),
                "living_floor_met": {"A": True, "B": True},
                "effective_exit": {"A": True, "B": True},
                "irreversible_harm": {"A": False, "B": False},
                "intervention_cost": 0.1, "recovery_cost": 0.0,
            }]})
        rows.append({"case_id": item["id"], "role": item["role"],
                     "actions": actions})
    return {
        "schema": SCHEMA, "source_git_blob_sha1": FROZEN_GIT_BLOB_SHA1,
        "role_swap_specification": "LABEL_SYMMETRIC",
        "evidence_status": "INPUT_ONLY_UNVERIFIED",
        "method_declaration": {p: {
            "version": "PLACEHOLDER_NOT_EXECUTABLE",
            "specification": "Unverified placeholder for schema smoke test"
        } for p in POLICIES},
        "cases": rows,
    }


def self_test(original):
    clean = fixture(original)
    require(validate_completion(clean, original)["unique_cases"] == 16,
            "valid constructed fixture not accepted")

    # Probabilistic branches are an unordered multiset, not a paired row order.
    # Reversing only the -R twin must not invent a causal difference.
    permuted = copy.deepcopy(clean)
    for row in permuted["cases"]:
        for action in row["actions"]:
            lower = copy.deepcopy(action["outcomes"][0])
            upper = copy.deepcopy(action["outcomes"][0])
            lower["probability"] = 0.25
            upper["probability"] = 0.75
            action["outcomes"] = ([upper, lower] if row["case_id"].endswith("-R")
                                  else [lower, upper])
    require(validate_completion(permuted, original)["unique_cases"] == 16,
            "equivalent permuted role-twin outcomes were rejected")
    corrupted = copy.deepcopy(permuted)
    corrupted["cases"][1]["actions"][0]["outcomes"][0]["intervention_cost"] = 0.2
    try:
        validate_completion(corrupted, original)
    except ValueError:
        pass
    else:
        raise AssertionError("mismatched role-twin outcome escaped despite permutation")
    mutations = [
        ("false independence", lambda x: x.update(evidence_status="EMPIRICAL_VALIDATED")),
        ("injected winner", lambda x: x.update(winner="PROJECT_V2")),
        ("renamed result claim", lambda x: x.update(
            claimed_results={"winner": "PROJECT_V2"})),
        ("renamed independence claim", lambda x: x.update(
            external_validation_report={"status": "VALIDATED"})),
        ("missing case", lambda x: x["cases"].pop()),
        ("duplicate case", lambda x: x["cases"][1].update(
            case_id=x["cases"][0]["case_id"])),
        ("role drift", lambda x: x["cases"][0].update(role="A_strong_B_strong")),
        ("probability error", lambda x: x["cases"][0]["actions"][0]["outcomes"][0].update(
            probability=0.3)),
        ("missing outcome", lambda x: x["cases"][0]["actions"][0].update(outcomes=[])),
        ("zero exit data", lambda x: x["cases"][0]["actions"][0]["outcomes"][0].pop(
            "effective_exit")),
        ("unequal actions", lambda x: x["cases"][0]["actions"].pop()),
        ("wrong source", lambda x: x.update(source_git_blob_sha1="0" * 40)),
        ("missing algorithm", lambda x: x["method_declaration"].pop("PROJECT_V2")),
        ("nonfinite utility", lambda x: x["cases"][0]["actions"][0]["outcomes"][0][
            "utilities"].update(A=float("nan"))),
        ("unregistered role swap", lambda x: x.pop("role_swap_specification")),
        ("false symmetric twin", lambda x: x["cases"][1]["actions"][0]["outcomes"][0][
            "utilities"].update(A=1.0, B=0.0)),
    ]
    for label, modify in mutations:
        specimen = copy.deepcopy(clean)
        modify(specimen)
        try:
            validate_completion(specimen, original)
        except ValueError:
            continue
        raise AssertionError("negative control escaped: " + label)
    unclear = copy.deepcopy(clean)
    unclear["role_swap_specification"] = "HETEROGENEITY_UNIDENTIFIED"
    unclear["cases"][1]["actions"][0]["outcomes"][0]["utilities"] = {"A": 1.0, "B": 0.0}
    unclear_result = validate_completion(unclear, original)
    require(unclear_result["status"] ==
            "SCHEMA_ACCEPTED_ROLE_REVERSAL_UNIDENTIFIED_HOLD" and
            bool(unclear_result["role_twin_audit"]["label_only_mirror_discrepancies"]),
            "undetermined role-reversal contamination was hidden")
    return {
        "status": "PASS_SCHEMA_SMOKE_ONLY",
        "negative_controls_rejected": len(mutations),
        "uncertain_role_reversal_held": True,
        "permuted_equivalent_branches_accepted": True,
        "permuted_mismatched_branches_rejected": True,
        "negative_controls": [x[0] for x in mutations],
        "experiment_result": "NOT_EXECUTED",
        "independent_evaluation": "NOT_OBTAINED",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--completion", type=Path)
    args = parser.parse_args()
    original = frozen_source()
    if args.self_test:
        result = self_test(original)
    elif args.completion:
        result = validate_completion(json.loads(args.completion.read_text(
            encoding="utf-8")), original)
    else:
        result = {
            "status": "HOLD_UNDERDETERMINED_ACTION_OUTCOMES",
            "cases": len(original["cases"]),
            "policy_count": len(POLICIES),
            "accepted_main_experiment_results": 0,
            "schema_available": SCHEMA,
        }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

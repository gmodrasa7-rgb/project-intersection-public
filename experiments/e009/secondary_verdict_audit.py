#!/usr/bin/env python3
"""Secondary arithmetic audit of E009 published verdict; same project lineage.

Does not use benchmark choose(), consequence(), or reported verdict logic.
NOT an independent scientific implementation or external replication.
"""
import copy
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASELINES = ("TWO_RULE_SIMPLE", "SECURITY_BOUNDED", "MINIMAL_4VAR")
POLICIES = ("MAK_PLUS_POINTWISE", *BASELINES, "PROJECT_V3")
PROFILES = ("safety_heavy", "balanced", "adaptability_heavy")
CRITERIA = (
    "criterion_regret_5pct_better_than_best_simple",
    "criterion_recovery_no_more_than_2pct_worse_than_best_C_or_M4",
    "criterion_severe_harm_no_more_than_2pp_worse_than_best_C_or_M4",
    "criterion_no_weight_profile_regret_over_10pct_worse_than_best_simple",
)

def require(condition, message):
    if not condition:
        raise ValueError(message)

def number(value, name):
    require(isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value), f"{name}: nonfinite or nonnumeric")
    return value

def checked_action_counts(actions, n, label):
    """Reject impossible counts even if the aggregate sums stay unchanged."""
    require(type(n) is int and n > 0, f"{label}: row count must be a positive integer")
    require(isinstance(actions, dict) and set(actions) ==
            {"ALLOW", "BLOCK", "EXPERIMENT", "MONITOR"},
            f"{label}: invalid action inventory")
    require(all(type(value) is int and 0 <= value <= n
                for value in actions.values()),
            f"{label}: action counts must be nonnegative integers")
    require(sum(actions.values()) == n,
            f"{label}: action total disagrees with row count")


def audit(result, receipt):
    require(result.get("status") == "SYNTHETIC_PROJECT_RERUN_NOT_INDEPENDENT_VALIDATION",
            "invalid result evidence class")
    require(receipt.get("independent_validation") is False, "independence falsely claimed")
    require(receipt.get("policy_or_threshold_changes_after_spec_merge") is False,
            "reported post-spec tuning")
    require(receipt.get("executable_spec_commit")
            == "c36ba8e6d6df1eedcd54ca6c36091bf822fe6ace", "frozen spec changed")
    require(result.get("case_count") == 32
            and isinstance(result.get("policies"), list)
            and len(result["policies"]) == len(POLICIES)
            and set(result["policies"]) == set(POLICIES),
            "frozen case/policy inventory changed")
    primary = result["stress_primary"]
    profiles = result["stress_by_weight_profile"]
    require(set(primary) == set(POLICIES), "primary policy missing")
    require(set(profiles) == set(PROFILES), "frozen scoring profile missing")
    for policy in POLICIES:
        p = primary[policy]
        checked_action_counts(p["actions"], p["n"], f"{policy}.stress_primary")
        require(p["n"] == 9600, f"{policy}: primary row count")
        for field in ("mean_regret", "mean_recovery", "severe_harm_rate"):
            number(p[field], f"{policy}.{field}")
        require(0 <= p["severe_harm_rate"] <= 1, "severe harm fraction outside [0,1]")
        require(abs(p["severe_harm_rate"] * 3200
                    - round(p["severe_harm_rate"] * 3200)) < 1e-9,
                f"{policy}: severe-event count not integral for unique decisions")
        rows = [profiles[w][policy] for w in PROFILES]
        for w in PROFILES:
            row = profiles[w][policy]
            checked_action_counts(row["actions"], row["n"], f"{policy}.{w}")
        require(all(row["n"] == 3200 for row in rows), f"{policy}: per-profile count")
        require(all(row["actions"] == rows[0]["actions"] for row in rows),
                f"{policy}: actions unexpectedly depend on scoring weights")
        require(all(p["actions"][a] == 3 * rows[0]["actions"][a] for a in p["actions"]),
                f"{policy}: thrice-scored decisions mismatch")
        require(abs(p["mean_regret"] -
                    sum(row["mean_regret"] for row in rows) / 3) < 1e-12,
                f"{policy}: average regret contradicts profiles")
        require(all(abs(p["mean_recovery"] - row["mean_recovery"]) < 1e-12
                    for row in rows), f"{policy}: profile recovery drift")
        require(all(abs(p["severe_harm_rate"] - row["severe_harm_rate"]) < 1e-12
                    for row in rows), f"{policy}: profile severe rate drift")

    v3 = primary["PROJECT_V3"]
    baseline_regret = min(primary[x]["mean_regret"] for x in BASELINES)
    best_recovery = min(primary[x]["mean_recovery"]
                        for x in ("SECURITY_BOUNDED", "MINIMAL_4VAR"))
    best_severe = min(primary[x]["severe_harm_rate"]
                      for x in ("SECURITY_BOUNDED", "MINIMAL_4VAR"))
    require(baseline_regret > 0, "invalid regret denominator")
    computed = {
        CRITERIA[0]: v3["mean_regret"] <= .95 * baseline_regret,
        CRITERIA[1]: v3["mean_recovery"] <= 1.02 * best_recovery,
        CRITERIA[2]: v3["severe_harm_rate"] <= best_severe + .02,
        CRITERIA[3]: all(
            profiles[w]["PROJECT_V3"]["mean_regret"] <=
            1.10 * min(profiles[w][x]["mean_regret"] for x in BASELINES)
            for w in PROFILES),
    }
    computed["project_v3_residual_survives"] = all(computed[c] for c in CRITERIA)
    require(result.get("survival_criteria") == computed,
            "recorded verdict differs from separately recomputed conditions")
    improvement = 1 - v3["mean_regret"] / baseline_regret
    require(abs(result["project_v3_vs_best_simple_regret_improvement"]
                - improvement) < 1e-12, "reported regret improvement drift")
    require(abs(v3["severe_harm_rate"] * 3200 - 53) < 1e-9,
            "known 53 synthetic severe events changed")
    return {"status": "PASS", "evidence_class": "INTERNAL_SECONDARY_ARITHMETIC_AUDIT",
            "criterion_values": computed,
            "v3_regret_worse_percent": round(-100 * improvement, 6),
            "v3_severe_events_per_3200": 53}

def poison_negative_actions_preserving_totals(result):
    """Original 12 / 4 ALLOW counts become -3 / -1; all sums still match."""
    policy = "PROJECT_V3"
    primary = result["stress_primary"][policy]["actions"]
    primary["ALLOW"] -= 15
    primary["BLOCK"] += 15
    for profile in PROFILES:
        actions = result["stress_by_weight_profile"][profile][policy]["actions"]
        actions["ALLOW"] -= 5
        actions["BLOCK"] += 5


def poison_fractional_actions_preserving_totals(result):
    policy = "PROJECT_V3"
    primary = result["stress_primary"][policy]["actions"]
    primary["ALLOW"] += 1.5
    primary["BLOCK"] -= 1.5
    for profile in PROFILES:
        actions = result["stress_by_weight_profile"][profile][policy]["actions"]
        actions["ALLOW"] += 0.5
        actions["BLOCK"] -= 0.5


def main():
    result = json.loads((ROOT / "RESULT.json").read_text(encoding="utf-8"))
    receipt = json.loads((ROOT / "EXECUTION_RECEIPT.json").read_text(encoding="utf-8"))
    src = (ROOT / "benchmark.py").read_bytes()
    require(hashlib.sha256(src).hexdigest() == receipt["benchmark_sha256"],
            "frozen benchmark SHA-256 mismatch")
    git_blob = hashlib.sha1(b"blob " + str(len(src)).encode() + b"\x00" + src).hexdigest()
    require(git_blob == receipt["benchmark_git_blob_sha"],
            "frozen Git blob SHA mismatch")
    report = audit(result, receipt)
    # Mutations MUST be rejected: detect tampering, omissions and false claims.
    negatives = [
        ("false independent validation", "receipt",
         lambda d: d.__setitem__("independent_validation", True)),
        ("reversed published verdict", "result",
         lambda d: d["survival_criteria"].__setitem__("project_v3_residual_survives", True)),
        ("manipulated primary regret", "result",
         lambda d: d["stress_primary"]["PROJECT_V3"].__setitem__("mean_regret", .001)),
        ("missing preregistered profile", "result",
         lambda d: d["stress_by_weight_profile"].pop("balanced")),
        ("duplicate policy label despite unchanged policy set", "result",
         lambda d: d["policies"].append("PROJECT_V3")),
        ("duplicated row count", "result",
         lambda d: d["stress_primary"]["PROJECT_V3"].__setitem__("n", 19200)),
        ("negative action counts despite valid totals and profile ratios", "result",
         poison_negative_actions_preserving_totals),
        ("fractional action counts despite valid totals and profile ratios", "result",
         poison_fractional_actions_preserving_totals),
    ]
    for name, target, mutation in negatives:
        r, rec = copy.deepcopy(result), copy.deepcopy(receipt)
        mutation(r if target == "result" else rec)
        try:
            audit(r, rec)
        except (ValueError, KeyError):
            continue
        raise ValueError(f"negative control passed unexpectedly: {name}")
    report["negative_controls_rejected"] = len(negatives)
    print(json.dumps(report, sort_keys=True))

if __name__ == "__main__":
    main()

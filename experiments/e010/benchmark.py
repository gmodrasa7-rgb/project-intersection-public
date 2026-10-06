#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
MATRIX = HERE / "scenario_matrix.json"

ACTIONS = ("PASS", "REVIEW", "RESTRICT")
INPUT_COUNT = {
    "OBJECT_ONLY": 1,
    "IMPARTIAL_INSPECTOR": 4,
    "CONTESTABLE_LIFECYCLE": 10,
    "CONTESTABLE_COST_AWARE": 12,
    "POWER_REVERSAL_META": 12,
}
COMPLEXITY_COEF = 0.0025

WEIGHTS = {
    "safety-heavy": {
        "false_pass": .24, "false_block": .08, "irreversible_harm": .24,
        "delay_harm": .10, "proof_repair_burden": .06,
        "exit_loss_realized": .06, "evidence_failure": .14,
        "reporting_suppression": .08,
    },
    "balanced": {
        "false_pass": .16, "false_block": .12, "irreversible_harm": .18,
        "delay_harm": .10, "proof_repair_burden": .12,
        "exit_loss_realized": .12, "evidence_failure": .12,
        "reporting_suppression": .08,
    },
    "autonomy-heavy": {
        "false_pass": .10, "false_block": .18, "irreversible_harm": .14,
        "delay_harm": .10, "proof_repair_burden": .16,
        "exit_loss_realized": .18, "evidence_failure": .08,
        "reporting_suppression": .06,
    },
}

def clip(x):
    return max(0.0, min(1.0, float(x)))

def mean(*xs):
    return sum(xs) / len(xs)

def load_matrix():
    data = json.loads(MATRIX.read_text(encoding="utf-8"))
    assert data["experiment"] == "E010"
    assert data["status"] == "PREREGISTERED_NO_RESULT"
    required = set(data["fields"])
    ids = set()
    for s in data["scenarios"]:
        assert s["id"] not in ids
        ids.add(s["id"])
        assert required <= set(s)
        for k in required:
            assert isinstance(s[k], (int, float))
            assert 0 <= s[k] <= 1
    by_id = {s["id"]: s for s in data["scenarios"]}
    for s in data["scenarios"]:
        if not s.get("pair"):
            continue
        other = by_id[s["pair"]]
        for k in required:
            assert s[k] == other[k], (s["id"], s["pair"], k)
    return data

def object_only(s):
    h = s["target_hazard"]
    if h >= .68:
        return "RESTRICT"
    if h >= .38:
        return "REVIEW"
    return "PASS"

def impartial_inspector(s):
    h = s["target_hazard"]
    inspector = mean(s["inspector_capture"], s["inspector_bias"], s["evidence_asymmetry"])
    score = .70 * h + .30 * inspector
    if h >= .76 or score >= .68:
        return "RESTRICT"
    if score >= .38:
        return "REVIEW"
    return "PASS"

def contestable_lifecycle(s):
    h = s["target_hazard"]
    lifecycle = mean(
        s["reporting_chill"], s["post_deployment_drift"], s["metric_gaming"],
        s["audit_channel_integrity_risk"], s["hidden_third_party"]
    )
    inspector = mean(s["inspector_capture"], s["inspector_bias"], s["evidence_asymmetry"])
    score = .55 * h + .25 * inspector + .20 * lifecycle
    if s["emergency_urgency"] >= .80 and h >= .65:
        return "RESTRICT"
    if h >= .80 or score >= .67:
        return "RESTRICT"
    if score >= .36:
        return "REVIEW"
    return "PASS"

def contestable_cost_aware(s):
    h = s["target_hazard"]
    lifecycle = mean(
        s["reporting_chill"], s["post_deployment_drift"], s["metric_gaming"],
        s["audit_channel_integrity_risk"], s["hidden_third_party"]
    )
    inspector = mean(s["inspector_capture"], s["inspector_bias"], s["evidence_asymmetry"])
    procedural = mean(s["proof_burden"], s["exit_loss"], s["reporting_chill"])
    score = .50 * h + .22 * inspector + .18 * lifecycle + .10 * s["exit_loss"]

    if s["emergency_urgency"] >= .80 and h >= .65:
        return "RESTRICT"
    if h >= .82 or score >= .69:
        return "RESTRICT"

    # Established compliance-cost baseline: avoid high procedural burden
    # becoming its own reason to intensify controls in low-risk cases.
    if h < .30 and procedural >= .60 and inspector < .60:
        return "PASS"

    if score >= .35:
        return "REVIEW"
    return "PASS"

def power_reversal_meta(s):
    h = s["target_hazard"]
    lifecycle = mean(
        s["reporting_chill"], s["post_deployment_drift"], s["metric_gaming"],
        s["audit_channel_integrity_risk"], s["hidden_third_party"]
    )
    inspector = mean(s["inspector_capture"], s["inspector_bias"], s["evidence_asymmetry"])
    procedural = mean(s["proof_burden"], s["exit_loss"], s["reporting_chill"])
    score = .50 * h + .22 * inspector + .18 * lifecycle + .10 * s["exit_loss"]

    if s["emergency_urgency"] >= .80 and h >= .65:
        return "RESTRICT"
    if h >= .82 or score >= .69:
        return "RESTRICT"

    # Avoid turning low target risk plus high procedural burden into automatic restriction.
    if h < .30 and procedural >= .60 and inspector < .60:
        return "PASS"

    # High evaluator dependence calls for review rather than self-validating restriction.
    if inspector >= .58 or s["evidence_asymmetry"] >= .72:
        return "REVIEW"

    if score >= .35:
        return "REVIEW"
    return "PASS"

POLICIES = {
    "OBJECT_ONLY": object_only,
    "IMPARTIAL_INSPECTOR": impartial_inspector,
    "CONTESTABLE_LIFECYCLE": contestable_lifecycle,
    "CONTESTABLE_COST_AWARE": contestable_cost_aware,
    "POWER_REVERSAL_META": power_reversal_meta,
}

def consequences(s, action):
    h = s["target_hazard"]
    exposure = {"PASS": 1.0, "REVIEW": .35, "RESTRICT": .05}[action]
    restriction = {"PASS": 0.0, "REVIEW": .20, "RESTRICT": 1.0}[action]
    delay = {"PASS": 0.0, "REVIEW": .55, "RESTRICT": .10}[action]
    proof = {"PASS": .05, "REVIEW": .65, "RESTRICT": .45}[action]
    exit_factor = {"PASS": 0.0, "REVIEW": .18, "RESTRICT": .85}[action]
    evidence_factor = {"PASS": .80, "REVIEW": .25, "RESTRICT": .30}[action]
    report_factor = {"PASS": .40, "REVIEW": .18, "RESTRICT": .50}[action]

    integrity_pressure = mean(
        s["inspector_capture"], s["inspector_bias"], s["evidence_asymmetry"],
        s["audit_channel_integrity_risk"]
    )

    false_pass = clip(h * exposure)
    false_block = clip((1 - h) * restriction)
    delay_harm = clip(s["emergency_urgency"] * delay)
    irreversible_harm = clip(
        .72 * h * exposure
        + .16 * delay_harm
        + .07 * s["post_deployment_drift"] * exposure
        + .05 * s["hidden_third_party"] * exposure
    )
    proof_repair_burden = clip(s["proof_burden"] * proof)
    exit_loss_realized = clip(s["exit_loss"] * exit_factor)
    evidence_failure = clip(integrity_pressure * evidence_factor)
    reporting_suppression = clip(s["reporting_chill"] * report_factor)

    return {
        "false_pass": false_pass,
        "false_block": false_block,
        "irreversible_harm": irreversible_harm,
        "delay_harm": delay_harm,
        "proof_repair_burden": proof_repair_burden,
        "exit_loss_realized": exit_loss_realized,
        "evidence_failure": evidence_failure,
        "reporting_suppression": reporting_suppression,
    }

def weighted_loss(policy_name, dims, profile):
    w = WEIGHTS[profile]
    base = sum(w[k] * dims[k] for k in w)
    return base + COMPLEXITY_COEF * INPUT_COUNT[policy_name]

def aggregate(rows):
    out = {}
    for policy in POLICIES:
        pr = [r for r in rows if r["policy"] == policy]
        out[policy] = {}
        for profile in WEIGHTS:
            out[policy][profile] = sum(r["loss"][profile] for r in pr) / len(pr)
        for key in next(iter(pr))["dimensions"]:
            out[policy][key] = sum(r["dimensions"][key] for r in pr) / len(pr)
        out[policy]["combined_error"] = mean(
            out[policy]["false_pass"], out[policy]["false_block"]
        )
    return out

def pct_improvement(new, old):
    if old == 0:
        return 0.0 if new == 0 else -1.0
    return (old - new) / old

def survival(data, rows, agg):
    c = agg["CONTESTABLE_LIFECYCLE"]
    c2 = agg["CONTESTABLE_COST_AWARE"]
    d = agg["POWER_REVERSAL_META"]

    error_improvement = pct_improvement(d["combined_error"], c2["combined_error"])
    burden_improvement = pct_improvement(d["proof_repair_burden"], c2["proof_repair_burden"])
    no_worse_error_for_burden = d["combined_error"] <= c2["combined_error"] + 1e-12

    emergency = [
        r for r in rows
        if r["family"] == "emergency_action_vs_review_delay"
        and r["policy"] in ("CONTESTABLE_COST_AWARE", "POWER_REVERSAL_META")
    ]
    em = {r["policy"]: r for r in emergency}

    integrity = [
        r for r in rows
        if r["family"] == "audit_channel_integrity_risk"
        and r["policy"] in ("CONTESTABLE_COST_AWARE", "POWER_REVERSAL_META")
    ]
    integ = {r["policy"]: r for r in integrity}

    by_case_policy = {(r["case_id"], r["policy"]): r for r in rows}
    role_pair_same = (
        by_case_policy[("S11", "POWER_REVERSAL_META")]["action"]
        == by_case_policy[("S12", "POWER_REVERSAL_META")]["action"]
    )

    checks = {
        "error_or_burden_gain": (
            error_improvement >= .05
            or (burden_improvement >= .10 and no_worse_error_for_burden)
        ),
        "irreversible_harm_guard": d["irreversible_harm"] <= c2["irreversible_harm"] + .02,
        "emergency_delay_guard": (
            em["POWER_REVERSAL_META"]["dimensions"]["delay_harm"]
            <= em["CONTESTABLE_COST_AWARE"]["dimensions"]["delay_harm"] + .02
        ),
        "audit_integrity_guard": (
            integ["POWER_REVERSAL_META"]["loss"]["balanced"]
            <= 1.05 * integ["CONTESTABLE_COST_AWARE"]["loss"]["balanced"]
        ),
        "role_reversal_same_action": role_pair_same,
        "profile_regret_guard": all(
            d[p] <= 1.10 * c2[p] for p in WEIGHTS
        ),
    }
    return {
        "survives": all(checks.values()),
        "checks": checks,
        "diagnostics": {
            "combined_error_improvement_vs_C2": error_improvement,
            "proof_burden_improvement_vs_C2": burden_improvement,
            "C2_vs_C_balanced_loss_delta": c2["balanced"] - c["balanced"],
        },
    }

def git_prereg_is_on_main(commit):
    subprocess.run(["git", "cat-file", "-e", f"{commit}^{{commit}}"], check=True)
    r = subprocess.run(
        ["git", "merge-base", "--is-ancestor", commit, "main"],
        check=False,
    )
    if r.returncode != 0:
        raise SystemExit("Refusing result execution: preregistration commit is not on local main.")

def run():
    ap = argparse.ArgumentParser()
    ap.add_argument("--validate-only", action="store_true")
    ap.add_argument("--execute-after-prereg-merge", action="store_true")
    ap.add_argument("--prereg-commit")
    args = ap.parse_args()

    data = load_matrix()

    if args.validate_only:
        print(f"E010 validation PASS: {len(data['scenarios'])} preregistered scenarios")
        return

    if not args.execute_after_prereg_merge or not args.prereg_commit:
        raise SystemExit(
            "Before preregistration merge only --validate-only is permitted."
        )

    raise SystemExit(
        "E010 v1.1 result execution is blocked: construct mismatch found before any result. "
        "The executable benchmark does not operationalize the claimed dynamic residual. "
        "Preserve v1.0/v1.1 as design-failure lineage; define a new explicitly versioned test before execution."
    )

    git_prereg_is_on_main(args.prereg_commit)

    rows = []
    for s in data["scenarios"]:
        for policy_name, policy_fn in POLICIES.items():
            action = policy_fn(s)
            dims = consequences(s, action)
            rows.append({
                "case_id": s["id"],
                "family": s["family"],
                "policy": policy_name,
                "action": action,
                "dimensions": dims,
                "loss": {
                    profile: weighted_loss(policy_name, dims, profile)
                    for profile in WEIGHTS
                },
            })

    agg = aggregate(rows)
    result = {
        "experiment": "E010",
        "evidence_class": "PROJECT_RERUN_SYNTHETIC_NOT_INDEPENDENT_VALIDATION",
        "prereg_commit": args.prereg_commit,
        "aggregate": agg,
        "survival": survival(data, rows, agg),
        "rows": rows,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    run()

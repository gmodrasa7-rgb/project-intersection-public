#!/usr/bin/env python3
"""Post-hoc E009 matched-observation audit. Project-lineage test, NOT independent validation.

Only the observation RNG coupling is changed relative to the frozen benchmark:
original: Random(f"{case_id}|{sigma}|{seed}|{policy}")
paired:   Random(f"{case_id}|{sigma}|{seed}")
The project-authored case, choice, loss and oracle logic remain unchanged.
"""
import argparse
import json
import random
import statistics
from collections import Counter, defaultdict
from pathlib import Path
import benchmark as b

HERE = Path(__file__).resolve().parent
METRICS = ("mean_regret", "mean_recovery", "severe_harm_rate",
           "mean_exit_retention", "mean_competitive_loss")


def paired_stress():
    rows = defaultdict(list)
    actions = defaultdict(Counter)
    by_family = defaultdict(Counter)
    for case in b.make_cases():
        if case["variant"] != "stress":
            continue
        for sigma in (0.08, 0.15):
            for seed in b.NOISY_SEEDS:
                rng = random.Random(f"{case['case_id']}|{sigma}|{seed}")
                obs = b.observed(case, sigma, rng)
                for policy in b.POLICIES:
                    action = b.choose(policy, obs)
                    outcome = b.consequence(case, action)
                    is_severe = outcome["harm"] >= b.SEVERE_HARM_THRESHOLD
                    actions[policy][action] += 1
                    if is_severe:
                        by_family[policy][case["family"]] += 1
                    for profile in b.WEIGHT_PROFILES:
                        regret = max(0.0, b.scalar_loss(outcome, profile, policy)
                                     - b.oracle_loss(case, profile))
                        rows[policy].append((
                            regret, outcome["recovery"], float(is_severe),
                            outcome["exit_retention"], outcome["competitive"]
                        ))
    result = {}
    for policy in b.POLICIES:
        rr = rows[policy]
        result[policy] = {
            "n_metric_rows": len(rr),
            "n_unique_policy_actions": sum(actions[policy].values()),
            "mean_regret": statistics.fmean(x[0] for x in rr),
            "mean_recovery": statistics.fmean(x[1] for x in rr),
            "severe_harm_rate": statistics.fmean(x[2] for x in rr),
            "mean_exit_retention": statistics.fmean(x[3] for x in rr),
            "mean_competitive_loss": statistics.fmean(x[4] for x in rr),
            "severe_harm_events": sum(by_family[policy].values()),
            "severe_harm_by_family": dict(sorted(by_family[policy].items())),
            "actions": dict(actions[policy]),
        }
    return result



# Post-hoc F-R020: a profile is not an independent decision, nor is a
# researcher-constructed family an IID draw from real-world cases.
# Keep the frozen E009 benchmark, canonical result, and prior auditor intact.
def _family_rows(common_noise=False):
    families = sorted(b.FAMILIES)
    policies = list(b.POLICIES)
    expected = {(sigma, seed) for sigma in (0.08, 0.15)
                for seed in b.NOISY_SEEDS}
    rows = {family: {policy: {} for policy in policies} for family in families}
    for case in b.make_cases():
        if case["variant"] != "stress":
            continue
        family = case["family"]
        for sigma, seed in sorted(expected):
            common = (b.observed(case, sigma,
                      random.Random(f"{case['case_id']}|{sigma}|{seed}"))
                      if common_noise else None)
            for policy in policies:
                observation = (common if common_noise else
                    b.observed(case, sigma,
                      random.Random(f"{case['case_id']}|{sigma}|{seed}|{policy}")))
                action = b.choose(policy, observation)
                outcome = b.consequence(case, action)
                # Three prespecified weight profiles evaluate the SAME action.
                # Average first to retain 1 independent decision unit per key.
                regret = statistics.fmean(
                    max(0.0, b.scalar_loss(outcome, profile, policy) -
                             b.oracle_loss(case, profile))
                    for profile in b.WEIGHT_PROFILES)
                key = (sigma, seed)
                if key in rows[family][policy]:
                    raise ValueError("DUPLICATE_DECISION_KEY")
                rows[family][policy][key] = (
                    regret, int(outcome["harm"] >= b.SEVERE_HARM_THRESHOLD))
    _verify_family_population(rows, expected)
    return rows


def _verify_family_population(rows, expected):
    if set(rows) != set(b.FAMILIES):
        raise ValueError("MISSING_OR_UNDECLARED_FAMILY")
    for family in b.FAMILIES:
        if set(rows[family]) != set(b.POLICIES):
            raise ValueError("MISSING_OR_UNDECLARED_POLICY")
        for policy in b.POLICIES:
            if set(rows[family][policy]) != expected:
                raise ValueError("INCOMPLETE_OR_UNDECLARED_DECISION_ROSTER")


def _group_summary(rows, excluded=None):
    included = [family for family in sorted(b.FAMILIES)
                if family != excluded]
    summary = {}
    for policy in b.POLICIES:
        values = [value for family in included
                  for value in rows[family][policy].values()]
        summary[policy] = {
            "decisions": len(values),
            "mean_regret": statistics.fmean(value[0] for value in values),
            "severe_events": sum(value[1] for value in values),
            "severe_rate": statistics.fmean(value[1] for value in values)}
    return summary


def _contrast(s):
    simpler = ("TWO_RULE_SIMPLE", "SECURITY_BOUNDED", "MINIMAL_4VAR")
    best_name = min(simpler, key=lambda p: (s[p]["mean_regret"], p))
    v3 = s["PROJECT_V3"]
    m4 = s["MINIMAL_4VAR"]
    return {
        "best_simple_policy": best_name,
        "project_minus_best_simple_mean_regret":
            v3["mean_regret"] - s[best_name]["mean_regret"],
        "project_minus_minimal4_mean_regret":
            v3["mean_regret"] - m4["mean_regret"],
        "project_minus_minimal4_severe_events":
            v3["severe_events"] - m4["severe_events"]}


def family_unit_audit(canonical):
    assert canonical["survival_criteria"]["project_v3_residual_survives"] is False
    expected = {(sigma, seed) for sigma in (0.08, 0.15)
                for seed in b.NOISY_SEEDS}
    independent = _family_rows(common_noise=False)
    paired = _family_rows(common_noise=True)
    orig = _group_summary(independent)
    pair = _group_summary(paired)
    # Check exact canonical per-policy rates, not merely chosen headline values.
    for policy in b.POLICIES:
        reference = canonical["stress_primary"][policy]
        if orig[policy]["decisions"] != 3200 or reference["n"] != 9600:
            raise AssertionError("PSEUDOREPLICATED_DENOMINATOR")
        if abs(orig[policy]["mean_regret"] - reference["mean_regret"]) > 1e-12:
            raise AssertionError("CANONICAL_REGRET_MISMATCH")
        if abs(orig[policy]["severe_rate"] - reference["severe_harm_rate"]) > 1e-12:
            raise AssertionError("CANONICAL_SEVERE_RATE_MISMATCH")

    # Positive and negative controls: an absent or unknown decision must not
    # silently count as a valid complete experiment population.
    test = {f: {p: dict(v) for p, v in grouped.items()}
            for f, grouped in independent.items()}
    family = sorted(test)[0]
    policy = "PROJECT_V3"
    key = sorted(expected)[0]
    removed = test[family][policy].pop(key)
    missing_blocked = False
    try:
        _verify_family_population(test, expected)
    except ValueError:
        missing_blocked = True
    test[family][policy][key] = removed
    test[family][policy][(99, 999)] = removed
    unknown_blocked = False
    try:
        _verify_family_population(test, expected)
    except ValueError:
        unknown_blocked = True
    if not (missing_blocked and unknown_blocked):
        raise AssertionError("FAMILY_ROSTER_MUTATION_NOT_DETECTED")

    leave_one_out = []
    for family in sorted(b.FAMILIES):
        leave_one_out.append({
            "excluded_family": family,
            "original": _contrast(_group_summary(independent, family)),
            "common_noise": _contrast(_group_summary(paired, family))})
    safety_min = min(canonical["stress_primary"][p]["severe_harm_rate"]
                     for p in ("SECURITY_BOUNDED", "MINIMAL_4VAR"))
    safety_cap = safety_min + 0.02  # frozen criterion: absolute 2 percentage points
    v3_count = orig["PROJECT_V3"]["severe_events"]
    m4_count = orig["MINIMAL_4VAR"]["severe_events"]
    return {
        "status": "E009_POSTHOC_DESCRIPTIVE_FAMILY_UNIT_AUDIT_ONLY",
        "original_frozen_benchmark_changed": False,
        "independent_validation": False,
        "family_count": len(b.FAMILIES),
        "per_policy_unique_decisions": 3200,
        "per_policy_metric_rows": 9600,
        "weight_profiles_per_decision": len(b.WEIGHT_PROFILES),
        "mutation_controls": {
            "wholly_missing_decision_blocked": missing_blocked,
            "undeclared_decision_blocked": unknown_blocked},
        "original": {"by_policy": orig, "contrast": _contrast(orig)},
        "common_noise": {"by_policy": pair, "contrast": _contrast(pair)},
        "severe_harm_gate_interpretation": {
            "preregistered_criterion_passed":
                canonical["survival_criteria"][
                    "criterion_severe_harm_no_more_than_2pp_worse_than_best_C_or_M4"],
            "allowed_absolute_excess_rate": 0.02,
            "allowed_excess_per_3200_decisions": 0.02 * 3200,
            "original_project_severe_events": v3_count,
            "original_minimal4_severe_events": m4_count,
            "observed_excess_events": v3_count - m4_count,
            "criterion_limit_rate": safety_cap,
            "warning": "A passing +2pp safety tolerance is not zero excess harm, individual survival protection, or empirical safety."},
        "leave_one_family_out": leave_one_out,
        "original_loo_project_worse_than_minimal4": sum(
            row["original"]["project_minus_minimal4_mean_regret"] > 0
            for row in leave_one_out),
        "common_noise_loo_project_worse_than_minimal4": sum(
            row["common_noise"]["project_minus_minimal4_mean_regret"] > 0
            for row in leave_one_out),
        "limitations": (
            "Sixteen hand-constructed stress families are not an IID sampling frame; "
            "leaving one out is a deterministic influence diagnostic, not a confidence "
            "interval or p-value. The same case outcomes are reweighted for three "
            "profiles; no party-specific loss distribution or real-world harm measured. "
            "Common random numbers can raise rather than lower variance in some designs. "
            "Do not revise the pre-registered E009 verdict or tune frozen thresholds.")}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="")
    parser.add_argument("--family-audit", action="store_true",
                        help="post-hoc complete family-unit, paired-noise, and LOFO audit")
    args = parser.parse_args()
    canonical = json.loads((HERE / "RESULT.json").read_text(encoding="utf-8"))
    assert canonical["survival_criteria"]["project_v3_residual_survives"] is False
    if args.family_audit:
        output = family_unit_audit(canonical)
        rendered = json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        if args.out:
            Path(args.out).write_text(rendered, encoding="utf-8")
        else:
            print(rendered)
        return
    original_recomputed = b.execute()["stress_primary"]
    for policy in b.POLICIES:
        a, expected = original_recomputed[policy], canonical["stress_primary"][policy]
        assert a["actions"] == expected["actions"], (policy, "action mismatch")
        for key in METRICS:
            assert abs(a[key] - expected[key]) < 1e-12, (policy, key)
    paired = paired_stress()
    delta = {
        p: {k: paired[p][k] - canonical["stress_primary"][p][k]
            for k in METRICS} for p in b.POLICIES
    }
    output = {
        "status": "EXPLORATORY_PROJECT_LINEAGE_PAIRED_OBSERVATION_SENSITIVITY",
        "independent_validation": False,
        "original_commit_result_reproduced": True,
        "only_changed_factor": "policy excluded from observation RNG key",
        "original": canonical["stress_primary"],
        "paired_observations": paired,
        "paired_minus_original": delta,
        "claim_boundary": (
            "Synthetic posthoc sensitivity, NOT a preregistered replacement, "
            "NOT an independent implementation, NOT empirical causal validation. "
            "Profile rows reuse the same policy action and outcome."
        )
    }
    rendered = json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.out:
        Path(args.out).write_text(rendered, encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()

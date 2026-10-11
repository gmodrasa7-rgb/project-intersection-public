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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="")
    args = parser.parse_args()
    canonical = json.loads((HERE / "RESULT.json").read_text(encoding="utf-8"))
    assert canonical["survival_criteria"]["project_v3_residual_survives"] is False
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

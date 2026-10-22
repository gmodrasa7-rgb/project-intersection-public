#!/usr/bin/env python3
"""E009 post-hoc policy non-nestedness and feature-toggle audit.

This imports the FROZEN original decision rules rather than editing them.
It is an internal project-lineage logic audit, not independent replication,
field evidence, causal feature attribution, or a new E009 outcome.
"""
import argparse
import json
import random

import benchmark as b

EXTRA = ("RF", "SEL", "INT", "VOI")
SHARED = ("ENF", "ID", "OV", "CUM", "harm_action", "harm_inaction", "reversibility")


def controlled_witness():
    """Identical observable vector, extra V3 features exactly zero."""
    x = {k: 0.0 for k in b.FEATURES}
    x.update(ENF=.2, ID=.2, OV=.2, CUM=.2,
             harm_action=.89, harm_inaction=.30, reversibility=.30,
             RF=0.0, SEL=0.0, INT=0.0, VOI=0.0)
    assert all(x[k] == 0.0 for k in EXTRA)
    return x


def verify_non_nested(choose_fn):
    """Return a falsifying witness for *feature-only* attribution.

    If the two policy branches were the same rule plus extra input features,
    zeroing those extras would not, by itself, entail different actions.
    A contrary witness proves the published comparison cannot isolate the
    value of four additional features from simultaneous rule changes.
    """
    x = controlled_witness()
    a = choose_fn("MINIMAL_4VAR", x)
    c = choose_fn("PROJECT_V3", x)
    if (a, c) != ("BLOCK", "EXPERIMENT"):
        raise AssertionError("NON_NESTED_WITNESS_CHANGED: audit needs review")
    return {"shared_input": {k: x[k] for k in SHARED},
            "extra_inputs": {k: x[k] for k in EXTRA},
            "minimal4_action": a, "project_v3_action": c}


def stress_toggle_diagnostic():
    """Describe chosen actions, NOT effects on real agents or model quality.

    Toggle each extra V3 feature to both domain endpoints while fixing all
    other observed inputs; record the number of changed actions. Endpoints
    may be off-distribution. Do not interpret counts as feature importance
    across real environments or the value of added information.
    """
    switches = {k: {"to_zero": 0, "to_one": 0} for k in EXTRA}
    observed_comparator_disagreements = 0
    all_extra_zero_switches = 0
    n = 0
    for case in b.make_cases():
        if case["variant"] != "stress":
            continue
        for sigma in (0.08, 0.15):
            for seed in b.NOISY_SEEDS:
                obs = b.observed(
                    case, sigma,
                    random.Random(f"{case['case_id']}|{sigma}|{seed}|PROJECT_V3"))
                original = b.choose("PROJECT_V3", obs)
                if original != b.choose("MINIMAL_4VAR", obs):
                    observed_comparator_disagreements += 1
                muted = dict(obs)
                for key in EXTRA:
                    muted[key] = 0.0
                if original != b.choose("PROJECT_V3", muted):
                    all_extra_zero_switches += 1
                for key in EXTRA:
                    for target, label in ((0.0, "to_zero"), (1.0, "to_one")):
                        toggled = dict(obs)
                        toggled[key] = target
                        if b.choose("PROJECT_V3", toggled) != original:
                            switches[key][label] += 1
                n += 1
    if n != 16 * 2 * 100:
        raise AssertionError(f"UNEXPECTED_DECISION_COUNT:{n}")
    if any(not (0 <= v <= n) for row in switches.values() for v in row.values()):
        raise AssertionError("BAD_SWITCH_COUNT")
    return {"unique_stress_decisions_per_policy": n,
            "original_V3_vs_M4_action_disagreements_on_V3_noise": observed_comparator_disagreements,
            "V3_action_switches_if_all_four_extra_features_zeroed": all_extra_zero_switches,
            "one_feature_endpoint_action_switch_counts": switches}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    witness = verify_non_nested(b.choose)
    if args.self_test:
        # Negative control: a falsely identical policy pair MUST be rejected.
        try:
            verify_non_nested(lambda policy, obs: "ALLOW")
        except AssertionError:
            rejected = True
        else:
            rejected = False
        if not rejected:
            raise AssertionError("MUTATION_CONTROL_ACCEPTED")
    else:
        rejected = None
    result = {
        "status": "PROJECT_LINEAGE_POSTHOC_LOGIC_DIAGNOSTIC_NOT_INDEPENDENT_VALIDATION",
        "original_E009_benchmark_modified": False,
        "claims_incremental_feature_value": False,
        "non_nestedness_witness": witness,
        "stress_observation_endpoint_sensitivity": stress_toggle_diagnostic(),
        "negative_control_rejected": rejected,
        "conclusion": "Policy comparisons mix decision-rule differences with added variables; "
                      "incremental feature value requires matched-rule ablations "
                      "under separately specified holdouts, outcomes and costs.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""E009 VOI identifiability diagnostic: same project lineage, post-hoc only.

This checks a frozen synthetic engine, not empirical or independent causal proof.
No preregistered E009 file or result is modified.
"""
import ast
import hashlib
import json
import math
from pathlib import Path

import benchmark as b

ROOT = Path(__file__).resolve().parent
EXPECTED_SHA256 = "86b50f9859858f16e57429fbda5bca3306e1680a2be081d16690c6e7776f188a"
LOSS_KEYS = ("harm", "capture", "resource", "competitive", "deadlock", "recovery", "option")


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def equal_number(x, y, message):
    require(math.isclose(x, y, rel_tol=0.0, abs_tol=1e-12), message)


def invariant(engine, cases):
    """Test action-conditional VOI invariance at paired extreme settings."""
    return all(
        engine({**case, "VOI": 0.0}, action)
        == engine({**case, "VOI": 1.0}, action)
        for case in cases for action in b.ACTIONS
    )


def unpenalized_loss(case, action, profile):
    out = b.consequence(case, action)
    return sum(b.WEIGHT_PROFILES[profile][key] * out[key] for key in LOSS_KEYS)


def audit():
    source = (ROOT / "benchmark.py").read_bytes()
    frozen_hash = hashlib.sha256(source).hexdigest()
    require(frozen_hash == EXPECTED_SHA256, "Frozen benchmark byte hash changed")
    parsed = ast.parse(source, filename="benchmark.py")
    fns = [n for n in parsed.body
           if isinstance(n, ast.FunctionDef) and n.name == "consequence"]
    require(len(fns) == 1, "Outcome function not uniquely found")
    # Frozen consequence() unpacks voi but does not use it. The hash fixes
    # the precise audited source; this lexical test aids defect localization.
    require(not any(isinstance(n, ast.Name) and n.id == "voi"
                    and isinstance(n.ctx, ast.Load) for n in ast.walk(fns[0])),
            "VOI is read in outcome function: investigate changed causal pathway")

    cases = b.make_cases()
    require(len(cases) == 32 and len({c["family"] for c in cases}) == 16,
            "Unexpected frozen case population")
    zero = {key: 0.0 for key in b.FEATURES}
    zero["case_id"] = "CONSTRUCTED_NOT_PREREGISTERED"
    require(invariant(b.consequence, [*cases, zero]),
            "Changing only VOI changed at least one action-conditional outcome")

    # An injected causal path MUST be caught: a non-vacuity negative control.
    def injected_path(case, action):
        out = b.consequence(case, action).copy()
        out["option"] = min(1.0, out["option"] + 0.01 * case["VOI"])
        return out

    require(not invariant(injected_path, [*cases, zero]),
            "Injected VOI effect was not detected")

    lo, hi = ({**zero, "VOI": 0.0}, {**zero, "VOI": 1.0})
    require(b.choose("PROJECT_V3", lo) == "ALLOW", "Low VOI action drift")
    require(b.choose("PROJECT_V3", hi) == "MONITOR", "High VOI action drift")
    for field, expected in {"deadlock": 0.0, "option": 0.0,
                            "exit_retention": 1.0}.items():
        equal_number(b.consequence(lo, "ALLOW")[field], expected, "ALLOW outcome mismatch")
    for field, expected in {"deadlock": 0.1152, "option": 0.03456,
                            "exit_retention": 0.97696}.items():
        equal_number(b.consequence(hi, "MONITOR")[field], expected,
                     "MONITOR outcome mismatch")

    extra_losses = {}
    for profile, expected in {"safety_heavy": 0.009792,
                              "balanced": 0.014976,
                              "adaptability_heavy": 0.0179712}.items():
        delta = unpenalized_loss(hi, "MONITOR", profile) - unpenalized_loss(lo, "ALLOW", profile)
        equal_number(delta, expected, "Profile conditional loss mismatch")
        equal_number(b.oracle_loss(lo, profile), b.oracle_loss(hi, profile),
                     "Oracle unexpectedly depends on VOI")
        low_regret = b.scalar_loss(b.consequence(lo, "ALLOW"), profile, "PROJECT_V3") - b.oracle_loss(lo, profile)
        high_regret = b.scalar_loss(b.consequence(hi, "MONITOR"), profile, "PROJECT_V3") - b.oracle_loss(hi, profile)
        equal_number(low_regret, 0.0385, "Unexpected low-VOI regret")
        equal_number(high_regret, 0.0385 + expected, "Unexpected high-VOI regret")
        extra_losses[profile] = delta

    # Paired deterministic diagnostic on the 32 project-authored cases.
    # No claim of 32 independent samples or new preregistered evidence.
    flips = dict(action_flips=0, higher_loss=0, lower_loss=0, same_loss=0)
    changed_case_details = []
    for case in cases:
        a = {**case, "VOI": 0.0}
        z = {**case, "VOI": 1.0}
        action_a = b.choose("PROJECT_V3", a)
        action_z = b.choose("PROJECT_V3", z)
        if action_a == action_z:
            continue
        flips["action_flips"] += 1
        difference = (unpenalized_loss(z, action_z, "balanced")
                      - unpenalized_loss(a, action_a, "balanced"))
        changed_case_details.append({"case_id": case["case_id"], "low_voi_action": action_a,
                                     "high_voi_action": action_z,
                                     "balanced_unpenalized_loss_change": round(difference, 12)})
        if difference > 1e-12:
            flips["higher_loss"] += 1
        elif difference < -1e-12:
            flips["lower_loss"] += 1
        else:
            flips["same_loss"] += 1
    require(sum(flips[k] for k in ("higher_loss", "lower_loss", "same_loss"))
            == flips["action_flips"], "Unaccounted action flip")

    return {
        "status": "PASS_PROJECT_LINEAGE_POSTHOC_SYNTHETIC_DIAGNOSTIC",
        "benchmark_sha256": frozen_hash,
        "case_families": 16,
        "registered_cases_examined": 32,
        "action_conditional_voi_invariant": True,
        "injected_voi_path_detected": True,
        "constructed_actions": {"voi_0": "ALLOW", "voi_1": "MONITOR"},
        "constructed_incremental_loss": extra_losses,
        "registered_case_voi_extremes_diagnostic": flips,
        "registered_case_action_flip_details": changed_case_details,
        "independent_replication": False,
        "empirical_validation": False,
        "frozen_verdict_changed": False,
    }


if __name__ == "__main__":
    print(json.dumps(audit(), indent=2, sort_keys=True))

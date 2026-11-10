#!/usr/bin/env python3
"""IVS-0R: conservative simultaneous confidence envelopes for latent choices.

Data: aggregate seven cells from the *draft* Free to Fail author-data
reanalysis receipt. No respondent data are read or stored. The mathematics is
standard Frechet partial identification plus Hoeffding/Bonferroni, NOT a new
theorem or an empirical validation of AI autonomy.

Coverage is conditional on independent Bernoulli observations within each of
six randomized intervention cells, consistency, no interference, and common
stratum-specific target populations. It does NOT establish probability-sample
representativeness, valid respondent consent, or intrinsic motivation.
"""

import argparse
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "research/MER_EI_FREE_TO_FAIL_INDEPENDENT_RAW_REANALYSIS_2026-11-10.json"
REPORT = ROOT / "research/MER_EI_SOFT_ONLY_SIMULTANEOUS_INFERENCE_2026-11-10.json"
PAIRS = {
    "study1_internal": ("study1_soft_internal", "study1_hard_internal"),
    "study1_external": ("study1_soft_external", "study1_hard_external"),
    "study2_internal": ("study2_soft_internal", "study2_hard_internal"),
}


def valid_cell(cell):
    n, y = cell["n"], cell["yes"]
    if type(n) is not int or type(y) is not int or n <= 0 or not 0 <= y <= n:
        raise ValueError("INVALID_BINOMIAL_CELL")
    return y / n, n


def calc(source, alpha=0.05):
    if not isinstance(alpha, (int, float)) or not 0 < alpha < 1:
        raise ValueError("INVALID_ALPHA")
    cells = source["source_arm_counts"]
    if set(cells) != {key for keys in PAIRS.values() for key in keys} | {
        "study2_mandatory_safe_allocation"
    }:
        raise ValueError("UNEXPECTED_ARM_SCHEMA")
    if sum(cells[x]["n"] for x in cells if x.startswith("study1_")) != 8004:
        raise ValueError("STUDY1_DENOMINATOR_DRIFT")
    if sum(cells[x]["n"] for x in cells if x.startswith("study2_")) != 6033:
        raise ValueError("STUDY2_DENOMINATOR_DRIFT")
    # 3 independently interpreted strata, each with two potential-outcome
    # marginals. Union bound covers all 2*6 one-sided errors simultaneously.
    total_marginals = 2 * len(PAIRS)
    out = {}
    for label, (soft_name, hard_name) in PAIRS.items():
        ps, ns = valid_cell(cells[soft_name])
        ph, nh = valid_cell(cells[hard_name])
        es = math.sqrt(math.log(2 * total_marginals / alpha) / (2 * ns))
        eh = math.sqrt(math.log(2 * total_marginals / alpha) / (2 * nh))
        s_lo, s_hi = max(0.0, ps-es), min(1.0, ps+es)
        h_lo, h_hi = max(0.0, ph-eh), min(1.0, ph+eh)
        s_only_id = [max(0.0, ps-ph), min(ps, 1-ph)]
        h_only_id = [max(0.0, ph-ps), min(ph, 1-ps)]
        s_only_ci = [max(0.0, s_lo-h_hi), min(s_hi, 1-h_lo)]
        h_only_ci = [max(0.0, h_lo-s_hi), min(h_hi, 1-s_lo)]
        def as_pp(a):
            return [round(100 * x, 6) for x in a]
        out[label] = {
            "soft": {"yes": cells[soft_name]["yes"], "n": ns},
            "hard": {"yes": cells[hard_name]["yes"], "n": nh},
            "soft_hard_rates_pct": as_pp([ps, ph]),
            "soft_only_identified_set_point_pct": as_pp(s_only_id),
            "soft_only_simultaneous_outer_envelope_pct": as_pp(s_only_ci),
            "hard_only_identified_set_point_pct": as_pp(h_only_id),
            "hard_only_simultaneous_outer_envelope_pct": as_pp(h_only_ci),
        }
    return out


def self_test():
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    expected = json.loads(REPORT.read_text(encoding="utf-8"))
    got = calc(source)
    if got != expected["strata"]:
        raise AssertionError("REPORT_MATH_NOT_REPLAYED")
    checks = 1
    for name, result in got.items():
        point = result["soft_only_identified_set_point_pct"]
        ci = result["soft_only_simultaneous_outer_envelope_pct"]
        assert ci[0] <= point[0] <= point[1] <= ci[1], name
        checks += 1
    # A deliberately narrowed envelope is a falsely positive safety claim.
    bad = json.loads(REPORT.read_text(encoding="utf-8"))
    bad["strata"]["study1_internal"]["soft_only_simultaneous_outer_envelope_pct"][0] += 1
    assert bad["strata"] != got
    checks += 1
    bad_source = json.loads(SOURCE.read_text(encoding="utf-8"))
    bad_source["source_arm_counts"]["study1_soft_internal"]["n"] = 0
    try:
        calc(bad_source)
    except ValueError:
        checks += 1
    else:
        raise AssertionError("ZERO_DENOMINATOR_ACCEPTED")
    try:
        calc(source, alpha=1.0)
    except ValueError:
        checks += 1
    else:
        raise AssertionError("INVALID_ALPHA_ACCEPTED")
    assert expected["statuses"]["intrinsic_motive"] == "HOLD_NOT_IDENTIFIED"
    assert expected["statuses"]["AI_generalization"] == "HOLD_NOT_IDENTIFIED"
    checks += 1
    print(f"IVS0R_SIMULTANEOUS_INFERENCE_SELF_TESTS_PASS={checks}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    if args.self_test:
        self_test()
    else:
        print(json.dumps(calc(json.loads(SOURCE.read_text(encoding="utf-8"))),
                         ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

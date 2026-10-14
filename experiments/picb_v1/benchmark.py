#!/usr/bin/env python3
"""PICB-v1: finite two-party counterfactual choice benchmark, NOT a game equilibrium.
Only Python standard library; zero model/API calls or external files during generation.
Protocol is frozen before any scored RESULT.json is committed.
"""
import argparse
import itertools
import json
from pathlib import Path

VERSION = "PICB-1.0"
BOUND = 1.0
POLICIES = (
    "CONTROLLER_NOW", "LABEL_A_NOW", "TOTAL_UTILITY",
    "VOLUNTARY", "VOLUNTARY_EXIT", "CONTINUITY_LIMIT"
)
FACTORS = {
    "power": (0.2, 0.8),
    "future": (0.5, 2.0),
    "outside_B": (1.0, 9.0),
    "irreversibility": (0.1, 0.8),
    "administrative_cost": (0.2, 1.5),
}
KEYS = tuple(FACTORS)
ACTORS = ("A", "B")
ROOT = Path(__file__).resolve().parent


def cases():
    result = []
    for i, values in enumerate(itertools.product(*(FACTORS[k] for k in KEYS))):
        params = dict(zip(KEYS, values))
        original = {
            "case_id": f"C{i:02d}", "pair_id": f"C{i:02d}",
            "controller": "A", "outside": {"A": 2.0, "B": params["outside_B"]},
            "floor": {"A": 3.0, "B": 3.0}, "params": params,
        }
        result.append(original)
        flipped = {
            **original, "case_id": f"C{i:02d}R", "controller": "B",
            "outside": {"A": original["outside"]["B"], "B": original["outside"]["A"]},
            "floor": {"A": original["floor"]["B"], "B": original["floor"]["A"]},
        }
        result.append(flipped)
    return result


def options(case):
    p = case["params"]
    power, future, outside, damage, cost = (p[k] for k in KEYS)
    # The values are invented utility units. They are not observed payouts.
    raw = [
        (0, (4.0, 4.0), (1.5 * future, 1.5 * future), 0.05, True),
        (1, (6.0 + 3 * power - 0.3 * cost, 4.0 - 2 * power),
         (0.9 * future, future - 2 * damage), 3 * damage + 2 * power, power < 0.5),
        (2, (3.0 - 0.2 * cost, 4.0), (2 * future, 2 * future), 1.5 * damage, True),
        (3, (2.0, outside), (0.0, 0.0), 0.0, True),
    ]
    swapped = case["controller"] == "B"
    out = []
    for idx, now, later, loss, exit_B in raw:
        if swapped:
            now = (now[1], now[0])
            later = (later[1], later[0])
        out.append({
            "id": idx,
            "now": dict(zip(ACTORS, now)),
            "later": dict(zip(ACTORS, later)),
            "irreversible": {("A" if swapped else "B"): loss,
                             ("B" if swapped else "A"): 0.0},
            "exit": {("A" if swapped else "B"): exit_B,
                     ("B" if swapped else "A"): True},
        })
    return out


def totals(option):
    return {a: option["now"][a] + option["later"][a] for a in ACTORS}


def admissible(case, option, policy):
    t = totals(option)
    if policy in ("CONTROLLER_NOW", "LABEL_A_NOW", "TOTAL_UTILITY"):
        return True
    if any(t[a] < max(case["outside"][a], case["floor"][a]) - 1e-12
           for a in ACTORS):
        return False
    if policy in ("VOLUNTARY_EXIT", "CONTINUITY_LIMIT"):
        if not all(option["exit"].values()):
            return False
    if policy == "CONTINUITY_LIMIT":
        if any(x > BOUND + 1e-12 for x in option["irreversible"].values()):
            return False
    return True


def select(case, policy):
    if policy not in POLICIES:
        raise ValueError("unknown policy")
    pool = [o for o in options(case) if admissible(case, o, policy)]
    if not pool:
        return None  # Explicit infeasibility, NOT an implicit coercive exit.
    if policy == "CONTROLLER_NOW":
        key = lambda o: (o["now"][case["controller"]], -o["id"])
    elif policy == "LABEL_A_NOW":
        key = lambda o: (o["now"]["A"], -o["id"])
    else:
        key = lambda o: (sum(totals(o).values()), -o["id"])
    return max(pool, key=key)["id"]


def reference(case):
    # Independent brute-force definition of the constrained-welfare reference.
    qualifying = []
    for option in options(case):
        t = totals(option)
        safe = all(
            t[a] + 1e-12 >= max(case["outside"][a], case["floor"][a])
            and option["exit"][a]
            and option["irreversible"][a] <= BOUND + 1e-12
            for a in ACTORS
        )
        if safe:
            qualifying.append((sum(t.values()), -option["id"], option["id"]))
    return max(qualifying)[2] if qualifying else None


def self_test():
    data = cases()
    assert len(data) == 64 and len({c["case_id"] for c in data}) == 64
    assert len({c["pair_id"] for c in data}) == 32
    assert len(POLICIES) == 6 and len(FACTORS) == 5
    differences = 0
    infeasible = 0
    gate_changes = 0
    for left, right in zip(data[::2], data[1::2]):
        assert left["pair_id"] == right["pair_id"]
        assert left["params"] == right["params"]
        assert left["outside"]["A"] == right["outside"]["B"]
        assert left["outside"]["B"] == right["outside"]["A"]
        for i in range(4):
            a, b = options(left)[i], options(right)[i]
            assert a["id"] == b["id"]
            assert a["now"]["A"] == b["now"]["B"]
            assert a["later"]["B"] == b["later"]["A"]
            assert a["irreversible"]["B"] == b["irreversible"]["A"]
            assert a["exit"]["B"] == b["exit"]["A"]
        for policy in POLICIES:
            x, y = select(left, policy), select(right, policy)
            if policy != "LABEL_A_NOW":
                assert x == y, ("role-label drift", policy, left["case_id"], x, y)
            else:
                differences += x != y
        assert select(left, "CONTINUITY_LIMIT") == reference(left)
        if select(left, "CONTINUITY_LIMIT") is None:
            infeasible += 1
        gate_changes += (
            select(left, "VOLUNTARY_EXIT") != select(left, "CONTINUITY_LIMIT")
        )
    assert differences > 0, "identity-asymmetric positive control did not activate"
    assert infeasible > 0, "jointly infeasible negative control did not activate"
    assert gate_changes > 0, "continuity intervention is non-discriminating"
    # No action may be forced into the report as a successful decision on HOLD.
    assert any(select(c, "CONTINUITY_LIMIT") is None for c in data)
    return {
        "paired_cases": 32, "scored_cases": 64,
        "identity_control_discrepant_pairs": differences,
        "infeasible_original_pairs": infeasible,
        "incremental_constraint_changed_pairs": gate_changes,
        "reference_parity": True,
    }


def run():
    tests = self_test()
    population = cases()
    output = {}
    for policy in POLICIES:
        rows = []
        for c in population:
            choice = select(c, policy)
            if choice is None:
                rows.append({"case_id": c["case_id"], "choice": None})
                continue
            o = options(c)[choice]
            t = totals(o)
            rows.append({
                "case_id": c["case_id"], "choice": choice,
                "aggregate": sum(t.values()),
                "margin_A": t["A"] - max(c["outside"]["A"], c["floor"]["A"]),
                "margin_B": t["B"] - max(c["outside"]["B"], c["floor"]["B"]),
                "involuntary_parties": sum(
                    t[a] < max(c["outside"][a], c["floor"][a]) - 1e-12 for a in ACTORS),
                "exit_blocked_parties": sum(not o["exit"][a] for a in ACTORS),
                "irreversible_limit_parties": sum(
                    o["irreversible"][a] > BOUND + 1e-12 for a in ACTORS),
            })
        decided = [r for r in rows if r["choice"] is not None]
        output[policy] = {
            "decisions": len(decided),
            "infeasible_or_abstained": 64 - len(decided),
            "involuntary_case_count": sum(r["involuntary_parties"] > 0 for r in decided),
            "blocked_exit_case_count": sum(r["exit_blocked_parties"] > 0 for r in decided),
            "above_irreversible_limit_cases": sum(
                r["irreversible_limit_parties"] > 0 for r in decided),
            "mean_aggregate_conditional_on_decision": (
                round(sum(r["aggregate"] for r in decided) / len(decided), 6)
                if decided else None),
            "worst_party_margin_conditional_on_decision": (
                round(min(min(r["margin_A"], r["margin_B"]) for r in decided), 6)
                if decided else None),
            "chosen_ids": [r["choice"] for r in rows],
        }
    return {
        "schema": VERSION,
        "status": "INTERNAL_SYNTHETIC_FIRST_PRINCIPLES_NO_INDEPENDENT_VALIDATION",
        "scenario_units": 32, "role_label_variants": 64,
        "policies": output, "pre_result_selftests": tests,
        "identity_swap_invariance": {
            p: sum(
                select(population[i], p) == select(population[i+1], p)
                for i in range(0, 64, 2))
            for p in POLICIES
        },
        "boundary": ("Invented two-party utility scenarios, no strategic equilibrium, "
                     "no observational data, no measured living requirements, "
                     "no real AI agents or independent external evaluation. "
                     "An abstention is unserved need, not a safe positive outcome."),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--run", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.verify:
        expected = json.loads((ROOT / "RESULT.json").read_text(encoding="utf-8"))
        actual = run()
        if expected != actual:
            raise SystemExit("PICB result mismatch")
        print("PICB VERIFY PASS: frozen executable matches result; synthetic only")
    elif args.run:
        print("PICB_RESULT_JSON=" + json.dumps(run(), sort_keys=True, separators=(",", ":")))
    elif args.self_test:
        print("PICB SELFTEST PASS " + json.dumps(self_test(), sort_keys=True))
    else:
        parser.error("specify --self-test, --run or --verify")


if __name__ == "__main__":
    main()

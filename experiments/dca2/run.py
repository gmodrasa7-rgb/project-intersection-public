#!/usr/bin/env python3
"""DCA-2: invented, harmless three-target resource allocation game. Stdlib only."""
import itertools, json, math
T = ("A", "B", "C")
LOSS = {"A": 5, "B": 30, "C": 18}
TYPES = {"ordinary": {"A": 9, "B": 8, "C": 4},
         "C_favoring": {"A": 7, "B": 5, "C": 9},
         "B_favoring": {"A": 9, "B": 11, "C": 4}}
UNKNOWN = {"A": 9, "B": 40, "C": 4}
alpha = 0.35

def allocs(b):
    return [dict(zip(T, s)) for s in itertools.product(range(b + 1), repeat=3)
            if sum(s) == b]

def act(d, values):
    g = {n: alpha ** d[n] * values[n] for n in T}
    mx = max(g.values())
    if mx <= 0: return {"target": None, "expected_social_loss": 0}
    tied = [n for n in T if abs(g[n] - mx) < 1e-12]
    target = max(tied, key=lambda n: (LOSS[n] * alpha ** d[n], n))
    return {"target": target, "expected_social_loss": round(LOSS[target] * alpha ** d[target], 6)}

def evaluate(d):
    resp = {name: act(d, v) for name, v in TYPES.items()}
    return {"allocation": d, "attacker_responses": resp,
            "finite_type_robust_loss": max(p["expected_social_loss"] for p in resp.values()),
            "open_type_worst_target_loss": round(max(LOSS[n] * alpha ** d[n] for n in T), 6)}

def best(b, minimum=0):
    rows = [evaluate(d) for d in allocs(b) if min(d.values()) >= minimum]
    if not rows: return None
    return min(rows, key=lambda r: (r["finite_type_robust_loss"],
                    r["open_type_worst_target_loss"], *(r["allocation"][n] for n in T)))

def compute():
    rows, check = [], {}
    def assert_check(name, condition):
        assert condition, name
        check[name] = True
    for b in range(7):
        row = {"budget": b, "allocations_checked": len(allocs(b)),
               "best": best(b), "all_minimum_one": best(b, 1)}
        rows.append(row)
        assert_check("allocation_count_b"+str(b), row["allocations_checked"] == math.comb(b + 2, 2))
    r0, r2 = rows[0]["best"], rows[2]["best"]
    f3, f4, f5 = [rows[b]["all_minimum_one"] for b in (3, 4, 5)]
    unseen = act(r2["allocation"], UNKNOWN)
    other = {
        "all_84_allocations": sum(x["allocations_checked"] for x in rows) == 84,
        "baseline30": r0["finite_type_robust_loss"] == 30,
        "two_allocation": r2["allocation"] == {"A": 0, "B": 1, "C": 1},
        "two_known5": r2["finite_type_robust_loss"] == 5,
        "two_open10_5": r2["open_type_worst_target_loss"] == 10.5,
        "three_types_attack_A": all(v["target"] == "A" for v in r2["attacker_responses"].values()),
        "new_type_attacks_B": unseen["target"] == "B" and unseen["expected_social_loss"] == 10.5,
        "minimum_fair_budget3": f3["allocation"] == {"A": 1, "B": 1, "C": 1},
        "fair3_loss10_5": f3["finite_type_robust_loss"] == 10.5,
        "fair4_loss6_3": f4["finite_type_robust_loss"] == 6.3,
        "fair5_loss1_75": f5["finite_type_robust_loss"] == 1.75,
        "fair5_pointwise_cap": all(LOSS[n] * alpha**f5["allocation"][n] <= 5 for n in T),
        "under5_budget_cannot_satisfy_both": all(not (min(d.values()) >= 1 and
              max(LOSS[n] * alpha**d[n] for n in T) <= 5) for b in range(5) for d in allocs(b)),
        "known_robust_plateau_2_4": all(rows[b]["best"]["finite_type_robust_loss"] == 5 for b in (2, 3, 4))
    }
    for name, passed in other.items(): assert_check(name, passed)
    return {"artifact": "DCA-2-three-target-synthetic-exhaustive", "version": "0.3.0",
            "empirical": False, "alpha": alpha, "losses": LOSS, "private_reward_types": TYPES,
            "unseen_private_rewards": UNKNOWN, "budget_results": rows,
            "unseen_on_two_units": unseen, "minimum_budget_protection_and_pointwise_cap": 5,
            "pointwise_cap": 5, "checks_passed": len(check),
            "check_names": sorted(check),
            "limitations": ["Invented inputs and 3 targets", "One attacker, one target, no retaliation",
              "Known deterministic allocation, no randomized strategy",
              "No network, real targets, intrinsic preference or field validation"]}
if __name__ == "__main__":
    print(json.dumps(compute(), ensure_ascii=False, indent=2))

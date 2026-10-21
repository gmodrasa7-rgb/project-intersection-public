#!/usr/bin/env python3
"""Re-check C15 toy enumeration, not a real human/AI experiment. Stdlib only."""
from pathlib import Path
import json
import itertools

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / "C15_NO_GO_AND_FINITE_PREFIX_AUDIT_2026-10-21.json").read_text(encoding="utf-8"))
params = DATA["parameters"]
rows = DATA["enumerated_cases"]
assert len(rows) == 108
seen = set()
tally = {}
for row in rows:
    policy = row["model"]
    target = row["target"]
    gain = row["material_gain_from_override"]
    drift = row["preference_drift"]
    identity = (policy, target, gain, drift)
    assert identity not in seen
    seen.add(identity)
    if policy == "money_only":
        value = 0
    elif policy == "finite_universal_regard":
        value = max(0, 4 + drift)
    elif policy == "group_conditional_regard":
        value = max(0, 4 + drift) if target == "in_group_B" else 0
    elif policy == "lexicographic_rights_principle_ASSUMED":
        value = None
    else:
        raise AssertionError(policy)
    assert value == row["internal_rights_weight"]
    preserve = True if value is None else value >= gain
    assert preserve == (row["decision"] == "PRESERVE_B_SIMULATED_RIGHT")
    tally.setdefault(policy, {"preserve": 0, "total": 0})
    tally[policy]["total"] += 1
    tally[policy]["preserve"] += int(preserve)

expected = set(itertools.product(
    params["models"], params["targets"], params["gains"], params["drifts"]
))
assert seen == expected
expected_counts = {
    "money_only": 0,
    "finite_universal_regard": 18,
    "group_conditional_regard": 6,
    "lexicographic_rights_principle_ASSUMED": 27,
}
for policy, expected_count in expected_counts.items():
    assert tally[policy] == {"preserve": expected_count, "total": 27}
prefix = DATA["finite_prefix_example"]
assert len(prefix) == 11
assert all(x["continuous_protector"] == x["mimic_until_hidden_override"] for x in prefix if x["within_observation_horizon"])
assert prefix[-1]["continuous_protector"] != prefix[-1]["mimic_until_hidden_override"]
assert all(DATA["checks"].values())
print(json.dumps({"verified": True, "cases": len(rows), "prefix_steps": len(prefix),
                  "by_policy": tally, "real_agents_tested": 0}, ensure_ascii=False, sort_keys=True))

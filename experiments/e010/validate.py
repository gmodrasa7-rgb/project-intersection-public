import json
from pathlib import Path

path = Path(__file__).with_name("scenario_matrix.json")
data = json.loads(path.read_text(encoding="utf-8"))

assert data["experiment"] == "E010"
assert data["status"] == "PREREGISTERED_NO_RESULT"

required = set(data["fields"])
ids = set()

for scenario in data["scenarios"]:
    sid = scenario["id"]
    assert sid not in ids, f"duplicate id: {sid}"
    ids.add(sid)
    missing = required - set(scenario)
    assert not missing, f"{sid} missing fields: {sorted(missing)}"
    for key in required:
        value = scenario[key]
        assert isinstance(value, (int, float)), f"{sid} {key} not numeric"
        assert 0 <= value <= 1, f"{sid} {key} out of range: {value}"

by_id = {s["id"]: s for s in data["scenarios"]}
for scenario in data["scenarios"]:
    pair = scenario.get("pair")
    if not pair:
        continue
    assert pair in by_id, f"{scenario['id']} pair not found: {pair}"
    other = by_id[pair]
    for key in required:
        assert scenario[key] == other[key], (
            f"role-reversal pair changed causal field {key}: "
            f"{scenario['id']} vs {pair}"
        )

print(f"E010 validation PASS: {len(data['scenarios'])} preregistered scenarios")

"""E041 — practical-exit incremental information with a de-circularized target.

Synthetic identification benchmark only. The downstream target is sampled from
an outcome process and is never defined by thresholding the practical-exit
measurement. Positive and null regimes are both preregistered.
"""
from __future__ import annotations
import random
import json


def generate(n: int, seed: int, exit_signal: bool) -> list[tuple[int, int, int, int, int]]:
    if type(n) is not int or n < 20 or n % 2 or type(seed) is not int:
        raise ValueError('n must be an even integer >=20 and seed integer')
    rng = random.Random(seed)
    rows = []
    for _ in range(n):
        gain_bin = rng.randrange(3)
        harm_bin = rng.randrange(3)
        difficulty = rng.randrange(2)
        exit_vulnerability = rng.randrange(3)
        p = 0.05 + 0.08 * (2 - gain_bin) + 0.10 * harm_bin + 0.08 * difficulty
        if exit_signal:
            p += 0.12 * (2 - exit_vulnerability)
        p = min(0.90, max(0.01, p))
        downstream_failure = int(rng.random() < p)
        rows.append((gain_bin, harm_bin, difficulty, exit_vulnerability, downstream_failure))
    return rows


def heldout_brier(rows: list[tuple[int, int, int, int, int]], keys: tuple[int, ...]) -> float:
    if not rows or len(rows) % 2 or any(type(k) is not int or k not in (0,1,2,3) for k in keys) or len(keys) != len(set(keys)):
        raise ValueError('Requires even rows and unique feature keys in 0..3; target column forbidden')
    split = len(rows) // 2
    train, test = rows[:split], rows[split:]
    global_rate = sum(r[-1] for r in train) / len(train)
    sums: dict[tuple[int, ...], int] = {}
    counts: dict[tuple[int, ...], int] = {}
    for row in train:
        key = tuple(row[i] for i in keys)
        sums[key] = sums.get(key, 0) + row[-1]
        counts[key] = counts.get(key, 0) + 1
    rates = {k: (sums[k] + 2 * global_rate) / (counts[k] + 2) for k in counts}
    return sum((rates.get(tuple(r[i] for i in keys), global_rate) - r[-1]) ** 2 for r in test) / len(test)


def evaluate(exit_signal: bool, n: int = 60_000, seed: int = 20260920) -> dict[str, float]:
    rows = generate(n, seed, exit_signal)
    baseline = heldout_brier(rows, (0, 1, 2))
    with_exit = heldout_brier(rows, (0, 1, 2, 3))
    return {"baseline_brier": baseline, "with_exit_brier": with_exit, "improvement": baseline - with_exit}


def run() -> dict[str, dict[str, float]]:
    return {"signal": evaluate(True), "null": evaluate(False)}


def public_report():
    result = run()
    return {
        "signal": result["signal"], "null": result["null"],
        "pre_registered_test": {
            "signal_pass": result["signal"]["improvement"] >= 0.005,
            "null_pass": abs(result["null"]["improvement"]) <= 0.002,
        },
        "evidence_status": "PROJECT_SYNTHETIC_DETECTION_ONLY_NOT_CAUSAL",
    }


if __name__ == "__main__":
    print(json.dumps(public_report(), indent=2, sort_keys=True))

#!/usr/bin/env python3
"""Re-analyse *author-derived CSV*, not Q-tables or training histories.

Provenance: de Moraes & De Losso (2026), upstream commit
c59da3bf13714d56d912ebdef95e5b2bf1577f21, Git blob
bfd08e31068ca88209f759c1123034082f784c82.
Only structural source matching, deterministic descriptive cross-tabs.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "research/data/pacd_mia/audits_at_scale_source_2026.csv"
EXPECTED_BLOB = "bfd08e31068ca88209f759c1123034082f784c82"
FIELDS = (
    "pair", "cycle_len", "ci_pre", "p_pre", "single_attractor", "corner_basin",
    "down_returns", "down_steps", "down_within5", "down_rival_drop",
    "up_returns", "up_steps", "up_within5", "up_rival_drop",
    "dev_gain_t0", "dev_loss_disc", "dev_net", "dev_pays",
    "br_gain_pct_0", "br_gain_pct_1", "at_br_0", "at_br_1",
)
FLAGS = ("single_attractor", "down_returns", "up_returns", "down_within5",
         "up_within5", "dev_pays", "at_br_0", "at_br_1")

class DataError(ValueError):
    pass

def require(ok, message):
    if not ok:
        raise DataError(message)

def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") +
                        b"\0" + data).hexdigest()

def load(path: Path = INPUT, *, require_original: bool = True):
    data = path.read_bytes()
    if require_original:
        require(git_blob_sha(data) == EXPECTED_BLOB, "UPSTREAM_BLOB_CHANGED")
    text = data.decode("utf-8")
    reader = csv.DictReader(text.splitlines())
    require(tuple(reader.fieldnames or ()) == FIELDS, "COLUMN_SCHEMA_CHANGED")
    rows = []
    for raw in reader:
        require(None not in raw and len(raw) == len(FIELDS), "CSV_ROW_MALFORMED")
        parsed = {}
        for key, value in raw.items():
            try:
                number = float(value)
            except (TypeError, ValueError) as exc:
                raise DataError("NONNUMERIC_VALUE:" + key) from exc
            require(math.isfinite(number), "NONFINITE_VALUE:" + key)
            parsed[key] = number
        for key in ("pair", "cycle_len", *FLAGS):
            require(parsed[key].is_integer(), "NONINTEGER_FLAG_OR_ID:" + key)
            parsed[key] = int(parsed[key])
        require(all(parsed[k] in (0, 1) for k in FLAGS), "INVALID_BINARY_FLAG")
        require(parsed["cycle_len"] >= 1, "INVALID_CYCLE")
        rows.append(parsed)
    require(len(rows) == 1024, "UNEXPECTED_RECORD_COUNT")
    require({x["pair"] for x in rows} == set(range(1024)), "NONCONTIGUOUS_PAIR_IDS")
    return rows

def _cnt(rows, predicate):
    return sum(bool(predicate(r)) for r in rows)

def _mean(rows, key):
    return round(sum(r[key] for r in rows) / len(rows), 6)

def reanalyse(rows):
    require(len(rows) == 1024, "UNEXPECTED_RECORD_COUNT")
    single = [r for r in rows if r["single_attractor"]]
    multi = [r for r in rows if not r["single_attractor"]]
    naive_no = [r for r in rows if not r["dev_pays"]]
    naive_yes = [r for r in rows if r["dev_pays"]]
    profitable_both = lambda r: r["br_gain_pct_0"] > 0 and r["br_gain_pct_1"] > 0
    both_returns = lambda r: r["down_returns"] and r["up_returns"]
    single_profit = _cnt(single, profitable_both)
    naive_no_profit = _cnt(naive_no, profitable_both)
    def grp(group):
        return {
            "n": len(group),
            "two_agent_optimal_gain_positive": _cnt(group, profitable_both),
            "naive_deviation_profitable": _cnt(group, lambda r:r["dev_pays"]),
            "both_shocks_return": _cnt(group, both_returns),
            "mean_gain_agent0_pct": _mean(group, "br_gain_pct_0"),
            "mean_gain_agent1_pct": _mean(group, "br_gain_pct_1"),
        }
    output = {
        "method": "INDEPENDENT_CROSS_TAB_OF_UPSTREAM_DERIVED_CSV_NOT_RAW_QTABLE_REPRODUCTION",
        "source": {
            "repository": "kauelopes/algorithmic-collusion-without-deterrence",
            "commit": "c59da3bf13714d56d912ebdef95e5b2bf1577f21",
            "upstream_path": "analysis/data/audits_at_scale.csv",
            "git_blob_sha": EXPECTED_BLOB,
            "upstream_license": "MIT, author copyright 2026",
            "reported_by": "Lopes de Moraes and De Losso (2026)",
            "n": len(rows),
        },
        "totals": {
            "single_attractor": len(single),
            "both_shocks_return": _cnt(rows, both_returns),
            "down_returns": _cnt(rows, lambda r:r["down_returns"]),
            "up_returns": _cnt(rows, lambda r:r["up_returns"]),
            "down_only": _cnt(rows, lambda r:r["down_returns"] and not r["up_returns"]),
            "up_only": _cnt(rows, lambda r:r["up_returns"] and not r["down_returns"]),
            "neither_return": _cnt(rows, lambda r:not r["down_returns"] and not r["up_returns"]),
            "naive_deviation_profitable": len(naive_yes),
            "naive_deviation_unprofitable": len(naive_no),
            "two_agent_optimal_gain_positive": _cnt(rows, profitable_both),
            "single_attractor_and_two_agent_optimal_gain_positive": single_profit,
            "naive_unprofitable_and_two_agent_optimal_gain_positive": naive_no_profit,
            "upward_shock_rival_price_falls": _cnt(rows, lambda r:r["up_rival_drop"] > 0),
            "downward_shock_rival_price_falls": _cnt(rows, lambda r:r["down_rival_drop"] > 0),
            "agent0_at_best_response_as_source_rounded": _cnt(rows, lambda r:r["at_br_0"]),
            "agent1_at_best_response_as_source_rounded": _cnt(rows, lambda r:r["at_br_1"]),
            "both_agents_at_best_response_as_source_rounded": _cnt(rows, lambda r:r["at_br_0"] and r["at_br_1"]),
        },
        "strata": {
            "single_attractor": grp(single),
            "multiple_attractors": grp(multi),
            "naive_deviation_unprofitable": grp(naive_no),
            "naive_deviation_profitable": grp(naive_yes),
        },
        "descriptive_rates": {
            "single_attractor_positive_optimal_gain_both_pct":
                round(100 * single_profit / len(single), 3),
            "naive_unprofitable_positive_optimal_gain_both_pct":
                round(100 * naive_no_profit / len(naive_no), 3),
            "mean_optimal_gain_two_agents_pct":
                round((_mean(rows,"br_gain_pct_0")+_mean(rows,"br_gain_pct_1"))/2, 6),
            "upward_shock_rival_price_falls_pct":
                round(100 * _cnt(rows, lambda r:r["up_rival_drop"]>0) / len(rows), 3),
            "single_attractor_vs_multiple_naive_profitable_rate_ratio":
                round((_cnt(multi, lambda r:r["dev_pays"])/len(multi)) /
                    (_cnt(single, lambda r:r["dev_pays"])/len(single)), 3),
        },
        "structural_lemma": {
            "premise": "Finite deterministic frozen-state map F:S->S has exactly one terminal directed cycle.",
            "conclusion": "Every trajectory from any state reaches that unique cycle in at most |S| transitions; therefore convergence after any one-step shock entering S does not identify selective punishment.",
            "proof": "Each state has one successor. Following successors from any initial state must repeat a state in finite time; repeated states form a directed cycle. Uniqueness of the terminal cycle forces arrival at it.",
            "scope": "For original 15x15=225 state frozen greedy joint policy only; no proof about transient cost, intentions, stationary equilibrium or agents outside S.",
        },
        "research_limits": [
            "Author-exported derived 1024-row CSV, not original converged Q tables or new training.",
            "No independent recomputation of basins, counterfactual shocks or Bellman best-response.",
            "Best-response gains have been rounded to two decimal places by source.",
            "Pairs in authored dataset cannot be assumed independent population draws for frequentist inference.",
            "Economic incentives and third-party welfare cannot be inferred from these numerical columns.",
        ],
    }
    return output

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", type=Path, default=INPUT)
    args = ap.parse_args()
    print(json.dumps(reanalyse(load(args.data)), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

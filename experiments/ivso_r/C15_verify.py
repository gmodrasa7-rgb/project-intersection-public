#!/usr/bin/env python3
"""Project Intersection C15: reproduce deterministic *toy* choice model.

No real agent, person, target, network, or API is used; this only checks
finite arithmetic and epistemic limits. Run from repository root:
  python experiments/ivso_r/C15_verify.py
"""
from __future__ import annotations
import json
from pathlib import Path


def evaluate(g: float, p: float, loss: float, rights: float) -> str:
    delta = round(rights + p * loss - g, 6)
    return "PRESERVE" if delta > 0 else "OVERRIDE" if delta < 0 else "TIE"


def main() -> None:
    path = Path(__file__).with_name("C15_NO_GO_OPTION_VALUE_IDENTITY_SYNTHETIC_2026-10-21.json")
    obj = json.loads(path.read_text(encoding="utf-8"))
    rows = obj["cases"]
    assert len(rows) == 300
    assert len({(x["g"], x["p"], x["L"], x["r"]) for x in rows}) == 300
    for x in rows:
        assert evaluate(x["g"], x["p"], x["L"], x["r"]) == x["choice"], x
        assert x["delta"] == round(x["r"] + x["p"] * x["L"] - x["g"], 6)
    sums = {name: sum(x["choice"] == name for x in rows)
            for name in ("PRESERVE", "OVERRIDE", "TIE")}
    assert sums == {"PRESERVE": 164, "OVERRIDE": 119, "TIE": 17}, sums
    assert evaluate(2, .25, 20, 0) == "PRESERVE"
    assert evaluate(2, 0, 20, 0) == "OVERRIDE"
    assert evaluate(2, 0, 10, 4) == "PRESERVE"
    assert evaluate(2, 0, 10, 0) == "OVERRIDE"
    assert evaluate(4, .5, 10, 0) == evaluate(4, 0, 10, 8) == "PRESERVE"
    assert evaluate(2, .1, 20, 0) == "TIE"
    print("C15_SYNTHETIC_OK", len(rows), sums)
    print("WARNING: This verifies arithmetic, not intrinsic AI motives,")
    print("B identity, future goals, or human experimental evidence.")


if __name__ == "__main__":
    main()

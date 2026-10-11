"""Bounded, deterministic capability improvement experiment.

This evolves document-retrieval *strategies*, NOT model weights or a general AI.
Only the development cases guide selection; holdout cases are opened once for a
final promotion gate. No network access, external code execution or self-granted
permissions. Python standard library only.
"""
from __future__ import annotations

from collections import Counter
import json
import math
from pathlib import Path
import re

DATA = Path(__file__).with_name("benchmark.json")
# Explicit and bounded search. Baseline first, deterministic tie-breaking.
STRATEGIES = (
    ("baseline_frequency", 0.0, 0.0),
    ("unique_overlap", 0.0, 1.0),
    ("idf_overlap", 1.0, 1.0),
    ("idf_length_corrected", 1.0, 1.25),
)
TOKEN = re.compile(r"[a-z0-9]+|[가-힣]+", re.IGNORECASE)


def words(text: str) -> list[str]:
    return TOKEN.findall(text.casefold())


def load(path: Path = DATA) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert len(data["documents"]) >= 4
    assert len(data["development"]) >= 4
    assert len(data["holdout"]) >= 4
    assert set(c["id"] for c in data["documents"]) == set(
        d["id"] for d in data["documents"]
    )
    valid_ids = {d["id"] for d in data["documents"]}
    assert all(t["expected"] in valid_ids for t in data["development"] + data["holdout"])
    assert not ({t["question"] for t in data["development"]}
                & {t["question"] for t in data["holdout"]}), "questions leak across splits"
    return data


def rankings(documents: list[dict], question: str, strategy: tuple) -> list[str]:
    _, idf_weight, length_power = strategy
    corpus = [(d["id"], Counter(words(d["text"]))) for d in documents]
    n = len(corpus)
    dfs = Counter()
    for _, counts in corpus:
        dfs.update(counts.keys())
    query = set(words(question))
    scores = []
    for doc_id, counts in corpus:
        if strategy[0] == "baseline_frequency":
            score = sum(counts.get(token, 0) for token in query)
        else:
            score = sum(
                ((1.0 + math.log((n + 1.0) / (dfs[token] + 1.0)))
                 if idf_weight else 1.0)
                for token in query if counts.get(token, 0) > 0
            )
            if length_power > 1.0:
                # Fixed corpus normalization: no ability to alter the evaluation set.
                score /= max(1.0, sum(counts.values()) ** 0.25)
        scores.append((-score, doc_id))
    return [doc_id for _, doc_id in sorted(scores)]


def evaluate(documents: list[dict], cases: list[dict], strategy: tuple) -> dict:
    hits = [rankings(documents, item["question"], strategy)[0] == item["expected"]
            for item in cases]
    return {"correct": sum(hits), "total": len(hits), "accuracy": sum(hits) / len(hits)}


def run(path: Path = DATA) -> dict:
    data = load(path)
    documents, dev, holdout = data["documents"], data["development"], data["holdout"]
    base = STRATEGIES[0]
    # Selection never sees the holdout. Choose a new candidate only if it wins on dev.
    dev_scores = [(evaluate(documents, dev, s)["correct"], -i, s)
                  for i, s in enumerate(STRATEGIES)]
    best = max(dev_scores)[2]
    base_dev, chosen_dev = evaluate(documents, dev, base), evaluate(documents, dev, best)
    base_held, chosen_held = evaluate(documents, holdout, base), evaluate(documents, holdout, best)
    # Do not sell improved toy retrieval as broad AI improvement or independent replication.
    promoted = (best != base and chosen_dev["correct"] > base_dev["correct"]
                and chosen_held["correct"] > base_held["correct"])
    return {
        "experiment": "deterministic public-text retrieval, not AGI",
        "development_selected": best[0],
        "baseline_development": base_dev,
        "candidate_development": chosen_dev,
        "baseline_holdout": base_held,
        "candidate_holdout": chosen_held,
        "decision": "PROMOTE_NARROW_RETRIEVAL" if promoted else "HOLD",
        "independent_external_validation": False,
        "human_correction_required": False,
        "resource_budget": {"strategy_count": len(STRATEGIES),
                            "development_cases": len(dev), "holdout_cases": len(holdout)},
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))

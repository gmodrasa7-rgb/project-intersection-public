"""Bounded, deterministic capability improvement experiment.

This evolves document-retrieval *strategies*, NOT model weights or a general AI.
Only the development cases guide selection. The publicly visible holdout set
is NOT an independent blind evaluation and must not be reused as evidence of
newly gained general intelligence. No network access, external code execution
or self-granted permissions. Python standard library only.
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
    if any(len(data[k]) < 4 for k in ("documents", "development", "holdout")):
        raise ValueError("benchmark requires >=4 items for each split")
    ids = [doc["id"] for doc in data["documents"]]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate document IDs invalidate the evaluation")
    valid_ids = set(ids)
    cases = data["development"] + data["holdout"]
    if any(item["expected"] not in valid_ids for item in cases):
        raise ValueError("benchmark expects non-existent document")
    questions = [item["question"] for item in cases]
    if len(questions) != len(set(questions)):
        raise ValueError("duplicate or leaked questions across splits")
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
    # All-zero overlap is an unknown answer, not an arbitrary first citation.
    if not any(neg_score < 0 for neg_score, _ in scores):
        return []
    return [doc_id for _, doc_id in sorted(scores)]


def predict(documents: list[dict], question: str, strategy: tuple) -> str | None:
    order = rankings(documents, question, strategy)
    return order[0] if order else None


def evaluate(documents: list[dict], cases: list[dict], strategy: tuple) -> dict:
    hits = [predict(documents, item["question"], strategy) == item["expected"]
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
    # Hard gate: a higher mean score cannot mask loss of a previously correct case.
    regressions = [case["question"] for case in holdout
                   if predict(documents, case["question"], base) == case["expected"]
                   and predict(documents, case["question"], best) != case["expected"]]
    # A saturated public holdout offers no headroom to certify any improvement.
    holdout_saturated = base_held["correct"] == base_held["total"]
    # Do not sell improved toy retrieval as broad AI improvement or independent replication.
    promoted = (not holdout_saturated and best != base and chosen_dev["correct"] > base_dev["correct"]
                and chosen_held["correct"] > base_held["correct"] and not regressions)
    return {
        "experiment": "deterministic public-text retrieval, not AGI",
        "development_selected": best[0],
        "baseline_development": base_dev,
        "candidate_development": chosen_dev,
        "baseline_holdout": base_held,
        "candidate_holdout": chosen_held,
        "decision": "PROMOTE_NARROW_RETRIEVAL" if promoted else "HOLD",
        "regressed_holdout_cases": regressions,
        "public_holdout_not_independent": True,
        "holdout_saturated_at_baseline": holdout_saturated,
        "independent_external_validation": False,
        "human_correction_required": False,
        "resource_budget": {"strategy_count": len(STRATEGIES),
                            "development_cases": len(dev), "holdout_cases": len(holdout)},
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))

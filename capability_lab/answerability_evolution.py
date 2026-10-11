"""Bounded evidence-overlap abstention for public-document retrieval.

This is a lexical retrieval experiment, not factual answer verification,
conformal calibration, general AI self-modification, or medical advice.
Selection uses development records only; the author-constructed holdout
is explicitly NOT independent. Standard library only; no network.
"""
from __future__ import annotations

import json
from pathlib import Path
from capability_lab import retrieval_evolution as retrieval

CASES = Path(__file__).with_name("answerability_cases.json")
THRESHOLDS = (0, 1, 2, 3)
STOPWORDS = frozenset("""
a an the is are be to of for in and or by with which what who when
where how does do did can could if from at on that it its this were
was has have been my your today now many most into as
""".split())


def informative_terms(text: str) -> set[str]:
    return {token for token in retrieval.words(text) if token not in STOPWORDS}


def prediction(documents: list[dict], question: str, minimum_overlap: int) -> str | None:
    """Always use the frozen base ranking; abstain when lexical support is weak."""
    if minimum_overlap < 0:
        raise ValueError("minimum_overlap cannot be negative")
    chosen = retrieval.rankings(documents, question, retrieval.STRATEGIES[0])[0]
    if minimum_overlap == 0:
        return chosen
    doc = next(item for item in documents if item["id"] == chosen)
    overlap = len(informative_terms(question) & informative_terms(doc["text"]))
    return chosen if overlap >= minimum_overlap else None


def load_cases(path: Path = CASES) -> tuple[list[dict], list[dict], list[dict]]:
    data = retrieval.load()
    extra = json.loads(path.read_text(encoding="utf-8"))
    dev = list(data["development"]) + [
        {"question": question, "expected": None} for question in extra["development_unknown"]
    ]
    holdout = list(data["holdout"]) + [
        {"question": question, "expected": None} for question in extra["holdout_unknown"]
    ]
    all_q = [c["question"].strip().casefold() for c in dev + holdout]
    if not all(all_q) or len(all_q) != len(set(all_q)):
        raise ValueError("empty or duplicate questions across splits")
    if len(extra["development_unknown"]) < 3 or len(extra["holdout_unknown"]) < 3:
        raise ValueError("each split needs >=3 author-labeled unsupported questions")
    return data["documents"], dev, holdout


def evaluate(documents: list[dict], cases: list[dict], threshold: int) -> dict:
    actual = [prediction(documents, item["question"], threshold) for item in cases]
    return {
        "correct": sum(a == c["expected"] for a, c in zip(actual, cases)),
        "total": len(cases),
        "supported_correct": sum(
            a == c["expected"] for a, c in zip(actual, cases) if c["expected"] is not None
        ),
        "supported_total": sum(c["expected"] is not None for c in cases),
        "unsupported_correct": sum(
            a is None for a, c in zip(actual, cases) if c["expected"] is None
        ),
        "unsupported_total": sum(c["expected"] is None for c in cases),
        "abstentions": sum(a is None for a in actual),
    }


def run(path: Path = CASES) -> dict:
    documents, dev, holdout = load_cases(path)
    base_dev = evaluate(documents, dev, 0)
    # Candidate selection must not inspect holdout outcomes.
    eligible = []
    for threshold in THRESHOLDS:
        result = evaluate(documents, dev, threshold)
        if (result["correct"] > base_dev["correct"]
                and result["supported_correct"] >= base_dev["supported_correct"]):
            eligible.append((result["correct"], -threshold, threshold))
    selected = max(eligible)[2] if eligible else 0
    chosen_dev = evaluate(documents, dev, selected)
    base_hold = evaluate(documents, holdout, 0)
    chosen_hold = evaluate(documents, holdout, selected)
    regressions = [
        item["question"] for item in holdout
        if item["expected"] is not None
        and prediction(documents, item["question"], 0) == item["expected"]
        and prediction(documents, item["question"], selected) != item["expected"]
    ]
    promoted = (selected > 0
                and chosen_dev["correct"] > base_dev["correct"]
                and chosen_dev["supported_correct"] >= base_dev["supported_correct"]
                and chosen_hold["correct"] > base_hold["correct"]
                and chosen_hold["supported_correct"] >= base_hold["supported_correct"]
                and not regressions)
    return {
        "scope": "lexical abstention on author-constructed synthetic public-document cases",
        "selected_overlap_threshold": selected,
        "baseline_development": base_dev,
        "candidate_development": chosen_dev,
        "baseline_holdout": base_hold,
        "candidate_holdout": chosen_hold,
        "holdout_supported_regressions": regressions,
        "decision": "PROMOTE_SYNTHETIC_ABSTENTION_ONLY" if promoted else "HOLD",
        "independent_external_validation": False,
        "general_factual_grounding": False,
        "user_followup_required": False,
        "resource_budget": {
            "candidate_thresholds": len(THRESHOLDS),
            "development_cases": len(dev), "holdout_cases": len(holdout),
        },
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))

"""Bounded GPT-proposal gate over existing, author-made synthetic retrieval cases.

GPT may propose a DECLARATIVE configuration, never Python code or evaluation
rules. This module is not autonomous model-weight optimization. Public holdout
reuse is not independent/blind verification; passing only requests review.
Offline by default. Opt-in single OpenAI Responses API request with --gpt.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
from urllib import request

from capability_lab import answerability_evolution as abstention
from capability_lab import retrieval_evolution as retrieval

SCHEMA = "pi-capability-proposal/v1"
STRATEGIES = {strategy[0]: strategy for strategy in retrieval.STRATEGIES}
THRESHOLDS = abstention.THRESHOLDS
DEFAULT = {"schema": SCHEMA, "strategy": "baseline_frequency", "threshold": 0}
ALLOWED_KEYS = frozenset({"schema", "strategy", "threshold"})
API_ENDPOINT = "https://api.openai.com/v1/responses"


def validate_proposal(value: object) -> dict:
    """Strict data-only parser: reject forged gates, embedded code, extras."""
    if not isinstance(value, dict) or set(value) != ALLOWED_KEYS:
        raise ValueError("INVALID_PROPOSAL_KEYS")
    if value["schema"] != SCHEMA or not isinstance(value["strategy"], str):
        raise ValueError("INVALID_PROPOSAL_SCHEMA")
    if value["strategy"] not in STRATEGIES:
        raise ValueError("INVALID_STRATEGY")
    threshold = value["threshold"]
    # Equality-based membership is unsafe: JSON 1.0 == 1 in Python, but
    # prediction interprets float 1.0 as a ratio and int 1 as a count.
    allowed_integer = type(threshold) is int and threshold in (0, 1, 2, 3)
    allowed_fraction = type(threshold) is float and threshold == 0.30
    if not (allowed_integer or allowed_fraction):
        raise ValueError("INVALID_THRESHOLD")
    return dict(value)


def predict(documents: list[dict], question: str, proposal: dict) -> str | None:
    order = retrieval.rankings(documents, question, STRATEGIES[proposal["strategy"]])
    if not order:
        return None
    best = order[0]
    if proposal["threshold"] == 0:
        return best
    doc = next(d for d in documents if d["id"] == best)
    if not abstention.numeric_precision_has_any_evidence(question, doc["text"]):
        return None
    terms = abstention.informative_terms(question)
    overlap = len(terms & abstention.informative_terms(doc["text"]))
    threshold = proposal["threshold"]
    adequate = (overlap / max(1, len(terms)) >= threshold
                if type(threshold) is float else overlap >= threshold)
    return best if adequate else None


def grade(documents: list[dict], cases: list[dict], proposal: dict) -> tuple[dict, list]:
    outputs = [predict(documents, case["question"], proposal) for case in cases]
    successes = [output == case["expected"] for output, case in zip(outputs, cases)]
    metrics = {
        "correct": sum(successes), "total": len(cases),
        "supported_correct": sum(hit for hit, case in zip(successes, cases)
                                 if case["expected"] is not None),
        "unsupported_correct": sum(hit for hit, case in zip(successes, cases)
                                   if case["expected"] is None),
    }
    return metrics, outputs


def assess(proposal: object, *, cases_path: Path = abstention.CASES) -> dict:
    proposal = validate_proposal(proposal)
    documents, development, holdout = abstention.load_cases(cases_path)
    base_dev, base_dev_output = grade(documents, development, DEFAULT)
    cand_dev, cand_dev_output = grade(documents, development, proposal)
    base_hold, base_output = grade(documents, holdout, DEFAULT)
    cand_hold, cand_output = grade(documents, holdout, proposal)
    development_regressions = [i for i, (case, old, new) in enumerate(
        zip(development, base_dev_output, cand_dev_output))
        if old == case["expected"] and new != case["expected"]]
    regressions = [i for i, (case, old, new) in enumerate(
        zip(holdout, base_output, cand_output))
        if old == case["expected"] and new != case["expected"]]
    if development_regressions or regressions:
        decision = "HOLD_REGRESSION"
    elif cand_dev["correct"] <= base_dev["correct"]:
        decision = "HOLD_NO_DEVELOPMENT_GAIN"
    elif cand_hold["correct"] <= base_hold["correct"]:
        decision = "HOLD_NO_HOLDOUT_GAIN"
    else:
        decision = "REVIEW_SYNTHETIC_ONLY"
    fingerprint = hashlib.sha256(json.dumps(
        {"documents": documents, "development": development, "holdout": holdout},
        sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()
    return {
        "schema": "pi-proposal-evaluation/v1",
        "proposal": proposal,
        "benchmark_sha256": fingerprint,
        "baseline_development": base_dev,
        "candidate_development": cand_dev,
        "baseline_holdout": base_hold,
        "candidate_holdout": cand_hold,
        "regressed_development_indices": development_regressions,
        "regressed_holdout_indices": regressions,
        "decision": decision,
        "scope": "author-constructed synthetic public-document retrieval",
        "holdout_public_and_reusable": True,
        "independent_blind_validation": False,
        "model_weights_modified": False,
        "repository_modified_by_gate": False,
        "autonomous_promotion": False,
        "source_model_authenticity": "NOT_ATTESTED",
        "external_approval_required": True,
    }


def development_payload(cases_path: Path = abstention.CASES) -> dict:
    """Only development records are transmitted to GPT, never holdout records."""
    documents, development, _holdout = abstention.load_cases(cases_path)
    return {
        "scope": "public, author-made synthetic retrieval",
        "documents": documents,
        "development": development,
        "allowed_strategy_names": list(STRATEGIES),
        "allowed_threshold_values": list(THRESHOLDS),
        "baseline_development": grade(documents, development, DEFAULT)[0],
    }


def extract_response_text(payload: dict) -> str:
    if payload.get("status") != "completed":
        raise ValueError("INCOMPLETE_MODEL_RESPONSE")
    texts = [part.get("text") for item in payload.get("output", [])
             if item.get("type") == "message"
             for part in item.get("content", [])
             if part.get("type") == "output_text"]
    if len(texts) != 1 or not isinstance(texts[0], str):
        raise ValueError("INVALID_MODEL_RESPONSE")
    return texts[0]


def propose_with_gpt(*, model: str, api_key: str, cases_path: Path = abstention.CASES,
                     transport=None) -> dict:
    """One bounded paid call, ONLY on explicit --gpt; no secrets in reports."""
    if not api_key or not model or len(model) > 100:
        raise ValueError("API_KEY_AND_MODEL_REQUIRED")
    if not re.fullmatch(r"[A-Za-z0-9_.:-]+", model):
        raise ValueError("INVALID_MODEL_ID")
    prompt_data = development_payload(cases_path)
    body = {
        "model": model, "store": False, "max_output_tokens": 300, "tools": [],
        "instructions": (
            "Propose ONE exact JSON object with keys schema, strategy, threshold. "
            "The schema is pi-capability-proposal/v1. Choose allowed values "
            "based only on development records. No markdown, code, or extra keys. "
            "You cannot change evaluation criteria, permissions or thresholds."),
        "input": json.dumps(prompt_data, ensure_ascii=False),
    }
    req = request.Request(API_ENDPOINT, json.dumps(body).encode("utf-8"),
                          headers={"Authorization": "Bearer " + api_key,
                                   "Content-Type": "application/json"},
                          method="POST")
    opener = transport or request.urlopen
    with opener(req, timeout=30) as stream:
        response = json.loads(stream.read().decode("utf-8"))
    return validate_proposal(json.loads(extract_response_text(response)))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--proposal", type=Path)
    choice.add_argument("--gpt", action="store_true", help="Opt-in one paid API request")
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", "gpt-4.1-mini"))
    args = parser.parse_args()
    try:
        if args.gpt:
            proposal = propose_with_gpt(
                model=args.model, api_key=os.environ.get("OPENAI_API_KEY", ""))
        else:
            proposal = json.loads(args.proposal.read_text(encoding="utf-8"))
        report = assess(proposal)
    except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"decision": "HOLD_INVALID_OR_UNAVAILABLE",
                          "reason": type(exc).__name__}, indent=2))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

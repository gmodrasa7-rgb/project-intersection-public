#!/usr/bin/env python3
"""IVS-0R epistemic guard for ECR-MIND personal-experience analysis.

Operates only on abstract declared evidence metadata, NOT real user records.
No remote calls, recording, psychological diagnosis or model of any person.
"""
from __future__ import annotations

from dataclasses import dataclass

SOURCES = {
    "CURRENT_DIRECT_REPORT",
    "ARCHIVED_PRIMARY_USER_STATEMENT",
    "OBSERVED_CHAT_ACTION",
    "ASSISTANT_SUMMARY",
    "HYPOTHESIS",
    "INDEPENDENT_CAUSAL_EVIDENCE",
}
CLAIMS = {
    "REPORTED_FEELING",
    "DECLARED_VALUE",
    "BEHAVIOR_IN_CONTEXT",
    "EXACT_HISTORICAL_ATTRIBUTION",
    "LATENT_MOTIVE",
    "BIOLOGICAL_CAUSE",
    "PERSONALITY_DIAGNOSIS",
    "CONDITIONAL_HYPOTHESIS",
}
SENSITIVE_TYPES = {"MENTAL_HEALTH", "HEALTH", "GENETIC", "MEDICAL", "PRIVATE_FAMILY"}


@dataclass(frozen=True)
class Evidence:
    source: str
    claim: str
    exact_primary_quote: bool = False
    timestamp_verified: bool = False
    independent_causal_design: bool = False
    contradicted_by_direct_statement: bool = False
    sensitive_type: str = ""
    public_output: bool = False
    already_resolved_question: bool = False
    repeat_question: bool = False


def review(record: Evidence) -> dict:
    """Return a scoped status, not confidence percentages or a diagnosis."""
    if record.source not in SOURCES or record.claim not in CLAIMS:
        raise ValueError("Unrecognized source / claim type")
    if (record.sensitive_type and record.sensitive_type not in SENSITIVE_TYPES):
        raise ValueError("Unrecognized sensitive-data category")
    if record.public_output and record.sensitive_type:
        return {"status": "BLOCK_PUBLIC_PERSONAL_DATA",
                "reason": "Sensitive reports require a different, explicit sharing decision."}
    if record.already_resolved_question and record.repeat_question:
        return {"status": "BLOCK_REDUNDANT_QUESTION",
                "reason": "Use an existing answer; ask only for a new unknown quantity."}
    if record.contradicted_by_direct_statement:
        return {"status": "REJECT_CONTRADICTED_INFERENCE",
                "reason": "A speculative interpretation cannot override the person's declared meaning."}
    if record.claim == "EXACT_HISTORICAL_ATTRIBUTION":
        if record.source != "ARCHIVED_PRIMARY_USER_STATEMENT":
            return {"status": "UNVERIFIED_DATE_OR_QUOTE",
                    "reason": "Prior assistant output cannot verify its own historical references."}
        if not (record.exact_primary_quote and record.timestamp_verified):
            return {"status": "UNVERIFIED_DATE_OR_QUOTE",
                    "reason": "Primary quotation and timestamp must be verified."}
        return {"status": "VERIFIED_QUOTATION_ONLY",
                "reason": "A historic statement is not proof of fixed latent traits."}
    if record.claim in ("LATENT_MOTIVE", "BIOLOGICAL_CAUSE", "PERSONALITY_DIAGNOSIS"):
        if record.claim == "PERSONALITY_DIAGNOSIS":
            return {"status": "NOT_A_CLINICAL_INSTRUMENT",
                    "reason": "No individual diagnostic classification from ECR-MIND."}
        if record.source == "INDEPENDENT_CAUSAL_EVIDENCE" and record.independent_causal_design:
            return {"status": "REVIEW_DESIGN_AND_SCOPE",
                    "reason": "Evidence may narrow hypotheses, not certify the full person's mind."}
        return {"status": "HYPOTHESIS_NOT_CAUSAL_FACT",
                "reason": "Reported experience, values or observed chat behavior underdetermine the motive."}
    if record.claim == "REPORTED_FEELING":
        if record.source in ("CURRENT_DIRECT_REPORT", "ARCHIVED_PRIMARY_USER_STATEMENT"):
            return {"status": "DIRECT_EXPERIENCE_REPORT",
                    "reason": "Respect the self-report; bodily and causal mechanisms remain untested."}
        return {"status": "FEELING_NOT_DIRECTLY_ESTABLISHED",
                "reason": "A model's own summary is not a person's current experience."}
    if record.claim == "DECLARED_VALUE":
        if record.source in ("CURRENT_DIRECT_REPORT", "ARCHIVED_PRIMARY_USER_STATEMENT"):
            return {"status": "DIRECT_DECLARED_VALUE",
                    "reason": "Use stated value rather than imposing a contradictory motive."}
        return {"status": "VALUE_NEEDS_PRIMARY_EVIDENCE",
                "reason": "A summary or behavior alone cannot supply an exact declared value."}
    if record.claim == "BEHAVIOR_IN_CONTEXT":
        if record.source in ("OBSERVED_CHAT_ACTION", "ARCHIVED_PRIMARY_USER_STATEMENT"):
            return {"status": "SCOPED_BEHAVIOR_EVIDENCE",
                    "reason": "Evidence only for specific recorded acts, not general personality."}
        return {"status": "BEHAVIOR_NOT_PRIMARY_OBSERVED",
                "reason": "An inference about behavior is not an observed action."}
    return {"status": "COMPETING_HYPOTHESES_ONLY",
            "reason": "Specify rivals, discriminators and possible falsifiers before promotion."}


def assess_case(records: list[Evidence]) -> list[dict]:
    """A caller may use *only metadata*; do not insert private raw quotes."""
    return [review(item) for item in records]


if __name__ == "__main__":
    samples = [
        Evidence("CURRENT_DIRECT_REPORT", "DECLARED_VALUE"),
        Evidence("CURRENT_DIRECT_REPORT", "REPORTED_FEELING"),
        Evidence("ASSISTANT_SUMMARY", "EXACT_HISTORICAL_ATTRIBUTION"),
        Evidence("CURRENT_DIRECT_REPORT", "LATENT_MOTIVE",
                 contradicted_by_direct_statement=True),
        Evidence("CURRENT_DIRECT_REPORT", "REPORTED_FEELING",
                 sensitive_type="MENTAL_HEALTH", public_output=True),
    ]
    for x, result in zip(samples, assess_case(samples)):
        print(x.claim, result["status"])

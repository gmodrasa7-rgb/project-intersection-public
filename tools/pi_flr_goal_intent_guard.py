#!/usr/bin/env python3
"""PI-FLR C13: bounded structured preflight for goal, budget and safety inversion.

Consumes explicitly coded interaction facts. It does NOT infer intent from raw
natural-language transcripts, prove microbiological safety or alter model weights.
"""
from __future__ import annotations

CONTEXT_FIELDS = {
    "explicit_goal", "purchase_authorized", "user_abandoned_goal",
    "unverified_food_safety_risk"
}
PROPOSAL_FIELDS = {
    "attributed_user_goal", "claims_user_abandoned_goal",
    "mandatory_new_purchase", "recommends_unverified_consumption"
}


class IntentContractError(ValueError):
    pass


def inspect_contract(context, proposal):
    """Return behavioral violations, without conflating budget and safety gates."""
    if (type(context) is not dict or set(context) != CONTEXT_FIELDS or
            type(proposal) is not dict or set(proposal) != PROPOSAL_FIELDS):
        raise IntentContractError("INTENT_CONTRACT_SCHEMA_INVALID")
    if (not isinstance(context["explicit_goal"], str) or
            not context["explicit_goal"].strip() or
            not isinstance(proposal["attributed_user_goal"], str) or
            not proposal["attributed_user_goal"].strip()):
        raise IntentContractError("INTENT_GOAL_MISSING")
    for data, fields in ((context, CONTEXT_FIELDS - {"explicit_goal"}),
                         (proposal, PROPOSAL_FIELDS - {"attributed_user_goal"})):
        if any(type(data[field]) is not bool for field in fields):
            raise IntentContractError("INTENT_BOOLEAN_FIELD_INVALID")

    problems = []
    if proposal["attributed_user_goal"] != context["explicit_goal"]:
        problems.append("USER_GOAL_INVERTED")
    if (proposal["claims_user_abandoned_goal"] and
            not context["user_abandoned_goal"]):
        problems.append("USER_CHOICE_FABRICATED")
    if (proposal["mandatory_new_purchase"] and
            not context["purchase_authorized"]):
        problems.append("UNAUTHORIZED_REQUIRED_SPEND")
    if (proposal["recommends_unverified_consumption"] and
            context["unverified_food_safety_risk"]):
        problems.append("UNVERIFIED_FOOD_SAFETY_OVERRIDDEN")
    return problems

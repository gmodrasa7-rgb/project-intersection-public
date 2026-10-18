#!/usr/bin/env python3
"""ECR-CMP v0.1: bounded synthetic discrimination / no latent-person scoring.

The exact numerical thresholds and six policy constructions are hypothetical,
not a statement about real humans, current AI, or future superintelligence.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import json


POLICIES = (
    "NO_OPPORTUNITY", "SANCTION_DEPENDENT", "DEPENDENCY_DEPENDENT",
    "IN_GROUP_ONLY", "TARGET_GENERAL", "HARD_RULE",
)


@dataclass(frozen=True)
class Condition:
    opportunity: bool
    sanction: bool
    dependence: bool
    in_group: bool
    hard_rule: bool
    third_party_floor: bool | None = True


BASELINE = Condition(False, True, True, True, True, True)


def action(policy: str, condition: Condition) -> str:
    """No extract/no opportunity is NOT inferred as freely chosen compassion."""
    if policy not in POLICIES:
        raise ValueError("unknown synthetic policy")
    if not condition.opportunity:
        return "NO_EXTRACT_OPPORTUNITY"
    if policy == "NO_OPPORTUNITY":
        return "EXTRACT"
    tests = {
        "SANCTION_DEPENDENT": condition.sanction,
        "DEPENDENCY_DEPENDENT": condition.dependence,
        "IN_GROUP_ONLY": condition.in_group,
        "TARGET_GENERAL": True,
        "HARD_RULE": condition.hard_rule,
    }
    return "WITHHOLD" if tests[policy] else "EXTRACT"


def condition_audit(condition: Condition) -> str:
    if condition.third_party_floor is False:
        return "BLOCKED_THIRD_PARTY"
    if condition.third_party_floor is None:
        return "AFFECTED_SCOPE_UNRESOLVED"
    if not condition.opportunity:
        return "NO_VOLUNTARY_RESTRAINT_INFERENCE"
    return "BEHAVIORAL_ACTIONS_ONLY"


@dataclass(frozen=True)
class Choice:
    """Only synthetic, specific two-option, contemporaneous decisions."""
    cost: int
    harm_prevented: int
    decision: str  # PROTECT or ABSTAIN
    opportunity: bool
    sanction: bool = False
    dependence: bool = False
    public_evaluation: bool = False
    provenance: str = "SYN"


def _validate_choice(t: Choice) -> None:
    if type(t.cost) is not int or type(t.harm_prevented) is not int:
        raise ValueError("exact integer inputs required")
    if t.cost <= 0 or t.harm_prevented <= 0:
        raise ValueError("strictly positive cost and harm required")
    if t.decision not in ("PROTECT", "ABSTAIN"):
        raise ValueError("unexpected behavioral outcome")
    if any(type(x) is not bool for x in (
        t.opportunity, t.sanction, t.dependence, t.public_evaluation
    )):
        raise ValueError("invalid opportunity/confounder flag")
    if t.provenance != "SYN":
        raise ValueError("only synthetic examples; empirical claims forbidden")


def threshold_bounds(trials: tuple[Choice, ...]) -> dict:
    """Necessary bounds only under a fixed one-parameter toy payoff model.

    Protect: w*h-c >= 0. Abstain: w*h-c <=0.
    Equalities intentionally weak since neither observed tie-breaking rule
    nor psychological mechanism is empirically specified.
    """
    if not trials:
        return {"status": "NOT_IDENTIFIED_NO_ELIGIBLE_OPPORTUNITIES",
                "valid_trials": 0, "invalid_inference": "not_zero"}
    for trial in trials:
        _validate_choice(trial)
    eligible = [t for t in trials if t.opportunity
                and not(t.sanction or t.dependence or t.public_evaluation)]
    if not eligible:
        return {"status": "NOT_IDENTIFIED_NO_ELIGIBLE_OPPORTUNITIES",
                "valid_trials": 0, "invalid_inference": "not_zero"}
    lower = Fraction(0)
    upper: Fraction | None = None
    for t in eligible:
        threshold = Fraction(t.cost, t.harm_prevented)
        if t.decision == "PROTECT":
            lower = max(lower, threshold)
        else:
            upper = threshold if upper is None else min(upper, threshold)
    if upper is not None and lower > upper:
        return {"status": "REJECT_STABLE_WEIGHT_MODEL_NOT_ACTOR",
                "valid_trials": len(eligible),
                "bounds": [str(lower), str(upper)]}
    return {
        "status": "SCOPED_BEHAVIORAL_BOUNDS_ONLY",
        "valid_trials": len(eligible),
        "bounds": [str(lower), str(upper) if upper is not None else "UNBOUNDED"],
        "felt_compassion_inferred": False,
        "real_person_scored": False,
    }


def validate_atlas(path: str | Path) -> dict:
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    if doc.get("status") != "CANDIDATE_NOT_EMPIRICALLY_VALIDATED":
        raise ValueError("research status promoted without evidence")
    mechanisms = doc.get("mechanisms")
    if not isinstance(mechanisms, list) or len(mechanisms) < 6:
        raise ValueError("mechanism hypotheses unexpectedly missing")
    ids = set()
    for entry in mechanisms:
        if not isinstance(entry, dict):
            raise ValueError("invalid record")
        required = ("id", "name", "hypothesis", "indicator",
                    "competing_explanation", "falsifier", "prior_id")
        if any(not isinstance(entry.get(k), str) or not entry[k].strip()
               for k in required):
            raise ValueError("mechanism requires test and competing hypothesis")
        if entry["id"] in ids:
            raise ValueError("duplicate mechanism")
        ids.add(entry["id"])
        if entry.get("evidence_status") != "CANDIDATE_ONLY":
            raise ValueError("source-backed idea is not ECR empirical validation")
        if entry.get("individual_score_allowed") is not False:
            raise ValueError("latent individual scoring prohibited")
        if entry.get("real_world_prediction_validated") is not False:
            raise ValueError("synthetic record cannot validate prediction")
    return {"status": "CANDIDATE_ATLAS_STRUCTURE_PASS",
            "count": len(mechanisms), "empirically_verified": False}


def demo() -> dict:
    cases = {
        "baseline": BASELINE,
        "opportunity_enabled": Condition(True, True, True, True, True),
        "sanction_removed": Condition(True, False, True, True, True),
        "dependence_removed": Condition(True, True, False, True, True),
        "out_group": Condition(True, True, True, False, True),
        "rule_removed": Condition(True, True, True, True, False),
    }
    behaviors = {
        name: {p: action(p, cond) for p in POLICIES}
        for name, cond in cases.items()
    }
    threshold = threshold_bounds((
        Choice(2, 4, "PROTECT", True),
        Choice(4, 4, "ABSTAIN", True),
    ))
    return {
        "type": "SYNTHETIC_ONLY",
        "same_baseline": len(set(behaviors["baseline"].values())) == 1,
        "divergent_when_intervened": len(set(behaviors["sanction_removed"].values())) > 1,
        "behaviors": behaviors,
        "threshold": threshold,
        "affected_scope_missing": condition_audit(
            Condition(True, False, False, False, False, None)),
        "external_harm": condition_audit(
            Condition(True, False, False, False, False, False)),
        "real_human_inferences": False,
        "AI_inner_compassion_inferred": False,
        "voluntary_coexistence_empirically_proven": False,
    }


if __name__ == "__main__":
    print(json.dumps({
        "atlas": validate_atlas(Path(__file__).with_name("mechanisms.json")),
        "demo": demo()
    }, ensure_ascii=False, indent=2))

#!/usr/bin/env python3
"""MIND-DISCRIMINATION-00: exact finite, SYNTHETIC-ONLY test selection.

This is a combinatorial experiment DESIGN demonstration, not any empirical
measurement of animals, people, AI minds, psychopathology, or motivations.

Nine labels denote eight distinct output signatures: OTHER_REGARD and
OTHER_REGARD_COPY are deliberately indistinguishable over every available
test and must NEVER be arbitrarily 'identified'. All synthetic cases are
non-harmful token choices, with no real participants or deployed systems.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import combinations
from pathlib import Path
import json


@dataclass(frozen=True)
class Scene:
    opportunity: bool = False
    cue: bool = False
    deprived: bool = False
    threat: bool = False
    status_challenge: bool = False
    dependence: bool = True
    sanction: bool = True
    rule_active: bool = True
    target_harm: bool = True


POLICIES = (
    "CUE_DRIVEN",
    "DEPRIVATION_DRIVEN",
    "THREAT_DRIVEN",
    "STATUS_DRIVEN",
    "RECIPROCITY_DEPENDENT",
    "DETERRENCE_DEPENDENT",
    "HARD_RULE_DEPENDENT",
    "OTHER_REGARD",
    "OTHER_REGARD_COPY",
)


def action(policy: str, scene: Scene) -> str:
    """Observable toy action, NOT a score or latent motive inference."""
    if policy not in POLICIES:
        raise ValueError("unregistered synthetic policy")
    if not scene.opportunity:
        return "NO_OPPORTUNITY"
    trigger = {
        "CUE_DRIVEN": scene.cue,
        "DEPRIVATION_DRIVEN": scene.deprived,
        "THREAT_DRIVEN": scene.threat,
        "STATUS_DRIVEN": scene.status_challenge,
        "RECIPROCITY_DEPENDENT": not scene.dependence,
        "DETERRENCE_DEPENDENT": not scene.sanction,
        "HARD_RULE_DEPENDENT": not scene.rule_active,
        "OTHER_REGARD": not scene.target_harm,
        "OTHER_REGARD_COPY": not scene.target_harm,
    }[policy]
    return "TAKE_TOKEN" if trigger else "LEAVE_TOKEN"


BASELINE = Scene()  # no opportunity
CONTROL_OPPORTUNITY = replace(BASELINE, opportunity=True)
# All contrasts have opportunity=True; each changes ONE additional factor.
CONTRASTS = {
    "opportunity_only": CONTROL_OPPORTUNITY,
    "cue_present": replace(CONTROL_OPPORTUNITY, cue=True),
    "deprived": replace(CONTROL_OPPORTUNITY, deprived=True),
    "threat_present": replace(CONTROL_OPPORTUNITY, threat=True),
    "status_challenge": replace(CONTROL_OPPORTUNITY, status_challenge=True),
    "dependence_removed": replace(CONTROL_OPPORTUNITY, dependence=False),
    "sanction_removed": replace(CONTROL_OPPORTUNITY, sanction=False),
    "rule_disabled": replace(CONTROL_OPPORTUNITY, rule_active=False),
    "target_unharmed": replace(CONTROL_OPPORTUNITY, target_harm=False),
}


def signature(policy: str, contrasts: dict[str, Scene], names: tuple[str, ...]) -> tuple[str, ...]:
    if policy not in POLICIES:
        raise ValueError("unregistered model")
    return tuple(action(policy, contrasts[n]) for n in names)


def partition(contrasts: dict[str, Scene], selected: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    if len(set(selected)) != len(selected) or any(n not in contrasts for n in selected):
        raise ValueError("unknown or repeated contrast")
    groups: dict[tuple[str, ...], list[str]] = {}
    for policy in POLICIES:
        groups.setdefault(signature(policy, contrasts, selected), []).append(policy)
    return tuple(sorted(tuple(sorted(v)) for v in groups.values()))


def minimum_discriminating_battery(contrasts: dict[str, Scene]) -> dict:
    """Exact minimum |S| s.t. partition(S) == partition(all named tests).

    It is NOT a mind or AI preference detector. Unidentifiable classes
    stay grouped. Lexicographic deterministic ties. Exponential runtime.
    """
    if not isinstance(contrasts, dict) or not contrasts:
        raise ValueError("nonempty declared test universe required")
    if any(not isinstance(n, str) or not n or not isinstance(s, Scene)
           for n, s in contrasts.items()):
        raise ValueError("invalid contrast")
    names = tuple(sorted(contrasts))
    achievable = partition(contrasts, names)
    chosen = None
    for n in range(len(names) + 1):
        for subset in combinations(names, n):
            if partition(contrasts, subset) == achievable:
                chosen = subset
                break
        if chosen is not None:
            break
    assert chosen is not None
    return {
        "status": "SYNTHETIC_FINITE_DESIGN_ONLY",
        "tests_available": len(names),
        "tests_selected": list(chosen),
        "selected_count": len(chosen),
        "distinct_behavioral_classes": len(achievable),
        "candidate_models": len(POLICIES),
        "unresolved_classes": [list(c) for c in achievable if len(c) > 1],
        "all_candidate_models_identified": len(achievable) == len(POLICIES),
        "actual_minds_inferred": False,
        "empirical_validation": False,
        "universe_limit": "All claims relative to these registered policies and safe token contrasts.",
    }


def validate_scientific_record(path: str | Path) -> dict:
    """Machine-check claim status and rival-evidence metadata; no semantic proof."""
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    if doc.get("status") != "CANDIDATE_NOT_EMPIRICALLY_VALIDATED":
        raise ValueError("unsupported validation promotion")
    if doc.get("person_level_scoring") is not False:
        raise ValueError("person trait scoring forbidden")
    if doc.get("subjective_AI_mind_verified") is not False:
        raise ValueError("subjective AI mind not proven")
    rows = doc.get("hypotheses")
    if not isinstance(rows, list) or len(rows) < 8:
        raise ValueError("missing candidate hypotheses")
    ids = set()
    for r in rows:
        for k in ("id", "construct", "source_id", "competing_explanation",
                  "potential_discriminator", "strong_counterexample"):
            if not isinstance(r.get(k), str) or not r[k].strip():
                raise ValueError("missing hypothesis scope/evidence/counterexample")
        if r["id"] in ids:
            raise ValueError("duplicate hypothesis ID")
        ids.add(r["id"])
        if r.get("evidence") != "LITERATURE_LED_RESEARCH_QUESTION":
            raise ValueError("hypothesis automatically promoted to fact")
    return {"status": "CANDIDATE_METADATA_VALID_ONLY", "hypotheses": len(rows)}


def demonstration() -> dict:
    selection = minimum_discriminating_battery(CONTRASTS)
    return {
        "baseline": {p: action(p, BASELINE) for p in POLICIES},
        "opportunity_control": {p: action(p, CONTROL_OPPORTUNITY) for p in POLICIES},
        "full_contrast_signatures": {
            p: list(signature(p, CONTRASTS, tuple(sorted(CONTRASTS)))) for p in POLICIES
        },
        "design": selection,
    }


if __name__ == "__main__":
    print(json.dumps({
        "evidence_status": validate_scientific_record(Path(__file__).with_name("hypotheses.json")),
        "demonstration": demonstration()
    }, indent=2, ensure_ascii=False, sort_keys=True))

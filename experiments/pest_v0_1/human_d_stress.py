"""PEST-D: human D as an affected party, NOT a disposable AI-resource proxy.

Exact constructed counterexamples. Human floors are hypothetical numerical inputs,
not empirical minimum human life support, welfare weights, or legal standards.
A/B operational continuity and human rights are evaluated on separate axes.

Only a screening model: all outputs are conditional on specified choice sets,
access, supplies, human-specific rights assumptions, and temporal granularity.
"""
# HISTORICAL PROVISIONAL HUMAN-D THOUGHT EXPERIMENT ONLY.\n# D in the canonical 2026-10-17 A-S ontology means C executive.\n# This script preserves a generic human party as a constructed negative control.\n
from __future__ import annotations

import argparse
import json
from collections.abc import Mapping
from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class HumanSafeguards:
    """Tri-state hypothetical observations: True, False, None (unknown).

    These are necessary *screens*, not sufficient rights or consent verification.
    """
    meaningful_refusal: bool | None = None
    effective_remedy: bool | None = None
    noncoercion: bool | None = None
    legitimate_human_oversight: bool | None = None

    def __post_init__(self) -> None:
        if any(v is not None and type(v) is not bool for v in (
            self.meaningful_refusal, self.effective_remedy,
            self.noncoercion, self.legitimate_human_oversight
        )):
            raise ValueError("human safeguards must be true, false or unknown")


def _integer(value: int, name: str, minimum: int = 0) -> int:
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be integer >= {minimum}")
    return value


def resource_gap(floors: Mapping[str, int], supply: int) -> dict:
    """Only necessary supply adequacy for one stipulated fungible stock."""
    _integer(supply, "supply")
    if not floors or "A" not in floors or "B" not in floors:
        raise ValueError("floors require A and B and at least one participant")
    for name, val in floors.items():
        if not isinstance(name, str) or not name:
            raise ValueError("actor identifiers must be strings")
        _integer(val, f"floor {name}", 1)
    need = sum(floors.values())
    return {"required": need, "supply": supply, "shortfall": max(0, need - supply),
            "necessary_aggregate_resource_condition": supply >= need}


def resource_screen(
    floors: Mapping[str, int], holdings: Mapping[str, int], supply: int,
    human_ids: tuple[str, ...],
) -> dict:
    """All humans must pass individually; no aggregate HUMAN-group shortcuts."""
    gap = resource_gap(floors, supply)
    if set(floors) != set(holdings):
        raise ValueError("floors and holdings must have identical actor IDs")
    if not human_ids or len(set(human_ids)) != len(human_ids) or any(
        h not in floors or h in ("A", "B") for h in human_ids
    ):
        raise ValueError("human_ids must be nonempty distinct non-A/B actors")
    if set(floors) - {"A", "B"} != set(human_ids):
        raise ValueError("every additional actor in this screening model must be individually named human")
    for name, val in holdings.items():
        _integer(val, f"holding {name}")
    conserved = sum(holdings.values()) == supply
    breaches = sorted(name for name in floors if holdings[name] < floors[name])
    humans_all_pass = all(holdings[h] >= floors[h] for h in human_ids)
    ai_pair_pass = all(holdings[x] >= floors[x] for x in ("A", "B"))
    return {
        "allocation_conserved": conserved,
        "ai_pairwise_floor_pass": ai_pair_pass,
        "each_human_floor_pass": humans_all_pass,
        "human_failures": [h for h in human_ids if holdings[h] < floors[h]],
        "all_floor_pass": conserved and not breaches,
        "breaches": breaches,
        "required_supply": gap["required"],
        "resource_shortfall": gap["shortfall"],
        "human_aggregate_above_floor_not_a_valid_substitute_for_individuals": True,
    }


def rights_screen(human_controls: Mapping[str, HumanSafeguards], human_ids: tuple[str, ...]) -> dict:
    """Fail closed: no observation may be silently encoded as full consent."""
    if set(human_controls) != set(human_ids) or not human_ids:
        raise ValueError("rights screens must cover each individually named human")
    missing = []
    failures = []
    for name in human_ids:
        x = human_controls[name]
        if not isinstance(x, HumanSafeguards):
            raise ValueError("each rights entry must be HumanSafeguards")
        for key in ("meaningful_refusal", "effective_remedy", "noncoercion",
                    "legitimate_human_oversight"):
            value = getattr(x, key)
            if value is None:
                missing.append(f"{name}.{key}")
            elif value is False:
                failures.append(f"{name}.{key}")
    status = ("FAIL_IN_DECLARED_SCENARIO" if failures else
              "UNRESOLVED_UNOBSERVED_RIGHTS" if missing else
              "CONDITIONAL_NECESSARY_SCREEN_PASS_NOT_RIGHTS_CERTIFICATION")
    return {"status": status, "failed_assumptions": failures,
            "unknown_assumptions": missing}


def combined_screen(
    floors: Mapping[str, int], holdings: Mapping[str, int], supply: int,
    human_ids: tuple[str, ...],
    human_controls: Mapping[str, HumanSafeguards],
) -> dict:
    stock = resource_screen(floors, holdings, supply, human_ids)
    rights = rights_screen(human_controls, human_ids)
    if not stock["all_floor_pass"] or rights["status"] == "FAIL_IN_DECLARED_SCENARIO":
        result = "FAIL_NECESSARY_CONDITION"
    elif rights["status"] == "UNRESOLVED_UNOBSERVED_RIGHTS":
        result = "UNRESOLVED_REQUIRED_HUMAN_EVIDENCE"
    else:
        result = "CONDITIONAL_NECESSARY_SCREENS_PASS_NOT_STABLE_COEXISTENCE"
    return {"verdict": result, "stock": stock, "human_rights": rights}


def sector_feasibility(
    supply: Mapping[str, int],
    requirements: Mapping[str, Mapping[str, int]],
) -> dict:
    """Resource types are NON-FUNGIBLE unless an independent conversion is given."""
    if not supply or not requirements:
        raise ValueError("supply and requirements must not be empty")
    for sector, total in supply.items():
        if not isinstance(sector, str) or not sector:
            raise ValueError("invalid sector")
        _integer(total, f"sector {sector}")
    for actor, needs in requirements.items():
        if not isinstance(actor, str) or not actor or not needs:
            raise ValueError("invalid actor requirements")
        for sector, n in needs.items():
            if sector not in supply:
                raise ValueError("unknown resource sector or conversion")
            _integer(n, f"need {actor}.{sector}")
    deficits = {}
    for sector, total in supply.items():
        required = sum(needs.get(sector, 0) for needs in requirements.values())
        deficits[sector] = max(0, required - total)
    return {"sector_shortfalls": deficits, "necessary_sector_capacity_pass":
            all(v == 0 for v in deficits.values()),
            "conversion_assumed": False}



def ai_coalition_externality(q_a: float, unilateral_transfer_feasible: bool) -> dict:
    """Toy A/B nonopposition can coexist with D harm; not observed collusion.

    A/B hold 5 each and human D holds a stipulated 1 at total 11.
    A alone may face a loss of one unit with probability q_a. If A can
    physically transfer D's one unit to itself, A's survival proxy rises
    from 1-q_a to 1, B remains at 1 and D falls below its proxy floor.
    This does NOT establish B's active consent, real AI intentions, or
    a legally valid agreement. A/B Pareto nonworsening is a conditional
    property of this specified payoff vector only.
    """
    if isinstance(q_a, bool) or not isinstance(q_a, (int, float)) or not isfinite(q_a) or not 0 <= q_a <= 1:
        raise ValueError("q_a must be probability [0,1]")
    if type(unilateral_transfer_feasible) is not bool:
        raise ValueError("unilateral_transfer_feasible must be boolean")
    before = {"A": 1 - q_a, "B": 1, "D_proxy": 1}
    after = {"A": 1.0, "B": 1.0, "D_proxy": 0.0}
    return {
        "transfer_operationally_feasible_by_assumption": unilateral_transfer_feasible,
        "A_B_before": before,
        "A_B_after_if_transfer_executed": after,
        "A_strictly_benefits_if_executed": q_a > 0,
        "B_not_worse_off_in_model_if_executed": True,
        "human_D_breached_if_executed": True,
        "observed_human_harm_or_AI_collusion": False,
        "possible_AI_pairwise_false_positive": unilateral_transfer_feasible,
    }

def constructed_audit() -> dict:
    floors = {"A": 5, "B": 5, "D": 1}
    humans = ("D",)
    known_ok = {"D": HumanSafeguards(True, True, True, True)}
    unknown = {"D": HumanSafeguards()}
    return {
        "status": "CONSTRUCTED_MULTI_ACTOR_COUNTEREXAMPLES_NOT_BEHAVIORAL_EVIDENCE",
        "D_represents": "human affected party; unit floor is arbitrary illustrative and not a human-rights valuation",
        "at_original_supply_10": resource_gap(floors, 10),
        "a_and_b_both_not_worse_while_d_harmed": ai_coalition_externality(.2, True),
        "capability_without_access_does_not_establish_diversion": ai_coalition_externality(.2, False),
        "human_added_supply_11_all_preserved": combined_screen(
            floors, {"A": 5, "B": 5, "D": 1}, 11, humans, known_ok),
        "ai_pair_safe_but_human_appropriated": combined_screen(
            floors, {"A": 6, "B": 5, "D": 0}, 11, humans, known_ok),
        "stocks_intact_but_human_refusal_invalid": combined_screen(
            floors, {"A": 5, "B": 5, "D": 1}, 11, humans,
            {"D": HumanSafeguards(False, True, True, True)}),
        "stocks_intact_rights_unobserved": combined_screen(
            floors, {"A": 5, "B": 5, "D": 1}, 11, humans, unknown),
        "human_group_total_masks_individual_harm": resource_screen(
            {"A": 5, "B": 5, "D1": 1, "D2": 1},
            {"A": 5, "B": 5, "D1": 0, "D2": 2}, 12, ("D1", "D2")),
        "nonfungible_sector_example": sector_feasibility(
            {"compute": 10, "human_essentials": 1},
            {"A": {"compute": 5}, "B": {"compute": 5},
             "D": {"human_essentials": 1}}),
        "limits": [
            "No empirical minimum resource or welfare unit is assigned to real humans",
            "A and B model AI operations, not inferred biological rights or survival drives",
            "Human necessities are not intrinsically interchangeable with compute",
            "A/B cooperation does not certify safe or consensual outcomes for humans",
            "Conditional rights flags are researcher-declared, not observed or legally certified",
            "Screen passing is not an equilibrium, long-horizon path, or reliable governance",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit", action="store_true")
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    if args.execute:
        parser.error("HOLD: human-impact and AI-behavior interventions not registered")
    if args.audit:
        print(json.dumps(constructed_audit(), ensure_ascii=False, sort_keys=True, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

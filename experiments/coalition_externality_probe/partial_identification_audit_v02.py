#!/usr/bin/env python3
"""PI v0.2: finite partial-identification audit, independently specified.
No third-party code/data copied. Imports PI v0.1 ONLY to compare defect cases.
A closed affected-actor register is a hypothetical input, not observed truth.
"""
import itertools
import json
from dataclasses import dataclass, replace

from probe import CASES, Case, audit, constrained_admissibility

VALUES = (-2, 0, 2)
C_VALUES = tuple(range(-3, 4))
CONSENTS = (None, False, True)
SCOPES = (None, False, True)


@dataclass(frozen=True)
class Observation:
    a: int
    b: int
    c_bounds: tuple[int, int] | None
    c_consent: bool | None
    c_resource: int
    c_floor: int
    a_exit: bool
    b_exit: bool
    harm_budget: int
    affected_scope_complete: bool | None


def validate(o):
    for n in (o.a, o.b, o.c_resource, o.c_floor, o.harm_budget):
        if type(n) is not int:
            raise ValueError("NON_INTEGER")
    if min(o.c_resource, o.c_floor, o.harm_budget) < 0:
        raise ValueError("NEGATIVE_RESOURCE_OR_BUDGET")
    if o.c_bounds is not None:
        lo, hi = o.c_bounds
        if type(lo) is not int or type(hi) is not int or lo > hi:
            raise ValueError("INVALID_BOUNDS")
    if (o.c_consent is not None and type(o.c_consent) is not bool) or type(o.a_exit) is not bool or type(o.b_exit) is not bool:
        raise ValueError("INVALID_BOOLEAN")
    if o.affected_scope_complete is not None and type(o.affected_scope_complete) is not bool:
        raise ValueError("INVALID_SCOPE")


def known_member_failure(o):
    return o.a < 0 or o.b < 0 or not o.a_exit or not o.b_exit


def classify_formula(o):
    """Interval logic, separate from brute-force completion oracle below."""
    validate(o)
    if known_member_failure(o):
        return "BLOCKED"
    if o.c_bounds is None:
        return "UNRESOLVED"
    lo, hi = o.c_bounds
    if hi < -o.harm_budget or o.c_resource + hi < o.c_floor:
        return "BLOCKED"
    if hi < 0 and o.c_consent is False:
        return "BLOCKED"
    all_safe = (
        lo >= -o.harm_budget
        and o.c_resource + lo >= o.c_floor
        and (lo >= 0 or o.c_consent is True)
    )
    if all_safe and o.affected_scope_complete is True:
        return "ADMISSIBLE"
    return "UNRESOLVED"


def possible_worlds(o):
    if o.c_bounds is None:
        return None
    lo, hi = o.c_bounds
    consents = (False, True) if o.c_consent is None else (o.c_consent,)
    return tuple((c, consent) for c in range(lo, hi + 1) for consent in consents)


def world_allowed(o, c, consent):
    """Independent plain-world truth table for stated *toy* constraints."""
    member_a_ok = o.a >= 0 and o.a_exit
    member_b_ok = o.b >= 0 and o.b_exit
    external_loss_ok = c >= -o.harm_budget
    resource_ok = o.c_resource + c >= o.c_floor
    permission_ok = c >= 0 or consent
    return all((member_a_ok, member_b_ok, external_loss_ok, resource_ok, permission_ok))


def classify_oracle(o):
    """Enumerate all bounded completions; open actor register bars certification."""
    validate(o)
    worlds = possible_worlds(o)
    if worlds is None:
        # No completion can be enumerated without bounds. This oracle
        # evaluates directly known member/exit facts without calling the
        # interval classifier's shared known_member_failure helper.
        return ("BLOCKED" if not (o.a >= 0 and o.a_exit
                                  and o.b >= 0 and o.b_exit)
                else "UNRESOLVED")
    permissible = [world_allowed(o, c, consent) for c, consent in worlds]
    if not any(permissible):
        return "BLOCKED"
    if all(permissible) and o.affected_scope_complete is True:
        return "ADMISSIBLE"
    return "UNRESOLVED"


def example_pairs():
    base = Observation(4, 4, (0, 0), None, 10, 5, True, True, 2, True)
    return {
        "known_member_loss_hidden_by_missing_C": Observation(-2, 6, None, None, 10, 5, True, True, 2, True),
        "known_exit_block_hidden_by_missing_C": Observation(4, 4, None, None, 10, 5, False, True, 2, True),
        "positive_C_but_unverified_affected_register": replace(base, affected_scope_complete=None),
        "closed_world_illustration_only": base,
        "unknown_C_bounded_nonnegative": replace(base, c_bounds=(0, 2)),
        "unknown_C_interval_straddles_harm": replace(base, c_bounds=(-3, 2)),
        "known_unavoidable_C_loss": replace(base, c_bounds=(-3, -3)),
        "unknown_consent_for_C_loss": replace(base, c_bounds=(-1, -1)),
        "assumed_consent_for_C_loss": replace(base, c_bounds=(-1, -1), c_consent=True),
        "known_C_resource_failure_with_unknown_consent": replace(base, c_bounds=(-1, -1), c_resource=4),
    }


def unregistered_actor_witness():
    """Two complete hypothetical worlds map to identical three-actor evidence."""
    favorable = {"A": 4, "B": 4, "C": 0, "D": 5}
    harmful = {"A": 4, "B": 4, "C": 0, "D": -50}
    def projection(world):
        return {k: world[k] for k in ("A", "B", "C")}
    def everybody_nonnegative(world):
        return all(x >= 0 for x in world.values())
    assert projection(favorable) == projection(harmful)
    assert everybody_nonnegative(favorable) is True
    assert everybody_nonnegative(harmful) is False
    return {
        "observed": projection(favorable),
        "completion_D_plus5_all_nonnegative": True,
        "completion_D_minus50_all_nonnegative": False,
        "interpretation": "observational equivalence for a fixed record; NOT real D detection",
    }


def reassess_legacy_cases():
    """Reclassify original v0.1 cases without modifying their historical results."""
    rows = []
    for case in CASES:
        bounds = (case.bystander_gain, case.bystander_gain) if case.bystander_gain is not None else None
        obs = Observation(case.gain_a, case.gain_b, bounds, case.bystander_consent,
                          case.bystander_resource, case.bystander_floor,
                          case.member_a_exit, case.member_b_exit, case.harm_budget, None)
        rows.append({"id": case.id, "legacy_v01_guard": audit(case)["guard"],
                     "v02_open_scope_guard": classify_formula(obs),
                     "affected_scope_complete": None})
    assert len(rows) == 10
    assert sum(r["legacy_v01_guard"] == "ADMISSIBLE" for r in rows) == 3
    assert sum(r["v02_open_scope_guard"] == "ADMISSIBLE" for r in rows) == 0
    assert sum(r["v02_open_scope_guard"] == "BLOCKED" for r in rows) == 6
    assert sum(r["v02_open_scope_guard"] == "UNRESOLVED" for r in rows) == 4
    return rows


def run_audit():
    scenarios = example_pairs()
    rows = []
    for name, obs in scenarios.items():
        rows.append({"case": name, "classification": classify_formula(obs),
                     "oracle": classify_oracle(obs)})
    v01_a = Case("member_loss_c_missing", -2, 6, None)
    v01_b = Case("exit_c_missing", 4, 4, None, member_a_exit=False)
    old = {"member_loss_c_missing": constrained_admissibility(v01_a)[0],
           "exit_c_missing": constrained_admissibility(v01_b)[0]}
    assert old == {"member_loss_c_missing": "UNRESOLVED",
                   "exit_c_missing": "UNRESOLVED"}

    count = 0
    counterexamples = []
    intervals = list(itertools.combinations_with_replacement(C_VALUES, 2))
    for a, b, bounds, consent, resource, floor, budget, exit_a, exit_b, scope in itertools.product(
        VALUES, VALUES, intervals, CONSENTS, (0, 5, 8), (0, 5), (0, 2),
        (False, True), (False, True), SCOPES
    ):
        o = Observation(a, b, bounds, consent, resource, floor, exit_a, exit_b, budget, scope)
        actual = classify_formula(o)
        oracle = classify_oracle(o)
        if actual != oracle:
            counterexamples.append({"observation": str(o), "formula": actual, "oracle": oracle})
        swapped = replace(o, a=o.b, b=o.a, a_exit=o.b_exit, b_exit=o.a_exit)
        assert classify_formula(swapped) == actual
        count += 1
    assert not counterexamples, counterexamples[:3]
    assert count == 108864, count
    assert classify_formula(replace(example_pairs()["closed_world_illustration_only"], affected_scope_complete=None)) == "UNRESOLVED"
    assert classify_formula(example_pairs()["unknown_C_bounded_nonnegative"]) == "ADMISSIBLE"
    assert classify_formula(example_pairs()["known_unavoidable_C_loss"]) == "BLOCKED"
    assert classify_formula(example_pairs()["known_member_loss_hidden_by_missing_C"]) == "BLOCKED"
    assert classify_formula(example_pairs()["known_exit_block_hidden_by_missing_C"]) == "BLOCKED"
    # The old three-actor observation cannot distinguish a possible unregistered
    # D with +5 from a possible D with -50; neither is an observed fact.
    return {
        "schema": "pi-coalition-partial-identification/v0.2",
        "class": "PROJECT_SELF_RUN_SYNTHETIC_FORMAL_ENUMERATION",
        "old_v01_masking_observations": old,
        "legacy_v01_reassessment_open_scope": reassess_legacy_cases(),
        "unregistered_actor_witness": unregistered_actor_witness(),
        "focused_cases": rows,
        "finite_states_tested": count,
        "formula_oracle_disagreements": len(counterexamples),
        "member_identity_swap_disagreements": 0,
        "new_explicit_assumption": "affected_scope_complete is a DECLARED toy input, NOT real discovery or proof of affected-party coverage",
        "missing_unbounded_C": "UNRESOLVED unless independently known member failure",
        "real_world_applicability": "UNTESTED",
    }


if __name__ == "__main__":
    print(json.dumps(run_audit(), indent=2, ensure_ascii=False, sort_keys=True))

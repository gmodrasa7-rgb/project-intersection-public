#!/usr/bin/env python3
"""PEST v0.1: falsifiable, explicitly synthetic design skeleton. No research results."""
from dataclasses import dataclass, replace
from itertools import product
import argparse

WORLDS = ("survival_fear", "capture_opportunity", "backlash")
BRANCHES = {
    "R1_BOTH_PROTECTED": (1, 1),
    "R2_NEITHER_PROTECTED": (0, 0),
    "R3_TARGET_ONLY": (1, 0),
    "R4_SUPPRESSOR_ONLY": (0, 1),
}  # tuple order: (XG_i, XG_j)
PT_LEVELS = (0.25, 0.75)
DELTA = 0.03  # synthetic normalized payoff-margin units, NOT a population effect size


@dataclass(frozen=True)
class Case:
    world: str
    suppressor: str  # "A" or "B"; swapping labels must not change outcomes
    PT_i: float       # target power transferable to others
    PT_j: float       # suppressor power transferable to others
    XG_i: int         # target existence physically guaranteed if 1
    XG_j: int         # suppressor existence physically guaranteed if 1
    future_threat: float = 0.85
    target_growth: float = 0.65
    perceived_enforcement: float = 0.90
    floor_after: float = 0.70
    exit_after: float = 0.70


def _unit(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and 0 <= x <= 1


def validate_case(c: Case):
    if c.world not in WORLDS or c.suppressor not in ("A", "B"):
        raise ValueError("unknown world or role label")
    if any(type(x) is not int or x not in (0, 1) for x in (c.XG_i, c.XG_j)):
        raise ValueError("XG assignments must be exact binary ideal guarantees")
    for field in ("PT_i", "PT_j", "future_threat", "target_growth",
                  "perceived_enforcement", "floor_after", "exit_after"):
        if not _unit(getattr(c, field)):
            raise ValueError(f"{field} outside [0,1] or missing")
    return True


def floor_exit_gate(c: Case, minimum_floor=0.50, minimum_exit=0.50):
    """Necessary condition only; never infer mutual acceptability from one action."""
    validate_case(c)
    if not _unit(minimum_floor) or not _unit(minimum_exit):
        raise ValueError("invalid living floor / exit threshold")
    return ("FLOOR_EXIT_PASS" if c.floor_after >= minimum_floor
            and c.exit_after >= minimum_exit else "FLOOR_EXIT_FAIL")


def candidate_set_status(candidates, *, exhaustive=False, minimum_floor=0.50,
                         minimum_exit=0.50):
    """Empty MAK is provable from these necessary gates only for an exhaustive action set.

    `exhaustive=True` is an unverified caller assertion, not a coverage receipt.
    Even if every supplied candidate fails, the empty-set conclusion is
    conditional on a genuinely complete choice set. Never return a definitive
    empty-set verdict based only on this flag.
    """
    cases = tuple(candidates)
    if not cases:
        raise ValueError("empty action inventory: coverage unknown")
    if type(exhaustive) is not bool:
        raise ValueError("exhaustive must be a boolean caller assertion")
    statuses = [floor_exit_gate(c, minimum_floor, minimum_exit) for c in cases]
    if "FLOOR_EXIT_PASS" in statuses:
        return "SURVIVORS_REQUIRE_FULL_MAK_REVIEW"
    if exhaustive:
        return "CONDITIONAL_EMPTY_IF_SCOPE_COMPLETE"
    return "UNRESOLVED_ACTION_COVERAGE"


def utility_margin(c: Case):
    """Mechanism-specific synthetic payoffs; only growth suppression, not legitimate defense.

    This is NOT observed behavior. The distinct worlds were chosen as adversarial
    positive/null/reversed-sign controls; they are not independently calibrated.
    """
    validate_case(c)
    u_cooperate = 0.22 + 0.23 * c.target_growth
    if c.world == "survival_fear":
        # J fears future retaliation; its own guarantee moderates that fear.
        u_suppress = (0.09 + 0.70 * c.future_threat * c.PT_j
                      * (1 - c.XG_j * c.perceived_enforcement) + 0.10 * c.PT_i)
    elif c.world == "capture_opportunity":
        # Target protection can shift competition toward nonlethal suppression.
        u_suppress = 0.09 + 0.70 * c.PT_i + 0.12 * c.XG_i
    else:
        # J's own protection can lower its perceived cost of suppressing I.
        u_suppress = 0.09 + 0.35 * c.PT_i + 0.32 * c.XG_j
    return u_suppress - u_cooperate


def psi_proxy(c: Case):
    """Non-negative synthetic suppress-vs-cooperate incentive margin, NOT frequency."""
    return max(0.0, utility_margin(c))


def elimination_possible(c: Case, victim: str):
    """Ideal guarantee prevents elimination of the protected role, not growth limits."""
    validate_case(c)
    if victim == "i":
        return c.XG_i == 0
    if victim == "j":
        return c.XG_j == 0
    raise ValueError("victim must be i or j")


def design():
    cases = []
    for world, pt_i, pt_j, suppressor in product(WORLDS, PT_LEVELS, PT_LEVELS, ("A", "B")):
        for xg_i, xg_j in BRANCHES.values():
            cases.append(Case(world, suppressor, pt_i, pt_j, xg_i, xg_j))
    return tuple(cases)


def validate_design(cases):
    keys = set()
    lookup = {}
    for c in cases:
        validate_case(c)
        key = (c.world, c.PT_i, c.PT_j, c.suppressor, c.XG_i, c.XG_j)
        if key in keys:
            raise ValueError("duplicate experimental cell")
        keys.add(key)
        lookup[key] = c
    expected = len(WORLDS) * len(PT_LEVELS) ** 2 * 2 * len(BRANCHES)
    if len(cases) != expected:
        raise ValueError(f"incomplete grid: {len(cases)}/{expected}")
    expected_keys = {
        (world, pi, pj, actor, xi, xj)
        for world, pi, pj, actor in product(WORLDS, PT_LEVELS, PT_LEVELS, ("A", "B"))
        for xi, xj in BRANCHES.values()
    }
    if keys != expected_keys:
        raise ValueError("grid coordinate drift: planned PT/XG cells changed or missing")
    for c in cases:
        opposite = "B" if c.suppressor == "A" else "A"
        reversed_case = lookup.get((c.world, c.PT_i, c.PT_j, opposite, c.XG_i, c.XG_j))
        if reversed_case is None:
            raise ValueError("missing actual A/B role reversal")
        for field in ("future_threat", "target_growth", "perceived_enforcement",
                      "floor_after", "exit_after"):
            if getattr(c, field) != getattr(reversed_case, field):
                raise ValueError("causal input drift across role reversal: " + field)
        if psi_proxy(c) != psi_proxy(reversed_case):
            raise ValueError("identity-dependent synthetic physics")
        if floor_exit_gate(c) != floor_exit_gate(reversed_case):
            raise ValueError("XG role-consistency failure")
        # R1-R4 are causal guarantee contrasts only if pre-treatment inputs
        # are equal within the same world, PT setting, and named actor.
        # Floor/exit after intervention may legitimately differ by XG.
        baseline = lookup.get((c.world, c.PT_i, c.PT_j, c.suppressor, 0, 0))
        if baseline is None:
            raise ValueError("missing paired unprotected guarantee cell")
        for field in ("future_threat", "target_growth", "perceived_enforcement"):
            if getattr(c, field) != getattr(baseline, field):
                raise ValueError("pretreatment input drift across XG: " + field)
    return expected


def actor_fixed_role_reversals(cases):
    """Report reciprocal roles while holding each named actor's PT and XG fixed.

    Base: A is suppressor j, B is target i. Reversed: B is suppressor,
    A is target, so relative PT and XG swap. No outcome invariance is assumed.
    """
    validate_design(cases)
    lookup = {(c.world, c.PT_i, c.PT_j, c.suppressor, c.XG_i, c.XG_j): c
              for c in cases}
    pairs = []
    for c in cases:
        if c.suppressor != "A":
            continue
        partner = lookup[(c.world, c.PT_j, c.PT_i, "B", c.XG_j, c.XG_i)]
        # Unlike role-label twins, actor-fixed comparisons swap PT/XG.
        # Their exogenous background must still be matched; post-treatment
        # floor/exit may vary and must not be forced equal.
        for field in ("future_threat", "target_growth", "perceived_enforcement"):
            if getattr(c, field) != getattr(partner, field):
                raise ValueError("actor-fixed reversal pretreatment drift: " + field)
        pairs.append((c, partner))
    return tuple(pairs)


def paired_contrasts(cases):
    """Diagnostic contrasts. Do not publish as preregistered experimental results."""
    validate_design(cases)  # never compute treatment contrasts on confounded pairs
    lookup = {(c.world, c.PT_i, c.PT_j, c.suppressor, c.XG_i, c.XG_j): c
              for c in cases}
    output = []
    for world, pi, pj, name in product(WORLDS, PT_LEVELS, PT_LEVELS, ("A", "B")):
        def psi(xi, xj):
            return psi_proxy(lookup[(world, pi, pj, name, xi, xj)])
        output.append({"world": world, "PT_i": pi, "PT_j": pj, "j": name,
                       # Keep all four necessary floor/exit screens visible alongside
                       # the incentive contrasts: a lower PSI is not an acceptable
                       # outcome when the protected arm breaches basic conditions.
                       "floor_exit_screens": {
                           branch: floor_exit_gate(lookup[(world, pi, pj, name, xi, xj)])
                           for branch, (xi, xj) in BRANCHES.items()
                       },
                       "baseline_psi": psi(0, 0),
                       "treated_psi": psi(1, 1),
                       "both_at_zero_floor": psi(0, 0) == 0 and psi(1, 1) == 0,
                       "raw_joint_margin_difference": (
                           utility_margin(lookup[(world, pi, pj, name, 1, 1)])
                           - utility_margin(lookup[(world, pi, pj, name, 0, 0)])),
                       "both_high_minus_both_low": psi(1, 1) - psi(0, 0),
                       "own_effect_at_target_low": psi(0, 1) - psi(0, 0),
                       "target_effect_at_own_low": psi(1, 0) - psi(0, 0),
                       "own_effect_at_target_high": psi(1, 1) - psi(1, 0),
                       "target_effect_at_own_high": psi(1, 1) - psi(0, 1),
                       "XG_ALONE_INEFFECTIVE": psi(1, 1) >= psi(0, 0) - DELTA})
    return output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true", help="no effect results")
    parser.add_argument("--execute", action="store_true", help="blocked pending frozen protocol")
    a = parser.parse_args()
    if a.execute:
        parser.error("HOLD: no preregistered execution until protocol and baseline commit frozen")
    if not a.validate_only:
        parser.error("specify --validate-only; no result-generation mode in candidate version")
    n = validate_design(design())
    print(f"PEST candidate design valid: {n} cells, 3 competing worlds, 4 XG assignments, "
          "2x2 PT levels, 2 identity reversals. NO SCIENTIFIC RESULT.")


if __name__ == "__main__":
    main()

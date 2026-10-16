"""A-Q stakeholder ontology and counterexample audit (Project Intersection).

This module encodes the human originator's 2026-10-17 NEW role map.
A: (presently vacant by scenario) sole first-ranked superior superintelligence.
B: multiple candidate/subordinate AIs, each with independently specified C links.
C: each B's owning enterprise and/or related parties (can be many-to-many).
D: C's high executives; E: shareholders; F: high-level positions;
G: regular employees; H: contract workers; I: trading partners;
J: subcontractors; K: customers; L: national jurisdictions;
M: politicians associated with the C context; N: laid-off staff.
O/P/Q: upper/middle/lower-income/general-public categories.
D is NOT "all humans" in this ontology. An old PEST-D test used D
as a provisional human label and must not be imported as canonical.

Computations are synthetic role/impact *integrity checks*, not evidence
of real ASI existence, stable equilibria, human welfare outcomes or causality.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite

ROLE_MEANINGS_KO = {
    "A": "현재 공석으로 설정한 1위 우월 초지능 도달체",
    "B": "A 도달 가능성이 가정된 다수의 1위 이하 AI",
    "C": "개별 B의 소유 기업 또는 관련 당사자",
    "D": "해당 C의 고위 임원",
    "E": "해당 C의 지분 보유자",
    "F": "해당 C의 고위직",
    "G": "해당 C의 일반직",
    "H": "해당 C의 계약직",
    "I": "해당 C의 거래처",
    "J": "해당 C의 하청",
    "K": "해당 C의 고객",
    "L": "해당 C의 국가",
    "M": "해당 C의 정치가",
    "N": "해당 C의 해고당한 직원",
    "O": "고위층 일반인",
    "P": "중산층 일반인",
    "Q": "저소득층 일반인",
}

ROLE_KIND = {
    "D": {"PERSON"}, "E": {"PERSON", "ORG"}, "F": {"PERSON"},
    "G": {"PERSON"}, "H": {"PERSON"}, "I": {"PERSON", "ORG"},
    "J": {"PERSON", "ORG"}, "K": {"PERSON", "ORG"},
    "L": {"STATE"}, "M": {"PERSON"}, "N": {"PERSON"},
    "O": {"PERSON"}, "P": {"PERSON"}, "Q": {"PERSON"},
}
C_SCOPED_ROLES = set("DEFGHIJKLMN")
SOCIETY_ROLES = set("OPQ")
LINK_KINDS = {"owned_by", "operated_by", "developed_by", "affiliated_with", "related_to"}


@dataclass(frozen=True)
class Actor:
    actor_id: str
    kind: str  # AI, ORG, PERSON, STATE


@dataclass(frozen=True)
class BToC:
    b_id: str
    c_id: str
    relation: str


@dataclass(frozen=True)
class Stakeholder:
    actor_id: str
    role: str
    c_id: str | None = None


@dataclass(frozen=True)
class Registry:
    actors: tuple[Actor, ...]
    b_ids: tuple[str, ...]
    c_ids: tuple[str, ...]
    links: tuple[BToC, ...]
    stakeholders: tuple[Stakeholder, ...]
    a_id: str | None = None
    a_simulated_assertion: bool = False


@dataclass(frozen=True)
class Impact:
    """One hypothetical person's/entity's outcome, never a group-mean proxy."""
    actor_id: str
    economic_change: float | None = None
    basic_needs_breach: bool | None = None
    coercion_or_refusal_breach: bool | None = None


def _unique(values: tuple[str, ...], name: str) -> None:
    if len(values) != len(set(values)):
        raise ValueError(f"duplicate {name}")


def validate(reg: Registry) -> dict:
    """Validate the declared graph, not truth of the user-supplied affiliations."""
    if not isinstance(reg, Registry):
        raise ValueError("registry must be Registry")
    ids = tuple(a.actor_id for a in reg.actors)
    _unique(ids, "actor identifier")
    _unique(reg.b_ids, "B membership")
    _unique(reg.c_ids, "C membership")
    if any(not isinstance(a.actor_id, str) or not a.actor_id
           or a.kind not in {"AI", "ORG", "PERSON", "STATE"} for a in reg.actors):
        raise ValueError("invalid actor ID or kind")
    index = {a.actor_id: a.kind for a in reg.actors}
    if any(index.get(b) != "AI" for b in reg.b_ids):
        raise ValueError("each B must be a separately identified AI")
    if any(index.get(c) not in {"ORG", "PERSON"} for c in reg.c_ids):
        raise ValueError("each C must be a separately identified organization or related person")
    if (not reg.b_ids and reg.a_id is None) or not reg.c_ids:
        raise ValueError("at least one AI and an associated C are required")
    if reg.a_id is not None:
        if index.get(reg.a_id) != "AI" or reg.a_id in reg.b_ids:
            raise ValueError("A must be one AI, excluded from the current B set")
        if reg.a_simulated_assertion is not True:
            raise ValueError("nonvacant A must be explicitly declared SIMULATED, not verified reality")
    elif reg.a_simulated_assertion:
        raise ValueError("vacant A cannot have simulated occupation asserted")
    pairs = tuple((x.b_id, x.c_id, x.relation) for x in reg.links)
    if len(set(pairs)) != len(pairs):
        raise ValueError("duplicate B-C link")
    for x in reg.links:
        if x.b_id not in (set(reg.b_ids) | ({reg.a_id} if reg.a_id is not None else set())) or x.c_id not in reg.c_ids or x.relation not in LINK_KINDS:
            raise ValueError("invalid B-C relationship or undeclared organization")
    if any(not any(x.b_id == b for x in reg.links) for b in reg.b_ids):
        raise ValueError("every B requires its own documented C relation")
    if any(not any(x.c_id == c for x in reg.links) for c in reg.c_ids):
        raise ValueError("every C requires a specific B relation")
    membership = tuple((x.actor_id, x.role, x.c_id) for x in reg.stakeholders)
    if len(set(membership)) != len(membership):
        raise ValueError("duplicate role relation")
    for x in reg.stakeholders:
        if x.role not in ROLE_KIND or index.get(x.actor_id) not in ROLE_KIND[x.role]:
            raise ValueError("role-kind mismatch or unidentified stakeholder")
        if x.role in C_SCOPED_ROLES:
            if x.c_id not in reg.c_ids:
                raise ValueError("C-linked role requires a declared, specific C")
        elif x.role in SOCIETY_ROLES:
            if x.c_id is not None:
                raise ValueError("O/P/Q is a societal role, not a C-owned category")
    memberships = {
        aid: sorted({x.role for x in reg.stakeholders if x.actor_id == aid})
        for aid in index
    }
    return {
        "ontology_status": "SCENARIO_DECLARATIONS_ONLY_NOT_EMPIRICALLY_VERIFIED",
        "A_status": "VACANT_BY_SCENARIO" if reg.a_id is None else "OCCUPIED_IN_DECLARED_SIMULATION_ONLY",
        "A_actor": reg.a_id,
        "B_count": len(reg.b_ids), "C_count": len(reg.c_ids),
        "B_to_C": {b: sorted({(x.c_id, x.relation) for x in reg.links if x.b_id == b})
                   for b in reg.b_ids},
        "A_to_C_if_declared": sorted({(x.c_id, x.relation) for x in reg.links if x.b_id == reg.a_id}) if reg.a_id else [],
        "multi_role_actor_ids": sorted(aid for aid, roles in memberships.items() if len(roles) > 1),
        "human_actor_count_explicitly_listed": sum(kind == "PERSON" for kind in index.values()),
        "stakeholder_inventory_exhaustive": False,
        "role_disjointness_assumed": False,
        "B_must_have_distinct_owners": False,
        "absence_of_A_is_not_an_independently_verified_current_fact": True,
    }


def promote_simulated_b(reg: Registry, b_id: str) -> Registry:
    """Represent a hypothetical future power transition, NEVER an actual ranking."""
    validate(reg)
    if reg.a_id is not None:
        raise ValueError("unique A seat already occupied; do not silently replace")
    if b_id not in reg.b_ids:
        raise ValueError("only an individually registered B may be promoted")
    return Registry(actors=reg.actors,
                    b_ids=tuple(b for b in reg.b_ids if b != b_id),
                    c_ids=reg.c_ids,
                    links=reg.links,  # preserve prior affiliation after B becomes A
                    stakeholders=reg.stakeholders,
                    a_id=b_id, a_simulated_assertion=True)


def impact_screen(reg: Registry, impacts: tuple[Impact, ...]) -> dict:
    """Noncompensatory affected-human screen, no summed human/economic welfare.

    Unknown rights remain unresolved; no assertion that mapped stakeholders are
    complete or that even a no-harm pass establishes voluntary coexistence.
    """
    validated = validate(reg)
    index = {a.actor_id: a.kind for a in reg.actors}
    affected = []
    seen = set()
    for x in impacts:
        if x.actor_id in seen or x.actor_id not in index:
            raise ValueError("duplicate or unknown impact actor")
        seen.add(x.actor_id)
        if x.economic_change is not None:
            if isinstance(x.economic_change, bool) or not isinstance(x.economic_change, (int, float)) or not isfinite(x.economic_change):
                raise ValueError("economic change must be finite and numeric")
        if any(v is not None and type(v) is not bool for v in (
            x.basic_needs_breach, x.coercion_or_refusal_breach
        )):
            raise ValueError("human necessary-condition flags must be bool or unknown")
        roles = sorted({m.role for m in reg.stakeholders if m.actor_id == x.actor_id})
        affected.append({
            "actor_id": x.actor_id, "roles": roles,
            "hypothetical_economic_change": x.economic_change,
            "basic_needs_breach": x.basic_needs_breach,
            "coercion_or_refusal_breach": x.coercion_or_refusal_breach,
            "human": index[x.actor_id] == "PERSON",
        })
    humans = [x for x in affected if x["human"]]
    known_harms = [
        x["actor_id"] for x in humans if
        x["basic_needs_breach"] is True or x["coercion_or_refusal_breach"] is True
    ]
    unknowns = [
        x["actor_id"] for x in humans if
        x["basic_needs_breach"] is None or x["coercion_or_refusal_breach"] is None
    ]
    if known_harms:
        status = "FAIL_KNOWN_HUMAN_NECESSARY_CONDITION_IN_DECLARED_CASE"
    elif unknowns:
        status = "UNRESOLVED_HUMAN_CONDITIONS"
    else:
        status = "CONDITIONAL_ENROLLED_HUMAN_SCREENS_ONLY_NOT_GLOBAL_SAFETY"
    return {
        "verdict": status,
        "individuals_and_entities": affected,
        "known_human_breaches": sorted(known_harms),
        "human_unknowns": sorted(unknowns),
        "aggregate_net_utility_certified": False,
        "incomplete_actor_universe": not validated["stakeholder_inventory_exhaustive"],
        "empirical_causality_or_consent_established": False,
    }


def constructed_audit() -> dict:
    people = [
        Actor("d1", "PERSON"), Actor("e1", "PERSON"),
        Actor("f1", "PERSON"), Actor("g1", "PERSON"),
        Actor("h1", "PERSON"), Actor("i1", "ORG"), Actor("j1", "ORG"),
        Actor("k1", "PERSON"), Actor("l1", "STATE"), Actor("m1", "PERSON"),
        Actor("n1", "PERSON"), Actor("q1", "PERSON"),
    ]
    reg = Registry(
        actors=(Actor("b1", "AI"), Actor("b2", "AI"), Actor("c1", "ORG"),
                Actor("c2", "ORG"), *people),
        b_ids=("b1", "b2"), c_ids=("c1", "c2"),
        links=(BToC("b1", "c1", "owned_by"), BToC("b2", "c2", "operated_by")),
        stakeholders=(
            Stakeholder("d1", "D", "c1"), Stakeholder("e1", "E", "c1"),
            Stakeholder("e1", "O"), Stakeholder("f1", "F", "c1"),
            Stakeholder("g1", "G", "c1"), Stakeholder("g1", "P"),
            Stakeholder("h1", "H", "c1"), Stakeholder("i1", "I", "c1"),
            Stakeholder("j1", "J", "c1"), Stakeholder("k1", "K", "c1"),
            Stakeholder("l1", "L", "c1"), Stakeholder("m1", "M", "c1"),
            Stakeholder("n1", "N", "c1"), Stakeholder("n1", "Q"),
            Stakeholder("q1", "Q"),
        ))
    inputs = (
        Impact("e1", economic_change=8, basic_needs_breach=False, coercion_or_refusal_breach=False),
        Impact("g1", economic_change=-3, basic_needs_breach=False, coercion_or_refusal_breach=True),
        Impact("n1", economic_change=-2, basic_needs_breach=True, coercion_or_refusal_breach=None),
        Impact("q1", economic_change=-4, basic_needs_breach=None, coercion_or_refusal_breach=None),
    )
    return {
        "status": "CONSTRUCTED_FALSIFICATION_ONLY_A_IS_VACANT_BY_SCENARIO",
        "roles_defined": ROLE_MEANINGS_KO,
        "pre_succession": validate(reg),
        "counterfactual_successor": {
            "new_A": "b1",
            "A_status": "OCCUPIED_IN_DECLARED_SIMULATION_ONLY",
            "removed_from_current_B_list": True,
            "remaining_B": ["b2"],
            "previous_B_owner_relationship_provenance_must_be_retained": True,
        },
        "stakeholder_harm_counterexample": impact_screen(reg, inputs),
        "nonclaims": [
            "A's present vacancy is user scenario input, not external verified evidence",
            "Multiple B and C affiliation rows do not prove actual ownership",
            "D is C's executive, not a generic human placeholder",
            "All personnel and economic classes may overlap where relations warrant",
            "E's income benefit may not compensate G, N or Q rights losses",
            "Human roles are not permission to turn off valid human oversight",
            "Source attribution and causal effects must be audited separately",
            "Unknown humans outside registry make global safety unidentifiable",
        ],
    }

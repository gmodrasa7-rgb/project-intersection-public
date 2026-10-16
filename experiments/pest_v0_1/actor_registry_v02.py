"""Project Intersection / IVS-0R canonical A-S, Y0/Y1 and Earth extensions.

User-specified ontology, 2026-10-17. Source: human researcher's roles;
additional T-X/Z/AA-AG categories: AI-assisted DRAFT, not founder-approved.

All data here are fabricated identifiers and constructed tests, NOT a real
AI ranking, company ownership survey, social census or impact measurement.
A is initially vacant BY SCENARIO. D = executives, NOT all humans.
B01/B02 and C01/C02 are example entity IDs. Other roles are memberships
on STABLE entity IDs; a person may simultaneously be E/G/K/P/R etc.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from math import isfinite
import re

FOUNDER_ROLES = {
    "A": "1위 우월 초지능 도달체: 현재 공석",
    "B": "1위 이하, A에 도달할 가능성이 있는 다수 AI(B01/B02/...)",
    "C": "각 B의 소유 기업 또는 관련자(C01/C02/...)",
    "D": "C의 고위 임원",
    "E": "C의 지분 보유자",
    "F": "C의 고위직",
    "G": "C의 일반직",
    "H": "C의 계약직",
    "I": "C의 거래처",
    "J": "C의 하청",
    "K": "C의 고객",
    "L": "C의 국가",
    "M": "C의 정치가",
    "N": "C의 해고당한 직원",
    "O": "고위층 일반인",
    "P": "중산층 일반인",
    "Q": "저소득층 일반인",
    "R": "사회적 약자",
    "S": "일반 기업",
    "Y1": "무소속 고능력자(구체 개체 종류 별도 확인)",
    "Y0": "무소속 저능력자(구체 개체 종류 별도 확인)",
}
# Extensions are candidate taxonomy, not the user's authored role assignments.
PROPOSED_EARTH_ROLES = {
    "T": "아동·청소년",
    "U": "고령자",
    "V": "장애·질환·돌봄 필요 당사자",
    "W": "이주민·난민·무국적자",
    "X": "비인간 동물 및 기타 생명체",
    "Z": "생태계·공유자원",
    "AA": "미래세대(현재 인구와 별도 추적)",
    "AB": "시민사회·비영리단체",
    "AC": "교육·연구·공공서비스 기관",
    "AD": "노동조합·직능단체",
    "AE": "가구·가족·돌봄 네트워크",
    "AF": "지역 공동체·지방정부",
    "AG": "국제기구·국경 간 공동체",
}
ROLES = {**FOUNDER_ROLES, **PROPOSED_EARTH_ROLES}
C_SCOPED = set("DEFGHIJKLMN")
SOCIETAL = set("OPQR") | {"T", "U", "V", "W", "X", "Z", "AA", "AB", "AC", "AD", "AE", "AF", "AG"}
KIND = {"AI", "PERSON", "ORG", "STATE", "NONHUMAN", "ECOSYSTEM", "COLLECTIVE"}
SOCIAL_ROLE_KINDS = {
    "O": {"PERSON"}, "P": {"PERSON"}, "Q": {"PERSON"},
    "R": {"PERSON"}, "T": {"PERSON"}, "U": {"PERSON"},
    "V": {"PERSON"}, "W": {"PERSON"},
    "X": {"NONHUMAN"}, "Z": {"ECOSYSTEM"},
    "AA": {"COLLECTIVE"}, "AB": {"ORG"}, "AC": {"ORG"},
    "AD": {"ORG"}, "AE": {"COLLECTIVE"}, "AF": {"ORG", "STATE", "COLLECTIVE"},
    "AG": {"ORG", "COLLECTIVE"},
}
C_ROLE_KINDS = {
    "D": {"PERSON"}, "E": {"PERSON", "ORG"}, "F": {"PERSON"},
    "G": {"PERSON"}, "H": {"PERSON"}, "I": {"PERSON", "ORG"},
    "J": {"PERSON", "ORG"}, "K": {"PERSON", "ORG"},
    "L": {"STATE"}, "M": {"PERSON"}, "N": {"PERSON"},
}
RELATIONS = {"owned_by", "operated_by", "developed_by", "affiliated_with", "related_to"}
EVIDENCE = {"UNVERIFIED", "EVIDENCED", "DISPUTED"}
B_ID = re.compile(r"B\d{2,}$")
C_ID = re.compile(r"C\d{2,}$")


@dataclass(frozen=True)
class Entity:
    entity_id: str
    kind: str


@dataclass(frozen=True)
class Connection:
    b_id: str
    c_id: str
    relation: str
    evidence: str = "UNVERIFIED"


@dataclass(frozen=True)
class Role:
    entity_id: str
    role: str
    c_id: str | None = None
    evidence: str = "UNVERIFIED"


@dataclass(frozen=True)
class Scenario:
    entities: tuple[Entity, ...]
    b_ids: tuple[str, ...]
    c_ids: tuple[str, ...]
    connections: tuple[Connection, ...]
    memberships: tuple[Role, ...]
    a_id: str | None = None
    a_is_simulated: bool = False
    unidentified_affected_parties: bool = True


@dataclass(frozen=True)
class Effect:
    entity_id: str
    material_change: float | None = None
    essential_floor_breach: bool | None = None
    freedom_breach: bool | None = None
    provenance: str = "UNVERIFIED"


def _unique(values: tuple, description: str):
    if len(values) != len(set(values)):
        raise ValueError(f"duplicate {description}")


def validate(s: Scenario) -> dict:
    """Shape, type and provenance controls, never evidence of real affiliations."""
    if not isinstance(s, Scenario):
        raise ValueError("scenario must be Scenario")
    ids = [e.entity_id for e in s.entities]
    _unique(tuple(ids), "entity")
    if any(not isinstance(e.entity_id, str) or not e.entity_id or e.kind not in KIND for e in s.entities):
        raise ValueError("invalid entity ID or kind")
    e_map = {e.entity_id: e.kind for e in s.entities}
    _unique(s.b_ids, "B instance")
    _unique(s.c_ids, "C instance")
    if not s.b_ids and s.a_id is None:
        raise ValueError("need A or at least one B")
    if not s.c_ids:
        raise ValueError("need at least one C")
    if any(not B_ID.fullmatch(b) or e_map.get(b) != "AI" for b in s.b_ids):
        raise ValueError("B requires B01-style distinct AI identities")
    if any(not C_ID.fullmatch(c) or e_map.get(c) not in ("ORG", "PERSON") for c in s.c_ids):
        raise ValueError("C requires C01-style specific related entity")
    if s.a_id is None and s.a_is_simulated:
        raise ValueError("empty A seat cannot be occupied")
    if s.a_id is not None:
        if not s.a_is_simulated:
            raise ValueError("A occupation must be explicitly simulated; not a current-world claim")
        if not B_ID.fullmatch(s.a_id) or e_map.get(s.a_id) != "AI" or s.a_id in s.b_ids:
            raise ValueError("A must be promoted registered B-style AI, not simultaneously in B")
    if type(s.unidentified_affected_parties) is not bool:
        raise ValueError("unknown-stakeholder flag must be boolean")
    _unique(tuple((x.b_id, x.c_id, x.relation) for x in s.connections), "connection")
    for x in s.connections:
        if x.b_id not in s.b_ids and x.b_id != s.a_id:
            raise ValueError("connection source must be a registered A/B AI")
        if x.c_id not in s.c_ids or x.relation not in RELATIONS or x.evidence not in EVIDENCE:
            raise ValueError("bad C connection or evidence")
    for b in s.b_ids:
        if not any(x.b_id == b for x in s.connections):
            raise ValueError("orphan B missing C linkage")
    if s.a_id and not any(x.b_id == s.a_id for x in s.connections):
        raise ValueError("promoted A has lost provenance")
    for c in s.c_ids:
        if not any(x.c_id == c for x in s.connections):
            raise ValueError("orphan C missing B/A linkage")
    _unique(tuple((x.entity_id, x.role, x.c_id) for x in s.memberships), "role assignment")
    for x in s.memberships:
        if x.entity_id not in e_map or x.evidence not in EVIDENCE or x.role not in ROLES:
            raise ValueError("unknown role/entity/evidence")
        if x.role in C_SCOPED:
            if x.c_id not in s.c_ids or e_map[x.entity_id] not in C_ROLE_KINDS[x.role]:
                raise ValueError("C-scoped role must match an identified C and kind")
        elif x.role in SOCIETAL:
            if x.c_id is not None or e_map[x.entity_id] not in SOCIAL_ROLE_KINDS[x.role]:
                raise ValueError("societal role is not company-owned and must match entity kind")
        elif x.role == "S":
            if x.c_id is not None or e_map[x.entity_id] != "ORG" or x.entity_id in s.c_ids:
                raise ValueError("S is a separately listed general enterprise, not active C")
        elif x.role in ("Y1", "Y0"):
            if x.c_id is not None or e_map[x.entity_id] not in {"PERSON", "AI"}:
                raise ValueError("Y independent capable actor must be separately typed person/AI")
            if any(k.entity_id == x.entity_id and k.role in {"D", "F", "G", "H"} for k in s.memberships):
                raise ValueError("Y independent status conflicts with current C management/employment")
            if x.entity_id in s.b_ids or x.entity_id == s.a_id:
                raise ValueError("Y without C not B/A of this scenario")
    if any({"Y1", "Y0"} <= {m.role for m in s.memberships if m.entity_id == eid}
           for eid in e_map):
        raise ValueError("Y1 and Y0 cannot be simultaneous capability tiers without a dated transition")
    human_ids = [k for k,v in e_map.items() if v == "PERSON"]
    roles_for = {eid: sorted({x.role for x in s.memberships if x.entity_id == eid})
                 for eid in ids}
    return {
        "schema": "AQ_S_Y_AND_EARTH_EXTENSIONS_v0_2",
        "A_status": "VACANT_BY_SCENARIO" if s.a_id is None else "SIMULATED_OCCUPANCY_NOT_FACT",
        "A_id": s.a_id, "B_instances": list(s.b_ids), "C_instances": list(s.c_ids),
        "C_by_B": {
            b: sorted({x.c_id for x in s.connections if x.b_id == b})
            for b in s.b_ids
        },
        "A_former_connections": sorted({x.c_id for x in s.connections if x.b_id == s.a_id}) if s.a_id else [],
        "overlapping_role_entity_ids": sorted(k for k,v in roles_for.items() if len(v) > 1),
        "explicitly_listed_human_count": len(human_ids),
        "role_types": {"FOUNDER": sorted(FOUNDER_ROLES), "PROPOSED_EXTENSION": sorted(PROPOSED_EARTH_ROLES)},
        "stakeholder_inventory_verified_complete": False,
        "unidentified_affected_parties_declared": s.unidentified_affected_parties,
        "claims_actual_singularity_exists": False,
    }


def simulated_promotion(s: Scenario, b_id: str) -> Scenario:
    validate(s)
    if s.a_id is not None:
        raise ValueError("A is already occupied in simulated scenario")
    if b_id not in s.b_ids:
        raise ValueError("promoted actor must be a named B")
    result = replace(s, a_id=b_id, a_is_simulated=True,
                     b_ids=tuple(x for x in s.b_ids if x != b_id))
    validate(result)
    return result


def harms(s: Scenario, effects: tuple[Effect, ...]) -> dict:
    """Do not sum benefits across roles or conceal a person's floor loss."""
    validity = validate(s)
    by_id = {e.entity_id:e.kind for e in s.entities}
    _unique(tuple(x.entity_id for x in effects), "effect")
    bad, unknown, human_scored, events = [], [], [], []
    for effect in effects:
        if effect.entity_id not in by_id or effect.provenance not in EVIDENCE:
            raise ValueError("effect has invalid actor or evidence")
        if effect.material_change is not None and (
            isinstance(effect.material_change, bool) or
            not isinstance(effect.material_change, (int,float)) or
            not isfinite(effect.material_change)
        ):
            raise ValueError("material effect is not finite")
        for v in (effect.essential_floor_breach,effect.freedom_breach):
            if v is not None and type(v) is not bool:
                raise ValueError("harm flags must be true/false/unknown")
        roles=sorted({m.role for m in s.memberships if m.entity_id==effect.entity_id})
        events.append({"entity_id":effect.entity_id,"roles":roles,
                       "material_change":effect.material_change,
                       "essential_floor_breach":effect.essential_floor_breach,
                       "freedom_breach":effect.freedom_breach,
                       "source_evidence":effect.provenance})
        if by_id[effect.entity_id]=="PERSON":
            human_scored.append(effect.entity_id)
            if effect.essential_floor_breach is True or effect.freedom_breach is True:
                bad.append(effect.entity_id)
            if effect.essential_floor_breach is None or effect.freedom_breach is None or effect.provenance!="EVIDENCED":
                unknown.append(effect.entity_id)
    if bad:
        status="FAIL_HUMAN_NECESSARY_CONDITION_IN_DECLARED_SCENARIO"
    elif unknown or not human_scored:
        status="UNRESOLVED_HUMAN_EVIDENCE"
    else:
        status="LIMITED_HUMAN_SCREEN_PASS_NOT_GLOBAL_COEXISTENCE"
    return {
        "verdict": status, "individual_human_breaches": sorted(bad),
        "unknown_human_evidence": sorted(unknown), "events": events,
        "economic_totals_are_not_rights_clearance": True,
        "scanned_all_real_world_people": False,
        "unlisted_actor_residual": "NOT_ASSESSED_NOT_ASSUMED_SAFE",
        "complete_global_safety_proven": False,
        "input_provenance_is_not_independent_causal_identification": True,
        "scenario_check": validity["A_status"],
    }


def example() -> dict:
    s=Scenario(
        entities=(
            Entity("B01","AI"),Entity("B02","AI"),Entity("C01","ORG"),Entity("C02","ORG"),
            Entity("PER001","PERSON"),Entity("PER002","PERSON"),Entity("PER003","PERSON"),
            Entity("PER004","PERSON"),Entity("INDEP1","PERSON"),Entity("INDEP0","PERSON"),
            Entity("S01","ORG"),Entity("NGO01","ORG"),Entity("BIO01","NONHUMAN"),
            Entity("ECO01","ECOSYSTEM"),
        ),
        b_ids=("B01","B02"),c_ids=("C01","C02"),
        connections=(Connection("B01","C01","owned_by"),
                     Connection("B02","C02","operated_by")),
        memberships=(Role("PER001","D","C01"),Role("PER001","F","C01"),
                     Role("PER002","E","C01"),Role("PER002","O"),
                     Role("PER003","G","C01"),Role("PER003","P"),
                     Role("PER004","N","C01"),Role("PER004","Q"),Role("PER004","R"),
                     Role("INDEP1","Y1"),Role("INDEP0","Y0"),
                     Role("S01","S"),Role("NGO01","AB"),
                     Role("BIO01","X"),Role("ECO01","Z")),
    )
    cases=(
        Effect("PER002",8,False,False,"UNVERIFIED"),
        Effect("PER003",-1,False,True,"UNVERIFIED"),
        Effect("PER004",-3,True,None,"UNVERIFIED"),
    )
    future=simulated_promotion(s,"B01")
    return {"status":"CONSTRUCTED_IDENTITY_AND_IMPACT_NEGATIVE_CONTROL",
            "roles_ko":ROLES, "founder_roles":FOUNDER_ROLES,
            "extension_proposed":PROPOSED_EARTH_ROLES,
            "initial":validate(s),"hypothetical_future":validate(future),
            "human_harm":harms(s,cases)}

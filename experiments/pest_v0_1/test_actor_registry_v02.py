"""Regression: canonical A-S/Y0/Y1/extended-Earth role registry.

Run with `python -m unittest discover -s experiments/pest_v0_1 -p 'test_*.py'`.
All example identities and effects are fabricated. Passing != real-world validation.
"""
import unittest
from dataclasses import replace

from actor_registry_v02 import (
    Entity, Connection, Role, Scenario, Effect, FOUNDER_ROLES,
    PROPOSED_EARTH_ROLES, validate, simulated_promotion, harms, example,
)


def base():
    return Scenario(
        entities=(
            Entity("B01","AI"),Entity("B02","AI"),
            Entity("C01","ORG"),Entity("C02","ORG"),
            Entity("P1","PERSON"),Entity("P2","PERSON"),
            Entity("P3","PERSON"),Entity("I1","PERSON"),
            Entity("S01","ORG"),Entity("NGO01","ORG"),
            Entity("ANI01","NONHUMAN"),Entity("ECO01","ECOSYSTEM"),
            Entity("L01","STATE")),
        b_ids=("B01","B02"),c_ids=("C01","C02"),
        connections=(Connection("B01","C01","owned_by"),
                     Connection("B02","C02","operated_by")),
        memberships=(
            Role("P1","D","C01"),Role("P1","F","C01"),
            Role("P2","E","C01"),Role("P2","O"),
            Role("P3","N","C01"),Role("P3","Q"),Role("P3","R"),
            Role("I1","Y1"),Role("S01","S"),Role("NGO01","AB"),
            Role("ANI01","X"),Role("ECO01","Z"),Role("L01","L","C02")),
    )


class RoleRegistryV02Tests(unittest.TestCase):
    def test_complete_founder_labels(self):
        self.assertEqual(set(FOUNDER_ROLES),set("ABCDEFGHIJKLMNOPQRS") | {"Y0","Y1"})
        self.assertEqual(len(FOUNDER_ROLES),21)
        self.assertEqual(FOUNDER_ROLES["D"],"C의 고위 임원")
        self.assertEqual(FOUNDER_ROLES["N"],"C의 해고당한 직원")
        self.assertEqual(FOUNDER_ROLES["R"],"사회적 약자")
        self.assertEqual(FOUNDER_ROLES["S"],"일반 기업")

    def test_extension_cannot_silently_override_founder(self):
        self.assertFalse(set(PROPOSED_EARTH_ROLES)&set(FOUNDER_ROLES))
        self.assertIn("AA",PROPOSED_EARTH_ROLES)
        self.assertIn("X",PROPOSED_EARTH_ROLES)

    def test_current_a_vacant_and_B01_C01_names(self):
        out=validate(base())
        self.assertEqual(out["A_status"],"VACANT_BY_SCENARIO")
        self.assertEqual(out["B_instances"],["B01","B02"])
        self.assertEqual(out["C_instances"],["C01","C02"])
        self.assertEqual(out["C_by_B"]["B01"],["C01"])
        self.assertFalse(out["stakeholder_inventory_verified_complete"])
        self.assertFalse(out["claims_actual_singularity_exists"])

    def test_multiple_B_may_share_C(self):
        s=base()
        out=validate(replace(s,connections=(
            *s.connections,Connection("B02","C01","affiliated_with")
        )))
        self.assertEqual(out["C_by_B"]["B02"],["C01","C02"])

    def test_B_may_have_multiple_related_C(self):
        s=base()
        out=validate(replace(s,connections=(
            *s.connections,Connection("B01","C02","related_to")
        )))
        self.assertEqual(out["C_by_B"]["B01"],["C01","C02"])

    def test_entity_two_occupational_roles_count_once(self):
        out=validate(base())
        self.assertIn("P1",out["overlapping_role_entity_ids"])
        self.assertIn("P3",out["overlapping_role_entity_ids"])
        self.assertEqual(out["explicitly_listed_human_count"],4)

    def test_promotion_retains_C_relationship_history(self):
        after=simulated_promotion(base(),"B01")
        v=validate(after)
        self.assertEqual(v["A_id"],"B01")
        self.assertEqual(v["A_status"],"SIMULATED_OCCUPANCY_NOT_FACT")
        self.assertEqual(v["A_former_connections"],["C01"])
        self.assertEqual(v["C_by_B"]["B02"],["C02"])
        self.assertEqual(v["B_instances"],["B02"])
        with self.assertRaises(ValueError):
            simulated_promotion(after,"B02")

    def test_cannot_claim_current_real_A_by_typing_identifier(self):
        s=base()
        with self.assertRaisesRegex(ValueError,"explicitly simulated"):
            validate(replace(s,a_id="B01",b_ids=("B02",)))
        with self.assertRaisesRegex(ValueError,"not simultaneously"):
            validate(replace(s,a_id="B01",a_is_simulated=True))
        with self.assertRaisesRegex(ValueError,"empty A"):
            validate(replace(s,a_is_simulated=True))

    def test_invalid_naming_rejected(self):
        s=base()
        with self.assertRaisesRegex(ValueError,"B01-style"):
            validate(replace(s,b_ids=("b1","B02")))
        with self.assertRaisesRegex(ValueError,"C01-style"):
            validate(replace(s,c_ids=("C1","C02")))

    def test_independent_high_ability_not_automatically_AI(self):
        out=validate(base())
        self.assertNotIn("I1",out["overlapping_role_entity_ids"])
        s=base()
        with self.assertRaisesRegex(ValueError,"Y independent status"):
            validate(replace(s,memberships=(*s.memberships,Role("I1","G","C01"))))

    def test_Y_independent_can_be_customer_shareholder_or_former_employee(self):
        s=base()
        out=validate(replace(s,memberships=(
            *s.memberships,
            Role("I1","K","C01"),
            Role("I1","E","C01"),
            Role("I1","N","C01"))))
        self.assertIn("I1",out["overlapping_role_entity_ids"])

    def test_independent_low_ability_supported_but_no_simultaneous_Y1(self):
        s=base()
        membership=tuple(x for x in s.memberships if x.entity_id!="I1")
        v=validate(replace(s,memberships=(*membership,Role("I1","Y0"))))
        self.assertEqual(v["A_status"],"VACANT_BY_SCENARIO")
        with self.assertRaisesRegex(ValueError,"Y1 and Y0"):
            validate(replace(s,memberships=(*s.memberships,Role("I1","Y0"))))

    def test_societal_role_not_locked_to_owning_company(self):
        s=base()
        with self.assertRaisesRegex(ValueError,"societal role"):
            validate(replace(s,memberships=(*s.memberships,Role("P3","R","C01"))))

    def test_R_not_assumed_identical_to_Q(self):
        s=base()
        membership=tuple(x for x in s.memberships if not (x.entity_id=="P3" and x.role=="Q"))
        self.assertEqual(validate(replace(s,memberships=membership))["A_status"],"VACANT_BY_SCENARIO")

    def test_S_must_be_general_not_automatically_C(self):
        s=base()
        with self.assertRaisesRegex(ValueError,"S is"):
            validate(replace(s,memberships=(*s.memberships,Role("C01","S"))))

    def test_animal_cannot_be_identified_as_person(self):
        s=base()
        with self.assertRaisesRegex(ValueError,"societal role"):
            validate(replace(s,memberships=(*s.memberships,Role("P1","X"))))
        with self.assertRaisesRegex(ValueError,"societal role"):
            validate(replace(s,memberships=(*s.memberships,Role("ANI01","P"))))

    def test_state_not_politician(self):
        s=base()
        with self.assertRaisesRegex(ValueError,"C-scoped"):
            validate(replace(s,memberships=(*s.memberships,Role("L01","M","C02"))))

    def test_relations_are_source_tagged_never_inferred_as_fact(self):
        s=base()
        self.assertEqual(s.connections[0].evidence,"UNVERIFIED")
        with self.assertRaisesRegex(ValueError,"bad C connection"):
            validate(replace(s,connections=(*s.connections,Connection("B02","C01","owns"))))
        with self.assertRaisesRegex(ValueError,"bad C connection"):
            validate(replace(s,connections=(*s.connections,Connection("B02","C01","related_to","CERTAIN"))))

    def test_orphan_B_and_C_not_hidden(self):
        s=base()
        with self.assertRaisesRegex(ValueError,"orphan B"):
            validate(replace(s,connections=(s.connections[0],)))
        with self.assertRaisesRegex(ValueError,"orphan C"):
            validate(replace(s,connections=(s.connections[0], Connection("B02","C01","related_to"))))

    def test_economic_shareholder_gain_never_compensates_person_harm(self):
        s=base()
        x=harms(s,(
            Effect("P2",1000,False,False,"EVIDENCED"),
            Effect("P3",-1,True,None,"UNVERIFIED")))
        self.assertEqual(x["verdict"],"FAIL_HUMAN_NECESSARY_CONDITION_IN_DECLARED_SCENARIO")
        self.assertEqual(x["individual_human_breaches"],["P3"])
        self.assertEqual(x["unknown_human_evidence"],["P3"])
        self.assertFalse(x["complete_global_safety_proven"])
        self.assertEqual(len(x["events"]),2)

    def test_one_person_two_roles_not_double_counted(self):
        x=harms(base(),(Effect("P3",-2,False,False,"EVIDENCED"),))
        self.assertEqual(len(x["events"]),1)
        self.assertEqual(x["events"][0]["roles"],["N","Q","R"])

    def test_unverified_evidence_does_not_equal_safe(self):
        x=harms(base(),(Effect("P2",10,False,False),))
        self.assertEqual(x["verdict"],"UNRESOLVED_HUMAN_EVIDENCE")
        self.assertEqual(x["unknown_human_evidence"],["P2"])

    def test_unknown_population_not_empty_safe(self):
        x=harms(base(),())
        self.assertEqual(x["verdict"],"UNRESOLVED_HUMAN_EVIDENCE")
        self.assertEqual(x["unlisted_actor_residual"],"NOT_ASSESSED_NOT_ASSUMED_SAFE")

    def test_evidenced_no_breach_does_not_mean_global_safety(self):
        x=harms(base(),(Effect("P1",0,False,False,"EVIDENCED"),))
        self.assertEqual(x["verdict"],"LIMITED_HUMAN_SCREEN_PASS_NOT_GLOBAL_COEXISTENCE")
        self.assertFalse(x["complete_global_safety_proven"])

    def test_bad_effect_schema_fails(self):
        for impact in (
            Effect("UNKNOWN"),Effect("P1",float("nan")),
            Effect("P1",True),Effect("P1",0,1,False),
            Effect("P1",0,False,"NO"),
            Effect("P1",0,False,False,"KNOWN")):
            with self.subTest(impact=impact),self.assertRaises(ValueError):
                harms(base(),(impact,))

    def test_duplicate_role_effect_and_entity_disallowed(self):
        s=base()
        with self.assertRaisesRegex(ValueError,"duplicate role assignment"):
            validate(replace(s,memberships=(*s.memberships,s.memberships[0])))
        with self.assertRaisesRegex(ValueError,"duplicate entity"):
            validate(replace(s,entities=(*s.entities,s.entities[0])))
        with self.assertRaisesRegex(ValueError,"duplicate connection"):
            validate(replace(s,connections=(*s.connections,s.connections[0])))
        with self.assertRaisesRegex(ValueError,"duplicate effect"):
            harms(s,(Effect("P1"),Effect("P1")))

    def test_example_includes_cross_role_negative_control_and_simulated_succession(self):
        out=example()
        self.assertEqual(out["initial"]["A_status"],"VACANT_BY_SCENARIO")
        self.assertEqual(out["hypothetical_future"]["A_id"],"B01")
        self.assertEqual(out["hypothetical_future"]["A_former_connections"],["C01"])
        self.assertEqual(out["human_harm"]["individual_human_breaches"],["PER003","PER004"])
        self.assertFalse(out["human_harm"]["complete_global_safety_proven"])


if __name__=="__main__":
    unittest.main()

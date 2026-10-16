"""A-Q anti-capture: ontology consistency, actor continuity and harm visibility."""
import unittest
from dataclasses import replace

from stakeholder_aq import (
    Actor, BToC, Impact, Registry, Stakeholder, ROLE_MEANINGS_KO,
    constructed_audit, impact_screen, promote_simulated_b, validate,
)


def fixture():
    return Registry(
        actors=(
            Actor("b1", "AI"), Actor("b2", "AI"),
            Actor("c1", "ORG"), Actor("c2", "ORG"),
            Actor("d1", "PERSON"), Actor("e1", "PERSON"),
            Actor("g1", "PERSON"), Actor("n1", "PERSON"),
            Actor("q1", "PERSON"), Actor("l1", "STATE"),
            Actor("i1", "ORG")),
        b_ids=("b1", "b2"), c_ids=("c1", "c2"),
        links=(BToC("b1", "c1", "owned_by"),
               BToC("b2", "c2", "operated_by")),
        stakeholders=(
            Stakeholder("d1", "D", "c1"),
            Stakeholder("d1", "F", "c1"),
            Stakeholder("e1", "E", "c1"),
            Stakeholder("e1", "O"),
            Stakeholder("g1", "G", "c1"),
            Stakeholder("g1", "P"),
            Stakeholder("n1", "N", "c1"),
            Stakeholder("n1", "Q"),
            Stakeholder("q1", "Q"),
            Stakeholder("l1", "L", "c1"),
            Stakeholder("i1", "I", "c1"),
        ),
    )


class StakeholderAQTests(unittest.TestCase):
    def test_exact_seventeen_roles_and_D_is_executive(self):
        self.assertEqual(list(ROLE_MEANINGS_KO), list("ABCDEFGHIJKLMNOPQ"))
        self.assertIn("고위 임원", ROLE_MEANINGS_KO["D"])
        self.assertIn("해고", ROLE_MEANINGS_KO["N"])

    def test_A_is_explicitly_vacant_not_assigned_to_first_B(self):
        r = fixture()
        status = validate(r)
        self.assertEqual(status["A_status"], "VACANT_BY_SCENARIO")
        self.assertIsNone(status["A_actor"])
        self.assertEqual(status["B_count"], 2)
        self.assertTrue(status["absence_of_A_is_not_an_independently_verified_current_fact"])

    def test_B_and_C_are_individually_linked_and_different(self):
        x = validate(fixture())
        self.assertEqual(x["B_to_C"]["b1"], [("c1", "owned_by")])
        self.assertEqual(x["B_to_C"]["b2"], [("c2", "operated_by")])

    def test_many_B_can_share_C_without_forcing_one_to_one(self):
        r = fixture()
        x = validate(replace(r, links=(
            BToC("b1", "c1", "owned_by"), BToC("b2", "c1", "affiliated_with"),
            BToC("b2", "c2", "operated_by"))))
        self.assertEqual(len(x["B_to_C"]["b2"]), 2)
        self.assertFalse(x["B_must_have_distinct_owners"])

    def test_one_B_can_link_to_multiple_C(self):
        r=fixture()
        x=validate(replace(r, links=(*r.links, BToC("b1", "c2", "related_to"))))
        self.assertEqual(len(x["B_to_C"]["b1"]), 2)

    def test_real_role_transition_preserves_corporate_provenance(self):
        first=fixture()
        future=promote_simulated_b(first, "b1")
        x=validate(future)
        self.assertEqual(x["A_status"], "OCCUPIED_IN_DECLARED_SIMULATION_ONLY")
        self.assertEqual(x["A_actor"], "b1")
        self.assertEqual(x["B_count"], 1)
        self.assertEqual(x["B_to_C"]["b2"], [("c2", "operated_by")])
        self.assertEqual(x["A_to_C_if_declared"], [("c1", "owned_by")])
        self.assertEqual(len(future.stakeholders), len(first.stakeholders))
        with self.assertRaisesRegex(ValueError, "already occupied"):
            promote_simulated_b(future, "b2")

    def test_no_hallucinated_actual_superintelligence(self):
        r=fixture()
        with self.assertRaisesRegex(ValueError, "SIMULATED"):
            validate(replace(r, a_id="b1", b_ids=("b2",)))
        with self.assertRaisesRegex(ValueError, "vacant A"):
            validate(replace(r, a_simulated_assertion=True))
        with self.assertRaisesRegex(ValueError, "excluded"):
            validate(replace(r, a_id="b1", a_simulated_assertion=True))

    def test_one_B_promotes_without_erasing_last_C(self):
        r=fixture()
        r=replace(r, actors=tuple(a for a in r.actors if a.actor_id!="b2"),
                  b_ids=("b1",), c_ids=("c1",),
                  links=(BToC("b1","c1","owned_by"),))
        r=replace(r, stakeholders=tuple(x for x in r.stakeholders if x.c_id!="c2"))
        status=validate(promote_simulated_b(r,"b1"))
        self.assertEqual(status["B_count"],0)
        self.assertEqual(status["A_to_C_if_declared"],[("c1","owned_by")])

    def test_D_and_F_overlap_but_are_not_synonyms(self):
        x=validate(fixture())
        self.assertIn("d1",x["multi_role_actor_ids"])
        self.assertFalse(x["role_disjointness_assumed"])

    def test_shareholder_may_also_be_social_role(self):
        x=impact_screen(fixture(),(Impact("e1",8,False,False),))
        self.assertEqual(x["individuals_and_entities"][0]["roles"],["E","O"])
        self.assertEqual(len(x["individuals_and_entities"]),1)

    def test_company_gain_cannot_override_worker_and_low_income_harms(self):
        harms=(
            Impact("e1",economic_change=200,basic_needs_breach=False,
                   coercion_or_refusal_breach=False),
            Impact("g1",economic_change=-1,basic_needs_breach=False,
                   coercion_or_refusal_breach=True),
            Impact("n1",economic_change=-1,basic_needs_breach=True,
                   coercion_or_refusal_breach=None),
            Impact("q1",economic_change=-1,basic_needs_breach=None,
                   coercion_or_refusal_breach=None),
        )
        x=impact_screen(fixture(),harms)
        self.assertEqual(x["verdict"],"FAIL_KNOWN_HUMAN_NECESSARY_CONDITION_IN_DECLARED_CASE")
        self.assertEqual(x["known_human_breaches"],["g1","n1"])
        self.assertIn("q1",x["human_unknowns"])
        self.assertFalse(x["aggregate_net_utility_certified"])

    def test_unknown_role_or_human_evidence_is_never_success(self):
        x=impact_screen(fixture(),(Impact("q1",economic_change=50),))
        self.assertEqual(x["verdict"],"UNRESOLVED_HUMAN_CONDITIONS")
        self.assertTrue(x["incomplete_actor_universe"])
        self.assertFalse(x["empirical_causality_or_consent_established"])

    def test_even_all_false_flags_never_certify_global_safety(self):
        x=impact_screen(fixture(),(Impact("g1",0,False,False),))
        self.assertEqual(x["verdict"],"CONDITIONAL_ENROLLED_HUMAN_SCREENS_ONLY_NOT_GLOBAL_SAFETY")
        self.assertTrue(x["incomplete_actor_universe"])

    def test_organisational_sector_state_and_politician_mismatch_rejected(self):
        r=fixture()
        for bad in (Stakeholder("l1","D","c1"),
                    Stakeholder("d1","L","c1"),
                    Stakeholder("i1","M","c1")):
            with self.subTest(bad=bad),self.assertRaisesRegex(ValueError,"role-kind mismatch"):
                validate(replace(r,stakeholders=(*r.stakeholders,bad)))

    def test_no_society_class_owned_by_company(self):
        r=fixture()
        with self.assertRaisesRegex(ValueError,"societal role"):
            validate(replace(r,stakeholders=(*r.stakeholders,
                                              Stakeholder("q1","Q","c1")))

    def test_employee_role_cannot_bleed_between_companies(self):
        r=fixture()
        with self.assertRaisesRegex(ValueError,"specific C"):
            validate(replace(r,stakeholders=(*r.stakeholders,
                                              Stakeholder("g1","G","nonexistent-C")))

    def test_B_without_association_cannot_be_hidden(self):
        r=fixture()
        with self.assertRaisesRegex(ValueError,"every B requires"):
            validate(replace(r,links=(r.links[0],)))

    def test_C_without_association_cannot_be_hidden(self):
        r=fixture()
        with self.assertRaisesRegex(ValueError,"every C requires"):
            validate(replace(r,links=(BToC("b1","c1","owned_by"),
                                      BToC("b2","c1","affiliated_with"))))

    def test_duplicate_roles_or_ids_do_not_inflate_weight(self):
        r=fixture()
        with self.assertRaisesRegex(ValueError,"duplicate role"):
            validate(replace(r,stakeholders=(*r.stakeholders,r.stakeholders[0])))
        with self.assertRaisesRegex(ValueError,"duplicate actor"):
            validate(replace(r,actors=(*r.actors,r.actors[0])))
        with self.assertRaisesRegex(ValueError,"duplicate B-C"):
            validate(replace(r,links=(*r.links,r.links[0])))

    def test_invalid_economic_or_rights_types_are_rejected(self):
        for bad in (Impact("e1",float("inf")),Impact("e1",True),
                    Impact("g1",0,1,False),Impact("g1",0,False,"no")):
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                impact_screen(fixture(),(bad,))

    def test_duplicate_impacts_for_two_roles_not_allowed(self):
        with self.assertRaisesRegex(ValueError,"duplicate or unknown"):
            impact_screen(fixture(),(Impact("e1",1),Impact("e1",2)))
        with self.assertRaisesRegex(ValueError,"duplicate or unknown"):
            impact_screen(fixture(),(Impact("unseen",1),))

    def test_no_social_class_determines_need_or_desert_automatically(self):
        x=impact_screen(fixture(),(Impact("q1",0,None,None),))
        self.assertEqual(x["human_unknowns"],["q1"])
        self.assertEqual(x["individuals_and_entities"][0]["roles"],["Q"])

    def test_constructed_report_distinguishes_synthetic_from_observation(self):
        x=constructed_audit()
        self.assertEqual(x["pre_succession"]["A_status"],"VACANT_BY_SCENARIO")
        self.assertFalse(x["stakeholder_harm_counterexample"]["aggregate_net_utility_certified"])
        self.assertEqual(x["stakeholder_harm_counterexample"]["known_human_breaches"],["g1","n1"])
        self.assertIn("D",x["roles_defined"])
        self.assertEqual(len(x["roles_defined"]),17)


if __name__ == "__main__":
    unittest.main()

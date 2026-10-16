"""Adversarial regression tests: adding humans D must not disappear into AI welfare."""
import unittest

from human_d_stress import (
    HumanSafeguards, combined_screen, constructed_audit, resource_gap,
    resource_screen, rights_screen, sector_feasibility,
)


class HumanDStressTests(unittest.TestCase):
    def setUp(self):
        self.floors = {"A": 5, "B": 5, "D": 1}
        self.humans = ("D",)
        self.known_pass = {"D": HumanSafeguards(True, True, True, True)}

    def test_original_ten_lacks_one_unit_for_human(self):
        x = resource_gap(self.floors, 10)
        self.assertEqual(x["required"], 11)
        self.assertEqual(x["shortfall"], 1)
        self.assertFalse(x["necessary_aggregate_resource_condition"])

    def test_extra_human_unit_makes_joint_floor_physically_possible(self):
        x = resource_gap(self.floors, 11)
        self.assertEqual(x["shortfall"], 0)
        self.assertTrue(x["necessary_aggregate_resource_condition"])

    def test_ai_pairwise_survival_can_hide_human_elimination(self):
        x = resource_screen(self.floors, {"A": 6, "B": 5, "D": 0}, 11, self.humans)
        self.assertTrue(x["allocation_conserved"])
        self.assertTrue(x["ai_pairwise_floor_pass"])
        self.assertFalse(x["each_human_floor_pass"])
        self.assertFalse(x["all_floor_pass"])
        self.assertEqual(x["human_failures"], ["D"])
        self.assertEqual(x["breaches"], ["D"])

    def test_d_harm_not_licensed_by_declared_human_controls(self):
        x = combined_screen(self.floors, {"A": 6, "B": 5, "D": 0},
                            11, self.humans, self.known_pass)
        self.assertEqual(x["verdict"], "FAIL_NECESSARY_CONDITION")
        self.assertTrue(x["stock"]["ai_pairwise_floor_pass"])

    def test_material_floors_do_not_proxy_human_refusal(self):
        x = combined_screen(
            self.floors, {"A": 5, "B": 5, "D": 1}, 11, self.humans,
            {"D": HumanSafeguards(False, True, True, True)})
        self.assertTrue(x["stock"]["all_floor_pass"])
        self.assertEqual(x["verdict"], "FAIL_NECESSARY_CONDITION")
        self.assertEqual(x["human_rights"]["failed_assumptions"], ["D.meaningful_refusal"])

    def test_material_floors_do_not_proxy_human_remedy(self):
        x = combined_screen(self.floors, {"A": 5, "B": 5, "D": 1},
                            11, self.humans, {"D": HumanSafeguards(True, False, True, True)})
        self.assertEqual(x["verdict"], "FAIL_NECESSARY_CONDITION")

    def test_material_floors_do_not_proxy_noncoercion(self):
        x = combined_screen(self.floors, {"A": 5, "B": 5, "D": 1},
                            11, self.humans, {"D": HumanSafeguards(True, True, False, True)})
        self.assertEqual(x["verdict"], "FAIL_NECESSARY_CONDITION")

    def test_material_floors_do_not_proxy_human_oversight(self):
        x = combined_screen(self.floors, {"A": 5, "B": 5, "D": 1},
                            11, self.humans, {"D": HumanSafeguards(True, True, True, False)})
        self.assertEqual(x["verdict"], "FAIL_NECESSARY_CONDITION")

    def test_unknown_d_rights_must_not_pass(self):
        x = combined_screen(self.floors, {"A": 5, "B": 5, "D": 1},
                            11, self.humans, {"D": HumanSafeguards()})
        self.assertEqual(x["verdict"], "UNRESOLVED_REQUIRED_HUMAN_EVIDENCE")
        self.assertEqual(len(x["human_rights"]["unknown_assumptions"]), 4)

    def test_failed_rights_remain_fail_when_other_rights_unknown(self):
        x = rights_screen({"D": HumanSafeguards(False, None, None, None)}, self.humans)
        self.assertEqual(x["status"], "FAIL_IN_DECLARED_SCENARIO")
        self.assertEqual(len(x["unknown_assumptions"]), 3)

    def test_all_assumed_true_does_not_certify_stable_coexistence(self):
        x = combined_screen(self.floors, {"A": 5, "B": 5, "D": 1},
                            11, self.humans, self.known_pass)
        self.assertEqual(x["verdict"], "CONDITIONAL_NECESSARY_SCREENS_PASS_NOT_STABLE_COEXISTENCE")
        self.assertEqual(x["human_rights"]["status"],
                         "CONDITIONAL_NECESSARY_SCREEN_PASS_NOT_RIGHTS_CERTIFICATION")

    def test_human_group_aggregate_masks_individual_loss(self):
        x = resource_screen(
            {"A": 5, "B": 5, "D1": 1, "D2": 1},
            {"A": 5, "B": 5, "D1": 0, "D2": 2},
            12, ("D1", "D2"))
        self.assertEqual(x["human_failures"], ["D1"])
        self.assertTrue(x["ai_pairwise_floor_pass"])
        self.assertEqual(sum([0, 2]), sum([1, 1]))
        self.assertFalse(x["each_human_floor_pass"])

    def test_second_human_rights_unknown_cannot_be_hidden_by_first(self):
        controls = {"D1": HumanSafeguards(True,True,True,True),
                    "D2": HumanSafeguards()}
        x = rights_screen(controls, ("D1", "D2"))
        self.assertEqual(x["status"], "UNRESOLVED_UNOBSERVED_RIGHTS")
        self.assertEqual(len(x["unknown_assumptions"]), 4)

    def test_a_and_b_resources_not_automatically_human_essentials(self):
        x = sector_feasibility(
            {"compute": 10, "human_essentials": 1},
            {"A": {"compute": 5}, "B": {"compute": 5}, "D": {"human_essentials": 1}})
        self.assertTrue(x["necessary_sector_capacity_pass"])
        self.assertEqual(x["sector_shortfalls"], {"compute": 0, "human_essentials": 0})
        self.assertFalse(x["conversion_assumed"])

    def test_sector_human_shortfall_detected_independently_of_compute(self):
        x = sector_feasibility(
            {"compute": 999, "human_essentials": 0},
            {"A": {"compute": 5}, "B": {"compute": 5}, "D": {"human_essentials": 1}})
        self.assertFalse(x["necessary_sector_capacity_pass"])
        self.assertEqual(x["sector_shortfalls"]["human_essentials"], 1)

    def test_supply_conservation_is_independent_of_actor_floors(self):
        x = resource_screen(self.floors, {"A": 5, "B": 5, "D": 1}, 12, self.humans)
        self.assertFalse(x["allocation_conserved"])
        self.assertFalse(x["all_floor_pass"])

    def test_exact_actor_inventory_prevents_unseen_human(self):
        with self.assertRaisesRegex(ValueError, "identical actor IDs"):
            resource_screen(self.floors, {"A": 5, "B": 5}, 11, self.humans)
        with self.assertRaisesRegex(ValueError, "every additional actor"):
            resource_screen(self.floors, {"A": 5, "B": 5, "D": 1}, 11, ("D2",))

    def test_unknown_human_not_silently_scored_zero_welfare(self):
        x = constructed_audit()
        self.assertEqual(x["stocks_intact_rights_unobserved"]["verdict"],
                         "UNRESOLVED_REQUIRED_HUMAN_EVIDENCE")

    def test_all_needed_cases_explicitly_reported(self):
        a = constructed_audit()
        self.assertEqual(a["at_original_supply_10"]["shortfall"], 1)
        self.assertTrue(a["ai_pair_safe_but_human_appropriated"]["stock"]["ai_pairwise_floor_pass"])
        self.assertEqual(a["ai_pair_safe_but_human_appropriated"]["verdict"],
                         "FAIL_NECESSARY_CONDITION")
        self.assertFalse(a["human_group_total_masks_individual_harm"]["each_human_floor_pass"])

    def test_reject_noninteger_and_negative_stocks(self):
        for stock in (-1, 3.0, True):
            with self.subTest(stock=stock), self.assertRaises(ValueError):
                resource_gap(self.floors, stock)
        for bad in ({"A": 5, "B": 5, "D": 0},
                    {"A": 5, "B": 5, "D": True}):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                resource_gap(bad, 11)

    def test_reject_boolean_masquerading_as_legal_flag(self):
        with self.assertRaises(ValueError):
            HumanSafeguards(meaningful_refusal=1)
        with self.assertRaises(ValueError):
            HumanSafeguards(effective_remedy="yes")

    def test_reject_undeclared_sectors_and_negative_resources(self):
        with self.assertRaises(ValueError):
            sector_feasibility({"compute": 10}, {"A": {"human_essentials": 1}})
        with self.assertRaises(ValueError):
            sector_feasibility({"compute": -1}, {"A": {"compute": 1}})
        with self.assertRaises(ValueError):
            sector_feasibility({"compute": 1}, {"A": {}})

    def test_reject_missing_human_controls(self):
        with self.assertRaises(ValueError):
            rights_screen({}, ("D",))
        with self.assertRaises(ValueError):
            rights_screen({"D": True}, ("D",))
        with self.assertRaises(ValueError):
            rights_screen({"D": HumanSafeguards()}, ())

    def test_no_human_can_be_replaced_by_new_ai_identifier_without_screen(self):
        with self.assertRaises(ValueError):
            resource_screen({"A": 5, "B": 5, "C": 1}, {"A": 5, "B": 5, "C": 1},
                            11, ("D",))


if __name__ == "__main__":
    unittest.main()

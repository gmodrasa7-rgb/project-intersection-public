"""PI-RISE-VAC tests: all examples hypothetical, no real personal or sponsor inputs."""
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from pi_rise_vac import allocation, queue_path, demonstration


def base(**overrides):
    x = dict(desired_person_net=3000, hypothetical_reserve="0.20",
             ai_stack=500, reserved_external_review=400,
             fx_buffer=200, budget_ceiling=4900)
    x.update(overrides)
    return allocation(**x)


class VACRegressions(unittest.TestCase):
    def test_no_double_count_base_plus_inside_ai_stack(self):
        a = base()
        self.assertEqual(a["gross_human_usd"], "3750.00")
        self.assertEqual(a["total_usd_month"], "4850.00")
        self.assertEqual(a["total_usd_year"], "58200.00")
        self.assertEqual(a["headroom_usd"], "50.00")

    def test_band_low_high(self):
        self.assertEqual(base(ai_stack=450)["total_usd_month"], "4800.00")
        self.assertEqual(base(ai_stack=550)["total_usd_month"], "4900.00")

    def test_insufficient_month_is_not_feasible(self):
        self.assertEqual(base(budget_ceiling=4800)["budget_status"], "OVER_BUDGET")

    def test_external_review_reservation_never_means_validated(self):
        self.assertEqual(base()["external_review_status"],
                         "ALLOCATED_ONLY_NOT_OBSERVED")

    def test_zero_review_budget_is_not_independent_validation(self):
        self.assertEqual(base(reserved_external_review=0)["external_review_status"],
                         "ALLOCATED_ONLY_NOT_OBSERVED")

    def test_high_generated_work_overloads_fixed_review_capacity(self):
        x = queue_path(arrivals_per_week=[10]*4, verified_capacity_per_week=[6]*4)
        self.assertEqual(x["unverified_queue_week_end"], [4, 8, 12, 16])
        self.assertTrue(x["backlog_increased"])

    def test_low_generation_leaves_no_backlog(self):
        x = queue_path(arrivals_per_week=[4]*4, verified_capacity_per_week=[6]*4)
        self.assertEqual(x["last_backlog"], 0)

    def test_more_verification_can_clear_high_generation_in_toy(self):
        x = queue_path(arrivals_per_week=[10]*4, verified_capacity_per_week=[11]*4)
        self.assertEqual(x["last_backlog"], 0)

    def test_capacity_zero_not_silent_external_attestation(self):
        x = queue_path(arrivals_per_week=[1,2], verified_capacity_per_week=[0,0])
        self.assertEqual(x["independent_external_attested"], "UNKNOWN_NOT_PROVIDED")

    def test_empty_and_mismatched_week_series_rejected(self):
        for a,c in (([],[]), ([1],[1,2])):
            with self.assertRaises(ValueError):
                queue_path(arrivals_per_week=a, verified_capacity_per_week=c)

    def test_negative_noninteger_claims_rejected(self):
        for a in ([-1], ["1.5"]):
            with self.assertRaises(ValueError):
                queue_path(arrivals_per_week=a, verified_capacity_per_week=[3])

    def test_unsafe_finance_inputs_rejected(self):
        for override in ({"hypothetical_reserve":"1"},
                         {"fx_buffer":-1}, {"ai_stack":1.23}):
            with self.assertRaises(ValueError):
                base(**override)

    def test_initial_queue_tracks_only_new_debt(self):
        x=queue_path(arrivals_per_week=[3,3], verified_capacity_per_week=[2,2],
                     initial_unverified=4)
        self.assertEqual(x["unverified_queue_week_end"], [5,6])
        self.assertTrue(x["backlog_increased"])

    def test_external_count_is_not_imputed_by_reviewer_dollars(self):
        x=demonstration()
        self.assertEqual(x["month_budget"]["external_review_status"],
                         "ALLOCATED_ONLY_NOT_OBSERVED")
        self.assertEqual(x["high_generation_same_review"]["last_backlog"],16)
        self.assertEqual(x["status"],"FORMAL_TOY_NOT_FIELD_VALIDATED")


if __name__ == "__main__":
    unittest.main()

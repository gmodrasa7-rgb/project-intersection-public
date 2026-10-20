"""PI-RISE-DC v0.1.0: adversarial synthetic tests of TWO resource clocks."""
import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from pi_rise_dual_clock import cash_timing, review_workload, demo
from pi_rise_vac import queue_path


class DualClockTests(unittest.TestCase):
    def test_delayed_but_full_payment_is_not_timely_cash(self):
        d=demo()["delayed_payment"]
        self.assertEqual(d["first_breach"]["event_id"],"human_due")
        self.assertEqual(d["minimum_initial_cash_by_pool_usd"]["unrestricted"],"3950.00")
        self.assertEqual(d["minimum_initial_cash_by_pool_usd"]["restricted_project"],"900.00")
        self.assertEqual(d["final_balances_usd"]["unrestricted"],"0.00")
        self.assertEqual(d["final_balances_usd"]["restricted_project"],"0.00")

    def test_adequate_initial_buffer_prevents_breach(self):
        d=demo()["adequately_prefunded"]
        self.assertIsNone(d["first_breach"])
        self.assertEqual(d["final_balances_usd"]["unrestricted"],"3950.00")
        self.assertEqual(d["final_balances_usd"]["restricted_project"],"900.00")

    def test_one_hard_packet_vs_five_easy(self):
        d=demo()
        hard=d["one_hard_claim"]["history"]
        easy=d["five_easy_claims"]["history"]
        self.assertEqual([x["unreviewed_hours"] for x in hard],
                         ["12.00","4.00","0.00"])
        self.assertEqual(hard[0]["completed_claims"],0)
        self.assertEqual(easy[0]["completed_claims"],5)
        self.assertEqual(easy[0]["unreviewed_hours"],"0.00")

    def test_same_total_aggregates_can_hide_intra_period_drought(self):
        events=[
            dict(event_id="spend", day=1,order=0,pool="unrestricted",
                 kind="human_support",amount_usd="500"),
            dict(event_id="later_payment", day=1,order=1,pool="unrestricted",
                 kind="inflow",amount_usd="500"),
        ]
        result=cash_timing(events)
        self.assertEqual(result["final_balances_usd"]["unrestricted"],"0.00")
        self.assertEqual(result["minimum_initial_cash_by_pool_usd"]["unrestricted"],"500.00")
        self.assertEqual(result["first_breach"]["event_id"],"spend")
        events[0]["order"]=1
        events[1]["order"]=0
        earlier=cash_timing(events)
        self.assertIsNone(earlier["first_breach"])
        self.assertEqual(earlier["minimum_initial_cash_by_pool_usd"]["unrestricted"],"0.00")

    def test_restricted_cannot_pay_human_under_declared_toy_contract(self):
        x=[dict(event_id="bad",day=1,order=0,pool="restricted_project",
                kind="human_support",amount_usd="3750")]
        with self.assertRaises(ValueError):
            cash_timing(x)

    def test_cross_pool_netting_forbidden(self):
        # Even an earlier, generously funded restricted project pool cannot
        # cover an unfunded personal payroll under the *toy* pool rules.
        x=[
            dict(event_id="grant",day=0,order=0,pool="restricted_project",
                 kind="inflow",amount_usd="5000"),
            dict(event_id="human",day=1,order=0,pool="unrestricted",
                 kind="human_support",amount_usd="3750"),
        ]
        a=cash_timing(x)
        self.assertEqual(a["minimum_initial_cash_by_pool_usd"]["unrestricted"],"3750.00")
        self.assertEqual(a["minimum_initial_cash_by_pool_usd"]["restricted_project"],"0.00")

    def test_duplicate_or_ambiguous_event_order_rejected(self):
        a=dict(event_id="a",day=1,order=0,pool="unrestricted",
               kind="inflow",amount_usd="1")
        b=dict(event_id="b",day=1,order=0,pool="unrestricted",
               kind="human_support",amount_usd="1")
        with self.assertRaises(ValueError):
            cash_timing([a,b])
        with self.assertRaises(ValueError):
            cash_timing([a,a])

    def test_invalid_amount_and_event_rejected(self):
        ev=dict(event_id="bad",day=1,order=0,pool="unrestricted",
                kind="inflow",amount_usd=1.25)
        with self.assertRaises(ValueError):
            cash_timing([ev])
        ev["amount_usd"]="1.001"
        with self.assertRaises(ValueError):
            cash_timing([ev])
        ev["amount_usd"]="NaN"
        with self.assertRaises(ValueError):
            cash_timing([ev])

    def test_invalid_review_capacity_and_packet_rejected(self):
        packets=[dict(id="a",arrival_week=1,priority=1,review_hours="0")]
        with self.assertRaises(ValueError):
            review_workload(packets,["8"])
        packets[0]["review_hours"]="10"
        with self.assertRaises(ValueError):
            review_workload(packets,["-8"])
        with self.assertRaises(ValueError):
            review_workload([packets[0],packets[0]],["8"])

    def test_review_is_not_claim_validity_or_independence(self):
        a=demo()["one_hard_claim"]
        self.assertFalse(a["external_independence_verified"])
        self.assertTrue(a["completion_means_assUMED_WORK_DONE_NOT_TRUE_CLAIM"])

    def test_prior_vac_aggregate_check_misses_temporal_overload(self):
        # Legacy VAC's sum(A)>sum(C) flag is NOT enough:
        # same total counts may still leave unverified work at horizon end.
        x=queue_path(arrivals_per_week=[0,10],
                     verified_capacity_per_week=[10,0])
        self.assertFalse(x["verifier_overload_observed_in_synthetic_model"])
        self.assertEqual(x["last_backlog"],10)

    def test_real_cash_unknown_from_synthetic_data(self):
        x=demo()
        self.assertEqual(x["empirical_status"],"TOY_SCENARIOS_ONLY")
        self.assertTrue(x["delayed_payment"]["starting_cash_is_not_a_bank_balance"])

if __name__ == "__main__":
    unittest.main()

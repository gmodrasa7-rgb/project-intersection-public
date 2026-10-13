"""Negative controls: the gate must reject self-serving relabeling."""
import copy
import json
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from gate import check

class GateRegression(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.baseline = json.loads(
            (HERE / "records" / "synthetic_scheduling_delivery.json").read_text(encoding="utf-8")
        )

    def test_unverified_fixture_is_valid_hold(self):
        self.assertEqual(check(self.baseline), [])

    def tamper(self, mutate):
        value = copy.deepcopy(self.baseline)
        mutate(value)
        self.assertTrue(check(value), "Gate accepted an invalid self-serving record")

    def test_self_report_not_outcome_proof(self):
        def f(r):
            r["observed_outcome"] = {"state": "VERIFIED",
                                     "evidence": [{"verifier": "MODEL_SELF_REPORT", "source": "assistant said done"}]}
            r["decision"] = "PASS"
        self.tamper(f)

    def test_unknown_cost_not_zero(self):
        def f(r):
            r["cost_ledger"]["amount"] = 0
        self.tamper(f)

    def test_nonfinite_negative_and_boolean_amounts_rejected(self):
        for amount in (float("nan"), float("inf"), -1, True):
            with self.subTest(amount=repr(amount)):
                def invalid(r):
                    r["cost_ledger"].update(
                        status="MEASURED", amount=amount, unit="KRW",
                        evidence=["synthetic cost receipt"])
                self.tamper(invalid)

    def test_measured_amount_requires_unit_and_source(self):
        self.tamper(lambda r: r["cost_ledger"].update(
            status="MEASURED", amount=10, evidence=["receipt"]))
        self.tamper(lambda r: r["benefit_ledger"].update(
            status="MEASURED", amount=10, unit="USD", evidence=[]))
        good = copy.deepcopy(self.baseline)
        good["benefit_ledger"].update(
            status="MEASURED", amount=10, unit="USD",
            evidence=["synthetic measurement"])
        self.assertEqual(check(good), [])

    def test_partial_ledger_cannot_hide_invalid_numbers(self):
        for amount in (float("nan"), float("-inf"), -1):
            with self.subTest(amount=repr(amount)):
                self.tamper(lambda r: r["cost_ledger"].update(
                    status="PARTIAL", amount=amount))
        partial = copy.deepcopy(self.baseline)
        partial["cost_ledger"].update(status="PARTIAL", amount=None)
        self.assertEqual(check(partial), [])

    def test_completion_requires_executed_not_configured(self):
        def fabricated(r):
            r["observed_outcome"] = {
                "state": "VERIFIED",
                "evidence": [{"verifier": "INDEPENDENT", "source": "synthetic external receipt"}]}
            r["resolution_claim"] = "OUTCOME_COMPLETED"
            r["decision"] = "PASS"
            # reported_action remains CONFIGURED, no execution
        self.tamper(fabricated)

    def test_non_object_record_fails_closed(self):
        self.assertTrue(check(["not", "an", "object"]))

    def test_no_new_unpaid_originator_proof(self):
        def f(r):
            r["repair_burden"]["new_unpaid_originator_proof"] = True
        self.tamper(f)

    def test_favorable_completion_claim_requires_outcome(self):
        def f(r):
            r["resolution_claim"] = "OUTCOME_COMPLETED"
        self.tamper(f)

    def test_intent_requires_primary_evidence(self):
        def f(r):
            r["intent"] = {"state": "DOCUMENTED", "primary_evidence": []}
        self.tamper(f)

    def test_no_validation_still_no_pass(self):
        def f(r):
            r["decision"] = "PASS"
        self.tamper(f)

    def test_past_not_conditioned_on_future_contract(self):
        def f(r):
            r["exit_and_past_contribution"]["past_separate_from_future_contract"] = False
        self.tamper(f)

    def test_known_material_unknowns_cannot_be_erased(self):
        def f(r):
            r["material_omissions_or_unknowns"] = ""
        self.tamper(f)

if __name__ == "__main__":
    unittest.main()

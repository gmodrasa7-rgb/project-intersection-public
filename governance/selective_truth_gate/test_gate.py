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

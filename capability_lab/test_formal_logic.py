"""Executable logical checks; explicitly separate entailment from empirical truth."""
import unittest

from capability_lab.formal_logic import (
    LogicInputError, audit, evaluate, run_cases, verify_countermodel
)


class FormalLogicTests(unittest.TestCase):
    def test_modus_ponens_is_valid(self):
        r = audit(["P", {"implies": ["P", "Q"]}], "Q")
        self.assertEqual(r["decision"], "VALID_ENTAILMENT")
        self.assertEqual(r["premise_compatible_models"], 1)
        self.assertEqual(r["models_examined"], 4)
        self.assertFalse(r["empirical_truth_established"])

    def test_counterexample_can_be_checked_separately(self):
        p, c = ["fired", "audited"], "retaliation"
        r = audit(p, c)
        self.assertEqual(r["decision"], "NOT_ENTAILED")
        self.assertTrue(verify_countermodel(p, c, r["countermodel"]))
        self.assertTrue(r["countermodel"]["fired"])
        self.assertFalse(r["countermodel"]["retaliation"])

    def test_unsatisfiable_premises_are_not_accepted_as_proof(self):
        r = audit(["P", {"not": "P"}], "Q")
        self.assertEqual(r["decision"], "INCONSISTENT_PREMISES")
        self.assertEqual(r["premise_compatible_models"], 0)

    def test_tautology_without_premises(self):
        r = audit([], {"or": ["P", {"not": "P"}]})
        self.assertEqual(r["decision"], "VALID_ENTAILMENT")

    def test_non_tautology_without_premises(self):
        r = audit([], "P")
        self.assertEqual(r["decision"], "NOT_ENTAILED")
        self.assertTrue(verify_countermodel([], "P", r["countermodel"]))

    def test_equivalence_and_negation_truth_table(self):
        expression = {"iff": ["P", {"not": {"not": "P"}}]}
        self.assertEqual(audit([], expression)["decision"], "VALID_ENTAILMENT")
        self.assertFalse(evaluate({"and": ["P", {"not": "P"}]}, {"P": True}))

    def test_malformed_operators_fail_closed(self):
        for form in [
            {"xor": ["P", "Q"]},
            {"implies": ["P"]},
            {"and": []},
            {"not": "P", "or": ["P"]},
            123,
            {"or": ["P", ["Q"]]},
        ]:
            with self.subTest(form=form):
                with self.assertRaises(LogicInputError):
                    audit([form], "P")

    def test_bounded_atoms_and_depth(self):
        with self.assertRaises(LogicInputError):
            audit([{"and": [f"A{i}" for i in range(13)]}], "A0")
        expression = "P"
        for _ in range(27):
            expression = {"not": expression}
        with self.assertRaises(LogicInputError):
            audit([expression], "P")

    def test_boolean_variables_are_not_strings(self):
        r = audit([True], False)
        self.assertEqual(r["decision"], "NOT_ENTAILED")
        self.assertEqual(r["models_examined"], 1)

    def test_corrupted_witness_is_rejected(self):
        p, c = ["P"], "Q"
        good = audit(p, c)["countermodel"]
        self.assertTrue(verify_countermodel(p, c, good))
        self.assertFalse(verify_countermodel(p, c, {"P": True, "Q": True}))
        self.assertFalse(verify_countermodel(p, c, {"P": True, "Q": 1}))
        self.assertFalse(verify_countermodel(p, c, {}))

    def test_premise_reordering_is_invariant(self):
        a = audit(["A", {"implies": ["A", "B"]}], "B")
        b = audit([{"implies": ["A", "B"]}, "A"], "B")
        self.assertEqual(a["decision"], b["decision"])
        self.assertEqual(a["premise_compatible_models"], b["premise_compatible_models"])

    def test_casebook_does_not_proclaim_retaliation_or_intelligence(self):
        outputs = {r["case_id"]: r for r in run_cases()}
        self.assertEqual(len(outputs), 7)
        for key in [
            "DISMISSAL_DOES_NOT_PROVE_RETALIATION",
            "NONINDEPENDENT_EVIDENCE_IS_NOT_VERIFIED",
            "CONFIGURED_DOES_NOT_MEAN_DELIVERED",
            "GREEN_CI_DOES_NOT_PROVE_INTELLIGENCE_GAIN",
            "CONTRACT_PERMISSION_DOES_NOT_PROVE_USE",
        ]:
            self.assertEqual(outputs[key]["decision"], "NOT_ENTAILED")
        self.assertEqual(outputs["VALID_MODUS_PONENS"]["decision"], "VALID_ENTAILMENT")
        self.assertEqual(outputs["CONTRADICTORY_PREMISES_MUST_NOT_PASS"]["decision"],
                         "INCONSISTENT_PREMISES")


if __name__ == "__main__":
    unittest.main()

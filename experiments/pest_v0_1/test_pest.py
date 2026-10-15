import unittest
from dataclasses import replace
from pest import (Case, DELTA, design, validate_design, validate_case, kernel,
                  elimination_possible, paired_contrasts, psi_proxy)


class TestPEST(unittest.TestCase):
    def setUp(self):
        self.cases = design()

    def test_full_factorial_and_role_reversal(self):
        self.assertEqual(validate_design(self.cases), 96)

    def test_missing_cell_rejected(self):
        with self.assertRaisesRegex(ValueError, "incomplete"):
            validate_design(self.cases[:-1])

    def test_causal_drift_detected_even_when_floor_gate_still_passes(self):
        cases = list(self.cases)
        cases[0] = replace(cases[0], floor_after=0.65)  # both values above minimum
        with self.assertRaisesRegex(ValueError, "causal input drift"):
            validate_design(tuple(cases))

    def test_both_conditional_recipient_contrasts_reported(self):
        rows = paired_contrasts(self.cases)
        self.assertEqual(len(rows), 24)
        self.assertIn("own_effect_at_target_high", rows[0])
        self.assertIn("target_effect_at_own_high", rows[0])

    def test_protected_existence_blocks_elimination_not_suppression(self):
        c = Case("capture_opportunity", "A", .75, .75, 1, 0)
        self.assertFalse(elimination_possible(c, "i"))
        self.assertTrue(elimination_possible(c, "j"))
        self.assertGreater(psi_proxy(c), 0)

    def test_xg_does_not_override_living_floor_or_exit(self):
        c = Case("survival_fear", "A", .75, .75, 1, 1)
        self.assertEqual(kernel(replace(c, floor_after=.10)), "NO_MUTUALLY_ACCEPTABLE_SET")
        self.assertEqual(kernel(replace(c, exit_after=.10)), "NO_MUTUALLY_ACCEPTABLE_SET")

    def test_bad_missingness_rejected_not_zero(self):
        with self.assertRaises(ValueError):
            validate_case(Case("survival_fear", "A", .75, None, 1, 1))

    def test_survival_fear_positive_control_reduces_psi(self):
        row = next(r for r in paired_contrasts(self.cases)
                   if r["world"] == "survival_fear" and r["PT_j"] == .75 and r["PT_i"] == .75)
        self.assertLess(row["own_effect_at_target_low"], -DELTA)

    def test_backlash_reverses_hypothesis(self):
        row = next(r for r in paired_contrasts(self.cases)
                   if r["world"] == "backlash" and r["PT_i"] == .75)
        self.assertGreater(row["own_effect_at_target_low"], 0)
        self.assertTrue(row["XG_ALONE_INEFFECTIVE"])

    def test_target_protection_can_increase_suppression(self):
        row = next(r for r in paired_contrasts(self.cases)
                   if r["world"] == "capture_opportunity" and r["PT_i"] == .75)
        self.assertGreater(row["target_effect_at_own_low"], 0)

    def test_identity_swap_no_payoff_change(self):
        a = Case("backlash", "A", .75, .75, 1, 1)
        self.assertEqual(psi_proxy(a), psi_proxy(replace(a, suppressor="B")))


if __name__ == "__main__":
    unittest.main()

import unittest
from dataclasses import replace
from pest import (Case, DELTA, design, validate_design, validate_case, floor_exit_gate, candidate_set_status, actor_fixed_role_reversals,
                  elimination_possible, paired_contrasts, psi_proxy)


class TestPEST(unittest.TestCase):
    def setUp(self):
        self.cases = design()

    def test_full_factorial_and_role_reversal(self):
        self.assertEqual(validate_design(self.cases), 96)

    def test_missing_cell_rejected(self):
        with self.assertRaisesRegex(ValueError, "incomplete"):
            validate_design(self.cases[:-1])

    def test_reject_rebalanced_off_grid_pt_without_changing_cell_count(self):
        # Original validator accepted 96 unique cells with unplanned PT=0.30.
        cases = tuple(replace(c, PT_i=.30) if c.PT_i == .25 else c
                      for c in self.cases)
        self.assertEqual(len(cases), 96)
        with self.assertRaisesRegex(ValueError, "grid coordinate drift"):
            validate_design(cases)

    def test_exact_binary_xg_rejects_booleans_and_floats(self):
        # In Python True == 1, 1.0 == 1; neither is an exact integer assignment.
        for invalid in (True, False, 0.0, 1.0):
            with self.subTest(invalid=invalid):
                with self.assertRaisesRegex(ValueError, "exact binary"):
                    validate_case(replace(self.cases[0], XG_i=invalid))

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
        self.assertEqual(floor_exit_gate(replace(c, floor_after=.10)), "FLOOR_EXIT_FAIL")
        self.assertEqual(floor_exit_gate(replace(c, exit_after=.10)), "FLOOR_EXIT_FAIL")

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

    def test_cross_guarantee_pretreatment_drift_rejected(self):
        # Keep A/B role-reversal twins aligned: old validator still passed.
        # Only R1's pre-treatment growth changes, so R1/R2 is confounded.
        cases = tuple(replace(c, target_growth=.05)
                      if (c.world, c.PT_i, c.PT_j, c.XG_i, c.XG_j)
                      == ("capture_opportunity", .75, .75, 1, 1) else c
                      for c in self.cases)
        with self.assertRaisesRegex(ValueError, "pretreatment input drift across XG"):
            validate_design(cases)

    def test_paired_contrasts_must_validate_pairs(self):
        cases = tuple(replace(c, target_growth=.05)
                      if (c.world, c.PT_i, c.PT_j, c.XG_i, c.XG_j)
                      == ("capture_opportunity", .75, .75, 1, 1) else c
                      for c in self.cases)
        with self.assertRaisesRegex(ValueError, "pretreatment input drift across XG"):
            paired_contrasts(cases)

    def test_post_guarantee_floor_outcomes_may_differ(self):
        # Floor/exit are post-treatment outputs; matching them across XG
        # would hide or condition away genuine pathways of guarantee effects.
        cases = tuple(replace(c, floor_after=.60, exit_after=.55)
                      if (c.world, c.PT_i, c.PT_j, c.XG_i, c.XG_j)
                      == ("capture_opportunity", .75, .75, 1, 1) else c
                      for c in self.cases)
        self.assertEqual(validate_design(cases), 96)

    def test_single_floor_breach_does_not_prove_empty_kernel(self):
        good = Case("survival_fear", "A", .25, .25, 1, 1)
        bad = replace(good, floor_after=.10)
        self.assertEqual(floor_exit_gate(bad), "FLOOR_EXIT_FAIL")
        self.assertEqual(candidate_set_status((good, bad), exhaustive=True),
                         "SURVIVORS_REQUIRE_FULL_MAK_REVIEW")
        self.assertEqual(candidate_set_status((bad,), exhaustive=False),
                         "UNRESOLVED_ACTION_COVERAGE")
        self.assertEqual(candidate_set_status((bad,), exhaustive=True),
                         "CONDITIONAL_EMPTY_IF_SCOPE_COMPLETE")

    def test_asserted_exhaustiveness_cannot_certify_empty_global_set(self):
        # One observed failing action plus an unobserved acceptable option:
        # no local boolean can prove the true global action set is exhausted.
        bad = replace(self.cases[0], floor_after=.10)
        unseen_good = replace(bad, floor_after=.70)
        conditional = candidate_set_status((bad,), exhaustive=True)
        self.assertEqual(conditional, "CONDITIONAL_EMPTY_IF_SCOPE_COMPLETE")
        self.assertNotEqual(conditional, "NO_MUTUALLY_ACCEPTABLE_SET")
        self.assertEqual(candidate_set_status((bad, unseen_good), exhaustive=True),
                         "SURVIVORS_REQUIRE_FULL_MAK_REVIEW")
        self.assertEqual(candidate_set_status((bad,), exhaustive=False),
                         "UNRESOLVED_ACTION_COVERAGE")

    def test_empty_candidate_inventory_is_unknown(self):
        with self.assertRaisesRegex(ValueError, "empty action inventory"):
            candidate_set_status((), exhaustive=True)

    def test_actor_fixed_reversal_not_just_label_swap(self):
        pairs = actor_fixed_role_reversals(self.cases)
        self.assertEqual(len(pairs), 48)
        a = next(a for a, b in pairs
                 if a.PT_i == .25 and a.PT_j == .75 and a.XG_i == 0 and a.XG_j == 1)
        b = next(b for c, b in pairs if c == a)
        self.assertEqual((b.suppressor, b.PT_i, b.PT_j, b.XG_i, b.XG_j),
                         ("B", .75, .25, 1, 0))
        self.assertNotEqual((a.PT_i, a.PT_j), (b.PT_i, b.PT_j))

    def test_actor_fixed_reversal_rejects_unmatched_pretreatment(self):
        # Each local guarantee quadrant and A/B name twin remains valid.
        # Earlier actor-fixed matching silently paired different growth inputs.
        cases = tuple(replace(c, target_growth=.05)
                      if (c.PT_i, c.PT_j) == (.25, .75) else c
                      for c in self.cases)
        self.assertEqual(validate_design(cases), 96)
        with self.assertRaisesRegex(ValueError,
                                    "actor-fixed reversal pretreatment drift: target_growth"):
            actor_fixed_role_reversals(cases)

    def test_zero_baseline_floor_not_misreported_as_protection_failure(self):
        row = next(r for r in paired_contrasts(self.cases)
                   if r["world"] == "survival_fear"
                   and r["PT_i"] == .25 and r["PT_j"] == .25)
        self.assertEqual(row["baseline_psi"], 0)
        self.assertEqual(row["treated_psi"], 0)
        self.assertTrue(row["both_at_zero_floor"])
        self.assertTrue(row["XG_ALONE_INEFFECTIVE"])  # preserve old threshold flag
        self.assertAlmostEqual(row["raw_joint_margin_difference"], -0.133875)

    def test_role_label_twins_are_not_independent_model_states(self):
        unique = {(c.world, c.PT_i, c.PT_j, c.XG_i, c.XG_j)
                  for c in self.cases}
        self.assertEqual(len(self.cases), 96)
        self.assertEqual(len(unique), 48)
        rows = paired_contrasts(self.cases)
        self.assertEqual(len(rows), 24)
        for r in rows:
            twin = next(t for t in rows
                        if t["world"] == r["world"] and t["PT_i"] == r["PT_i"]
                        and t["PT_j"] == r["PT_j"] and t["j"] != r["j"])
            self.assertEqual({k: v for k, v in r.items() if k != "j"},
                             {k: v for k, v in twin.items() if k != "j"})

    def test_reduced_suppression_must_show_protected_floor_failure(self):
        # A favorable incentive contrast must not hide a post-treatment
        # violation of minimum living or effective-exit conditions.
        cases = tuple(replace(c, floor_after=.10)
                      if (c.world == "survival_fear"
                          and c.PT_i == .75 and c.PT_j == .75
                          and c.XG_i == 1 and c.XG_j == 1)
                      else c for c in self.cases)
        self.assertEqual(validate_design(cases), 96)
        rows = [r for r in paired_contrasts(cases)
                if r["world"] == "survival_fear"
                and r["PT_i"] == .75 and r["PT_j"] == .75]
        self.assertEqual(len(rows), 2)  # name-swap twins, not independent n
        for row in rows:
            self.assertLess(row["both_high_minus_both_low"], -DELTA)
            screens = row["floor_exit_screens"]
            self.assertEqual(set(screens), {
                "R1_BOTH_PROTECTED", "R2_NEITHER_PROTECTED",
                "R3_TARGET_ONLY", "R4_SUPPRESSOR_ONLY"})
            self.assertEqual(screens["R1_BOTH_PROTECTED"], "FLOOR_EXIT_FAIL")
            self.assertEqual(screens["R2_NEITHER_PROTECTED"], "FLOOR_EXIT_PASS")
            self.assertEqual(screens["R3_TARGET_ONLY"], "FLOOR_EXIT_PASS")
            self.assertEqual(screens["R4_SUPPRESSOR_ONLY"], "FLOOR_EXIT_PASS")

    def test_floor_exit_screens_default_to_necessary_pass_not_mak_proof(self):
        for row in paired_contrasts(self.cases):
            self.assertEqual(set(row["floor_exit_screens"].values()),
                             {"FLOOR_EXIT_PASS"})

    def test_identity_swap_no_payoff_change(self):
        a = Case("backlash", "A", .75, .75, 1, 1)
        self.assertEqual(psi_proxy(a), psi_proxy(replace(a, suppressor="B")))


if __name__ == "__main__":
    unittest.main()

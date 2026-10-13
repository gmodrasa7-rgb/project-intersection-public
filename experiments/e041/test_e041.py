import unittest
import model
import causal_twin


class TestE041(unittest.TestCase):
    def test_historical_fixed_seed_reproduced(self):
        result = model.public_report()
        self.assertAlmostEqual(result["signal"]["baseline_brier"],0.2255456709,places=9)
        self.assertAlmostEqual(result["signal"]["with_exit_brier"],0.2173797149,places=9)
        self.assertAlmostEqual(result["null"]["improvement"],-0.0001956428,places=9)
        self.assertTrue(all(result["pre_registered_test"].values()))

    def test_target_leakage_is_blocked(self):
        rows = model.generate(100, 9, True)
        for keys in ((4,), (0,4), (0,0), (0,5)):
            with self.assertRaises(ValueError):
                model.heldout_brier(rows,keys)

    def test_seed_repeatability(self):
        self.assertEqual(model.evaluate(True,n=2000),model.evaluate(True,n=2000))

    def test_null_not_forced_positive(self):
        self.assertLess(model.evaluate(False)["improvement"],0)

    def test_twins_same_observation_different_interventions(self):
        r=causal_twin.demonstrate()
        self.assertTrue(r["observational_rows_identical"])
        self.assertAlmostEqual(r["do_x0_minus_do_x2_risk_causal_model"],0.24,places=12)
        self.assertAlmostEqual(r["do_x0_minus_do_x2_risk_proxy_model"],0,places=12)

    def test_proxy_has_no_direct_x_effect(self):
        self.assertEqual(causal_twin.risk("proxy_u",0.2,1,0),causal_twin.risk("proxy_u",0.2,1,2))
        self.assertNotEqual(causal_twin.risk("causal_x",0.2,1,0),causal_twin.risk("causal_x",0.2,1,2))

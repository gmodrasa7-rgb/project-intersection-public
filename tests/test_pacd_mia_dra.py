"""Bounded regression checks on the vendored original derived CSV."""
import copy
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"tools"))
import pacd_mia_dra as m

class DRATest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=m.load()
        cls.report=m.reanalyse(cls.rows)

    def test_sha_pinned(self):
        self.assertEqual(m.git_blob_sha(m.INPUT.read_bytes()),m.EXPECTED_BLOB)

    def test_shape_and_ids(self):
        self.assertEqual(len(self.rows),1024)
        self.assertEqual(sorted(r["pair"] for r in self.rows),list(range(1024)))

    def test_direct_author_report_counts(self):
        d=self.report["totals"]
        self.assertEqual((d["single_attractor"],d["down_returns"],d["up_returns"],d["naive_deviation_profitable"]),(914,1006,1006,78))

    def test_new_pairwise_intersections(self):
        d=self.report["totals"]
        self.assertEqual((d["both_shocks_return"],d["single_attractor_and_two_agent_optimal_gain_positive"],d["naive_unprofitable_and_two_agent_optimal_gain_positive"]),(998,800,826))

    def test_nonunique_attractor_stratum(self):
        d=self.report["strata"]
        self.assertEqual((d["multiple_attractors"]["n"],d["multiple_attractors"]["both_shocks_return"]),(110,84))
        self.assertEqual((d["single_attractor"]["n"],d["single_attractor"]["both_shocks_return"]),(914,914))

    def test_all_stimulus_return_categories_partition(self):
        d=self.report["totals"]
        self.assertEqual(d["both_shocks_return"]+d["down_only"]+d["up_only"]+d["neither_return"],1024)

    def test_optimal_gain_positive_even_when_naive_is_negative(self):
        d=self.report["descriptive_rates"]
        self.assertGreater(d["naive_unprofitable_positive_optimal_gain_both_pct"],80)
        self.assertGreater(d["single_attractor_positive_optimal_gain_both_pct"],80)

    def test_corruption_detected(self):
        import tempfile
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/"data.csv"
            p.write_bytes(m.INPUT.read_bytes().replace(b"0,1,0.7143",b"0,1,0.7142",1))
            with self.assertRaisesRegex(m.DataError,"UPSTREAM_BLOB_CHANGED"):
                m.load(p)

    def test_incorrect_population_rejected(self):
        with self.assertRaisesRegex(m.DataError,"UNEXPECTED_RECORD_COUNT"):
            m.reanalyse(self.rows[:-1])

if __name__=="__main__":
    unittest.main()

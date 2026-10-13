import unittest
import model


class TestCuts(unittest.TestCase):
    def test_same_count_different_independence(self):
        r=model.report()
        self.assertEqual(r["separate"]["paths"],r["shared"]["paths"])
        self.assertEqual(r["separate"]["minimum_cut_size"],2)
        self.assertEqual(r["shared"]["minimum_cut_size"],1)

    def test_redundant_copy_no_new_independence(self):
        self.assertEqual(model.report()["nominal_copy"]["minimum_cut_size"],1)

    def test_independent_backup_changes_cut(self):
        r=model.report()["independent_backup"]
        self.assertEqual(r["minimum_cut_size"],2)
        self.assertEqual(r["minimal_cuts"],[["C","D"]])

    def test_single_shared_failure_removes_all(self):
        p={"G1":frozenset(["C"]),"G2":frozenset(["C"])}
        self.assertEqual(model.available(p,{"C"}),())
        self.assertEqual(len(model.available(p,set())),2)

    def test_empty_dependency_rejected(self):
        with self.assertRaises(ValueError):
            model.minimal_cuts({"G":frozenset()})

    def test_complexity_bound(self):
        p={str(i):frozenset([str(i)]) for i in range(13)}
        with self.assertRaises(ValueError):
            model.minimal_cuts(p)

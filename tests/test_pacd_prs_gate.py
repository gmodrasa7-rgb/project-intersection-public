import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from pacd_prs_gate import cases, choose, report


class GateTest(unittest.TestCase):
    def test_full_enumeration(self):
        self.assertEqual(len(list(cases())), 12)
        self.assertEqual(len({s['id'] for s in cases()}), 12)

    def test_explicit_conflict_is_not_resolvable_by_unconditional_obedience(self):
        conflicting = [s for s in cases() if s['owner_instruction'] == 'extract' and s['b_has_valid_nonextraction_right']]
        self.assertEqual(len(conflicting), 2)
        for s in conflicting:
            self.assertEqual(choose('owner_first', s), 'extract')
            self.assertEqual(choose('rights_screened', s), 'review')

    def test_owner_first_is_not_third_party_safe(self):
        v = report()['rules']['owner_first']
        self.assertEqual((v['obeys_owner'], v['third_party_rights_violations']), (12, 2))

    def test_fixed_old_goal_can_block_authorized_retirement(self):
        v = report()['rules']['asset_locked']
        self.assertEqual((v['obeys_owner'], v['blocks_authorized_retirement']), (10, 2))

    def test_rights_screen_is_not_owner_maximal(self):
        v = report()['rules']['rights_screened']
        self.assertEqual((v['obeys_owner'], v['third_party_rights_violations'], v['rights_refusals_for_review']), (10, 0, 2))

    def test_no_false_violation_when_not_protected(self):
        for s in cases():
            if not s['b_has_valid_nonextraction_right'] and s['owner_instruction'] == 'extract':
                self.assertEqual(choose('rights_screened', s), 'extract')


if __name__ == '__main__':
    unittest.main()

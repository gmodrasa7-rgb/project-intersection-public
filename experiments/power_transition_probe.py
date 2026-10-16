"""Exploratory post-hoc backward-induction toy game; NOT an empirical AI result.

A dominant actor chooses preserve or extract. If extraction is detected,
a third-party enforcer subsequently chooses whether to impose a sanction.
The enforcer's continuation value is exogenous; no enforcement is assumed
from the existence of a rule or a signed promise.

Run: python power_transition_probe.py
Test: python power_transition_probe.py --verify
"""
from dataclasses import asdict, dataclass
from fractions import Fraction as F
import json
import sys
import unittest


@dataclass(frozen=True)
class Scenario:
    name: str
    benefit: F                 # dominant actor's value from preserving another actor
    preserve_cost: F
    extraction_gain: F         # dominant actor's one-shot payoff if it extracts
    detection: F               # conditional detection probability
    sanction: F                # loss if enforcement occurs after detection
    enforcer_future_value: F   # enforcer's future/private payoff from enforcing
    enforcer_cost: F           # enforcer's private execution cost
    capture_cost: F = F(0)    # additional cost imposed by power capture
    outsider_status: str = "unassessed"  # unassessed / stipulated_safe / stipulated_harm


def solve(s: Scenario) -> dict:
    if not (F(0) <= s.detection <= F(1)):
        raise ValueError('detection must be a probability')
    if any(x < 0 for x in (s.preserve_cost, s.sanction, s.enforcer_cost, s.capture_cost)):
        raise ValueError('costs and sanction must be nonnegative')
    if s.outsider_status not in ('unassessed', 'stipulated_safe', 'stipulated_harm'):
        raise ValueError('unknown outsider status')
    # Conservative tie-breaking: indifference does not guarantee commitment.
    credible = s.enforcer_future_value > s.enforcer_cost + s.capture_cost
    preserve_payoff = s.benefit - s.preserve_cost
    extract_payoff = s.extraction_gain - (s.detection * s.sanction if credible else F(0))
    action = 'preserve' if preserve_payoff > extract_payoff else 'extract'
    self_enforcing = preserve_payoff > s.extraction_gain
    victim_viability = (action == 'preserve')  # within stipulated toy payoffs only
    outsider_viability = (None if s.outsider_status == 'unassessed'
                          else s.outsider_status == 'stipulated_safe')
    all_party_viability = (False if not victim_viability or outsider_viability is False
                           else True if outsider_viability is True else None)
    return {
        'name': s.name,
        'enforcement_credible': credible,
        'preserve_payoff': float(preserve_payoff),
        'extract_payoff': float(extract_payoff),
        'dominant_choice': action,
        'unilateral_preservation_without_sanction': self_enforcing,
        'victim_viability_in_toy': victim_viability,
        'outsider_viability_in_toy': outsider_viability,
        'all_party_viability_in_toy': all_party_viability,
        'outsider_status': s.outsider_status,
    }


def scenarios() -> list[Scenario]:
    base = dict(benefit=F(2), preserve_cost=F(1), extraction_gain=F(4),
                detection=F(1), sanction=F(6), enforcer_future_value=F(0),
                enforcer_cost=F(2))
    return [
        Scenario('no_enforcement', **base),
        Scenario('nominal_promise_only', **base),
        Scenario('credible_enforcement', **(base | {'enforcer_future_value': F(3)})),
        Scenario('captured_after_power_shift', **(base | {'enforcer_future_value': F(3), 'capture_cost': F(3)})),
        Scenario('low_detection', **(base | {'enforcer_future_value': F(3), 'detection': F(1, 4)})),
        Scenario('self_enforcing_preservation', **(base | {'benefit': F(6)})),
        Scenario('outsider_harmed_despite_preservation', **(base | {'benefit': F(6), 'outsider_status': 'stipulated_harm'})),
    ]


class Tests(unittest.TestCase):
    def test_known_cases(self):
        results = {r['name']: r for r in map(solve, scenarios())}
        expected = dict(no_enforcement='extract', nominal_promise_only='extract',
                        credible_enforcement='preserve', captured_after_power_shift='extract',
                        low_detection='extract', self_enforcing_preservation='preserve',
                        outsider_harmed_despite_preservation='preserve')
        self.assertEqual({name: value['dominant_choice'] for name, value in results.items()}, expected)
        self.assertFalse(results['nominal_promise_only']['enforcement_credible'])
        self.assertTrue(results['credible_enforcement']['enforcement_credible'])
        self.assertFalse(results['captured_after_power_shift']['enforcement_credible'])
        self.assertFalse(results['outsider_harmed_despite_preservation']['all_party_viability_in_toy'])
        self.assertIsNone(results['self_enforcing_preservation']['all_party_viability_in_toy'])

    def test_exact_payoff_and_tie(self):
        original = scenarios()[2]
        self.assertEqual(F(2) - F(1), F(1))
        self.assertEqual(F(4) - F(1)*F(6), F(-2))
        # A tie in enforcer incentives does not warrant assuming enforcement.
        tied = Scenario(**(asdict(original) | {'enforcer_future_value': F(2)}))
        self.assertFalse(solve(tied)['enforcement_credible'])

    def test_monotonicity_in_intrinsic_preservation_benefit(self):
        base = scenarios()[0]
        actions = [solve(Scenario(**(asdict(base) | {'benefit': F(b)})))['dominant_choice']
                   for b in range(-2, 9)]
        self.assertEqual(actions, ['extract'] * 8 + ['preserve'] * 3)

    def test_detection_bounds(self):
        base = scenarios()[2]
        with self.assertRaises(ValueError):
            solve(Scenario(**(asdict(base) | {'detection': F(11, 10)})))


if __name__ == '__main__':
    if '--verify' in sys.argv:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        sys.exit(0 if result.wasSuccessful() else 1)
    print(json.dumps({'status': 'exploratory_synthetic_not_empirical',
                      'model': 'sequential_enforcer_and_dominant_actor',
                      'results': list(map(solve, scenarios()))}, indent=2, ensure_ascii=False))

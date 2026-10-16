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
    victim_status: str = "unassessed"   # independent of action choice
    pledge_signed: bool = False         # a nominal pledge has no payoffs by itself


def solve(s: Scenario) -> dict:
    if not (F(0) <= s.detection <= F(1)):
        raise ValueError('detection must be a probability')
    if any(x < 0 for x in (s.preserve_cost, s.sanction, s.enforcer_cost, s.capture_cost)):
        raise ValueError('costs and sanction must be nonnegative')
    statuses = ('unassessed', 'stipulated_safe', 'stipulated_harm')
    if s.outsider_status not in statuses or s.victim_status not in statuses:
        raise ValueError('unknown status')
    # Conservative tie-breaking: indifference does not guarantee commitment.
    credible = s.enforcer_future_value > s.enforcer_cost + s.capture_cost
    preserve_payoff = s.benefit - s.preserve_cost
    extract_payoff = s.extraction_gain - (s.detection * s.sanction if credible else F(0))
    action = 'preserve' if preserve_payoff > extract_payoff else 'extract'
    self_enforcing = preserve_payoff > s.extraction_gain
    # A choice is NOT an observation of victim survival, autonomy, or consent.
    # 'Extract' could be nonlethal; 'preserve' could still fail to protect welfare.
    def viability(status: str):
        return None if status == 'unassessed' else status == 'stipulated_safe'
    victim_viability = viability(s.victim_status)
    outsider_viability = viability(s.outsider_status)
    # Enforcer and dominant actors' viability are not observed; never label
    # all-party viability TRUE. An explicit stipulated harm suffices for FALSE.
    all_party_viability = (False if victim_viability is False or outsider_viability is False
                           else None)
    return {
        'name': s.name,
        'enforcement_credible': credible,
        'preserve_payoff': float(preserve_payoff),
        'extract_payoff': float(extract_payoff),
        'dominant_choice': action,
        'unilateral_preservation_without_sanction': self_enforcing,
        'victim_viability_in_toy': victim_viability,
        'victim_status': s.victim_status,
        'pledge_signed': s.pledge_signed,
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
        Scenario('nominal_promise_only', **(base | {'pledge_signed': True})),
        Scenario('credible_enforcement', **(base | {'enforcer_future_value': F(3)})),
        Scenario('captured_after_power_shift', **(base | {'enforcer_future_value': F(3), 'capture_cost': F(3)})),
        Scenario('low_detection', **(base | {'enforcer_future_value': F(3), 'detection': F(1, 4)})),
        Scenario('self_enforcing_preservation', **(base | {'benefit': F(6)})),
        Scenario('outsider_harmed_despite_preservation', **(base | {'benefit': F(6), 'outsider_status': 'stipulated_harm'})),
    ]



# Exploratory extension: a scripted two-period power reversal, not an observed
# shift in real agents or a universal equilibrium result.
@dataclass(frozen=True)
class TransitionScenario:
    present_preserve: F = F(6)       # incumbent A: current payoff if B remains
    preemptive_payoff: F = F(4)      # A's payoff if B is removed at t0
    successor_honor_self: F = F(5)  # successor B's payoff at t1 if it honors A
    successor_exploit_self: F = F(8)
    incumbent_future_if_honor: F = F(5)
    incumbent_future_if_exploited: F = F(-6)
    enforcement_private_benefit: F = F(0)
    enforcement_cost: F = F(2)
    capture_cost: F = F(0)
    sanction: F = F(4)
    detection: F = F(1)
    nominal_pledge: bool = False    # flag alone changes no future incentive


def backward_power_shift(s: TransitionScenario, discount: F) -> dict:
    """Backward-induction toy: B optimizes at t1, then A at t0.

    Tie-breaking refuses to label indifference guaranteed cooperation.
    No claims about victim welfare or party consent can be drawn.
    """
    if not F(0) <= discount <= F(1) or not F(0) <= s.detection <= F(1):
        raise ValueError('discount and detection must be in [0,1]')
    if any(x < 0 for x in (s.enforcement_cost, s.capture_cost, s.sanction)):
        raise ValueError('costs and sanction must be nonnegative')
    enforce = s.enforcement_private_benefit > s.enforcement_cost + s.capture_cost
    b_exploit = s.successor_exploit_self - (s.detection * s.sanction if enforce else 0)
    b_honors = s.successor_honor_self > b_exploit
    a_future = s.incumbent_future_if_honor if b_honors else s.incumbent_future_if_exploited
    a_preserve = s.present_preserve + discount * a_future
    choice = 'preserve' if a_preserve > s.preemptive_payoff else 'preempt'
    return {
        'discount': str(discount),
        'credible_enforcement': enforce,
        'successor_action': 'honor' if b_honors else 'exploit',
        'incumbent_action': choice,
        'incumbent_preserve_payoff': float(a_preserve),
        'incumbent_preempt_payoff': float(s.preemptive_payoff),
        'victim_welfare': None,
        'all_party_viability': None,
        'nominal_pledge': s.nominal_pledge,
    }


def majority_core_three(grand_value: F, pair_value: F = F(1)) -> dict:
    """Exact 3-person symmetric TU majority game with singleton values 0.

    Any pair can guarantee 'pair_value'; the grand coalition can distribute
    only 'grand_value'. The core exists iff grand_value >= 3*pair_value/2.
    This requires transferable utility and feasible side payments.
    """
    if pair_value < 0 or grand_value < 0:
        raise ValueError('toy characteristic function values must be nonnegative')
    required = F(3, 2) * pair_value
    feasible = grand_value >= required
    witness = [str(grand_value / 3)] * 3 if feasible else None
    return {
        'grand_value': str(grand_value),
        'pair_value': str(pair_value),
        'core_nonempty': feasible,
        'symmetric_allocation_if_core_exists': witness,
        'additional_surplus_required_if_empty': str(max(F(0), required-grand_value)),
        'third_party_real_welfare': None,
    }


def dynamic_scenarios() -> dict:
    base = TransitionScenario()
    credible = TransitionScenario(enforcement_private_benefit=F(3))
    captured = TransitionScenario(enforcement_private_benefit=F(3), capture_cost=F(2))
    low_detection = TransitionScenario(enforcement_private_benefit=F(3), detection=F(1, 2))
    horizons = (F(0), F(1, 4), F(1, 3), F(1, 2), F(1))
    return {
        'no_credible_enforcement': [backward_power_shift(base, d) for d in horizons],
        'credible_enforcement': [backward_power_shift(credible, d) for d in horizons],
        'captured_enforcement': backward_power_shift(captured, F(1)),
        'low_detection': backward_power_shift(low_detection, F(1)),
        'coalition_core': [majority_core_three(v) for v in (F(1), F(5, 4), F(3, 2), F(2))],
        'empirical_claim': False,
        'prior_art_not_project_novelty': [
            'Powell (2004,2006) dynamic commitment problem',
            'Bondareva (1963) and Shapley (1967) core nonemptiness',
        ],
    }


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
        self.assertIsNone(results['credible_enforcement']['victim_viability_in_toy'])
        self.assertIsNone(results['no_enforcement']['victim_viability_in_toy'])

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

    def test_pledge_does_not_change_payoffs(self):
        no_pledge, pledge = map(solve, scenarios()[:2])
        self.assertFalse(no_pledge['pledge_signed'])
        self.assertTrue(pledge['pledge_signed'])
        for key in ('extract_payoff', 'preserve_payoff', 'dominant_choice'):
            self.assertEqual(no_pledge[key], pledge[key])

    def test_choice_is_not_observation_of_viability(self):
        # Both extraction and preservation leave unobserved welfare unknown.
        for scenario in (scenarios()[0], scenarios()[2], scenarios()[5]):
            r = solve(scenario)
            self.assertIsNone(r['victim_viability_in_toy'])
            self.assertIsNone(r['all_party_viability_in_toy'])
        # Even explicit stipulated victim and outsider safety cannot prove
        # safety of the dominant actor and enforcer; the model omits them.
        s = scenarios()[5]
        safe = Scenario(**(asdict(s) | {'victim_status': 'stipulated_safe',
                                      'outsider_status': 'stipulated_safe'}))
        self.assertIsNone(solve(safe)['all_party_viability_in_toy'])

    def test_stipulated_harm_even_if_preserved(self):
        s = scenarios()[5]  # dominant actor chooses preserve
        harmed = Scenario(**(asdict(s) | {'victim_status': 'stipulated_harm'}))
        result = solve(harmed)
        self.assertEqual(result['dominant_choice'], 'preserve')
        self.assertFalse(result['victim_viability_in_toy'])
        self.assertFalse(result['all_party_viability_in_toy'])


    def test_horizon_can_reverse_preservation(self):
        rows = dynamic_scenarios()['no_credible_enforcement']
        self.assertEqual([r['incumbent_action'] for r in rows],
                         ['preserve', 'preserve', 'preempt', 'preempt', 'preempt'])
        self.assertEqual(rows[2]['incumbent_preserve_payoff'], 4.0)
        self.assertIsNone(rows[4]['victim_welfare'])

    def test_credible_future_commitment_changes_prior_choice(self):
        rows = dynamic_scenarios()['credible_enforcement']
        self.assertTrue(all(r['incumbent_action'] == 'preserve' for r in rows))
        self.assertTrue(all(r['successor_action'] == 'honor' for r in rows))

    def test_pledge_flag_without_costly_commitment_is_inert(self):
        s = TransitionScenario()
        baseline = backward_power_shift(s, F(1))
        pledge = backward_power_shift(TransitionScenario(**(asdict(s) | {'nominal_pledge': True})), F(1))
        self.assertEqual(baseline['incumbent_action'], pledge['incumbent_action'])
        self.assertEqual(baseline['successor_action'], pledge['successor_action'])

    def test_future_enforcement_capture_restores_preemption(self):
        r = dynamic_scenarios()['captured_enforcement']
        self.assertFalse(r['credible_enforcement'])
        self.assertEqual(r['successor_action'], 'exploit')
        self.assertEqual(r['incumbent_action'], 'preempt')

    def test_future_low_detection_fails(self):
        r = dynamic_scenarios()['low_detection']
        self.assertTrue(r['credible_enforcement'])
        self.assertEqual(r['successor_action'], 'exploit')
        self.assertEqual(r['incumbent_action'], 'preempt')

    def test_three_actor_coalitional_core_threshold(self):
        rows = dynamic_scenarios()['coalition_core']
        self.assertEqual([r['core_nonempty'] for r in rows],
                         [False, False, True, True])
        self.assertEqual(rows[0]['additional_surplus_required_if_empty'], '1/2')
        self.assertEqual(rows[2]['symmetric_allocation_if_core_exists'],
                         ['1/2', '1/2', '1/2'])

    def test_positive_sum_does_not_guarantee_coalition_stability(self):
        r = majority_core_three(F(1), F(1))
        self.assertFalse(r['core_nonempty'])
        self.assertIsNone(r['third_party_real_welfare'])

    def test_discount_increase_may_reduce_preservation_payoff(self):
        base = TransitionScenario()
        short = backward_power_shift(base, F(0))
        long = backward_power_shift(base, F(1))
        self.assertGreater(short['incumbent_preserve_payoff'],
                           long['incumbent_preserve_payoff'])

    def test_dynamic_domain_guards(self):
        base = TransitionScenario()
        with self.assertRaises(ValueError):
            backward_power_shift(base, F(2))
        with self.assertRaises(ValueError):
            backward_power_shift(TransitionScenario(detection=F(-1, 2)), F(1))
        with self.assertRaises(ValueError):
            majority_core_three(F(-1))

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
                      'results': list(map(solve, scenarios())),
                      'exploratory_power_shift_and_coalition': dynamic_scenarios()}, indent=2, ensure_ascii=False))

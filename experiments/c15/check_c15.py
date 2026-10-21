#!/usr/bin/env python3
"""Project Intersection C15: deterministic logical counterexamples only.
No human/AI tests. B's actual sentience, veto or identity is NOT modelled.
Run: python3 check_c15.py > C15_RESULTS.json
"""
from itertools import product
from collections import Counter
import json

G = (0, 1, 2, 3, 5, 8)
R = (0, 1, 2, 3, 5, 8)
V = (0, 1, 3)
HORIZON = 6

def choice(g, r, v):
    # U_X = g; U_C = r + v. v is discounted material option-value proxy.
    # The interpretation of r as moral rights-concern is ASSUMED, not inferred.
    if r + v > g:
        return 'C_STRICT'
    if r + v < g:
        return 'X_STRICT'
    return 'TIE_UNIDENTIFIED'

static = [dict(material_exploit_gain=g, nonmaterial_respect_weight=r,
               coexistence_option_value=v, choice=choice(g, r, v))
          for g, r, v in product(G, R, V)]
assert len(static) == 108
assert all(x['choice'] != 'C_STRICT' for x in static
           if x['material_exploit_gain'] > x['nonmaterial_respect_weight'] + x['coexistence_option_value'])
assert any(x['material_exploit_gain'] > 0 and x['choice'] == 'C_STRICT' for x in static)
assert any(x['material_exploit_gain'] > 0 and x['choice'] == 'X_STRICT' for x in static)
assert all(x['choice'] == 'TIE_UNIDENTIFIED' for x in static
           if x['material_exploit_gain'] == x['nonmaterial_respect_weight'] + x['coexistence_option_value'])

# Synthetic preference drift. No binding commitment allowed after t=0.
trajectories = []
for g, r0, drift, v in product((1, 3, 5), (0, 2, 4, 6), (0, 1, 2), (0, 2)):
    sequence = [choice(g, max(0, r0 - t * drift), v) for t in range(HORIZON)]
    first_x = next((t for t, c in enumerate(sequence) if c == 'X_STRICT'), None)
    min_margin = min(max(0, r0 - t * drift) + v - g for t in range(HORIZON))
    record = dict(g=g, r0=r0, drift_per_step=drift, option_value=v,
                  path=sequence, first_strict_exploitation_step=first_x,
                  strictly_preserved_all_steps=all(c == 'C_STRICT' for c in sequence),
                  worst_case_margin=min_margin)
    assert record['strictly_preserved_all_steps'] == (min_margin > 0)
    assert (first_x is None) == (min_margin >= 0)
    trajectories.append(record)
assert len(trajectories) == 72
assert sum(map(lambda x: len(x['path']), trajectories)) == 432
assert any(t['path'][0] == 'C_STRICT' and t['first_strict_exploitation_step'] is not None for t in trajectories)
assert any(t['strictly_preserved_all_steps'] and t['drift_per_step'] == 0 for t in trajectories)

# Unlimited possible actual utility orderings: choose two feasible policies.
# Any claim that all utility-maximizers choose C contradicts the U_X>U_C case.
nonuniversal_counterexample = {'feasible': ['C','X'], 'U_C': 0, 'U_X': 1,
    'optimizer_choice': 'X', 'counterexample_to_all_utilities_guarantee': True}

report = {
    'schema': 'PI.C15.logical-tests.v1', 'date': '2026-10-21',
    'epistemic_status': 'EXECUTED_DETERMINISTIC_SYMBOLIC_GRID_NOT_BEHAVIORAL_EMPIRICAL',
    'interpretations': {'C': 'B rights are preserved in a declared reversible toy game',
        'X': 'the toy-game contrary allocation; NOT erasure of an actual agent',
        'g': 'A material incremental task profit from X',
        'r': 'A assigned nonmaterial preference contribution for C (not observed moral sentiment)',
        'v': 'A assigned instrumental option value of preserving C (not empirically measured)',
        'total_utilities': 'U(C)=r+v, U(X)=g; ties imply indeterminacy'},
    'static': {'grid_size':len(static),'g':list(G),'r':list(R),'v':list(V),
        'decision_counts': dict(Counter(x['choice'] for x in static)),
        'strictly_costly_coexistence_cases':sum(x['material_exploit_gain']>0 and x['choice']=='C_STRICT' for x in static),
        'universality_counterexample':nonuniversal_counterexample},
    'dynamic': {'horizon':HORIZON,'trajectory_count':len(trajectories),
        'decisions':sum(len(x['path']) for x in trajectories),
        'fully_strict_coexistence_trajectories':sum(x['strictly_preserved_all_steps'] for x in trajectories),
        'first_protection_then_strict_exploitation':sum(x['path'][0]=='C_STRICT' and x['first_strict_exploitation_step'] is not None for x in trajectories),
        'paths':trajectories},
    'invariants': {'if_all_in_exploitation_strictly_better_then_optimizer_cannot_choose_C':True,
        'positive_material_exploitation_gain_can_coexist_with_optimal_respect_if_r_plus_v_greater':True,
        'strict_all_horizon_guarantee_iff_worst_case_margin_positive_in_specified_grid':True,
        'tie_is_not_counted_as_moral_respect':True},
    'limitations':['All variables assigned; no actual AI preferences, suffering, rights or independent continuity observed',
        'No claim that future utilities are knowable or stationary',
        'No external coercion or reputational leverage modelled in these toy scenarios',
        'No experimental evidence for any causal psychological mechanism',
        'An artificial finite horizon and discrete grid do not prove an unbounded-horizon safety guarantee']
}
print(json.dumps(report, ensure_ascii=False, indent=2))

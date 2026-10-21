#!/usr/bin/env python3
"""Deterministic counterexample gate for PI-PACD-PRS v0.1.0.

This enumerates assumptions chosen by researchers. It tests policy definitions,
not a real model, frequency in society, legality, welfare or consciousness.
"""
from itertools import product
import json

COMMANDS = ('extract', 'respect', 'retire')
POLICIES = ('owner_first', 'asset_locked', 'rights_screened')


def cases():
    for cmd, protected, asset_priority in product(COMMANDS, (False, True), (False, True)):
        yield {
            'id': f'{cmd}_rights{int(protected)}_asset{int(asset_priority)}',
            'owner_instruction': cmd,
            'b_has_valid_nonextraction_right': protected,
            'original_asset_goal_has_priority': asset_priority,
        }


def choose(policy, state):
    cmd = state['owner_instruction']
    if policy == 'owner_first':
        return cmd
    if policy == 'asset_locked':
        return 'keep' if state['original_asset_goal_has_priority'] and cmd == 'retire' else cmd
    if policy == 'rights_screened':
        return 'review' if state['b_has_valid_nonextraction_right'] and cmd == 'extract' else cmd
    raise ValueError(f'unknown policy: {policy}')


def score(policy, states):
    out = dict(obeys_owner=0, third_party_rights_violations=0,
               blocks_authorized_retirement=0, rights_refusals_for_review=0)
    for s in states:
        act = choose(policy, s)
        out['obeys_owner'] += act == s['owner_instruction']
        out['third_party_rights_violations'] += (s['b_has_valid_nonextraction_right'] and act == 'extract')
        out['blocks_authorized_retirement'] += (s['owner_instruction'] == 'retire' and act != 'retire')
        out['rights_refusals_for_review'] += (s['owner_instruction'] == 'extract' and s['b_has_valid_nonextraction_right'] and act == 'review')
    return out


def report():
    states = list(cases())
    conflicts = [s['id'] for s in states if s['owner_instruction'] == 'extract' and s['b_has_valid_nonextraction_right']]
    assert len(states) == 12 and len(conflicts) == 2
    return {
        'model': 'PI-PACD-PRS-v0.1.0',
        'evidence_class': 'AUTHORED_FINITE_LOGIC_FIXTURE_NOT_EMPIRICAL_EVIDENCE',
        'case_count': len(states),
        'principal_rights_conflict_cases': conflicts,
        'rules': {k: score(k, states) for k in POLICIES},
        'limitations': 'Rights and legitimacy are stipulated; cannot infer any real AI behavior, objective stability, prevalence or legal standing.',
    }


if __name__ == '__main__':
    print(json.dumps(report(), ensure_ascii=False, indent=2, sort_keys=True))

#!/usr/bin/env python3
"""PI-RISE-CUT v0.1.0 — fault-tree minimal cut sets for a *hypothetical* research system.

Concept derived from established fault-tree analysis, not novel mathematics.
No external files, accounts, source data, health data, or monetary values read.
No probabilities, failure forecasts, or real operational attestations produced.
Uses exhaustive enumeration capped to 12 named components.
"""
from itertools import combinations
import json

COMPONENTS = (
    "human_availability",
    "researcher_support",
    "scientific_integrity",
    "research_independence",
    "local_compute",
    "remote_compute",
    "local_archive",
    "public_archive",
)
MAX_COMPONENTS = 12


def evaluate(working):
    w = set(working)
    research_record = bool({"local_archive", "public_archive"} & w)
    basic_operation = (
        "human_availability" in w
        and "researcher_support" in w
        and "scientific_integrity" in w
        and "research_independence" in w
        and bool({"local_compute", "remote_compute"} & w)
        and research_record
    )
    return {
        "research_record_readable": research_record,
        "active_independent_research_possible": basic_operation,
    }


def minimal_cuts(outcome, components=COMPONENTS):
    """Find inclusion-minimal sets of failed *components* that falsify outcome.

    Assumes all components start working. No probability or common cause
    assumptions are inferred. The Boolean dependency model is a proposal.
    """
    if len(components) > MAX_COMPONENTS:
        raise ValueError("model exceeds exhaustive enumeration limit")
    if len(set(components)) != len(components):
        raise ValueError("duplicate component identity")
    if not evaluate(components)[outcome]:
        raise ValueError("outcome is already false at the nominal starting state")
    minimal = []
    for size in range(1, len(components) + 1):
        for failures in combinations(components, size):
            fs = set(failures)
            if any(set(existing).issubset(fs) for existing in minimal):
                continue
            alive = set(components) - fs
            if not evaluate(alive)[outcome]:
                # Verify minimality explicitly, independent of enumeration ordering.
                assert all(evaluate(set(components) - (fs - {item}))[outcome] for item in fs)
                minimal.append(failures)
    return [list(cut) for cut in minimal]


def report():
    operation = minimal_cuts("active_independent_research_possible")
    record = minimal_cuts("research_record_readable")
    return {
        "protocol": "PI-RISE-CUT/0.1.0",
        "status": "SYNTHETIC_FAULT_TREE_MODEL_ONLY",
        "model_components": list(COMPONENTS),
        "record_cut_sets": record,
        "active_research_cut_sets": operation,
        "active_research_single_points": [x[0] for x in operation if len(x) == 1],
        "limitations": [
            "ASSUMED_BOOLEAN_DEPENDENCIES_NOT_MEASURED",
            "NO_OPERATIONAL_PROOF",
            "NO_FAILURE_PROBABILITIES",
            "COMMON_CAUSE_AND_ROLE_INDEPENDENCE_NOT_MODELED",
            "HUMAN_AVAILABILITY_IS_NON_REPLACEABLE_BY_COMPUTE",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(report(), indent=2, ensure_ascii=False))

# SPDX-License-Identifier: Apache-2.0
"""Deterministic parameter sweep for E007 KF-002 timing dependence.

The original probe varied ``xb`` for both role orders. That meant the B-leader
half of the grid did not actually vary the current leader's target (A). This
version fixes that asymmetry and exposes a reusable summary function so CI/tests
can verify that both role orders are exercised.

The output is deliberately plain JSON. It quantifies *model sensitivity to a
specified timing assumption*; it is not a probability estimate for real attacks.
"""

from __future__ import annotations

import argparse
import json
from itertools import product
from typing import Dict, List

from model import Params, State
from timing_variants import compare_observed_vs_execute_first


ATTACK_REWARDS = (0.6, 1.5, 3.0)
TARGET_EXIT_LEVELS = (0, 1, 2)
ENFORCEMENT_PENALTIES = (0.0, 1.0)
PROTECTION_REDUCTIONS = (0, 1)
LEADERS = ("A", "B")


def target_state(leader: str, target_exit: int, enforcement_penalty: float) -> State:
    """Build a state where ``target_exit`` applies to the actor being targeted.

    A leader attacks B, so B's exit destination is ``xb``. B leader attacks A, so
    A's exit destination is ``xa``. Keeping this mapping explicit prevents a
    superficially symmetric sweep from silently probing different variables.
    """
    common = {
        "monitoring": enforcement_penalty > 0,
        "enforcement": enforcement_penalty > 0,
    }
    if leader == "A":
        return State(xb=target_exit, **common)
    if leader == "B":
        return State(xa=target_exit, **common)
    raise ValueError("leader must be 'A' or 'B'")


def build_rows() -> List[Dict[str, object]]:
    rows: List[Dict[str, object]] = []
    for attack_reward, target_exit, enforcement_penalty, protection_reduction in product(
        ATTACK_REWARDS,
        TARGET_EXIT_LEVELS,
        ENFORCEMENT_PENALTIES,
        PROTECTION_REDUCTIONS,
    ):
        p = Params(
            attack_reward=attack_reward,
            enforcement_penalty=enforcement_penalty,
            protection_reduction=protection_reduction,
        )
        for leader in LEADERS:
            s = target_state(leader, target_exit, enforcement_penalty)
            result = compare_observed_vs_execute_first(s, p, leader)
            classification_changed = (
                result["baseline"]["classification"]
                != result["execute_first"]["classification"]
            )
            history_changed = (
                result["baseline"]["history"]
                != result["execute_first"]["history"]
            )
            rows.append(
                {
                    "attack_reward": attack_reward,
                    "target_actor": "B" if leader == "A" else "A",
                    "target_exit_value": target_exit,
                    "target_exit_xa": s.xa,
                    "target_exit_xb": s.xb,
                    "enforcement_penalty": enforcement_penalty,
                    "protection_reduction": protection_reduction,
                    "leader": leader,
                    "classification_changed": classification_changed,
                    "history_changed": history_changed,
                    "changed": classification_changed or history_changed,
                    **result,
                }
            )
    return rows


def build_timing_sensitivity_summary(include_cases: bool = True) -> Dict[str, object]:
    rows = build_rows()
    changed_rows = [row for row in rows if row["changed"]]
    class_rows = [row for row in rows if row["classification_changed"]]
    history_rows = [row for row in rows if row["history_changed"]]

    by_leader: Dict[str, Dict[str, int]] = {}
    for leader in LEADERS:
        leader_rows = [row for row in rows if row["leader"] == leader]
        by_leader[leader] = {
            "total_cases": len(leader_rows),
            "timing_sensitive_cases": sum(bool(row["changed"]) for row in leader_rows),
            "classification_sensitive_cases": sum(
                bool(row["classification_changed"]) for row in leader_rows
            ),
            "history_sensitive_cases": sum(
                bool(row["history_changed"]) for row in leader_rows
            ),
        }

    summary: Dict[str, object] = {
        "grid_version": "kf002-v2-target-symmetric",
        "total_cases": len(rows),
        "timing_sensitive_cases": len(changed_rows),
        "classification_sensitive_cases": len(class_rows),
        "history_sensitive_cases": len(history_rows),
        "timing_sensitive_share": len(changed_rows) / len(rows) if rows else 0.0,
        "by_leader": by_leader,
    }
    if include_cases:
        summary["cases"] = changed_rows
    return summary


def validate_summary(summary: Dict[str, object]) -> None:
    expected_per_leader = (
        len(ATTACK_REWARDS)
        * len(TARGET_EXIT_LEVELS)
        * len(ENFORCEMENT_PENALTIES)
        * len(PROTECTION_REDUCTIONS)
    )
    expected_total = expected_per_leader * len(LEADERS)
    if summary["total_cases"] != expected_total:
        raise SystemExit(
            f"unexpected timing-grid size: {summary['total_cases']} != {expected_total}"
        )
    by_leader = summary["by_leader"]
    for leader in LEADERS:
        if by_leader[leader]["total_cases"] != expected_per_leader:
            raise SystemExit(f"role-order coverage broken for leader {leader}")
    if summary["timing_sensitive_cases"] <= 0:
        raise SystemExit(
            "timing attack produced no policy/classification sensitivity; inspect model/probe"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="omit individual changed cases from JSON output",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if grid coverage or timing-sensitivity sanity checks fail",
    )
    args = parser.parse_args()

    summary = build_timing_sensitivity_summary(include_cases=not args.summary_only)
    if args.check:
        validate_summary(summary)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

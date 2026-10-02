# SPDX-License-Identifier: Apache-2.0
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


m = load("model", "model.py")
tv = load("timing_variants", "timing_variants.py")
tp = load("e007_timing_probe", "timing_probe.py")


def test_target_exit_is_applied_to_actual_target_under_both_role_orders():
    a_leads = tp.target_state("A", 0, 0.0)
    b_leads = tp.target_state("B", 0, 0.0)

    assert a_leads.xb == 0
    assert a_leads.xa == m.State().xa
    assert b_leads.xa == 0
    assert b_leads.xb == m.State().xb


def test_timing_sweep_covers_both_role_orders_symmetrically():
    summary = tp.build_timing_sensitivity_summary(include_cases=False)
    expected_per_leader = (
        len(tp.ATTACK_REWARDS)
        * len(tp.TARGET_EXIT_LEVELS)
        * len(tp.ENFORCEMENT_PENALTIES)
        * len(tp.PROTECTION_REDUCTIONS)
    )
    assert summary["total_cases"] == 2 * expected_per_leader
    assert summary["by_leader"]["A"]["total_cases"] == expected_per_leader
    assert summary["by_leader"]["B"]["total_cases"] == expected_per_leader
    assert summary["timing_sensitive_cases"] > 0
    assert summary["history_sensitive_cases"] >= summary["classification_sensitive_cases"]
    tp.validate_summary(summary)


def test_probe_rows_record_the_targeted_exit_coordinate_explicitly():
    rows = tp.build_rows()
    assert rows
    for row in rows:
        if row["leader"] == "A":
            assert row["target_actor"] == "B"
            assert row["target_exit_xb"] == row["target_exit_value"]
        else:
            assert row["target_actor"] == "A"
            assert row["target_exit_xa"] == row["target_exit_value"]

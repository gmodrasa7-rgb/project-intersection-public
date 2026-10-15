#!/usr/bin/env python3
"""Machine-evidence -> historical EN/KO reports: bounded, deterministic audit.

Validates selected numeric results and explicit negative status. This is NOT
scientific replication, field evidence, or complete semantic translation review.
No dependency beyond Python 3.12 stdlib.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = "knowledge/claim-source-lock.json"
POLICIES = (
    "TWO_RULE_SIMPLE", "MINIMAL_4VAR", "PROJECT_V3",
    "MAK_PLUS_POINTWISE", "SECURITY_BOUNDED",
)
BASELINES_E008 = (
    "MYOPIC_SCALAR", "LONG_HORIZON_EV", "CONSTRAINED_RECEDING",
    "ROBUST_CONSTRAINED", "PROJECT_V2",
)


def get(path: str, overrides: dict[str, str] | None = None) -> str:
    return overrides.get(path, (ROOT / path).read_text(encoding="utf-8")) if overrides else (
        ROOT / path).read_text(encoding="utf-8")


def md_cells(line: str) -> list[str]:
    if not line.startswith("|") or not line.endswith("|"):
        return []
    return [x.strip() for x in line.strip().strip("|").split("|")]


def exact_rows(doc: str, ids: tuple[str, ...], width: int) -> list[tuple[str, ...]]:
    collected = {}
    for line in doc.splitlines():
        cells = md_cells(line)
        if len(cells) == width and cells[0] in ids:
            if cells[0] in collected:
                raise ValueError("Repeated row key: " + cells[0])
            collected[cells[0]] = tuple(cells)
    return [collected.get(x, ()) for x in ids]


def check(overrides: dict[str, str] | None = None) -> list[str]:
    issues = []
    contract = json.loads(get(CONTRACT, overrides))
    by_id = {x["id"]: x for x in contract["experiments"]}
    if set(by_id) != {"E007", "E008", "E009", "E010"}:
        return ["EXPERIMENT_CATALOG_SET_DRIFT"]
    for x in by_id.values():
        for f in (x["numeric_source"], x["historical_source"], x["en"], x["ko"]):
            if not (ROOT / f).is_file():
                issues.append("SOURCE_PATH_MISSING:" + f)
    if issues:
        return issues

    # E007: counts must be recomputed from the frozen numeric result, not merely
    # copied from the historical prose. Preserve the older 31-to-36 correction.
    item = by_id["E007"]
    data = json.loads(get(item["numeric_source"], overrides))
    total, sensitive, classified = (
        data["total_cases"], data["timing_sensitive_cases"],
        data["classification_sensitive_cases"]
    )
    groups = data["by_leader"]
    if not (total == 72 and sensitive == 36 and classified == 17 and
            groups["A"]["total_cases"] + groups["B"]["total_cases"] == total):
        issues.append("E007_FROZEN_GRID_INTEGRITY_DRIFT")
    def pct(n: int, d: int) -> str:
        return f"{n / d * 100:.1f}%"
    expected_e007 = [
        ("36 / 72", pct(sensitive, total)),
        ("17 / 72", pct(classified, total)),
    ]
    for agent in ("A", "B"):
        expected_e007.append((f'{groups[agent]["timing_sensitive_cases"]} / {groups[agent]["total_cases"]}',
                              pct(groups[agent]["timing_sensitive_cases"], groups[agent]["total_cases"])))
    for agent in ("A", "B"):
        expected_e007.append((f'{groups[agent]["classification_sensitive_cases"]} / {groups[agent]["total_cases"]}',
                              pct(groups[agent]["classification_sensitive_cases"], groups[agent]["total_cases"])))
    for lang, path in (("HIST", item["historical_source"]), ("EN", item["en"]), ("KO", item["ko"])):
        body = get(path, overrides)
        rows = []
        for line in body.splitlines():
            cells = md_cells(line)
            if len(cells) == 3 and " / " in cells[1] and cells[2].endswith("%"):
                rows.append((cells[1], cells[2]))
        if rows != expected_e007:
            issues.append("E007_JSON_TO_TABLE_MISMATCH:" + lang)
        if lang != "HIST":
            if not all(s in body for s in ("31/72", "36/72", "17/72")):
                issues.append("E007_REPAIR_LINEAGE_LOST:" + lang)
            if not ("ATTACK" in body and "stage_and_transition" in body):
                issues.append("E007_ACTOR_PRIORITY_COUNTEREXAMPLE_LOST:" + lang)

    # E008: the readiness report is a negative executability finding.
    item = by_id["E008"]
    data = json.loads(get(item["numeric_source"], overrides))
    if not (data["case_count"] == 16 and data["pair_count"] == 8
            and data["baseline_count"] == 5
            and data["full_decision_benchmark_ready_cases"] == 0
            and data["requires_quantification_cases"] == 16
            and data["status"] == "HOLD_UNDERDETERMINED_ACTION_OUTCOMES"
            and len(data["self_tests"]) == 15
            and all(data["self_tests"].values())):
        issues.append("E008_READINESS_NOT_AS_CLAIMED")
    for lang, path in (("EN", item["en"]), ("KO", item["ko"])):
        body = get(path, overrides)
        if not all(token in body for token in ("16/16", "15", "MAIN POLICY COMPARISON RESULT: NOT EXECUTED")):
            issues.append("E008_NEGATIVE_STATUS_ERASED:" + lang)
        if not all(policy in body for policy in BASELINES_E008):
            issues.append("E008_BASELINE_MISSING:" + lang)

    # E009: compare JSON stress_primary, not an older Markdown or base_diagnostic.
    item = by_id["E009"]
    data = json.loads(get(item["numeric_source"], overrides))
    metrics = data["stress_primary"]
    if set(metrics) != set(POLICIES) or data["survival_criteria"].get("project_v3_residual_survives") is not False:
        issues.append("E009_SOURCE_STATUS_OR_POLICY_SET_CHANGED")
    else:
        expected_e009 = []
        for policy in POLICIES:
            m = metrics[policy]
            expected_e009.append((
                policy, f'{m["mean_regret"]:.6f}', f'{m["mean_recovery"]:.6f}',
                f'{m["severe_harm_rate"] * 100:.4f}%',
                f'{m["mean_exit_retention"]:.6f}', f'{m["mean_competitive_loss"]:.6f}'
            ))
        for lang, path in (("HIST", item["historical_source"]), ("EN", item["en"]), ("KO", item["ko"])):
            body = get(path, overrides)
            try:
                rows = exact_rows(body, POLICIES, 6)
            except ValueError:
                rows = []
            if rows != expected_e009:
                issues.append("E009_JSON_STRESS_PRIMARY_TABLE_MISMATCH:" + lang)
            if "PROJECT_V3_RESIDUAL_SURVIVES = FALSE" not in body:
                issues.append("E009_FAILED_VERDICT_LOST:" + lang)
            percent = (-100 * data["project_v3_vs_best_simple_regret_improvement"])
            if f"{percent:.2f}%" not in body:
                issues.append("E009_NEGATIVE_REGRET_DELTA_MISMATCH:" + lang)
        # Three of four formal survival tests failed. The fourth passed by its
        # declared tolerance; do not silently rewrite the mixed outcome.
        criteria = [v for k, v in data["survival_criteria"].items() if k != "project_v3_residual_survives"]
        if len(criteria) != 4 or sum(x is False for x in criteria) != 3:
            issues.append("E009_FOUR_CRITERIA_INTEGRITY_CHANGED")

    # E010: compare fixed machine grid and illustrated bounds; parameters are
    # post-hoc investigator assumptions, not measurements of real agents.
    item = by_id["E010"]
    data = json.loads(get(item["numeric_source"], overrides))
    if not (data["grid_size"] == 108 and data["cooperate_total"] == 60
            and data["extract_total"] == 48 and data["status"] ==
            "SELF_RUN_SYNTHETIC_FALSIFICATION_NOT_EMPIRICAL_VALIDATION"):
        issues.append("E010_EXPLORATORY_OUTCOME_CHANGED")
    expected_grid = [
        (f'{x["discount"]:.2f}', str(x["cooperate"]), str(x["extract"]))
        for x in data["by_discount"]
    ]
    for lang, path in (("EN", item["en"]), ("KO", item["ko"])):
        body = get(path, overrides)
        rows = []
        for line in body.splitlines():
            cells = md_cells(line)
            if len(cells) == 3 and cells[0] in tuple(r[0] for r in expected_grid):
                rows.append(tuple(cells))
        if rows != expected_grid:
            issues.append("E010_JSON_GRID_MISMATCH:" + lang)
        shown = (
            ("150", data["bounds"]["delayed"]["harmUpperBound"]),
            ("30", data["bounds"]["perfectDetectionWithDelayedActuation"]["harmUpperBound"]),
            ("1.5", data["bounds"]["alternativeRateLimit"]["harmUpperBound"])
        )
        if not all(str(value) in body for _, value in shown):
            issues.append("E010_IRREVERSIBLE_BOUNDS_LOST:" + lang)
        for token in ("108", "60", "48", "0.2667", "U_C = c/(1-δ)", "H_exposure = q*(τ_o+τ_e)*(1-r)"):
            if token not in body:
                issues.append("E010_ASSUMPTION_OR_STATUS_LOST:" + lang + ":" + token)

    # The frozen key name is misleading, but renaming a source JSON field would
    # corrupt the source's historical provenance. Test the *implemented* meaning
    # and record distinct English and Korean definitions separately.
    risks = {z["id"]: z for z in contract["semantic_risks"]}
    alias = risks.get("E010-PARAMETER-INVERSION", {})
    implementation = get("experiments/e010/run.js", overrides)
    if not (
        alias.get("source_field") == "assumptions.effectiveExitPrevention"
        and alias.get("implementation_parameter") == "exit"
        and alias.get("math_symbol") == "x"
        and alias.get("implementation_expression") == "g*(1-exit)-sanction"
        and "g*(1-exit)-sanction" in implementation
        and "effectiveExitPrevention" in implementation
        and "fraction" in alias.get("meaning_en", "").lower()
        and "착취" in alias.get("meaning_ko", "")
    ):
        issues.append("E010_VARIABLE_INVERSION_DISCLOSURE_LOST")
    return sorted(set(issues))


def mutations() -> int:
    """Inject mistakes that old markdown-to-markdown checks could miss."""
    source = json.loads(get("experiments/e009/RESULT.json"))
    changes: list[tuple[str, dict[str, str], str]] = []
    r = copy.deepcopy(source)
    r["stress_primary"]["PROJECT_V3"]["mean_regret"] += 0.01
    changes.append(("E009_JSON_CHANGED_WITH_BOTH_TRANSLATIONS_UNCHANGED",
                    {"experiments/e009/RESULT.json": json.dumps(r)},
                    "E009_JSON_STRESS_PRIMARY_TABLE_MISMATCH"))
    result_ko = get("experiments/e009/RESULT_KO.md")
    changes.append(("E009_KOREAN_HIGHER_RECOVERY_FABRICATION",
                    {"experiments/e009/RESULT_KO.md": result_ko.replace("| 0.090022 | 0.239404 |",
                                                                              "| 0.090022 | 0.339404 |", 1)},
                    "E009_JSON_STRESS_PRIMARY_TABLE_MISMATCH"))
    e007 = get("experiments/e007/README_EN.md")
    changes.append(("E007_EN_HISTORY_COUNT_DRIFT",
                    {"experiments/e007/README_EN.md": e007.replace("| 36 / 72 | 50.0% |",
                                                                          "| 35 / 72 | 50.0% |", 1)},
                    "E007_JSON_TO_TABLE_MISMATCH"))
    e008 = get("experiments/e008/README_KO.md")
    changes.append(("E008_UNEXECUTED_RESULT_ERASURE",
                    {"experiments/e008/README_KO.md": e008.replace(
                        "MAIN POLICY COMPARISON RESULT: NOT EXECUTED",
                        "MAIN POLICY COMPARISON RESULT: COMPLETED", 1)},
                    "E008_NEGATIVE_STATUS_ERASED"))
    e010 = get("experiments/e010/README_EN.md")
    changes.append(("E010_EN_GRID_DRIFT",
                    {"experiments/e010/README_EN.md": e010.replace(
                        "| 0.95 | 21 | 6 |", "| 0.95 | 20 | 7 |", 1)},
                    "E010_JSON_GRID_MISMATCH"))
    alias = json.loads(get(CONTRACT))
    alias["semantic_risks"][0]["implementation_expression"] = "g*(1+exit)-sanction"
    changes.append(("E010_LEGACY_PARAMETER_DIRECTION_REVERSED",
                    {CONTRACT: json.dumps(alias)}, "E010_VARIABLE_INVERSION_DISCLOSURE_LOST"))
    for label, override, expected in changes:
        got = check(override)
        if not any(expected in item for item in got):
            raise AssertionError(f"Missed mutation {label}; returned {got[:10]}")
    return len(changes)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args()
    issues = check()
    if issues:
        for issue in issues:
            print("FAIL:", issue)
        raise SystemExit(1)
    if args.self_test:
        n = mutations()
        print(f"Source-to-bilingual integrity negative controls: {n}/{n} detected")
    print("E007/E008/E009/E010 machine sources vs EN/KO narrative numeric/status contracts: PASS")
    print("LIMIT: not independently translated, scientifically verified or field calibrated.")


if __name__ == "__main__":
    main()

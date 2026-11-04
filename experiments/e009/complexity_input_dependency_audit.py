#!/usr/bin/env python3
"""Post-hoc E009 complexity-count ambiguity audit (same project lineage).

Parses frozen policy code; does not change pre-registered scores or evidence class.
AST references are an *upper bound* on behavioral feature dependence, not a
causal feature-importance estimate. This is a conditional pricing sensitivity.
"""
import ast
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "benchmark.py"
RESULT = ROOT / "RESULT.json"
EXPECTED_USED = {
    "MAK_PLUS_POINTWISE": {"harm_action", "harm_inaction"},
    "TWO_RULE_SIMPLE": {"harm_action", "harm_inaction"},
    "SECURITY_BOUNDED": {"harm_action", "harm_inaction", "reversibility", "ENF", "ID", "OV"},
    "MINIMAL_4VAR": {"harm_action", "harm_inaction", "reversibility", "ENF", "ID", "OV", "CUM"},
    "PROJECT_V3": {"harm_action", "harm_inaction", "reversibility",
                   "ENF", "ID", "OV", "CUM", "RF", "SEL", "INT", "VOI"},
}
DECLARED_FROZEN = {"MAK_PLUS_POINTWISE": 5, "TWO_RULE_SIMPLE": 3,
                   "SECURITY_BOUNDED": 6, "MINIMAL_4VAR": 7, "PROJECT_V3": 11}
BASELINES = ("TWO_RULE_SIMPLE", "SECURITY_BOUNDED", "MINIMAL_4VAR")


def checked(ok, reason):
    if not ok:
        raise AssertionError(reason)


def literal_named(tree, name):
    matches = [stmt.value for stmt in tree.body
               if isinstance(stmt, ast.Assign) and any(
                   isinstance(t, ast.Name) and t.id == name for t in stmt.targets)]
    checked(len(matches) == 1, f"Expected one {name} constant")
    return ast.literal_eval(matches[0])


def field_from_o(item):
    if isinstance(item, ast.Subscript) and isinstance(item.value, ast.Name) and item.value.id == "o":
        checked(isinstance(item.slice, ast.Constant) and isinstance(item.slice.value, str),
                "Dynamic observation index requires manual audit")
        return item.slice.value
    return None


def policy_features(tree):
    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "choose"]
    checked(len(funcs) == 1, "choose function not uniquely available")
    body = funcs[0].body
    aliases = {}
    for stmt in body:
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Tuple):
            target = stmt.targets[0].elts
            value = stmt.value.elts if isinstance(stmt.value, (ast.Tuple, ast.List)) else []
            if len(value) == len(target):
                for name, sub in zip(target, value):
                    key = field_from_o(sub)
                    if isinstance(name, ast.Name) and key:
                        aliases[name.id] = key
    checked(aliases == {"ha": "harm_action", "hi": "harm_inaction", "rev": "reversibility"},
            "Global observation aliases changed; parser assumptions invalid")
    results = {}
    for stmt in body:
        if not isinstance(stmt, ast.If):
            continue
        test = stmt.test
        if not (isinstance(test, ast.Compare) and isinstance(test.left, ast.Name)
                and test.left.id == "policy" and len(test.ops) == 1
                and isinstance(test.ops[0], ast.Eq) and len(test.comparators) == 1
                and isinstance(test.comparators[0], ast.Constant)):
            continue
        label = test.comparators[0].value
        checked(label not in results, "Duplicate policy clause")
        nodes = [sub for item in stmt.body for sub in ast.walk(item)]
        used = {aliases[n.id] for n in nodes if isinstance(n, ast.Name)
                and isinstance(n.ctx, ast.Load) and n.id in aliases}
        used.update(key for n in nodes if (key := field_from_o(n)) is not None)
        results[label] = used
    checked(set(results) == set(EXPECTED_USED), "Policy branch inventory changed")
    return results


def compute(result, used, declared, rate):
    primary = result["stress_primary"]
    output = {}
    for name in EXPECTED_USED:
        value = primary[name]["mean_regret"]
        checked(isinstance(value, (int, float)) and math.isfinite(value), "Invalid original regret")
        checked(value >= rate * declared[name],
                "Linear sensitivity invalid: regret may be truncated to zero")
        # Oracle penalty is zero; the published regret is strictly nonnegative
        # before the declared penalty, so replace the penalty without clipping.
        output[name] = value + rate * (len(used[name]) - declared[name])
    return output


def main():
    tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
    used = policy_features(tree)
    declared = literal_named(tree, "POLICY_COMPLEXITY")
    rate = literal_named(tree, "COMPLEXITY_PENALTY_PER_INPUT")
    checked(declared == DECLARED_FROZEN, "Frozen declared complexity counts drifted")
    checked(rate == 0.0035, "Frozen complexity penalty changed")
    checked(used == EXPECTED_USED, "Frozen policy input references changed")
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    output = compute(result, used, declared, rate)
    original = result["stress_primary"]
    best = min(output[name] for name in BASELINES)
    v3 = output["PROJECT_V3"]
    checked(best > 0, "Invalid comparator")
    checked(original["MAK_PLUS_POINTWISE"]["mean_regret"] > original["PROJECT_V3"]["mean_regret"],
            "Original MAK-v3 regret ordering changed")
    checked(output["MAK_PLUS_POINTWISE"] < v3,
            "Conditional input-count correction no longer flips MAK-v3 order")
    checked(output["TWO_RULE_SIMPLE"] < original["TWO_RULE_SIMPLE"]["mean_regret"],
            "Two-rule count sensitivity missing")
    checked(v3 > best, "V3 original negative result not robust to this penalty scenario")
    # Negative control: introduce a new syntactic reference to reversibility into
    # B's clause. This ensures that the parser refuses the stale two-input claim.
    modified = SCRIPT.read_text(encoding="utf-8").replace(
        'if max(ha,hi)>=.50: return "EXPERIMENT"',
        'if max(ha,hi)>=.50 and rev>=0: return "EXPERIMENT"', 1)
    checked(modified != SCRIPT.read_text(encoding="utf-8"), "Negative control injection failed")
    altered = policy_features(ast.parse(modified))
    checked(altered["TWO_RULE_SIMPLE"] != EXPECTED_USED["TWO_RULE_SIMPLE"]
            and "reversibility" in altered["TWO_RULE_SIMPLE"],
            "Mutation control did not detect the newly referenced input")
    report = {
        "status": "PASS",
        "scope": "POSTHOC_SYNTACTIC_REFERENCE_COUNT_SENSITIVITY_NOT_CAUSAL_INDEPENDENT_REPLICATION",
        "declared_counts": declared,
        "referenced_input_counts": {k: len(v) for k, v in used.items()},
        "adjusted_regret_conditional": {k: round(v, 9) for k, v in output.items()},
        "v3_regret_worse_percent_conditional": round(100 * (v3 / best - 1), 6),
        "mak_vs_v3_regret_ranking_flips_under_conditional_pricing": True,
        "mutation_control_rejected": True,
        "published_frozen_result_unchanged": True,
    }
    print(json.dumps(report, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()

"""Small exhaustive propositional-logic audit: genuine models, not LLM self-grading.

Checks formal entailment CONDITIONAL on the supplied premises and correct
translation into symbols. Does not establish the truth of empirical premises.
Every unentailed conclusion yields a directly checkable countermodel.
An inconsistent premise set is explicitly classified, never claimed as proof.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import re
import sys

ATOM = re.compile(r"[A-Za-z][A-Za-z0-9_]{0,63}\Z")
MAX_ATOMS = 12
MAX_NODES = 250
MAX_DEPTH = 25


class LogicInputError(ValueError):
    """Malformed or resource-unbounded proposition."""


def _parse(formula, atoms: set[str], budget: list[int], depth: int = 0):
    budget[0] += 1
    if budget[0] > MAX_NODES or depth > MAX_DEPTH:
        raise LogicInputError("formula exceeds fixed node/depth budget")
    if type(formula) is bool:
        return
    if isinstance(formula, str) and ATOM.fullmatch(formula):
        atoms.add(formula)
        if len(atoms) > MAX_ATOMS:
            raise LogicInputError("too many atomic propositions")
        return
    if not isinstance(formula, dict) or len(formula) != 1:
        raise LogicInputError("formula must be an atom, boolean, or one-key operator")
    op, arg = next(iter(formula.items()))
    if op == "not":
        _parse(arg, atoms, budget, depth + 1)
        return
    if op in {"and", "or", "implies", "iff"}:
        if not isinstance(arg, list) or (len(arg) != 2 if op in {"implies", "iff"} else len(arg) < 1):
            raise LogicInputError(f"invalid operands for {op}")
        for sub in arg:
            _parse(sub, atoms, budget, depth + 1)
        return
    raise LogicInputError("unsupported logical operator")


def evaluate(formula, assignment: dict[str, bool]) -> bool:
    """Interpret a previously validated formula under a total assignment."""
    if type(formula) is bool:
        return formula
    if isinstance(formula, str):
        return assignment[formula]
    op, arg = next(iter(formula.items()))
    if op == "not":
        return not evaluate(arg, assignment)
    if op == "and":
        return all(evaluate(x, assignment) for x in arg)
    if op == "or":
        return any(evaluate(x, assignment) for x in arg)
    if op == "implies":
        return not evaluate(arg[0], assignment) or evaluate(arg[1], assignment)
    if op == "iff":
        return evaluate(arg[0], assignment) == evaluate(arg[1], assignment)
    raise LogicInputError("unsupported operator")


def audit(premises: list, conclusion) -> dict:
    """Exhaust all Boolean interpretations; return a countermodel or valid status."""
    if not isinstance(premises, list):
        raise LogicInputError("premises must be a list")
    atoms: set[str] = set()
    budget = [0]
    for statement in premises + [conclusion]:
        _parse(statement, atoms, budget)
    names = sorted(atoms)
    total = 0
    compatible = 0
    countermodel = None
    for values in product((False, True), repeat=len(names)):
        env = dict(zip(names, values))
        total += 1
        if all(evaluate(p, env) for p in premises):
            compatible += 1
            if not evaluate(conclusion, env):
                # Keep enumerating to verify the total search was exhaustive.
                if countermodel is None:
                    countermodel = env.copy()
    if compatible == 0:
        decision = "INCONSISTENT_PREMISES"
    elif countermodel is not None:
        decision = "NOT_ENTAILED"
    else:
        decision = "VALID_ENTAILMENT"
    payload = {"premises": premises, "conclusion": conclusion}
    return {
        "decision": decision,
        "conditional_on_premises": True,
        "empirical_truth_established": False,
        "symbolic_translation_verified": False,
        "atoms": names,
        "models_examined": total,
        "premise_compatible_models": compatible,
        "countermodel": countermodel,
        "problem_sha256": sha256(
            json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
    }


def verify_countermodel(premises: list, conclusion, countermodel: dict) -> bool:
    """Witness check; the caller can inspect each true premise and false conclusion."""
    if not isinstance(countermodel, dict):
        return False
    names = set()
    budget = [0]
    for formula in premises + [conclusion]:
        _parse(formula, names, budget)
    if set(countermodel) != names or any(type(v) is not bool for v in countermodel.values()):
        return False
    return all(evaluate(p, countermodel) for p in premises) and not evaluate(conclusion, countermodel)


def run_cases(path: Path | None = None):
    path = path or Path(__file__).with_name("logic_cases.json")
    cases = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(cases, list):
        raise LogicInputError("casebook must contain a list")
    result = []
    for case in cases:
        outcome = audit(case["premises"], case["conclusion"])
        outcome["case_id"] = case["case_id"]
        outcome["question"] = case["question"]
        if outcome["countermodel"] is not None and not verify_countermodel(
            case["premises"], case["conclusion"], outcome["countermodel"]
        ):
            raise AssertionError("invalid counterexample witness")
        result.append(outcome)
    return result


if __name__ == "__main__":
    print(json.dumps(run_cases(Path(sys.argv[1]) if len(sys.argv) > 1 else None),
                     ensure_ascii=False, indent=2))

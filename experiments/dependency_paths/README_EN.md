# U21 — Nominal path count versus independent recovery

**Original 1 English public adaptation (2026-10-13)**. Evidence: **EXECUTED LOGICAL/SYNTHETIC COUNTEREXAMPLE**. No claim about actual outages, evaluator capture or real-world probabilities.

The historical Project Intersection U21/U41 research identifies a trap: multiple formally independent exit/recovery/review routes may share the same *necessary* provider, credential or failure domain. Here each path is available only if all mandatory dependencies work; one available path suffices. We enumerate **minimal sets of prerequisite failures** that remove every path (minimum cut sets).

| Toy case | Nominal route count | Smallest joint-disabling cut |
|---|---:|---:|
| G1→C1, G2→C2 (separate) | 2 | 2 |
| G1→C, G2→C (shared) | 2 | **1** |
| Add same-dependency G3→C | 3 | **1** |
| Add independent G3→D | 3 | 2 |

A nominal third route on the same required provider does **not** increase redundancy against that provider's failure. **Common dependency does not itself establish actual failure, wrongdoing, coercion, probability or capture.** This algorithm knows only declared components; hidden dependencies, switching time, action enforcement and correlation risks are not measured.

From public repo root:

```bash
python experiments/dependency_paths/model.py
python -m unittest discover -s experiments/dependency_paths -p 'test_*.py' -v
```

[Deterministic expected result](RESULT.json). Six tests cover equal route counts but different cut sets, nominal duplicates, diverse backup, common-cause failure, empty requirements, and the explicit 12-component computational bound. The U41 claim of **pressure on independent decision makers through shared essential resources** is a separate causal/organizational hypothesis and is not tested by this connectivity toy.

Prior art: fault trees, network cut sets, common-cause failure and redundancy engineering. This is a project-specific reproducible illustration, not a novel mathematical theorem. Human problem discovery/corrections and AI-assisted formalization have distinct lineage. The public document uses English Original 1 / Korean Original 2; original internal source ordering is preserved. No private topology, secrets or identified sensitive systems are disclosed. [License HOLD](LICENSE_STATUS.md) · [E041 causal twin](../e041/README_EN.md) · [evidence index](../../PUBLIC_EVIDENCE_INDEX.md).

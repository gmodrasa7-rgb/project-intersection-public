# Provenance

This directory is an automatically constructed reviewer-safe candidate bundle.
It is not evidence of real-world safety or external validation.

Source commit: `4830a7456989ecf94a1ccf0bc333110915b00912`

## Allowlisted source mapping

- `public/PUBLIC_WORK_SAMPLE_CANDIDATE_2026-09-15.md` -> `README.md`
- `experiments/007_explicit_exit_consent_game/model.py` -> `model.py`
- `experiments/007_explicit_exit_consent_game/timing_variants.py` -> `timing_variants.py`
- `experiments/007_explicit_exit_consent_game/timing_probe.py` -> `timing_probe.py`
- `experiments/007_explicit_exit_consent_game/test_e007_model.py` -> `test_e007_model.py`
- `experiments/007_explicit_exit_consent_game/test_e007_timing_variants.py` -> `test_e007_timing_variants.py`
- `experiments/007_explicit_exit_consent_game/test_e007_timing_probe.py` -> `test_e007_timing_probe.py`

## Interpretation boundary

The timing sweep measures sensitivity inside a synthetic finite-horizon model. Counts are not empirical probabilities.
The generated summary is pinned to the publication-candidate headline; a changed count forces review instead of silently changing the claim.
Runtime residue such as __pycache__, .pyc, and .pytest_cache is excluded from the release boundary.

## Current rerun

Python 3.12.14; pytest 9.1.1; 27 tests passed; 72/36/17 reproduced. Earlier documentation/test-count records were stale; the current bundle has 27 passing tests. This is same-implementation computational reproduction, not independent scientific replication. The released E007 directory now has an explicit scoped license: code and requirements.txt under Apache-2.0; project-authored documentation and timing_summary.json under CC BY 4.0. See LICENSE_STATUS.md.

Release lineage: the original scoped-license release was followed by the 2026-10-04 post-strike history-encoding correction. The correction changes recorded history semantics, not utilities or the 17/72 classification-sensitive result; the 72-case grid is unchanged. License decision remains scoped to this directory.


## 2026-10-04 history-encoding correction

A falsification pass found that execute-first history recording used the pre-strike activity state for the follower. A follower rendered inactive before its response could therefore appear to choose a strategic action in the logged history. The correction records the realized effective follower action from the post-strike response state. Utilities and the 17/72 classification-sensitive count are unchanged; history/timing-sensitive cases change from 31/72 to 36/72. The new regression requires a lethally preempted follower to be logged as WAIT.

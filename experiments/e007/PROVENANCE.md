# Provenance

This directory is an automatically constructed reviewer-safe candidate bundle.
It is not evidence of real-world safety or external validation.

Source commit: `d7242191f284d713781129c1720e233c7bd4708d`

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

Python 3.12.14; pytest 9.1.1; 26 tests passed; 72/31/17 reproduced. Documentation test counts updated from 24 to 26. This is same-implementation computational reproduction, not independent scientific replication. The released E007 directory now has an explicit scoped license: code and requirements.txt under Apache-2.0; project-authored documentation and timing_summary.json under CC BY 4.0. See LICENSE_STATUS.md.

Release changes: scoped license notices/texts and Korean summary added; scientific code and grid unchanged. License decision delegated by the user after power-reversal review.

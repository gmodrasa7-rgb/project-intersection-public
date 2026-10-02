# Reproduce

```bash
python -m pip install -r requirements.txt
PYTHONDONTWRITEBYTECODE=1 python -m pytest -q
PYTHONDONTWRITEBYTECODE=1 python timing_probe.py --summary-only --check
```

Expected isolated regression result: **26 passed**.
Expected timing summary: 72 cases; 31 timing/history-sensitive; 17 classification-sensitive.
These are synthetic-model sensitivity counts, not empirical probabilities.

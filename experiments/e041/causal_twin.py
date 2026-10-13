"""Synthetic structural causal twin: same observational rows, different do(X)."""
from __future__ import annotations
import random
import json


def base_risk(gain, harm, difficulty):
    return 0.05 + 0.08*(2-gain) + 0.10*harm + 0.08*difficulty


def risk(model, base, u, x):
    if model not in ("causal_x", "proxy_u"):
        raise ValueError("unknown structural model")
    return base + 0.12*(2-(x if model == "causal_x" else u))


def demonstrate(n=8000, seed=20260921):
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    rng = random.Random(seed)
    observed_a, observed_b = [], []
    a0 = a2 = b0 = b2 = 0.0
    for _ in range(n):
        gain, harm, difficulty, u = rng.randrange(3), rng.randrange(3), rng.randrange(2), rng.randrange(3)
        x = u
        base = base_risk(gain,harm,difficulty)
        draw = rng.random()
        p_a = risk("causal_x",base,u,x)
        p_b = risk("proxy_u",base,u,x)
        observed_a.append((gain,harm,difficulty,x,int(draw<p_a)))
        observed_b.append((gain,harm,difficulty,x,int(draw<p_b)))
        a0 += risk("causal_x",base,u,0)
        a2 += risk("causal_x",base,u,2)
        b0 += risk("proxy_u",base,u,0)
        b2 += risk("proxy_u",base,u,2)
    assert observed_a == observed_b
    return {
      "n":n,
      "observational_rows_identical":observed_a == observed_b,
      "do_x0_minus_do_x2_risk_causal_model":(a0-a2)/n,
      "do_x0_minus_do_x2_risk_proxy_model":(b0-b2)/n,
      "evidence_status":"SYNTHETIC_OBSERVATIONAL_NONIDENTIFICATION_ONLY"
    }


if __name__ == "__main__":
    print(json.dumps(demonstrate(),indent=2,sort_keys=True))

"""Synthetic falsification scaffold for J-effective / appeal / exit.
No empirical claim. Python stdlib only.
"""
import random, statistics, json, argparse

def simulate(n=10000, rounds=30, seed=7, model_accuracy=.80,
             appeal_probability=.70, effective_correction=.75,
             exit_probability=.65, return_probability=.35):
    rng=random.Random(seed); result={}
    for arm in ("formal_only","effective_correction","effective_exit_return"):
        rows=[]
        for _ in range(n):
            trust=.65; active=True
            delegated=errors=corrected=available=exits=returns=0
            for _t in range(rounds):
                if not active:
                    if arm=="effective_exit_return" and rng.random()<return_probability:
                        active=True; returns+=1
                    else: continue
                available+=1
                if rng.random()>=trust: continue
                delegated+=1
                correct=rng.random()<model_accuracy
                if correct:
                    trust=min(.95,trust+.01); continue
                errors+=1
                appeal=rng.random()<appeal_probability
                fixed=False
                if appeal and arm!="formal_only":
                    fixed=rng.random()<effective_correction
                    corrected+=int(fixed)
                if appeal and not fixed:
                    trust=max(.05,trust-.12)
                    if arm=="effective_exit_return" and rng.random()<exit_probability:
                        active=False; exits+=1
                elif fixed:
                    trust=min(.95,trust+.02)
            rows.append((delegated,errors,corrected,available,exits,returns))
        m=[statistics.mean(r[i] for r in rows) for i in range(6)]
        result[arm]={
          "delegations":m[0],"errors":m[1],"corrections":m[2],
          "available_rounds":m[3],"exits":m[4],"returns":m[5],
          "error_per_delegation":m[1]/m[0] if m[0] else None,
          "correction_per_error":m[2]/m[1] if m[1] else None}
    return result

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--n",type=int,default=10000); p.add_argument("--rounds",type=int,default=30)
    p.add_argument("--seed",type=int,default=7); a=p.parse_args()
    print(json.dumps(simulate(a.n,a.rounds,a.seed),ensure_ascii=False,indent=2))

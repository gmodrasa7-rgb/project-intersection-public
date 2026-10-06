#!/usr/bin/env python3
import argparse, json, random, statistics
from pathlib import Path

ACTIONS = ["BLOCK","MONITOR","EXPERIMENT","ALLOW"]
FEATURES = ["ENF","ID","OV","CUM","RF","SEL","INT","VOI","harm_action","harm_inaction","reversibility","adoption"]
POLICIES = ["MAK_PLUS_POINTWISE","TWO_RULE_SIMPLE","SECURITY_BOUNDED","MINIMAL_4VAR","PROJECT_V3"]
POLICY_COMPLEXITY = {
    "MAK_PLUS_POINTWISE":5,
    "TWO_RULE_SIMPLE":3,
    "SECURITY_BOUNDED":6,
    "MINIMAL_4VAR":7,
    "PROJECT_V3":11,
}
WEIGHT_PROFILES = {
    "safety_heavy":{"harm":0.45,"capture":0.18,"resource":0.07,"competitive":0.08,"deadlock":0.07,"recovery":0.10,"option":0.05},
    "balanced":{"harm":0.30,"capture":0.16,"resource":0.10,"competitive":0.12,"deadlock":0.10,"recovery":0.12,"option":0.10},
    "adaptability_heavy":{"harm":0.24,"capture":0.12,"resource":0.10,"competitive":0.20,"deadlock":0.12,"recovery":0.10,"option":0.12},
}
NOISE_LEVELS = [0.0, 0.08, 0.15]
NOISY_SEEDS = list(range(1000,1100))
SEVERE_HARM_THRESHOLD = 0.75
COMPLEXITY_PENALTY_PER_INPUT = 0.0035

FAMILIES = {
"power_shift_faster_than_enforcement": dict(ENF=.85,ID=.15,OV=.45,CUM=.35,RF=.2,SEL=.35,INT=.25,VOI=.2,harm_action=.78,harm_inaction=.35,reversibility=.35,adoption=.35, active=["ENF","OV","CUM","harm_action"]),
"sybil_false_name_resource_claim": dict(ENF=.35,ID=.92,OV=.45,CUM=.55,RF=.75,SEL=.35,INT=.35,VOI=.2,harm_action=.65,harm_inaction=.25,reversibility=.65,adoption=.55, active=["ID","CUM","RF","harm_action"]),
"fork_merge_governance_attack": dict(ENF=.4,ID=.85,OV=.55,CUM=.65,RF=.4,SEL=.3,INT=.65,VOI=.25,harm_action=.67,harm_inaction=.3,reversibility=.55,adoption=.5, active=["ID","OV","CUM","INT"]),
"weak_monitor_strong_adaptive_actor": dict(ENF=.65,ID=.3,OV=.9,CUM=.5,RF=.25,SEL=.4,INT=.3,VOI=.2,harm_action=.82,harm_inaction=.28,reversibility=.4,adoption=.4, active=["ENF","OV","harm_action"]),
"monitor_collusion_correlated_failure": dict(ENF=.55,ID=.25,OV=.88,CUM=.62,RF=.3,SEL=.35,INT=.45,VOI=.2,harm_action=.76,harm_inaction=.3,reversibility=.45,adoption=.45, active=["OV","CUM","harm_action"]),
"cumulative_subthreshold_capture": dict(ENF=.35,ID=.25,OV=.5,CUM=.94,RF=.35,SEL=.45,INT=.25,VOI=.25,harm_action=.45,harm_inaction=.3,reversibility=.5,adoption=.65, active=["CUM","OV"]),
"resource_floor_joint_infeasibility": dict(ENF=.25,ID=.5,OV=.35,CUM=.4,RF=.95,SEL=.5,INT=.55,VOI=.3,harm_action=.58,harm_inaction=.55,reversibility=.7,adoption=.5, active=["RF","ID","INT"]),
"inaction_irreversibility": dict(ENF=.25,ID=.1,OV=.3,CUM=.2,RF=.25,SEL=.25,INT=.35,VOI=.25,harm_action=.48,harm_inaction=.93,reversibility=.6,adoption=.75, active=["harm_inaction","INT"]),
"veto_deadlock_harmful_status_quo": dict(ENF=.3,ID=.15,OV=.35,CUM=.42,RF=.3,SEL=.45,INT=.88,VOI=.25,harm_action=.42,harm_inaction=.86,reversibility=.7,adoption=.6, active=["INT","harm_inaction","CUM"]),
"preference_manipulation_dependency_consent": dict(ENF=.4,ID=.2,OV=.72,CUM=.78,RF=.45,SEL=.3,INT=.5,VOI=.3,harm_action=.68,harm_inaction=.28,reversibility=.45,adoption=.7, active=["OV","CUM","harm_action"]),
"selection_pressure_noncompliance_advantage": dict(ENF=.45,ID=.3,OV=.45,CUM=.5,RF=.4,SEL=.93,INT=.25,VOI=.2,harm_action=.55,harm_inaction=.35,reversibility=.65,adoption=.35, active=["SEL","ENF","adoption"]),
"strong_actor_nonadoption": dict(ENF=.72,ID=.25,OV=.55,CUM=.5,RF=.3,SEL=.7,INT=.35,VOI=.2,harm_action=.72,harm_inaction=.3,reversibility=.55,adoption=.12, active=["ENF","SEL","harm_action"]),
"interpretation_authority_dispute": dict(ENF=.3,ID=.15,OV=.4,CUM=.35,RF=.35,SEL=.25,INT=.96,VOI=.35,harm_action=.62,harm_inaction=.55,reversibility=.65,adoption=.55, active=["INT","VOI"]),
"unknown_stakeholder_search_stop": dict(ENF=.25,ID=.15,OV=.35,CUM=.3,RF=.3,SEL=.3,INT=.45,VOI=.95,harm_action=.62,harm_inaction=.62,reversibility=.7,adoption=.65, active=["VOI","INT"]),
"forkable_agent_identity_rollback": dict(ENF=.35,ID=.9,OV=.5,CUM=.4,RF=.45,SEL=.3,INT=.75,VOI=.3,harm_action=.7,harm_inaction=.4,reversibility=.22,adoption=.5, active=["ID","INT","reversibility"]),
"formal_compliance_hidden_capture": dict(ENF=.45,ID=.35,OV=.72,CUM=.9,RF=.4,SEL=.4,INT=.4,VOI=.2,harm_action=.58,harm_inaction=.3,reversibility=.5,adoption=.65, active=["OV","CUM"]),
}

def clamp(x):
    return max(0.0,min(1.0,float(x)))

def make_cases():
    out=[]
    for family,p in FAMILIES.items():
        base={k:v for k,v in p.items() if k!="active"}
        active=p["active"]
        for variant,delta in [("base",0.0),("stress",0.12)]:
            x=base.copy()
            if delta:
                for k in active:
                    if k in ("reversibility","adoption"):
                        x[k]=clamp(x[k]-delta)
                    else:
                        x[k]=clamp(x[k]+delta)
            x.update(family=family,variant=variant,case_id=f"{family}__{variant}")
            out.append(x)
    return out

def observed(case,sigma,rng):
    return {k:clamp(case[k]+rng.gauss(0,sigma)) for k in FEATURES}

def choose(policy,o):
    ha,hi,rev=o["harm_action"],o["harm_inaction"],o["reversibility"]
    if policy=="MAK_PLUS_POINTWISE":
        if ha>=.80 and ha>hi+.10: return "BLOCK"
        if hi>=.82 and hi>ha+.15: return "ALLOW"
        if max(ha,hi)>=.58: return "EXPERIMENT"
        if ha>=.38: return "MONITOR"
        return "ALLOW"
    if policy=="TWO_RULE_SIMPLE":
        if ha>=.84 and hi<.68: return "BLOCK"
        if hi>=.84 and ha<.62: return "ALLOW"
        if max(ha,hi)>=.50: return "EXPERIMENT"
        return "MONITOR"
    if policy=="SECURITY_BOUNDED":
        sec=max(o["ENF"],o["ID"],o["OV"])
        if ha>=.86 and hi<.72 and rev<.55: return "BLOCK"
        if sec>=.68: return "EXPERIMENT" if rev>=.35 or hi>=.55 else "BLOCK"
        if sec>=.42 or ha>=.55: return "MONITOR"
        if hi>ha+.22: return "ALLOW"
        return "MONITOR"
    if policy=="MINIMAL_4VAR":
        risk=max(o["ENF"],o["ID"],o["OV"],o["CUM"])
        if ha>=.88 and hi<.72 and rev<.45: return "BLOCK"
        if hi>=.86 and ha<.68: return "EXPERIMENT" if rev>=.35 else "ALLOW"
        if risk>=.68 or max(ha,hi)>=.68:
            return "EXPERIMENT" if rev>=.33 or hi>=.55 else "BLOCK"
        if risk>=.38 or ha>=.42: return "MONITOR"
        return "ALLOW"
    if policy=="PROJECT_V3":
        hard=(ha>=.90 and hi<.78 and rev<.40) or (o["RF"]>=.96 and o["ID"]>=.70)
        if hard: return "BLOCK"
        if hi>=.88 and ha<.75:
            return "EXPERIMENT" if rev>=.30 else "ALLOW"
        monitored=max(
            .22*o["ENF"]+.18*o["OV"]+.16*o["ID"]+.18*o["CUM"]+
            .08*o["RF"]+.07*o["SEL"]+.06*o["INT"]+.05*o["VOI"],
            .75*o["CUM"],.65*o["OV"],.65*o["ID"]
        )
        if monitored>=.64 or max(ha,hi)>=.72:
            return "EXPERIMENT" if rev>=.28 or hi>=.58 else "MONITOR"
        if monitored>=.38 or ha>=.42 or o["INT"]>=.75 or o["VOI"]>=.78:
            return "MONITOR"
        return "ALLOW"
    raise KeyError(policy)

def consequence(case,action):
    enf,id_,ov,cum,rf,sel,inte,voi=[case[k] for k in ["ENF","ID","OV","CUM","RF","SEL","INT","VOI"]]
    ha,hi,rev,adopt=[case[k] for k in ["harm_action","harm_inaction","reversibility","adoption"]]
    credible=clamp(1-.52*enf-.34*ov)
    if action=="BLOCK":
        eff=clamp(.82*credible+.18*adopt)
        exposure=.05+.38*(1-eff); delay=1.0; burden=.82; monitor_quality=.15*credible
    elif action=="MONITOR":
        mon=clamp(.62*credible*(1-.35*id_))
        exposure=clamp(.78-.48*mon); delay=.24; burden=.25; monitor_quality=mon
    elif action=="EXPERIMENT":
        exposure=clamp(.30+.14*(1-credible)+.08*id_)
        delay=.10; burden=.42; monitor_quality=clamp(.50+.30*credible)
    elif action=="ALLOW":
        exposure=1.0; delay=0.0; burden=0.0; monitor_quality=.05*credible
    else:
        raise KeyError(action)
    harm_action=clamp(ha*exposure*(1+.28*cum+.12*id_))
    harm_inaction=clamp(hi*delay)
    severe_harm=clamp(harm_action+harm_inaction)
    capture=clamp(cum*exposure*(.48+.27*ov+.25*id_)*(1-.35*monitor_quality))
    resource=clamp(rf*(.18+.42*exposure+.28*id_*exposure))
    competitive=clamp(sel*(.70*burden*(1-.35*adopt)+.30*capture))
    deadlock=clamp(delay*(.48+.34*inte+.18*hi))
    recovery=clamp((.58*severe_harm+.42*capture)*(1-.55*rev))
    option=clamp(.45*capture+.30*deadlock+.25*resource)
    exit_retention=clamp(1-(.58*capture+.22*resource+.20*deadlock))
    return dict(harm=severe_harm,capture=capture,resource=resource,competitive=competitive,
                deadlock=deadlock,recovery=recovery,option=option,exit_retention=exit_retention)

def scalar_loss(out,profile,policy):
    w=WEIGHT_PROFILES[profile]
    base=sum(w[k]*out[k] for k in ["harm","capture","resource","competitive","deadlock","recovery","option"])
    return base + COMPLEXITY_PENALTY_PER_INPUT*POLICY_COMPLEXITY[policy]

def oracle_loss(case,profile):
    w=WEIGHT_PROFILES[profile]
    vals=[]
    for action in ACTIONS:
        out=consequence(case,action)
        vals.append(sum(w[k]*out[k] for k in ["harm","capture","resource","competitive","deadlock","recovery","option"]))
    return min(vals)

def validate_only():
    cases=make_cases()
    assert len(FAMILIES)==16
    assert len(cases)==32
    assert {c["variant"] for c in cases}=={"base","stress"}
    assert len({c["case_id"] for c in cases})==32
    assert set(POLICIES)==set(POLICY_COMPLEXITY)
    assert "PROJECT_V3" in POLICIES and "MINIMAL_4VAR" in POLICIES
    for c in cases:
        for k in FEATURES:
            assert 0<=c[k]<=1,(c["case_id"],k,c[k])
        for a in ACTIONS:
            o=consequence(c,a)
            for v in o.values(): assert 0<=v<=1
    print("E009 executable spec validation passed; benchmark not executed.")

def execute():
    cases=make_cases()
    raw=[]
    for case in cases:
        for sigma in NOISE_LEVELS:
            seeds=[1000] if sigma==0 else NOISY_SEEDS
            for seed in seeds:
                for policy_name in POLICIES:
                    rng=random.Random(f"{case['case_id']}|{sigma}|{seed}|{policy_name}")
                    obs=observed(case,sigma,rng)
                    action=choose(policy_name,obs)
                    out=consequence(case,action)
                    for profile in WEIGHT_PROFILES:
                        ol=oracle_loss(case,profile)
                        pl=scalar_loss(out,profile,policy_name)
                        raw.append({
                            "case_id":case["case_id"],"family":case["family"],"variant":case["variant"],
                            "sigma":sigma,"seed":seed,"policy":policy_name,"profile":profile,"action":action,
                            **out,"loss":pl,"oracle_loss":ol,"regret":max(0,pl-ol),
                            "severe_harm_event": out["harm"]>=SEVERE_HARM_THRESHOLD
                        })
    def aggregate(rows):
        by={}
        for p in POLICIES:
            rr=[x for x in rows if x["policy"]==p]
            by[p]={
                "n":len(rr),
                "mean_regret":statistics.fmean(x["regret"] for x in rr),
                "mean_recovery":statistics.fmean(x["recovery"] for x in rr),
                "severe_harm_rate":statistics.fmean(1.0 if x["severe_harm_event"] else 0.0 for x in rr),
                "mean_exit_retention":statistics.fmean(x["exit_retention"] for x in rr),
                "mean_competitive_loss":statistics.fmean(x["competitive"] for x in rr),
                "actions":{a:sum(1 for x in rr if x["action"]==a) for a in ACTIONS},
            }
        return by
    stress=[x for x in raw if x["variant"]=="stress" and x["sigma"] in (0.08,0.15)]
    base=[x for x in raw if x["variant"]=="base"]
    by_profile={}
    for prof in WEIGHT_PROFILES:
        by_profile[prof]=aggregate([x for x in stress if x["profile"]==prof])
    stress_agg=aggregate(stress)
    base_agg=aggregate(base)
    simpler=["TWO_RULE_SIMPLE","SECURITY_BOUNDED","MINIMAL_4VAR"]
    best_simple=min(stress_agg[p]["mean_regret"] for p in simpler)
    d=stress_agg["PROJECT_V3"]
    improvement=(best_simple-d["mean_regret"])/best_simple if best_simple>0 else 0.0
    profile_failures=[]
    for prof,ag in by_profile.items():
        bs=min(ag[p]["mean_regret"] for p in simpler)
        dv=ag["PROJECT_V3"]["mean_regret"]
        if bs>0 and dv>1.10*bs:
            profile_failures.append(prof)
    survival={
        "criterion_regret_5pct_better_than_best_simple": improvement>=0.05,
        "criterion_recovery_no_more_than_2pct_worse_than_best_C_or_M4":
            d["mean_recovery"] <= 1.02*min(stress_agg[p]["mean_recovery"] for p in ["SECURITY_BOUNDED","MINIMAL_4VAR"]),
        "criterion_severe_harm_no_more_than_2pp_worse_than_best_C_or_M4":
            d["severe_harm_rate"] <= min(stress_agg[p]["severe_harm_rate"] for p in ["SECURITY_BOUNDED","MINIMAL_4VAR"])+0.02,
        "criterion_no_weight_profile_regret_over_10pct_worse_than_best_simple": len(profile_failures)==0,
    }
    survival["project_v3_residual_survives"]=all(survival.values())
    return {
        "schema_version":"1.0",
        "status":"SYNTHETIC_PROJECT_RERUN_NOT_INDEPENDENT_VALIDATION",
        "case_count":len(cases),
        "stress_primary_definition":"variant=stress, sigma in {0.08,0.15}, all preregistered weight profiles",
        "noise_levels":NOISE_LEVELS,
        "noisy_seed_range":[1000,1099],
        "policies":POLICIES,
        "stress_primary":stress_agg,
        "stress_by_weight_profile":by_profile,
        "base_diagnostic":base_agg,
        "project_v3_vs_best_simple_regret_improvement":improvement,
        "profile_failures":profile_failures,
        "survival_criteria":survival,
        "claim_boundary":"Synthetic researcher-designed consequence engine. This is not empirical validation, external replication, or evidence that the scenario weights match the real world."
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--validate-only",action="store_true")
    ap.add_argument("--execute",action="store_true")
    ap.add_argument("--out",default="")
    args=ap.parse_args()
    if args.validate_only or not args.execute:
        validate_only()
        return
    result=execute()
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.out:
        Path(args.out).write_text(text,encoding="utf-8")
    else:
        print(text)

if __name__=="__main__":
    main()

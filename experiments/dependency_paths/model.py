"""Synthetic practical-exit / recovery dependency min-cut toy. Not field reliability."""
from itertools import combinations
import json


def available(paths,failed):
    if not paths or any(not req for req in paths.values()):
        raise ValueError("Every path must have mandatory dependencies")
    return tuple(name for name, req in paths.items() if not set(req).intersection(failed))


def minimal_cuts(paths):
    if not paths or any(not req for req in paths.values()):
        raise ValueError("Cannot analyze an empty or zero-dependency path")
    nodes=sorted(set().union(*paths.values()))
    if len(nodes)>12:
        raise ValueError("Toy enumerator supports up to 12 dependencies")
    result=[]
    for size in range(1,len(nodes)+1):
        for items in combinations(nodes,size):
            failed=set(items)
            if not available(paths,failed) and not any(set(c).issubset(failed) for c in result):
                result.append(list(items))
    return result


def report():
    cases={
      "separate":{"G1":frozenset(["C1"]),"G2":frozenset(["C2"])},
      "shared":{"G1":frozenset(["C"]),"G2":frozenset(["C"])},
      "nominal_copy":{"G1":frozenset(["C"]),"G2":frozenset(["C"]),"G3":frozenset(["C"])},
      "independent_backup":{"G1":frozenset(["C"]),"G2":frozenset(["C"]),"G3":frozenset(["D"])}
    }
    out={}
    for name,paths in cases.items():
        m=minimal_cuts(paths)
        out[name]={"paths":len(paths),"minimum_cut_size":min(len(x) for x in m),"minimal_cuts":m}
    out["evidence_status"]="LOGICAL_SYNTHETIC_COMMON_CAUSE_ONLY"
    return out


if __name__ == "__main__":
    print(json.dumps(report(),indent=2,sort_keys=True))

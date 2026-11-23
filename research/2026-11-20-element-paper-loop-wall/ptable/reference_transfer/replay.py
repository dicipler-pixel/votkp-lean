"""Execute PROTOCOL.md (e3367e4); pinned archive, Python standard library."""
from collections import Counter
from dataclasses import dataclass
import csv
import gzip
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
TABLE = HERE.parent / "v2/ptable_v2_data.json"
ARCHIVE = HERE.parents[3] / "data/element_thresholds_20261011.json.gz"


@dataclass(frozen=True)
class Ladder:
    Z: int
    sym: str
    period: int
    col: int
    grades: str
    logs: tuple
    profile: tuple


def load():
    if hashlib.sha256(ARCHIVE.read_bytes()).hexdigest() != "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c":
        raise ValueError("Threshold archive digest changed")
    table = {e["Z"]: e for e in json.loads(TABLE.read_bytes())["elements"]}
    with gzip.open(ARCHIVE, "rt") as f:
        records = json.load(f)["records"]
    ladders, excluded = [], {}
    for record in records:
        z, sym = record["Z"], record["symbol"]
        if 57 <= z <= 71 or 89 <= z <= 103:
            excluded[sym] = "La–Lu or Ac–Lr display row"
            continue
        thresholds = {r["q"]: r for r in record["thresholds"]}
        missing = [q for q in range(9) if q not in thresholds]
        if missing:
            excluded[sym] = "missing q=" + ",".join(map(str, missing))
            continue
        row = table[z]
        assert row["sym"] == sym and 2 <= row["period"] <= 7
        energy = [thresholds[q]["IE_eV"] for q in range(9)]
        logs = tuple(math.log(b/a) for a,b in zip(energy,energy[1:]))
        assert min(logs) > 0
        grades = "".join(thresholds[q]["grade"] for q in range(9))
        assert set(grades) <= set("EST")
        ladders.append(Ladder(z,sym,row["period"],row["col"],grades,logs,tuple(map(math.log, logs))))
    return ladders, excluded


def nearest(q, candidates, mode):
    def distance(r):
        if mode == "logs":
            return math.dist(q.logs, r.logs)
        differences = [v-w for v,w in zip(q.profile, r.profile)]
        return max(differences) - min(differences)
    ranks = [(distance(r),r) for r in candidates]
    minimum = min(d for d,r in ranks)
    tied = [r for d,r in ranks if math.isclose(d, minimum, rel_tol=1e-12, abs_tol=1e-14)]
    answers = {q.col == r.col for r in tied}
    return "/".join(r.sym for r in tied), "/".join(r.grades for r in tied), (answers.pop() if len({r.col for r in tied}) == 1 else None), len(tied)


def run(refs, queries, exclude_period):
    details = []
    for q in queries:
        pool = [r for r in refs if not exclude_period or r.period != q.period]
        row = dict(symbol=q.sym, period=q.period, column=q.col, grades=q.grades, candidates=len(pool),
                   label_available=any(r.col == q.col for r in pool))
        for mode in ("simplex", "logs"):
            name, grades, hit, ntie = nearest(q,pool,mode) if pool else ("","",None,0)
            row.update({mode:name, mode+"_grades":grades, mode+"_hit":hit, mode+"_tie_size":ntie})
        details.append(row)
    return details


def report(rows):
    wins, losses = [], []
    for r in rows:
        a,b = r["simplex_hit"],r["logs_hit"]
        if a is True and b is False: wins.append(r["symbol"])
        if a is False and b is True: losses.append(r["symbol"])
    n = len(wins)+len(losses)
    p = min(1,2*sum(math.comb(n,i) for i in range(min(len(wins),len(losses))+1))/2**n) if n else 1
    return dict(queries=len(rows), simplex_hits=sum(r["simplex_hit"] is True for r in rows),
                log_hits=sum(r["logs_hit"] is True for r in rows), simplex_only=wins, log_only=losses,
                no_group=[r["symbol"] for r in rows if not r["label_available"]],
                unresolved=[r["symbol"] for r in rows if None in (r["simplex_hit"],r["logs_hit"])],
                ties=[r["symbol"] for r in rows if max(r["simplex_tie_size"],r["logs_tie_size"])>1],
                query_thresholds=dict(sorted(Counter("".join(r["grades"] for r in rows)).items())),
                descriptive_sign_p=p if rows else None)


def main():
    ladders, excluded = load()
    ref = [r for r in ladders if r.Z <= 85]
    ext = [r for r in ladders if r.Z >= 86]
    assert len(ref)==62 and len(ladders)+len(excluded)==118
    summary = {"excluded":excluded}
    allrows = []
    for cohort,query,hold_period in [("historical",ref,True),("heavy",ext,False)]:
        for measured in (False, True):
            panel = cohort+("_all_E" if measured else "")
            refs = [r for r in ref if not measured or r.grades=="E"*9]
            qs = [r for r in query if not measured or r.grades=="E"*9]
            rows = run(refs,qs,hold_period)
            summary[panel]=report(rows) | {"reference_elements":len(refs),"query_pool_before_grade_filter":len(query)}
            allrows.extend({"panel":panel,**r} for r in rows)
    with (HERE/"predictions.csv").open("w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=allrows[0],lineterminator="\n")
        writer.writeheader();writer.writerows(allrows)
    (HERE/"results.json").write_text(json.dumps(summary,indent=2,ensure_ascii=False)+"\n")
    for k,v in summary.items():
        if k!="excluded": print(k, v)


if __name__ == "__main__":
    main()

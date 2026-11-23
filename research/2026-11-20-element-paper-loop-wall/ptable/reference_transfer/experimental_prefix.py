"""Execute the experimental-only protocol frozen at 67c1435."""
from dataclasses import replace
import csv
import gzip
import hashlib
import json
import math

from replay import HERE, ARCHIVE, TABLE, Ladder, report, run


def eligible(k):
    with gzip.open(ARCHIVE, "rt") as f:
        records = json.load(f)["records"]
    table = {e["Z"]:e for e in json.loads(TABLE.read_bytes())["elements"]}
    found = []
    for rec in records:
        z = rec["Z"]
        if z < 9 or 57 <= z <= 71 or 89 <= z <= 103:
            continue
        th = {r["q"]:r for r in rec["thresholds"]}
        if any(q not in th or th[q]["grade"] != "E" for q in range(k+1)):
            continue
        e = table[z]
        assert e["sym"]==rec["symbol"]
        logs = tuple(math.log(th[i+1]["IE_eV"]/th[i]["IE_eV"]) for i in range(k))
        assert min(logs)>0
        found.append(Ladder(z,e["sym"],e["period"],e["col"],"E"*(k+1),logs,tuple(map(math.log,logs))))
    return found


def first_two(e):
    return replace(e, grades=e.grades[:3], logs=e.logs[:2], profile=e.profile[:2])


def main():
    assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()=="75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
    summary, rows = [], []
    previous = None
    for k in range(2,9):
        group = eligible(k)
        ids = {e.Z for e in group}
        assert previous is None or ids <= previous
        previous = ids
        refs = [e for e in group if e.Z<=85]
        for historical in (True,False):
            queries = refs if historical else [e for e in group if e.Z>=86]
            initial = run(refs,queries,historical)
            paired = run(list(map(first_two,refs)),list(map(first_two,queries)),historical)
            assert [r["symbol"] for r in initial]==[r["symbol"] for r in paired]
            cell = {"k":k,"panel":"historical" if historical else "heavy","references":len(refs)}
            for name, subset in [("full",initial),("k2_matched",paired)]:
                available = [r for r in subset if r["label_available"]]
                evaluated = any(r["candidates"] for r in subset)
                totals = report(subset)
                totals["scorable"] = evaluated
                if not evaluated:
                    totals["descriptive_sign_p"]=None
                cell[name]=totals
                cell[name+"_available"]=report(available)
                rows.extend(dict(k=k,panel=cell["panel"],reading=name,**r) for r in subset)
            summary.append(cell)
    dest = HERE/"experimental_prefix_rows.csv"
    with dest.open("w", newline="") as f:
        out = csv.DictWriter(f,fieldnames=rows[0],lineterminator="\n")
        out.writeheader()
        out.writerows(rows)
    (HERE/"experimental_prefix_results.json").write_text(json.dumps(summary,indent=2)+"\n")
    for c in summary:
        r=c["full"]; p=c["k2_matched"]
        print(c["panel"],c["k"],c["references"],r["queries"],r["simplex_hits"],r["log_hits"],
              len(r["no_group"]),r["descriptive_sign_p"],p["simplex_hits"],p["log_hits"])
    for c in summary[:2]:print(c["panel"],c["full"])


if __name__ == "__main__":
    main()

"""Score every available held-out row against the already frozen CSV intervals."""
import argparse
import csv
from statistics import mean
from pathlib import Path
import sys

root=Path(__file__).resolve().parent
with (root/"krypton_forecast.csv").open() as f:
    predictions=list(csv.DictReader(f))
with (root/"phase_shell_means.csv").open() as f:
    measurements={r["mesh"]:r for r in csv.DictReader(f)
                  if (r["series"],r["symbol"],r["shell"])==("default","Kr","shortest")}
cli=argparse.ArgumentParser(description=__doc__)
cli.add_argument("--phase-directions",nargs="*",type=Path,default=[],
                 help="Optional direct NC krypton outputs from microscopic_response.py")
for file in cli.parse_args().phase_directions:
    with file.open() as stream:
        rows=[r for r in csv.DictReader(stream) if r["shell"]=="shortest"]
    assert len(rows)==4 and all(r["symbol"]=="Kr" and r["mesh"]==rows[0]["mesh"] for r in rows)
    fields=("microscopic_L_A2","twist_log_L_A2")
    points={f:mean(float(r[f]) for r in rows) for f in fields}
    if rows[0]["mesh"] in measurements:
        assert all(abs(points[f]-float(measurements[rows[0]["mesh"]][f]))<1e-12 for f in fields)
    measurements[rows[0]["mesh"]]=points
out=csv.DictWriter(sys.stdout,["field","mesh","predicted_A2","lower_A2","upper_A2",
                               "computed_A2","computed_minus_predicted_A2","inside_frozen_interval"],
                   lineterminator="\n")
out.writeheader()
for p in predictions:
    if p["mesh"] not in measurements:
        continue
    value=float(measurements[p["mesh"]][p["field"]])
    center=float(p["quadratic_4_6_8"])
    lo,hi=float(p["lower_A2"]),float(p["upper_A2"])
    out.writerow(dict(field=p["field"],mesh=p["mesh"],predicted_A2=center,lower_A2=lo,
                      upper_A2=hi,computed_A2=value,computed_minus_predicted_A2=value-center,
                      inside_frozen_interval=lo<=value<=hi))

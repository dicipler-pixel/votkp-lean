"""Collect the unrounded output of site_tensor.py and microscopic_response.py."""
import argparse
import csv
from itertools import groupby
from pathlib import Path
from statistics import mean

import numpy as np


def datasets():
    # (series, file prefix, site output or Bloch-phase output).
    yield "default", "NC-", "site"
    yield "default", "PAW-", "site"
    yield "default", "micro-", "phase"
    for name, tag in (("alternate","alternate_twist"), ("lower-ws","60_Ry"), ("ws","grid_32")):
        for field, prefix in (("site","csite-"),("phase","cmicro-")):
            yield tag, prefix + name + "-", field


def write_table(path, rows):
    with path.open("w",newline="") as f:
        out=csv.DictWriter(f,rows[0].keys(),lineterminator="\n")
        out.writeheader()
        out.writerows(rows)


def collect(source, target):
    tables={"site":[],"phase":[]}
    for tag,pattern,kind in datasets():
        for f in sorted(source.glob(pattern + "*.csv")):
            with f.open() as file:
                rows=list(csv.DictReader(file))
            if kind=="phase" and rows and "twist_log_L_A2" not in rows[0]:
                raise RuntimeError("Stale file: " + str(f))
            tables[kind].extend(dict(series=tag, **row) for row in rows)
    site = sorted(tables["site"],key=lambda r:(r["series"],r["family"],r["symbol"],int(r["mesh"])))
    phase = sorted(tables["phase"],key=lambda r:(r["series"],r["symbol"],int(r["mesh"]),r["shell"],
                                                  int(r["h"]),int(r["k"]),int(r["l"])))
    write_table(target/"site_moments.csv",site)
    write_table(target/"phase_directions.csv",phase)
    means=[]
    for (tag,el,n,shell),g in groupby(phase,key=lambda r:(r["series"],r["symbol"],r["mesh"],r["shell"])):
        rows=list(g)
        assert len(rows)==(3 if shell=="axial" else {"Kr":4,"Rb":6}[el])
        out=dict(series=tag,symbol=el,mesh=n,shell=shell,directions=len(rows))
        for key in ("q_inv_A","S_per_electron","microscopic_L_A2","rank_change_A2",
                    "overlap_loss_A2","WS_phase_L_A2","twist_log_L_A2"):
            out[key]=mean(float(r[key]) for r in rows)
        assert np.isclose(out["rank_change_A2"]+out["overlap_loss_A2"],out["microscopic_L_A2"])
        means.append(out)
    write_table(target/"phase_shell_means.csv",means)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("rows_dir",type=Path)
    p.add_argument("output_dir",type=Path)
    a=p.parse_args()
    collect(a.rows_dir,a.output_dir)

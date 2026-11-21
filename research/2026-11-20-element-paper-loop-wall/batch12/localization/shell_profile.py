"""Resolve the zeroth and second moments into complete Wigner–Seitz distance shells."""
import argparse
import csv
from pathlib import Path

import numpy as np

from site_tensor import image_dyads
from weight_io import read_weights


def profile(path):
    family,el,mesh_text=path.stem.split("-")
    mesh=int(mesh_text)
    X,cell,nu=read_weights(path)
    assert X.shape==(mesh,)*3
    distances2,_,_=image_dyads(mesh,cell)
    # These perfect cubic structures have exact degeneracies in ideal arithmetic.
    # Collective rounding serves only to group equal squared distances (in Å²).
    keys=np.round(distances2,8)
    B=X.sum()-X.flat[0]
    groups=[]
    for shell,dist2 in enumerate(np.unique(keys[keys>0]),start=1):
        mask=keys==dist2
        xr=X.ravel()[mask]
        r2=distances2[mask]
        assert np.ptp(r2)<1e-8
        groups.append(dict(family=family,element=el,mesh=mesh,shell=shell,
                           distance_A=np.sqrt(r2.mean()),site_classes=mask.sum(),
                           weight=xr.sum(),mean_square_per_axis_A2=(xr@r2)/(6*nu)))
    total=sum(row["mean_square_per_axis_A2"] for row in groups)
    cum0=cum2=0.
    for row in groups:
        row["fraction_offsite"]=row["weight"]/B
        row["fraction_second_moment"]=row["mean_square_per_axis_A2"]/total
        cum0+=row["fraction_offsite"]
        cum2+=row["fraction_second_moment"]
        row["cumulative_offsite"]=cum0
        row["cumulative_second_moment"]=cum2
    assert np.isclose(cum0,1.) and np.isclose(cum2,1.)
    summary=dict(family=family,element=el,mesh=mesh,
                 first_shell_fraction_offsite=groups[0]["fraction_offsite"],
                 first_shell_fraction_second_moment=groups[0]["fraction_second_moment"],
                 median_offsite_distance_A=next(r["distance_A"] for r in groups if r["cumulative_offsite"]>=.5),
                 median_moment_distance_A=next(r["distance_A"] for r in groups if r["cumulative_second_moment"]>=.5),
                 rms_distance_conditional_offsite_A=np.sqrt(total*6*nu/B))
    return groups,summary


def write(path,rows):
    with path.open("w",newline="") as file:
        w=csv.DictWriter(file,rows[0].keys(),lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("work",type=Path,help="folder containing weights/*.csv")
    args=p.parse_args()
    shell_rows=[]
    summaries=[]
    for path in sorted((args.work/"weights").glob("*.csv"),
                       key=lambda p:(*p.stem.split("-")[:2],int(p.stem.split("-")[2]))):
        groups,summary=profile(path)
        shell_rows.extend(groups)
        summaries.append(summary)
    write(args.work/"shell_profile.csv",shell_rows)
    write(args.work/"shell_summary.csv",summaries)

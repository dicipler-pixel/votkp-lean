"""Frozen NC krypton finite-mesh forecasts based only on 4³, 6³ and 8³ runs."""
import argparse
import csv
from pathlib import Path
import sys

import numpy as np


def make_predictions(source):
    early={}
    with source.open() as stream:
        for r in csv.DictReader(stream):
            m=int(r["mesh"])
            if (r["series"],r["symbol"],r["shell"])==("default","Kr","shortest") and m in (4,6,8):
                early[m]=r
    assert sorted(early)==[4,6,8]
    # For a smooth gapped state, cubic averaging and reversal make even q powers
    # the natural candidate. q scales as 1/M at fixed reciprocal star.
    for field in ("microscopic_L_A2","twist_log_L_A2"):
        x=np.array([1/m**2 for m in (4,6,8)])
        y=np.array([float(early[m][field]) for m in (4,6,8)])
        p1=np.polynomial.polynomial.polyfit(x[1:],y[1:],1)
        p2=np.polynomial.polynomial.polyfit(x,y,2)
        for m in (10,12):
            low_order=np.polynomial.polynomial.polyval(1/m**2,p1)
            forecast=np.polynomial.polynomial.polyval(1/m**2,p2)
            tolerance=max(1e-5,2*abs(low_order-forecast))
            yield dict(field=field,mesh=m,linear_6_8=low_order,quadratic_4_6_8=forecast,
                       lower_A2=forecast-tolerance,upper_A2=forecast+tolerance)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("early_phase_means",type=Path)
    args=p.parse_args()
    rows=list(make_predictions(args.early_phase_means))
    w=csv.DictWriter(sys.stdout,rows[0].keys(),lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

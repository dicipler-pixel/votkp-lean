"""Ideal-contact uncertainty for carbon's and nitrogen's helium-core openings."""
from fractions import Fraction as Q
import csv
import math
import sys
from pathlib import Path

def interval(row):
    a,b = Q(row["start_q_IE_eV"]),Q(row["end_q_plus_1_IE_eV"])
    da,db = Q(row["start_unc_eV"]),Q(row["end_unc_eV"])
    return (b-db)/(a+da), (b+db)/(a-da)

def opening(z):
    return math.degrees(math.acos(float((z-1)/(z+1))))

with Path(sys.argv[1]).open(newline='') as f:
    rows = {r["element"]:r for r in csv.DictReader(f) if r["core"]=="helium"}
c = interval(rows["Carbon"]); n = interval(rows["Nitrogen"])
# Both forward intervals lie above one. arccos(gamma(z)) decreases with z.
lower = opening(c[1])+opening(n[1])
upper = opening(c[0])+opening(n[0])
assert 89.8 < lower < upper < 89.9
print(f"Upper contact interval from the two energy boxes: [{lower:.9f}, {upper:.9f}] degrees.")
print(f"Rotation from 90 degrees to upper contact: [{90-upper:.9f}, {90-lower:.9f}] degrees.")

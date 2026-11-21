"""Evaluate preregistered Hf shell-ordering and W thermal-distance controls."""
import csv
from collections import Counter
from decimal import Decimal as D
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
HERE=Path(__file__).resolve().parent
with (HERE/"hafnium_axis_inputs.csv").open() as f:
    axes=list(csv.DictReader(f))
with (HERE/"hafnium_shells.csv").open("w",newline="") as f:
    out=csv.writer(f,lineterminator="\n")
    out.writerow(["run","P_GPa","c_over_a","interlayer_d_over_a","basal_d_over_a","q_slack_8_minus_3q2","shortest_even_after_rounding"])
    for r in axes:
        v=F(r["c_over_a"])
        upper=v+F(1,2000)
        side="interlayer" if 3*upper**2<8 else "unresolved"
        diff=8-3*v*v
        relative=(D(1)/3+D(r['c_over_a'])**2/4).sqrt()
        out.writerow([r["run"],r["P_GPa"],r["c_over_a"],str(relative),1,str(diff),side])
        print(r["run"],"relative basal minus interlayer:",1-relative,"printed shell order:",side)
with (HERE/"crystals.csv").open() as f:
    rows=sorted([r for r in csv.DictReader(f) if 9006486<=int(r["COD"])<=9006520],key=lambda r:(int(r["temperature_K_if_reported"]),r["COD"]))
assert len(rows)==35
temps=[int(r["temperature_K_if_reported"]) for r in rows]
counts=Counter()
extremal=None
with (HERE/"tungsten_thermal.csv").open("w",newline="") as f:
    out=csv.writer(f,lineterminator="\n")
    out.writerow(["COD","T_K","a_A","nearest_A_from_exact_a","relative_length_vs_first"])
    a0=D(rows[0]["a_A"])
    for r in rows:
        a=D(r["a_A"]); d=D(3).sqrt()*a/2
        assert abs(d-D(r["shortest_A"]))<D(".000001")
        out.writerow([r["COD"],r["temperature_K_if_reported"],a,d,a/a0-1])
for aa,bb in combinations(rows,2):
    a,b=D(aa["a_A"]),D(bb["a_A"])
    if aa["temperature_K_if_reported"]==bb["temperature_K_if_reported"]:
        counts["same T"]+=1;continue
    k="increase" if a<b else "decrease" if a>b else "tie"
    counts[k]+=1
    if k=="decrease" and (extremal is None or b-a<extremal[0]):
        extremal=(b-a,aa["COD"],bb["COD"],aa["temperature_K_if_reported"],bb["temperature_K_if_reported"])
first,last=rows[0],rows[-1]
ratio=D(last["a_A"])/D(first["a_A"])
print("W distinct-temperature pair comparisons plus replicate pairs:",dict(counts),"largest decline:",extremal)
print("W temperature endpoints, cell lengths:",(temps[0],first["a_A"]),(temps[-1],last["a_A"]))
print("W fractional endpoint length and volume gains:",ratio-1,ratio**3-1)

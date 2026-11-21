"""Kinematics of bound beta versus the ionization-threshold span. Ground-state inputs."""
import csv
import gzip
import hashlib
import json
from decimal import Decimal as D
from pathlib import Path

HERE=Path(__file__).resolve().parent
FILE=HERE.parents[3]/"data/element_thresholds_20261011.json.gz"
PIN="75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
if hashlib.sha256(FILE.read_bytes()).hexdigest()!=PIN:
    raise ValueError("Unpinned archive")
with gzip.open(FILE,"rt") as f:
    records=json.load(f,parse_float=D)["records"]
re,os=(records[i]["thresholds"] for i in (74,75))
assert len(re)==75 and len(os)==76 and all(t["q"]==i for seq in (re,os) for i,t in enumerate(seq))
def total(seq,key):
    return sum(D(r[key]) for r in seq)
binding_re=total(re,"IE_eV")
binding_os=total(os,"IE_eV")
shell=D(os[-1]["IE_eV"])
unc=sum(total(seq,"unc_eV") for seq in (re,os[:-1]))
corr=binding_re-total(os[:-1],"IE_eV")
assert corr==binding_re-binding_os+shell
initial,terminal=re[0],re[-1]
span=D(terminal["IE_eV"])/D(initial["IE_eV"])
span_min=(D(terminal["IE_eV"])-D(terminal["unc_eV"]))/(D(initial["IE_eV"])+D(initial["unc_eV"]))
span_max=(D(terminal["IE_eV"])+D(terminal["unc_eV"]))/(D(initial["IE_eV"])-D(initial["unc_eV"]))
# The 42 Gyr is the historical neutral comparison in Bosch 1996; its uncertainty
# is not given there. Apply the 2.0 y endpoints only for this historical ratio.
acc=D("42e9")/D("32.9")
print("Binding-energy sums, eV: Re, Os, H-like Os",binding_re,binding_os,shell)
print("Net electronic correction, eV:",corr,"rectangular width:",unc)
print("Threshold-span IE75/IE1 central and interval:",span,span_min,span_max)
print("Historical neutral/bare rate central and bare-width-only limits:",
      acc,D("42e9")/D("34.9"),D("42e9")/D("30.9"))
print("Ratio of the two central spans",acc/span)
assert acc/span>100000 and D("42e9")/D("34.9")>span_max
with (HERE/"rhenium_nuclear_inputs.csv").open() as f:
    inputs=list(csv.DictReader(f))
with (HERE/"rhenium_channels.csv").open("w",newline="") as f:
    out=csv.writer(f,lineterminator="\n")
    out.writerow(["A","source","neutral_Q_keV","neutral_unc_keV","Hlike_final_Q_keV","box_low_keV","box_high_keV",
                  "bare_continuum_Q_keV","continuum_low_keV","continuum_high_keV","ground_daughter_K_channel"])
    for r in inputs:
        q,u=D(r["qbm_keV"]),D(r["qbm_unc_keV"])
        q_b=q+corr/1000
        u_b=u+unc/1000
        q_c=q+(binding_re-binding_os)/1000
        u_c=u_b+D(os[-1]["unc_eV"])/1000
        pred="open" if q_b-u_b>0 else "closed" if q_b+u_b<0 else "unresolved"
        assert pred==("open" if r["A"]=="187" else "closed")
        assert q_c+u_c<0
        out.writerow([r["A"],r["source"],q,u,q_b,q_b-u_b,q_b+u_b,q_c,q_c-u_c,q_c+u_c,pred])

# Use positive removal costs. Neutral Q equals ionic Q plus sum(Os) − sum(Re).
partial=total(os[:29],"IE_eV")-total(re[:29],"IE_eV")
pu=total(re[:29],"unc_eV")+total(os[:29],"unc_eV")
print("First 29 threshold sum Os minus Re, eV:",partial,"box",partial-pu,partial+pu)
# Direct ionic-mass route: the same 29-electron correction appears both in the
# published neutral mass difference and when removing the first 29 electrons.
# Thus use the positive measured m(Re29+)−m(Os29+) mass difference directly.
ion_q,ion_u=D("2417.4"),D("0.9")
remaining=total(re[29:],"IE_eV")-total(os[29:-1],"IE_eV")
remaining_u=total(re[29:],"unc_eV")+total(os[29:-1],"unc_eV")
hybrid=ion_q+remaining
hybrid_u=ion_u+remaining_u
print("Direct mass + 46 remaining threshold pairs, eV:",hybrid,"width",hybrid_u,"box",hybrid-hybrid_u,hybrid+hybrid_u)
print("Daughter free-electron comparator, eV:",hybrid-shell,"width",hybrid_u+D(os[-1]["unc_eV"]))
assert len(re[29:])==len(os[29:-1])==46
assert remaining==corr+partial and remaining_u==unc-pu
assert hybrid-hybrid_u>0 and hybrid-shell+hybrid_u+D(os[-1]["unc_eV"])<0
with (HERE/"osmium_first_levels.csv").open() as f:
    ground,first=csv.DictReader(f)
exc,exc_u=D(first["energy"])*1000,D(first["unc_e"])*1000
assert ground["jp"]=="1/2-" and first["jp"]=="3/2-"
neutral,neutral_u=D("2470.9"),D("1.3")
print("Excited Os: bare parent, K capture, eV:",
      hybrid-exc,"width",hybrid_u+exc_u)
print("Excited Os: neutral parent, continuum, eV:",
      neutral-exc,"width",neutral_u+exc_u)
assert hybrid-exc-hybrid_u-exc_u>0 and neutral-exc+neutral_u+exc_u<0

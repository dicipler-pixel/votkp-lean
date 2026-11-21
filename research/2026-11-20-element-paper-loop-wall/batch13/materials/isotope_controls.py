"""Test continuation of the N=82 and ionic-radius trends; check measured sign at two optical lines."""
import csv
from decimal import Decimal as D
from pathlib import Path

HERE=Path(__file__).resolve().parent


def read(path):
    with path.open() as f:
        return list(csv.DictReader(f))


def run():
    nuclides=read(HERE/"isotopes.csv")
    ions=read(HERE/"ionic_radii.csv")
    N82=sorted([r for r in nuclides if r["N"]=="82"],key=lambda r:int(r["Z"]))
    prev=next(r for r in read(HERE.parents[1]/"batch12/materials/isotopes.csv") if r["Z"]=="60" and r["N"]=="82")
    ion_prev=D("110.9")  # Nd3+ VIII; checked directly below
    iri=lambda z,rows:D(next(r["Shannon_ionic_radius_pm"] for r in rows if
                             r["Z"]==str(z) and r["charge"]=="3" and r["coordination"]=="VIII"))
    assert ion_prev==iri(60,read(HERE.parents[1]/"batch12/materials/ionic_radii.csv"))
    data=[]
    for n in N82:
        Z=int(n["Z"])
        atom=n["symbol"]
        ion=iri(Z,ions)
        row=[n[k] for k in ("symbol","Z","A","N","net_up","net_down","spin_parity","charge_radius_fm","radius_unc_fm")]
        if prev["charge_radius_fm"] and n["charge_radius_fm"]:
            diff=D(n["charge_radius_fm"])-D(prev["charge_radius_fm"])
            u=D(n["radius_unc_fm"])+D(prev["radius_unc_fm"])
            step=[diff,diff-u,diff+u]
            status="positive in full box" if diff>u else "negative in full box" if diff < -u else "overlaps zero"
        else:
            step=["","",""]
            status="absolute radius missing"
        data.append([*row,*step,status,ion,ion-ion_prev])
        prev,ion_prev=n,ion
    with (HERE/"isotone_continuation.csv").open("w",newline="") as f:
        w=csv.writer(f,lineterminator="\n")
        w.writerow("element Z A N net_up net_down spin_parity R_fm R_unc_fm step_fm step_min_fm step_max_fm status ion3plus_VIII_pm ion3plus_step_pm".split())
        w.writerows(data)
    print("N=82 tests vs preceding Z:",[(r[0],r[-3]) for r in data])
    if any(r[-1]>=0 for r in data):
        raise ValueError("Fixed charge, CN VIII: expected central contraction failed")
    print("Fixed trivalent ionic radius falls on all five steps from Nd.")
    for r in read(HERE/"pm_isotope_lines.csv"):
        A=int(r["A"])
        if A==147: continue
        x,y=D(r["shift_452_MHz"]),D(r["shift_468_MHz"])
        u,v=D(r["unc_452_MHz"]),D(r["unc_468_MHz"])
        if not (x-u>0 and y+v<0):
            raise ValueError("Opposite signs are unconfirmed in a quoted box")
        print(f"147/{A} fixed isotope pair at 452/468 nm: minimum opposite signed shift magnitudes {x-u}/{-y-v} MHz.")
    print("The two lines disagree in sign for all four isotope substitutions, including all quoted uncertainty corners.")


if __name__=="__main__":
    run()

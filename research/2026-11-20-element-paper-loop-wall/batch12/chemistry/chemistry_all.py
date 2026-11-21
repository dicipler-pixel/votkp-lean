"""Compute anion chemistry from pinned IE1, evaluated EA inputs, and historical read-only ladders."""
import argparse
import csv
import gzip
import hashlib
import json
from collections import Counter
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
PAPER=HERE.parents[1]
ARCHIVE_SHA="75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
EV_PER_RECIP_CM=F("6.62607015e-34")*299792458*100/F("1.602176634e-19")
SOURCES={
    "EA22": (2022,"https://doi.org/10.1063/5.0080243"),
    "H91": (1991,"https://doi.org/10.1103/PhysRevA.43.6104"),
    "ScY23": (2023,"https://doi.org/10.1063/5.0124882"),
    "As25": (2025,"https://doi.org/10.1103/PhysRevLett.134.043001"),
    "Se26_cm-1": (2026,"https://pubmed.ncbi.nlm.nih.gov/41626821/"),
    "Zr17": (2017,"https://doi.org/10.1063/1.4986547"),
    "Tc02": (2002,"https://doi.org/10.1103/PhysRevA.65.064502"),
    "Rh26": (2026,"https://doi.org/10.1088/1674-1056/ae5173"),
}
getcontext().prec=70
INV_W=D(3)-2*D(2).sqrt()


def read(path):
    with path.open() as f:
        return list(csv.DictReader(f))


def csv_out(path, columns, values):
    with path.open("w",newline="") as f:
        writer=csv.writer(f,lineterminator="\n")
        writer.writerow(columns.split())
        writer.writerows(values)


def w(x):
    return D(x.numerator)/D(x.denominator)


def val(x):
    return f"{w(x):.12f}"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inputs():
    src={}
    sourcefiles = read(HERE/"source_hashes.csv")
    for entry in sourcefiles:
        if digest(PAPER/entry["file"])!=entry["sha256"]:
            raise ValueError("EA table differs from frozen source "+entry["file"])
    for r in read(PAPER/sourcefiles[0]["file"]):
        z=int(r["Z"])
        src[z]=(r["symbol"],r["EA_source_units"],r["unc_source_units"],r["status"],r["source"])
    for r in read(PAPER/sourcefiles[1]["file"]):
        if r["k"]=="0":
            src[int(r["Z"])]=(r["symbol"],r["start_eV"],r["start_unc_eV"],"measured","EA22")
    src[54]=("Xe","","","unbound","EA22")
    for r in read(PAPER/sourcefiles[2]["file"]):
        src[int(r["Z"])]=(r["symbol"],r["EA_eV"],r["unc_eV"],"measured","EA22")
    return src


def historical():
    """Byte-check historical files before secondary comparisons with their displayed rung zero."""
    stored={}
    total=0
    for item in read(HERE/"historical_input_hashes.csv"):
        path=PAPER/item["paper_relative_file"]
        if digest(path)!=item["sha256"]:
            raise ValueError(f"Historical ladder bytes changed for {path}")
        records=read(path)
        if len(records)!=int(item["registered_rows"]):
            raise ValueError("Historical row count mismatch")
        total+=len(records)
        for r in records:
            raw=r.get("IE_k (eV)",r.get("energy_eV"))
            if r["k"]=="0" and raw:
                stored[int(r["Z"])]=F(raw)
    return stored,total


def inside_values(a,I):
    eta=(I-a)/2
    chi=(I+a)/2
    gamma=eta/chi
    omega=chi**2/(2*eta)
    return gamma, omega/eta, 2*gamma**2-1


def generate(archive,outdir):
    if digest(archive)!=ARCHIVE_SHA:
        raise ValueError("Pinned archive mismatch")
    with gzip.open(archive,"rt") as f:
        rec=json.load(f,parse_float=D)["records"][:60]
    affinities=inputs()
    if list(sorted(affinities))!=list(range(1,61)):
        raise ValueError("Wrong element coverage in EA sources")
    historical_ea,hist_count=historical()
    changes=[]
    table=[]
    omitted=[]
    statistics=Counter()
    inside=[]
    margins=[]
    for e in rec:
        z,s,name=e["Z"],e["symbol"],e["name"]
        sym,raw,unc,status,source=affinities[z]
        if sym!=s:
            raise ValueError(f"Missing element: {s}")
        year,url=SOURCES[source]
        if status=="unbound":
            omitted.append([z,s,name,"no bound ground-state anion in adopted ledger",year,url])
            continue
        scale=EV_PER_RECIP_CM if source=="Se26_cm-1" else 1
        a=F(raw)*scale
        da=F(unc)*scale if unc else None
        t=e["thresholds"][0]
        I,dI=F(t["IE_eV"]),F(t["unc_eV"]) if t["unc_eV"] is not None else None
        eta,chi=(I-a)/2,(I+a)/2
        H=I-a
        omega=chi**2/(2*eta)
        big_omega=chi**2/(2*H)
        if not 0<a<I:
            raise ValueError("Forward positive rung prerequisites failed")
        gamma,ratio,slack=inside_values(a,I)
        outside=slack>0
        if not (gamma==(I/a-1)/(I/a+1) and ratio==1/(2*gamma**2) and
                omega/H==ratio/2 and big_omega/H==ratio/4 and chi/H==1/(2*gamma)):
            raise ValueError("Hardness conventions disagree with the exact input ratios")
        if outside!=(ratio<1) or outside!=(big_omega/H<F(1,4)) or outside!=(omega/H<F(1,2)):
            raise ValueError("Wall classification depends on hardness convention")
        side="outside" if outside else "inside" if slack<0 else "on"
        if side=="inside":
            inside.append(s)
        complete=da is not None and dI is not None
        if complete:
            gamma_lo,r_hi,s_lo=inside_values(a+da,I-dI)
            gamma_hi,r_lo,s_hi=inside_values(a-da,I+dI)
            if not (0<gamma_lo<=gamma<=gamma_hi and s_lo<=slack<=s_hi and r_lo<=ratio<=r_hi
                    and (s_lo>0 if outside else s_hi<0)):
                raise ValueError(f"Uncertainty changes classification for {s}")
            bounds=[val(s_lo),val(s_hi),val(r_lo),val(r_hi)]
        else:
            bounds=["","","",""]
        old=historical_ea.get(z)
        if z<=55 and old is None:
            raise ValueError(f"No historical row zero for {s}")
        if old is not None and old!=a:
            changes.append((s,old,a))
        crit=w(I)*INV_W
        delta_A=w(a)-crit
        if (delta_A<0)!=outside:
            raise ValueError(f"EA boundary disagrees for {s}")
        margins.append((abs(delta_A),s,delta_A))
        statistics[side,status,complete]+=1
        table.append([z,s,name,status,source,year,url,raw,unc,"cm^-1" if scale!=1 else "eV",
                      val(a),val(da) if da is not None else "",str(t["IE_eV"]),str(t["unc_eV"]) if dI is not None else "",
                      t["grade"],t["references"],val(I/a),val(gamma),val(eta),val(chi),val(omega),val(ratio),
                      val(H),val(omega/H),val(big_omega),val(big_omega/H),val(chi/H),val(slack),
                      *bounds,f"{crit:.12f}",f"{delta_A:.12f}",side])
    if len(table)!=49 or [s for s,_,_ in changes]!=["Sc","Se"]:
        raise ValueError("Expected reference coverage or historical display differences changed")
    outdir.mkdir(exist_ok=True,parents=True)
    columns=("Z symbol element EA_status EA_source EA_source_year EA_source_URL EA_source_value "
             "EA_source_unc EA_source_unit EA_eV EA_unc_eV IE1_pinned_eV IE1_unc_eV IE1_grade IE1_ref "
             "z0 Gamma0 eta_half_eV chi_eV omega_eV omega_over_eta H_full_eV omega_over_H "
             "Omega_full_index_eV Omega_over_H chi_over_H signed_wall_slack slack_lo slack_hi "
             "omega_over_eta_lo omega_over_eta_hi critical_EA_eV EA_minus_critical_eV wall")
    csv_out(outdir/"anion_chemistry_h_nd.csv",columns,table)
    csv_out(outdir/"no_bound_anion_h_nd.csv","Z symbol element status EA_source_year EA_source_URL",omitted)
    print(f"{len(table)} numeric anion inputs and {len(omitted)} without a bound ground-state anion entry.")
    print("Class / source status / complete boxes:",dict(statistics))
    print("Inside:",", ".join(inside))
    print(f"Read-only historical files verified by SHA-256: 10, rows {hist_count}, numeric anions {len(historical_ea)}.")
    for s,old,a in changes:
        print(f"Historical display and evaluated source differ at {s}: {w(old)} vs {w(a)} eV.")
    for _,s,m in sorted(margins)[:3]:
        print(f"Nearest to critical EA in absolute eV distance: {s} {m:.9f} eV signed (A - A_critical).")
    print("Precision test: rational identities hold for each row; decimal rounding occurs only in output.")
    print("Output SHA-256:",digest(outdir/"anion_chemistry_h_nd.csv"))


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("archive",type=Path)
    p.add_argument("--out",type=Path,default=HERE)
    args=p.parse_args()
    generate(args.archive,args.out)

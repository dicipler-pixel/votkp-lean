"""Generate exact archive and uncertainty-window certificates for antimony to cesium."""
import argparse
import csv
import gzip
import hashlib
import json
import os
import re
import subprocess
import tempfile
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

HERE=Path(__file__).resolve().parent
HASH="75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
NAMES=["Antimony","Tellurium","Iodine","Xenon","Cesium"]
EA=[("1.047401",".000019"),("1.970875",".000007"),("3.0590465",".0000036"),None,(".471626",".000025")]

def dec(x):
    return format(Decimal(x),"f")

def box(e,u):
    unc="none" if u is None else "(some "+dec(u)+")"
    return "some ⟨"+dec(e)+","+unc+"⟩"

def generate(path,printed):
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=HASH:
        raise ValueError("Archive differs from 8e5d44f")
    rs=json.loads(gzip.decompress(raw),parse_float=Decimal)["records"]
    with printed.open(newline="") as h:
        rows=list(csv.DictReader(h))
    shifted=0
    if [(int(r["Z"]),int(r["k"])) for r in rows] != [(z,k) for z in range(51,56) for k in range(z+1)]:
        raise ValueError("Wrong serialized batch-11 row keys")
    lines=["-- Archive central energies and uncertainties in electron volts. No fitted thresholds.",
           "import Batch11Kernel", "namespace ElementPaper.Batch11","set_option maxRecDepth 8192",
           "set_option maxHeartbeats 10000000",""]
    prior=[]
    decl=["agreesAtAnyCut","sharpWindow","orderedEndpoints"]
    for z,r in enumerate(rs[:55],1):
        th=r["thresholds"]
        if r["Z"]!=z or [q["q"] for q in th]!=list(range(z)):
            raise ValueError("Archive rows incomplete")
        values=[dec(q["IE_eV"]) for q in th]
        if z<=50:
            prior.append("["+", ".join(values)+"]")
            if z%10==0:
                name=f"priorThrough{z}"
                lines += [f"def {name} : List (List Rat) :=", "  ["+",\n   ".join(prior)+"]","",
                          f"theorem {name}Window : {name}.all (centralTest nitrogen carbon) = true := by",
                          "  decide +kernel",""]
                decl.append(name+"Window")
                prior=[]
            continue
        name=NAMES[z-51];aff=EA[z-51]
        vals=[box(*aff) if aff else "none"]+[box(q["IE_eV"],q["unc_eV"]) for q in th]
        erows=rows[shifted:shifted+z+1];shifted+=z+1
        if [Fraction(i["IE_k (eV)"]) for i in erows[1:]]!=list(map(Fraction,values)):
            raise ValueError("Archive/public ordinary energy mismatch")
        if (Fraction(erows[0]["IE_k (eV)"]) if erows[0]["IE_k (eV)"] else None)!=(Fraction(aff[0]) if aff else None):
            raise ValueError("Public affinity mismatch")
        groups=[", ".join(vals[i:i+4]) for i in range(0,len(vals),4)]
        lines += [f"def {name} : List (Option Energy) :=", "  ["+",\n   ".join(groups)+"]",""]
        # The expected first entries encode k=0, then subsequent ordinary crossing numbers.
        heads={"Antimony":["some .outside","some .inside","some .missing","some .missing"],
               "Tellurium":["some .inside"],"Iodine":["some .inside"],"Xenon":["none"],
               "Cesium":["some .outside","some .outside"]}[name]
        lines += [f"theorem {name}BoxCalls : labels {name} =","    ["+", ".join(heads)+"] ++ "+
                  f"List.replicate {z-len(heads)} (some .inside) := by decide +kernel","",
                  f"def {name}Ordinary := {name}.tail.filterMap (fun e => e.map Energy.e)",
                  f"theorem {name}OrdinaryCalls :",
                  f"    {name}Ordinary.length = {z} ∧ centralTest nitrogen cesium {name}Ordinary = true ∧",
                  f"    (({name}Ordinary.zip {name}Ordinary.tail).zipIdx.filterMap fun ((a,b),i) =>",
                  "      if outside a b then some (i+1) else none) = "+("[1]" if z==55 else "[]")+" := by decide +kernel",""]
        decl += [name+"BoxCalls",name+"OrdinaryCalls"]
    lines+=["/-- The newly met upper endpoint is attained by the first ordinary cesium crossing. -/",
            "theorem cesiumWitness : CesiumOrdinary[1]! / CesiumOrdinary[0]! = cesium ∧",
            "    ¬ (6 < CesiumOrdinary[1]! / CesiumOrdinary[0]!) ∧",
            "    outside CesiumOrdinary[0]! CesiumOrdinary[1]! = true := by decide +kernel","",
            "theorem previousWitnesses :",
            "    let n := priorThrough10[6]!",
            "    let c := priorThrough10[5]!",
            "    n[5]!/n[4]!==nitrogen ∧ outside n[4]! n[5]! = false ∧",
            "    c[4]!/c[3]!==carbon ∧ outside c[3]! c[4]! = true := by decide +kernel",""]
    # Avoid token ambiguity between Lean's indexing and bool equality operators.
    lines=[s.replace("]!==","]! = ") for s in lines]
    decl+=["cesiumWitness","previousWitnesses"]
    lines += ["def historical := ("+" ++ ".join(f"priorThrough{z}" for z in range(10,51,10))+").flatMap (fun e => e.zip e.tail)",
              "def beforeCesium := historical ++ (["+", ".join(n+"Ordinary" for n in NAMES[:-1])+"] : List (List Rat)).flatMap (fun e => e.zip e.tail)",
              "def expanded := beforeCesium ++ CesiumOrdinary.zip CesiumOrdinary.tail","",
              "theorem historicalAndExpandedCount : historical.length=1225 ∧ beforeCesium.length=1431 ∧ expanded.length=1485 := by decide +kernel",""]
    decl.append("historicalAndExpandedCount")
    for ledger,upper,highpair,title in [("historical","carbon","(64.49352,392.09056)","windowHydrogenTin"),
                                        ("beforeCesium","carbon","(64.49352,392.09056)","windowHydrogenXenon"),
                                        ("expanded","cesium","(3.89390572743,23.15745)","windowHydrogenCesium")]:
        lines += [f"theorem {title} (c : Rat) : Fits {ledger} c ↔ nitrogen ≤ c ∧ c < {upper} := by",
                  f"  apply sharpWindow {ledger} (97.8901,552.06741) {highpair} <;> decide +kernel",""]
        decl.append(title)
    lines+=["theorem cutoffSixFirstFailsWithCesium : Fits beforeCesium 6 ∧ ¬ Fits expanded 6 := by",
            "  rw [windowHydrogenXenon, windowHydrogenCesium]",
            "  decide +kernel",""]
    decl.append("cutoffSixFirstFailsWithCesium")
    lines += ["#print axioms "+n for n in decl]+["","end ElementPaper.Batch11",""]
    return "\n".join(lines),len(decl)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive",type=Path)
    parser.add_argument("csv",type=Path)
    parser.add_argument("--lean",default="lean")
    parser.add_argument("--generate",action="store_true")
    args=parser.parse_args()
    s,n=generate(args.archive,args.csv)
    p=HERE/"AntimonyCesium.lean"
    if args.generate:p.write_text(s)
    if p.read_text()!=s:raise ValueError("Generated source differs")
    # Independent second parse of every emitted new ordinary threshold and uncertainty.
    with gzip.open(args.archive,"rt") as f:rec=json.load(f,parse_float=Fraction)["records"]
    for z,name in enumerate(NAMES,51):
        chunk=re.search(rf"def {name} : List \(Option Energy\) :=\s*\[(.*?)\]",p.read_text(),re.S)[1]
        encoded=re.findall(r"some ⟨([^,]+),(?:\(some ([^)]+)\)|(none))⟩",chunk)
        if name!="Xenon":encoded=encoded[1:]
        read=[(Fraction(e),Fraction(u) if u else None) for e,u,_ in encoded]
        if read!=[(Fraction(q["IE_eV"]),q["unc_eV"]) for q in rec[z-1]["thresholds"]]:
            raise ValueError("Emitted energy/uncertainty list differs")
    print("265 generated energies and 265 uncertainty fields independently reparsed; archive and public energy values agree.")
    print(subprocess.check_output([args.lean,"--version"],text=True).strip(),flush=True)
    with tempfile.TemporaryDirectory() as tmp:
        tmp=Path(tmp);env=dict(os.environ,LEAN_PATH=str(tmp));cmd=[args.lean,"-j1"]
        for name in ["Batch11Kernel.lean",p.name]:(tmp/name).write_bytes((HERE/name).read_bytes())
        subprocess.run(cmd+["-o","Batch11Kernel.olean","Batch11Kernel.lean"],cwd=tmp,env=env,check=True)
        out=subprocess.run(cmd+["-o","AntimonyCesium.olean",p.name],cwd=tmp,env=env,capture_output=True,text=True)
        if out.returncode:raise ValueError(out.stdout+out.stderr)
        audits=[l for l in out.stdout.splitlines() if "depends on axioms:" in l]
        if len(audits)!=n or any(set(l.split("[")[1].split("]")[0].split(", "))-{"propext","Quot.sound","Classical.choice"} for l in audits):
            raise ValueError(out.stdout)
        print(out.stdout.rstrip())
        (tmp/"False.lean").write_text("import AntimonyCesium\nopen ElementPaper.Batch11\nexample : 6 < cesium := by decide +kernel\n")
        fail=subprocess.run(cmd+["False.lean"],cwd=tmp,env=env,text=True,capture_output=True)
        if fail.returncode==0 or "error: Tactic `decide`" not in fail.stdout:raise ValueError("False control passed")
        print("Rejected false claim 6 < cesium. The first ordinary cesium crossing is outside the wall and inside at cutoff 6.")

if __name__=="__main__":main()

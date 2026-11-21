"""Check the prewritten heavy-anion and lithium-like shell forecasts in core Lean."""
import argparse
import csv
import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
PAPER=HERE.parents[1]
ARCHIVE=PAPER.parents[1]/"data/element_thresholds_20261011.json.gz"
SHA="75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
# Forecast registered before scoring, in holdouts/heavy_anions_protocol.md.
PREDICTED={76:True,77:False,78:False,79:False,82:True,83:True,84:True,85:False}
PER_CM=F("6.62607015e-34")*299792458*100/F("1.602176634e-19")


def table(path):
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def num(x):
    return format(Decimal(x),"f")


def load():
    if hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()!=SHA:
        raise ValueError("Pinned archive changed")
    with gzip.open(ARCHIVE,"rt") as stream:
        records=json.load(stream,parse_float=Decimal)["records"][:85]
    if [a["Z"] for a in records]!=list(range(1,86)):
        raise ValueError("Missing atomic number")
    for a in records:
        if [t["q"] for t in a["thresholds"]]!=list(range(a["Z"])):
            raise ValueError("Missing ion charge")
    aff={}
    printed={}
    for batch,filename in [(16,"batch16_os_hg.csv"),(17,"batch17_tl_at.csv")]:
        folder=PAPER/f"batch{batch}/ladder"
        for r in table(folder/"affinities.csv"):
            aff[int(r["Z"])]=r
        for r in table(folder/filename):
            printed[int(r["Z"]),int(r["k"])]=r
    for z in range(76,86):
        row=printed[z,0]
        ea=aff[z]["EA_eV"]
        if not ea:
            if any(row[k] for k in ("IE_k (eV)","z_k","Gamma_k")):
                raise ValueError(f"Spurious numeric primary affinity in Z={z} ladder")
            continue
        e=F(ea)
        y=F(records[z-1]["thresholds"][0]["IE_eV"])
        if (F(row["IE_k (eV)"]),F(row["z_k"]),F(row["Gamma_k"]))!=(e,round(y/e,6),round((y-e)/(y+e),6)):
            raise ValueError(f"Wrong printed heavy anion rung at Z={z}")
    return records,aff


def source(records,aff):
    out=["-- Generated from the pinned archive and the batch 16–17 affinity evidence tables.",
         "import HeavyChambers","", "namespace ElementPaper.HeavyChambers",
         "open VOTKP.NearestPair", "open ElementPaper.Batch12 (endpointLo endpointHi admitsInside admitsOutside)",
         "set_option maxRecDepth 8192", "set_option maxHeartbeats 10000000","",
         "/-- Beginning at lithium: each pair is (last 2s IE, u, first 1s IE, u), in eV. -/",
         "def kOpenings : List Face :="]
    encoded=[]
    for atom in records[2:]:
        a,b=atom["thresholds"][atom["Z"]-3:atom["Z"]-1]
        ns=[a["IE_eV"],a["unc_eV"],b["IE_eV"],b["unc_eV"]]
        encoded.append("⟨"+", ".join(map(num,ns))+"⟩")
    out.extend(["  ["+",\n   ".join(encoded)+"]","",
                "def goldK := kOpenings[76]'(by decide +kernel)", "def mercuryK := kOpenings[77]'(by decide +kernel)","",
                "theorem fullFirstCrossing : kOpenings.length = 83 ∧",
                "    (kOpenings.take 77).all aboveFour = true ∧ (kOpenings.drop 77).all belowFour = true ∧",
                "    (kOpenings.zip kOpenings.tail).all (fun (a,b) => decide (endpointHi b < endpointLo a)) = true := by",
                "  decide +kernel", "",
                "theorem goldMercuryK : aboveFour goldK = true ∧ belowFour mercuryK = true ∧",
                "    admitsInside goldK = true ∧ admitsInside mercuryK = true := by decide +kernel",""])
    audits=["strictlyAbove","strictlyBelow","descending","sameCutForEveryInput","fullFirstCrossing","goldMercuryK"]
    ppath=PAPER/"holdouts/k_opening/predictions.csv"
    if hashlib.sha256(ppath.read_bytes()).hexdigest()!="a2fe1e2a9644c9f2725e5a2259dcd52703832fdc98ee7a31194c02edca1a28cd":
        raise ValueError("Frozen forecast changed")
    models=table(ppath)
    if [int(m["Z"]) for m in models]!=list(range(71,86)):
        raise ValueError("Unexpected forecast keys")
    pairs=[f"({m['linear_from_65_70']},{m['dirac_plus_constant_over_Z']})" for m in models]
    out.extend(["def frozenModels : List (Rat × Rat) :=", "  ["+", ".join(pairs)+"]",
                "def scored := (kOpenings.drop 68).zip frozenModels", "",
                "theorem linearAlwaysNearer : scored.length = 15 ∧",
                "    scored.all (fun (f,m) => nearerTest f m) = true := by decide +kernel","",
                "theorem forecastBoxCoverage :",
                "    (scored.zipIdx.filterMap (fun ((f,m),i) => if whollyIn f m.1 then some (i+71) else none)) = [71,80] ∧",
                "    scored.all (fun (f,m) => whollyIn f m.1 || whollyOut f m.1) = true ∧",
                "    scored.all (fun (f,m) => whollyOut f m.2) = true := by decide +kernel",""])
    audits.extend(["nearerOnLeft","nearerAcrossFullBox","linearAlwaysNearer","forecastBoxCoverage"])
    forecasts=[]
    for z in range(76,86):
        a=records[z-1]
        r=aff[z]
        if not r["EA_eV"]:
            continue
        t=a["thresholds"][0]; name=a["name"]
        out.extend([f"def {name}EA : Face := ⟨{r['EA_eV']}, {r['unc_eV']}, {num(t['IE_eV'])}, {num(t['unc_eV'])}⟩"])
        if z in PREDICTED:
            forecasts.append("⟨"+f"{z},{name}EA,{str(PREDICTED[z]).lower()}"+"⟩")
    out.extend(["","/-- Polonium has no final ground-state primary point in the evidence selection. -/",
                "def primary : List Forecast := ["+", ".join(forecasts)+"]","",
                "theorem primarySeven : primary.map Forecast.z = [76,77,78,79,82,83,85] ∧",
                "    primary.all predictionSupported = true ∧ primary.all leavesWindow = true ∧",
                "    primary.all (fun r => chemistry r.face) = true := by decide +kernel","",
                "theorem thalliumComparison : admitsOutside ThalliumEA = true := by decide +kernel","",
                "/-- Both gold readings are inside the loop wall, on opposite sides of the bare reference four. -/",
                "theorem goldOppositeAtFour : belowFour GoldEA = true ∧ aboveFour goldK = true ∧",
                "    admitsInside GoldEA = true ∧ admitsInside goldK = true := by decide +kernel","",
                "def inverseCmToEV : Rat := "+str(PER_CM.numerator)+"/"+str(PER_CM.denominator),"",
                "/-- The second argument is an assumed half-width in cm⁻¹, not an inferred systematic uncertainty. -/",
                "def polonium (wave halfWidth : Rat) : Face :=",
                "  ⟨wave * inverseCmToEV, halfWidth * inverseCmToEV, "+
                num(records[83]["thresholds"][0]["IE_eV"])+", "+num(records[83]["thresholds"][0]["unc_eV"])+"⟩","",
                "theorem poloniumStatisticalOnly :",
                "    admitsInside (polonium 11905.631 0.009) = true ∧",
                "    predictionSupported ⟨84,polonium 11905.631 0.009,true⟩ = false := by decide +kernel","",
                "theorem poloniumIfInDisplayedRange :",
                "    let f := polonium 11875 75",
                "    (f.a-f.ua = 11800*inverseCmToEV ∧ f.a+f.ua = 11950*inverseCmToEV) ∧",
                "    admitsInside f = true ∧ leavesWindow ⟨84,f,false⟩ = true ∧",
                "    predictionSupported ⟨84,f,true⟩ = false := by decide +kernel","",
                "/-- Even the archived IE uncertainty is allowed when bracketing the forward wall at fixed wavenumber. -/",
                "theorem poloniumCriticalBracket :",
                "    admitsOutside (polonium 11649.160 0) = true ∧",
                "    admitsInside (polonium 11649.172 0) = true ∧",
                "    (11905.631:Rat)-11649.172 = 256.459 := by decide +kernel",""])
    audits.extend(["primarySeven","thalliumComparison","goldOppositeAtFour","poloniumStatisticalOnly",
                   "poloniumIfInDisplayedRange","poloniumCriticalBracket"])
    out.extend(["theorem controlsFalse : belowFour goldK = false ∧ aboveFour mercuryK = false ∧",
                "    84 ∉ primary.map Forecast.z ∧",
                "    predictionSupported ⟨84,polonium 11875 75,true⟩ = false := by decide +kernel",""])
    audits.append("controlsFalse")
    out.extend(["#print axioms "+n for n in audits])
    out.extend(["","end ElementPaper.HeavyChambers",""])
    return "\n".join(out),audits


def verify_independent(src,records,aff):
    with gzip.open(ARCHIVE,"rt") as f:
        r=json.load(f,parse_float=F)["records"]
    block=re.search(r"def kOpenings : List Face :=\s*\[(.*?)\]",src,re.S)[1]
    encoded=[[F(v.strip()) for v in item.split(",")] for item in re.findall(r"⟨([^⟩]+)⟩",block)]
    actual=[]
    bounds=[]
    for a in r[2:85]:
        s,t=a["thresholds"][a["Z"]-3:a["Z"]-1]
        x,u,y,v=map(F,(s["IE_eV"],s["unc_eV"],t["IE_eV"],t["unc_eV"]))
        actual.append([x,u,y,v])
        bounds.append(((y-v)/(x+u),y/x,(y+v)/(x-u)))
    if actual!=encoded:
        raise ValueError("Generated 83 shell energy/uncertainty pairs differ")
    if not (all(b[0]>4 for b in bounds[:77]) and all(b[2]<4 for b in bounds[77:]) and
            all(i[0]>j[2] for i,j in zip(bounds,bounds[1:]))):
        raise ValueError("Frozen first crossing or interval separation failed")
    print("83 K-opening rows re-parsed from Lean; all 82 adjacent intervals are disjoint and descending.")
    for z in [79,80]:
        lo,y,hi=bounds[z-3]
        print(f"K Z={z}: {float(y):.12f}, [{float(lo):.12f},{float(hi):.12f}].")
    for z in range(76,86):
        if not aff[z]["EA_eV"]:
            continue
        name=records[z-1]["name"]
        exact=[F(v.strip()) for v in re.search(rf"def {name}EA : Face := ⟨(.*?)⟩",src)[1].split(",")]
        t=r[z-1]["thresholds"][0]
        expect=[F(aff[z]["EA_eV"]),F(aff[z]["unc_eV"]),F(t["IE_eV"]),F(t["unc_eV"])]
        if exact!=expect:
            raise ValueError(f"Source mismatch for {name}")
        x,u,y,v=exact
        label=2*(y-x)**2>(y+x)**2
        if z in PREDICTED and label!=PREDICTED[z]:
            raise ValueError(f"Heavy primary central forecast failed at {name}")
        print(f"{name}: IE={y}, EA={x}, z={float(y/x):.9f}, Gamma={float((y-x)/(y+x)):.9f}, "
              f"rectangular [{float((y-v)/(x+u)):.9f},{float((y+v)/(x-u)):.9f}], "
              f"{'outside' if label else 'inside'}"+(" (comparison only)" if z not in PREDICTED else ""))
    if aff[84]["EA_eV"] or aff[80]["EA_eV"]:
        raise ValueError("Unexpected numeric Po or Hg in primary input")
    pt=r[83]["thresholds"][0]
    for w,u in [(F("11905.631"),F(".009")),(F(11875),F(75))]:
        e,de=F(pt["IE_eV"]),F(pt["unc_eV"])
        lo=(e-de)/((w+u)*PER_CM)
        hi=(e+de)/((w-u)*PER_CM)
        print(f"Polonium conditional {w}±{u} cm^-1: z in [{float(lo):.9f}, {float(hi):.9f}].")
    print("Seven sourced primary predictions supported. Po separately conditional; Tl excluded from predictions.")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--generate",action="store_true")
    parser.add_argument("--lean",default="lean")
    parser.add_argument("--checked-dependencies",type=Path,
                        help="Use previously built dependency oleans with identical accompanying source files.")
    args=parser.parse_args()
    records,aff=load()
    s,audits=source(records,aff)
    path=HERE/"HeavyPredictions.lean"
    if args.generate:
        path.write_text(s)
    if path.read_text()!=s:
        raise ValueError("Regenerated source differs")
    verify_independent(s,records,aff)
    files=[PAPER/"batch10/nearest_lean/MarginBounds.lean",PAPER/"batch11/lean/Batch11Kernel.lean",
           PAPER/"batch11/lean/AntimonyCesium.lean",PAPER/"batch12/lean/Batch12Bounds.lean",
           HERE/"HeavyChambers.lean",path]
    print(subprocess.check_output([args.lean,"--version"],text=True).strip(),flush=True)
    with tempfile.TemporaryDirectory() as td:
        tmp=Path(td)
        env=dict(os.environ,LEAN_PATH=td)
        for p in files:
            shutil.copyfile(p,tmp/p.name)
            if args.checked_dependencies and p.parent!=HERE:
                cached=args.checked_dependencies/p.name
                if cached.read_bytes()!=p.read_bytes():
                    raise ValueError(f"Cached source differs for {p.name}")
                shutil.copyfile(cached.with_suffix(".olean"),(tmp/p.name).with_suffix(".olean"))
                print(f"Reusing previously checked {p.stem}.olean, identical source SHA-256 "
                      +hashlib.sha256(p.read_bytes()).hexdigest())
                continue
            run=subprocess.run([args.lean,"-j1","-o",p.stem+".olean",p.name],
                               cwd=tmp,env=env,capture_output=True,text=True)
            if run.returncode:
                raise RuntimeError(run.stdout+run.stderr)
        found=re.findall(r"'ElementPaper\.HeavyChambers\.(\w+)' depends on axioms: \[([^\]]+)\]",run.stdout)
        if [n for n,_ in found]!=audits or any(set(re.split(r",\s*",a))-{"propext","Quot.sound","Classical.choice"} for _,a in found):
            raise RuntimeError("Unexpected axiom scan\n"+run.stdout)
        print(run.stdout.rstrip())
        controls={
            "gold helium-core opening is below four":"belowFour goldK = true",
            "mercury helium-core opening exceeds four":"aboveFour mercuryK = true",
            "polonium is a primary scored case":"84 ∈ primary.map Forecast.z",
            "stated Po display window supports outside":"predictionSupported ⟨84,polonium 11875 75,true⟩ = true",
        }
        lines=["import HeavyPredictions","open ElementPaper.HeavyChambers"]
        expected={}
        for title,claim in controls.items():
            lines.append(f"example : {claim} := by decide +kernel")
            expected[len(lines)]=title
        (tmp/"Wrong.lean").write_text("\n".join(lines)+"\n")
        out=subprocess.run([args.lean,"-j1","Wrong.lean"],cwd=tmp,env=env,text=True,capture_output=True)
        errs=[(int(i),msg) for i,msg in re.findall(r"^Wrong.lean:(\d+):\d+: error(?:\([^)]+\))?: ([^\n]+)",out.stdout,re.M)]
        if out.returncode==0 or [k for k,_ in errs]!=list(expected) or any(not msg.startswith("Tactic `decide`") for _,msg in errs):
            raise RuntimeError("Invalid false control\n"+out.stdout+out.stderr)
        for title in controls:
            print("Rejected: "+title)
    print(f"{len(audits)} axiom audits passed. Four false controls rejected.")


if __name__=="__main__":
    main()

"""Regenerate the Lean certificate, audit every archive row and run both controls."""
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

HERE = Path(__file__).resolve().parent
SHA256 = "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
CORES = {2:"Helium", 10:"Neon", 18:"Argon", 36:"Krypton", 54:"Xenon", 86:"Radon"}
FIELDS = ("a","ua","b","ub")


def generate(archive):
    raw = archive.read_bytes()
    if hashlib.sha256(raw).hexdigest() != SHA256:
        raise ValueError("Archive differs from bcedbd9")
    data = json.loads(gzip.decompress(raw),parse_float=Decimal)["records"]
    if [r["Z"] for r in data] != list(range(1,119)):
        raise ValueError("Missing archive record")
    text = ["-- Generated central values and quoted uncertainties in eV. Each face row is",
            "-- (a, δa, b, δb) for consecutive charges q=Z−N−1, q+1, with occupancy N.",
            "import MarginBounds", "namespace VOTKP.NearestPair", "",
            "set_option maxRecDepth 8192", "set_option maxHeartbeats 10000000", "",
            "def consecutive (core startZ : Nat) (faces : List Face) : List OpeningPair :=",
            "  (faces.zip faces.tail).zipIdx.map fun ((a, b), k) => ⟨core, startZ+k, a, b⟩", ""]
    for core,symbol in CORES.items():
        faces = []
        for rec in data:
            q = rec["Z"]-core-1
            th = {t["q"]:t for t in rec["thresholds"]}
            if q not in th or q+1 not in th:
                continue
            if rec["Z"] != core+1+len(faces):
                raise ValueError("A core series has an internal gap; refuse to bridge it")
            a,b = th[q],th[q+1]
            values=[a["IE_eV"],a["unc_eV"],b["IE_eV"],b["unc_eV"]]
            if any(v is None for v in values):
                raise ValueError("Missing uncertainty")
            faces.append("⟨"+", ".join(format(Decimal(v),"f") for v in values)+"⟩")
        text += [f"def {symbol}Pairs : List OpeningPair := consecutive {core} {core+1}",
                 "  ["+",\n   ".join(faces)+"]","",
                 f"theorem check{symbol} : {symbol}Pairs.all certify = true := by decide +kernel",""]
    text += ["def allPairs : List OpeningPair :=", "  "+" ++ ".join(n+"Pairs" for n in CORES.values()),"",
             "theorem coversAndHasOneTarget : allPairs.length = 427 ∧",
             "    ((allPairs.filter target).map fun p => (p.core,p.leftZ)) = [(2,6)] := by",
             "  decide +kernel", "",
             "theorem allCuts : allPairs.all certify = true := by",
             "  simp only [allPairs, List.all_append, "+", ".join("check"+n for n in CORES.values())+", Bool.and_self]", "",
             "/-- Every admissible realization of the unique helium-core carbon–nitrogen",
             "pair is closer to ideal than every realization of any other listed pair. -/",
             "theorem uniquelyNearest {p q : OpeningPair} (hp : p ∈ allPairs) (hq : q ∈ allPairs)",
             "    (tp : target p = true) (tq : target q = false) {m n : Rat}",
             "    (hm : AdmissibleMargin p m) (hn : AdmissibleMargin q n) : m.abs < n.abs :=",
             "  nearestFromCuts (List.all_eq_true.mp allCuts p hp) (List.all_eq_true.mp allCuts q hq)",
             "    tp tq hm hn", "",
             "/-- The nearest rival's box (argon-core potassium with calcium) is farther",
             "away than the upper cut for the winner, even at its closest endpoint. -/",
             "theorem wrongWinner : (ArgonPairs[0]?).any (fun p =>",
             "    decide ((-(31/10000) : Rat) < low p ∧ high p < 31/10000)) = false := by",
             "  decide +kernel",""]
    for name in ["powerBounds","certifiedCut","nearestFromCuts"]+["check"+n for n in CORES.values()]+[
            "coversAndHasOneTarget","allCuts","uniquelyNearest","wrongWinner"]:
        text.append("#print axioms "+name)
    return "\n".join(text+["","end VOTKP.NearestPair",""])


def verify_keys(source, archive, pair_csv):
    # Independent enumeration in the opposite order: scan every observed physical
    # charge, infer the core occupancy, then intersect keys for Z and Z+1.
    with gzip.open(archive,"rt") as f:
        fresh=json.load(f,parse_float=Fraction)["records"]
    expected={}
    for rec in fresh:
        by_charge={t["q"]:t for t in rec["thresholds"]}
        for q,row in by_charge.items():
            n=rec["Z"]-q-1
            if n in CORES and q+1 in by_charge:
                following=by_charge[q+1]
                expected[n,rec["Z"]]=tuple(Fraction(v) for v in [
                    row["IE_eV"],row["unc_eV"],following["IE_eV"],following["unc_eV"]])
    got={}
    for n,name in CORES.items():
        block=re.search(rf'def {name}Pairs : List OpeningPair := consecutive (\d+) (\d+)\s*\[(.*?)\]',source,re.S)
        if not block or int(block[1])!=n:
            raise ValueError("Missing core block")
        for j,row in enumerate(re.findall(r"⟨([^⟩]+)⟩",block[3]),int(block[2])):
            got[n,j]=tuple(Fraction(v.strip()) for v in row.split(","))
    if got!=expected:
        raise ValueError("Lean input literals or their (core,Z) keys differ")
    pairs={(n,z) for (n,z) in expected if (n,z+1) in expected}
    inverse={name.lower():n for n,name in CORES.items()}
    with pair_csv.open(newline="") as f:
        printed=list(csv.DictReader(f))
    printed_keys={(inverse[i["core"]],int(i["Z_left"])) for i in printed}
    if (printed_keys!=pairs or len(printed)!=len(pairs) or len(pairs)!=427 or
        any(int(i["Z_right"])!=int(i["Z_left"])+1 for i in printed)):
        raise ValueError("Mixed-map comparison keys differ or were duplicated")
    print(f"Reparsed {len(got)} energy/uncertainty tuples from Lean; all {len(pairs)} adjacent keys match archive and published packet.")


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("archive",type=Path)
    p.add_argument("pairs_csv",type=Path)
    p.add_argument("--lean",default="lean")
    p.add_argument("--generate",action="store_true")
    args=p.parse_args()
    src=HERE/"ClosestCarbonNitrogen.lean"
    s=generate(args.archive)
    if args.generate:
        src.write_text(s)
    if src.read_text()!=s:
        raise ValueError("Generated source differs")
    verify_keys(src.read_text(),args.archive,args.pairs_csv)
    print(subprocess.check_output([args.lean,"--version"],text=True).strip(),flush=True)
    with tempfile.TemporaryDirectory() as temp:
        work=Path(temp)
        env=dict(os.environ,LEAN_PATH=temp)
        command=[args.lean,"-j1"]
        for name in ["MarginBounds.lean",src.name]:
            (work/name).write_bytes((HERE/name).read_bytes())
        subprocess.run(command+["-o","MarginBounds.olean","MarginBounds.lean"],cwd=work,env=env,check=True)
        audit=subprocess.check_output(command+["-o","ClosestCarbonNitrogen.olean",src.name],cwd=work,env=env,text=True)
        if audit.count("depends on axioms: [propext, Classical.choice, Quot.sound]")!=13:
            raise ValueError(audit)
        print(audit.rstrip())
        control="""import ClosestCarbonNitrogen
open VOTKP.NearestPair
example : (ArgonPairs[0]?).any (fun p => decide ((-(31/10000):Rat) < low p ∧ high p < 31/10000)) = true := by decide +kernel
"""
        (work/"Control.lean").write_text(control)
        r=subprocess.run(command+["Control.lean"],cwd=work,env=env,text=True,capture_output=True)
        if r.returncode==0 or r.stdout.count("error:")!=1 or "error: Tactic `decide`" not in r.stdout:
            raise ValueError("Wrong-winner control did not fail as expected")
        print("Rejected wrong winner: argon-core potassium with calcium fails the carbon–nitrogen envelope.")


if __name__=="__main__":
    main()

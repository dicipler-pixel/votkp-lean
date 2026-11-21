"""Generate and check exact palladium to tin ordinary and filled-subshell certificates."""
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
ARCHIVE_DIGEST = "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"
NAMES = ("Palladium", "Silver", "Cadmium", "Indium", "Tin")
SYMBOLS = ("Pd", "Ag", "Cd", "In", "Sn")


def build(archive, printed):
    raw = archive.read_bytes()
    if hashlib.sha256(raw).hexdigest() != ARCHIVE_DIGEST:
        raise ValueError("Archive differs from bcedbd9")
    data = json.loads(gzip.decompress(raw), parse_float=Decimal)["records"]
    text = ["-- Archive at bcedbd9. k=1 is the first ordinary rung.", "import OrdinaryGaZr",
            "namespace VOTKP.ElementBatch10", "open VOTKP.ElementBatches7And8", ""]
    with printed.open(newline="") as f:
        rows = list(csv.DictReader(f))
    if [(int(r["Z"]), int(r["k"])) for r in rows] != [(z,k) for z in range(46,51) for k in range(z+1)]:
        raise ValueError("Wrong public CSV row order")
    audit = []
    for z, (name, symbol) in enumerate(zip(NAMES,SYMBOLS), 46):
        thresholds = data[z-1]["thresholds"]
        rowset = [r for r in rows if r["symbol"] == symbol and int(r["k"]) > 0]
        if not (data[z-1]["symbol"] == symbol and [t["q"] for t in thresholds] == list(range(z)) and len(rowset) == z):
            raise ValueError("Incomplete inputs")
        values = [format(Decimal(t["IE_eV"]), "f") for t in thresholds]
        if list(map(Fraction,values)) != [Fraction(r["IE_k (eV)"]) for r in rowset]:
            raise ValueError("CSV energy differs from archive")
        groups = [", ".join(values[i:i+6]) for i in range(0,z,6)]
        text += [f"def {name} : List Rat :=", "  [" + ",\n   ".join(groups) + "]", ""]
        audit.append("ordinary"+name)
        text += [f"theorem ordinary{name} : {name}.length = {z} ∧ checkLadder {name} [] = true := by",
                 "  decide +kernel", ""]
    # The first value is an external affinity. Audit it against Ning & Lu (2022) Table 3.
    if (rows[0]["source"], Fraction(rows[0]["IE_k (eV)"])) != ("EA22", Fraction("0.56214")):
        raise ValueError("Palladium affinity differs from Ning & Lu Table 3")
    text += [f"def palladiumEA : Rat := {rows[0]['IE_k (eV)']}", ""]
    ratios = []
    walls = []
    for j, name in enumerate(NAMES):
        lower = f"{name}[{j-1}]!" if j else "palladiumEA"
        upper = f"{name}[{j}]!"
        ratios.append(f"({upper} / {lower})")
        walls.append(f"checkWall {lower} {upper} {'true' if j==0 else 'false'} = true")
    text += ["/-- Crossing numbers 0,1,2,3,4 in element order. Only palladium uses the affinity. -/",
             "theorem filled4dWallCalls :", "    "+" ∧\n    ".join(walls)+" := by","  decide +kernel","",
             "/-- The five exact ratios strictly decrease; the first divides by an affinity. -/",
             "theorem filled4dRatiosDecrease :", "    "+" ∧\n    ".join(f"{x} > {y}" for x,y in zip(ratios,ratios[1:]))+
             " := by", "  decide +kernel", "",
             "/-- Removing the anion boundary from palladium removes its only outside crossing. -/",
             "theorem wrongPalladiumFirstOrdinaryOutside : checkLadder Palladium [1] = false := by",
             "  decide +kernel", ""]
    audit += ["filled4dWallCalls","filled4dRatiosDecrease","wrongPalladiumFirstOrdinaryOutside"]
    return "\n".join(text+[f"#print axioms {n}" for n in audit]+["","end VOTKP.ElementBatch10",""])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("archive", type=Path)
    p.add_argument("printed_csv", type=Path)
    p.add_argument("batch8_lean", type=Path)
    p.add_argument("--lean",default="lean")
    p.add_argument("--generate",action="store_true")
    args = p.parse_args()
    output = HERE / "OrdinaryPalladiumTin.lean"
    s = build(args.archive,args.printed_csv)
    if args.generate:
        output.write_text(s)
    if s != output.read_text():
        raise ValueError("Generated Lean differs from checked source")
    with gzip.open(args.archive,"rt") as f:
        raw = json.load(f,parse_float=Decimal)["records"]
    for z,name in enumerate(NAMES,46):
        literals = re.search(rf"def {name} : List Rat :=\s*\[(.*?)\]",output.read_text(),re.DOTALL)
        if not literals or [Fraction(x.strip()) for x in literals[1].split(",")] != [Fraction(t["IE_eV"]) for t in raw[z-1]["thresholds"]]:
            raise ValueError("Serialized Lean literal mismatch")
    with tempfile.TemporaryDirectory() as temp:
        work = Path(temp)
        (work/output.name).write_text(s)
        (work/"OrdinaryGaZr.lean").write_bytes(args.batch8_lean.read_bytes())
        env = dict(os.environ,LEAN_PATH=temp)
        cmd = [args.lean,"-j1"]
        print(subprocess.check_output([args.lean,"--version"],text=True).strip())
        print("All 240 generated Lean energy literals equal the archive and the public CSV.")
        subprocess.run(cmd+["-o","OrdinaryGaZr.olean","OrdinaryGaZr.lean"],cwd=work,env=env,stdout=subprocess.DEVNULL,check=True)
        audit=subprocess.check_output(cmd+[output.name],cwd=work,env=env,text=True)
        if audit.count("depends on axioms: [propext, Classical.choice, Quot.sound]") != 8:
            raise ValueError(audit)
        print(audit.rstrip())
        for old,new in [
                ("checkLadder Palladium [] = true","checkLadder Palladium [1] = true"),
                ("checkWall palladiumEA Palladium[0]! true = true","checkWall palladiumEA Palladium[0]! false = true")]:
            if s.count(old)!=1:
                raise ValueError("Mutation cannot be uniquely applied")
            (work/"Control.lean").write_text(s.replace(old,new))
            probe=subprocess.run(cmd+["Control.lean"],cwd=work,env=env,text=True,capture_output=True)
            if probe.returncode==0 or probe.stdout.count("error:")!=1 or "error: Tactic `decide`" not in probe.stdout:
                raise ValueError("False control unexpectedly failed validation")
            print(f"Rejected false control: {new}")
        print("235 ordinary crossings inside. Five filled 4d¹⁰ crossings in order: outside, inside, inside, inside, inside.")


if __name__ == "__main__":
    main()

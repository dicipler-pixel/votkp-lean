"""Cross-check the weighted same-charge identity in both existing isobar ledgers."""
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
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
PAPER=HERE.parents[1]
ARCHIVE=PAPER.parents[1]/"data/element_thresholds_20261011.json.gz"
HASH="75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"


def sign(x):
    return (x>0)-(x<0)


def run_pair(atoms,z,neutral,path,energy_field):
    with path.open(newline="") as f:
        rows=list(csv.DictReader(f))
    h,l=atoms[z-1],atoms[z-2]
    if [int(r["q"]) for r in rows]!=list(range(z)):
        raise ValueError("Unexpected charge keys")
    gap=neutral
    if F(rows[0][energy_field])!=gap:
        raise ValueError("Neutral anchor differs")
    keypairs=Counter()
    for q,(ha,la) in enumerate(zip(h["thresholds"],l["thresholds"])):
        if ha["q"]!=q or la["q"]!=q:
            raise ValueError("Wrong charge alignment")
        a,b=F(ha["IE_eV"]),F(la["IE_eV"])
        rho=(a-b)/(a+b)
        increment=rho*(a+b)
        next_gap=gap+increment
        if F(rows[q+1][energy_field])!=next_gap or sign(rho)!=sign(next_gap-gap):
            raise ValueError(f"Weighted mass check failed: Z={z}, initial q={q}")
        keypairs[sign(rho),sign(next_gap)]+=1
        if sign(next_gap)!=sign(gap):
            print(f"{h['symbol']}/{l['symbol']} q={q}→{q+1}: rho={rho}, weight {a+b} eV, "
                  f"increment {increment} eV, gap {float(gap):.6f}→{float(next_gap):.6f} eV.")
        gap=next_gap
    matches=sum(n for (local,total),n in keypairs.items() if local==total)
    print(f"{h['symbol']}/{l['symbol']}: all {z-1} increments and all {z} cumulative central gaps reproduced; "
          f"bare sign(rho) equals sign(Q after the step) {matches}/{z-1} times, "
          f"including {sum(n for (local,_),n in keypairs.items() if local==0)} zero increments.")
    return gap


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean",default="lean")
    args=parser.parse_args()
    if hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()!=HASH:
        raise ValueError("Archive differs")
    with gzip.open(ARCHIVE,"rt") as f:
        atoms=json.load(f,parse_float=F)["records"]
    run_pair(atoms,67,F("2863.2"),PAPER/"batch14/materials/ho_dy_decay.csv","Q_Ho_minus_Dy_eV")
    final=run_pair(atoms,82,F(50600),PAPER/"batch17/materials/tl_pb_decay.csv","Q_ground_Pb_minus_Tl_eV")
    if -final-2329!=F("31071.5295484"):
        raise ValueError("Excited daughter correction differs")
    print("Bare Tl endpoint release to the 2329-eV excited state: 31071.5295484 eV.")
    print(subprocess.check_output([args.lean,"--version"],text=True).strip(),flush=True)
    with tempfile.TemporaryDirectory() as td:
        tmp=Path(td)
        env=dict(os.environ,LEAN_PATH=td)
        for stem in ("ShapeScale","Weighted"):
            shutil.copyfile(HERE/(stem+".lean"),tmp/(stem+".lean"))
            proof=subprocess.run([args.lean,"-j1","-o",stem+".olean",stem+".lean"],cwd=tmp,
                                 env=env,capture_output=True,text=True)
            if proof.returncode:
                raise RuntimeError(proof.stdout+proof.stderr)
        matches=re.findall(r"'ElementPaper\.MassAnchors\.Weighted\.(\w+)' depends on axioms: \[([^\]]+)\]",proof.stdout)
        names=re.findall(r"#print axioms ElementPaper\.MassAnchors\.Weighted\.(\w+)",(HERE/"Weighted.lean").read_text())
        if [n for n,_ in matches]!=names or any(set(re.split(r",\s*",a))-{"propext","Classical.choice","Quot.sound"} for _,a in matches):
            raise RuntimeError("Axiom mismatch\n"+proof.stdout)
        print(proof.stdout.rstrip())
    print(f"{len(names)} theorem audits passed.")


if __name__=="__main__":
    main()

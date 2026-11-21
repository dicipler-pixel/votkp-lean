"""Reparse the pinned COD CIF and verify the exact Lean certificate."""
import argparse
import hashlib
import re
import subprocess
import tempfile
from decimal import Decimal
from pathlib import Path

HERE = Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__)
p.add_argument("cif",type=Path)
p.add_argument("--lean",default="lean")
args=p.parse_args()
raw=args.cif.read_bytes()
if hashlib.sha256(raw).hexdigest()!="ac27d99b1c3c9e1d9997917fa41086702ed451ea2e80392132ae3b75dd31eb89":
    raise ValueError("CIF differs from pinned COD 2204812")
source=(HERE/"SeleniumRing.lean").read_text()
payload=source.split("-- BEGIN CIF VALUES")[1].split("-- END CIF VALUES")[0]
encoded=[(int(a),int(b)) for a,b in re.findall(r"band (\d+) (\d+)",payload)]
cif=raw.decode()
def site(value):
    m=re.fullmatch(r"(\d+\.\d+)\((\d+)\)",value)
    digits=len(m[1].split(".")[1])
    center=Decimal(m[1])*100000
    uncertainty=Decimal(m[2]).scaleb(-digits)*100000
    if center!=int(center) or uncertainty!=int(uncertainty):
        raise ValueError("Scaling loses precision")
    return int(center),int(uncertainty)

points={}
for line in cif.splitlines():
    fields=line.split()
    if len(fields)==9 and fields[5]=="Uani" and re.fullmatch(r"Se[1-8]",fields[0]):
        points[int(fields[0][2:])]=list(map(site,fields[1:4]))
if len(points)!=8 or [v for i in range(1,9) for v in points[i]]!=encoded:
    raise ValueError("Coordinates or uncertainties differ")
bonds={tuple(sorted(map(int,t))) for t in re.findall(r"^Se([1-8]) Se([1-8]) \d+\.\d+\(\d+\)$",cif,re.M)}
if bonds!={(i,i+1) for i in range(1,8)}|{(1,8)}:
    raise ValueError("Published bonds differ")
ops=re.search(r"_symmetry_equiv_pos_as_xyz\n(.*?)\nloop_",cif,re.S)[1].splitlines()
if ops!=["'x, y, z'","'-x, y+1/2, -z+1/2'","'-x, -y, -z'","'x, -y-1/2, z-1/2'"]:
    raise ValueError("Unexpected symmetry setting")
print("Pinned CIF: 24 coordinates and their 24 uncertainties match Lean; 8 bonds and 4 symmetry operations verified.")
print(subprocess.check_output([args.lean,"--version"],text=True).strip(),flush=True)
out=subprocess.check_output([args.lean,"-j1",HERE/"SeleniumRing.lean"],text=True)
audits=[s for s in out.splitlines() if s.startswith("'VOTKP.SeleniumRing.")]
if len(audits)!=10 or any("axioms: " in s and set(s.split("[")[1].split("]")[0].split(", "))-{"propext","Quot.sound","Classical.choice"} for s in audits):
    raise ValueError(out)
print(out.rstrip())
with tempfile.TemporaryDirectory() as td:
    bad=Path(td)/"WrongPermutation.lean"
    bad.write_text(source.replace("(determinants badOrder).any (fun d => decide (d.hi < 0)) = true","(determinants badOrder).any (fun d => decide (d.hi < 0)) = false"))
    failed=subprocess.run([args.lean,"-j1",bad],capture_output=True,text=True)
    if failed.returncode==0 or failed.stdout.count("error:")!=1 or "error: Tactic `decide`" not in failed.stdout:
        raise ValueError("Wrong permutation control failure differed")
print("Rejected assigning the nonnegative orientation test to the vertex 3/6 permutation.")

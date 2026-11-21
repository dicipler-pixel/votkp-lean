"""Audit rational witnesses and the frozen class centres without modifying the predictor."""
import argparse
import gzip
import hashlib
import itertools
import json
import os
import re
import runpy
import shutil
import subprocess
import tempfile
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parents[2]
ARCHIVE = PAPER.parents[1]/"data/element_thresholds_20261011.json.gz"
SOURCE = HERE/"XenonContrast.lean"
HASH = "75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lean",default="lean")
    args = parser.parse_args()
    src = SOURCE.read_text()
    assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()==HASH
    with gzip.open(ARCHIVE,"rt") as f:
        atoms = json.load(f,parse_float=F)["records"]
    model = runpy.run_path(str(HERE.parent/"test_xenon_transfer.py"))
    train = [model["window"](c,o,q) for c,o,q in itertools.product((10,18,36),range(3),range(8))]
    centers = model["fit"](train,"first_two_contrast")
    for label,index in [("Zero",0),("Two",2)]:
        value=F(re.search(rf"def center{label} : Rat := ([-\d/]+)",src)[1])
        assert value==F.from_float(centers[index][0])
    boundary = (F(centers[0][0])+F(centers[2][0]))/2
    assert boundary<F(-1,8)
    print(f"Frozen 72-window feature centroids verified. Exact midpoint (class 2 vs 0): {boundary} < −1/8.")
    for z,name in [(58,"cerium"),(59,"praseodymium"),(60,"neodymium")]:
        q=z-56
        ts=atoms[z-1]["thresholds"][q:q+5]
        assert [r["q"] for r in ts]==list(range(q,q+5))
        central=model["window"](54,2,q)
        guess=model["predict"](model["old"]["dims"](central,"first_two_contrast"),centers)
        assert guess==0
        subset=[ts[i] for i in (0,1,2,4)]
        source_quad=re.search(rf"def {name} : Window := ⟨(.*?)⟩",src)[1]
        pairs=[(F(a),F(b)) for a,b in re.findall(r"\(([\d.]+),([\d.]+)\)",source_quad)]
        assert pairs==[(t["IE_eV"],t["unc_eV"]) for t in subset]
        (a,da),(b,db),(c,dc),(e,de)=pairs
        delta=(b-db)**2-(a+da)*(c+dc)
        scale=((b-db)**2/((a+da)*(c+dc)))**8*(e-de)/(a+da)
        assert scale>1
        print(f"{name.capitalize()} q={q}, actual 2, frozen centre predicts {guess}; "
              f"minimum E₂²−E₁E₃ = {delta} eV², conservative scaled logarithm argument {float(scale):.9f} > 1.")
    print(subprocess.check_output([args.lean,"--version"],text=True).strip())
    with tempfile.TemporaryDirectory() as tmp:
        p=Path(tmp)
        shutil.copyfile(SOURCE,p/SOURCE.name)
        env=dict(os.environ,LEAN_PATH=tmp)
        c=[args.lean,"-j1"]
        run=subprocess.run(c+["-o","XenonContrast.olean",SOURCE.name],cwd=p,env=env,capture_output=True,text=True)
        if run.returncode:
            raise RuntimeError(run.stdout+run.stderr)
        names=re.findall(r"^#print axioms (\w+)",src,re.M)
        audits=re.findall(r"'ElementPaper\.XenonContrast\.(\w+)' depends on axioms: \[([^\]]+)\]",run.stdout)
        assert [n for n,_ in audits]==names
        for n,axioms in audits:
            assert set(axioms.split(", "))<={"propext","Classical.choice","Quot.sound"}
        print(run.stdout.rstrip())
        for label,claim in [("cerium can have a nonpositive minimum","positiveCorner cerium ≤ 0"),
                             ("praseodymium is uniformly positive","0 < positiveCorner praseodymium")]:
            (p/"Wrong.lean").write_text("import XenonContrast\nopen ElementPaper.XenonContrast\n"
                                       +f"example : {claim} := by decide +kernel\n")
            wrong=subprocess.run(c+["Wrong.lean"],cwd=p,env=env,capture_output=True,text=True)
            if wrong.returncode==0 or "error: Tactic `decide`" not in wrong.stdout:
                raise RuntimeError(wrong.stdout+wrong.stderr)
            print("Rejected false control: "+label)
    print(f"{len(names)} theorem audits, two controls rejected.")


if __name__=="__main__":
    main()

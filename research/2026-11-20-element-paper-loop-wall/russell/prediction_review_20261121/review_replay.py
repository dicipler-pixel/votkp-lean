"""Replay the self-contained prediction-review Lean files, including the negative control."""
import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

def run():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--lean',default='lean')
    a=p.parse_args()
    compiler=shutil.which(a.lean)
    if not compiler: p.error('Lean executable missing')
    root=a.root.resolve()
    version=subprocess.check_output([compiler,'--version'],text=True).strip()
    print(version,flush=True)
    if 'version 4.34.1,' not in version: raise SystemExit('expected 4.34.1')
    files=('TwoFaceForms.lean','consistency/BoundaryAgreement.lean','angle/ObliqueFaces.lean',
           'rivals/FiniteWallGap.lean','rivals/PellControls.lean','precision/OpticalWall.lean','state_observables/PreparedRoute.lean')
    with TemporaryDirectory() as temp:
        for path in files:
            source=root/path
            args=[compiler]
            if path=='consistency/BoundaryAgreement.lean': args+=['-o',temp+'/BoundaryAgreement.olean']
            r=subprocess.run([*args,str(source.relative_to(root))],cwd=root,capture_output=True,text=True)
            if r.returncode or re.search(r"declaration uses 'sorry'",r.stdout+r.stderr):sys.exit(r.stdout+r.stderr)
            print(path, 'PASS',flush=True)
            for line in r.stdout.splitlines():
                if 'depends on axioms:' in line:
                    axioms=line.split('depends on axioms:')[-1].strip(' []').split(', ')
                    if set(axioms)-{'propext','Classical.choice','Quot.sound'}:sys.exit(line)
                    print(' ',line)
        reject=subprocess.run([compiler,'consistency/controls/FalseAtThird.lean'],cwd=root,
                env=dict(os.environ,LEAN_PATH=temp),capture_output=True,text=True)
        if reject.returncode==0 or not re.search(r"error: .*grind.* failed",reject.stdout+reject.stderr):
            sys.exit('false-control replay failed: '+reject.stdout+reject.stderr)
        print('FalseAtThird.lean REJECTED at its false goal',flush=True)
if __name__=='__main__':run()

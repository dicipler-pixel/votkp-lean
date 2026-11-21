"""Non-self-consistent full shifted meshes on a converged QE charge density."""
import argparse
from itertools import product
import os
from pathlib import Path
import re
import shutil
import subprocess

def run(scf, root, symbol, mesh, pw):
    folder = root / f"{symbol}-{mesh}"
    folder.mkdir(parents=True,exist_ok=True)
    save=folder/"out/system.save"
    save.mkdir(parents=True,exist_ok=True)
    for f in (scf/"out/system.save").iterdir():
        if not f.name.startswith('wfc') and f.is_file(): shutil.copy(f,save/f.name)
    text=(scf/"scf.in").read_text().split('K_POINTS')[0]
    text=text.replace("calculation='scf'", "calculation='nscf'").replace("ibrav=","nosym=.true., noinv=.true., ibrav=")
    # Non-special shift removes symmetry-enforced degeneracies at partially filled shells.
    shifts=(.411,.097,.233)
    text+=f'K_POINTS crystal\n{mesh**3}\n'
    for idx in product(range(mesh),repeat=3):
        k=[(n+s)/mesh for n,s in zip(idx,shifts)]
        text+=' '.join(f'{x:.15f}' for x in k)+f' {1/mesh**3:.15f}\n'
    (folder/'nscf.in').write_text(text)
    env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1')
    with (folder/'nscf.out').open('w') as log:
        subprocess.run([pw,'-in','nscf.in'],cwd=folder,env=env,check=True,stdout=log,stderr=subprocess.STDOUT)
    assert 'JOB DONE.' in (folder/'nscf.out').read_text()

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('scf',type=Path);p.add_argument('root',type=Path)
    p.add_argument('symbol');p.add_argument('mesh',type=int);p.add_argument('--pw',default='pw.x')
    a=p.parse_args();run(a.scf.resolve(),a.root.resolve(),a.symbol,a.mesh,a.pw)

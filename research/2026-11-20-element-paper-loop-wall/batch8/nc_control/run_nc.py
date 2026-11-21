"""Rebuild SCF densities, full shifted NSCF meshes and NC Wigner–Seitz controls.

Requires numpy, scipy and a serial pw.x. The mesh utility is ../ws_control/qe_full_mesh.py
or can be supplied with --mesh-script. The --pps directory holds the verified upstream UPFs.
"""
import argparse
from pathlib import Path
import hashlib
import os
import shutil
import subprocess
import sys


HASHES={
    'Kr':'42d25c77ed07bf438be5b8543f4afd66f10ae46f90d1b80155b6519f4c9bb8c3',
    'Rb':'b40d0424cd413a24da3396b6fb62081bbb13be49acbf1fc666ca976c239ed736',
}


def run(root, pps, element, mesh, grid, pw, mesh_script, semicore, cutoff):
    if hashlib.sha256((pps/f'{element}.upf').read_bytes()).hexdigest()!=HASHES[element]:
        raise ValueError(f'Unexpected pseudopotential for {element}.')
    env=dict(os.environ,OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1')
    scf=root/f'{element}-scf';scf.mkdir(exist_ok=True,parents=True)
    here=Path(__file__).resolve().parent
    inp=(here/f'{element}.scf.in').read_text().replace('@PSEUDO_DIR@',str(pps))
    if cutoff!=75:
        inp=inp.replace('ecutwfc=75, ecutrho=300',f'ecutwfc={cutoff}, ecutrho={4*cutoff}')
    done=scf/'scf.out'
    existing=scf/'scf.in'
    if existing.exists() and existing.read_text()!=inp:
        raise ValueError(f'Existing {existing} differs; choose a fresh work directory.')
    existing.write_text(inp)
    if not done.exists() or 'JOB DONE.' not in done.read_text():
        with done.open('w') as f:
            subprocess.run([pw,'-in','scf.in'],env=env,cwd=scf,stdout=f,stderr=subprocess.STDOUT,check=True)
    result=root/'ws'/f'{element}-{mesh}'
    nscf=result/'nscf.out'
    if not nscf.exists() or 'JOB DONE.' not in nscf.read_text():
        subprocess.run([sys.executable,str(mesh_script),str(scf),str(root/'ws'),element,str(mesh),'--pw',pw],check=True,env=env)
    args=[sys.executable,str(here/'nc_projector.py'),str(result/'out/system.save'),element,str(mesh),str(grid)]
    if semicore: args.append('--include-semicore')
    subprocess.run(args,check=True,env=env)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('work',type=Path);parser.add_argument('pps',type=Path)
    parser.add_argument('element',choices=HASHES);parser.add_argument('mesh',type=int)
    parser.add_argument('grid',type=int);parser.add_argument('--include-semicore',action='store_true')
    parser.add_argument('--pw',default='pw.x')
    parser.add_argument('--cutoff',type=int,choices=[60,75],default=75)
    parser.add_argument('--mesh-script',type=Path,default=Path(__file__).resolve().parents[1]/'ws_control/qe_full_mesh.py')
    args=parser.parse_args()
    run(args.work.resolve(),args.pps.resolve(),args.element,args.mesh,args.grid,shutil.which(args.pw) or args.pw,args.mesh_script.resolve(),args.include_semicore,args.cutoff)

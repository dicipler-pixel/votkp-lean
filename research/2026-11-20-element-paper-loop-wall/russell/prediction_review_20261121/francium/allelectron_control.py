"""Run QE ld1.x radial all-electron total energy differences for alkali p holes."""
import argparse
import csv
import itertools
import json
import os
import re
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal
from pathlib import Path

# Each prefix ends at the filled ns orbital before the closed np subshell.
ION_CORE={'Rb':('[Ar] 3d10 4s2',4), 'Cs':('[Kr] 4d10 5s2',5),
          'Fr':('[Xe] 4f14 5d10 6s2',6)}

def calculate(task):
    program, atom, rel, dft, dx, state, outdir=task
    core, n=ION_CORE[atom]
    p=f'{n}p'
    configs={'neutral': f'{p}6 {n+1}s1','ion': f'{p}6',
             'dication_ground': f'{p}5','dication_excited': f'{p}1 {p}4'}
    inp=("&input\n"+f" atom='{atom}', iswitch=1, rel={rel}, lsd=0, dft='{dft}',\n"
         +f" config='{core} {configs[state]}',\n"
         +f" xmin=-9.0, dx={dx}, rmax=100.0, tr2=1.0d-12,\n"
         +" rytoev_fact=13.605693122994, prefix='atom'\n/\n")
    with tempfile.TemporaryDirectory() as work:
        completed=subprocess.run([str(program)],input=inp,text=True,capture_output=True,
            cwd=work,env={**os.environ, 'UCX_VFS_ENABLE':'n','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','HWLOC_COMPONENTS':'-linux'},timeout=90)
    output=completed.stdout
    if completed.returncode or 'End of All-electron run' not in output:
        raise RuntimeError(f'{atom} {rel} {state} {dx} {dft}: {completed.stderr[-600:]} {output[-1500:]}')
    m=re.search(r'Etot =\s*([-0-9.]+) Ry,\s*([-0-9.]+) Ha,\s*([-0-9.]+) eV',output)
    conv=re.search(r'final scf error:\s*(\S+) reached in\s*(\d+) iterations', output)
    if not m or not conv or float(conv[1])>1.1e-12:
        raise ValueError((atom,rel,state,dx,dft,'SCF/precision check'))
    occup=[]
    if rel==2:
        pattern=rf'^\s*{n} 1 ([0-9.]+) {p.upper()} 1\(\s*([0-9.]+)\)'
        occup=[(float(j),float(q)) for j,q in re.findall(pattern,output,flags=re.M)]
        expected={'neutral':[(0.5,2.0),(1.5,4.0)], 'ion':[(0.5,2.0),(1.5,4.0)],
                  'dication_ground':[(0.5,2.0),(1.5,3.0)], 'dication_excited':[(0.5,1.0),(1.5,4.0)]}
        if occup!=expected[state]:
            raise ValueError((atom,rel,state,'hole-identity check',occup))
    sample=(atom=='Fr' and rel==2 and dft=='PBE' and dx==0.00625)
    if sample:
        (outdir/f'ld1_Fr_{state}.in').write_text(inp)
        (outdir/f'ld1_Fr_{state}.out').write_text(output)
    return dict(atom=atom,rel=rel,functional=dft,dx=dx,state=state,total_eV=m[3],
                residual=conv[1],iterations=int(conv[2]),p_occupations=json.dumps(occup))


def write_csv(path, rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,rows[0].keys());w.writeheader();w.writerows(rows)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('ld1',type=Path)
    ap.add_argument('--out',type=Path,default=Path(__file__).parent)
    ap.add_argument('--workers',type=int,default=2)
    a=ap.parse_args()
    p=a.ld1.resolve(); out=a.out.resolve()
    grid=list(itertools.product(ION_CORE,(0,1,2),('PBE','PZ'),(.0125,.00625)))
    tasks=[(p,atom,rel,dft,dx,s,out) for atom,rel,dft,dx in grid
        for s in (['neutral','ion','dication_ground']+(['dication_excited'] if rel==2 else []))]
    with ThreadPoolExecutor(max_workers=a.workers) as pool:
        rows=list(pool.map(calculate,tasks))
    write_csv(out/'allelectron_totals.csv',rows)
    summary=[]
    for atom,rel,dft,dx in grid:
        energies={r['state']:Decimal(r['total_eV']) for r in rows if (r['atom'],r['rel'],r['functional'],r['dx'])==(atom,rel,dft,dx)}
        i1=energies['ion']-energies['neutral']; i2=energies['dication_ground']-energies['ion']
        upper=(energies['dication_excited']-energies['ion']) if rel==2 else None
        summary.append(dict(atom=atom,rel=rel,functional=dft,dx=dx,IE1_eV=i1,IE2_eV=i2,
            ratio=i2/i1,upper_threshold_eV=upper,fine_split_eV=(upper-i2 if upper is not None else None)))
    write_csv(out/'allelectron_summary.csv',summary)
    print(f'Checked {len(rows)} states in {len(grid)} comparisons.')

if __name__=='__main__':
    main()

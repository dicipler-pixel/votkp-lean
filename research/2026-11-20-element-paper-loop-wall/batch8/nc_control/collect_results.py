"""Collect projector output rows and compact SCF diagnostics from completed runs."""
import argparse
import csv
from pathlib import Path
import re

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('work',type=Path);p.add_argument('destination',type=Path)
    args=p.parse_args()
    rows=[]
    for log in sorted((args.work/'projlogs').glob('*.txt')):
        line=log.read_text().strip()
        if not line:continue
        fields=line.split(',')
        if len(fields)!=11:raise ValueError(f'Unexpected projector result in {log}.')
        semicore='semi' in log.stem.split('-')
        ecut=60 if 'lower' in log.stem.split('-') else 75
        neigh={'Rb':8,'Kr':12}[fields[0]]
        frac=float(fields[8]);budget=float(fields[4])
        twist='0.411 0.097 0.233' if 'alternate' in log.stem.split('-') else '0.137 0.271 0.389'
        rows.append([fields[0],ecut,4*ecut,fields[1],fields[2],twist,
                     'outer+semicore' if semicore else 'outer',*fields[3:],
                     f'{budget/(3*neigh):.9f}',str(frac>1/3),str(float(fields[6])>budget/(3*neigh))])
    with (args.destination/'results.csv').open('w',newline='') as out:
        w=csv.writer(out,lineterminator='\n');w.writerow(['element','ecutwfc_Ry','ecutrho_Ry','mesh','real_grid','twist_mesh_units','subspace','electrons_per_cell','B','nearest_X_mean','nearest_X_min','nearest_X_max','nearest_shell_fraction','minimum_Gram_eigenvalue','sum_rule_residual','single_link_cutoff','shell_passes','every_direction_passes'])
        w.writerows(rows)
    with (args.destination/'scf_summary.csv').open('w',newline='') as out:
        w=csv.writer(out,lineterminator='\n');w.writerow(['element','ecutwfc_Ry','iterations','final_energy_Ry','last_estimated_scf_error_Ry','irreducible_k_points'])
        for ecut,d in [(75,args.work),(60,args.work/'lower')]:
            for el in ('Rb','Kr'):
                log=d/f'{el}-scf/scf.out'
                if not log.exists():continue
                s=log.read_text()
                if 'JOB DONE.' not in s:continue
                nit=re.findall(r'convergence has been achieved in\s+(\d+) iterations',s)[-1]
                energy=re.findall(r'!\s+total energy\s+=\s+([-\d.]+) Ry',s)[-1]
                error=re.findall(r'estimated scf accuracy\s+<\s+(\S+) Ry',s)[-1]
                count=re.findall(r'number of k points=\s*(\d+)',s)[-1]
                w.writerow([el,ecut,nit,energy,error,count])

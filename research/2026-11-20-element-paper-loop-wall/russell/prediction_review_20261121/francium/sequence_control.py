"""Test the same francium 6p-hole model along the neighboring Rn-like sequence."""
import argparse
import csv
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal
from pathlib import Path
from allelectron_control import ION_CORE, calculate, write_csv


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('ld1',type=Path)
    parser.add_argument('--out',type=Path,default=Path(__file__).parent)
    cfg=parser.parse_args()
    seq=['Rn','Fr','Ra','Ac','Th','Pa','U']
    out=cfg.out.resolve()
    data={r['element']:r for r in csv.DictReader((out/'radonlike.csv').open())}
    ION_CORE.update({a:ION_CORE['Fr'] for a in seq})
    tasks=[(cfg.ld1.resolve(),a,2,func,.00625,state,out) for a in seq for func in ('PBE','PZ')
           for state in ('ion','dication_ground','dication_excited')]
    with ThreadPoolExecutor(max_workers=2) as pool:
        rows=list(pool.map(calculate,tasks))
    result=[]
    for atom in seq:
        for func in ('PBE','PZ'):
            en={r['state']:Decimal(r['total_eV']) for r in rows if (r['atom'],r['functional'])==(atom,func)}
            low=en['dication_ground']-en['ion'];high=en['dication_excited']-en['ion']
            ref=data[atom]
            result.append(dict(atom=atom,initial_charge=ref['ion_charge'],functional=func,
                archive_ground_eV=ref['IE_eV'],archive_unc_eV=ref['unc_eV'],grade=ref['grade'],
                ground_eV=low,upper_eV=high,fine_split_eV=high-low,
                ground_minus_archive_eV=low-Decimal(ref['IE_eV'])))
    write_csv(out/'sequence_energies.csv',result)
    for f in ('PBE','PZ'):
        family=[r for r in result if r['functional']==f]
        a,b,c,d=[row['ground_eV'] for row in family[:4]]
        print(f,'linear interpolated Fr', (a+c)/2,'quadratic interpolated Fr',c+(a-d)/3,'direct Fr',b)

if __name__=='__main__':
    main()

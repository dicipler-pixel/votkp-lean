"""Recheck the committed printed tables, then compare fresh ASD fields separately."""
import csv, gzip, json
from fractions import Fraction as F
from pathlib import Path
from check_batch_range_v2 import check

HERE=Path(__file__).resolve().parent
PAPER=HERE.parent
ARCH=PAPER.parents[1]/'data/element_thresholds_20261011.json.gz'
with gzip.open(ARCH,'rt') as f:
    atoms=json.load(f,parse_float=F)['records']
tables=[(7,31,'checks/batch7.csv'),(8,36,'batch8/ladder/batch8_kr_zr.csv')]
for n in range(12,18):
    file,=PAPER.glob(f'batch{n}/ladder/batch{n}_*.csv')
    tables.append((n,5*n-4,str(file.relative_to(PAPER))))
def opt(v):
    return None if v is None or v=='' else F(v)
mismatches=[]
fresh_count=0
for n,z,path in tables:
    print(n,*check(ARCH,PAPER/path,z,z+4,6))
    if n<12:
        continue
    with (PAPER/f'batch{n}/ladder/asd_states_20261121.csv').open() as f:
        states=list(csv.DictReader(f))
    keys={(int(r['Z']),int(r['q'])) for r in states}
    assert keys=={(a,q) for a in range(z,z+5) for q in range(a)} and len(keys)==len(states)
    for r in states:
        a,q=int(r['Z']),int(r['q'])
        atom=atoms[a-1]
        t=atom['thresholds'][q]
        e=r['NIST_energy_eV']
        live=(F(e.strip('[]()')),opt(r['NIST_unc_eV']),{'[':'S','(':'T'}.get(e[0],'E'),r['NIST_refs'])
        pin=(F(t['IE_eV']),opt(t['unc_eV']),t['grade'],t['references'])
        if live!=pin:
            mismatches.append((atom['symbol'],q+1,pin,live))
        fresh_count+=1
for record in mismatches:
    print('Fresh ASD difference',*record)
assert [(a,q) for a,q,_,_ in mismatches]==[('Nd',1)]
print('Full four-field fresh-ASD records:',fresh_count,'matching:',fresh_count-len(mismatches))

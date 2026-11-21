"""Archive rational controls for the screening sign and the bare shell benchmark."""
import argparse
import gzip
import json
import hashlib
from decimal import Decimal as D
from fractions import Fraction as F
from pathlib import Path
from batch10_ladder import HASH, HARTREE, AFF, exact_q6

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('archive',type=Path)
    path=p.parse_args().archive
    if hashlib.sha256(path.read_bytes()).hexdigest()!=HASH:
        raise ValueError('Archive hash mismatch')
    data=json.loads(gzip.decompress(path.read_bytes()),parse_float=F)['records']
    intervals=[]
    for rec in data[45:50]:
        Z=rec['Z']
        th=rec['thresholds']
        penult=th[-2]
        bare=F(HARTREE)*Z*Z/2
        shift=F(penult['IE_eV'])-bare
        u=F(penult['unc_eV'])
        if Z==46:assert shift+u<0
        else:assert shift-u>0
        print(f"{rec['name']} helium-like energy minus bare one-electron energy: {exact_q6(shift)} eV, input ±{exact_q6(u)} eV")
        # The first line of this series is a rung-0 detachment.
        k=Z-46
        x,dx=(AFF['Pd'][:2] if k==0 else (th[k-1]['IE_eV'],th[k-1]['unc_eV']))
        y,dy=th[k]['IE_eV'],th[k]['unc_eV']
        x,y,dx,dy=map(F,(x,y,dx,dy))
        intervals.append(((y-dy)/(x+dx),(y+dy)/(x-dx)))
    assert all(b[1]<a[0] for a,b in zip(intervals,intervals[1:]))
    print('Filled 4d opening: all four adjacent endpoint intervals are strictly descending; palladium uses rung 0.')
    for rec in data[43:50]:
        Z=rec['Z']
        a,b=rec['thresholds'][Z-29:Z-27]
        x,y=a['IE_eV'],b['IE_eV']
        dx,dy=a['unc_eV'],b['unc_eV']
        ratio=F(y)/x
        lo,hi=(y-dy)/(x+dx),(y+dy)/(x-dx)
        floor=F(16,9)
        if Z==44:assert ratio>floor
        else:assert ratio<floor
        if Z<46:assert lo<floor<hi
        else:assert hi<floor
        print(f"{rec['name']} filled 3d: {exact_q6(ratio)} [{exact_q6(lo)}, {exact_q6(hi)}]; "
              + ('straddles' if lo<floor<hi else 'below')+' bare 16/9.')
    # This double check compares the current silver affinity against the algebraic
    # wall without rounding the irrational ratio itself.
    silver=data[46]['thresholds'][0]
    a,da=map(F,AFF['Ag'][:2]);b,db=map(F,(silver['IE_eV'],silver['unc_eV']))
    assert a>da and 1<(b+db)/(a-da)
    assert 2*((b+db)-(a-da))**2<((b+db)+(a-da))**2
    print('Silver anion remains inside at its largest possible forward ratio from the quoted endpoints.')

if __name__=='__main__':
    main()

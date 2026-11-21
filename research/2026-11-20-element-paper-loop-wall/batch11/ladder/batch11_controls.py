"""Compare homologous p-block openings, uncertainty intervals and normalization."""
import argparse
import csv
import gzip
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from batch11_ladder import HASH, exact_q6

def window(r,n):
    q=r['Z']-n-1
    a,b=r['thresholds'][q:q+2]
    assert (a['q'],b['q'])==(q,q+1)
    x,y,dx,dy=map(F,[a['IE_eV'],b['IE_eV'],a['unc_eV'],b['unc_eV']])
    return y/x,(y-dy)/(x+dx),(y+dy)/(x-dx)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('archive',type=Path)
    p.add_argument('output',type=Path)
    args=p.parse_args()
    raw=args.archive.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=HASH:
        raise ValueError('Archive pin mismatch.')
    r=json.loads(gzip.decompress(raw),parse_float=F)['records']
    flo3,flo4=F(16,9),F(25,16)
    with args.output.open('w',newline='') as f:
        w=csv.writer(f,lineterminator='\n')
        w.writerow(['first_element','second_element','z3d','z4d','normalized_z3d','normalized_z4d',
                    'minimum_absolute_z3d_minus_z4d','minimum_normalized_z4d_minus_z3d'])
        for z in range(31,36):
            e,f=r[z-1],r[z+18-1]
            t3,l3,h3=window(e,28);t4,l4,h4=window(f,46)
            gap1,gap2=l3-h4,l4/flo4-h3/flo3
            assert gap1>0 and gap2>0
            w.writerow([e['name'],f['name'],*map(exact_q6,[t3,t4,t3/flo3,t4/flo4,gap1,gap2])])
    for z in range(49,55):
        e,f=r[z-1],r[z]
        t1, l1, h1=window(e,46);t2,l2,h2=window(f,46)
        assert (t1>t2)==(z<54)
        status='resolved decline' if l1>h2 else 'resolved rise' if h1<l2 else 'interval overlap'
        print(e['name'],'to',f['name'],status)
    for z in range(51,56):
        e=r[z-1];t3,l3,h3=window(e,28);t4,l4,h4=window(e,46)
        assert (t4>t3)==(z<=52)
        print(e['name'],'4d vs 3d:', '4d greater throughout' if l4>h3 else
              '4d smaller throughout' if h4<l3 else 'intervals overlap')
    cs=r[54]; z,lo,hi=window(cs,54)
    assert 2*(lo-1)**2>(lo+1)**2
    print('Cesium xenon core remains outside at the least-open allowed endpoint:',exact_q6(lo))

if __name__=='__main__':
    main()

"""Planar semi-infinite normal-incidence reflectance, with a separate Os axis per optical channel."""
from decimal import Decimal as D
from pathlib import Path
import csv

DIR=Path(__file__).resolve().parent
channels=('Os ordinary','Os extraordinary','Ir polycrystal','Pt film','Au film','Hg liquid')


def run():
    records=list(csv.DictReader((DIR/'optical_brackets.csv').open()))
    out=[]
    for r in records:
        a,b,w,n1,k1,n2,k2=(D(r[key]) for key in ['lambda_low_um','lambda_high_um','lambda_target_um','n_low','k_low','n_high','k_high'])
        assert a<=w<=b
        f=(w-a)/(b-a) if a!=b else D(0)
        n=n1+f*(n2-n1);k=k1+f*(k2-k1)
        R=((n-1)**2+k**2)/((n+1)**2+k**2)
        alpha=4*D('3.141592653589793238462643383')*k/(w*D(1000))
        assert 0<R<1 and n>0 and k>0
        out.append([r['channel'],w,*[f'{x:.8f}' for x in (n,k,R,1-R,1/alpha)]])
    with (DIR/'optics.csv').open('w',newline='') as f:
        writer=csv.writer(f,lineterminator='\n')
        writer.writerow(['channel','wavelength_um','n','k','R_semi_infinite','one_minus_R','intensity_penetration_nm'])
        writer.writerows(out)
    assert len(out)==18
    for c in channels:
        print(c,[r[4] for r in out if r[0]==c])
    o=[D(r[4]) for r in out if r[0]=='Os ordinary']
    e=[D(r[4]) for r in out if r[0]=='Os extraordinary']
    assert all(a!=b for a,b in zip(o,e))
    au=[D(r[4]) for r in out if r[0]=='Au film']
    assert au[-1]>au[0]


if __name__=='__main__':
    run()

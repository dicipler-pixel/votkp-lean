"""Count optical half-power crossings under linear interpolation of the two indices.

The margin sign is exact for decimal ordinates. Ordinary line segments map to
a quadratic in wavelength, so a pair of positive endpoints can still hide a dip.
"""
from fractions import Fraction as Q
from pathlib import Path
import csv

DIR=Path(__file__).resolve().parent


def margin(n,k):
    return (n-3)**2+k*k-8


def crossings(x,n,k,y,m,l):
    # t scales [x,y] to [0,1], q=(n(t)-3)^2 + k(t)^2 - 8.
    dn,dk=m-n,l-k
    a=dn**2+dk**2
    b=2*((n-3)*dn+k*dk)
    c=margin(n,k)
    def q(t):
        return a*t*t+b*t+c
    boundaries=[Q(0),Q(1)]
    if a and 0 < -b/(2*a) < 1:
        boundaries.insert(1,-b/(2*a))
    roots=[]
    for left,right in zip(boundaries,boundaries[1:]):
        f,g=q(left),q(right)
        assert f!=0 and g!=0,'exact endpoint or tangent needs separate classification'
        if f*g>0:continue
        for _ in range(55):
            mid=(left+right)/2
            if q(mid)==0:
                left=right=mid
                break
            if f*q(mid)<0:right=mid
            else:left=mid
        roots.append((float(1000*(x+(y-x)*(left+right)/2)),'upward' if f<0 else 'downward'))
    return roots


def run():
    with (DIR/'os_native_channels.csv').open() as f:
        rows=list(csv.DictReader(f))
    for axis in ('ordinary','extraordinary'):
        vals=[tuple(Q(r[key]) for key in ('wavelength_um','n','k')) for r in rows if r['axis']==axis]
        roots=[]
        for (x,n,k),(y,m,l) in zip(vals,vals[1:]):
            for v,direction in crossings(x,n,k,y,m,l):
                roots.append((x,y,v,direction))
        expected=1 if axis=='ordinary' else 2
        assert len(roots)==expected
        for x,y,v,direction in roots:
            print(axis, int(1000*x),int(1000*y),'nm',f'{v:.3f}',direction)
        if axis=='extraordinary':
            half=Q(1,200)
            for w,n,k in vals:
                if 1000*w not in (600,620,640):continue
                n_min=max(Q(0),abs(n-3)-half)
                n_max=abs(n-3)+half
                lower=n_min**2+(k-half)**2-8
                upper=n_max**2+(k+half)**2-8
                assert lower*upper>0
                print('  native',int(1000*w),float(margin(n,k)),f'rounding-only [{float(lower):.6f}, {float(upper):.6f}]')


if __name__=='__main__':
    run()

"""Shortest chains and oriented triple product in two archived tellurium models."""
from fractions import Fraction as F
from itertools import product
from math import acos, degrees, dist, isclose, sqrt
from pathlib import Path
import re
HERE=Path(__file__).resolve().parent

def unit_cell(x,a,c):
    u,v,w=x
    return float(a*(u-v/2)),float(a*v)*sqrt(3)/2,float(c*w)

def difference(b,a):
    return tuple(v-u for u,v in zip(a,b))

def det(a,b,c):
    return sum(a[j]*(b[(j+1)%3]*c[(j+2)%3]-b[(j+2)%3]*c[(j+1)%3]) for j in range(3))

def chi(points):
    return det(*(difference(b,a) for a,b in zip(points,points[1:])))

def tick(p,turn):
    x,y,z=p
    if turn==1:return -y,x-y,z+F(1,3)
    return y-x,-x,z+F(1,3)

def val(s,key):
    return re.search(r'^'+re.escape(key)+r'\s+(\S+)',s,re.M)[1]

def check(path):
    s=path.read_text()
    n=int(val(s,'_space_group_IT_number'))
    turn={152:1,154:-1}[n]
    assert ('-y,x-y,z+1/3' if turn==1 else '-x+y,-x,1/3+z') in s
    a,c=F(val(s,'_cell_length_a')),F(val(s,'_cell_length_c'))
    assert a==F(val(s,'_cell_length_b'))
    assert [val(s,'_cell_angle_'+i) for i in ['alpha','beta','gamma']]==['90','90','120']
    m=re.search(r'^Te(?:1 Te)?\s+(-?[\d.]+)\s+([\d.]+)\s+([\d.]+)',s,re.M)
    u,v,w=map(F,m.groups());assert v==0
    # The CIFs round the special-position height. A common axial shift cancels
    # from every distance and determinant. Keep the recorded ordinate exactly.
    frac=[(u,v,w)]
    for _ in range(3):frac.append(tick(frac[-1],turn))
    assert frac[-1]==(u,v,w+1)
    pts=[unit_cell(p,a,c) for p in frac]
    length=dist(pts[0],pts[1]);vol=chi(pts)
    assert all(isclose(dist(x,y),length,abs_tol=1e-12) for x,y in zip(pts,pts[1:]))
    # The three distinct sites of this orbit exhaust Z=3 atoms per primitive cell.
    assert int(val(s,'_cell_formula_units_Z'))==len(frac[:-1]) and val(s,'_chemical_formula_sum')=='Te'
    candidates=[]
    # An unexamined |translation| >=3 has horizontal length at least
    # a*sqrt(3)/2 times its largest shifted fractional basal coordinate,
    # or vertical length c times its shifted axial coordinate.
    for p in frac[:-1]:
        for x,y,z in product(range(-2,3),repeat=3):
            coord=unit_cell((p[0]+x,p[1]+y,p[2]+z),a,c)
            d=dist(coord,pts[0])
            if d>1e-10:candidates.append(d)
    ds=sorted(candidates)
    assert all(isclose(d,length,abs_tol=1e-9) for d in ds[:2]) and ds[2]>length+0.1
    basal_delta=max(abs(p[i]-frac[0][i]) for p in frac[:-1] for i in (0,1))
    axial_delta=max(abs(p[2]-frac[0][2]) for p in frac[:-1])
    omitted_lb=min(float(a)*(3-float(basal_delta))*sqrt(3)/2,float(c*(3-axial_delta)))
    assert omitted_lb>ds[2]
    mirrored=[(x,-y,z) for x,y,z in pts]
    assert isclose(chi(mirrored),-vol,abs_tol=1e-10) and isclose(chi(pts[::-1]),vol,abs_tol=1e-10)
    factor=turn*3*sqrt(3)/2*float(c*(a*u)**2)
    assert isclose(vol,factor,abs_tol=1e-10)
    v1=difference(pts[0],pts[1]);v2=difference(pts[2],pts[1])
    angle=degrees(acos(sum(i*j for i,j in zip(v1,v2))/length**2))
    print(f'COD {path.stem}, group {n}: a={float(a):g} Å, c={float(c):g} Å, x={float(u):g}, '
          f'two nearest {length:.6f} Å, next contact {ds[2]:.6f} Å, bond angle {angle:.4f} degrees.')
    print(f'  signed triple in Å³: forward {vol:+.6f}, reversal {chi(pts[::-1]):+.6f}, '
          f'constructed mirror {chi(mirrored):+.6f}.')

if __name__=='__main__':
    for name in ('2020222','9008580'):
        check(HERE/(name+'.cif'))

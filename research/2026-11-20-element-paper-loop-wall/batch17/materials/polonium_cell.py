"""Cubic/rhombohedral alpha and beta Po, 1966 refinement at printed cell centres."""
import csv
import itertools
import math
from pathlib import Path

alpha, beta, ua=3.359,3.368,0.001
angle=98+14.4/60
def volume(a,deg):
    c=math.cos(math.radians(deg))
    return a**3*math.sqrt(1-3*c*c+2*c**3)

def neighbours(a,deg):
    c=math.cos(math.radians(deg))
    ds=[a*math.sqrt(i*i+j*j+k*k+2*c*(i*j+i*k+j*k))
        for i,j,k in itertools.product(range(-2,3),repeat=3) if (i,j,k)!=(0,0,0)]
    first=min(ds)
    return first,sum(math.isclose(d,first) for d in ds),min(d for d in ds if d>first+1e-7)

# Allow three printed length uncertainties in the unfavourable direction;
# bound the angle separately since its experimental uncertainty is unreported.
lo,hi=90,angle
for _ in range(60):
    g=(lo+hi)/2
    if volume(beta+3*ua,g)>volume(alpha-3*ua,90): lo=g
    else: hi=g
rows=[]
for phase,a,deg,observed_density in [('alpha',alpha,90,9.142),('beta',beta,angle,9.392)]:
    d,n,d2=neighbours(a,deg)
    assert n==6 and math.isclose(d,a)
    rows.append(dict(phase=phase,a_A=a,ua_A=ua,alpha_deg=deg,V_A3=volume(a,deg),
                     d1_A=d,n1=n,d2_A=d2,reported_Xray_density_g_cm3=observed_density))
assert rows[1]['V_A3']<rows[0]['V_A3'] and beta-3*ua>alpha+3*ua
with Path(__file__).with_name('polonium_cells.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n')
    w.writeheader();w.writerows(rows)
print('Length change %, volume change %, 3u worst length equal-volume angle (degrees):',
      100*(beta/alpha-1),100*(volume(beta,angle)/volume(alpha,90)-1),hi)

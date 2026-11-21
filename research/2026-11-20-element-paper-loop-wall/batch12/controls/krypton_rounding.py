"""Bound the screened-optics ratio on the whole fitted band under last-place perturbations."""
import csv
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path

from scipy.constants import epsilon_0,hbar,m_e

DIRECTORY=Path(__file__).resolve().parent


def box(printed):
    mid=F(printed)
    half=F(10)**Decimal(printed).as_tuple().exponent/2
    return (mid-half,mid+half)


def times(a,b):
    products=[x*y for x in a for y in b]
    return min(products),max(products)


def divide(a,b):
    if b[0]<=0:
        raise ValueError("denominator")
    return times(a,(1/b[1],1/b[0]))


def square(a):
    return (0 if a[0]<=0<=a[1] else min(a[0]**2,a[1]**2),max(a[0]**2,a[1]**2))


def add(a,b):
    return a[0]+b[0],a[1]+b[1]


def neg(a):
    return -a[1],-a[0]


def check(rows):
    density=box(rows[0]['number_density_1e21_cm3'])
    central=F(str(1e27*hbar*hbar/(epsilon_0*m_e)))
    factor=(central*(1-F(1,10**7)),central*(1+F(1,10**7)))
    gain=times(density,factor)
    bg=box(rows[0]['eps_background'])
    osc=[(square(box(r['E_eV'])),box(r['gamma_eV']),times(gain,box(r['f']))) for r in rows]
    cutoff=F(172,1000)  # > 3-2 sqrt(2), since W(cutoff)<0.
    assert cutoff**2-6*cutoff+1<0
    def lower(interval):
        e2=square(interval)
        re=bg
        im=(0,0)
        for resonance,width,strength in osc:
            delta=add(resonance,neg(e2))
            imag=times(width,interval)
            denom=add(square(delta),square(imag))
            re=add(re,divide(times(strength,delta),denom))
            im=add(im,divide(times(strength,imag),denom))
        return square(re)[0]+square(im)[0]
    intervals=[(F(9),F(11))]
    accepted=[]
    unresolved=[]
    while intervals:
        a,b=intervals.pop()
        bound=lower((a,b))
        if bound>cutoff:
            accepted.append((bound,a,b))
        elif b-a < F(1,16384):
            unresolved.append((bound,a,b))
        else:
            mid=(a+b)/2
            intervals.extend([(a,mid),(mid,b)])
    if sum((b-a for _,a,b in accepted+unresolved),F(0)) != 2:
        raise AssertionError("energy coverage")
    return min(bound for bound,_,_ in accepted+unresolved),len(accepted),len(unresolved)


def main():
    with (DIRECTORY/'krypton_fit_inputs.csv').open() as f:
        data=list(csv.DictReader(f))
    with (DIRECTORY/'krypton_rounding.csv').open('w',newline='') as stream:
        writer=csv.writer(stream,lineterminator="\n")
        writer.writerow(("phase","T_K","test_lower_z","intervals_accepted","intervals_unresolved","certified_global_lower_z_floor_1e_9"))
        for phase in ("solid","fluid"):
            rows=[row for row in data if row["phase"]==phase]
            bound,num,unresolved=check(rows)
            # Round down for a conservative printed decimal.
            scaled=int(bound*10**9)
            writer.writerow((phase,rows[0]["T_K"],"0.172",num,unresolved,f"{scaled//10**9}.{scaled%10**9:09d}"))


if __name__=="__main__":
    main()

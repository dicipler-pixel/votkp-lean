"""Ideal independent Poisson counting for three balanced Stokes bases."""
from fractions import Fraction as F
from math import sqrt, ceil
from stokes_test import calc

def estimate(a,b, description):
    m0,q,u,v,L=calc(a,b)
    # For basis i, count both output analyzer signs for each of the two input signs.
    # N_i/2 incident on each input. α_i=1/3 averages the three I estimates.
    alpha=F(1,3)
    costs=[(alpha**2+beta**2)*m0+2*alpha*beta*mi
           for beta,mi in zip((1,1,-3),(q,u,v))]
    assert all(x>=0 for x in costs)
    scales=[sqrt(float(c)) for c in costs]
    tot=sum(scales)
    print(description, "L",float(L),"flux fractions Q/U/V",*(round(s/tot,5) for s in scales))
    if L:
        for snr in (3,5):
            photon_count=ceil((snr*tot/float(L))**2)
            print("  nominal SNR",snr,"incident",photon_count,"detected expectation",round(float(m0)*photon_count))
    return costs
if __name__=="__main__":
    estimate(F(35,6),F(35,6),"35/6")
    estimate(F('153.896205')/F('18.21115'),F('18305.886')/F('4356.865'),"Be/Rb")
    estimate(F(9),F(4),"null 9/4")
    estimate(F(4),F(4),"inside 4/4")

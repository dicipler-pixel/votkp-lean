# SCRIPT: JOIN-K-01
# Claim: on T(2,q) one odd integer k labels three things read in three papers:
#  (Two Trees Thm 8.7)  tr(ab) = 2cos(k*pi/q), roots of the Riley relation written in t = tr(ab)
#  (vacuum disk v5)      direction Re V0/pi^2 = -k^2/(2q) mod 1
#  (Dirac Time 13.1)     arc-end step k, alpha_end = k/(2pq)
# Why this would prove it: the t-polynomials and the direction lists are taken from the papers as printed;
# the script only asks whether ONE set of k reproduces both lists. Kill: any printed root or direction not hit,
# or a k that gives a root but a direction not in the printed list.
from fractions import Fraction as F
import sympy as sp
t=sp.symbols('t')
polys={3:t-1,5:t**2-t-1,7:t**3-t**2-2*t+1}                 # Two Trees Thm 8.7
dirs={3:[F(5,6)],5:[F(1,10),F(9,10)],7:[F(3,14),F(5,14),F(13,14)]}  # path notes / vacuum disk v5
ok=True
for q in (3,5,7):
    ks=[k for k in range(1,q,2)]
    roots=sorted(float(r) for r in sp.Poly(polys[q],t).nroots())
    mine=sorted(float(2*sp.cos(k*sp.pi/q)) for k in ks)
    d=sorted((-F(k*k,2*q))%1 for k in ks)
    r_ok=all(abs(a-b)<1e-12 for a,b in zip(roots,mine)) and len(roots)==len(mine)
    d_ok=d==sorted(dirs[q]); ok&=r_ok and d_ok
    print(q,'k =',ks,'| tr(ab) match',r_ok,'| directions',[str(x) for x in d],'match',d_ok)
    for k in ks:
        a=F(k,4*q)  # alpha_end = k/(2pq), p=2
        print('   k',k,' rotation half-angle of ab = %d*pi/%d'%(k,q),' alpha_end',a,' -4pq*alpha^2 mod 1 =',(-4*2*q*a*a)%1)
print('ALL MATCH' if ok else 'KILLED')

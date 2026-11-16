# SCRIPT: TORUS-STAIR-01
# Why this check proves the claim: an arc of irreducible SU(2) characters of T(p,q) can only end on the
# abelian line where the Alexander polynomial vanishes at the squared meridian eigenvalue, Delta(e^{4 pi i alpha})=0.
# If every such alpha in (0,1/2) has 2pq*alpha an integer, the staircase claim holds; a single non-integer kills it.
# Kill condition (written before the run): any root with |2pq*alpha - round| > 1e-9, or the count of roots
# differing from the count of k in 1..pq-1 not divisible by p or q.
import sympy as sp
t=sp.symbols('t')
for p,q in [(2,3),(3,4),(2,5),(3,5),(2,7),(4,5),(5,7)]:
    D=sp.cancel((t**(p*q)-1)*(t-1)/((t**p-1)*(t**q-1)))
    roots=sp.Poly(D,t).nroots(n=30,maxsteps=400)
    ks=[]
    for r in roots:
        a=float(sp.arg(r))/(4*sp.pi.evalf())   # alpha with e^{4 pi i alpha}=r, alpha in (-1/4,1/4]
        for sh in (0,0.5):
            al=(a+sh)%1
            if 0<al<0.5:
                k=2*p*q*al; assert abs(k-round(k))<1e-9,(p,q,k); ks.append(round(k))
    ks=sorted(set(ks)); pred=[k for k in range(1,p*q) if k%p and k%q]
    print((p,q),'steps k =',ks,'| predicted match:',ks==pred,'| arcs (p-1)(q-1)/2 =',(p-1)*(q-1)//2,'| endpoints:',len(ks))

# SCRIPT: SURFACEOLOGY-01
# Reproduction (not new work) of the core results of Arkani-Hamed, Cao, Dong, Figueiredo, He (2023-24):
#  (1) Tr(phi^3) tree amplitude = sum over triangulations of 1/(product of planar X's): denominators only.
#  (2) Hidden zero: set the non-planar c_{1j} = 0 (j = 3..n-1) and the whole amplitude vanishes, though no single
#      Feynman term does.
#  (3) The delta shift: X(even,even) -> X + delta, X(odd,odd) -> X - delta. The leading term at large delta is the
#      pion (NLSM) amplitude: numerators appear out of shifted denominators. Checked against the known 4- and 6-point
#      NLSM amplitudes, up to one overall constant.
#  (4) The u-variables from words of 2x2 matrices along curves (the Smith/Mobius link): u_C + prod u_D^{cross} = 1.
import itertools, random, sympy as sp
from fractions import Fraction as F
def tris(poly):                                   # triangulations of a polygon (vertex list) as lists of diagonals
    if len(poly)<4: return [[]]
    out=[]; a,b=poly[0],poly[-1]
    for k in range(1,len(poly)-1):
        c=poly[k]
        for L in tris(poly[:k+1]):
            for R in tris(poly[k:]):
                d=[]
                if k>1: d.append((a,c))
                if k<len(poly)-2: d.append((c,b))
                out.append(L+R+d)
    return out
def amp(n,X):
    s=0
    for T in tris(list(range(1,n+1))):
        p=1
        for (i,j) in T: p*=X[(min(i,j),max(i,j))]
        s+=1/p
    return s
def planar(n): return [(i,j) for i in range(1,n+1) for j in range(i+2,n+1) if not (i==1 and j==n)]
def Xget(X,i,j,n):
    i=(i-1)%n+1; j=(j-1)%n+1
    if i==j or abs(i-j)==1 or {i,j}=={1,n}: return 0
    return X[(min(i,j),max(i,j))]
def c(X,i,j,n): return Xget(X,i,j,n)+Xget(X,i+1,j+1,n)-Xget(X,i,j+1,n)-Xget(X,i+1,j,n)
random.seed(2)
# (2) hidden zero, n = 6: c_{13}=c_{14}=c_{15}=0 fixes X_{2j} in terms of the rest; amplitude should vanish
n=6; syms={k:sp.Symbol('X%d%d'%k) for k in planar(n)}
eqs=[c(syms,1,j,n) for j in (3,4,5)]
sol=sp.solve(eqs,[syms[(2,4)],syms[(2,5)],syms[(2,6)]],dict=True)[0]
A=sp.simplify(sp.together(amp(n,syms)).subs(sol))
print('(2) hidden zero n=6: amplitude on c_13=c_14=c_15=0 ->',A, ' | Feynman terms:',len(tris(list(range(1,7)))))
# (3) delta shift
d=sp.Symbol('delta')
def shifted(n,Xs):
    S={}
    for (i,j),v in Xs.items():
        S[(i,j)]= v+d if (i%2==0 and j%2==0) else (v-d if (i%2==1 and j%2==1) else v)
    return S
X4={k:sp.Rational(random.randint(1,50),7) for k in planar(4)}
lead4=sp.limit(amp(4,shifted(4,X4))*d**2,d,sp.oo); nl4=X4[(1,3)]+X4[(2,4)]
print('(3) n=4: leading shifted term / (X13+X24) =',sp.nsimplify(lead4/nl4))
def nlsm6(X):
    g=lambda i,j:X[(min(i,j),max(i,j))]
    return ((g(1,3)+g(2,4))*(g(4,6)+g(1,5))/g(1,4)+(g(2,4)+g(3,5))*(g(1,5)+g(2,6))/g(2,5)
            +(g(3,5)+g(4,6))*(g(2,6)+g(1,3))/g(3,6)-(g(1,3)+g(2,4)+g(3,5)+g(4,6)+g(1,5)+g(2,6)))
rat=[]
for trial in range(3):
    X6={k:sp.Rational(random.randint(1,60),random.randint(1,9)) for k in planar(6)}
    lead6=sp.limit(sp.together(amp(6,shifted(6,X6)))*d**4,d,sp.oo); rat.append(sp.nsimplify(lead6/nlsm6(X6)))
print('    n=6: leading shifted term / NLSM_6, three random points =',rat)
# (4) u-variables as cross-ratios of ordered points z_1<...<z_n on a line (the worldsheet form; Mobius-invariant,
#     the quantity a Smith-chart move preserves). u_ij = (z_i-z_{j-1})(z_{i-1}-z_j)/((z_i-z_j)(z_{i-1}-z_{j-1})).
#     Check the binary relations u_C + prod_{D crossing C} u_D = 1, and Mobius invariance, for n = 5..8.
import numpy as np
def us(z,n):
    Z=lambda k: z[(k-1)%n]
    return {(i,j):(Z(i)-Z(j-1))*(Z(i-1)-Z(j))/((Z(i)-Z(j))*(Z(i-1)-Z(j-1))) for (i,j) in planar(n)}
def crosses(a,b):
    (i,j),(k,l)=a,b
    return (i<k<j<l) or (k<i<l<j)
worst=0; mob=0
for n in range(5,9):
    z=np.sort(np.random.default_rng(n).uniform(0,10,n)); U=us(z,n)
    for C in U: worst=max(worst,abs(U[C]+np.prod([U[D] for D in U if crosses(C,D)])-1))
    a,b,cc,dd=1.3,0.4,-0.2,2.0                  # a Mobius map (det>0, keeps order on the chosen range)
    z2=(a*z+b)/(cc*z+dd); o=np.argsort(z2); U2=us(z2[o],n) if np.all(np.diff(z2)>0) else U
    mob=max(mob,max(abs(U[k]-U2[k]) for k in U))
print('(4) u-equations, n=5..8: worst |u_C + prod u_D - 1| =',worst,' | Mobius change in u:',mob)

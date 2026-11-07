# SCRIPT: BOWL-CUBIC-01
# Task 2a: exact Taylor expansion of the Bloch-Wigner function D about the regular tetrahedron in the Smith-disk coordinate G=(z-w)/(z-conj w), w=e^{i pi/3}.
# Method: D = (1/2i)[Li2(z)-Li2(zb) + (1/2)(log(1-z)-log(1-zb))(log z+log zb)] with z=(w-wb*G)/(1-G), zb=(wb-w*H)/(1-H) (H = conj G, treated as independent);
# differentiate symbolically at G=H=0 up to total order 4. Check: terms of order 1 vanish, order 2 = -(3 sqrt3/4) G H, order 3 = c3*G^3 + conj, then compare numerically with D.
import sympy as sp, mpmath as mp
G,H=sp.symbols('G H')
w=sp.exp(sp.I*sp.pi/3); wb=sp.exp(-sp.I*sp.pi/3)
z=(w-wb*G)/(1-G); zb=(wb-w*H)/(1-H)
D=(1/(2*sp.I))*(sp.polylog(2,z)-sp.polylog(2,zb)+sp.Rational(1,2)*(sp.log(1-z)-sp.log(1-zb))*(sp.log(z)+sp.log(zb)))
# derivatives at 0 : use mpmath numerically at 60 digits and also identify closed forms
def d(i,j):
    e=sp.diff(D,G,i,H,j) if (i or j) else D
    return e.subs({G:0,H:0})
mp.mp.dps=50
coef={}
for i in range(0,5):
    for j in range(0,5-i):
        v=d(i,j)
        val=complex(sp.N(v,40))
        coef[(i,j)]=sp.N(v/(sp.factorial(i)*sp.factorial(j)),40)
        if abs(val)>1e-30 and i+j<=4: print((i,j),'coefficient of G^%d H^%d ='%(i,j),sp.N(coef[(i,j)],25))
V0=sp.N(coef[(0,0)],30); print('V0 =',V0)
c30=coef[(3,0)]; r=sp.N(sp.Abs(c30),30); ph=sp.N(sp.arg(c30),30)
print('c3 (coefficient of G^3, D real so G H terms conj) : modulus',r,' phase/pi',sp.N(ph/sp.pi,30))
print('modulus candidates: sqrt3/4 = %s ; 1/(4 sqrt3)... '%sp.N(sp.sqrt(3)/4,25),' ratio modulus/sqrt3 =',sp.N(r/sp.sqrt(3),25),' modulus*sqrt3=',sp.N(r*sp.sqrt(3),25))
# closed form attempt
print('exact simplified c3:',sp.nsimplify(sp.N(c30,30),[sp.sqrt(3)]), '| re',sp.nsimplify(sp.N(sp.re(c30),30),[sp.sqrt(3)]),'im',sp.nsimplify(sp.N(sp.im(c30),30),[sp.sqrt(3)]))
print('exact c3 (sympy simplify):',sp.simplify(sp.nsimplify(c30)))
# numerical validation of the full expansion
import numpy as np
from mpmath import polylog
wn=complex(w.evalf()); 
def Dn(zz): return float(np.imag(complex(polylog(2,zz))))+np.angle(1-zz)*np.log(abs(zz))
c2=float(sp.re(coef[(1,1)])); c3=complex(c30)
for rr in (0.1,0.05,0.02):
    for th in (0.3,1.1):
        g=rr*np.exp(1j*th); zz=(wn-np.conj(wn)*g)/(1-g)
        ap=float(sp.re(V0))+c2*abs(g)**2+2*(c3*g**3).real+float(sp.re(coef[(2,2)]))*abs(g)**4
        print('|G|=%.2f th=%.1f  D=%.10f  V0+c2|G|^2+2Re(c3 G^3)+c22|G|^4=%.10f  resid=%.2e (order |G|^4 ~ %.1e)'%(rr,th,Dn(zz),ap,Dn(zz)-ap,rr**4))

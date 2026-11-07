# SCRIPT: WINDING-CS-01
# Does the turn book (Chern-Simons) live in winding integers? Neumann's flattening formula (Geom. Topol. 2004):
# give each tetrahedron log-parameters w0 = log z + p*pi*i, w1 = log z' + q*pi*i, w2 = -w0-w1 (z' = 1/(1-z)),
# with integers p, q chosen so every edge's and both cusp curves' log-parameters sum to 0. Then
#   i(Vol + i CS) = sum_j R(z_j; p_j, q_j)  mod pi^2,  R = Li2(z) + 1/2 log z log(1-z) + (pi i/2)(q log z + p log(1-z)) - pi^2/6.
# Why this tests it: Vol needs no integers (the continuous part gives it, as SHAPE-DISK found); if CS truly sits in the
# windings, the formula with the solved integers must reproduce snappy's CS, and dropping the integer term must lose it.
import numpy as np, snappy, warnings, re, database_knotinfo as d
from cypari import pari
from mpmath import polylog, mpc
warnings.filterwarnings('ignore')
def solve_int(A,b):
    M=pari('['+';'.join(','.join(str(int(x)) for x in r) for r in A)+']'); B=pari('['+','.join(str(int(x)) for x in b)+']~')
    s=pari.matsolvemod(M,0,B)
    return None if s==0 else [int(s[i]) for i in range(len(A[0]))]
def R(z,p,q):
    lz=np.log(z); l1=np.log(1-z)
    return complex(polylog(2,mpc(z)))+0.5*lz*l1+0.5j*np.pi*(q*lz+p*l1)-np.pi**2/6
out=[]
names=[r['name'] for r in d.link_list() if re.match(r'^\d+_\d+$',r['name'] or '') and 4<=int(r['name'].split('_')[0])<=9]
for nm in names:
    M=snappy.Manifold(nm)
    if M.solution_type()!='all tetrahedra positively oriented': continue
    z=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); n=len(z); zp=1/(1-z)
    G=M.gluing_equations(); E=np.array(G.list(),dtype=int).reshape(-1,3*n)   # rows: edges..., meridian, longitude
    a,b,c=E[:,0::3],E[:,1::3],E[:,2::3]                     # interleaved (a,b,c) per tetrahedron; checked below
    zpp=1-1/z; chk=np.exp(a@np.log(z)+b@np.log(zp)+c@np.log(zpp))
    if np.max(abs(chk[:-2]-1))>1e-6: a,b,c=E[:,:n],E[:,n:2*n],E[:,2*n:]
    L=(a-c)@np.log(z)+(b-c)@np.log(zp)
    tgt=np.zeros(len(E),dtype=complex)                    # flattening: every edge and cusp curve sums to 0 (Zickert Def 6.1)
    rhs=(tgt-L)/(1j*np.pi)
    if np.max(abs(rhs-np.round(rhs.real)))>1e-6: out.append((nm,'nonint')); continue
    A=np.hstack([a-c,b-c]); sol=solve_int(A.tolist(),np.round(rhs.real).astype(int).tolist())
    if sol is None: out.append((nm,'nosol')); continue
    p,q=np.array(sol[:n]),np.array(sol[n:])
    tot=sum(R(z[j],p[j],q[j]) for j in range(n)); vol=tot.imag; cs=-tot.real
    cont=-sum((complex(polylog(2,mpc(zj)))+0.5*np.log(zj)*np.log(1-zj)-np.pi**2/6).real for zj in z)
    cv=complex(M.complex_volume())
    def m(x,per): return (x+per/2)%per-per/2
    per=np.pi**2/2                                           # compare modulo pi^2/2 (convention-safe)
    out.append((nm,vol,cv.real,m(cs-cv.imag,per),m(cont-cv.imag,per),int(np.sum(abs(p))+np.sum(abs(q)))))
ok=[o for o in out if len(o)==6]; bad=[o for o in out if len(o)==2]
print('knots solved: %d ; no integer flattening found: %d %s'%(len(ok),len(bad),bad[:5]))
V=np.array([o[1]-o[2] for o in ok]); E1=np.array([o[3] for o in ok]); E0=np.array([o[4] for o in ok])
print('volume from formula vs snappy: max |diff| = %.2e'%np.max(abs(V)))
print('CS WITH winding integers, mismatch mod pi^2/2: max %.2e, median %.2e'%(np.max(abs(E1)),np.median(abs(E1))))
print('CS WITHOUT winding term (continuous part only): median |mismatch| %.3f, as share of the period: %.0f%%'%(np.median(abs(E0)),100*np.median(abs(E0))/(np.pi**2/4)))
print('examples (knot, total |p|+|q|):',[(o[0],o[5]) for o in ok[:8]])
off=np.pi**2/6
def allow(x):  # distance to the nearest of 0, +pi^2/6, -pi^2/6 modulo pi^2/2 (weak-flattening ambiguity, Neumann 2004)
    w=lambda y:abs((y+np.pi**2/4)%(np.pi**2/2)-np.pi**2/4)
    return np.minimum(np.minimum(w(x),w(x-off)),w(x+off))
b1=allow(E1); b0=allow(E0)
print('CS WITH windings (up to the pi^2/6 ambiguity): max mismatch %.2e over %d knots; exact without any allowance: %d'%(b1.max(),len(b1),int(np.sum(abs(E1)<1e-8))))
print('CS from the continuous part only, same allowance: median mismatch %.3f, max %.3f, matched to 1e-6: %d of %d'%(np.median(b0),b0.max(),int(np.sum(b0<1e-6)),len(b0)))

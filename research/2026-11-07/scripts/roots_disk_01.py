# SCRIPT: ROOTS-DISK-01
# All solutions of a knot's gluing equations (edges + meridian completeness) = every way to put a hyperbolic-type
# geometry on the knot: the true one, its mirror, flat (real) ones, and other Galois-conjugate ones. These are the roots
# of the knot's shape polynomial. On the Smith disk centred at the regular tetrahedron, G = (z - w)/(z - conj w):
# prediction (from the vacuum-well law): the true geometry is the solution whose pieces sit nearest the vacuum
# (smallest sum |G|^2); mirrors sit outside the disk; flat solutions on the rim. Compare: max volume picks the true one
# (Cho; Francaviglia). Each solution's 'decay' = its volume (sum D), and the test asks whether nearest-vacuum agrees.
import numpy as np, snappy, warnings, re, database_knotinfo as d
from mpmath import polylog
warnings.filterwarnings('ignore')
w=np.exp(1j*np.pi/3)
def D(z): return float(np.imag(complex(polylog(2,z))))+np.angle(1-z)*np.log(abs(z))
def solve_all(M,starts=400,seed=0):
    g=M.gluing_equations('rect'); A=np.array([r[0] for r in g],float); B=np.array([r[1] for r in g],float); c=np.array([r[2] for r in g],complex)
    n=A.shape[1]; rows=list(range(n-1))+[n]                  # n-1 edges + meridian
    A,B,c=A[rows],B[rows],c[rows]
    def F(z): return np.exp(A@np.log(z)+B@np.log(1-z))-c       # principal logs only enter through exp: branch-free
    def J(z):
        f=np.exp(A@np.log(z)+B@np.log(1-z))
        return f[:,None]*(A/z[None,:]-B/(1-z)[None,:])
    rng=np.random.default_rng(seed); sols=[]
    for _ in range(starts):
        z=rng.normal(0.5,1.2,n)+1j*rng.normal(0,1.2,n)
        for it in range(60):
            try: dz=np.linalg.solve(J(z),-F(z))
            except np.linalg.LinAlgError: break
            z=z+dz
            if np.max(abs(dz))<1e-13: break
        if np.all(np.isfinite(z)) and np.max(abs(F(z)))<1e-9 and np.min(abs(z))>1e-6 and np.min(abs(1-z))>1e-6:
            if not any(np.max(abs(z-s))<1e-7 for s in sols): sols.append(z)
    return sols
names=[r['name'] for r in d.link_list() if re.match(r'^\d+_\d+$',r['name'] or '') and 4<=int(r['name'].split('_')[0])<=8]
agree=tot=0; mirror_out=0; flat_rim=0; rows=[]
for nm in names:
    M=snappy.Manifold(nm)
    if M.solution_type()!='all tetrahedra positively oriented': continue
    zg=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); sols=solve_all(M)
    if not any(np.max(abs(s-zg))<1e-6 for s in sols): sols.append(zg)
    info=[]
    for s in sols:
        G=(s-w)/(s-np.conj(w)); info.append((np.sum(abs(G)**2),sum(D(x) for x in s),np.max(abs(s-zg))<1e-6,np.max(abs(s-np.conj(zg)))<1e-6,np.all(abs(s.imag)<1e-9),np.max(abs(G))))
    gi=[i for i,x in enumerate(info) if x[2]][0]; near=int(np.argmin([x[0] for x in info])); big=int(np.argmax([x[1] for x in info]))
    tot+=1; agree+=(near==gi)
    mi=[x for x in info if x[3]]; mirror_out+= bool(mi) and all(x[5]>1 for x in mi)
    rows.append((nm,len(sols),near==gi,big==gi,sorted([(round(x[0],3),round(x[1],3)) for x in info])[:4]))
print('knots: %d   true geometry = nearest the vacuum: %d   (= max volume: %d)'%(tot,agree,sum(r[3] for r in rows)))
print('mirror solutions found sitting outside the disk: %d knots'%mirror_out)
for r in rows[:8]: print('  %-5s solutions %2d  nearest=true %s  maxvol=true %s  (sum|G|^2, volume) smallest: %s'%r)

# SCRIPT: STRONG-FLAT-01
# Task 1: strong flattening. Neumann 2004 Def 4.3/4.4: a flattening needs (i) log-parameter zero around every edge,
# (ii) PARITY zero along every closed normal path of the triangulation; strong = also log-parameter zero on cusp curves.
# Parity parameter of an edge of a tetrahedron = s mod 2 where its log-parameter is log(shape)+s*pi*i (p, q, r=-1-p-q).
# Parity along a path = sum over the edges it passes. Model implemented (flat_lib_01.parity_system): a normal path crossing
# tetra t from face fin to face fout passes the edge fin∩fout (same parity as its opposite edge); closed paths = closed walks
# through glued faces. All such walks pay 0 iff a potential phi on half-faces exists: linear mod-2 system in (p,q,phi).
# Why this tests it: if the model of 'passes' is right, adding these mod-2 rows to the integer edge/cusp system must turn every
# weak flattening (CS exact only up to 0/+-pi^2/6) into one reproducing snappy's CS exactly (mod snappy's own period pi^2/2).
import sys; sys.path.insert(0,'/home/claude/votkp_research')
from flat_lib_01 import *
pari.allocatemem(2*10**9)
import re, database_knotinfo as d
def R(z,p,q):
    lz=np.log(z); l1=np.log(1-z)
    return complex(polylog(2,mpc(z)))+0.5*lz*l1+0.5j*np.pi*(q*lz+p*l1)-np.pi**2/6
per=np.pi**2/2
def m(x,per=per): return (x+per/2)%per-per/2
def mode_rows(M,mode):
    return parity_system(M)
names=[r['name'] for r in d.link_list() if re.match(r'^\d+_\d+$',r['name'] or '') and 4<=int(r['name'].split('_')[0])<=9]
res=[]
for nm in names:
    M=snappy.Manifold(nm)
    if M.solution_type()!='all tetrahedra positively oriented': continue
    z=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); n=len(z); zp=1/(1-z)
    E=np.array(M.gluing_equations().list(),dtype=int).reshape(-1,3*n); a,b,c=E[:,0::3],E[:,1::3],E[:,2::3]
    L=(a-c)@np.log(z)+(b-c)@np.log(zp); rhs=np.round((-L/(1j*np.pi)).real).astype(int)
    A0=np.hstack([a-c,b-c]); cv=complex(M.complex_volume())
    def cs_of(sol):
        p,q=np.array(sol[:n]),np.array(sol[n:2*n]); tot=sum(R(z[j],p[j],q[j]) for j in range(n)); return m(-tot.real-cv.imag),tot.imag-cv.real
    s0=solve_int=solve_mod(A0.tolist(),[0]*len(A0),rhs.tolist())
    e0=cs_of(s0)[0] if s0 else None
    pc=parity_constraints(M)
    if pc is None: res.append((nm,n,e0,None,None,'mod2-inconsistent')); continue
    cons=pc[0]; P=np.array([[ (x>>v)&1 for v in range(2*n)] for x,r in cons],int).reshape(len(cons),2*n); pb=[r for x,r in cons]
    Aug=np.vstack([A0,P]); mods=[0]*len(A0)+[2]*len(cons); bb=list(rhs)+pb
    s1=solve_mod(Aug.tolist(),mods,bb)
    if s1 is None: res.append((nm,n,e0,None,None,'no integer solution')); continue
    e1,v1=cs_of(s1); res.append((nm,n,e0,e1,v1,len(cons)))
ok=[r for r in res if r[3] is not None]; none=[r for r in res if r[3] is None]
print('hyperbolic knots 4-9 crossings:',len(res),'; parity+log system solvable:',len(ok),'; unsolvable:',[(r[0],r[5]) for r in none])
E0=np.array([r[2] for r in res if r[2] is not None]); E1=np.array([r[3] for r in ok])
print('weak (log only):   exact (<1e-8) on %d of %d ; max |mismatch| %.3e'%(np.sum(abs(E0)<1e-8),len(E0),abs(E0).max()))
print('with parity rows:  exact (<1e-8) on %d of %d ; max |mismatch| %.3e'%(np.sum(abs(E1)<1e-8),len(E1),abs(E1).max()))
print('volume check max diff %.2e'%max(abs(r[4]) for r in ok))
print('mismatch values (in units of pi^2/6) among non-exact:',sorted(set(np.round(E1[abs(E1)>1e-8]/(np.pi**2/6),4)))[:10])
print('first failures:',[(r[0],round(r[3]/(np.pi**2/6),3)) for r in ok if abs(r[3])>1e-8][:15])

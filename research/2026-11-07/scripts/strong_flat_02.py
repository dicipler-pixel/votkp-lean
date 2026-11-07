# SCRIPT: STRONG-FLAT-02
# Task 1, second pass. STRONG-FLAT-01 showed the pi^2/6 offsets are NOT cured by extra mod-2 rows alone: the mismatch is constant over the
# whole coset of log-solutions. Cause found by test: Neumann's R(z;p,q) is not invariant under relabelling the three edge pairs of one
# tetrahedron (R(z';q,r)-R(z;p,q) = (1+3q) pi^2/6 for every z), and his formula needs an ORDERED triangulation (vertex orders agreeing on
# faces, sign eps_i = +-1). SnapPy's triangulations are unordered, so here we (1) find a branching (an ordering of each tetra's vertices
# with every face gluing order-preserving) by brute force over edge-class directions, (2) re-read each tetra in that order:
# x_k = cross ratio of the permuted ideal vertices, eps = sign of the permutation, new integers s'_k = eps * s_j (log-parameters w' = eps w),
# (3) sum eps*R(x; s'_0, s'_1). Edge/cusp log-parameter equations are unchanged (sum of eps*w' = sum of w). Parity rows from
# flat_lib_01.parity_constraints (model of 'passes'): validated against Neumann Prop 5.3 (l(x;0,0) in the ordered labelling has zero parity).
# Kill conditions written before the run: (a) Prop 5.3 check must hold for every knot/branching; (b) CS must equal snappy's to 1e-8 mod pi^2/2
# on all hyperbolic knots 4-9 crossings, with no pi^2/6 allowance; any failure is reported.
import sys; sys.path.insert(0,'/home/claude/votkp_research')
from flat_lib_01 import *
import re, database_knotinfo as d
pari.allocatemem(2*10**9)
per=np.pi**2/2
def m(x,per=per): return (x+per/2)%per-per/2
def hom(x): return (x,1.0) if x!='inf' else (1.0,0.0)
def sub(a,b): return a[0]*b[1]-a[1]*b[0]
def cr(a,b,c,d_): return (sub(c,b)*sub(d_,a))/(sub(c,a)*sub(d_,b))
def R(z,p,q):
    lz=np.log(z); l1=np.log(1-z)
    return complex(polylog(2,mpc(z)))+0.5*lz*l1+0.5j*np.pi*(q*lz+p*l1)-np.pi**2/6
def reorder(z,order):
    """x_0,x_1,x_2 of the tetra read in vertex order `order` (old labels low->high), and eps=sign of the permutation.
    even: x_k = old param of the pair carrying new slot k ; odd (orientation reversed): inverse of it."""
    eps=perm_sign(order); zo=(z,1/(1-z),1-1/z)
    jk=[pair_of(order[0],order[1]),pair_of(order[0],order[2]),pair_of(order[0],order[3])]
    xs=[zo[j] if eps==1 else 1/zo[j] for j in jk]
    assert abs(xs[1]-1/(1-xs[0]))<1e-9 and abs(xs[2]-(1-1/xs[0]))<1e-9
    return xs[0],xs[1],xs[2],eps
names=[r['name'] for r in d.link_list() if re.match(r'^\d+_\d+$',r['name'] or '') and 4<=int(r['name'].split('_')[0])<=9]
rows=[]; prop53_fail=[]; multi=[]
for nm in names:
    M=snappy.Manifold(nm)
    if M.solution_type()!='all tetrahedra positively oriented': continue
    z=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); n=len(z); zp=1/(1-z)
    E=np.array(M.gluing_equations().list(),dtype=int).reshape(-1,3*n); a,b,c=E[:,0::3],E[:,1::3],E[:,2::3]
    L=(a-c)@np.log(z)+(b-c)@np.log(zp); rhs=np.round((-L/(1j*np.pi)).real).astype(int); A0=np.hstack([a-c,b-c])
    cv=complex(M.complex_volume())
    br=find_branching(M,maxsol=6)
    zold=[(z[j],zp[j],1-1/z[j]) for j in range(n)]
    # parity constraints (intrinsic, old slots)
    pc=parity_constraints(M)[0]
    Pm=np.array([[(x>>v)&1 for v in range(2*n)] for x,r in pc],int).reshape(len(pc),2*n); pb=[r for x,r in pc]
    def total(orders,sol):
        p,q=np.array(sol[:n]),np.array(sol[n:2*n]); s_old=[(p[j],q[j],-1-p[j]-q[j]) for j in range(n)]
        tot=0
        for t in range(n):
            x0,x1,x2,eps=reorder(z[t],orders[t])
            # which old pair does new slot k carry:
            o=orders[t]; jk=[pair_of(o[0],o[1]),pair_of(o[0],o[2]),pair_of(o[0],o[3])]
            xs=[x0,x1,x2]
            for k in range(3):
                ref=zold[t][jk[k]] if eps==1 else 1/zold[t][jk[k]]
                assert abs(xs[k]-ref)<1e-9,(nm,t,k,xs[k],ref,eps)
            s_new=[eps*s_old[t][jk[k]] for k in range(3)]
            tot+=eps*R(x0,s_new[0],s_new[1])
        return tot
    res_here=[]
    for orders in br:
        # (a) Prop 5.3: new-slot parity (0,0,1) must satisfy the mod-2 system
        delta_old=np.zeros(2*n,int)
        for t in range(n):
            o=orders[t]; jk=[pair_of(o[0],o[1]),pair_of(o[0],o[2]),pair_of(o[0],o[3])]
            par_old=[0,0,0]
            for k in range(3): par_old[jk[k]]=(0,0,1)[k]
            delta_old[t]=par_old[0]; delta_old[n+t]=par_old[1]
        p53=all(((Pm@delta_old)%2)==np.array(pb)) if len(pc) else True
        # weak (log only, ordered) and strong (log + parity)
        sw=solve_mod(A0.tolist(),[0]*len(A0),rhs.tolist())
        Aug=np.vstack([A0,Pm]); ss=solve_mod(Aug.tolist(),[0]*len(A0)+[2]*len(pc),list(rhs)+pb)
        ew=m(-total(orders,sw).real-cv.imag) if sw else None
        tt=total(orders,ss) if ss else None
        es=m(-tt.real-cv.imag) if ss else None
        vs=(tt.imag-cv.real) if ss else None
        res_here.append((p53,ew,es,vs))
    rows.append((nm,n,res_here))
    if not all(r[0] for r in res_here): prop53_fail.append(nm)
print('hyperbolic knots 4-9 crossings:',len(rows))
print('(a) Prop 5.3 check (0,0,1 in ordered slots satisfies the mod-2 path system): failed on',len(prop53_fail),prop53_fail[:10])
allr=[r for _,_,rs in rows for r in rs]
ew=np.array([r[1] for r in allr]); es=np.array([r[2] for r in allr]); vs=np.array([r[3] for r in allr])
print('branchings tested per knot: up to 6 ; total (knot,branching) runs:',len(allr))
print('(b) ordered, log-equations only (no parity):  exact (<1e-8): %d of %d, max |mismatch| %.2e (units pi^2/6 of non-exact: %s)'%(np.sum(abs(ew)<1e-8),len(ew),abs(ew).max(),sorted(set(np.round(ew[abs(ew)>1e-8]/(np.pi**2/6),3)))[:6]))
print('(b) ordered, log + parity (strong):            exact (<1e-8): %d of %d, max |mismatch| %.2e (units pi^2/6 of non-exact: %s)'%(np.sum(abs(es)<1e-8),len(es),abs(es).max(),sorted(set(np.round(es[abs(es)>1e-8]/(np.pi**2/6),3)))[:6]))
print('volume check max diff %.2e'%abs(vs).max())
bad=[(nm,[round(r[2]/(np.pi**2/6),3) for r in rs]) for nm,_,rs in rows if any(abs(r[2])>1e-8 for r in rs)]
print('knots with any strong mismatch:',len(bad),bad[:12])
badw=[nm for nm,_,rs in rows if any(abs(r[1])>1e-8 for r in rs)]
print('knots with any weak(ordered) mismatch:',len(badw),badw[:12])

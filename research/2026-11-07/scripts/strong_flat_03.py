# SCRIPT: STRONG-FLAT-03
# Does parity matter beyond snappy's period pi^2/2? For each hyperbolic knot 4-9 crossings (ordered reading, first branching):
# compare the weak integer solution (log rows only) and the strong one (log + mod-2 normal-path parity), as sums of eps*R mod pi^2 (Neumann's period).
# Why: snappy only records CS mod pi^2/2, so exactness against snappy cannot see a pi^2/2 shift; but the two flattenings' own sums can be compared.
# Also scans 40 further integer solutions of the log system (kernel combos) and reports which obey parity and what their sums do mod pi^2.
import sys; sys.path.insert(0,'/home/claude/votkp_research')
exec(open('/home/claude/votkp_research/strong_flat_02.py').read().split("names=[r['name']")[0])
import itertools
names=[r['name'] for r in d.link_list() if re.match(r'^\d+_\d+$',r['name'] or '') and 4<=int(r['name'].split('_')[0])<=9]
def Rtot(z,orders,sol,n):
    p,q=np.array(sol[:n]),np.array(sol[n:2*n]); s_old=[(p[j],q[j],-1-p[j]-q[j]) for j in range(n)]; tot=0
    for t in range(n):
        x0,x1,x2,eps=reorder(z[t],orders[t]); o=orders[t]; jk=[pair_of(o[0],o[1]),pair_of(o[0],o[2]),pair_of(o[0],o[3])]
        sn=[eps*s_old[t][jk[k]] for k in range(3)]; tot+=eps*R(x0,sn[0],sn[1])
    return tot
def mp(x): return (x+np.pi**2/2)%(np.pi**2)-np.pi**2/2
rng=np.random.default_rng(0)
cnt_wdiff=0; tot=0; rows=[]; viol_w=0; allpar_ok=0; allpar_n=0; par_split=[]
for nm in names:
    M=snappy.Manifold(nm)
    if M.solution_type()!='all tetrahedra positively oriented': continue
    z=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); n=len(z); zp=1/(1-z)
    E=np.array(M.gluing_equations().list(),dtype=int).reshape(-1,3*n); a,b,c=E[:,0::3],E[:,1::3],E[:,2::3]
    L=(a-c)@np.log(z)+(b-c)@np.log(zp); rhs=np.round((-L/(1j*np.pi)).real).astype(int); A0=np.hstack([a-c,b-c])
    orders=find_branching(M,maxsol=1)[0]
    pc=parity_constraints(M)[0]; Pm=np.array([[(x>>v)&1 for v in range(2*n)] for x,r in pc],int).reshape(len(pc),2*n); pb=np.array([r for x,r in pc])
    sw=solve_mod(A0.tolist(),[0]*len(A0),rhs.tolist()); ss=solve_mod(np.vstack([A0,Pm]).tolist(),[0]*len(A0)+[2]*len(pc),list(rhs)+list(pb))
    wpar=np.all(((Pm@(np.array(sw[:2*n])%2))%2)==pb)
    tw=Rtot(z,orders,sw,n); ts=Rtot(z,orders,ss,n)
    diff=mp((tw-ts).real)
    # kernel combos: find integer kernel of A0 via pari
    ker=pari.matkerint(pari('['+';'.join(','.join(str(int(x)) for x in r) for r in A0)+']'))
    K=np.array([[int(ker[i,j]) for j in range(ker.ncols())] for i in range(2*n)]) if ker.ncols()>0 else np.zeros((2*n,0),int)
    base=np.array(ss[:2*n]); res=[]
    for _ in range(40):
        v=base+(K@rng.integers(-2,3,K.shape[1]) if K.shape[1] else 0)
        par_ok=np.all(((Pm@(v%2))%2)==pb); tv=Rtot(z,orders,list(v),n); res.append((par_ok,mp((tv-ts).real)))
    rows.append((nm,wpar,diff,res))
print('knots:',len(rows))
print('weak solution (log rows only) already obeys parity on %d of %d'%(sum(r[1] for r in rows),len(rows)))
print('weak minus strong, mod pi^2: |diff| values (units pi^2/2):',sorted(set(np.round(np.array([abs(r[2]) for r in rows])/(np.pi**2/2),4))))
allres=[x for r in rows for x in r[3]]
okp=[x for x in allres if x[0]]; badp=[x for x in allres if not x[0]]
print('random kernel shifts of the strong solution: %d obey parity, %d violate'%(len(okp),len(badp)))
print('  parity-obeying: max |sum diff| mod pi^2 = %.2e'%max([abs(x[1]) for x in okp]+[0]))
print('  parity-violating: |sum diff| values in units pi^2/2: %s'%sorted(set(np.round(np.array([abs(x[1]) for x in badp])/(np.pi**2/2),4)))[:6])
print('knots where weak differs from strong by pi^2/2:',[r[0] for r in rows if abs(r[2])>1e-8][:20])

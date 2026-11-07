# SCRIPT: STRONG-FLAT-05
# Is the pi^2/2 sensitivity to kernel shifts tied to tetrahedra read with eps=-1? For every hyperbolic knot 4-7 crossings, over ALL branchings (cap 64),
# split by number of eps=-1 tetrahedra; for each, test every kernel basis vector k (+k) and record whether sum changes by pi^2/2.
import sys; sys.path.insert(0,'/home/claude/votkp_research')
exec(open('/home/claude/votkp_research/strong_flat_03.py').read().split("rng=np.random")[0])
from collections import defaultdict
stat=defaultdict(lambda:[0,0])   # nneg -> [shifts tested, shifts with odd change]
for nm in [x for x in names if int(x.split('_')[0])<=7]:
    M=snappy.Manifold(nm)
    if M.solution_type()!='all tetrahedra positively oriented': continue
    z=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); n=len(z); zp=1/(1-z)
    E=np.array(M.gluing_equations().list(),dtype=int).reshape(-1,3*n); a,b,c=E[:,0::3],E[:,1::3],E[:,2::3]
    L=(a-c)@np.log(z)+(b-c)@np.log(zp); rhs=np.round((-L/(1j*np.pi)).real).astype(int); A0=np.hstack([a-c,b-c])
    base=np.array(solve_mod(A0.tolist(),[0]*len(A0),rhs.tolist())[:2*n])
    ker=pari.matkerint(pari('['+';'.join(','.join(str(int(x)) for x in r) for r in A0)+']'))
    K=np.array([[int(ker[i,j]) for j in range(ker.ncols())] for i in range(2*n)])
    for orders in find_branching(M,maxsol=64):
        nneg=sum(1 for o in orders if perm_sign(o)==-1); t0=Rtot(z,orders,list(base),n)
        for j in range(K.shape[1]):
            dlt=mp((Rtot(z,orders,list(base+K[:,j]),n)-t0).real)/(np.pi**2/2)
            stat[nneg][0]+=1; stat[nneg][1]+= abs(round(dlt))%2
for k in sorted(stat): print('tetra with eps=-1: %d  shifts tested %d, odd (pi^2/2) change in %d'%(k,*stat[k]))

# SCRIPT: STRONG-FLAT-06
# Candidate strongest parity condition: parity vector of the flattening equals EXACTLY that of l(x;0,0) in the ordered labelling
# (new slots (0,1,0) in this reading, validated in STRONG-FLAT-02/Prop 5.3 check), i.e. p,q,r mod 2 fixed per tetra. Then every shift between
# two such flattenings is even, so the sum is invariant mod pi^2 automatically (N(2k)=2N(k)). Question: does such a flattening exist
# (log rows solvable with those parities) for every knot/branching, and does it give exact CS mod pi^2/2?
import sys; sys.path.insert(0,'/home/claude/votkp_research')
exec(open('/home/claude/votkp_research/strong_flat_03.py').read().split("rng=np.random")[0])
ok=0;tot=0;fail=[];mis=[]
for nm in names:
    M=snappy.Manifold(nm)
    if M.solution_type()!='all tetrahedra positively oriented': continue
    z=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); n=len(z); zp=1/(1-z); cv=complex(M.complex_volume())
    E=np.array(M.gluing_equations().list(),dtype=int).reshape(-1,3*n); a,b,c=E[:,0::3],E[:,1::3],E[:,2::3]
    L=(a-c)@np.log(z)+(b-c)@np.log(zp); rhs=np.round((-L/(1j*np.pi)).real).astype(int); A0=np.hstack([a-c,b-c])
    for orders in find_branching(M,maxsol=6):
        tot+=1
        dold=np.zeros(2*n,int)
        for t in range(n):
            o=orders[t]; jk=[pair_of(o[0],o[1]),pair_of(o[0],o[2]),pair_of(o[0],o[3])]
            po=[0,0,0]; po[jk[1]]=1          # odd parity on the slot that the Prop 5.3 test selected (new slot 1)
            dold[t]=po[0]; dold[n+t]=po[1]
        # rows: x_i = dold_i mod 2 for all unknowns
        I=np.eye(2*n,dtype=int)
        s=solve_mod(np.vstack([A0,I]).tolist(),[0]*len(A0)+[2]*(2*n),list(rhs)+list(dold))
        if s is None: fail.append((nm,'rhs parity')); continue
        ok+=1; mis.append(abs(m(-Rtot(z,orders,s,n).real-cv.imag)))
print('runs %d ; flattening with exact l(x;0,0)-parity exists in %d ; CS exact (<1e-8) in %d ; failures e.g. %s'%(tot,ok,sum(1 for x in mis if x<1e-8),fail[:8]))

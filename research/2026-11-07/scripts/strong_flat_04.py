# SCRIPT: STRONG-FLAT-04
# Which integer shifts of a flattening change the sum of eps*R by pi^2/2 (mod pi^2)? Takes the strong solution of each knot, adds each integer
# kernel vector k (edges and cusp log-parameters unchanged) with coefficient 1 and 2, and reports the change in units of pi^2/2, with k mod 2
# and with the parity-model verdict. Looking for the exact extra mod-2 condition (Neumann: strong flattening => sum exact mod pi^2).
import sys; sys.path.insert(0,'/home/claude/votkp_research')
exec(open('/home/claude/votkp_research/strong_flat_03.py').read().split("rng=np.random")[0])
for nm in ['4_1','5_2','6_1','6_2','7_2']:
    M=snappy.Manifold(nm)
    z=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); n=len(z); zp=1/(1-z)
    E=np.array(M.gluing_equations().list(),dtype=int).reshape(-1,3*n); a,b,c=E[:,0::3],E[:,1::3],E[:,2::3]
    L=(a-c)@np.log(z)+(b-c)@np.log(zp); rhs=np.round((-L/(1j*np.pi)).real).astype(int); A0=np.hstack([a-c,b-c])
    orders=find_branching(M,maxsol=1)[0]
    pc=parity_constraints(M)[0]; Pm=np.array([[(x>>v)&1 for v in range(2*n)] for x,r in pc],int).reshape(len(pc),2*n); pb=np.array([r for x,r in pc])
    ss=solve_mod(np.vstack([A0,Pm]).tolist(),[0]*len(A0)+[2]*len(pc),list(rhs)+list(pb)); base=np.array(ss[:2*n])
    ker=pari.matkerint(pari('['+';'.join(','.join(str(int(x)) for x in r) for r in A0)+']'))
    K=np.array([[int(ker[i,j]) for j in range(ker.ncols())] for i in range(2*n)])
    t0=Rtot(z,orders,list(base),n)
    print(nm,'n',n,'kernel rank',K.shape[1],'cons rows',len(pc))
    for j in range(K.shape[1]):
        k=K[:,j]; out=[]
        for cc in (1,2):
            v=base+cc*k; out.append(round(mp((Rtot(z,orders,list(v),n)-t0).real)/(np.pi**2/2),3))
        print('   k=',k.tolist(),'mod2',(k%2).tolist(),'Δ(1,2) in pi^2/2:',out,'parity ok after +k:',bool(np.all(((Pm@((base+k)%2))%2)==pb)))

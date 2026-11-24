# SCRIPT: GAPS186-AXIOM2-DIAGONAL-01
# Axiom 2 split into A = B and A != B, with the max ratio |S|/(p^1.5) tracked against p.
# The cited Fouvry-Kowalski-Michel bound may assume A != B; the Lean axiom also allows A = B.
# KILL (written before the run): the axiom is in danger if the A = B maximum grows with p
# (a fitted exponent above 0 in ratio ~ p^a, with the ratio still rising at the largest p).
import numpy as np, sys
def primes(n):
    s=np.ones(n+1,bool); s[:2]=False
    for i in range(2,int(n**.5)+1):
        if s[i]: s[i*i::i]=False
    return [int(x) for x in np.nonzero(s)[0]]
out=[]
for p in [x for x in primes(int(sys.argv[1])) if x>=5]:
    e=np.exp(2j*np.pi*np.arange(p)/p); inv=np.array([pow(int(u),p-2,p) if u else 0 for u in range(p)])
    u=np.arange(1,p); K2=np.array([e[(u+c*inv[u])%p].sum() for c in range(p)])
    t=np.array([tt for tt in range(1,p-1)]); it=inv[t]; it1=inv[(t+1)%p]
    A=np.arange(1,p)
    Ac=K2[(A[:,None]*it[None,:])%p]; Bc=K2[(A[:,None]*it1[None,:])%p]
    S=np.abs(Ac@Bc.T)/p**1.5
    d=np.diag(S).max(); np.fill_diagonal(S,0); o=S.max()
    out.append((p,d,o))
for p,d,o in out[::max(1,len(out)//14)]+[out[-1]]:
    print('p=%4d  A=B max %.3f   A!=B max %.3f'%(p,d,o))
ps=np.array([x[0] for x in out]); ds=np.array([x[1] for x in out]); os_=np.array([x[2] for x in out])
k=ps>=50
print('fitted exponent a (ratio ~ p^a): A=B %.3f   A!=B %.3f'%(np.polyfit(np.log(ps[k]),np.log(ds[k]),1)[0],np.polyfit(np.log(ps[k]),np.log(os_[k]),1)[0]))

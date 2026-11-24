# SCRIPT: OPPOSITE-TWIN-C-01
# T0 reference twin chain; c-30 (mod 30 arms), c-7 (mod 7, five arms, SO(1,5)), c-9 (mod 9, three arms), c-rev (reversed product).
# Kill lines in PREDICTIONS.md (written before this run).
import numpy as np, math
from owalk import *
N=10**8; P=primes_upto(N)
tw=P[:-1][(P[1:]-P[:-1])==2]; T=tw[tw>5]
r=np.log(T[1:]/T[:-1]); nxt=T[1:]
cuts=[10**k for k in range(3,9)]
def shares(arm,m):
    return np.array([r[arm==s].sum() for s in range(m)])/r.sum()
out={}
arm=np.searchsorted([1,7,9],nxt%10); E=np.eye(3); Pv=np.ones(3)/3
print('T0 r-weighted shares',shares(arm,3).round(4))
rows=report('T0 twin end digit 1/7/9',nxt,r,arm,E,cuts,Pv); out['T0']=(rows,verdict(rows,np.linalg.norm(Pv)))
arm30=np.searchsorted([11,17,29],nxt%30)
print('c-30: arms identical to end-digit arms?',bool((arm30==arm).all()))
rows=report('c-30 twin residue mod 30',nxt,r,arm30,E,cuts,Pv); out['c30']=(rows,verdict(rows,np.linalg.norm(Pv)))
res7=nxt%7; print('mod-7 residues seen',np.unique(res7))
arm7=np.searchsorted([1,2,3,4,6],res7); E5=np.eye(5); P5=np.ones(5)/5
print('c-7 r-weighted shares',shares(arm7,5).round(4))
rows=report('c-7 twin residue mod 7, 5 arms SO(1,5)',nxt,r,arm7,E5,cuts,P5); out['c7']=(rows,verdict(rows,np.linalg.norm(P5)))
res9=nxt%9; print('mod-9 residues seen',np.unique(res9))
arm9=np.searchsorted([2,5,8],res9)
print('c-9 r-weighted shares',shares(arm9,3).round(4))
rows=report('c-9 twin residue mod 9',nxt,r,arm9,E,cuts,Pv); out['c9']=(rows,verdict(rows,np.linalg.norm(Pv)))
# reversed product B_N ... B_1 at cut 1e8 and 1e7: walk the reversed sequence
print('=== c-rev reversed product (B_N...B_1) at each cut, versus T0 at the same cut')
for x in cuts:
    m=np.searchsorted(nxt,x,side='right')
    D,Nn,RR,_=walk(r[:m][::-1].copy(),arm[:m][::-1].copy(),E,np.array([m-1]))
    Df,Nf,Rf,_=walk(r[:m],arm[:m],E,np.array([m-1]))
    uf=Rf[0].T@Nf[0]
    print(' cut %.0e: d_rev-d_fwd=%.2e  turn_rev=%.4f turn_fwd=%.4f  |R_rev - R_fwd^T|=%.2e  |n_rev - u_fwd|=%.2e'%(
        x,D[0]-Df[0],rot_angles(RR[0])[0],rot_angles(Rf[0])[0],np.abs(RR[0]-Rf[0].T).max(),np.abs(Nn[0]-uf).max()))
import pickle; pickle.dump(out,open('v_twin_c.pkl','wb'))

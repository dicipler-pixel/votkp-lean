# SCRIPT: ladder_data_v2
# Entanglement ladder of a block of the dimerized chain (v = 0), ũ = (t2-t1)/(t2+t1).
# Why this checks the claim: if the block's levels are a ladder with spacing 4 pi K(ũ)/K'(ũ),
# then at ũ^2 = 1/2 (t2/t1 = 3+2 sqrt2, the loop-wall ratio) the spacing must read 4 pi.
import numpy as np, mpmath as mp, json
def block_levels(t1,t2,v,N=600,L=40,off=280):
    H=np.zeros((N,N))
    for i in range(N-1): H[i,i+1]=H[i+1,i]=-(t1 if i%2==0 else t2)
    for i in range(N): H[i,i]=v*(1 if i%2==0 else -1)
    w,U=np.linalg.eigh(H); occ=U[:,:N//2]; C=occ@occ.T
    nu=np.linalg.eigvalsh(C[off:off+L,off:off+L]); nu=nu[(nu>1e-15)&(nu<1-1e-15)]
    return np.sort(np.log((1-nu)/nu))
def spacing(u): return float(4*mp.pi*mp.ellipk(u*u)/mp.ellipk(1-u*u))
out=[]
for u in np.linspace(0.30,0.92,32):
    t2=(1+u)/(1-u); e=block_levels(1.0,t2,0.0)
    pos=np.sort(e[e>0.5]); meas=float(pos[1]-pos[0]) if len(pos)>1 else None
    out.append(dict(u=round(float(u),5),D=spacing(u),meas=meas,eps=[round(float(x),4) for x in e if abs(x)<40]))
uw=2**-0.5; e=block_levels(1.0,3+2*2**.5,0.0); pos=np.sort(e[e>0.5])
print('at wall: formula',spacing(uw),' 4pi',4*np.pi,' measured',pos[1]-pos[0], pos[:3])
for r in out[::6]: print(r['u'],round(r['D'],4),r['meas'] and round(r['meas'],4))
# reference Rice-Mele block (0.6,1,0.4): levels and which rung is inside the wall
e=block_levels(0.6,1.0,0.4,L=41); ew=np.log(3+2*2**.5)
nu=1/(1+np.exp(e)); s=-(nu*np.log(nu)+(1-nu)*np.log(1-nu)); 
print('RM ref levels',np.round(e[abs(e)<20],4)); print('inside',e[abs(e)<ew], 'entropy share of inside',s[abs(e)<ew].sum()/s.sum())
json.dump(dict(sweep=out,ref=[round(float(x),4) for x in e if abs(x)<36]),open('ladder_data_v2.json','w'))

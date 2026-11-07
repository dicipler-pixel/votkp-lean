# SCRIPT: TILT-01
# Exploratory. Opposed fusion with the branches no longer exact mirrors: V (+) -(V + eps*D), D a fixed real matrix.
# Read: how far H(w) restricted to the shared half L = {(x,x)} departs from zero, and how the principal angles
# between the positive projector P+(w) and L spread away from 45 deg, as eps grows. Also a true unlike pair:
# 3_1 fused with the reversed mirror of 5_1 (no shared half of equal size exists).
import numpy as np
def seifert_T2(n):
    m=n-1; V=np.zeros((m,m))
    for i in range(m): V[i,i]=-1
    for i in range(m-1): V[i+1,i]=1
    return V
def H(V,w): return (1-w)*V+(1-np.conj(w))*V.T
def bsum(A,B):
    n,m=A.shape[0],B.shape[0]; C=np.zeros((n+m,n+m)); C[:n,:n]=A; C[n:,n:]=B; return C
rng=np.random.default_rng(7); V=seifert_T2(7); n=V.shape[0]; D=rng.standard_normal((n,n))
Lb=np.vstack([np.eye(n),np.eye(n)])/np.sqrt(2)
grid=np.linspace(0.02,np.pi-0.02,300)
print('7_1 with a deformed mirror: eps, max|H on L|, principal angles P+ vs L (min..max deg), signature range')
for eps in [0,0.01,0.03,0.1,0.3,1.0]:
    M=bsum(V,-(V+eps*D)); iso=0; lo=90; hi=0; sg=set()
    for a in grid:
        w=np.exp(1j*a); Hw=H(M,w); iso=max(iso,np.max(np.abs(Lb.T@Hw@Lb)))
        e,U=np.linalg.eigh(Hw)
        if np.min(np.abs(e))<1e-9: continue
        Q=U[:,e>0]; s=np.linalg.svd(Q.conj().T@Lb,compute_uv=False)
        ang=np.degrees(np.arccos(np.clip(s,0,1))); lo=min(lo,ang.min()); hi=max(hi,ang.max())
        sg.add(int(np.sum(e>0)-np.sum(e<0)))
    print(f'   eps {eps:<5} max|H on L| {iso:8.4f}   angles {lo:7.3f} .. {hi:7.3f}   signatures {sorted(sg)}')
# unlike pair: 3_1 (+) -(5_1); compare signature function and angle spread to a 2-dim and 4-dim block
V3=seifert_T2(3); V5=seifert_T2(5); M=bsum(V3,-V5)
sg=[]; 
for a in grid:
    w=np.exp(1j*a); e=np.linalg.eigvalsh(H(M,w)); sg.append(int(np.sum(e>1e-9)-np.sum(e<-1e-9)))
print('3_1 # reversed-mirror 5_1: signature values met around the circle:',sorted(set(sg)),' (nonzero windows survive: hands do not fully cancel)')
# part 2: where does the 45 deg lock break? distance of each phase to the nearest wall of 7_1 vs angle deviation
walls=np.array([1,3,5])*np.pi/7
print('\nwhere the lock breaks (eps = 0.03): median and max angle deviation from 45 deg, by distance to nearest wall')
M=bsum(V,-(V+0.03*D)); bins=[(0,0.02),(0.02,0.1),(0.1,0.3),(0.3,1.6)]
dev={b:[] for b in bins}
for a in np.linspace(0.005,np.pi-0.005,4000):
    w=np.exp(1j*a); e,U=np.linalg.eigh(H(M,w))
    if np.min(np.abs(e))<1e-12: continue
    Q=U[:,e>0]; s=np.linalg.svd(Q.conj().T@Lb,compute_uv=False); ang=np.degrees(np.arccos(np.clip(s,0,1)))
    dw=np.min(np.abs(walls-a))
    for b in bins:
        if b[0]<=dw<b[1]: dev[b].append(np.max(np.abs(ang-45)))
for b in bins: print(f'   distance to wall {b[0]:.2f}-{b[1]:.2f} rad: n={len(dev[b]):4d}  median dev {np.median(dev[b]):6.3f} deg  max {np.max(dev[b]):6.3f} deg')

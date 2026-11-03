# SCRIPT: MATTER-DISK-S06  is the disk-exit law universal? second model: the cone paper's band in 1D
# WHY THIS CHECK PROVES WHAT IT CLAIMS
# Section 5 found, on the PT-symmetric SSH chain, that the census levels leave the Smith disk exactly
# where the band-averaged Petermann factor <K> equals 2. For any two-band h(k) = d(k).sigma the
# Petermann factor of the lower band is K(k) = (1 + |d|^2/|E|^2)/2 with E^2 = d.d (checked below).
# A law that belongs to the SSH chain alone would fail on a different band. Here the band is the cone
# paper's family made one-dimensional, d = (t1 + cos k, sin k, m + i*gamma): a mass term, no PT symmetry.
# Path: start closed (gamma = 0, census real, inside the disk) and raise gamma until the census leaves
# the disk (largest rotation |Im ln z| reaches pi/2, census window 1e-9 < nu < 1-1e-9).
# KILL (written before the run): at any of the four (t1, m) settings, <K> at the measured exit differs
# from 2 by more than 1e-4. Control: gamma = 0 must give a real census inside the disk.
import numpy as np
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
def H(t1,m,g,k): return (t1+np.cos(k))*sx+np.sin(k)*sy+(m+1j*g)*sz
def lower(t1,m,g,k):
    ev,R=np.linalg.eig(H(t1,m,g,k)); o=np.argsort(ev.real); ev,R=ev[o],R[:,o]
    L=np.linalg.inv(R).conj().T; return ev,R,L
def corr(t1,m,g,N,Lc):
    ks=2*np.pi*(np.arange(N)+0.5)/N; C=np.zeros((2*Lc,2*Lc),complex)
    for k in ks:
        ev,R,L=lower(t1,m,g,k); P=np.outer(R[:,0],L[:,0].conj())
        ph=np.exp(1j*k*np.arange(Lc)); C+=np.kron(np.outer(ph,ph.conj()),P)
    return C/N
def rotation(t1,m,g,N=2000,Lc=40,d=1e-9):
    nu=np.linalg.eigvals(corr(t1,m,g,N,Lc)).astype(complex)
    keep=(np.abs(nu)>d)&(np.abs(1-nu)>d); nu=nu[keep]
    if len(nu)==0: return 0.0, 0.0
    W=np.log((1-nu)/nu); return np.max(np.abs(W.imag))/np.pi, np.max(np.abs(1-2*nu))
ks=2*np.pi*(np.arange(4000)+0.5)/4000
def meanK(t1,m,g):
    out=[]
    for k in ks:
        ev,R,L=lower(t1,m,g,k); out.append(np.vdot(L[:,0],L[:,0]).real*np.vdot(R[:,0],R[:,0]).real)
    return np.mean(out)
# check the general Petermann formula on random points
rng=np.random.default_rng(5); worst=0
for _ in range(300):
    t1,m,g,k=rng.uniform(0.2,2),rng.uniform(-1,1),rng.uniform(0,1.5),rng.uniform(0,2*np.pi)
    ev,R,L=lower(t1,m,g,k); d=np.array([t1+np.cos(k),np.sin(k),m+1j*g]); E2=np.sum(d*d)
    if abs(E2)<1e-3: continue
    Kn=np.vdot(L[:,0],L[:,0]).real*np.vdot(R[:,0],R[:,0]).real; Kf=(1+np.sum(abs(d)**2)/abs(E2))/2
    worst=max(worst,abs(Kn-Kf))
print('general Petermann formula K=(1+|d|^2/|E|^2)/2, worst error on 300 random points:',worst)
print('settings (t1, m): control at gamma=0, measured exit gamma, <K> at exit')
ok=True
for t1,m in [(0.5,0.4),(1.5,0.4),(0.5,0.0),(1.5,0.8)]:
    r0,G0=rotation(t1,m,0.0)
    lo,hi=0.0,None; g=0.05
    while hi is None and g<4:
        if rotation(t1,m,g)[0]>=0.5: hi=g
        else: lo=g; g*=1.4
    if hi is None: print(f'  ({t1},{m}): census never left the disk up to gamma=4'); ok=False; continue
    for _ in range(28):
        mid=(lo+hi)/2
        if rotation(t1,m,mid)[0]<0.5: lo=mid
        else: hi=mid
    ge=(lo+hi)/2; K=meanK(t1,m,ge)
    ok&=abs(K-2)<1e-4
    print(f'  ({t1},{m}): control rot={r0:.3f} pi max|Gamma|={G0:.4f} | exit gamma={ge:.7f} | <K>={K:.6f}  {"PASS" if abs(K-2)<1e-4 else "FAIL"}')
print('VERDICT:', 'exit law <K> = 2 holds on the second model' if ok else 'KILLED on the second model at the stated bar')

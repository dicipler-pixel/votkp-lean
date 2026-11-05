# SCRIPT: s16_weight_between_checks
"""s16: numerical controls for the weight-between theorems (journal edition).
Random positive contractions C on a=4, b=5 (seed 16)."""
import numpy as np
rng=np.random.default_rng(16); a,b=4,5; n=a+b
def rand_contraction(n,pure=False):
    Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); U,_=np.linalg.qr(Z)
    lam=(rng.integers(0,2,n).astype(float) if pure else rng.uniform(0,1,n))
    return U@np.diag(lam)@U.conj().T
h=lambda x: -(x*np.log(x)+(1-x)*np.log(1-x))
def trh(M): e=np.linalg.eigvalsh(M); e=np.clip(e,1e-300,1-1e-16); return np.sum(h(e))
L=[]; w={}
def upd(k,x): w[k]=max(w.get(k,-np.inf),x)
for _ in range(400):
    C=rand_contraction(n); A=C[:a,:a]; B=C[:a,a:]; D=C[a:,a:]
    X=B@B.conj().T; XB=B.conj().T@B; F=A-A@A
    TA=(C-C@C)[:a,:a]
    upd('defect split |F-T-X|',np.abs(F-TA-X).max())
    ex=np.linalg.eigvalsh(X); ef=np.linalg.eigvalsh(F)
    upd('order: max eig X - 1/4',ex.max()-0.25); upd('order: min eig(F-X)',-np.linalg.eigvalsh(F-X).min())
    pos=lambda e: np.sort(e[e>1e-12])
    upd('two-sided |spec X_A - spec X_B|',np.abs(pos(ex)-pos(np.linalg.eigvalsh(XB))).max())
    # min-max comparison
    upd('ordered lambda_j(X)-lambda_j(F)',(np.sort(ex)-np.sort(ef)).max())
    # stability
    E=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); E=(E+E.conj().T)/2; E*=1e-3/np.linalg.norm(E,2)
    Ct=C+E; ev,V=np.linalg.eigh(Ct); Ct=V@np.diag(np.clip(ev,0,1))@V.conj().T
    dl=np.linalg.norm(C-Ct,2); Xt=Ct[:a,a:]@Ct[:a,a:].conj().T
    upd('stability ||X-X~||/delta - 1',np.linalg.norm(X-Xt,2)/dl-1)
# information bound on 64 interior covariances
lo=np.inf; up=np.inf
for _ in range(64):
    C=rand_contraction(n); ev,V=np.linalg.eigh(C); dlt=0.05; ev=dlt+(1-2*dlt)*ev; C=V@np.diag(ev)@V.conj().T
    A=C[:a,:a]; D=C[a:,a:]; X=C[:a,a:]@C[:a,a:].conj().T
    I=trh(A)+trh(D)-trh(C); tx=np.trace(X).real
    lo=min(lo,I-4*tx); up=min(up,tx/(dlt*(1-dlt))-I)
L.append(f'info bound, 64 covariances with spectrum in [0.05,0.95]: min(I_G-4TrX)={lo:.3e}, min(TrX/(d(1-d))-I_G)={up:.3e}')
for r in [1e-2,1e-3,1e-4]:
    I=2*np.log(2)-2*h(0.5+r); L.append(f'sharp family C=1/2 I+r sigma_x, r={r:g}: I_G/TrX={I/r**2:.9f}')
# pure states: census recovery
mx=0
for _ in range(100):
    C=rand_contraction(n,pure=True); A=C[:a,:a]; X=C[:a,a:]@C[:a,a:].conj().T
    mx=max(mx,np.abs(X-(A-A@A)).max())
L.append(f'pure states (100): max |X_A-(A_C-A_C^2)| = {mx:.2e}')
# speed-limit saturating pair
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]])
worst=0
for om in [0.5,1.0,2.0]:
    H=om*sx
    for sgn in [+1,-1]:
        P0=0.5*(np.eye(2)+sgn*sy)
        for t in np.linspace(0.01,0.7/om,31):
            if abs(np.sin(2*om*t))>0.95: continue
            U=np.cos(om*t)*np.eye(2)-1j*np.sin(om*t)*sx; P=U@P0@U.conj().T
            Pd=-1j*(H@P-P@H); nu=P[0,0].real; nud=Pd[0,0].real
            taud=-nud/(nu*(1-nu)); g=0.5*np.linalg.norm(Pd)**2; S=1/(nu*(1-nu))
            worst=max(worst,abs(taud**2/(4*g*S)-1))
L.append(f'offset speed limit, pair P+-: max |taudot^2/(4gS)-1| over 3 omegas, 2 signs, 31 times = {worst:.1e}')
for k,x in w.items(): L.insert(0,f'400 random contractions (a=4,b=5): max[{k}] = {x:.2e}')
L.insert(0,'(for order and stability lines, a negative maximum means the bound holds with that margin)')
print('\n'.join(L)); open('../outputs/s16_weight_between_checks.txt','w').write('\n'.join(L)+'\n')

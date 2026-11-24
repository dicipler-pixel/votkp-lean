# SCRIPT: TWIN-TURN-CONNECTION-ENERGY-01
# Checks (1) the 2x2 identity ||[L,L*]||_F = sqrt2 sinh d |n - R n| for L = P U (polar split)
# and (2) runs the twin chain as an SL(2,C) product and reads frame turn, heading, normalized non-normality.
import numpy as np, math
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
S=[sx,sy,sz]
def sv(v): return v[0]*sx+v[1]*sy+v[2]*sz
def boost(e,r): return math.cosh(r/2)*np.eye(2)+math.sinh(r/2)*sv(e)
def polar(L):
    H=L@L.conj().T; w,V=np.linalg.eigh(H); P=V@np.diag(np.sqrt(w))@V.conj().T
    U=np.linalg.solve(P,L); return P,U
def vec(M): return np.array([0.5*np.trace(M@s).real for s in S])
def rotvec(U):  # rotation 3x3 of U acting v -> U v U*
    return np.array([[0.5*np.trace(s@U@t@U.conj().T).real for t in S] for s in S])
rng=np.random.default_rng(1); worst=0
for _ in range(200):
    L=np.eye(2,dtype=complex)
    for k in range(5):
        e=rng.normal(size=3); e/=np.linalg.norm(e); L=L@boost(e,rng.uniform(0,2))
        th=rng.normal(size=3); a=np.linalg.norm(th); L=L@(math.cos(a/2)*np.eye(2)-1j*math.sin(a/2)*sv(th/a))
    P,U=polar(L); d=math.acosh(np.trace(L@L.conj().T).real/2)
    n=vec(P); n/=np.linalg.norm(n); R=rotvec(U.conj().T)
    lhs=np.linalg.norm(L@L.conj().T-L.conj().T@L); rhs=math.sqrt(2)*math.sinh(d)*np.linalg.norm(n-R@n)
    worst=max(worst,abs(lhs-rhs)/max(lhs,1e-12))
print('identity check, worst relative error over 200 random L:',worst)
# twin chain
N=int(2e7); sieve=np.ones(N+3,bool); sieve[:2]=False
for i in range(2,int((N+2)**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
tw=[p for p in np.nonzero(sieve[:N])[0] if p>=11 and sieve[p+2]]
ax={1:np.array([1.,0,0]),7:np.array([0,1.,0]),9:np.array([0,0,1.])}
L=np.eye(2,dtype=complex); marks={10**3,10**4,10**5,10**6,10**7}
print('a_n  L  d  d-L/sqrt3  frame_turn_deg  beta_deg(heading vs rot axis)  Nnorm  sqrt2*sin(phi/2)*sin(beta)')
for i in range(1,len(tw)):
    r=math.log(tw[i]/tw[i-1]); L=L@boost(ax[tw[i]%10],r)
    if tw[i]%10==1 and i%50==0:  # renormalise det drift
        L/=np.sqrt(np.linalg.det(L))
    nxt=tw[i+1] if i+1<len(tw) else None
    if any(tw[i-1]<m<=tw[i] for m in marks):
        P,U=polar(L); d=math.acosh(np.trace(L@L.conj().T).real/2); Lp=math.log(tw[i]/11)
        n=vec(P); n/=np.linalg.norm(n)
        c=np.clip(abs(np.trace(U).real)/2,0,1); phi=2*math.acos(c)
        m=np.array([ (1j*np.trace(U@s)).real for s in S]); m=m/np.linalg.norm(m) if np.linalg.norm(m)>1e-14 else m
        beta=math.degrees(math.acos(abs(np.clip(n@m,-1,1))))
        Nn=np.linalg.norm(L@L.conj().T-L.conj().T@L)/np.linalg.norm(L)**2
        print(tw[i],round(Lp,4),round(d,4),round(d-Lp/math.sqrt(3),4),round(math.degrees(phi),3),round(beta,2),round(Nn,5),round(math.sqrt(2)*math.sin(phi/2)*math.sin(math.radians(beta))*math.tanh(d),5))

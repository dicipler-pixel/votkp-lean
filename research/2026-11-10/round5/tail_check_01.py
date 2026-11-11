# SCRIPT: TAIL-CHECK-01
# Independent check of the hidden-walk comparison in the attached note, sharing no code with its checker or with the
# original SU(3) verifier.  Model as the note states it: characters (p,q), c = (p^2+pq+q^2+3p+3q)/3,
# H = C + 3 lam - (lam/2) A, A the six-neighbour fusion adjacency.
# Why this decides it: (a) the note's inequality says K_m(z) <= S(z), so every eigenvalue of K_m must lie at or below the
# matching eigenvalue of the exact Schur complement, computed here from a very large truncation (cutoff 60);
# (b) the note's conclusion is E1 >= z, so the true E1 of the large truncation must be >= each claimed z;
# (c) K_m must have exactly one negative eigenvalue at each claimed z, and more than one at a z above the true E1.
# KILL: any eigenvalue of K_m above the exact Schur one (beyond 1e-9), any claimed z above the true E1, or a wrong count.
import numpy as np
def states(N): return [(p,s-p) for s in range(N+1) for p in range(s+1)]
def cas(p,q): return (p*p+p*q+q*q+3*p+3*q)/3
def nbrs(p,q): return [v for v in [(p+1,q),(p-1,q+1),(p,q-1),(p,q+1),(p+1,q-1),(p-1,q)] if v[0]>=0 and v[1]>=0]
def ham(N,lam):
    st=states(N); ix={v:i for i,v in enumerate(st)}; H=np.zeros((len(st),len(st)))
    for v,i in ix.items():
        H[i,i]=cas(*v)+3*lam
        for w in nbrs(*v):
            if w in ix: H[i,ix[w]]-=lam/2
    return st,ix,H
def run(N,lam,z,m,BIG=60):
    st,ix,H=ham(BIG,lam); ev=np.linalg.eigvalsh(H); nP=(N+1)*(N+2)//2
    A=H[:nP,:nP]; B=H[:nP,nP:]; D=H[nP:,nP:]; n=D.shape[0]
    S=A-z*np.eye(nP)-B@np.linalg.solve(D-z*np.eye(n),B.T)
    D0=np.diag(D)-z; W=-(D-np.diag(np.diag(D)))
    s=N+1; cplus=(s*s-(s*s)//4+3*s)/3; d=cplus+3*lam-z; rho=3*lam/d; eps=rho**(m+1)/(d*(1-rho))
    Y=B.T/D0[:,None]; R=B@Y
    for _ in range(m): Y=(W@Y)/D0[:,None]; R=R+B@Y
    K=A-z*np.eye(nP)-R-eps*(B@B.T)
    eK=np.linalg.eigvalsh(K); eS=np.linalg.eigvalsh(S)
    print('lam=%g N=%d m=%d z=%g: rho=%.5f eps=%.3e | true E0=%.7f E1=%.7f (cutoff %d) | neg eig of K_m: %d, of exact S: %d | max(eig K - eig S) = %.2e | min Casimir omitted %.4f vs c+ %.4f | norm W %.4f vs 3 lam %.1f'%(
        lam,N,m,z,rho,eps,ev[0],ev[1],BIG,(eK<0).sum(),(eS<0).sum(),(eK-eS).max(),min(cas(*v) for v in st[nP:]),cplus,np.linalg.norm(W,2),3*lam))
    return ev
print('claimed cases'); 
run(6,10,15.1,6); ev=run(15,100,43.3,6); run(15,100,50.56,12)
print('controls: z above the true E1 must give more than one negative eigenvalue')
run(6,10,17.0,6); run(15,100,58.5,12)
print('how far depth alone can go at fixed N (largest z with one negative eigenvalue, bisection)')
for N,lam,E1 in ((6,10,16.8641),(15,100,57.9392)):
    for m in (0,6,12,24,48):
        st,ix,H=ham(60,lam); nP=(N+1)*(N+2)//2; A=H[:nP,:nP]; B=H[:nP,nP:]; D=H[nP:,nP:]; s=N+1; cplus=(s*s-(s*s)//4+3*s)/3
        def cnt(z):
            D0=np.diag(D)-z; W=-(D-np.diag(np.diag(D))); d=cplus+3*lam-z; rho=3*lam/d
            if d<=0 or rho>=1: return 99
            eps=rho**(m+1)/(d*(1-rho)); Y=B.T/D0[:,None]; R=B@Y
            for _ in range(m): Y=(W@Y)/D0[:,None]; R=R+B@Y
            return int((np.linalg.eigvalsh(A-z*np.eye(nP)-R-eps*(B@B.T))<0).sum())
        lo,hi=H[0,0]-3*lam, min(E1+1,cplus-1e-6)
        lo=np.linalg.eigvalsh(H)[0]+1e-6
        for _ in range(50):
            mid=(lo+hi)/2
            if cnt(mid)<=1: lo=mid
            else: hi=mid
        print('   lam=%g N=%d depth %2d: threshold z = %.6f   (true E1 = %.4f)'%(lam,N,m,lo,E1))

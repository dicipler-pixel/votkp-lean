# SCRIPT: BRANCH-CUT-02
# Exploratory. (A) walls and windows of parallel K#K vs opposed K#(-K-bar) on the unit circle.
# (B) the cut: opposed Seifert matrix V (+) (-V); test whether the diagonal half L = {(x,x)} is isotropic
#     for H(w) at every phase, compare the parallel fusion, and read principal angles between P+(w) and L.
import numpy as np, sympy as sp
t=sp.symbols('t')
def seifert_T2(n):
    m=n-1; V=np.zeros((m,m))
    for i in range(m): V[i,i]=-1
    for i in range(m-1): V[i+1,i]=1
    return V
knots={'3_1':seifert_T2(3),'5_1':seifert_T2(5),'7_1':seifert_T2(7),'4_1':np.array([[-1.,1.],[0.,1.]])}
def H(V,w): return (1-w)*V+(1-np.conj(w))*V.T
def bsum(A,B):
    n,m=A.shape[0],B.shape[0]; C=np.zeros((n+m,n+m)); C[:n,:n]=A; C[n:,n:]=B; return C
def sig(M): e=np.linalg.eigvalsh(M); return int(np.sum(e>1e-9)-np.sum(e<-1e-9))
def walls(V):
    p=sp.Poly(sp.expand(sp.Matrix(V.astype(int)).__sub__(t*sp.Matrix(V.T.astype(int))).det()),t)
    rts=[complex(r) for r in sp.Poly(p,t).nroots(n=30)]
    out=[]
    for r in rts:
        if abs(abs(r)-1)<1e-8 and r.imag>1e-9: out.append(np.angle(r))
    return sorted(set(np.round(out,10)))
print('(A) WALLS AND WINDOWS  (phase a of w=e^{ia}; jump = signature just after minus just before)')
for k,V in knots.items():
    par=bsum(V,V); opp=bsum(V,-V)
    ws=walls(V)
    rowK=[];rowP=[];rowO=[]
    for a in ws:
        d=1e-6; w1,w2=np.exp(1j*(a-d)),np.exp(1j*(a+d))
        rowK.append(sig(H(V,w2))-sig(H(V,w1))); rowP.append(sig(H(par,w2))-sig(H(par,w1))); rowO.append(sig(H(opp,w2))-sig(H(opp,w1)))
    print(f'  {k}: walls at a/pi = {[round(a/np.pi,5) for a in ws]}')
    print(f'      jump K {rowK} | parallel {rowP} | opposed {rowO}')
print()
print('(B) THE CUT  L = {(x,x)} in the opposed fusion V (+) (-V)')
rng=np.random.default_rng(20261107)
for k,V in knots.items():
    n=V.shape[0]; par=bsum(V,V); opp=bsum(V,-V)
    L=np.vstack([np.eye(n),np.eye(n)])/np.sqrt(2)            # orthonormal basis of the diagonal half
    iso_opp=0; iso_par=0; angs=[]
    for a in np.linspace(0.02,np.pi-0.02,200):
        w=np.exp(1j*a)
        iso_opp=max(iso_opp,np.max(np.abs(L.conj().T@H(opp,w)@L)))
        iso_par=max(iso_par,np.max(np.abs(L.conj().T@H(par,w)@L)))
        e,U=np.linalg.eigh(H(opp,w))
        if np.min(np.abs(e))<1e-9: continue
        Q=U[:,e>0]
        s=np.linalg.svd(Q.conj().T@L,compute_uv=False)
        angs.append(np.degrees(np.arccos(np.clip(s,0,1))))
    angs=np.array(angs)
    print(f'  {k}: max |H restricted to L|  opposed {iso_opp:.1e}  parallel {iso_par:.2f}  | principal angles P+(w) vs L: min {angs.min():.4f} deg, max {angs.max():.4f} deg')

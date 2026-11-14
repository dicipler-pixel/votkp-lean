# SCRIPT: LOOP2-CHECK3-EXIT-LINE-VS-LOOP
# WHY THIS DECIDES IT: any traceless 2x2 matrix is n.sigma, n complex; two such matrices are similar (up to scaling s) iff
# n.n agree up to s^2; the Petermann factor is a similarity invariant of the eigenvector pair. So: compute c with log(-W) = c.sigma
# (-W acts identically to W on directions: same Mobius map, same eigenvectors, so same K), split c = a + i b, test a.b = 0
# (equivalent to Im(c.c)=0), rotate so that b is along z, a in the xy plane => the form h(k) = (x,y,i u). Choose the scale s in {1, i}
# so that |a|>|b| (the regime in which E^2=|v+we^{ik}|^2-u^2>0 and the quoted K=1+u^2/E^2 is valid). Then compare
# K_h = 1+u^2/E^2 with K_W computed independently from the biorthogonal eigenvectors of W (K = |L|^2|R|^2/|<L|R>|^2).
# Predictions written BEFORE the run:
#   inside the wall (Gamma^2<1/2): s=i; E = E' = 2 arccos(Gamma^2/(1-Gamma^2)); u = E' sinh(eta), |v+we^{ik}| = E' cosh(eta), cosh^2(eta)=1/(1-2Gamma^2);
#       K_h = cosh^2 eta = K_W = 1/(1-2 Gamma^2); K=2 <-> Gamma^2=1/4 <-> u=E.
#   past the wall: K_W (true, biorthogonal) = 2Gamma^2/(2Gamma^2-1) = 1 - 1/(1-2Gamma^2) (NOT the continued 1/(1-2Gamma^2), which is negative there).
# KILL LINES: (1) a.b != 0 at any z (residual>1e-40) -> no real-rotation form, map killed;
#   (2) K_h != K_W (rel residual > 1e-40) at any z where a map is claimed -> map killed;
#   (3) the closed forms above off by more than 1e-40 -> those closed forms killed.
import mpmath as mp
mp.mp.dps=60
sig=[mp.matrix([[0,1],[1,0]]),mp.matrix([[0,-1j],[1j,0]]),mp.matrix([[1,0],[0,-1]])]
def W_of(z):
    r=mp.log(mp.mpf(z)); c,s=mp.cosh(r/2),mp.sinh(r/2)
    Bx=mp.matrix([[c,s],[s,c]]); By=mp.matrix([[c,-1j*s],[1j*s,c]]); Bxi=mp.matrix([[c,-s],[-s,c]]); Byi=mp.matrix([[c,1j*s],[-1j*s,c]])
    return Bx*By*Bxi*Byi
def Ktrue(W):
    E,V=mp.eig(W); VL=mp.inverse(V).H   # columns = left eigenvectors (biorthogonal)
    out=[]
    for i in range(2):
        r=V[:,i]; l=VL[:,i]
        nr=sum(abs(x)**2 for x in r); nl=sum(abs(x)**2 for x in l); ov=abs(sum(l[j].conjugate()*r[j] for j in range(2)))**2
        out.append(nr*nl/ov)
    return out
print('z, regime, a.b, |a|,|b|, scale, E, u, A=|v+we^ik|, K_h, K_W, resid_K, resid_closedforms')
rows=[]
for z in ['1.5','2','3','4','5','5.5','5.8','5.99','5.9','6.5','8','16.8177','206.768']:
    W=W_of(z); G2=mp.tanh(mp.log(mp.mpf(z))/2)**2; M=-W
    E,V=mp.eig(M); L=V*mp.diag([mp.log(E[0]),mp.log(E[1])])*mp.inverse(V)
    tr=L[0,0]+L[1,1]
    c=[ (L*sg)[0,0]+(L*sg)[1,1] for sg in sig]; c=[x/2 for x in c]   # tr(L sigma_j)/2
    a=[x.real for x in c]; b=[x.imag for x in c]
    ab=sum(x*y for x,y in zip(a,b)); na=mp.sqrt(sum(x*x for x in a)); nb=mp.sqrt(sum(y*y for y in b))
    s='i' if na<nb else '1'
    A,u=(nb,na) if s=='i' else (na,nb)           # multiplying by i swaps real and imaginary parts (up to sign)
    Ee=mp.sqrt(A*A-u*u); Kh=1+u*u/Ee**2
    KW=Ktrue(W)[0]
    cf_resid=None
    if G2<0.5:
        Ep=2*mp.acos(G2/(1-G2)); ch=1/mp.sqrt(1-2*G2); sh=mp.sqrt(ch*ch-1)
        cf_resid=max(abs(Ee-Ep),abs(u-Ep*sh),abs(A-Ep*ch),abs(Kh-1/(1-2*G2)),abs(KW-1/(1-2*G2)))
    else:
        lam=4*mp.acosh(G2/(1-G2)); Kp=2*G2/(2*G2-1)
        cf_resid=max(abs(2*Ee-lam/1*0.5*2) if False else abs(Ee-lam/2),abs(KW-Kp))
    rows.append((z,mp.nstr(ab,3),mp.nstr(na,8),mp.nstr(nb,8),s,mp.nstr(Ee,10),mp.nstr(u,10),mp.nstr(A,10),mp.nstr(Kh,12),mp.nstr(KW,12),mp.nstr(abs(Kh-KW)/KW,3),mp.nstr(cf_resid,3)))
    print(' | '.join(rows[-1]))

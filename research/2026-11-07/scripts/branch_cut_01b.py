# SCRIPT: BRANCH-CUT-01b
# Same construction as BRANCH-CUT-01; reads the projector metric for both spectral halves, skipping phases where a half is empty.
import numpy as np
def seifert_T2(n):
    m=n-1; V=np.zeros((m,m))
    for i in range(m): V[i,i]=-1
    for i in range(m-1): V[i+1,i]=1
    return V
knots={'3_1':seifert_T2(3),'5_1':seifert_T2(5),'7_1':seifert_T2(7),'4_1':np.array([[-1.,1.],[0.,1.]])}
def H(V,w): return (1-w)*V+(1-np.conj(w))*V.T
def bsum(A,B):
    n,m=A.shape[0],B.shape[0]; C=np.zeros((n+m,n+m)); C[:n,:n]=A; C[n:,n:]=B; return C
def proj(M,sgn):
    e,U=np.linalg.eigh(M); Q=U[:,sgn*e>1e-9]; return Q@Q.conj().T, Q.shape[1]
def speed(V,a,sgn,h=1e-5):
    P1,r1=proj(H(V,np.exp(1j*(a-h))),sgn); P2,r2=proj(H(V,np.exp(1j*(a+h))),sgn)
    if r1!=r2 or r1==0: return np.nan
    dP=(P2-P1)/(2*h); return 0.5*np.real(np.trace(dP@dP))
grid=np.linspace(0.05,np.pi-0.05,60)
for k,V in knots.items():
    par=bsum(V,V); opp=bsum(V,-V.T)
    out=[]
    for a in grid:
        gk=speed(V,a,1)+speed(V,a,-1) if not np.isnan(speed(V,a,1)+speed(V,a,-1)) else np.nan
        gkp=np.nansum([speed(V,a,1),speed(V,a,-1)])
        gpp=np.nansum([speed(par,a,1),speed(par,a,-1)])
        gop=np.nansum([speed(opp,a,1),speed(opp,a,-1)])
        if gkp>1e-12: out.append((gpp/gkp,gop/gkp))
    out=np.array(out)
    print(k,' phases read',len(out),' parallel/K speed: median',round(float(np.median(out[:,0])),6),
          ' opposed/K speed: median',round(float(np.median(out[:,1])),6),' max spread',round(float(np.ptp(out)),6))

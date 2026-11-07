# SCRIPT: BRANCH-CUT-01
# Exploratory (not a pass/kill test). Fusion of two knots = connected sum = block sum of Seifert matrices.
# Parallel fusion: K # K.  Opposed fusion: K # mirror(K), mirror Seifert matrix = -V^T.
# Levine-Tristram form H(w) = (1-w)V + (1-conj w)V^T on the unit circle.
# Reads: even records (Alexander, determinant, projector metric) and odd records (signature, +/- spectral pairing).
import numpy as np, sympy as sp
t=sp.symbols('t')
def seifert_T2(n):            # T(2,n), n odd: genus (n-1)/2, size n-1
    m=n-1; V=np.zeros((m,m)); 
    for i in range(m): V[i,i]=-1
    for i in range(m-1): V[i+1,i]=1
    return V
knots={'3_1':seifert_T2(3),'5_1':seifert_T2(5),'7_1':seifert_T2(7),'4_1':np.array([[-1.,1.],[0.,1.]])}
def alex(V):
    M=sp.Matrix(V.astype(int))
    p=sp.expand((M-t*M.T).det()); return sp.factor(p)
def H(V,w): return (1-w)*V+(1-np.conj(w))*V.T
def bsum(A,B):
    n,m=A.shape[0],B.shape[0]; C=np.zeros((n+m,n+m)); C[:n,:n]=A; C[n:,n:]=B; return C
def sig(M): 
    e=np.linalg.eigvalsh(M); return int(np.sum(e>1e-9)-np.sum(e<-1e-9)), e
def proj_pos(M):
    e,U=np.linalg.eigh(M); Q=U[:,e>1e-9]; return Q@Q.conj().T
def metric_speed(V,a,h=1e-5):
    P1=proj_pos(H(V,np.exp(1j*(a-h)))); P2=proj_pos(H(V,np.exp(1j*(a+h))))
    dP=(P2-P1)/(2*h); return 0.5*np.real(np.trace(dP@dP))
grid=np.linspace(0.01,np.pi-0.01,400)   # phase of w = e^{i a}, upper half circle
print('Seifert check: Alexander polynomials')
for k,V in knots.items(): print(' ',k, alex(V))
for k,V in knots.items():
    Vm=-V.T; par=bsum(V,V); opp=bsum(V,Vm)
    A_par,A_opp=alex(par),alex(opp)
    same_alex=sp.simplify(A_par-A_opp)==0 or sp.simplify(A_par+A_opp)==0
    det_par=abs(int(sp.Matrix((par).astype(int)).__add__(sp.Matrix(par.T.astype(int))).det()))
    det_opp=abs(int(sp.Matrix((opp).astype(int)).__add__(sp.Matrix(opp.T.astype(int))).det()))
    sK=[];sP=[];sO=[];pair=0.0;gK=[];gP=[];gO=[]
    for a in grid:
        w=np.exp(1j*a)
        s1,_=sig(H(V,w)); s2,_=sig(H(par,w)); s3,e3=sig(H(opp,w))
        sK.append(s1);sP.append(s2);sO.append(s3)
        es=np.sort(e3); pair=max(pair,np.max(np.abs(es+es[::-1])))
    for a in grid[5:-5:20]:
        gK.append(metric_speed(V,a)); gP.append(metric_speed(par,a)); gO.append(metric_speed(opp,a))
    sK,sP,sO=map(np.array,(sK,sP,sO)); gK,gP,gO=map(np.array,(gK,gP,gO))
    print('\n==',k,' size',V.shape[0])
    print('  even: Alexander equal (up to sign):',same_alex,' |  det parallel',det_par,' det opposed',det_opp)
    print('  odd : signature range K',sK.min(),sK.max(),' | parallel = 2*K at every phase:',bool(np.all(sP==2*sK)),
          ' | opposed range',sO.min(),sO.max())
    print('  opposed spectrum pairs as +/-lambda: max |l_i + l_(n-i)| =',f'{pair:.2e}')
    print('  projector metric speed: parallel/K =',np.round(np.median(gP/np.where(gK>1e-12,gK,np.nan)),6),
          ' opposed/K =',np.round(np.median(gO/np.where(gK>1e-12,gK,np.nan)),6), ' (K speed nonzero at',int(np.sum(gK>1e-12)),'of',len(gK),'sample phases)')

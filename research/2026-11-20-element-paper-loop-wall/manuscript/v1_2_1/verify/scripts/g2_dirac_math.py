# SCRIPT: G2_DIRAC_MATH (numeric checks of equations stated in 04_dirac_time.md)
import numpy as np
rng=np.random.default_rng(1)
def herm(n):
    A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); return (A+A.conj().T)/2
# (a) g_tt = Tr(P H (I-P) H P) = 1/2 Tr(Pdot^2), Pdot=-i[H,P] (hbar=1), rank-2 projector in dim 5
n=5;H=herm(n);M=rng.normal(size=(n,2))+1j*rng.normal(size=(n,2));Q,_=np.linalg.qr(M);P=Q@Q.conj().T
Pd=-1j*(H@P-P@H);lhs=0.5*np.trace(Pd@Pd).real
rhs=np.trace(P@H@(np.eye(n)-P)@H@P).real
print('g_tt identity rank2: ',lhs,rhs,abs(lhs-rhs))
# rank-1: QFI=4 Var(H)=4 g_tt
v=rng.normal(size=n)+1j*rng.normal(size=n);v/=np.linalg.norm(v);P1=np.outer(v,v.conj())
Pd=-1j*(H@P1-P1@H);g=0.5*np.trace(Pd@Pd).real
var=(v.conj()@H@H@v).real-((v.conj()@H@v).real)**2
print('F_Q=4 g_tt (rank1):',4*g,4*var)
# (b) Sec 11.4 witness: |c0|^2-|c1|^2 = sin(2gt) sin Phi ; population dev from 1/2 = (1/2) sin(2gt) sin Phi
g_=0.7;t=0.9;Phi=1.1
V=g_*np.array([[0,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,0]],dtype=complex)
from scipy.linalg import expm
psi=np.zeros(4,complex);psi[1]=1/np.sqrt(2);psi[2]=np.exp(1j*Phi)/np.sqrt(2)
out=expm(-1j*V*t)@psi
p01=abs(out[1])**2;p10=abs(out[2])**2
print('p01-p10',p01-p10,'sin2gt sinPhi',np.sin(2*g_*t)*np.sin(Phi),' p01-1/2',p01-0.5,' half form',0.5*np.sin(2*g_*t)*np.sin(Phi))
# (c) Sec 14: (1/8)||[H,H^dag]||_F^2 = sum_edges ||D_i - A_ij D_j A_ij^dag||^2, 3 nodes path graph 0-1-2, 2x2 blocks
def rand_u(k):
    X=rng.normal(size=(k,k))+1j*rng.normal(size=(k,k));q,_=np.linalg.qr(X);return q
k=2;Ds=[herm(k) for _ in range(3)];U01=rand_u(k);U12=rand_u(k)
N=3*k;D=np.zeros((N,N),complex);A=np.zeros((N,N),complex)
for i in range(3):D[i*k:(i+1)*k,i*k:(i+1)*k]=Ds[i]
# anti-Hermitian A: block (i,j)=U_ij, block (j,i)=-U_ij^dag
A[0:k,k:2*k]=U01;A[k:2*k,0:k]=-U01.conj().T;A[k:2*k,2*k:3*k]=U12;A[2*k:3*k,k:2*k]=-U12.conj().T
Hm=D+A;com=Hm@Hm.conj().T-Hm.conj().T@Hm
left=np.linalg.norm(com,'fro')**2/8
# A_ij = U_ij (block (i,j)); formula uses A_ij D_j A_ij^dag
right=np.linalg.norm(Ds[0]-U01@Ds[1]@U01.conj().T)**2+np.linalg.norm(Ds[1]-U12@Ds[2]@U12.conj().T)**2
print('connection energy: ',left,right)
print('[H,H^dag] = -2[D,A]:',np.linalg.norm(com-(-2)*(D@A-A@D)))
# (d) Sec 16: |d'|^2 = rho'^2 + Delta^2 g, g=1/2 Tr(Pdot^2)=|n'|^2/4, rho^2 chi'^2 <= Delta^2 g
worst=0;viol=0
for _ in range(2000):
    d=rng.normal(size=3);dd=rng.normal(size=3);rho=np.linalg.norm(d);nn=d/rho
    rhod=nn@dd;nd=(dd-rhod*nn)/rho;gss=np.linalg.norm(nd)**2/4;Delta=2*rho
    worst=max(worst,abs(dd@dd-(rhod**2+Delta**2*gss)))
    chid=nd[2]
    if rho**2*chid**2>Delta**2*gss+1e-12:viol+=1
print('two-level identity worst',worst,'bound violations',viol)
# (e) Sec 5: positive projector; eigenvalues 2pi sqrt(a^2+b^2)
a,b=0.3,-0.45;s1=np.array([[0,1],[1,0]]);s2=np.array([[0,-1j],[1j,0]])
Dm=2*np.pi*(a*s1+b*s2);w,V=np.linalg.eigh(Dm);phi=np.arctan2(b,a)
Pp=(np.eye(2)+np.cos(phi)*s1+np.sin(phi)*s2)/2;proj=np.outer(V[:,1],V[:,1].conj())
print('eig',w,2*np.pi*np.hypot(a,b),'P+ err',np.linalg.norm(Pp-proj))
# (f) Sec 8: circle odometer eta = 1-2{a}: sum over k of sign(k+a) regularized: eta(s)=sum sgn(k+a)|k+a|^-s at s->0 ; check via Hurwitz zeta
import mpmath as mp
for a in (0.3,0.75):
    eta=mp.zeta(0,a)-mp.zeta(0,1-a)
    print('eta(a=%g) = %s vs 1-2a = %s'%(a,mp.nstr(eta,8),1-2*a))
# (g) Sec 12: telescoping memory term (eps_h-eps_c)*eta*(1-eta)^n*dp : sum_n finite = (eps_h-eps_c)*dp
eh,ec,ph,pc,et=3,1,0.4,0.2,0.25
def run(pm0,N=40):
    pm=pm0;W=[]
    for n in range(N):
        ps=(1-et)*ph+et*pm;W.append((eh-ec)*(ps-pc));pm=(1-et)*pm+et*ph
    return np.array(W)
Wa=run(0.3);Wb=run(0.1)
for n in (0,1,5):
    print('engine diff n=%d'%n,Wa[n]-Wb[n],(eh-ec)*et*(1-et)**n*(0.3-0.1)) if False else None
# engine: p*=(1-eta)ph+eta pm ; pm'=(1-eta)pm+eta ph. The stated recursion (primary 12.1) gives difference below
pa,pb=0.3,0.1
for n in range(4):
    d_=(eh-ec)*(et*(pa-pb));print('n',n,'diff',(Wa[n]-Wb[n]),'formula (eh-ec)*eta*(1-eta)^n*dpm0',(eh-ec)*et*(1-et)**n*(pa-pb))

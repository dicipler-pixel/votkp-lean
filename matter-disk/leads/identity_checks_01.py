# SCRIPT: LEADS_IDENTITY_CHECKS_01
import numpy as np
rng=np.random.default_rng(1)
sx=np.array([[0,1],[1,0]],complex);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]).astype(complex)
S=[sx,sy,sz]
def sig(d): return sum(d[i]*S[i] for i in range(3))
def riesz(d):
    E=np.sqrt(np.sum(d*d)+0j)
    n=d/E
    Pp=(np.eye(2)+sig(n))/2; Pm=(np.eye(2)-sig(n))/2
    return E,n,Pp,Pm
# ---- I1: real-E d = a+ib, a perp b, |a|>|b|
worst=[0]*5
for _ in range(2000):
    a=rng.normal(size=3); b=rng.normal(size=3); b-= a*(a@b)/(a@a); b*=rng.uniform(0.05,0.95)*np.linalg.norm(a)/np.linalg.norm(b)
    d=a+1j*b
    E,n,Pp,Pm=riesz(d)
    K=np.linalg.norm(Pp)**2   # Frobenius^2 of Riesz projector
    K1=0.5*(1+np.sum(abs(d)**2)/abs(E)**2)
    H=sig(d); Hh=(H+H.conj().T)/2; Hs=(H-H.conj().T)/2
    rho2=np.linalg.norm(Hs)**2/np.linalg.norm(Hh)**2
    K2=1/(1-rho2)
    # eigenvectors angle
    w,V=np.linalg.eig(H); r1=V[:,0]/np.linalg.norm(V[:,0]); r2=V[:,1]/np.linalg.norm(V[:,1])
    cphi=abs(np.vdot(r1,r2)); K3=1/(1-cphi**2)
    # self commutator
    comm=Pp@Pp.conj().T-Pp.conj().T@Pp
    N=np.linalg.norm(comm)**2
    worst[0]=max(worst[0],abs(K-K1),abs(K-K2),abs(K-K3)); worst[1]=max(worst[1],abs(rho2-cphi**2)); worst[2]=max(worst[2],abs(N-2*K*(K-1)))
    # H self-commutator energy 32|a|^2|b|^2
    worst[3]=max(worst[3],abs(np.linalg.norm(H@H.conj().T-H.conj().T@H)**2-32*(a@a)*(b@b)))
    # q(T)
    q=0.5*np.trace(H@H).real; worst[4]=max(worst[4],abs(q-(a@a-b@b)*2/2*1))
print('I1 K three forms',worst[0],' rho2=cos2phi',worst[1],' |[Pi,Pi*]|^2=2K(K-1)',worst[2],' |[H,H*]|^2=32|a|^2|b|^2',worst[3],' q(T)=|a|^2-|b|^2',worst[4])
# ---- I2: rails edge (lam+,lam-) , D=1, T>2
for T in [2.2,2*np.sqrt(2),4,34]:
    lp=(T+np.sqrt(T*T-4))/2; lm=1/lp
    Em=(lp-lm)**2; Ep=(lp+lm)**2
    psi=np.arccos(2/T)
    M=np.array([[T,-1],[1,0]]); w,V=np.linalg.eig(M)
    r1=V[:,0]/np.linalg.norm(V[:,0]); r2=V[:,1]/np.linalg.norm(V[:,1]); K=1/(1-abs(np.vdot(r1,r2))**2)
    print('T',T,'E-=T^2-4:',Em-(T*T-4),'E+=T^2:',Ep-T*T,'K-E+/E-:',K-Ep/Em,'K-1/sin^2psi:',K-1/np.sin(psi)**2,'E-/E+ - sin^2psi:',Em/Ep-np.sin(psi)**2,
          'Gamma(lam+) - tan(psi/2):',(lp-1)/(lp+1)-np.tan(psi/2),'tanh(log lp)-sin psi',np.tanh(np.log(lp))-np.sin(psi))
# ---- I4/I5: constants
rc=np.arccosh(3); print('r_c',rc,'2ln(1+sqrt2)',2*np.log(1+np.sqrt(2)),'Apery rate',np.log(17+12*np.sqrt(2)),'2 r_c',2*rc,'pi+e rate',np.log(1+np.sqrt(2)),'r_c/2',rc/2)
print('cosh 2rc',np.cosh(2*rc),'sinh 2rc',np.sinh(2*rc),12*np.sqrt(2))
# Gamma^2=1/2 faces
G=1/np.sqrt(2); nu=(1-G)/2; print('nu',nu,'sin^2(pi/8)',np.sin(np.pi/8)**2,'lambda',nu*(1-nu),'cosh tau',np.cosh(2*np.arctanh(G)),'z',(1-nu)/nu,3+2*np.sqrt(2),'cos psi at z=3+2r2: sech(ln z)',1/np.cosh(np.log(3+2*np.sqrt(2))))
# ---- I6 Thomas
for z in [5,7,3+2*np.sqrt(2)]:
    Gm=(z-1)/(z+1); th=np.arctan2((z*z-1)**2,4*z*(z*z+1)); print('z',z,'tan(th/2)',np.tan(th/2),'Gamma^2',Gm**2,'E-/E+',((z-1)**2)/((z+1)**2))
# ---- I7 Mercator / offset speed limit on Bloch sphere
def tau_of(nz): return 2*np.arctanh(-nz)  # Gamma=1-2c, c=(1+nz)/2 => Gamma=-nz ; tau=log((1-c)/c)
worst=0; viol=0
for _ in range(2000):
    th=rng.uniform(0.2,np.pi-0.2); ph=rng.uniform(0,6.28); thd=rng.normal(); phd=rng.normal()
    # P=(1+n.sigma)/2
    def n(th,ph): return np.array([np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph),np.cos(th)])
    h=1e-6
    P=lambda th,ph:(np.eye(2)+sig(n(th,ph)))/2
    Pd=(P(th+h*thd,ph+h*phd)-P(th-h*thd,ph-h*phd))/(2*h)
    g=0.5*np.linalg.norm(Pd)**2
    c=P(th,ph)[0,0].real; Sv=1/(c*(1-c))
    taud=(tau_of(n(th+h*thd,ph+h*phd)[2])-tau_of(n(th-h*thd,ph-h*phd)[2]))/(2*h)
    gap=4*g*Sv-taud**2
    worst=min(worst,gap/(4*g*Sv)); 
    pred=4*(np.sin(th)**2*phd**2)*Sv/4  # 4gS - taud^2 = S*sin^2 th * phd^2 ... check below
    worst=worst
    gm=0.25*(thd**2+np.sin(th)**2*phd**2)
    assert abs(g-gm)<1e-6*(1+g)
    assert abs(gap-Sv*np.sin(th)**2*phd**2)<1e-5*(1+abs(gap)), (gap,Sv*np.sin(th)**2*phd**2)
print('I7 min (4gS-taud^2)/(4gS)=',worst,' identity 4gS-taud^2 = S sin^2(th) phid^2 holds')
# saturating trajectory m=1
Om=2*np.pi*1e3; t=np.linspace(0,1e-4,5)
tau=2*np.arctanh(np.sin(2*Om*t[:-1])); gd_inv=lambda x: np.arcsinh(np.tan(x))
print('tau vs 2 gd^-1(2 Om t):',np.max(abs(tau-2*gd_inv(2*Om*t[:-1]))))
# ---- I8 cone
def Pi_of(k,gam=0.6,m=0.4):
    d=np.array([k[0],k[1],m+1j*gam]); return riesz(d)
k0=np.array([1.6,1.2]); 
E,n,Pp,Pm=Pi_of(k0); d0=np.array([k0[0],k0[1],0.4+0.6j])
for th in [0.0,0.65,1.2,2.4]:
    u=np.array([np.cos(th),np.sin(th)]); V=np.cos(th)*sx+np.sin(th)*sy
    # Pi' by finite difference
    h=1e-6
    Pd=(Pi_of(k0+h*u)[2]-Pi_of(k0-h*u)[2])/(2*h)
    Q=np.trace(Pp@V@Pm@V)/(2*E)**2
    Q2=(np.dot([np.cos(th),np.sin(th),0],[np.cos(th),np.sin(th),0])-(n[:2]@u)**2)/(2*(2*E)**2)*1  # candidate
    Q3=0.5*np.trace(Pd@Pd)
    cdel=0.01; C=np.trace(Pp@Pi_of(k0+cdel*u)[2]); 
    print('theta',th,'Q',Q,'1/2 Tr Pi\'^2',Q3,'formula (1-(n.v)^2)/(8E^2)',(1-(n[:2]@u)**2)/(8*E*E),'ReC',C.real,'1-ReQ d^2',1-Q.real*cdel**2,'|Q|<=K/|dE|^2',abs(Q)<=np.linalg.norm(Pp)**2/abs(2*E)**2)
# ---- I10 opened SSH
for (v,w,u) in [(0.5,1,0.3),(0.4,1,0.2),(1,1.5,0.6)]:
    E0=np.sqrt((v+w)**2-u*u); Ep_=np.sqrt(abs((v-w)**2-u*u)+0j)
    ks=np.linspace(0,2*np.pi,200001)[:-1]; q=v+w*np.exp(1j*ks); Kk=abs(q)**2/(abs(q)**2-u*u)
    K0=1+u*u/E0**2; Kpi=1+u*u/abs(Ep_)**2
    print('SSH',v,w,u,'<K>',Kk.mean(),'1+u^2/(E0 Epi)',1+u*u/(E0*abs(Ep_)),'1+1/sqrt((K0-1)(Kpi-1))',1+1/np.sqrt((K0-1)*(Kpi-1)),'utilde^2 cont',((w-v)**2-u*u)/((w+v)**2-u*u),'Epi^2/E0^2',abs(Ep_)**2/E0**2)
# exit line example u=0.5 find v with E0 Epi = u^2 (w=1)
from scipy.optimize import brentq
u=0.5;w=1.0
f=lambda v: np.sqrt((v+w)**2-u*u)*np.sqrt((w-v)**2-u*u)-u*u
vx=brentq(f,0.01,0.49); E0=np.sqrt((vx+w)**2-u*u); Ep_=np.sqrt((w-vx)**2-u*u)
print('exit v',vx,'utilde',Ep_/E0,'K0-1',u*u/E0**2,'1/(Kpi-1)',Ep_**2/u**2,' <K>',1+u*u/(E0*Ep_))
# ---- I11 Koide
me,mm,mt=0.51099895069,105.6583755,1776.93
Q=(me+mm+mt)/(np.sqrt(me)+np.sqrt(mm)+np.sqrt(mt))**2; z2=3*Q-1
print('Q',Q,'zeta^2',z2,'K_lepton=max(z2,1)/|z2-1|',max(z2,1)/abs(z2-1))
x=np.sqrt([me,mm,mt]); s=x.sum()/np.sqrt(3); h1=(x[0]-x[1])/np.sqrt(2); h2=(x[0]+x[1]-2*x[2])/np.sqrt(6)
Z=h1*sz+h2*sx+s*np.array([[0,1],[-1,0]]); Ev=np.linalg.eigvals(Z); 
# Petermann of Z via eigenvectors
w_,V_=np.linalg.eig(Z); r1=V_[:,0]/np.linalg.norm(V_[:,0]); r2=V_[:,1]/np.linalg.norm(V_[:,1]); print('eig',w_,'K via eigvec',1/(1-abs(np.vdot(r1,r2))**2))
# ---- I13 census edge
for nu in [0.1,0.3,0.45]:
    di,dj=1-nu,nu; print('nu',nu,'E-',(di-dj)**2,'Gamma^2',(1-2*nu)**2,'E+-E-',(di+dj)**2-(di-dj)**2,'4 lambda',4*nu*(1-nu),'S=1/lam',1/(nu*(1-nu)),'4cosh^2(tau/2)',4*np.cosh(np.log((1-nu)/nu)/2)**2)
# ---- I14 passivity
for _ in range(3):
    z=rng.normal()+1j*rng.normal(); G=(z-1)/(z+1); print('1-|G|^2',1-abs(G)**2,'4Re z/|1+z|^2',4*z.real/abs(1+z)**2)

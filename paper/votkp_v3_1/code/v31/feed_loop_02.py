# SCRIPT: FEED-LOOP-02
# WHY THIS DECIDES IT: the loop W(z) is a 2x2 matrix; its two eigen-directions are two points on the rim.
# The line joining them inside the ball is the set the loop leaves fixed. Its nearest point to the centre,
# the angle between the eigen-directions, and the turn angle are all read from W itself, exactly.
# FEED-LOOP-01 picked the fixed point by a coarse search; here it is computed in closed form.
# KILL LINES (before the run):
#  K1  Petermann factor K = 1/(1-2 Gamma^2) for every step ratio inside the wall: rel. residual > 1e-9 -> kill
#  K2  centre-of-turn radius rho^2 = (1-s)/(1+s), s = sqrt(1-2 Gamma^2): residual > 1e-9 -> kill
#  K3  rho^2 = 1/2 exactly at z = 5 and nowhere else inside the wall (rho monotone in z): else kill
#  K4  W = S U S^-1 with S the positive step from the centre to that point, U unitary: residual > 1e-9 -> kill
#  K5  light fed by the loop equals [1 + sin(n theta) sin(phi)]/2 for every prepared arm: residual > 1e-9 -> kill
#  K6  lab-frame signal: Gamma_lab(n) is the own-frame Gamma moved by the fixed step (Mobius), residual > 1e-9 -> kill
import numpy as np, json
from scipy.linalg import expm
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
SIG=[sx,sy,sz]; I2=np.eye(2); ZW=3+2*np.sqrt(2)
B=lambda a,r: expm(0.5*r*SIG[a])
loop=lambda r: B(0,r)@B(1,r)@B(0,-r)@B(1,-r)
def bloch(psi): psi=psi/np.linalg.norm(psi); return np.array([np.real(psi.conj()@s@psi) for s in SIG])
def proj(v): v=np.array(v,float); v=v/np.linalg.norm(v); return 0.5*(I2+sum(v[i]*SIG[i] for i in range(3)))
def state(v): w,V=np.linalg.eigh(proj(v)); return V[:,1]
def anatomy(z):
    r=np.log(z); G=np.tanh(r/2); W=loop(r); w,V=np.linalg.eig(W)
    e1,e2=bloch(V[:,0]),bloch(V[:,1]); ca=float(np.dot(e1,e2)); alpha=np.arccos(np.clip(ca,-1,1))
    K=1/(1-abs(np.vdot(V[:,0]/np.linalg.norm(V[:,0]),V[:,1]/np.linalg.norm(V[:,1])))**2)
    d=(e1+e2); d=d/np.linalg.norm(d); rho=(1-np.sin(alpha/2))/np.cos(alpha/2)
    eta=2*np.arctanh(rho); S=expm(0.5*eta*sum(d[i]*SIG[i] for i in range(3)))
    U=np.linalg.inv(S)@W@S; th=2*np.arccos(np.clip(1-2*np.sinh(r/2)**4,-1,1))
    ax=-np.array([np.trace(U@s).imag for s in SIG]); ax=ax/np.linalg.norm(ax)
    return dict(z=z,G=G,W=W,K=K,rho=rho,d=d,eta=eta,S=S,U=U,theta=th,axis=ax,alpha=alpha)
out={}; k1=k2=k4=0; rhos=[]; zs=np.linspace(1.02,ZW-1e-3,600)
for z in zs:
    a=anatomy(z); s=np.sqrt(1-2*a['G']**2)
    k1=max(k1,abs(a['K']*(1-2*a['G']**2)-1)); k2=max(k2,abs(a['rho']**2-(1-s)/(1+s)))
    k4=max(k4,np.linalg.norm(a['U'].conj().T@a['U']-I2)); rhos.append(a['rho'])
    # direction of the centre of turn and the axis
out['K1_Petermann_rel_residual']=k1; out['K2_radius_residual']=k2; out['K4_unitary_residual']=k4
out['K3_rho_monotone']=bool(np.all(np.diff(rhos)>0))
a5=anatomy(5.0)
out['K3_at_z5']={'rho^2':a5['rho']**2,'rho^2-1/2':a5['rho']**2-0.5,'K':a5['K'],'cosh_eta_fixed':float(np.cosh(a5['eta'])),
   'centre_direction':a5['d'].round(12).tolist(),'turn_axis':a5['axis'].round(12).tolist(),'theta_over_2pi':a5['theta']/(2*np.pi),'theta_rad':a5['theta']}
tab=[]
for z in [1.5,2,3,4,5,5.5,5.8]:
    a=anatomy(z); tab.append(dict(z=z,Gamma2=a['G']**2,K=a['K'],rho=a['rho'],cosh_eta=float(np.cosh(a['eta'])),turn_over_2pi=a['theta']/(2*np.pi),
        dir=a['d'].round(6).tolist(),axis=a['axis'].round(6).tolist()))
out['table']=tab
# where K = 2
out['K=2_at']={'Gamma2':0.25,'z':3.0,'K_at_z3':anatomy(3.0)['K']}
# ---- K5 light fed by the loop, z = 5
def feed(z,prep,N=40):
    a=anatomy(z); Si=np.linalg.inv(a['S']); psi=Si@state(prep); s0=bloch(psi); ax=a['axis']
    phi=np.arccos(np.clip(np.dot(s0,ax),-1,1)); q=np.cross(ax,s0); nq=np.linalg.norm(q)
    if nq<1e-10: return dict(prep=prep,sin2phi=0.0,res=0.0,note='on the axis')
    q/=nq; Q=proj(q); res=0; res6=0; Ut=I2; Wt=I2; Qlab=None
    for n in range(N):
        ps=Ut@psi; ps/=np.linalg.norm(ps); c=np.real(ps.conj()@Q@ps); Gown=1-2*c
        res=max(res,abs(c-(1+np.sin(n*a['theta'])*np.sin(phi))/2))
        # K6: lab state W^n psi_lab has Bloch vector = own-frame Bloch vector carried by S (Mobius on the rim)
        lab=Wt@state(prep); lab/=np.linalg.norm(lab); viaS=a['S']@ps; viaS/=np.linalg.norm(viaS)
        res6=max(res6,1-abs(np.vdot(lab,viaS)))
        Ut=a['U']@Ut; Wt=a['W']@Wt
    return dict(prep=prep,phi_over_pi=phi/np.pi,sin2phi=np.sin(phi)**2,kappa=a['theta']/2,g=(a['theta']/2)**2*np.sin(phi)**2,res=res,res6=res6,
                reaches_half_line=bool(np.sin(phi)**2>=0.5))
rows=[feed(5.0,p) for p in ([1,0,0],[0,1,0],[0,0,1],[0,0,-1],[1,1,1],[1,1,0],[-1,-1,0])]
out['K5_rows']=rows; out['K5_residual']=max(r['res'] for r in rows); out['K6_residual']=max(r.get('res6',0) for r in rows)
# closed forms to test for the arm angles at z=5
out['candidates']={'8/9':8/9,'1/9':1/9,'1/3':1/3,'2/3':2/3}
print(json.dumps(out,indent=1,default=float)); open('feed_loop_02.out','w').write(json.dumps(out,indent=1,default=float))

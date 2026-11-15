# SCRIPT: FEED-LOOP-01
# WHY THIS DECIDES IT: every statement below is an identity between 2x2 matrices built from
# the tree's own step (a positive Hermitian step of ratio z along an arm). If the identity
# is false the residual is order 1, not order 1e-12. Nothing is fitted.
# KILL LINES (written before the run):
#  A  light on the peel disk: |Gamma-(1-2c)|, speed bound violated, or half-line reach wrong  -> kill if > 1e-12 / any violation
#  B  loop trace: |tr W - (2-4 sinh^4(r/2))| > 1e-10 -> kill
#  C  inside the wall W = S U S^-1 with S positive Hermitian, U unitary: residual > 1e-9 -> kill
#  D  at the wall: (W+1)^2 = 0 and W+1 != 0 (one Jordan block): else kill
#  E  light fed by the tree: occupation from U^n equals [1+sin(n theta) sin(phi)]/2 form: residual > 1e-10 -> kill
#  F  one ball, three readings: Klein radius = p (+) p, particle radius^2 = Gamma(E/m), E = 3m on the red sphere: residual > 1e-12 -> kill
import numpy as np, json
from scipy.linalg import expm, sqrtm, logm
np.set_printoptions(precision=6, suppress=True)
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.array([[1,0],[0,-1]],complex)
SIG=[sx,sy,sz]; I2=np.eye(2)
def B(a,r): return expm(0.5*r*SIG[a])           # tree step: positive Hermitian, eigen-ratio z=e^r
def loop(r): return B(0,r)@B(1,r)@B(0,-r)@B(1,-r)  # four-step word, arms i and j
def bloch(psi):
    psi=psi/np.linalg.norm(psi); return np.array([np.real(psi.conj()@s@psi) for s in SIG])
ZW=3+2*np.sqrt(2); out={}
# ---------- A
rng=np.random.default_rng(20261112); worst=0; viol=0
for _ in range(20000):
    phi=rng.uniform(0,np.pi); k=rng.uniform(0,2); t=rng.uniform(0,6.28)
    c=(1+np.sin(2*k*t)*np.sin(phi))/2
    if c<1e-9 or c>1-1e-9: continue
    G=np.tanh(0.5*np.log((1-c)/c)); worst=max(worst,abs(G-(1-2*c)))
    Gd=-2*k*np.sin(phi)*np.cos(2*k*t); g=k*k*np.sin(phi)**2
    if Gd*Gd>4*g*(1-G*G)+1e-12: viol+=1
    worst=max(worst,abs((4*g*(1-G*G)-Gd*Gd)-4*g*np.cos(phi)**2*np.sin(2*k*t)**2))
reach=[(round(p/np.pi,3), bool(np.sin(p)**2>=0.5)) for p in [0.2,np.pi/4-1e-6,np.pi/4+1e-6,1.0,np.pi/2]]
out['A']={'max_residual':worst,'bound_violations':viol,'half_line_reached(phi/pi)':reach}
# ---------- B
wB=0
for z in np.linspace(1.05,20,400):
    r=np.log(z); wB=max(wB,abs(np.trace(loop(r)).real-(2-4*np.sinh(r/2)**4))/max(1,4*np.sinh(r/2)**4), abs(np.trace(loop(r)).imag))
out['B']={'max_rel_residual':wB,'trace_at_wall':float(np.trace(loop(np.log(ZW))).real)}
# ---------- C  fixed point and frame
def frame(z):
    r=np.log(z); W=loop(r)
    # fixed positive X with W X W^dag = X : solve linear system on Hermitian X = a0 + a.sigma
    basis=[I2]+SIG
    M=np.array([[0.5*np.trace(b2@(W@b1@W.conj().T-b1)).real for b1 in basis] for b2 in basis])
    u,s,vh=np.linalg.svd(M); null=vh[s<1e-9]
    best=None
    for v in null:
        for sgn in (1,-1):
            X=sum(sgn*v[i]*basis[i] for i in range(4))
            ev=np.linalg.eigvalsh(X)
            if ev.min()>1e-12: best=X/np.sqrt(np.linalg.det(X).real)
    if best is None:
        # 2-dim null space: search combination that is positive
        for th in np.linspace(0,2*np.pi,7201):
            v=np.cos(th)*null[0]+np.sin(th)*null[1] if len(null)>1 else null[0]
            X=sum(v[i]*basis[i] for i in range(4)); ev=np.linalg.eigvalsh(X)
            if ev.min()>1e-9:
                X=X/np.sqrt(np.linalg.det(X).real)
                if best is None or np.trace(X).real<np.trace(best).real: best=X
    return W,best,len(null)
rows=[]; wC=0
for z in [1.5,2,3,4,5,5.5,5.8]:
    W,X,nd=frame(z); S=sqrtm(X); U=np.linalg.inv(S)@W@S
    resU=np.linalg.norm(U.conj().T@U-I2); wC=max(wC,resU,np.linalg.norm(S-S.conj().T))
    r=np.log(z); th=2*np.arccos(np.clip(1-2*np.sinh(r/2)**4,-1,1))
    ax=np.array([np.trace(U@s).imag for s in SIG]); ax=-ax/np.linalg.norm(ax)
    eta=np.arccosh(np.trace(X).real/2); nX=np.array([np.trace(X@s).real/2 for s in SIG]); 
    nX=nX/np.linalg.norm(nX) if np.linalg.norm(nX)>1e-12 else nX
    # obliqueness of the lab-frame eigenvectors (Petermann factor)
    w,VR=np.linalg.eig(W); VL=np.linalg.inv(VR).conj().T
    K=[ (np.vdot(VL[:,i],VL[:,i])*np.vdot(VR[:,i],VR[:,i])).real/abs(np.vdot(VL[:,i],VR[:,i]))**2 for i in range(2)]
    conn=0.5*np.linalg.norm(W@W.conj().T-W.conj().T@W)**2
    rows.append(dict(z=z,Gamma2=np.tanh(r/2)**2,theta_over_2pi=th/(2*np.pi),null_dim=nd,unitary_res=resU,axis=ax.round(6).tolist(),
                     fixed_radius=np.tanh(eta/2),fixed_dir=nX.round(6).tolist(),K=K[0],self_comm=conn))
out['C']={'max_residual':wC,'rows':rows}
# ---------- D  wall
W=loop(np.log(ZW)); N=W+I2
out['D']={'norm_W_plus_1':float(np.linalg.norm(N)),'norm_(W+1)^2':float(np.linalg.norm(N@N)),'rank_W_plus_1':int(np.linalg.matrix_rank(N,tol=1e-9))}
# past the wall
rowsH=[]
for z in [5.9,6.5,8,16.8177,206.768]:
    r=np.log(z); t=2-4*np.sinh(r/2)**4; lam=2*np.arccosh(-t/2); rowsH.append(dict(z=z,trace=t,run_rapidity=lam))
out['D']['past_wall']=rowsH
# ---------- E  light fed by the tree (Garrett step z=5), each arm as the prepared projector
def feed(z,prep):
    W,X,nd=frame(z); S=sqrtm(X); Si=np.linalg.inv(S); U=Si@W@S
    r=np.log(z); th=2*np.arccos(1-2*np.sinh(r/2)**4)
    ax=np.array([np.trace(U@s).imag for s in SIG]); ax=-ax/np.linalg.norm(ax)
    # prepared pure state with Bloch vector along prep (lab), carried to the loop's own frame
    v=np.array(prep,float); v/=np.linalg.norm(v); P=0.5*(I2+sum(v[i]*SIG[i] for i in range(3)))
    w,V=np.linalg.eigh(P); psi=V[:,1]; psi_f=Si@psi; s0=bloch(psi_f)
    cphi=float(np.dot(s0,ax)); phi=np.arccos(np.clip(cphi,-1,1))
    # readout axis q: perpendicular to the loop axis and to the starting state (so the signal starts at c=1/2)
    q=np.cross(ax,s0); 
    if np.linalg.norm(q)<1e-12: return dict(prep=prep,phi_over_pi=phi/np.pi,theta=th,kappa=th/2,note='state on the loop axis: no signal',res=0.0,sin2phi=np.sin(phi)**2)
    q/=np.linalg.norm(q); Q=0.5*(I2+sum(q[i]*SIG[i] for i in range(3)))
    res=0; Ut=I2
    for n in range(0,60):
        ps=Ut@psi_f; ps/=np.linalg.norm(ps); c=np.real(ps.conj()@Q@ps)
        res=max(res,abs(c-(1+np.sin(n*th)*np.sin(phi))/2)); Ut=U@Ut
    return dict(prep=prep,phi_over_pi=phi/np.pi,sin2phi=np.sin(phi)**2,theta=th,kappa=th/2,g=(th/2)**2*np.sin(phi)**2,res=res)
E_rows=[feed(5,p) for p in ([1,0,0],[0,1,0],[0,0,1],[1,1,1],[1,-1,0])]
out['E']={'rows':E_rows,'max_residual':max(x['res'] for x in E_rows)}
# also the lab-frame (oblique) signal for arm k vs own-frame signal: how different
W,X,nd=frame(5); S=sqrtm(X)
# ---------- F  one ball, three readings
wF=0
for eta in np.linspace(0.01,12,500):
    p=np.tanh(eta/2); b=np.tanh(eta); wF=max(wF,abs(b-2*p/(1+p*p)))
    Em=np.cosh(eta); wF=max(wF,abs(p*p-(Em-1)/(Em+1)), abs(p-(np.exp(eta)-1)/(np.exp(eta)+1)))
eta3=np.arccosh(3.0)
out['F']={'max_residual':wF,'radius_at_E=3m':float(np.tanh(eta3/2)),'1/sqrt2':float(1/np.sqrt(2)),
          'half_line_point':{'eta=ln(3+2sqrt2)':float(np.log(ZW)),'E_over_m':float(np.cosh(np.log(ZW))),'Klein_radius':float(np.tanh(np.log(ZW)))}}
print(json.dumps(out,indent=1,default=float))
open('feed_loop_01.out','w').write(json.dumps(out,indent=1,default=float))

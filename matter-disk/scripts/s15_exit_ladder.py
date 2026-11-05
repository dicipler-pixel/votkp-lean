# SCRIPT: s15_exit_ladder
"""s15: the exit ladder on the opened PT-symmetric SSH chain.
Checks, at 200 random gapped parameter points (w=1, seed 15):
  (a) T_R = 1/2{X+1/2,H} restricted to the right half commutes with the biorthogonal block C_R
      (measured as the eigen-residual of C_R on edge-localised eigenvectors of T_R);
  (b) the edge levels are eps_j = j*Delta + i*theta with Delta = 2*pi*K'(k)/K(k), k = v'/w';
  (c) theta = pi*F(arcsin s | k^2)/K(k), s = u*w/(w^2 - v'^2);
  (d) the ladder is inside the disk iff E(0)E(pi) > u^2 (sign of cos theta).
Also the exact dimer case v=0, theta = 2 arcsin(u/w)."""
import numpy as np, mpmath as mp
rng=np.random.default_rng(15)
def block(v,w,u,Lc,N=6000):
    ks=2*np.pi*(np.arange(N)+0.5)/N
    E=np.sqrt(v*v+w*w-u*u+2*v*w*np.cos(ks)+0j)
    q=v+w*np.exp(-1j*ks)                          # h = [[iu, q],[conj-in-k q~, -iu]]
    qt=v+w*np.exp(1j*ks)
    P=np.empty((N,2,2),complex)                    # lower band P = (I - h/E)/2
    P[:,0,0]=0.5*(1-1j*u/E); P[:,1,1]=0.5*(1+1j*u/E)
    P[:,0,1]=-0.5*q/E; P[:,1,0]=-0.5*qt/E
    d=np.arange(-(Lc-1),Lc)
    G=np.einsum('dk,kab->dab',np.exp(1j*np.outer(d,ks)),P)/N
    C=np.zeros((2*Lc,2*Lc),complex)
    for c in range(Lc):
        for cp in range(Lc):
            C[2*c:2*c+2,2*cp:2*cp+2]=G[c-cp+Lc-1]
    return C
def Tmat(v,w,u,L):
    T=np.zeros((2*L,2*L),complex)
    for c in range(L):
        a,b=2*c,2*c+1; x=c+0.5
        T[a,a]=1j*u*x; T[b,b]=-1j*u*x; T[a,b]=T[b,a]=v*x
        if c<L-1: T[b,a+2]=T[a+2,b]=w*(c+1)
    return T
def predict(v,w,u):
    E0=np.sqrt((v+w)**2-u*u); Ep=np.sqrt((w-v)**2-u*u)
    wp=(E0+Ep)/2; vp=(E0-Ep)/2; k=vp/wp
    K=float(mp.ellipk(k*k)); Kp=float(mp.ellipk(1-k*k))
    s=u*w/(w*w-vp*vp)
    th=np.pi*float(mp.ellipf(mp.asin(s),k*k))/K
    return 2*np.pi*Kp/K, th, E0*Ep
def measure(v,w,u,L=90):
    C=block(v,w,u,L); T=Tmat(v,w,u,L)
    ev,R=np.linalg.eig(T); lv=[]
    for i in np.argsort(abs(ev))[:12]:
        r=R[:,i]/np.linalg.norm(R[:,i])
        if np.abs(r[-30:]).max()>1e-9: continue
        nu=(r.conj()@C@r)
        if abs(nu)<1e-14 or abs(1-nu)<1e-14: continue
        res=np.linalg.norm(C@r-nu*r)
        lv.append((ev[i].real,np.log((1-nu)/nu),res))
    lv.sort(key=lambda x:x[0])
    return lv
out=[]
pts=[]
while len(pts)<200:
    v=rng.uniform(0.02,0.7); u=rng.uniform(0.02,0.9)
    Ep2=(1-v)**2-u*u
    if Ep2<0.2**2 : continue
    pts.append((v,u))
worst={'res':0,'phase':0,'spacing':0}; agree=0; outside=0
for (v,u) in pts:
    D,th,p=predict(v,1.0,u)
    lv=measure(v,1.0,u)
    if not lv:
        print('no edge levels at',v,u); continue
    j0=min(range(len(lv)),key=lambda i:abs(lv[i][1].real))
    use=[x for x in lv if abs(x[1].real)<1.5*D+1e-9 and x[2]<1e-6]   # j=0,+-1
    for t,e,res in use:
        worst['res']=max(worst['res'],res)
        worst['phase']=max(worst['phase'],abs(np.angle(np.exp(1j*(e.imag-th)))))
    re=sorted(x[1].real for x in use)
    for a,b in zip(re,re[1:]):
        if D<40: worst['spacing']=max(worst['spacing'],abs((b-a)-D)/D)
    meas_in=np.cos(lv[j0][1].imag)>0; pred_in=p>u*u
    agree+= (meas_in==pred_in); outside+= (not pred_in)
lines=[f'points: 200 (w=1, seed 15, gap E(pi)>=0.2, block 90 cells), of which {outside} lie past the exit line E0*Epi<u^2',
 f'(a) max eigen-residual of C_R on T_R edge eigenvectors (levels j=0,+-1): {worst["res"]:.2e}',
 f'(b) max relative spacing error |Re(eps_(j+1)-eps_j)-Delta|/Delta:          {worst["spacing"]:.2e}',
 f'(c) max phase error |Im eps_j - theta_pred| (j=0,+-1):                    {worst["phase"]:.2e}',
 f'(d) inside/outside verdict agrees with sign(E0*Epi-u^2): {agree}/200']
# exact dimer case v=0
md=0
for u in [0.1,0.3,0.5,0.6,0.7,0.75,0.9]:
    D,th,p=predict(0.0,1.0,u)
    md=max(md,abs(th-2*np.arcsin(u)))
lines.append(f'v=0 dimer limit: max |theta_pred - 2 arcsin(u/w)| over 7 values of u: {md:.2e}')
# exit line: theta_pred at E0*Epi=u^2 equals pi/2
mx=0
for v in [0.05,0.1,0.2,0.3,0.4,0.5]:
    uu=(1-v*v)/np.sqrt(2*(1+v*v))   # closed form of E0*Epi=u^2 at w=1
    mx=max(mx,abs(predict(v,1.0,uu)[1]-np.pi/2))
lines.append(f'exit line: max |theta_pred - pi/2| on E0*Epi=u^2 at 6 values of v: {mx:.2e}')
smax=0
for (v,u) in pts:
    E0=np.sqrt((1+v)**2-u*u); Ep=np.sqrt((1-v)**2-u*u); vp=(E0-Ep)/2
    smax=max(smax,u/(1-vp*vp))
lines.append(f'domain: max s = u*w/(w^2-v\'^2) over the 200 points: {smax:.4f} (< 1)')
print('\n'.join(lines))
open('../outputs/s15_exit_ladder.txt','w').write('\n'.join(lines)+'\n')

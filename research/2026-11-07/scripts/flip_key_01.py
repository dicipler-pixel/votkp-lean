# SCRIPT: FLIP-KEY-01
# Exploratory. The intermediate-axis flip (Dzhanibekov key) read in the IQGT.
# 1) climb rate at each axis from linearised Euler equations vs the Connection Energy formula.
# 2) small key: an axis is a saddle exactly when its two neighbouring inertia gaps have opposite sign.
# 3) one full period near the separatrix: the direction n(t) = L/|L| in the body frame, its projector P = (1+n.sigma)/2,
#    gauge-free overlap (Bargmann) phase around the loop vs -1/2 * enclosed solid angle (IQGT curvature 1/2 sin th dth dph),
#    and Montgomery's total rotation: dtheta = 2 E T/|L| - solid angle, checked against the attitude integration.
import numpy as np
from scipy.integrate import solve_ivp
I=np.array([1.0,2.0,3.0])           # I1 < I2 < I3, the key
def euler(t,L): w=L/I; return np.cross(L,w)
# 1) linearised climb rates
print('1) linear rates at each principal axis, unit spin rate')
for k in range(3):
    W=1.0; L0=np.zeros(3); L0[k]=I[k]*W
    J=np.zeros((3,3)); h=1e-7
    for j in range(3):
        d=np.zeros(3); d[j]=h; J[:,j]=(euler(0,L0+d)-euler(0,L0-d))/(2*h)
    ev=np.linalg.eigvals(J); grow=max(ev.real)
    a,b=[i for i in range(3) if i!=k]
    prod=(I[k]-I[a])*(I[k]-I[b])
    ce=W*np.sqrt(abs((I[2]-I[1])*(I[1]-I[0])/(I[0]*I[2]))) if k==1 else 0.0
    print(f'   axis {k+1}: max growth {grow:.6f}  | gap product (I_k-I_a)(I_k-I_b) = {prod:+.1f} -> {"climb (saddle)" if prod<0 else "turn (centre)"} | Connection-Energy rate {ce:.6f}')
# 3) one period near the intermediate axis
eps=1e-3
L0=np.array([eps, I[1]*1.0, eps*0.7]); Lmag=np.linalg.norm(L0); E=0.5*np.sum(L0**2/I)
sol=solve_ivp(euler,[0,200],L0,rtol=1e-12,atol=1e-14,dense_output=True,max_step=0.01)
# period: second return of L2 sign pattern -> use return of L to start
ts=np.linspace(0,200,400001); Ls=sol.sol(ts).T
d=np.linalg.norm(Ls-L0,axis=1); idx=np.where((d[1:-1]<d[:-2])&(d[1:-1]<d[2:])&(d[1:-1]<1e-2))[0]+1
T=ts[idx[0]]
from scipy.optimize import minimize_scalar
T=minimize_scalar(lambda t: np.linalg.norm(sol.sol(t)-L0),bracket=(T-0.05,T,T+0.05)).x
tt=np.linspace(0,T,200001); n=(sol.sol(tt)/Lmag).T
flips=np.sum(np.diff(np.sign(n[:,1]))!=0)
print(f'3) one period T = {T:.6f} (unit spin), sign flips of the intermediate component in one period: {flips}')
# projector path and gauge-free overlap phase
def ket(v):
    th=np.arccos(np.clip(v[2],-1,1)); ph=np.arctan2(v[1],v[0])
    return np.array([np.cos(th/2), np.exp(1j*ph)*np.sin(th/2)])
ks=[ket(v) for v in n[::20]]; ks.append(ks[0])
prod=1+0j
for a,b in zip(ks[:-1],ks[1:]): prod*=np.vdot(a,b)
berry=-np.angle(prod)
# enclosed solid angle by line integral of (1-cos th) dph about the z axis (body 3-axis)
th=np.arccos(np.clip(n[:,2],-1,1)); ph=np.unwrap(np.arctan2(n[:,1],n[:,0]))
sa=np.sum((1-np.cos(0.5*(th[1:]+th[:-1])))*np.diff(ph))
print(f'   Bargmann overlap phase of P(t) around the loop: {berry:+.9f}')
print(f'   -1/2 * solid angle enclosed (about axis 3):    {(-0.5*sa+np.pi)%(2*np.pi)-np.pi:+.9f}   solid angle = {sa:+.9f}')
# attitude: integrate R' = R hat(w), compare rotation about L with Montgomery
def att(t,y):
    R=y.reshape(3,3); w=sol.sol(t)/I
    W=np.array([[0,-w[2],w[1]],[w[2],0,-w[0]],[-w[1],w[0],0]]); return (R@W).ravel()
A=solve_ivp(att,[0,T],np.eye(3).ravel(),rtol=1e-12,atol=1e-14,max_step=0.01)
R=A.y[:,-1].reshape(3,3); Ls_=R@sol.sol(T)
u=Ls_/np.linalg.norm(Ls_)
# rotation angle of R about u (R maps body to space; R(T) fixes spatial L direction)
c=(np.trace(R)-1)/2; ang=np.arccos(np.clip(c,-1,1))
axis=np.array([R[2,1]-R[1,2],R[0,2]-R[2,0],R[1,0]-R[0,1]]); sgn=np.sign(axis@u)
rot=sgn*ang
mont=(2*E*T/Lmag - sa)
print(f'   attitude after one period: rotation about L = {rot:+.9f} rad;  Montgomery 2ET/|L| - solid angle = {(mont+np.pi)%(2*np.pi)-np.pi:+.9f} (mod 2pi)')
print(f'   dynamical part 2ET/|L| = {2*E*T/Lmag:.6f}, geometric part (solid angle) = {sa:.6f}')

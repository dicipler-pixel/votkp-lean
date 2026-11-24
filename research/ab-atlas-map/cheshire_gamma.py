# SCRIPT: CHESHIRE-GAMMA-01
# Setup: two arms L, R; polarization H, V; grin observable s = circular handedness (s = i|V><H| - i|H><V|).
# Pre-selection: (|L> + |R>)/sqrt2 (x) |H>.  Post-selection: (|L>|a> + e^{i Phi}|R>|b>)/sqrt2, any polarizations a, b, flux Phi on R.
# z   = (R-arm amplitude)/(L-arm amplitude) of <f|i>          -> Gamma   = (z-1)/(z+1)      (the cat)
# z_s = same ratio with s inserted                              -> Gamma_s = (z_s-1)/(z_s+1)  (the grin)
# w_x = <x|s|H>/<x|H> (handedness weak value in one arm)        -> Gamma_x = (w_x-1)/(w_x+1)
# Kill lines, written before the run:
#  K1: cat arm weak values differ from (1-Gamma)/2 (L) and (1+Gamma)/2 (R) by more than 1e-10
#  K2: grin arm weak values differ from s_w*(1-Gamma_s)/2 and s_w*(1+Gamma_s)/2 (s_w = total grin weak value) by more than 1e-10
#  K3: Gamma_s differs from Gamma (+) Gamma_b (+) (-Gamma_a) under u(+)v=(u+v)/(1+uv) (card B98) by more than 1e-9
#  K4: changing the flux Phi changes the separation Gamma_s (+) (-Gamma)   (flux alone must not split cat from grin)
#  K5: the original Cheshire arrangement (a=H, b=V) does not sit at Gamma=-1 with the grin share entirely in R
#  K6: card B158 bound violated for any of the four arm observables
#  K7: a mirror-fixed (linear) arm polarization gives |Gamma_x| different from 1 by more than 1e-10
import numpy as np
rng=np.random.default_rng(11)
H=np.array([1,0],complex); V=np.array([0,1],complex)
s=np.array([[0,-1j],[1j,0]])
PL=np.diag([1.0,0]); PR=np.diag([0,1.0]); I2=np.eye(2)
def cay(z): return (z-1)/(z+1)
def add(u,v): return (u+v)/(1+u*v)
def rnd():
    v=rng.normal(size=2)+1j*rng.normal(size=2); return v/np.linalg.norm(v)
def run(a,b,Phi):
    i=np.kron(np.array([1,1])/np.sqrt(2),H)
    f=(np.kron([1,0],a)+np.exp(1j*Phi)*np.kron([0,1],b))/np.sqrt(2)
    ov=np.vdot(f,i)
    wv=lambda A: np.vdot(f,A@i)/ov
    ops=dict(catL=np.kron(PL,I2),catR=np.kron(PR,I2),grinL=np.kron(PL,s),grinR=np.kron(PR,s))
    W={k:wv(A) for k,A in ops.items()}
    aL=np.vdot(a,H); aR=np.exp(-1j*Phi)*np.vdot(b,H)
    sL=np.vdot(a,s@H); sR=np.exp(-1j*Phi)*np.vdot(b,s@H)
    b158=max(abs(ov)**2*abs(W[k])**2-np.vdot(i,ops[k]@ops[k]@i).real for k in ops)
    return W,aR/aL,sR/sL,(sL/aL),(np.vdot(b,s@H)/np.vdot(b,H)),b158,abs(ov)**2
k1=k2=k3=k4=0; k6=-1
for t in range(4000):
    a,b=rnd(),rnd(); Phi=rng.uniform(-3,3)
    W,z,zs,wa,wb,b158,p0=run(a,b,Phi)
    G,Gs=cay(z),cay(zs); sw=W['grinL']+W['grinR']
    k1=max(k1,abs(W['catL']-(1-G)/2),abs(W['catR']-(1+G)/2))
    k2=max(k2,abs(W['grinL']-sw*(1-Gs)/2),abs(W['grinR']-sw*(1+Gs)/2))
    pred=add(add(G,cay(wb)),-cay(wa)); 
    if abs(1+G*cay(wb))>1e-3 and abs(Gs)<50: k3=max(k3,abs(Gs-pred)/(1+abs(Gs)))
    W2,z2,zs2,_,_,_,_=run(a,b,Phi+0.9)
    k4=max(k4,abs(zs/z-zs2/z2)); k6=max(k6,b158)
print('K1 worst cat-arm error      :',k1)
print('K2 worst grin-arm error     :',k2)
print('K3 worst addition-law error :',k3)
print('K4 worst change of z_s/z when the flux changes:',k4)
print('K6 worst (lhs - rhs) of B158, must be <= 0   :',k6)
# K5 original arrangement, approached as b -> V
for eps in (1e-2,1e-4,1e-6):
    a=H; b=np.array([eps,1],complex); b/=np.linalg.norm(b)
    W,z,zs,wa,wb,_,p0=run(a,b,0.0); sw=W['grinL']+W['grinR']
    print('K5 eps=%g  Gamma=%.6f  catL=%.6f catR=%.6f | grin share in R=%.6f  |grinR|=%.6f grinL=%.2e  p0=%.4f'%(eps,cay(z).real,W['catL'].real,W['catR'].real,(W['grinR']/sw).real,abs(W['grinR']),abs(W['grinL']),p0))
k7=0
for th in np.linspace(0.05,1.5,30):
    x=np.cos(th)*H+np.sin(th)*V; w=np.vdot(x,s@H)/np.vdot(x,H); k7=max(k7,abs(abs(cay(w))-1))
print('K7 worst | |Gamma_x| - 1 | for linear (mirror-fixed) arm polarization:',k7)
for chi,name in ((np.pi/2,'handed one way'),(-np.pi/2,'handed the other way')):
    x=np.cos(0.6)*H+np.exp(1j*chi)*np.sin(0.6)*V; w=np.vdot(x,s@H)/np.vdot(x,H)
    print('   elliptical,',name,': w =',np.round(w,6),' Gamma_x =',np.round(cay(w),6))
print('   flux alone (a=b): Gamma =',np.round(cay(np.exp(-1j*1.0)),6),' (imaginary axis)')

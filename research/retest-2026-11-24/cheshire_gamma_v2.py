# SCRIPT: CHESHIRE-GAMMA-02
# Changes from 01: the published pre-selection (i|L> + |R>)/sqrt2 is used, weak values are printed as complex numbers,
# and one convention is fixed for the whole record:
#   z = (right-arm amplitude)/(left-arm amplitude) of <f|i>,  Gamma = (z-1)/(z+1),
#   right arm reads (1+Gamma)/2, left arm reads (1-Gamma)/2.
# Which lines can fail and which cannot (stated before the run):
#   CAN FAIL  C1: published states give cat (1, 0) and grin (0, 1) as complex numbers, not only in modulus
#   CAN FAIL  C2: the flux reading reaches the rim |Gamma| = 1 at a quarter flux quantum (Phi = pi/2) and is outside the disc beyond it
#   CAN FAIL  C3: which twists land on the rim depends on the grin observable (three observables tried)
#   CANNOT FAIL (dictionary, true by definition): arm shares (1 -/+ Gamma)/2; the addition law joining cat and grin; flux moving both together
import numpy as np
H=np.array([1,0],complex); V=np.array([0,1],complex); L=np.array([1,0],complex); R=np.array([0,1],complex)
plus=(H+1j*V)/np.sqrt(2); minus=(H-1j*V)/np.sqrt(2); D=(H+V)/np.sqrt(2); A=(H-V)/np.sqrt(2)
obs={'circular (the published grin)':np.outer(plus,plus.conj())-np.outer(minus,minus.conj()),
     'diagonal':np.outer(D,D.conj())-np.outer(A,A.conj()),
     'horizontal/vertical':np.outer(H,H.conj())-np.outer(V,V.conj())}
PL=np.outer(L,L.conj()); PR=np.outer(R,R.conj()); I2=np.eye(2)
cay=lambda z:(z-1)/(z+1)
pre=np.kron((1j*L+R)/np.sqrt(2),H); post=(np.kron(L,H)+np.kron(R,V))/np.sqrt(2); ov=np.vdot(post,pre)
s=obs['circular (the published grin)']
for nm,Aop in (('cat  left ',np.kron(PL,I2)),('cat  right',np.kron(PR,I2)),('grin left ',np.kron(PL,s)),('grin right',np.kron(PR,s))):
    print('C1',nm,np.round(np.vdot(post,Aop@pre)/ov,12))
print('   success probability',round(abs(ov)**2,6))
for frac in (0.1,0.2,0.25,0.3,0.4,0.49):
    Phi=2*np.pi*frac; G=cay(np.exp(-1j*Phi)); print('C2 flux %.2f of a quantum: Gamma = %+.6fi   |Gamma| = %.6f'%(frac,G.imag,abs(G)))
for nm,s in obs.items():
    out=[]
    for lab,x in (('linear 35 deg',np.cos(0.6)*H+np.sin(0.6)*V),('handed',np.cos(0.6)*H+1j*np.sin(0.6)*V),('other hand',np.cos(0.6)*H-1j*np.sin(0.6)*V)):
        den=np.vdot(x,H); w=np.vdot(x,s@H)/den; g=cay(w)
        out.append('%s: Gamma_x=%s |.|=%.4f'%(lab,np.round(g,4),abs(g)))
    print('C3',nm,'->',' ; '.join(out))

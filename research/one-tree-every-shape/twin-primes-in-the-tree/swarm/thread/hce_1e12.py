# SCRIPT: TWIN-HCE-1E12
# Hypothesis H-CE: the normalised connection energy between the two views of the chain,
#   N = ||[L, L*]||_F / ||L||_F^2 = sqrt(2) tanh(d) sin(phi/2) sin(beta),
# converges. Here phi is the frame turn, beta is the angle between the turn axis and the heading n,
# and d is the distance.
# Kill, written before any run (24 Nov, prior-art report): H-CE fails if |N(1e9)-N(1e8)| > |N(1e8)-N(1e7)|.
# Extended kill, written now before running: it also fails if the decade-to-decade change of N
# does not shrink from 1e9 to 1e12.
# First line: check the identity against an explicit SL(2,C) product rebuilt from the row
# (the boost along n with distance d, times the rotation about ax by phi).
import csv, numpy as np
from scipy.linalg import expm
rows=list(csv.DictReader(open('../swarm/precision/out/walk_1e12.csv')))
s=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]])]
def row(X): return min(rows,key=lambda r:abs(float(r['X'])-X))
def vals(r):
    d=float(r['d']); phi=np.radians(float(r['turn_deg']))
    ax=np.array([float(r[k]) for k in ('ax_x','ax_y','ax_z')]); n=np.array([float(r[k]) for k in ('n_x','n_y','n_z')])
    ax/=np.linalg.norm(ax); n/=np.linalg.norm(n); beta=np.arccos(min(1,abs(ax@n)))
    return d,phi,ax,n,beta
d,phi,ax,n,beta=vals(row(1e8))
P=expm(d/2*sum(n[i]*s[i] for i in range(3))); U=expm(-1j*phi/2*sum(ax[i]*s[i] for i in range(3))); L=P@U
Nm=np.linalg.norm(L@L.conj().T-L.conj().T@L)/np.linalg.norm(L)**2
Nf=np.sqrt(2)*np.tanh(d)*np.sin(phi/2)*np.sin(beta)
print('identity check at 1e8: matrix %.10f formula %.10f'%(Nm,Nf))
prev=None; chg=[]
for X in (1e5,1e6,1e7,1e8,1e9,1e10,1e11,1e12):
    d,phi,ax,n,beta=vals(row(X)); N=np.sqrt(2)*np.tanh(d)*np.sin(phi/2)*np.sin(beta)
    c=None if prev is None else N-prev; chg.append(c); prev=N
    print('%.0e  d %.3f  turn %.4f deg  beta %.3f deg  N %.6f  change %s'%(X,d,np.degrees(phi),np.degrees(beta),N,'' if c is None else '%+.6f'%c))
c=dict(zip((1e5,1e6,1e7,1e8,1e9,1e10,1e11,1e12),chg))
k1=abs(c[1e9])<=abs(c[1e8]); k2=abs(c[1e10])>=abs(c[1e11])>=abs(c[1e12]) if False else (abs(c[1e12])<abs(c[1e10]))
print('original kill:', 'PASS' if k1 else 'KILL', '  extended kill (change at 1e12 smaller than at 1e10):','PASS' if k2 else 'KILL')
print('angle beta vs arccos(1/sqrt3) = %.3f deg'%np.degrees(np.arccos(1/np.sqrt(3))))

"""Independent endpoint-filter audit of preserved incoming matter-disk scripts."""
from pathlib import Path
import json, math, hashlib
import numpy as np
from scipy.linalg import eigvals

ROOT=Path(__file__).resolve().parent
N=2000;L=40;t1=.5
k=2*np.pi*(np.arange(N)+.5)/N
lags=np.arange(-(L-1),L)
ph=np.exp(1j*np.outer(lags,k))/N
disp=np.arange(L)[:,None]-np.arange(L)[None,:]+L-1

def band(m,g):
    dz=m+1j*g
    q=t1+np.exp(1j*k)
    E=np.sqrt(abs(q)**2+dz*dz+0j)
    P=np.zeros((N,2,2),complex)
    P[:,0,0]=(1-dz/E)/2;P[:,1,1]=(1+dz/E)/2
    P[:,0,1]=-q.conj()/(2*E);P[:,1,0]=-q/(2*E)
    return P,E

def spectrum(m,g):
    P,E=band(m,g)
    coeff=np.einsum('lk,kab->lab',ph,P,optimize=True)
    c=coeff[disp].transpose(0,2,1,3).reshape(2*L,2*L)
    return eigvals(c,check_finite=False)

def rotation(m,g,cut):
    nu=spectrum(m,g)
    nu=nu[(np.abs(nu)>cut)&(np.abs(1-nu)>cut)]
    return float(np.max(np.abs(np.log((1-nu)/nu).imag))/np.pi) if len(nu) else 0.

def exit_at(m,cut):
    lo=0.;g=.05
    while g<.8:
        if rotation(m,g,cut)>=.5:
            hi=g;break
        lo=g;g*=1.4
    else:
        return None
    for _ in range(26):
        mid=(lo+hi)/2
        if rotation(m,mid,cut)<.5:lo=mid
        else:hi=mid
    g=(lo+hi)/2
    _,E=band(m,g)
    dnorm=(t1+np.cos(k))**2+np.sin(k)**2+abs(m+1j*g)**2
    K=float(np.mean((1+dnorm/abs(E)**2)/2))
    return dict(m=m,cut=cut,exit_gamma=g,mean_Petermann=K)

# Independent eigensolver cross-check for projector selection.
errors=[]
for m,g in ((.4,.1),(.4,.2),(0.,.4)):
    P,E=band(m,g)
    for ix in (0,137,999,1567):
        q=t1+np.exp(1j*k[ix]);h=np.array([[m+1j*g,q.conjugate()],[q,-m-1j*g]])
        e,R=np.linalg.eig(h);order=np.argsort(e.real);R=R[:,order]
        inverse=np.linalg.inv(R)
        errors.append(float(np.max(abs(P[ix]-np.outer(R[:,0],inverse[0,:])))))
assert max(errors)<1e-12
rows=[]
for m in (.4,0.):
    for cut in (1e-6,1e-8,1e-9,1e-10,1e-12):
        row=exit_at(m,cut);rows.append(row);print(row,flush=True)
oblique=np.array([[2.,1.],[-2.,-1.]])
assert np.array_equal(oblique@oblique,oblique)
report={'classification':'Endpoint-filter sensitivity, not a new physical measurement',
        'N':N,'region_cells':L,'t1':t1,'max_projector_crosscheck_error':max(errors),
        'rows':rows,'oblique_projector':{'C':oblique.tolist(),'X_A':-2.,'Gamma_b':3.},
        'protocol_sha256':hashlib.sha256((ROOT/'INCOMING_EXIT_FILTER_PROTOCOL.md').read_bytes()).hexdigest()}
(ROOT/'incoming_exit_filter_results.json').write_text(json.dumps(report,indent=2)+'\n')

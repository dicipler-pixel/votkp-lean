"""Post-sensitivity diagnostics at recorded exits; residuals are not certified bounds."""
from pathlib import Path
import json
import numpy as np
from scipy.linalg import eig

ROOT=Path(__file__).resolve().parent
source=json.loads((ROOT/'incoming_exit_filter_results.json').read_text())
N,L,t1=source['N'],source['region_cells'],source['t1']
k=2*np.pi*(np.arange(N)+.5)/N
lags=np.arange(-(L-1),L)
ph=np.exp(1j*np.outer(lags,k))/N
disp=np.arange(L)[:,None]-np.arange(L)[None,:]+L-1
out=[]
for row in source['rows']:
    m,g=row['m'],row['exit_gamma']
    q=t1+np.exp(1j*k);dz=m+1j*g;E=np.sqrt(abs(q)**2+dz*dz+0j)
    P=np.zeros((N,2,2),complex)
    P[:,0,0]=(1-dz/E)/2;P[:,1,1]=(1+dz/E)/2
    P[:,0,1]=-q.conj()/(2*E);P[:,1,0]=-q/(2*E)
    coef=np.einsum('lk,kab->lab',ph,P,optimize=True)
    c=coef[disp].transpose(0,2,1,3).reshape(2*L,2*L)
    vals,V=eig(c,check_finite=False)
    cnorm=float(np.linalg.norm(c,2))
    residual=float(np.max(np.linalg.norm(c@V-V*vals,axis=0))/max(1.,cnorm))
    keep=(abs(vals)>row['cut'])&(abs(1-vals)>row['cut'])
    out.append(dict(m=m,cut=row['cut'],exit_gamma=g,
                    normalized_max_eigenpair_residual=residual,
                    eigenvector_condition_number=float(np.linalg.cond(V)),
                    retained_eigenvalues=int(keep.sum()),compression_norm=cnorm))
report={'classification':'Diagnostic added after observing endpoint-filter sensitivity; not a preregistered new decision test',
        'caveat':'Small residuals in a nonnormal eigenproblem do not certify small eigenvalue errors or a continuum-limit threshold.',
        'maximum_normalized_eigenpair_residual':max(x['normalized_max_eigenpair_residual'] for x in out),
        'rows':out}
(ROOT/'incoming_exit_residuals.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))

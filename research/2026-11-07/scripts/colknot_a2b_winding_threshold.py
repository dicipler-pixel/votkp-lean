# SCRIPT: COLKNOT-A2B
# The film's winding integer as a function of the substrate point on the Smith disk (no dispersion: constant N).
# Prediction (derived): r = (r01 + r12 e^{i phi})/(1 + r01 r12 e^{i phi}); the denominator never winds (|r01 r12|<1);
# the numerator winds once per phi-cycle iff |r12| > |r01| = 0.2.  So W = 4 (d=1000 nm) outside the circle |r12| = 0.2 about the film-medium match point N=1.5, 0 inside.
# Check on a grid of (n,k), and on the ELEMENT values (real dispersion).
import numpy as np, warnings; warnings.filterwarnings('ignore')
import cknot_common as C
lam=np.arange(380,781,1.0); nf=1.5; d=1000.0
def Wc(N):
    r=C.film_r(np.full(lam.shape,N),np.array([d]),nf,lam)[0]; ph=np.unwrap(np.angle(r))
    return int(round((-(ph[-1]-ph[0])-np.angle(r[0]/r[-1]))/(2*np.pi)))
ns=np.linspace(0.05,6,60); ks=np.linspace(0,6,61); bad=0; tot=0; counts={}
for n in ns:
    for k in ks:
        N=n+1j*k; W=Wc(N); inside=abs((nf-N)/(nf+N))<0.2; pred=0 if inside else 4
        counts[W]=counts.get(W,0)+1; tot+=1; bad+=(W!=pred)
print('grid n in 0.05..6, k in 0..6: W values seen',counts,' mismatches against |r12|>0.2 rule: %d of %d'%(bad,tot))
print('lossless substrate scan, W_closed vs index: ',[(round(n,2),Wc(n+0j)) for n in [0.5,0.9,1.0,1.05,1.5,2.0,2.2,2.3,3.0,4.0]])
print('   (boundaries at N=1.0 and N=n_f^2=2.25: the AR window, where the film-substrate interface reflects less than the air-film one)')
E=C.elements()
import ri_load; S=ri_load.element_sets(); w=0
out=[]
for el,N in E.items():
    Nn=np.interp(lam/1000,np.sort(S[el]['lam']),(S[el]['n'][np.argsort(S[el]['lam'])]))+1j*np.interp(lam/1000,np.sort(S[el]['lam']),(S[el]['k'][np.argsort(S[el]['lam'])]))
    r=C.film_r(Nn,np.array([d]),nf,lam)[0]; ph=np.unwrap(np.angle(r)); W=int(round((-(ph[-1]-ph[0])-np.angle(r[0]/r[-1]))/(2*np.pi)))
    r12=np.abs((nf-Nn)/(nf+Nn)); out.append((el,W,r12.min(),r12.max()))
print('elements (real dispersion, d=1000): W=0 for',[o[0] for o in out if o[1]==0],' | W=4 for',sum(o[1]==4 for o in out),'| others',[o for o in out if o[1] not in (0,4)])
print('   smallest |r12| over the band among W=4 elements: %.3f (threshold 0.2): %s'%(min(o[2] for o in out if o[1]==4),[o[0] for o in sorted(out,key=lambda x:x[2]) if o[1]==4][:3]))

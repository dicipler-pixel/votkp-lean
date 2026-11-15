import numpy as np,json
rng=np.random.default_rng(31);worst=0;rel=0
for _ in range(500):
 v,u,k=rng.uniform(.05,2),rng.uniform(.01,.8),rng.uniform(0,2*np.pi);w=1.;E2=v*v+w*w+2*v*w*np.cos(k)-u*u
 if abs(E2)<.03:continue
 h=np.array([[1j*u,v+w*np.exp(-1j*k)],[v+w*np.exp(1j*k),-1j*u]])
 ev,R=np.linalg.eig(h);L=np.linalg.inv(R).conj().T
 dk=np.array([[0,-1j*w*np.exp(-1j*k)],[1j*w*np.exp(1j*k),0]]);dv=np.array([[0,1],[1,0]])
 def Q(V):return ((L[:,1].conj()@V@R[:,0])*(L[:,0].conj()@V@R[:,1])/(ev[1]-ev[0])**2).real
 a,c=Q(dk),Q(dv);b=Q((dk+dv)/np.sqrt(2))-(a+c)/2
 det=a*c-b*b;expected=-u*u*w*w*np.cos(k)**2/(16*E2**3)
 worst=max(worst,abs(det-expected));rel=max(rel,abs(det-expected)/max(1,abs(expected)))
assert rel<1e-10
out={'samples':500,'max_absolute_error':worst,'max_scaled_error':rel,'formula':'det Re Q = -u^2 w^2 cos(k)^2 / (16 (E^2)^3)','scope':'real v,w,u,k, E^2 != 0; metric on (k,v) with fixed u,w'}
open('review_round2/metric_signature_check.json','w').write(json.dumps(out,indent=2));print(out)

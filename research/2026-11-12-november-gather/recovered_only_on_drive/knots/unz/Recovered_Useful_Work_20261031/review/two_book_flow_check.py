"""Small independent diagnostic for the exact trace identities in the note."""
from pathlib import Path
import json
import numpy as np

rng=np.random.default_rng(20261031)
def books(k):
    kd=k.conj().T
    c=k@kd-kd@k
    return np.array([np.linalg.norm(c,'fro')**2/8,
                     np.linalg.norm(k@k-kd@kd,'fro')**2/8])
records=[]
for n in [2,3,4,6]:
    worst=np.zeros(2)
    for _ in range(20):
        k=(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/np.sqrt(2*n)
        c=k@k.conj().T-k.conj().T@k
        x=c@k-k@c
        v=-2*x
        expected=-np.array([np.linalg.norm(x,'fro')**2,
                            np.linalg.norm(c@k+k@c,'fro')**2])
        step=1e-6/max(1,np.linalg.norm(v,'fro'))
        observed=(books(k+step*v)-books(k-step*v))/(2*step)
        error=np.abs(observed-expected)/np.maximum(1,np.abs(expected))
        worst=np.maximum(worst,error)
        assert np.all(error<1e-7), (n,error)
    records.append({'dimension':n,'matrices':20,'max_scaled_errors':worst.tolist()})
out={'seed':20261031,'matrices':80,'result':'passed','checks':records,
     'scope':'Centered directional derivative diagnostic; exact proof is cyclic trace algebra in the accompanying note. No source-paper code or physical simulation was rerun.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))

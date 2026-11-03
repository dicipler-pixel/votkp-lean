"""Independent finite checks for B13, with explicit hypothesis/limit controls."""
from pathlib import Path
import json,hashlib
import numpy as np
from scipy.special import xlogy

ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(2026110313)
def h(x):
    x=np.clip(x,0,1)
    return -xlogy(x,x)-xlogy(1-x,1-x)
def ent(c):return float(np.sum(h(np.linalg.eigvalsh(c))))
rows=[]
for delta in (.05,.15,.25,.45):
    for sample in range(16):
        z=rng.normal(size=(12,12))+1j*rng.normal(size=(12,12))
        u,_=np.linalg.qr(z)
        c=(u*rng.uniform(delta,1-delta,12))@u.conj().T
        a,d,b=c[:5,:5],c[5:,5:],c[:5,5:]
        x=b@b.conj().T;tr=float(np.trace(x).real)
        info=ent(a)+ent(d)-ent(c)
        count=int(np.count_nonzero(np.linalg.eigvalsh(x)>=.09))
        lower=info-4*tr;upper=tr/(delta*(1-delta))-info
        assert lower>=-2e-12 and upper>=-2e-12
        assert count<=info/.36+2e-12
        rows.append(dict(delta=delta,information=info,cross_trace=tr,
                         lower_margin=lower,upper_margin=upper,census=count))
sharp=[]
for r in (.01,.001,.0001):
    info=float(2*np.log(2)-2*h(.5+r));ratio=info/r**2
    assert abs(ratio-4)<.002
    sharp.append(dict(r=r,ratio=ratio))
pure=[]
for p in (.01,.0001,.000001):
    pure.append(dict(p=p,cross_trace=p*(1-p),information=float(2*h(p)),
                     ratio=float(2*h(p)/(p*(1-p)))))
assert all(pure[i+1]['ratio']>pure[i]['ratio'] for i in range(2))
out={'status':'PASS','class':'Gauge-invariant Gaussian covariance implementation checks',
     'natural_log_units':True,'cases':len(rows),
     'minimum_lower_bound_margin':min(x['lower_margin'] for x in rows),
     'minimum_upper_bound_margin':min(x['upper_margin'] for x in rows),
     'sharp_lower_family':sharp,'pure_upper_counterfamily':pure,
     'protocol_sha256':hashlib.sha256((ROOT/'GAUSSIAN_INFORMATION_PROTOCOL.md').read_bytes()).hexdigest()}
(ROOT/'gaussian_information_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

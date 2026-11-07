# SCRIPT: RI-LOAD
# Loads tabulated n,k datasets for single elements from the refractiveindex.info database (local clone).
import os, re, yaml, numpy as np
ROOT='/home/claude/data_ri/ri/database/data/main'
def load(path):
    d=yaml.safe_load(open(path))
    for blk in d.get('DATA',[]):
        if blk.get('type')=='tabulated nk':
            arr=np.array([[float(x) for x in ln.split()] for ln in blk['data'].strip().split('\n') if ln.strip()])
            if arr.shape[1]>=3: return arr[:,0],arr[:,1],arr[:,2]
    return None
def element_sets():
    out={}
    for el in sorted(os.listdir(ROOT)):
        if not re.fullmatch(r'[A-Z][a-z]?',el): continue
        best=None
        for dp,dn,fn in os.walk(os.path.join(ROOT,el)):
            for f in fn:
                if not f.endswith('.yml'): continue
                r=load(os.path.join(dp,f))
                if r is None: continue
                lam,n,k=r
                if lam.min()>0.38 or lam.max()<0.78: continue
                span=np.log(lam.max()/lam.min())
                if best is None or span>best[0]: best=(span,f,lam,n,k)
        if best: out[el]=dict(file=best[1],lam=best[2],n=best[3],k=best[4])
    return out

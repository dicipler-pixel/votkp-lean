# SCRIPT: TWIN-WALK-RUNNER-01
# Lays out contiguous chunks [lo,hi) and runs twinwalk on two cores; each chunk writes out/w_<lo>.txt (skips if done).
import subprocess, sys, os
from concurrent.futures import ThreadPoolExecutor
edges=[10000001000]+[k*10**10 for k in range(2,11)]+[k*5*10**10 for k in range(3,21)]+[10**12+20000]
def job(i):
    lo,hi=edges[i],edges[i+1]; fn='out/w_%015d.txt'%lo
    if os.path.exists(fn+'.done'): return
    with open(fn,'w') as f: subprocess.run(['./twinwalk',str(lo),str(hi)],stdout=f,stderr=open(fn+'.err','w'))
    open(fn+'.done','w').close()
n=int(sys.argv[1]) if len(sys.argv)>1 else len(edges)-1
with ThreadPoolExecutor(2) as ex: list(ex.map(job,range(n)))

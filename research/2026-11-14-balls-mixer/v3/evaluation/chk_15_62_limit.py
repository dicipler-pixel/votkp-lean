# SCRIPT: CHK-15-62-LIMIT (6_2 at x=12 at 200 digits; does the k=1/4 branch appear)
import importlib.util
from mpmath import mp, mpf, exp
spec=importlib.util.spec_from_file_location('c7','/home/claude/harness2/eval/chk_07_riley_census.py'); c7=importlib.util.module_from_spec(spec); spec.loader.exec_module(c7)
mp.dps=200
s=exp(mpf(12)); poly=c7.riley_poly(c7.WORDS['6_2'],s)
print("degree",len(poly)-1)
rts=c7.polyroots(poly[::-1],maxsteps=2000,extraprec=800)
for r in rts:
    k=r*((s-1/s)**2-r)
    print("root",mp.nstr(r,12),"k",mp.nstr(k,10))

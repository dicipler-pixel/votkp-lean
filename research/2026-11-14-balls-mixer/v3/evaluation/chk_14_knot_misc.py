# SCRIPT: CHK-14-KNOT-MISC (4_1 v roots at x=0.5 and 0.9; relation residual; large-x limits of k=2-tr[a,b] for 4_1, 5_2, 6_2; x0=arccosh(3/2)/2 = ln golden)
import importlib.util
from mpmath import mp, mpf, exp, acosh, log, sqrt
spec=importlib.util.spec_from_file_location('c7','/home/claude/harness2/eval/chk_07_riley_census.py'); c7=importlib.util.module_from_spec(spec); spec.loader.exec_module(c7)
mp.dps=60
for x in (0.5,0.9):
    s=exp(mpf(x)); print("4_1 x",x,"real v roots:",[float(v) for v in c7.real_roots(c7.riley_poly(c7.WORDS['4_1'],s))],"(R6-10: +0.33976, -0.25360 at 0.5; +4.01557, -0.80062 at 0.9)")
print("x0 = acosh(3/2)/2 =",acosh(mpf(3)/2)/2," ln golden =",log((1+sqrt(5))/2))
for nm,x in (('4_1',12),('5_2',12),('6_2',12),('4_1',6)):
    s=exp(mpf(x)); out=[]
    for v in c7.real_roots(c7.riley_poly(c7.WORDS[nm],s)):
        k=c7.kvals(s,v)
        if abs(k)<10: out.append(float(k))
    print(nm,"x",x,"k=2-tr[a,b] values with |k|<10:",out,"(R6-52: 4_1 1.0; 5_2 1.0,2.0; 6_2 0.25,~0)")

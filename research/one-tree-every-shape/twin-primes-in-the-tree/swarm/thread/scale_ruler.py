# SCRIPT: TWIN-SCALE-RULER-01
# Question: if the ruler shrinks with the screw (measure each twin gap in units of the local
# mean gap), does the twin chain look the same at every size?
# KILL (written before the run): fails if the scaled-gap quartiles (25/50/75/90%) differ by more
# than 5% between the decade 1e5-1e6 and the decade 1e8-1e9.
import numpy as np, sys
a=np.load(sys.argv[1]).astype(np.int64)
C2=0.6601618158
for lo,hi in ((1e5,1e6),(1e6,1e7),(1e7,1e8),(1e8,1e9)):
    b=a[(a>lo)&(a<=hi)]; g=np.diff(b); x=b[1:].astype(float)
    G_hl=np.log(x)**2/(2*C2)
    s=g/G_hl
    q=np.percentile(s,[25,50,75,90])
    print('%.0e-%.0e  mean gap %7.1f  HL mean %7.1f  scaled-gap quartiles 25/50/75/90 = %s  turn per 30 in log path at end %.1e'%(lo,hi,g.mean(),G_hl.mean(),np.round(q,3),30/hi))

# SCRIPT: TWIN-THREAD-CHECK-1E12
# Test the full-product screw predictions past 1e9, using the 1e12 walk checkpoints.
# The walk records S_s = sum r (1[arm=s] - 1/3), with r = ln(a'/a). Per decade, dS_s/dL is the
# log-step-weighted share minus 1/3. Times the decade's mean gap, that is the same quantity as dev*G
# up to the weighting and the count-share term.
# Step 1: calibrate on 1e8-1e9, where the gap-weighted real value is known (-0.924, 0.839, 0.085).
# Step 2 KILL (written before the run): the predictions fail if, in any decade 1e9-1e12, digit 1 or 7
# differs from the walk value by more than 0.10 after the step-1 calibration offset.
import csv, numpy as np
rows=list(csv.DictReader(open('../swarm/precision/out/walk_1e12.csv')))
def at(X):
    r=min(rows,key=lambda r:abs(float(r['X'])-X)); return r
pred={(1e9,1e10):[-0.945,0.809,0.136],(1e10,1e11):[-0.951,0.806,0.145],(1e11,1e12):[-0.955,0.806,0.15]}
def walkval(lo,hi):
    A,B=at(lo),at(hi)
    dL=float(B['L'])-float(A['L']); dS=np.array([float(B[k])-float(A[k]) for k in ('S_x','S_y','S_z')])
    G=(float(B['X'])-float(A['X']))/(int(B['count'])-int(A['count']))
    return dS/dL*G, G
w89,_=walkval(1e8,1e9); off=np.array([-0.924,0.839,0.085])-w89
print('1e8-1e9 walk metric',np.round(w89,3),' calibration offset',np.round(off,3))
ok=True
for (lo,hi),p in pred.items():
    w,G=walkval(lo,hi); wc=w+off; diff=np.array(p)-wc; ok&=bool(np.all(abs(diff[:2])<=0.10))
    print('%.0e-%.0e  walk (calibrated) %s  predicted %s  diff %s  G %.0f'%(lo,hi,np.round(wc,3),p,np.round(diff,3),G))
print('PASS' if ok else 'KILL')

# SCRIPT: G5-BMN-SCREW-RECOMPUTE
# Recompute beta-Mn Mn1 screw-orbit chi from the batch6 operation g(x,y,z)=(1/4-y, x-1/4, z+1/4), a=6.3145, seed (.061,.061,.061).
# WHY IT PROVES IT: independent arithmetic from the stated operation and seed; mirror x->-x must flip the sign; reversal must keep it.
import numpy as np
a=6.3145
p=np.array([.061,.061,.061]); P=[p]
for _ in range(3):
    x,y,z=P[-1]; P.append(np.array([.25-y,x-.25,z+.25]))
P=[q*a for q in P]
d=[P[i+1]-P[i] for i in range(3)]
chi=lambda d:np.dot(np.cross(d[0],d[1]),d[2])
print('step',np.linalg.norm(d[0]),'chi',chi(d))
print('reversed',chi([-d[2],-d[1],-d[0]]))
m=np.diag([-1,1,1]); print('mirror',chi([m@v for v in d]))

# SCRIPT: LARGE-FIELD-FLOOR-02
# SU(3) eigenphases (a,b,-a-b). Large field at radius delta: some eigenphase has |theta| >= delta (principal branch).
# Claim under test: min of 3 - Re chi over the large-field set = m(delta) = (1 - cos delta) + 2(1 - cos(delta/2)),
# attained at (delta, -delta/2, -delta/2). At delta = pi this is 4, the B128 winding floor.
# Kill: any grid point in the large-field set with 3 - Re chi < m(delta) - 1e-9.
import numpy as np
n=2001; t=np.linspace(-np.pi,np.pi,n); A,B=np.meshgrid(t,t); C=-(A+B)
L=np.angle(np.exp(1j*np.stack([A,B,C])))          # principal eigenphases
well=3-np.cos(L).sum(0); big=np.abs(L).max(0)
print(" delta/pi   m(delta)    grid min    violation")
for d in np.linspace(0.05,1.0,20)*np.pi:
    m=(1-np.cos(d))+2*(1-np.cos(d/2)); sel=big>=d-1e-12
    gm=well[sel].min()
    print(f"{d/np.pi:8.3f} {m:10.6f} {gm:11.6f} {max(0,m-gm):10.2e}")

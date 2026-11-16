# SCRIPT: PENDULUM-SWING-01
# Real pendulum theta'' = -sin(theta) (omega0 = 1). Checks three things the wheel reading leans on.
# (a) energy constant along the swing (kill: drift > 1e-9 relative)
# (b) equal time-average shares KE = PE (true for the linear oscillator; kill for the real pendulum if |KE/E - 1/2| > 1e-3)
# (c) period vs amplitude against exact 4K(sin(theta0/2)) (kill: mismatch > 1e-8)
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ellipk
def run(th0):
    k=np.sin(th0/2); T=4*ellipk(k**2)
    f=lambda t,y:[y[1],-np.sin(y[0])]
    s=solve_ivp(f,[0,T],[th0,0],rtol=1e-12,atol=1e-12,dense_output=True)
    t=np.linspace(0,T,200001); th,w=s.sol(t)
    KE=0.5*w**2; PE=1-np.cos(th); E=KE+PE
    drift=np.max(abs(E-E[0]))/E[0]
    ret=abs(th[-1]-th0)
    frac=np.trapezoid(KE,t)/T/E[0]
    return T,drift,ret,frac
print("theta0_deg  period/2pi  energy_drift  return_err  <KE>/E")
for d in [5,30,60,90,120,150,170,179]:
    T,dr,ret,fr=run(np.radians(d))
    print(f"{d:9d}  {T/(2*np.pi):10.6f}  {dr:.2e}  {ret:.2e}  {fr:.6f}")

# SCRIPT: B128-FLOOR-CHECK-01
# SU(3) eigenphases (a, b, -a-b). w = (Arg l1 + Arg l2 + Arg l3)/2pi with principal Arg in (-pi, pi].
# Claim under test: on w != 0, 3 - Re chi >= 4. Kill: any grid point with w != 0 and 3 - Re chi < 4 - 1e-12.
# Also checks delta = mean|l-1|^2 equals (2/3)(3 - Re chi) exactly (kill: mismatch > 1e-12).
import numpy as np
n=1201
t=np.linspace(-np.pi,np.pi,n)
A,B=np.meshgrid(t,t)
C=-(A+B)
L=np.exp(1j*np.stack([A,B,C]))
arg=np.angle(L)
w=np.rint(arg.sum(0)/(2*np.pi)).astype(int)
rechi=np.cos(A)+np.cos(B)+np.cos(C)
well=3-rechi
delta=(np.abs(L-1)**2).mean(0)
print("max |delta - (2/3)(3-Rechi)| =",np.abs(delta-(2/3)*well).max())
for k in sorted(set(w.ravel())):
    m=w==k; print(f"w={k:+d}: points {m.sum():7d}  min(3-Re chi) = {well[m].min():.12f}")

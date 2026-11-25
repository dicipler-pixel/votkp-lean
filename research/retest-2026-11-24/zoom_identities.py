# SCRIPT: ZOOM-IDENTITIES-01
import math,cmath
print('ln(4/3) =',math.log(4/3),'  2*ln(1/sin 60deg) =',2*math.log(1/math.sin(math.pi/3)),'  sin^2(60deg) =',math.sin(math.pi/3)**2)
for th in (40,90,120,150):
    t=math.radians(th); L=30.0; d=math.acosh(math.cosh(L)**2-math.sinh(L)**2*math.cos(t)); print('  legs at',th,'deg: end-to-end - 2*leg =',round(d-2*L,9),'  -2 ln(1/sin(half angle)) =',round(-2*math.log(1/math.sin(t/2)),9))
for f in (0.1,0.25,0.4):
    P=2*math.pi*f; print('  flux',f,': |1-e^{iP}|^2/|1+e^{iP}|^2 =',round(abs(1-cmath.exp(1j*P))**2/abs(1+cmath.exp(1j*P))**2,9),'  tan^2(P/2) =',round(math.tan(P/2)**2,9))

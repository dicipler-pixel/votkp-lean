# SCRIPT: G4_CARBON_NITROGEN
import math
from math import sqrt,atan,asin,degrees,sinh,log,tanh
G=lambda z:(z-1)/(z+1)
C=392.09056/64.49352; N=552.06741/97.8901
print('C',C,'rounded inputs',392.09/64.4935,'N',N)
print('G2 sum -1',G(C)**2+G(N)**2-1)
# critical partner with C fixed: Gb^2 = 1-Ga^2
Gb=sqrt(1-G(C)**2); zb=(1+Gb)/(1-Gb); print('critical z',zb)
# check with rounded
Cr=392.09/64.4935; Gb=sqrt(1-G(Cr)**2); print('critical z rounded',(1+Gb)/(1-Gb))
print('angle sum -90', degrees(asin(G(C))+asin(G(N)))-90)
# other pairs
IE={'Na':(0,0)}
# forward-sector window: Gram approach. Poincare circle geometry with axes meeting at angle phi
import numpy as np
def perp_circle(z):
    h=0.5*log(z); r=tanh(h/2); c=(1+r*r)/(2*r); R=(1-r*r)/(2*r); return c,R
def closes_angle(za,zb,phi):
    ca,Ra=perp_circle(za); cb,Rb=perp_circle(zb)
    A=np.array([ca,0]); B=cb*np.array([math.cos(phi),math.sin(phi)])
    # circles centered A (R=Ra) and B (Rb); intersect inside the disk and in forward sector
    d=np.linalg.norm(A-B)
    if d>=Ra+Rb or d<=abs(Ra-Rb): return False
    a=(Ra**2-Rb**2+d**2)/(2*d); h=math.sqrt(max(Ra**2-a**2,0))
    P=A+a*(B-A)/d; perp=np.array([-(B-A)[1],(B-A)[0]])/d
    for s in (1,-1):
        X=P+s*h*perp
        if np.linalg.norm(X)<1:
            # forward sector: coordinates along each axis positive
            ua=np.array([1,0]); ub=np.array([math.cos(phi),math.sin(phi)])
            M=np.array([ua,ub]).T; co=np.linalg.solve(M,X)
            if co[0]>0 and co[1]>0: return True
    return False
lo=[];prev=None
for deg in np.arange(0.5,120,0.001):
    c=closes_angle(C,N,math.radians(deg))
    if prev is not None and c!=prev: lo.append((round(deg,3),c))
    prev=c
print(lo)

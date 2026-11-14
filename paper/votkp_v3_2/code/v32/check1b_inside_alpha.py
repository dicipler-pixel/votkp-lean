# SCRIPT: LOOP2-CHECK1B-ALPHA-INSIDE
# WHY: completes the closed form of the fixed-direction angle on the inside of the wall so one law covers both sides.
# Candidate: cos^2(alpha/2) = 2 Gamma^2 inside (K = 1/sin^2(alpha/2) = 1/(1-2Gamma^2)); past wall cos^2(alpha/2)=1/(2Gamma^2).
# KILL LINE: residual > 1e-40 at 60 digits for any z -> candidate killed.
import mpmath as mp
mp.mp.dps=60
for z in ['1.5','2','3','4','5','5.5','5.8','5.9','6.5','8','16.8177','206.768']:
    r=mp.log(mp.mpf(z)); c,s=mp.cosh(r/2),mp.sinh(r/2); G=mp.tanh(r/2)
    Bx=mp.matrix([[c,s],[s,c]]); By=mp.matrix([[c,-1j*s],[1j*s,c]]); Bxi=mp.matrix([[c,-s],[-s,c]]); Byi=mp.matrix([[c,1j*s],[-1j*s,c]])
    W=Bx*By*Bxi*Byi; E,V=mp.eig(W)
    n=lambda v: mp.sqrt(abs(v[0])**2+abs(v[1])**2)
    a=V[:,0]/n(V[:,0]); b=V[:,1]/n(V[:,1]); c2=abs(a[0].conjugate()*b[0]+a[1].conjugate()*b[1])**2
    cand=2*G*G if G*G<0.5 else 1/(2*G*G)
    print(z,'G2=',mp.nstr(G*G,8),'cos2(alpha/2)=',mp.nstr(c2,15),'resid=',mp.nstr(abs(c2-cand),3))

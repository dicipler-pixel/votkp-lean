# SCRIPT: TWIN-WALK-ANALYSE-01
# Reads the combined checkpoint CSV and answers: (1) half-decade table; (2) H3 per decade; (3) turn-limit fits; (4) c.
# Kill conditions written before the run:
#  H3-K: if the per-decade tilt beta_s does NOT shrink between the first and last full decade (|beta| last >= 0.5 |beta| at 1e6-1e7)
#        the "tilt decays like 1/L^2" reading is killed; if beta*L^2 rises by more than a factor 2 across decades,
#        the 1/L^2 law is killed (and 1/L or constant tilt is preferred).
#  TURN-K: if the three fit forms give limits spread by more than 0.1 deg, no limit is claimed to better than that spread.
#  PRED-K: the 'turn if the tilt dies' readout (frame carried by the minimal rotation that brings the body heading onto the
#        cube diagonal) must not move by more than 0.01 deg between 1e8 and the last mark, else it is not a usable limit.
#  C-K: if c = d - L/sqrt3 moves by more than 2e-4 between 1e9 and the last mark, c is not quoted to 4 digits.
import csv, math, sys, numpy as np
from scipy.optimize import curve_fit
R=list(csv.DictReader(open(sys.argv[1])))
def f(r,k): return float(r[k])
X=np.array([f(r,'X') for r in R]); A=np.array([f(r,'a') for r in R]); L=np.array([f(r,'L') for r in R])
T=np.array([f(r,'turn_deg') for r in R]); C=np.array([f(r,'d_minus_L_over_sqrt3') for r in R])
S=np.array([[f(r,'S_x'),f(r,'S_y'),f(r,'S_z')] for r in R]); AX=np.array([[f(r,'ax_x'),f(r,'ax_y'),f(r,'ax_z')] for r in R])
S2=np.array([f(r,'sum_r2') for r in R]); ANG=np.array([f(r,'angle_heading_Rm_deg') for r in R]); PRED=np.array([f(r,'turn_if_tilt_dies_deg') for r in R])
print('=== (1) half-decade table (cut-off: first twin start a >= X) ===')
print('X        a             steps        L        turn_deg     axis(x,y,z)                 axis_move  d-L/sqrt3   sum r^2       S_x      S_y      S_z     ang(n,Rm)  turn_if_tilt_dies')
prev=None
for i in range(len(R)):
    lg=math.log10(X[i])
    if lg>=4 and abs(2*lg-round(2*lg))<1e-9:
        mv='' if prev is None else '%.4f'%math.degrees(math.acos(min(1,float(AX[i]@AX[prev]))))
        print('%-8.3g %-13d %-12s %-8.4f %-12.6f (%+.4f,%+.4f,%+.4f) %-9s %.6f  %.10f %+.4f %+.4f %+.4f %.4f    %.5f'%(X[i],A[i],R[i]['steps'],L[i],T[i],*AX[i],mv,C[i],S2[i],*S[i],ANG[i],PRED[i])); prev=i
print('\n=== (2) H3: per-decade fit S_s = beta_s L + gamma_s (40 grid points per decade) ===')
print('decade      L_mid   beta_x     beta_y     beta_z    |beta|     |beta|L^2  rms_rem   max_rem   noise_ref=sqrt(2/9 sum r^2 in decade)')
dec=[]
for k in range(4,13):
    m=(X>=10**k*(1-1e-9))&(X<=10**(k+1)*(1+1e-9))
    if m.sum()<30: continue
    Lm=L[m]; Lmid=(Lm[0]+Lm[-1])/2; bs=[]; rem=[]
    for s in range(3):
        p=np.polyfit(Lm,S[m,s],1); bs.append(p[0]); rem.append(S[m,s]-np.polyval(p,Lm))
    rem=np.array(rem); nb=np.linalg.norm(bs); im=np.argmin(abs(L-Lmid)); lam=A[im]/float(R[im]['count']); nref=math.sqrt(2/9*(S2[m][-1]-S2[m][0]))
    dec.append((k,Lmid,bs,nb)); jm=np.argmin(abs(L-Lmid))
    print('1e%-2d-1e%-2d %6.2f  %+.5f  %+.5f  %+.5f  %.5f   %.3f     %.2e  %.2e  %.2e   mean gap %.0f, |beta|*gap = %.3f, sqrt3|beta| = %.3f deg vs angle(n,Rm) at mid = %.3f deg'%(k,k+1,Lmid,*bs,nb,nb*Lmid**2,np.sqrt((rem**2).mean()),abs(rem).max(),nref,lam,nb*lam,math.degrees(math.sqrt(3)*nb),ANG[jm]))
# global comparison of forms for S_s on X>=1e6
m=X>=1e6
print('\nGlobal forms for S_s on X >= 1e6 (rms residual):')
for s,nm in enumerate('xyz'):
    y=S[m,s]; l=L[m]
    p1=np.polyfit(l,y,1); r1=y-np.polyval(p1,l)
    M2=np.vstack([np.ones_like(l),1/l]).T; c2,*_=np.linalg.lstsq(M2,y,rcond=None); r2=y-M2@c2
    M3=np.vstack([np.ones_like(l),np.log(l)/l]).T; c3,*_=np.linalg.lstsq(M3,y,rcond=None); r3=y-M3@c3
    print('  S_%s: linear (const tilt) beta=%+.5f rms %.2e | S_inf - kappa/L: S_inf=%+.4f kappa=%+.3f rms %.2e | S_inf + kappa logL/L: S_inf=%+.4f rms %.2e'%(nm,p1[0],np.sqrt((r1**2).mean()),c2[0],-c2[1],np.sqrt((r2**2).mean()),c3[0],np.sqrt((r3**2).mean())))
print('\n=== (3) turn-limit fits ===')
def fitset(lo):
    m=X>=lo; l=L[m]; a=A[m]; y=T[m]; res={}
    M=np.vstack([np.ones_like(l),1/l]).T; c,*_=np.linalg.lstsq(M,y,rcond=None); res['A+B/L']=(c[0],np.sqrt(((y-M@c)**2).mean()))
    M=np.vstack([np.ones_like(l),a**-0.5]).T; c,*_=np.linalg.lstsq(M,y,rcond=None); res['A+B x^-1/2']=(c[0],np.sqrt(((y-M@c)**2).mean()))
    M=np.vstack([np.ones_like(l),np.log(a)*a**-0.5]).T; c,*_=np.linalg.lstsq(M,y,rcond=None); res['A+B logx x^-1/2']=(c[0],np.sqrt(((y-M@c)**2).mean()))
    M=np.vstack([np.ones_like(l),1/l**2]).T; c,*_=np.linalg.lstsq(M,y,rcond=None); res['A+B/L^2']=(c[0],np.sqrt(((y-M@c)**2).mean()))
    lamv=a/np.array([float(R[i]['count']) for i in np.nonzero(m)[0]])
    M=np.vstack([np.ones_like(l),1/lamv]).T; c,*_=np.linalg.lstsq(M,y,rcond=None); res['A+B/meangap']=(c[0],np.sqrt(((y-M@c)**2).mean()))
    M=np.vstack([np.ones_like(l),ANG[m]]).T; c,*_=np.linalg.lstsq(M,y,rcond=None); res['A+B*angle(n,Rm)']=(c[0],np.sqrt(((y-M@c)**2).mean()))
    try:
        pp,_=curve_fit(lambda l,A_,B_,k_:A_+B_*np.exp(-k_*(l-l[0])),l,y,p0=[y[-1],y[0]-y[-1],0.3],maxfev=20000)
        res['A+B e^-kL']=(pp[0],np.sqrt(((y-(pp[0]+pp[1]*np.exp(-pp[2]*(l-l[0]))))**2).mean()),pp[2])
    except Exception as e: res['A+B e^-kL']=(float('nan'),float('nan'))
    return res
for lo in (1e7,1e8,1e9):
    res=fitset(lo); vals=[v[0] for v in res.values()]
    print('fit window X >= %.0e:'%lo,'; '.join('%s: A=%.4f (rms %.4f%s)'%(k,v[0],v[1],'' if len(v)<3 else ', k=%.3f'%v[2]) for k,v in res.items()),'| spread %.4f'%(max(vals)-min(vals)))
# noise-tail scale: rotation noise beyond N ~ (180/pi)*sqrt(2/3)*sqrt(sum_{n>N} r_n^2); tail of sum r^2 beyond the last mark
# is estimated from the last decade increment times the observed decade ratio.
i9=np.argmin(abs(X-1e9)); il=len(X)-1
for k in range(6,13):
    j=np.argmin(abs(X-10**k))
    if abs(X[j]/10**k-1)>1e-6: continue
    tail=S2[il]-S2[j]
    print('  noise scale from 1e%d to the last mark: sqrt(2/3 * sum r^2) = %.4f deg;  turn moved %.4f deg'%(k,math.degrees(math.sqrt(2/3*tail)),T[il]-T[j]))
print('\n=== (4) c = d - L/sqrt3 ===')
for k in range(5,13):
    j=np.argmin(abs(X-10**k))
    if abs(X[j]/10**k-1)<1e-6: print('  1e%d: c = %.6f'%(k,C[j]))
m=X>=1e8; print('  X>=1e8: mean %.6f, sd %.2e, min %.6f, max %.6f'%(C[m].mean(),C[m].std(),C[m].min(),C[m].max()))
l=L[m]; M=np.vstack([np.ones_like(l),1/l]).T; c,*_=np.linalg.lstsq(M,C[m],rcond=None); print('  fit c = c_inf + B/L on X>=1e8: c_inf = %.6f, B = %+.5f'%(c[0],c[1]))
p=np.polyfit(L[m],C[m],1); print('  linear slope of c in L over X>=1e8: %+.2e per unit L'%p[0])

print('\n=== (5) turn if the tilt dies (Hardy-Littlewood endpoint) ===')
for k in range(5,13):
    j=np.argmin(abs(X-10**k))
    if abs(X[j]/10**k-1)<1e-6: print('  1e%d: %.5f deg   (actual turn %.5f)'%(k,PRED[j],T[j]))
for lo in (1e6,1e8,1e10):
    m=X>=lo
    if m.sum()>3: print('  X>=%.0e: mean %.5f  sd %.1e  range [%.5f, %.5f]'%(lo,PRED[m].mean(),PRED[m].std(),PRED[m].min(),PRED[m].max()))
j8=np.argmin(abs(X-1e8)); print('  PRED-K: move 1e8 -> last = %.5f deg -> %s'%(PRED[-1]-PRED[j8],'PASS' if abs(PRED[-1]-PRED[j8])<0.01 else 'KILL'))
print('  ang(n,Rm) per decade ratio:',' '.join('%.3f'%(ANG[np.argmin(abs(X-10**(k+1)))]/ANG[np.argmin(abs(X-10**k))]) for k in range(6,12) if X[-1]>=10**(k+1)*0.999))

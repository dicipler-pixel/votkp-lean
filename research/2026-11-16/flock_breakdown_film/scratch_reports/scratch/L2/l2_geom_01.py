# SCRIPT: L2-GEOM-01
# Independent recomputation of the ball geometry the Flock inherits. numpy/scipy only; shares no code with lh_math / fl_math.
# Hyperboloid vectors (t,x,y,z), signature (+,-,-,-).
import numpy as np, math
from scipy.optimize import minimize
np.set_printoptions(precision=12, suppress=True)
def mink(p,q): return p[0]*q[0]-p[1]*q[1]-p[2]*q[2]-p[3]*q[3]
AX=np.eye(3)
def boost(u,r):
    B=np.eye(4); c,s=math.cosh(r),math.sinh(r)
    B[0,0]=c; B[0,1:]=s*u; B[1:,0]=s*u; B[1:,1:]=np.eye(3)+(c-1)*np.outer(u,u); return B
O=np.array([1.,0,0,0])
def ball(u,r): return np.array([math.cosh(r),*(math.sinh(r)*u)])
def normal(u,h): return np.array([math.sinh(h),*(math.cosh(h)*u)])
rng=np.random.default_rng(7)
print('G1 ball one peel step out: hyperbolic distance from centre = r = ln z; Poincare radius = Gamma = (z-1)/(z+1)')
e=0
for z in [1.5,3,5,7,9,13]:
    r=math.log(z); p=boost(AX[0],r)@O
    d=math.acosh(mink(p,O)); rad=np.linalg.norm(p[1:])/(1+p[0])
    e=max(e,abs(d-r),abs(rad-(z-1)/(z+1)),abs(rad-math.tanh(r/2)),abs((1+rad)/(1-rad)-z)/z)
print('   largest residual over z = 1.5..13 (distance, radius, (1+G)/(1-G) = z): %.2e'%e)
print('G2 face = set of points equally far from centre and ball; unit normal N = (sinh h, cosh h u), h = r/2')
e=0
for z in [1.5,3,5,7,13]:
    r=math.log(z);h=r/2;u=AX[1];p=ball(u,r);N=normal(u,h)
    e=max(e,abs(mink(N,N)+1), np.abs((p-O)-2*math.sinh(h)*N).max())
    # random points on the plane: equal distance to O and p
    m=np.array([math.cosh(h),*(math.sinh(h)*u)])
    for _ in range(50):
        a,b=rng.normal(size=2); rho=math.hypot(a,b); t=(a*AX[0]+b*AX[2])/rho
        x=math.cosh(rho)*m+math.sinh(rho)*np.array([0,*t])
        e=max(e,abs(mink(x,N)),abs(mink(x,O)-mink(x,p))/mink(x,O),abs(math.acosh(mink(m,O))-h))
print('   largest residual (N unit, p - O = 2 sinh h N, plane points equidistant, foot at r/2): %.2e'%e)
print('G3 g = <N_a,N_b> = sinh h_a sinh h_b for perpendicular arms; interior angle of the centre cell at the edge = arccos g (g<1)')
e1=0;e2=0;n=0
for _ in range(400):
    ha,hb=rng.uniform(0.05,1.6,2); Na=normal(AX[0],ha);Nb=normal(AX[1],hb); g=math.sinh(ha)*math.sinh(hb)
    e1=max(e1,abs(mink(Na,Nb)-g))
    if g<0.999:
        ta,tb=math.tanh(ha),math.tanh(hb); t=1/math.sqrt(1-ta*ta-tb*tb); q=np.array([t,t*ta,t*tb,0])
        def tang(N,Nother):
            # v in the slice (k-component 0), <v,q>=0, <v,N>=0, Riemannian unit, pointing to the centre side of the other face
            A=np.array([[q[0],-q[1],-q[2]],[N[0],-N[1],-N[2]]]); v3=np.linalg.svd(A)[2][-1]; v=np.array([*v3,0.]); v=v/math.sqrt(-mink(v,v))
            return v if mink(v,Nother)>0 else -v
        va,vb=tang(Na,Nb),tang(Nb,Na); ang=math.acos(max(-1,min(1,-mink(va,vb))))
        e2=max(e2,abs(ang-math.acos(g))); n+=1
print('   <Na,Nb> - sinh sinh: %.2e ; measured interior angle - arccos g on %d crossing pairs: %.2e'%(e1,n,e2))
for (za,zb) in [(3,5),(3,3),(5,5)]:
    g=math.sinh(math.log(za)/2)*math.sinh(math.log(zb)/2); print('   z = %g,%g  g = %.6f  alpha = %.4f deg  360/alpha = %.4f'%(za,zb,g,math.degrees(math.acos(g)),360/math.degrees(math.acos(g))))
print('G4 g > 1: faces stand apart; least distance between the two planes, minimised over both planes (4 parameters), against arccosh g')
def plane_pt(u,h,par,e1,e2):
    m=np.array([math.cosh(h),*(math.sinh(h)*u)]); a,b=par; rho=math.hypot(a,b)
    if rho<1e-300: return m
    t=(a*e1+b*e2)/rho; return math.cosh(rho)*m+math.sinh(rho)*np.array([0,*t])
worst=0;rows=[]
for (za,zb) in [(5,7),(7,7),(7,9),(9,13),(13,13),(6,6),(5.9,5.9)]:
    ha,hb=math.log(za)/2,math.log(zb)/2; g=math.sinh(ha)*math.sinh(hb)
    f=lambda v: mink(plane_pt(AX[0],ha,v[:2],AX[1],AX[2]),plane_pt(AX[1],hb,v[2:],AX[0],AX[2]))
    best=None
    for s in range(12):
        res=minimize(f,rng.normal(scale=1.0,size=4),method='Nelder-Mead',options={'xatol':1e-13,'fatol':1e-15,'maxiter':40000,'maxfev':40000})
        if best is None or res.fun<best.fun: best=res
    dmin=math.acosh(max(1,best.fun)); rows.append((za,zb,g,dmin,math.acosh(g))); worst=max(worst,abs(dmin-math.acosh(g)))
    # opposite: arccosh(g^2) must fail
for r in rows: print('   z = %g,%g  g = %.6f  least distance found = %.9f  arccosh g = %.9f  (arccosh g^2 = %.6f)'%(r[0],r[1],r[2],r[3],r[4],math.acosh(r[2]**2)))
print('   largest |least distance - arccosh g|: %.2e'%worst)
print('   ratio 7 equal steps: cosh delta = sinh^2(ln7/2) = %.12f ; 9/7 = %.12f'%(math.sinh(math.log(7)/2)**2,9/7))
print('G5 the wall: Gamma^2 = 1/2 <=> z = 3 + 2 sqrt 2')
zw=3+2*math.sqrt(2); r=math.log(zw); G=(zw-1)/(zw+1)
print('   z = %.12f  Gamma^2 - 1/2 = %.1e  sinh^2(r/2) - 1 = %.1e  (z-3)^2 - 8 = %.1e  R - T = %.1e  2 - 4 sinh^4 + 2 = %.1e  tanh r - 2sqrt2/3 = %.1e'%(zw,G*G-.5,math.sinh(r/2)**2-1,(zw-3)**2-8,2*G*G-1,2-4*math.sinh(r/2)**4+2,math.tanh(r)-2*math.sqrt(2)/3))
print('   z = 5: Gamma^2 = %.6f (4/9), (5-3)^2 = 4 < 8 ; z = 7: Gamma^2 = %.6f (9/16), (7-3)^2 = 16 > 8'%((4/6)**2,(6/8)**2))
print('G6 right triangle centre, ball I, ball J: cosh d = cosh r_I cosh r_J')
e=0
for _ in range(500):
    ra,rb=rng.uniform(0.05,3,2); pa,pb=boost(AX[0],ra)@O,boost(AX[1],rb)@O; e=max(e,abs(mink(pa,pb)-math.cosh(ra)*math.cosh(rb))/mink(pa,pb))
print('   largest relative residual on 500 pairs: %.2e ; z = 3,5: d = %.4f ; z = 5,5: cosh d = %.6f (169/25 = %.6f)'%(e,math.acosh(math.cosh(math.log(3))*math.cosh(math.log(5))),math.cosh(math.log(5))**2,169/25))
print('G7 Thomas turn of B_a B_b (polar decomposition) = area of that right triangle (angle defect) = 2 arctan(Gamma_a Gamma_b)')
e1=e2=0
def thomas(ra,rb):
    Lam=boost(AX[0],ra)@boost(AX[1],rb); p=Lam@O; n=np.linalg.norm(p[1:]); Li=boost(-p[1:]/n,math.acosh(p[0])); R=Li@Lam
    return math.acos(max(-1,min(1,(np.trace(R[1:,1:])-1)/2))),R
def area(ra,rb):
    pa,pb=ball(AX[0],ra),ball(AX[1],rb); d=math.acosh(mink(pa,pb))
    A=math.acos((math.cosh(ra)*math.cosh(d)-math.cosh(rb))/(math.sinh(ra)*math.sinh(d)))
    B=math.acos((math.cosh(rb)*math.cosh(d)-math.cosh(ra))/(math.sinh(rb)*math.sinh(d)))
    return math.pi-math.pi/2-A-B
for _ in range(500):
    ra,rb=rng.uniform(0.05,3,2); th,_=thomas(ra,rb); f=2*math.atan(math.tanh(ra/2)*math.tanh(rb/2)); e1=max(e1,abs(th-f)); e2=max(e2,abs(area(ra,rb)-f))
print('   polar angle - formula: %.2e ; triangle area - formula: %.2e (500 random pairs)'%(e1,e2))
for z in (5,7):
    th,R=thomas(math.log(z),math.log(z)); print('   z = %d: cos, sin = %.12f, %.12f ; exact %s ; tan(theta/2) = %.12f, Gamma^2 = %.12f ; theta = %.4f deg'%(z,math.cos(th),math.sin(th),'65/97, 72/97 = %.12f, %.12f'%(65/97,72/97) if z==5 else '175/337, 288/337 = %.12f, %.12f'%(175/337,288/337),math.tan(th/2),((z-1)/(z+1))**2,math.degrees(th)))
print('   z = 3,5: theta_T = %.4f deg ; z = 5,7: %.4f deg ; z = 3,7: %.4f deg'%tuple(math.degrees(2*math.atan(math.tanh(math.log(a)/2)*math.tanh(math.log(b)/2))) for a,b in [(3,5),(5,7),(3,7)]))
print('G8 the square W = Ba Bb Ba^-1 Bb^-1 (4x4): g<1 turn with cos phi = 8g^4-8g^2+1; g>1 run 4 arccosh g; equal steps SL2 trace 2-4sinh^4 = comm_trace at v = 2 sinh^2')
e=0
for _ in range(500):
    ra,rb=rng.uniform(0.05,3,2); W=boost(AX[0],ra)@boost(AX[1],rb)@boost(-AX[0],ra)@boost(-AX[1],rb); g=math.sinh(ra/2)*math.sinh(rb/2); half=(np.trace(W)-2)/2
    if g<1-1e-6: e=max(e,abs(half-(8*g**4-8*g*g+1)))
    elif g>1+1e-6: e=max(e,abs(math.acosh(half)-4*math.acosh(g))/(4*math.acosh(g)))
e3=0
for _ in range(200):
    x=rng.uniform(0.05,1.5); s=math.exp(x); v=2*math.sinh(x)**2
    a=np.array([[s,1],[0,1/s]]); b=np.array([[s,0],[-v,1/s]]); tr=np.trace(a@b@np.linalg.inv(a)@np.linalg.inv(b))
    e3=max(e3,abs(tr-(2-v*((s-1/s)**2-v)))/abs(tr-2+1), abs(tr-(2-4*math.sinh(x)**4))/(1+abs(tr)))
print('   turn/run residual on 500 pairs: %.2e ; Riley form at v = 2 sinh^2 against 2 - 4 sinh^4 (200 cases): %.2e'%(e,e3))
g5=math.sinh(math.log(5)/2)**2; print('   z = 5: g = %.6f, cos phi = %.9f (Two Trees Thm 5.4: -527/625 = %.9f)'%(g5,8*g5**4-8*g5*g5+1,-527/625))
print('G9 incidence in the ball: centre ray at angle psi to the arm meets the face at h with sin theta = cosh h sin psi; meets it only if cos psi >= tanh h')
e=0;miss=0
for _ in range(2000):
    h=rng.uniform(0.05,1.5); psi=rng.uniform(0,math.pi/2); N=normal(AX[0],h); v=np.array([0,math.cos(psi),math.sin(psi),0])
    A,B=mink(O,N),mink(v,N); q=-A/B
    if q<1 and q>0:
        s=math.atanh(q); tan_=math.sinh(s)*O+math.cosh(s)*v; c=abs(mink(tan_,N)); e=max(e,abs(math.sqrt(1-c*c)-math.cosh(h)*math.sin(psi)))
        if math.cos(psi)<math.tanh(h): miss+=1
    else:
        if math.cos(psi)>math.tanh(h)+1e-12: miss+=1
print('   largest |sin theta - cosh h sin psi|: %.2e ; cases against the meeting rule: %d'%(e,miss))
print('G10 card witnesses: B30 50 deg in R=1 -> R=4: theta2 = %.4f deg ; B39 R=4->1: critical = %.4f deg ; with kappa = z^2, theta_crit = arcsin(1/z): z=3 %.4f, z=5 %.4f, z=7 %.4f deg'%(math.degrees(math.asin(math.sin(math.radians(50))/2)),math.degrees(math.asin(math.sqrt(1/4))),*[math.degrees(math.asin(1/z)) for z in (3,5,7)]))
print('G11 pressure algebra: P = 2R, K = 1/(T-R) = 1/(1-P), sinh^2(r/2) = R/T')
e=0
for z in np.exp(rng.uniform(0.05,3,500)):
    G=(z-1)/(z+1);R=G*G;T=1-R; e=max(e,abs(math.sinh(math.log(z)/2)**2-R/T)/(R/T),abs(1/(T-R)-1/(1-2*R))/abs(1/(T-R)) if abs(T-R)>1e-6 else 0)
print('   largest relative residual: %.2e ; z = 3,5,7: P = %.6f, %.6f, %.6f ; P = 1 exactly at the wall'%(e,2*(2/4)**2,2*(4/6)**2,2*(6/8)**2))
print('G12 rim: aberration cos psi\' = cos psi (+) tanh r; frequency ratio t\'/t = cosh r + sinh r cos psi (= z on the axis, 1/z against it); face shadow cos psi0 = Gamma')
e=0
for _ in range(2000):
    r=rng.uniform(0,3); c=rng.uniform(-1,1); s=math.sqrt(1-c*c); n=np.array([1,c,s,0]); m=boost(AX[0],r)@n
    e=max(e,abs(m[1]/m[0]-(c+math.tanh(r))/(1+c*math.tanh(r))),abs(m[0]-(math.cosh(r)+math.sinh(r)*c)),abs(mink(m,m)))
    h=r/2; cc=math.tanh(h); e=max(e,abs(mink(np.array([1,cc,math.sqrt(1-cc*cc),0]),normal(AX[0],h))))
print('   largest residual: %.2e'%e)
for z in (3,5,7): print('   z = %d: forward factor %.6f, backward factor %.6f (1/z = %.6f), time-dilation factor cosh r = %.6f, mirror at speed Gamma two-way: (1+G)/(1-G) = %.6f, one-way sqrt = %.6f'%(z,math.cosh(math.log(z))+math.sinh(math.log(z)),math.cosh(math.log(z))-math.sinh(math.log(z)),1/z,math.cosh(math.log(z)),(1+(z-1)/(z+1))/(1-(z-1)/(z+1)),math.sqrt(z)))
# ping-pong threshold from the aberration law
def pp(z,N=100000):
    r=math.log(z); v=rng.normal(size=(N,3)); v/=np.linalg.norm(v,axis=1)[:,None]; ex=0
    for k in range(3):
        for sg in (1,-1):
            c=sg*v[:,k]; out=~(-c>1/math.sqrt(2)); c2=(c+math.tanh(r))/(1+c*math.tanh(r)); ex+=int(np.sum(out&~(c2>1/math.sqrt(2))))
    return ex
print('   ping-pong exceptions in 1e5 directions x 6 steps: z = 5: %d ; z = wall(1+1e-6): %d ; z = 7: %d ; z = 13: %d'%(pp(5),pp(zw*(1+1e-6)),pp(7),pp(13)))
m=np.array([25*3+24*1,24*3+25*1,7*2,7*2]); print('   z = 7 integer step of (3,1,2,2): %s, null: %s, in cap of +i (t^2 < 2 x^2): %s'%(m.tolist(),m[0]**2==m[1]**2+m[2]**2+m[3]**2,m[0]**2<2*m[1]**2))

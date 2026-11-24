# SCRIPT: TWIN-PROOF-EXACT-WIGNER-01
# Purpose: confirm, at 160 working digits (>=50 kept), the EXACT one-step formulas derived in REPORT.md Step 1:
#  (E1) Boost(d n) Boost(r w) = Boost(d' n') W   with W the rotation by angle eps about axis (w x n)/|w x n|, where
#       tan(eps/2) = sin(th) / ( coth(d/2) coth(r/2) + cos(th) ),  th = angle(n, w)
#  (E2) cosh d' = cosh d cosh r + sinh d sinh r cos(th)
#  (E3) sinh d' n' = (sinh d cosh r + (cosh d - 1) sinh r cos(th)) n + sinh r w
#  (E4) body-frame reduction: Y_n := L_n^T e0 = (cosh d_n, sinh d_n u_n) obeys Y_n = B(e_s, r) Y_{n-1}  (frame-free)
#  (E5) body increment: R_n = R_{n-1} exp(hat nu_n), nu_n = eps_n (e_s x u_{n-1})/|e_s x u_{n-1}| with eps from (E1)
#       using th = angle(u_{n-1}, e_s)
#  (E6) first and second order: eps = r tanh(d/2) sin th - (r^2/2) tanh(d/2)^2 sin th cos th + O(r^3)
# KILL CONDITIONS (written before the run):
#  K1: if any of E1-E5 disagrees with direct 4x4 matrix algebra by more than 1e-45 (relative) on 300 random cases
#      with d in (0,12), r in (0,6) (large r included on purpose), the exact formula is wrong -> Step 1 dies.
#  K2: if the axis sign comes out as (n x w) instead of (w x n) in more than 0 cases, the stated sign is wrong.
#  K3: if the E6 remainder divided by r^3 is not bounded (ratio at r=1e-6 vs r=1e-4 differs by >10%), E6 is wrong.
import mpmath as mp, random
mp.mp.dps = 160   # chain reaches d~60, polar split loses ~2d/ln10 digits; 160 keeps >50 digits
random.seed(7)
def unit(v):
    n = mp.sqrt(sum(x*x for x in v)); return [x/n for x in v]
def cross(a,b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def boost(n, d):
    B = mp.eye(4); c, s = mp.cosh(d), mp.sinh(d)
    B[0,0] = c
    for i in range(3):
        B[0,i+1] = B[i+1,0] = s*n[i]
        for j in range(3):
            B[i+1,j+1] = (1 if i==j else 0) + (c-1)*n[i]*n[j]
    return B
def polar(L):
    g = L[0,0]; d = mp.acosh(g); sh = mp.sinh(d); n = [L[i,0]/sh for i in range(1,4)]
    R = mp.inverse(boost(n, d))*L
    return d, n, R
def rot(axis, ang):
    a = unit(axis); c, s = mp.cos(ang), mp.sin(ang); R = mp.eye(4)
    K = [[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]]
    for i in range(3):
        for j in range(3):
            R[i+1,j+1] = c*(1 if i==j else 0) + s*K[i][j] + (1-c)*a[i]*a[j]
    return R
def mnorm(M): return max(abs(M[i,j]) for i in range(M.rows) for j in range(M.cols))
def randunit(): return unit([mp.mpf(random.gauss(0,1)) for _ in range(3)])
worst = {'E1':0,'E2':0,'E3':0,'E4':0,'E5':0}; badsign = 0
for trial in range(300):
    n = randunit(); w = randunit(); d = mp.mpf(random.uniform(0.01,12)); r = mp.mpf(random.uniform(0.001,6))
    M = boost(n,d)*boost(w,r); d2, n2, W = polar(M)
    cth = dot(n,w); sth = mp.sqrt(1-cth*cth)
    eps = 2*mp.atan(sth/(mp.coth(d/2)*mp.coth(r/2)+cth))
    Wp = rot(cross(w,n), eps); Wm = rot(cross(n,w), eps)
    e1 = mnorm(W-Wp); worst['E1'] = max(worst['E1'], e1)
    if mnorm(W-Wm) < e1: badsign += 1
    worst['E2'] = max(worst['E2'], abs(mp.cosh(d2) - (mp.cosh(d)*mp.cosh(r)+mp.sinh(d)*mp.sinh(r)*cth))/mp.cosh(d2))
    pred = [(mp.sinh(d)*mp.cosh(r)+(mp.cosh(d)-1)*mp.sinh(r)*cth)*n[i] + mp.sinh(r)*w[i] for i in range(3)]
    worst['E3'] = max(worst['E3'], max(abs(mp.sinh(d2)*n2[i]-pred[i]) for i in range(3))/mp.sinh(d2))
# E4, E5 along a random chain of axis boosts with a general starting frame
E = [[1,0,0],[0,1,0],[0,0,1]]
L = boost(randunit(), mp.mpf('0.7'))*rot(randunit(), mp.mpf('1.1'))
d0, n0, R0 = polar(L)
Y = L.T*mp.matrix([1,0,0,0]); Rb = R0
for step in range(60):
    s = random.randrange(3); r = mp.mpf(random.uniform(0.001, 2.5))
    dprev = mp.acosh(Y[0]); uprev = [Y[i]/mp.sinh(dprev) for i in range(1,4)]
    L = L*boost(E[s], r); Y = boost(E[s], r)*Y
    d, n, R = polar(L)
    Ydirect = L.T*mp.matrix([1,0,0,0])
    worst['E4'] = max(worst['E4'], mnorm(Ydirect-Y)/Y[0])
    cth = uprev[s]; sth = mp.sqrt(1-cth*cth)
    eps = 2*mp.atan(sth/(mp.coth(dprev/2)*mp.coth(r/2)+cth))
    Rb = Rb*rot(cross(E[s], uprev), eps)
    worst['E5'] = max(worst['E5'], mnorm(Rb-R))
for k,v in worst.items(): print('%s worst error = %s' % (k, mp.nstr(v, 5)))
print('axis-sign: cases where (n x w) fits better than (w x n):', badsign)
print('K1', 'PASS' if max(worst.values()) < mp.mpf('1e-45') else 'KILL', ' K2', 'PASS' if badsign == 0 else 'KILL')
# E6 expansion check
d = mp.mpf(3); th = mp.mpf('0.9')
for r in (mp.mpf('1e-4'), mp.mpf('1e-6')):
    eps = 2*mp.atan(mp.sin(th)/(mp.coth(d/2)*mp.coth(r/2)+mp.cos(th)))
    t = mp.tanh(d/2); approx = r*t*mp.sin(th) - r*r/2*t*t*mp.sin(th)*mp.cos(th)
    print('E6 r=%s: (eps - 2nd order)/r^3 = %s' % (mp.nstr(r,2), mp.nstr((eps-approx)/r**3, 12)))

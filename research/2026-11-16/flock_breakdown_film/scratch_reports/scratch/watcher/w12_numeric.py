# SCRIPT: W12-NUMERIC (watcher) independent re-runs of numerical claims in L1, L2, L3. numpy/scipy only; nothing imported from the lineage scripts.
import numpy as np, itertools
from scipy.optimize import minimize
rng = np.random.default_rng(12345)
print('=== L1 ===')
# N1: evanescent slab by TRANSFER MATRIX (method differs from the lineage's three-region matching).
# slab: u'' = k^2 u, flux j = -(i ke / k) u'. M = [[cosh kd, i sinh kd/ke],[-i ke sinh kd, cosh kd]] maps (u,j)(0)->(u,j)(d). Outer media real admittance Y1.
worst_t = worst_r = worst_sech = 0
for _ in range(3000):
    Y1, ke, k, d = 0.1+3*rng.random(), 0.1+3*rng.random(), 0.1+2*rng.random(), 3*rng.random()
    c, s = np.cosh(k*d), np.sinh(k*d)
    M = np.array([[c, 1j*s/ke],[-1j*ke*s, c]])
    # unknown (r,t): M @ [1+r, Y1(1-r)] = [t, Y1 t]
    A = np.array([[M[0,0]-M[0,1]*Y1*0, 0]])  # placeholder to keep shape explicit
    # solve linear system: unknowns r,t
    lhs = np.array([[M[0,0]-M[0,1]*Y1, -1],[M[1,0]-M[1,1]*Y1, -Y1]], dtype=complex)  # row: M[:,0]*(1)+M[:,0]*r + M[:,1]*Y1 - M[:,1]*Y1*r ...
    # build properly: M00(1+r)+M01*Y1(1-r)=t ; M10(1+r)+M11*Y1(1-r)=Y1 t
    lhs = np.array([[M[0,0]-M[0,1]*Y1, -1],[M[1,0]-M[1,1]*Y1, -Y1]], dtype=complex)
    rhs = -np.array([M[0,0]+M[0,1]*Y1, M[1,0]+M[1,1]*Y1], dtype=complex)
    r, t = np.linalg.solve(lhs, rhs)
    r0 = (Y1-1j*ke)/(Y1+1j*ke); phi = np.angle(r0); s2 = np.sin(phi)**2; sh2 = s**2
    worst_t = max(worst_t, abs(abs(t)**2 - s2/(sh2+s2))); worst_r = max(worst_r, abs(abs(r)**2 - sh2/(sh2+s2)))
print('N1 slab transfer matrix vs |t|^2 = sin^2phi/(sinh^2 kd + sin^2phi): worst %.2e ; |r|^2 form worst %.2e ; (tol 1e-11)' % (worst_t, worst_r))
w = 0
for _ in range(2000):
    Y1, kd = 0.1+3*rng.random(), 4*rng.random(); ke = Y1; c, s = np.cosh(kd), np.sinh(kd)
    M = np.array([[c, 1j*s/ke],[-1j*ke*s, c]]); lhs = np.array([[M[0,0]-M[0,1]*Y1, -1],[M[1,0]-M[1,1]*Y1, -Y1]], dtype=complex); rhs = -np.array([M[0,0]+M[0,1]*Y1, M[1,0]+M[1,1]*Y1], dtype=complex)
    r, t = np.linalg.solve(lhs, rhs); w = max(w, abs(abs(t)-1/c), abs(abs(r)-np.tanh(kd)), abs(r - (-1j)*np.tanh(kd)))
print('N1b phi=pi/2 (ke=Y1): |t|=sech kd, |r|=tanh kd, r=-i tanh kd: worst %.2e' % w)
# N2: K4 first-pass numbers from the closed form alone, and sech(arccosh g)=1/g
for za, zb in [(5,7),(7,9),(9,13)]:
    ga, gb = (za-1)/(za+1), (zb-1)/(zb+1); g = np.sinh(np.log(za)/2)*np.sinh(np.log(zb)/2); dl = np.arccosh(g)
    print('N2 z=%d,%d g=%.6f delta=%.6f first pass=%.10f  (1/g^2 gap pass %.10f, sech^2 %.10f)' % (za, zb, g, dl, (1-ga**2)*(1-gb**2)/np.cosh(dl)**2, 1/g**2, 1/np.cosh(dl)**2))
# N3: zero-phase cascade by transfer matrices T=(1/tau)[[1,rho],[rho,1]]; total back-reflection = T10/T00 must equal tanh(ra/2+delta-rb/2); total transmission 1/T00 = sech(...)
za, zb = 7, 9; ra, rb = np.log(za), np.log(zb); dl = np.arccosh(np.sinh(ra/2)*np.sinh(rb/2))
def T(rho): tau = np.sqrt(1-rho**2); return np.array([[1, rho],[rho, 1]])/tau
Tt = T(np.tanh(ra/2)) @ T(np.tanh(dl)) @ T(-np.tanh(rb/2))
print('N3 cascade (7,9): R_total %.10f vs tanh(ra/2+d-rb/2) %.10f ; T_total %.10f vs sech %.10f' % (Tt[1,0]/Tt[0,0], np.tanh(ra/2+dl-rb/2), 1/Tt[0,0], 1/np.cosh(ra/2+dl-rb/2)))
Tt2 = T(np.tanh(ra/2)) @ T(-np.tanh(rb/2)); print('N3b no gap: R_total %.10f vs (za-zb)/(za+zb) %.10f' % (Tt2[1,0]/Tt2[0,0], (za-zb)/(za+zb)))

print('=== L2 ===')
eta = np.diag([1.,-1,-1,-1])
def boost(u, r):
    u = np.array(u, float); B = np.eye(4); B[0,0] = np.cosh(r); B[0,1:] = np.sinh(r)*u; B[1:,0] = np.sinh(r)*u; B[1:,1:] += (np.cosh(r)-1)*np.outer(u,u); return B
# N4: distance between the two face planes by direct minimisation on the hyperboloid (formula g never used inside the search)
def normal(r, u):  # unit spacelike normal of the plane equidistant from O and B(u,r)O :  N=(sinh h, cosh h u)
    h = r/2; return np.concatenate([[np.sinh(h)], np.cosh(h)*np.array(u)])
def dist_planes(za, zb):
    ra, rb = np.log(za), np.log(zb); Na, Nb = normal(ra,[1,0,0]), normal(rb,[0,1,0])
    def pt(N, ab):  # point on hyperboloid with <p,N>=0: build orthonormal basis of N-perp (Minkowski), p = cosh s e0 + sinh s dir  using two free params
        # basis of the 3-dim Minkowski orthogonal complement of N via Gram-Schmidt in the metric eta
        basis=[]; vecs=[np.array(v,float) for v in np.eye(4)]
        for v in vecs:
            w = v - (v@eta@N)/(N@eta@N)*N
            for b in basis: w = w - (w@eta@b)/(b@eta@b)*b
            if abs(w@eta@w) > 1e-9: basis.append(w)
        basis = basis[:3]; tm = [b for b in basis if b@eta@b > 0][0]; sp = [b for b in basis if b@eta@b < 0]
        tm = tm/np.sqrt(tm@eta@tm); sp = [s/np.sqrt(-(s@eta@s)) for s in sp]
        a1, a2 = ab; v = a1*sp[0] + a2*sp[1]; n = np.sqrt(-(v@eta@v)); return np.cosh(n)*tm + (np.sinh(n)/n*v if n>1e-12 else v)
    best = 1e9
    for _ in range(12):
        x0 = rng.normal(size=4)*1.5
        f = lambda x: np.arccosh(max(1.0, pt(Na, x[:2])@eta@pt(Nb, x[2:])))
        res = minimize(f, x0, method='Nelder-Mead', options={'xatol':1e-10,'fatol':1e-13,'maxiter':4000}); best = min(best, res.fun)
    return best, np.arccosh(np.sinh(ra/2)*np.sinh(rb/2))
for za, zb in [(5,7),(7,9),(9,13),(7,7)]:
    d, a = dist_planes(za, zb); print('N4 z=%d,%d least distance between the two face planes %.9f  arccosh g %.9f  diff %.1e' % (za, zb, d, a, abs(d-a)))
# N5: Thomas turn from the 4x4 product Ba Bb (polar decomposition) and triangle area, and the two closed forms
def thomas_angle(ra, rb):
    P = boost([1,0,0], ra) @ boost([0,1,0], rb); S = P[0,0]; # polar: P = L R, L symmetric pure boost. L = (P P^T)^(1/2) in Euclidean sense for a Lorentz matrix with R rotation: P P^T = L^2
    w, V = np.linalg.eigh(P@P.T); L = V@np.diag(np.sqrt(w))@V.T; R = np.linalg.inv(L)@P
    return np.arccos(np.clip((np.trace(R[1:,1:])-1)/2,-1,1)), R
for za, zb in [(5,5),(7,7),(3,5),(5,7),(3,7)]:
    ra, rb = np.log(za), np.log(zb); th, R = thomas_angle(ra, rb)
    Ga, Gb = np.tanh(ra/2), np.tanh(rb/2)
    # triangle: right angle at O; sides ra (O-A), rb (O-B), hypotenuse cosh d = cosh ra cosh rb. area = pi - sum of angles
    d = np.arccosh(np.cosh(ra)*np.cosh(rb)); ang = lambda a,b,c: np.arccos((np.cosh(a)*np.cosh(b)-np.cosh(c))/(np.sinh(a)*np.sinh(b)))
    area = np.pi - (np.pi/2 + ang(ra,d,rb) + ang(rb,d,ra))
    print('N5 z=%d,%d polar angle %.10f  triangle area %.10f  2atan(GaGb) %.10f   (deg %.4f)  tan(th/2)=%.6f' % (za, zb, th, area, 2*np.arctan(Ga*Gb), np.degrees(th), np.tan(th/2)))
th5,_ = thomas_angle(np.log(5), np.log(5)); print('N5b z=5 cos,sin = %.12f %.12f ; 65/97, 72/97 = %.12f %.12f' % (np.cos(th5), np.sin(th5), 65/97, 72/97))
# N6: the square at z=5: commutator trace, cos(phi)
A_, B_ = boost([1,0,0], np.log(5)), boost([0,1,0], np.log(5)); W = A_@B_@np.linalg.inv(A_)@np.linalg.inv(B_)
print('N6 z=5 commutator Lorentz trace %.10f => cos phi %.10f ; -527/625 = %.10f ; 8g^4-8g^2+1 (g=.8) = %.10f' % (np.trace(W), (np.trace(W)-2)/2, -527/625, 8*.8**4-8*.8**2+1))
z = 3+2*np.sqrt(2); print('N6b wall: Gamma^2 = %.12f, sinh^2(r/2)=%.12f, g = %.12f' % (np.tanh(np.log(z)/2)**2, np.sinh(np.log(z)/2)**2, np.sinh(np.log(z)/2)**2))
print('N6c refraction 50deg R1=1 -> R2=4 (sin2 kept: sin t2 = sin t1 *sqrt(R1/R2)): %.4f deg' % np.degrees(np.arcsin(np.sin(np.radians(50))/2)))

print('=== L3 ===')
sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
def rsu2():
    q = rng.normal(size=4); q /= np.linalg.norm(q); return q[0]*np.eye(2) - 1j*(q[1]*sig[0]+q[2]*sig[1]+q[3]*sig[2])
def conn_test(n, edges, weights=None, mode='skew'):
    ds = [rng.normal(size=3) for _ in range(n)]; D = [sum(x*s for x,s in zip(d,sig)) for d in ds]
    H = np.zeros((2*n,2*n),complex); lhs_e = 0
    U = {}; 
    for (i,j),wgt in zip(edges, weights or [1]*len(edges)):
        u = rsu2(); U[(i,j)] = u; c = np.sqrt(wgt)
        H[2*i:2*i+2, 2*j:2*j+2] = c*u; H[2*j:2*j+2, 2*i:2*i+2] = -c*u.conj().T   # skew-hermitian off-block (A* = -A)
        lhs_e += wgt*np.linalg.norm(D[i] - u@D[j]@u.conj().T)**2
    for i in range(n): H[2*i:2*i+2, 2*i:2*i+2] = D[i]
    C = H@H.conj().T - H.conj().T@H
    return np.linalg.norm(C)**2/8, lhs_e
w = 0
for _ in range(300):
    n = 7; edges = [(i,j) for i in range(n) for j in range(i+1,n) if rng.random()<0.5] or [(0,1)]
    wts = list(rng.random(len(edges))+0.1); a, b = conn_test(n, edges, wts); w = max(w, abs(a-b)/b)
print('N7 (1/8)||[H,H*]||^2 = sum_edges w ||D_i - U D_j U^dag||^2 with random Hermitian traceless blocks, random SU(2), random graphs, weights: worst rel %.2e' % w)
# Hermitian companion: H_h = D + hop (hop_ji = hop_ij^dag) is normal? and K = D + i*hop has the identity with w=c^2
n=3; ds=[rng.normal(size=3) for _ in range(n)]; D=[sum(x*s for x,s in zip(d,sig)) for d in ds]; Hh=np.zeros((6,6),complex); K=np.zeros((6,6),complex); edges=[(0,1),(0,2),(1,2)]; cs=[0.4,0.3,0.2]; rhs=0
for (i,j),c in zip(edges,cs):
    u=rsu2(); Hh[2*i:2*i+2,2*j:2*j+2]=c*u; Hh[2*j:2*j+2,2*i:2*i+2]=c*u.conj().T; K[2*i:2*i+2,2*j:2*j+2]=1j*c*u; K[2*j:2*j+2,2*i:2*i+2]=1j*c*u.conj().T; rhs+=c**2*np.linalg.norm(D[i]-u@D[j]@u.conj().T)**2
for i in range(n): Hh[2*i:2*i+2,2*i:2*i+2]=D[i]; K[2*i:2*i+2,2*i:2*i+2]=D[i]
cm=lambda X: np.linalg.norm(X@X.conj().T-X.conj().T@X)**2/8
print('N7b Hermitian hop matrix: ||[H,H*]||^2/8 = %.2e (Hermitian => 0) ; K=D+i*hop: %.12f vs sum c^2||D_i-U D_j U^dag||^2 = %.12f' % (cm(Hh), cm(K), rhs))
# hmm: D here is the sum of d.sigma blocks; Hh with D blocks is Hermitian only if hop is Hermitian: yes.
# N8: Flock rest connection energy forced by clocks: 2*sum_links (|d_i|-|d_j|)^2, |d| = omega*rate/2 = rate (omega=2); rates 1,1/3,1/5 ; and the inequality ||D_i - U D_j U^dag||^2 >= 2(|d_i|-|d_j|)^2
rates=[1,1/3,1/5]; print('N8 2*sum over the 3 links (|di|-|dj|)^2 = %.9f  (L3 table: 2.204444444)' % (2*sum((rates[i]-rates[j])**2 for i,j in [(0,1),(0,2),(1,2)])))
worst=1e9
for _ in range(20000):
    a,b=rng.normal(size=3),rng.normal(size=3); u=rsu2(); Da=sum(x*s for x,s in zip(a,sig)); Db=sum(x*s for x,s in zip(b,sig)); worst=min(worst, np.linalg.norm(Da-u@Db@u.conj().T)**2 - 2*(np.linalg.norm(a)-np.linalg.norm(b))**2)
print('N8b min over 20000 of ||D_i-UD_jU^dag||^2 - 2(|d_i|-|d_j|)^2 = %.3e (must be >= 0)' % worst)
# triangle holonomy numbers
for r1,r2 in [(np.log(3),np.log(5)),(1.0986122887,1.9125468038)]:
    print('N9 2*atan(tanh(r1/2)tanh(r2/2)) for (%.10f,%.10f) = %.10f' % (r1,r2,2*np.arctan(np.tanh(r1/2)*np.tanh(r2/2))))
# N10: offset speed limit tau'^2 <= 4 g S on random driven projector families (dimension 6, rank 2 or 3, ball block m=2)
def proj(P0, Hm, t):
    w,V = np.linalg.eigh(Hm); Ut = V@np.diag(np.exp(-1j*w*t))@V.conj().T; return Ut@P0@Ut.conj().T
worst = 0; cnt=0
for _ in range(500):
    n, k = 6, int(rng.integers(2,4)); X = rng.normal(size=(n,k))+1j*rng.normal(size=(n,k)); Q,_ = np.linalg.qr(X); P0 = Q@Q.conj().T
    Hm = rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); Hm = (Hm+Hm.conj().T)/2
    E = np.zeros((n,2)); E[0,0]=1; E[1,1]=1   # embedding of a 2-component ball
    t=0.37; e=1e-6
    def tau(t):
        P=proj(P0,Hm,t); C=E.T@P@E; I=np.eye(2); return np.log(np.linalg.det(I-C).real)-np.log(np.linalg.det(C).real)
    P=proj(P0,Hm,t); C=(E.T@P@E); w_=np.linalg.eigvalsh(C)
    if w_.min()<1e-6 or w_.max()>1-1e-6: continue
    td=(tau(t+e)-tau(t-e))/(2*e); Pd=-1j*(Hm@P-P@Hm); g=0.5*np.linalg.norm(Pd)**2; S=np.trace(np.linalg.inv(C@(np.eye(2)-C))).real
    worst=max(worst, td**2/(4*g*S)); cnt+=1
print('N10 offset speed limit: largest tau-dot^2/(4 g S) over %d random cases = %.4f (must be <= 1)' % (cnt, worst))

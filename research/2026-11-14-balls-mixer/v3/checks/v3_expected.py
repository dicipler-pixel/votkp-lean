# SCRIPT: BALLS-MIXER-V3-EXPECTED-01
# Why this decides it: each new eye of mixer v3 shows a number two ways: from the 4x4 boost matrices themselves
# (what the page multiplies out) and from a closed formula. Here the same two routes are computed away from the
# page in 50-digit arithmetic. If a formula is wrong, the two routes differ and the eye is not built.
# KILL LINES (written before the run):
#  K1 Thomas turn: angle of the rotation left over from B_a(r1) B_b(r2), a perpendicular to b, against
#     2 atan(G1 G2); kill if any of 7 pairs differs by more than 1e-30. Reversed order must give the same
#     angle about the opposite axis; kill if the axis does not flip.
#  K2 level shells: n straight steps reach ball radius (z^n-1)/(z^n+1); kill above 1e-30.
#  K3 same tree from every ball: move the depth-4 tree back one step; its nodes within 3 edges of the new
#     centre must be the depth-3 tree as a point set; kill if any point is off by more than 1e-25.
#  K4 fixed point of the equal-step square: tanh^2(rho/2) against (1-s)/(1+s), s = sqrt(1-2G^2); kill above 1e-30.
#  K5 return counts at z=5: first n with the centre carried back within 0.1, 0.01, 0.001 of its start;
#     kill if they are not 83, 1345, 7594 (the Two Trees appendix values).
#  K6 chain: 3802 twin starts from 11 below 400000; table of path length and distance for the page to match.
from mpmath import mp, mpf, cosh, sinh, log, atan, acosh, acos, sqrt, tanh, matrix, eye
import itertools, json
mp.dps = 50
U = [[1,0,0],[0,1,0],[0,0,1]]
def boost(u, r):
    c, s = cosh(r), sinh(r); B = matrix(4,4); B[0,0] = c
    for i in range(3):
        B[0,i+1] = s*u[i]; B[i+1,0] = s*u[i]
        for j in range(3): B[i+1,j+1] = (1 if i==j else 0) + (c-1)*u[i]*u[j]
    return B
O = matrix([1,0,0,0])
def G(z): return (mpf(z)-1)/(mpf(z)+1)
out = {}
# K1
worst = 0; flips = True; rows = []
for z1, z2 in [(2,2),(3,3),(5,5),(7,7),(3,5),(5,7),(2,9)]:
    res = []
    for order in (0,1):
        A = boost(U[0], log(z1))*boost(U[1], log(z2)) if order==0 else boost(U[1], log(z2))*boost(U[0], log(z1))
        p = A*O; rap = acosh(p[0]); n = [p[i+1]/sinh(rap) for i in range(3)]
        R = boost([-x for x in n], rap)*A
        th = acos((R[1,1]+R[2,2]+R[3,3]-1)/2); axis_k = (R[2,1]-R[1,2])/(2*mp.sin(th))
        res.append((th, axis_k, abs(R[0,0]-1)))
    f = 2*atan(G(z1)*G(z2)); worst = max(worst, abs(res[0][0]-f), abs(res[1][0]-f)); flips &= (res[0][1]*res[1][1] < 0)
    rows.append((z1, z2, float(f*180/mp.pi), float(res[0][1]), float(res[1][1])))
out['K1'] = dict(worst=float(worst), flips=bool(flips), rows=rows)
print('K1 worst', mp.nstr(worst,5), 'axis flips', flips, 'KILL' if worst > mpf(10)**-30 or not flips else 'not hit'); [print('  ', r) for r in rows]
# K2
worst = 0
for z in (2,3,5,7):
    M = eye(4)
    for n in range(1,6):
        M = M*boost(U[0], log(z)); p = M*O; worst = max(worst, abs(p[1]/(1+p[0]) - (mpf(z)**n-1)/(mpf(z)**n+1)))
print('K2 worst', mp.nstr(worst,5), 'KILL' if worst > mpf(10)**-30 else 'not hit'); out['K2'] = float(worst)
# K3
def nodes(z, D):
    gens = []
    for a in range(3): gens += [boost(U[a], log(z)), boost([-x for x in U[a]], log(z))]
    res = [(eye(4), -1, 0)]; fr = res[:]
    for d in range(1, D+1):
        nx = []
        for (M, last, _) in fr:
            for k in range(6):
                if last >= 0 and (k ^ 1) == last: continue
                nx.append((M*gens[k], k, d))
        res += nx; fr = nx
    return res, gens
worst = 0
for z in (5, 7):
    t4, gens = nodes(z, 4); t3, _ = nodes(z, 3)
    back = boost([-1,0,0], log(z))            # stand on the +i neighbour
    key = lambda p: tuple(int(mp.nint(p[i]/(1+p[0])*mpf(10)**20)) for i in (1,2,3))
    moved = {key(back*(M*O)): back*(M*O) for (M,l,d) in t4}
    for (M,l,d) in t3:
        p = M*O; k = key(p)
        if k not in moved: worst = mpf(1); continue
        q = moved[k]; worst = max(worst, max(abs(p[i]-q[i]) for i in range(4))/p[0])
    print('  z', z, 'depth-4 nodes', len(t4), 'depth-3 nodes', len(t3))
print('K3 worst', mp.nstr(worst,5), 'KILL' if worst > mpf(10)**-25 else 'not hit'); out['K3'] = float(worst)
# K4
worst = 0; rows = []
for z in (2, 3, 4, 5, mpf('5.5')):
    r = log(z); C = boost(U[0], r)*boost(U[1], r)*boost([-1,0,0], r)*boost([0,-1,0], r)
    # fixed point in the (t,i,j) block: null vector of C - 1
    W = matrix(3,3)
    for a,i in enumerate((0,1,2)):
        for b,j in enumerate((0,1,2)): W[a,b] = C[i,j] - (1 if i==j else 0)
    cr = lambda x,y: [x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]]
    q = cr([W[0,0],W[0,1],W[0,2]], [W[1,0],W[1,1],W[1,2]]); n2 = q[0]**2-q[1]**2-q[2]**2; q = [x/sqrt(n2) for x in q]
    if q[0] < 0: q = [-x for x in q]
    rho = acosh(q[0]); s = sqrt(1-2*G(z)**2); d = abs(tanh(rho/2)**2 - (1-s)/(1+s)); worst = max(worst, d); rows.append((float(z), float(rho), float(q[0])))
print('K4 worst', mp.nstr(worst,5), 'KILL' if worst > mpf(10)**-30 else 'not hit'); [print('  z, rho, cosh rho', r) for r in rows]; out['K4'] = rows
# K5
r = log(5); C = boost(U[0], r)*boost(U[1], r)*boost([-1,0,0], r)*boost([0,-1,0], r); x = O; got = {}
for n in range(1, 8001):
    x = C*x; d = acosh(x[0]) if x[0] > 1 else mpf(0)
    for tol in ('0.1','0.01','0.001'):
        if tol not in got and d < mpf(tol): got[tol] = n
print('K5', got, 'KILL' if got != {'0.1':83,'0.01':1345,'0.001':7594} else 'not hit'); out['K5'] = got
# K6
N = 400000; sv = bytearray([1])*(N+3); sv[0] = sv[1] = 0
for i in range(2, int(N**0.5)+2):
    if sv[i]: sv[i*i::i] = bytearray(len(sv[i*i::i]))
TW = [a for a in range(11, N) if sv[a] and sv[a+2]]
ax = {1:0, 7:1, 9:2}
mp.dps = 30; Gm = eye(4); tab = {}
for j in range(2400):
    if j+1 in (2, 10, 100, 1000, 2400):
        p = Gm*O; tab[j+1] = (TW[j], float(log(mpf(TW[j])/11)), float(acosh(p[0])) if p[0] > 1 else 0.0)
    Gm = Gm*boost(U[ax[TW[j+1] % 10]], log(mpf(TW[j+1])/TW[j]))
print('K6 twin starts', len(TW), 'KILL' if len(TW) != 3802 else 'not hit'); [print('  n, a, path ln(a/11), distance', k, v) for k, v in tab.items()]
out['K6'] = tab; json.dump(out, open('v3_expected.json','w'), indent=1)

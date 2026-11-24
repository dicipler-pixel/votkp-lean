# SCRIPT: GAPS-TOTALS-CHECK-01
# Independent check of the "Gaps and Totals" draft (24 Nov 2026).
# KILL LINES (written before the run):
#  K1 sum rule: |total - N(N-2)| > 1e-5 for any N in 3..7  -> sum rule failed this way
#  K2 per-pair: |norm2 - (1/mi+1/mj-d^2)| > 1e-5           -> per-pair rule failed this way
#  K3 three bodies: |s1+s2-3| > 1e-5 or |s1*s2 - 12A^2/(xyz)| > 1e-5 -> failed this way
#  K4 cone: gap/delta not -> 3 in every direction, or holonomy not -1 -> cone claim failed this way
#  K5 comparison: squared-distance map run through the same code (no kill; it is the comparison)
import numpy as np
rng = np.random.default_rng(7)

def normalise(q, m):
    q = q - (m[:, None] * q).sum(0) / m.sum()
    return q / np.sqrt((m[:, None] * q * q).sum())

def dist_vec(q, m, squared=False):
    q = normalise(q, m)
    N = len(m); out = []
    for i in range(N):
        for j in range(i + 1, N):
            d2 = ((q[i] - q[j]) ** 2).sum()
            out.append(d2 if squared else np.sqrt(d2))
    return np.array(out)

def jac(q, m, squared=False, h=1e-6):
    N = len(m); f0 = dist_vec(q, m, squared); J = np.zeros((len(f0), N, 2))
    for k in range(N):
        for c in range(2):
            e = np.zeros_like(q); e[k, c] = h
            J[:, k, c] = (dist_vec(q + e, m, squared) - dist_vec(q - e, m, squared)) / (2 * h)
    return J

def gram(q, m, squared=False):
    J = jac(q, m, squared)
    return np.einsum('akc,bkc,k->ab', J, J, 1.0 / m)

print('--- K1 sum rule, equal unit masses')
for N in range(3, 8):
    m = np.ones(N); q = normalise(rng.normal(size=(N, 2)), m)
    tot = np.trace(gram(q, m))
    print('N =', N, ' total =', round(tot, 8), ' N(N-2) =', N * (N - 2))

print('--- K2 per-pair rule, unequal masses')
worst = 0
for N in (3, 4, 6, 8):
    m = rng.uniform(0.5, 3.0, size=N); q = normalise(rng.normal(size=(N, 2)), m)
    K = gram(q, m); d = dist_vec(q, m); a = 0
    for i in range(N):
        for j in range(i + 1, N):
            worst = max(worst, abs(K[a, a] - (1 / m[i] + 1 / m[j] - d[a] ** 2))); a += 1
print('worst per-pair residual =', worst)

print('--- K3 three equal bodies: sum and determinant')
m3 = np.ones(3); worst_s = 0; worst_d = 0
for _ in range(30):
    q = normalise(rng.normal(size=(3, 2)), m3)
    ev = np.sort(np.linalg.eigvalsh(gram(q, m3)))[::-1]
    x, y, z = dist_vec(q, m3, True)
    e1 = q[1] - q[0]; e2 = q[2] - q[0]; A = 0.5 * abs(e1[0] * e2[1] - e1[1] * e2[0])
    worst_s = max(worst_s, abs(ev[0] + ev[1] - 3)); worst_d = max(worst_d, abs(ev[0] * ev[1] - 12 * A * A / (x * y * z)))
print('worst |s1+s2-3| =', worst_s, '  worst |det - 12A^2/xyz| =', worst_d)

def equilateral(m):
    ang = np.array([0, 2 * np.pi / 3, 4 * np.pi / 3])
    return normalise(np.c_[np.cos(ang), np.sin(ang)], m)

def horizontal_basis(q0, m):
    # tangent vectors that are centred, and mass-orthogonal to q0 (dilation) and to the rotation of q0
    N = len(m); rot = np.c_[-q0[:, 1], q0[:, 0]]
    cons = [q0, rot, np.c_[np.ones(N), np.zeros(N)], np.c_[np.zeros(N), np.ones(N)]]
    Cm = np.array([(m[:, None] * c).ravel() for c in cons])
    u, s, vt = np.linalg.svd(Cm); null = vt[len(cons):]
    W = np.sqrt(np.repeat(m, 2))
    qq, _ = np.linalg.qr((null * W).T)          # orthonormal in mass metric
    return [(qq[:, k] / W).reshape(N, 2) for k in range(qq.shape[1])]

def gap_and_top(q, m, squared):
    w, V = np.linalg.eigh(gram(q, m, squared))
    return w[-1] - w[-2], V[:, -1]

for squared, name in ((False, 'DISTANCE map (the draft)'), (True, 'SQUARED-distance map (your August operator)')):
    print('--- K4/K5', name)
    q0 = equilateral(m3); v1, v2 = horizontal_basis(q0, m3)
    for delta in (1e-1, 1e-2, 1e-3):
        row = []
        for phi in (0.0, 0.9, 2.0, 4.1):
            v = np.cos(phi) * v1 + np.sin(phi) * v2
            g, _ = gap_and_top(np.cos(delta) * q0 + np.sin(delta) * v, m3, squared)
            row.append((g / delta, g / delta ** 2))
        print('delta', delta, ' gap/delta:', [round(r[0], 4) for r in row], ' gap/delta^2:', [round(r[1], 3) for r in row])
    for r in (1e-2, 3e-3):
        prev = None; first = None
        for phi in np.linspace(0, 2 * np.pi, 721):
            v = np.cos(phi) * v1 + np.sin(phi) * v2
            _, u = gap_and_top(np.cos(r) * q0 + np.sin(r) * v, m3, squared)
            if prev is not None and np.dot(u, prev) < 0: u = -u
            if first is None: first = u
            prev = u
        print('loop radius', r, ' holonomy =', round(float(np.dot(first, prev)), 6))

print('--- mass breaking: gap of the distance map AT the equilateral shape')
for mm in ((1, 1, 2), (1, 2, 3), (1, 1, 1.1), (1, 1, 1.01)):
    m = np.array(mm, float); g, _ = gap_and_top(equilateral(m), m, False)
    print('masses', mm, ' gap =', round(g, 6))

print('--- near the collinear locus: smaller squared singular value against distance eps')
qc = normalise(np.array([[-1.0, 0], [0.3, 0], [0.7, 0]]), m3); vs = horizontal_basis(qc, m3)
vn = max(vs, key=lambda v: abs(v[:, 1]).sum())   # the direction that leaves the line
for eps in (1e-1, 1e-2, 1e-3):
    for squared in (False, True):
        w = np.sort(np.linalg.eigvalsh(gram(np.cos(eps) * qc + np.sin(eps) * vn, m3, squared)))
        print('eps', eps, 'squared' if squared else 'distance', ' smaller sigma^2 / eps^2 =', round(w[-2] / eps ** 2, 4))

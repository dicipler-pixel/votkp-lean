# SCRIPT: CHECK-GRAVITY-02-TWO-PLANE-WALL
# Gravity paper against the Loop Wall element paper.
# Connection checked: the loop wall is a sign change of a TWO-PLANE GRAM DETERMINANT of an
# indefinite quadratic form, the same mathematical event as the gravity paper's det g = 0 on a
# probe plane (final_v3 Section 5.3 / Appendix W: "the sign of a two-plane determinant is a
# property of the plane"). The indefinite form here is the auxiliary quadratic form of the
# hyperboloid model of the element paper's disk (signature (-,+,+)); it is NOT a spacetime metric
# and NOT the intrinsic projector-bundle metric. Also checked: what survives the wall. The single
# quantity s = sinh(ha) sinh(hb) is cos(phi) of the Lambert quadrilateral's fourth angle while the
# loop closes, and cosh(d) of the common-perpendicular gap of the right-angled pentagon once it
# opens: one analytic function, an angle on one side and a length on the other.
#
# WHY THIS PROVES WHAT IT CLAIMS. Each face perpendicular is a geodesic with unit spacelike normal
# n = (sinh h, cosh h u) (u the axis direction). Two geodesics meet inside the disk iff the plane
# spanned by n1, n2 is spacelike, i.e. iff the 2x2 Gram matrix [[<n1,n1>,<n1,n2>],[<n2,n1>,<n2,n2>]]
# is positive definite; they touch at the rim iff it is degenerate; they are ultraparallel iff it is
# Lorentzian (det < 0). That is a theorem of the hyperboloid model. The script (a) constructs the
# intersection point directly and compares with the Gram-determinant sign and the element paper's
# margin Ga^2+Gb^2-1 for every adjacent pair; (b) measures the actual angle at the constructed
# fourth vertex and the actual distance between ultraparallel lines, and compares with s;
# (c) rotates the second axis (plane choice) and checks that the determinant sign follows the
# plane, reproducing the archived carbon-with-nitrogen contacts 13.11528523 and 89.82270223 deg.
# Kill conditions (written before the run): any sign disagreement; |cos phi - s| or |cosh d - s|
# above 1e-9; contact angles off the archived values by more than 1e-6 deg.
import gzip, json, math, sys
import numpy as np

d = json.load(gzip.open(sys.argv[1])); rec = {r['Z']: r for r in d['records']}
J = np.diag([-1.0, 1.0, 1.0])
def mink(x, y): return x @ J @ y
def normal(h, th): return np.array([math.sinh(h), math.cosh(h) * math.cos(th), math.cosh(h) * math.sin(th)])
def point(h, th): return np.array([math.cosh(h), math.sinh(h) * math.cos(th), math.sinh(h) * math.sin(th)])

cores = [(2, 'helium'), (10, 'neon'), (18, 'argon'), (36, 'krypton'), (54, 'xenon'), (86, 'radon')]
faces = []
for N, name in cores:
    for Z in range(N + 1, 119):
        th = {t['q']: t['IE_eV'] for t in rec[Z]['thresholds']}; q = Z - N - 1
        if q in th and q + 1 in th: faces.append((name, Z, th[q + 1] / th[q]))
pairs = [(a, b) for a, b in zip(faces, faces[1:]) if a[0] == b[0] and b[1] == a[1] + 1]

signbad = 0; worst_cos = 0.0; worst_cosh = 0.0; worst_direct = 0.0
for (_, Za, za), (_, Zb, zb) in pairs:
    ha, hb = 0.5 * math.log(za), 0.5 * math.log(zb)
    Ga, Gb = math.tanh(ha), math.tanh(hb)
    n1, n2 = normal(ha, 0.0), normal(hb, math.pi / 2)
    G = np.array([[mink(n1, n1), mink(n1, n2)], [mink(n2, n1), mink(n2, n2)]])
    detG = np.linalg.det(G); s = math.sinh(ha) * math.sinh(hb)
    X = np.cross(J @ n1, J @ n2); q = mink(X, X)          # Minkowski-orthogonal to both normals
    meets = q < 0
    margin = Ga * Ga + Gb * Gb - 1
    if not ((detG > 0) == meets == (margin < 0) == (s < 1)): signbad += 1
    if meets:
        X = X / math.sqrt(-q); X = X if X[0] > 0 else -X
        # angle at X between the two face geodesics: their unit normals give cos(angle) = |<n1,n2>|
        # measured instead from tangent vectors at X: t_i = J n_i projected orthogonal to X, then cross with X
        t1 = np.cross(J @ X, J @ n1); t2 = np.cross(J @ X, J @ n2)
        t1 = t1 / math.sqrt(mink(t1, t1)); t2 = t2 / math.sqrt(mink(t2, t2))
        # the Lambert quadrilateral's fourth angle is acute, so cos(phi) = |<t1,t2>|
        phi = math.acos(max(-1, min(1, abs(mink(t1, t2)))))
        worst_cos = max(worst_cos, abs(math.cos(phi) - s))
    else:
        # ultraparallel: distance between lines from |<n1,n2>| = cosh d
        dist = math.acosh(abs(mink(n1, n2)))
        worst_cosh = max(worst_cosh, abs(math.cosh(dist) - s))
        # independent distance: minimise over points of line 1 the distance to line 2
        # point on line 1: foot F1=point(ha,0) moved along direction e2-ish; sinh(dist to line2) = |<P,n2>|
        def dist2(t):
            P = math.cosh(t) * point(ha, 0.0) + math.sinh(t) * np.array([0, 0, 1.0])
            return math.asinh(abs(mink(P, n2)))
        lo, hi = -8.0, 8.0
        for _ in range(300):            # ternary search: distance to a line is convex along a geodesic
            m1, m2 = lo + (hi - lo) / 3, hi - (hi - lo) / 3
            if dist2(m1) < dist2(m2): hi = m2
            else: lo = m1
        worst_direct = max(worst_direct, abs(dist2(0.5 * (lo + hi)) - dist))
print('pairs', len(pairs), ': sign disagreements (Gram det / intersection / margin / s<1):', signbad)
print('closed loops: max |cos(phi_measured) - sinh ha sinh hb| =', f'{worst_cos:.2e}')
print('open loops: max |cosh(d) - sinh ha sinh hb| =', f'{worst_cosh:.2e}', '; direct minimised distance vs d:', f'{worst_direct:.2e}')

# regular hypersurface (codimension one): gradient of F = sinh ha sinh hb - 1 on F=0
grads = []
for ha in np.linspace(0.05, 3.0, 300):
    hb = math.asinh(1 / math.sinh(ha))
    grads.append(math.hypot(math.cosh(ha) * math.sinh(hb), math.sinh(ha) * math.cosh(hb)))
print('min |grad F| on the wall curve (must be > 0):', round(min(grads), 6))

# plane conditioning: rotate the second axis by theta; contacts where |<n1,n2>| = 1
zC = 392.09056 / 64.49352; zN = 552.06741 / 97.8901
a, b = 0.5 * math.log(zC), 0.5 * math.log(zN)
def gram_det(th):
    n1, n2 = normal(a, 0.0), normal(b, th); return 1 - mink(n1, n2) ** 2
def forward(th):
    n1, n2 = normal(a, 0.0), normal(b, th); X = np.cross(J @ n1, J @ n2); q = mink(X, X)
    if q >= 0: return False
    X = X / math.sqrt(-q); X = X if X[0] > 0 else -X
    ang = math.atan2(X[2], X[1]); return 0 < ang < th
def bisect(f, lo, hi):
    flo = f(lo)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(mid) == flo: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)
c1 = math.degrees(bisect(lambda t: gram_det(t) > 0, math.radians(0.5), math.radians(45)))
c2 = math.degrees(bisect(lambda t: gram_det(t) > 0, math.radians(45), math.radians(120)))
f1 = math.degrees(bisect(forward, math.radians(2), math.radians(45)))
print('carbon with nitrogen: Gram-det contacts (deg):', round(c1, 8), round(c2, 8),
      '| forward-sector closing window starts at', round(f1, 8))
print('closes at 89.8 deg:', forward(math.radians(89.8)), '| closes at 90 deg:', forward(math.radians(90)))

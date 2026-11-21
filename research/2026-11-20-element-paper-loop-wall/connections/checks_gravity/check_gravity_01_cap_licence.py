# SCRIPT: CHECK-GRAVITY-01-CAP-LICENCE
# Gravity paper ("The Ledger Outlives the Metric") against the Loop Wall element paper.
# Connection checked: the two-face loop test  Gamma_a^2 + Gamma_b^2 < 1  is the same inequality as
#   (i)  the gravity paper's persistence cap Tr(P R) <= k (Theorem 1) for a rank-one P and the
#        rank-two orthogonal projector R onto the two face directions (Bessel / Cauchy-Schwarz);
#   (ii) the gravity paper's two-dimensional licence: [[a, b+i w/2],[b-i w/2, c]] is PSD iff
#        a>=0, c>=0, 4(ac-b^2) >= w^2 (Edition 6/7 Theorem 3; final_v3 Theorem 2 and Section 4),
#        with a = c = 1, b = Gamma_a, w = 2 Gamma_b;
#   (iii) the nesting of final_v3 Theorem 5: wherever w != 0 the licence locus 4 det g = w^2 lies
#        strictly inside det g > 0. Here det g = 1 - Gamma_a^2 stays > 0 when the loop opens.
# Also: Gamma = cos(angle of parallelism of h); closing iff the two angles sum to more than 90 deg.
# Chemistry instance at the anion rung: a = c = chi, b = eta, w = 2 eta; det g = chi^2 - eta^2 = IE*EA.
#
# WHY THIS PROVES WHAT IT CLAIMS. (i) For a real unit vector u and orthonormal e1, e2,
# Tr(uu^T R) = <u,e1>^2 + <u,e2>^2. A unit u with <u,e1> = Ga, <u,e2> = Gb exists in R^3 iff
# 1 - Ga^2 - Gb^2 >= 0 (its third component squared). So "closes" must coincide, pair by pair,
# with "a rank-one orthogonal projector realises the two overlaps below its rank cap". (ii) The
# 2x2 Hermitian criterion is a theorem; if the script finds one archive pair where the loop
# verdict and the PSD verdict differ, the claimed identity is false. (iii) Nesting requires every
# open pair to have 1 - Ga^2 > 0 (metric definite) while the full determinant is negative.
# Kill condition (written before the run): any single disagreement among the 433 faces, 427
# adjacent pairs or 49 anion rungs kills the EXACT grade.
import gzip, json, math, sys, csv
import numpy as np
from fractions import Fraction as F

arch = sys.argv[1]
anion_csv = sys.argv[2]
d = json.load(gzip.open(arch)); rec = {r['Z']: r for r in d['records']}
cores = [(2, 'helium'), (10, 'neon'), (18, 'argon'), (36, 'krypton'), (54, 'xenon'), (86, 'radon')]

def gam(z): return (z - 1) / (z + 1)

faces = []  # (core, Z, z exact Fraction)
for N, name in cores:
    for Z in range(N + 1, 119):
        th = {t['q']: t['IE_eV'] for t in rec[Z]['thresholds']}; q = Z - N - 1
        if q in th and q + 1 in th:
            faces.append((name, Z, F(repr(th[q + 1])) / F(repr(th[q]))))
pairs = [(a, b) for a, b in zip(faces, faces[1:]) if a[0] == b[0] and b[1] == a[1] + 1]
print('faces', len(faces), 'adjacent same-core pairs', len(pairs))

R = np.diag([1.0, 1.0, 0.0])
bad = 0; nest_bad = 0; opens = []; ang_bad = 0
for (c, Za, za), (_, Zb, zb) in pairs:
    Ga, Gb = gam(za), gam(zb)                      # exact rationals
    margin = Ga * Ga + Gb * Gb - 1                 # exact signed margin
    loop_closes = margin < 0
    # (ii) gravity 2x2 licence criterion with a=c=1, b=Ga, w=2Gb  (exact)
    a = c_ = F(1); b = Ga; w = 2 * Gb
    licence = (a >= 0) and (c_ >= 0) and (4 * (a * c_ - b * b) >= w * w)
    licence_strict = 4 * (a * c_ - b * b) > w * w
    # (i) rank-one orthogonal realisation below the cap: third component squared
    t2 = 1 - Ga * Ga - Gb * Gb
    realisable_strict = t2 > 0
    if realisable_strict:
        u = np.array([float(Ga), float(Gb), math.sqrt(float(t2))]); P = np.outer(u, u)
        assert abs(np.trace(P) - 1) < 1e-12 and abs(np.trace(P @ R) - float(Ga * Ga + Gb * Gb)) < 1e-12
    # numerical eigenvalue check of the Hermitian form [[1, w],[conj w, 1]], w = Ga + i Gb
    Hm = np.array([[1, complex(float(Ga), float(Gb))], [complex(float(Ga), -float(Gb)), 1]])
    psd_num = np.linalg.eigvalsh(Hm).min() > 0
    if not (loop_closes == licence_strict == realisable_strict == psd_num): bad += 1
    if not loop_closes:
        opens.append((c, Za, Zb, float(margin)))
        # (iii) nesting: metric part det g = ac - b^2 = 1 - Ga^2 must be > 0 while licence fails
        if not (1 - Ga * Ga > 0 and Gb != 0): nest_bad += 1
    # angle of parallelism: cos Pi(h) = tanh h = Gamma ; closes iff Pi(ha) + Pi(hb) > 90 deg
    Pa = math.acos(float(Ga)); Pb = math.acos(float(Gb))
    if (Pa + Pb > math.pi / 2) != loop_closes: ang_bad += 1
print('disagreements loop / licence / rank-one cap / eigenvalue :', bad)
print('open pairs:', [(c, Za, Zb, round(m, 9)) for c, Za, Zb, m in opens])
print('nesting failures among open pairs (need 1-Ga^2>0, Gb!=0):', nest_bad)
print('angle-of-parallelism disagreements:', ang_bad)

# equal faces: wall Gamma^2 = 1/2  <=>  Pi(h) = 45 deg  <=>  tan(Pi/2) = exp(-h) = sqrt2 - 1
zs = 3 + 2 * math.sqrt(2); h = 0.5 * math.log(zs)
print('wall: Pi(h) deg =', round(math.degrees(math.acos(math.tanh(h))), 12),
      ' tan(Pi/2)=e^-h =', round(math.exp(-h), 15), ' sqrt2-1 =', round(math.sqrt(2) - 1, 15))
# all 433 equal-face self pairs
selfbad = 0
for c, Z, z in faces:
    G = gam(z); closes = 2 * G * G < 1
    lic = 4 * (1 - G * G) > (2 * G) ** 2
    if closes != lic: selfbad += 1
print('equal-face disagreements (433 faces):', selfbad)

# chemistry instance at the anion rung: a=c=chi, b=eta, w=2eta
rows = list(csv.DictReader(open(anion_csv)))
cb = 0; idb = 0; nb = 0
for r in rows:
    I = F(r['IE1_pinned_eV']); A = F(r['EA_eV'])
    eta = (I - A) / 2; chi = (I + A) / 2
    G0 = gam(I / A)
    if G0 != eta / chi: cb += 1
    if chi * chi - eta * eta != I * A: idb += 1           # metric determinant = IE*EA
    lic = 4 * (chi * chi - eta * eta) >= (2 * eta) ** 2    # licence form
    omega = chi * chi / (2 * eta)
    if (lic and not omega >= eta) or (omega >= eta and not lic): nb += 1
    if omega < eta and not (chi * chi - eta * eta > 0): nb += 1   # nesting: metric still definite
print('anion rungs', len(rows), ': Gamma0 != eta/chi:', cb, '; chi^2-eta^2 != IE*EA:', idb,
      '; licence vs omega>=eta disagreements or nesting failures:', nb)
n_out = sum(1 for r in rows if (F(r['IE1_pinned_eV']) + F(r['EA_eV'])) ** 2 < 2 * (F(r['IE1_pinned_eV']) - F(r['EA_eV'])) ** 2)
print('anion rungs outside the wall (licence failed, IE*EA > 0 still):', n_out, 'of', len(rows))

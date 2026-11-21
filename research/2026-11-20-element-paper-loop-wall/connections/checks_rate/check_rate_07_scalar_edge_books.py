# SCRIPT: RATE-WEIGHT-EDGE-BOOKS-07
# Connection tested: the two books of The Weight Between v1.1 (section 2.3: connection book
# E- = (1/8)||[H, H^dagger]||_F^2, opposite book E+ = (1/8)||H^2 - H^dagger^2||_F^2, H = diag D + A with a
# unitary antihermitian connection A on edges) evaluated on ONE scalar edge whose two vertex values are the
# two removal energies of a peel step, d_i = IE_(k+1), d_j = IE_k.
# Claim (atlas card B189 states the scalar-edge form; this script checks it from the paper's definitions):
#   E- = (d_i - d_j)^2,  E+ = (d_i + d_j)^2,  so E-/E+ = Gamma^2 and (E+ - E-)/E+ = 4 d_i d_j/(d_i+d_j)^2
#   = 4 nu(1 - nu) = 1 - Gamma^2, the census of check 01 (nu = d_j/(d_i + d_j)).
#   The loop wall Gamma^2 = 1/2 is then E+ = 2 E-: the reflected share equals the transmitted share.
# WHY THE CHECK PROVES IT: the books are computed from the matrix definitions in the paper, not from the
# closed forms, on random edges (exact identity expected to rounding) and on every archive step; a
# non-unitary edge block is the control that must break eq. (8)'s premise.
# NAME CLASH (stated before running): these books are NOT Englert's visibility/distinguishability pair of
# section 3 of the same paper; with B189's books "equal books" means Gamma^2 = 1, not the wall.
# KILL CONDITIONS: K1 any random-edge residual above 1e-12 (relative); K2 any archive step whose E-/E+ differs
# from Gamma^2 by more than 1e-12; K3 the non-unitary control reproduces E- = (d_i - d_j)^2 to 1e-6.
import sys, gzip, json, math
import numpy as np

rng = np.random.default_rng(3)

def books(di, dj, a):
    A = np.array([[0, a], [-np.conj(a), 0]], dtype=complex)
    H = np.diag([di, dj]).astype(complex) + A
    Hd = H.conj().T
    Em = np.linalg.norm(H @ Hd - Hd @ H) ** 2 / 8
    Ep = np.linalg.norm(H @ H - Hd @ Hd) ** 2 / 8
    return Em, Ep

w1 = 0.0
for _ in range(1000):
    di, dj = rng.uniform(0.1, 50, size=2)
    a = np.exp(1j * rng.uniform(0, 2 * np.pi))
    Em, Ep = books(di, dj, a)
    w1 = max(w1, abs(Em - (di - dj) ** 2) / (di + dj) ** 2, abs(Ep - (di + dj) ** 2) / (di + dj) ** 2)
Em_c, Ep_c = books(5.0, 2.0, 1.7)   # non-unitary edge block |a| != 1
print(f'random scalar edges: worst relative residual of E- = (di-dj)^2, E+ = (di+dj)^2: {w1:.1e}')
print(f'control |a| = 1.7: E- = {Em_c:.6f} against (di-dj)^2 = 9 (must differ)')

d = json.load(gzip.open(sys.argv[1]))
W = 3 + 2 * math.sqrt(2)
w2 = w3 = 0.0
n = 0
near = []
for r in d['records']:
    if r['Z'] > 85:
        continue
    E = [x['IE_eV'] for x in sorted(r['thresholds'], key=lambda x: x['q']) if x.get('IE_eV') is not None]
    for k in range(len(E) - 1):
        dj, di = E[k], E[k + 1]
        Em, Ep = books(di, dj, 1.0)
        z = di / dj
        G = (z - 1) / (z + 1)
        nu = dj / (di + dj)
        w2 = max(w2, abs(Em / Ep - G * G))
        w3 = max(w3, abs((Ep - Em) / Ep - 4 * nu * (1 - nu)))
        n += 1
        near.append((abs(Em / Ep - 0.5), r['name'], k + 1, Em / Ep, (Ep - Em) / Ep))
print(f'archive H..At, {n} steps: worst |E-/E+ - Gamma^2| = {w2:.1e}; worst |(E+-E-)/E+ - 4nu(1-nu)| = {w3:.1e}')
print('closest ordinary steps to reflected = transmitted (E-/E+ = 1/2):')
for t in sorted(near)[:4]:
    print(f'   {t[1]:10s} step {t[2]:2d}  reflected share {t[3]:.5f}  transmitted share {t[4]:.5f}')
print('KILL K1', 'FIRED' if w1 > 1e-12 else 'not fired', '| K2', 'FIRED' if w2 > 1e-12 else 'not fired',
      '| K3', 'FIRED' if abs(Em_c - 9) < 1e-6 else 'not fired')

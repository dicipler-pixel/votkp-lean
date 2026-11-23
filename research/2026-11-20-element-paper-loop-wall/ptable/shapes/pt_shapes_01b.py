# SCRIPT: PT-SHAPES-01B  (PT-SHAPES-01 on the H-to-At baseline only, as the v2.2 Shapes view uses)  every element on different measuring shapes, not just the circle
# Jeromie Beasley, 23 Nov 2026, AI-assisted.  Data: Periodic Table of Elemental Peels v2 (ptable_v2_data.json, element-paper/loop-wall).
# BOOKS: for each element the first K ionization steps z_k = IE_{k+1}/IE_k (never zero, always > 1).  Peel step g_k = G(z_k).
# SHAPES (same books, different reading):
#   circle/ball  : the Gamma-vector as a point in the Poincare ball (scaled into it), hyperbolic distance  [what the table uses now, one disk]
#   diamond      : each step its own peel line, distances added (L1 of atanh g = 1/2 ln z)  [the Poincare diamond, K axes]
#   cube own     : the cube's own reading, max over all face pairs (Hilbert)                  [square/cube fork, other side]
#   simplex      : the K step-logs ln z_k as parts of one whole (triangle/tetrahedron family), flat log-book distance  [shape of the ladder only]
#   control      : plain straight-line distance on the raw ionization energies (no shape)
# SCORE: column recall = share of elements whose nearest other element (by that shape) sits in the same column.
# WHY THIS TESTS IT: a shape that reads the periodic structure puts same-column elements nearest; chance is about 1 in 18.
# KILL (written before the run): a shape "beats the circle" only if its recall exceeds the circle's by more than the
#   95% bootstrap spread of the difference; any shape not above the shuffled-column control's 99th percentile reads nothing.
import json, numpy as np
rng = np.random.default_rng(23)
D = json.load(open('ptable_v2_data.json'))['elements']
G = lambda z: (z - 1) / (z + 1)
def run(K):
    E = [e for e in D if len(e['ie']) >= K + 1 and e.get('col') and not e.get('heavy')]   # H to At only (the table's baseline)
    Z = np.array([e['Z'] for e in E]); col = np.array([e['col'] for e in E]); sym = [e['sym'] for e in E]
    ie = np.array([e['ie'][:K + 1] for e in E]); z = ie[:, 1:] / ie[:, :-1]; g = G(z); L = 0.5 * np.log(z)
    n = len(E)
    def ball(i, j):
        x, y = g[i] / np.sqrt(K) * .999, g[j] / np.sqrt(K) * .999
        num = 2 * np.sum((x - y) ** 2); den = (1 - x @ x) * (1 - y @ y); return np.arccosh(1 + num / den)
    def diamond(i, j): return np.sum(np.abs(L[i] - L[j]))
    def cube_own(i, j):
        # cube (-1,1)^K with faces 1 - x_k and 1 + x_k ; point x = g (peel coordinate)
        bx = np.concatenate([1 - g[i], 1 + g[i]]); by = np.concatenate([1 - g[j], 1 + g[j]]); r = np.log(by) - np.log(bx)
        return .5 * (r.max() - r.min())
    def simplex(i, j):
        a, b = np.log(np.log(z[i])), np.log(np.log(z[j])); r = b - a; return .5 * (r.max() - r.min()) * 2
    def control(i, j): return np.linalg.norm(ie[i] - ie[j])
    shapes = {'circle/ball (now)': ball, 'diamond (per-step peel)': diamond, 'cube own reading': cube_own,
              'simplex (ladder shape)': simplex, 'control: raw energies': control}
    Ms = {}
    for nm, f in shapes.items():
        M = np.full((n, n), np.inf)
        for i in range(n):
            for j in range(n):
                if i != j: M[i, j] = f(i, j)
        Ms[nm] = M
    def recall(M, idx=None, c=col):
        idx = np.arange(n) if idx is None else idx
        hits = []
        for i in idx:
            row = M[i, idx].copy(); row[idx == i] = np.inf; j = idx[np.argmin(row)]; hits.append(c[i] == c[j])
        return np.mean(hits)
    res = {nm: recall(M) for nm, M in Ms.items()}
    # shuffled-column control on the circle
    null = [recall(Ms['circle/ball (now)'], c=rng.permutation(col)) for _ in range(300)]
    # bootstrap the difference vs circle
    boot = {nm: [] for nm in Ms}
    for _ in range(300):
        idx = np.unique(rng.choice(n, n))
        rc = recall(Ms['circle/ball (now)'], idx)
        for nm, M in Ms.items(): boot[nm].append(recall(M, idx) - rc)
    print("K = %d steps per element, %d elements (Z %d to %d)" % (K, n, Z.min(), Z.max()))
    print("   shuffled-column control: mean %.3f, 99th percentile %.3f" % (np.mean(null), np.percentile(null, 99)))
    for nm in Ms:
        lo, hi = np.percentile(boot[nm], [2.5, 97.5])
        verdict = '' if nm.startswith('circle') else ('BEATS the circle' if lo > 0 else ('loses to the circle' if hi < 0 else 'no clear difference'))
        print("   %-26s recall %.3f   difference vs circle %+.3f [%+.3f, %+.3f]  %s" % (nm, res[nm], res[nm] - res['circle/ball (now)'], lo, hi, verdict))
    # examples
    for s in ['Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'Fe', 'Cu']:
        if s in sym:
            i = sym.index(s)
            print("      %-3s nearest: " % s + ', '.join('%s %s' % (nm.split()[0], sym[np.argmin(Ms[nm][i])]) for nm in Ms))
    return res
for K in (8,):
    run(K); print()

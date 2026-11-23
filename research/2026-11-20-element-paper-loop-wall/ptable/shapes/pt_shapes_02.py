# SCRIPT: PT-SHAPES-02  do the shapes read the long table (18 columns) or the old short table (8 groups, Mendeleev / Russell octaves)?
# Jeromie Beasley, 23 Nov 2026, AI-assisted.  Same books and shapes as PT-SHAPES-01.
# Seen in PT-SHAPES-01: Al's nearest was Y, Si's was Zr, P's was Nb -- elements with the same count of outer electrons
#   across the main and transition blocks.  That is the old short-form grouping: columns 3-7 and 13-17 share groups 3-7,
#   11-12 share groups 1-2, 18 (and 8-10) are group 8.
# KILL (before the run): short-form recall must beat long-form recall for the same shape by more than the 95% bootstrap
#   spread, AND beat a shuffled short-form control's 99th percentile.  Otherwise the shapes read the long table.
import json, numpy as np
rng = np.random.default_rng(8)
D = json.load(open('ptable_v2_data.json'))['elements']
G = lambda z: (z - 1) / (z + 1)
def short(c):
    if c in (1, 2): return c
    if 3 <= c <= 7: return c
    if 13 <= c <= 17: return c - 10
    if c in (11, 12): return c - 10
    return 8                                   # 8, 9, 10 and 18
K = 8
E = [e for e in D if len(e['ie']) >= K + 1 and e.get('col')]
col = np.array([e['col'] for e in E]); sh = np.array([short(c) for c in col]); n = len(E)
ie = np.array([e['ie'][:K + 1] for e in E]); z = ie[:, 1:] / ie[:, :-1]; g = G(z); L = .5 * np.log(z); LL = np.log(np.log(z))
def mats():
    x = g / np.sqrt(K) * .999; nx = 1 - np.sum(x * x, 1)
    d2 = np.sum((x[:, None] - x[None]) ** 2, -1); ball = np.arccosh(1 + 2 * d2 / (nx[:, None] * nx[None]))
    dia = np.sum(np.abs(L[:, None] - L[None]), -1)
    bx = np.concatenate([1 - g, 1 + g], 1); r = np.log(bx[None]) - np.log(bx[:, None]); cube = .5 * (r.max(-1) - r.min(-1))
    r2 = LL[None] - LL[:, None]; simp = r2.max(-1) - r2.min(-1)
    return {'circle/ball (now)': ball, 'diamond (per-step peel)': dia, 'cube own reading': cube, 'simplex (ladder shape)': simp}
Ms = mats()
for M in Ms.values(): np.fill_diagonal(M, np.inf)
def recall(M, lab, idx):
    sub = M[np.ix_(idx, idx)]; j = np.argmin(sub, 1); return np.mean(lab[idx] == lab[idx][j])
allidx = np.arange(n)
print("K = %d, %d elements" % (K, n))
null = [recall(Ms['circle/ball (now)'], rng.permutation(sh), allidx) for _ in range(300)]
print("   shuffled short-form control: mean %.3f, 99th %.3f" % (np.mean(null), np.percentile(null, 99)))
for nm, M in Ms.items():
    rl, rs = recall(M, col, allidx), recall(M, sh, allidx); b = []
    for _ in range(400):
        idx = np.unique(rng.choice(n, n)); b.append(recall(M, sh, idx) - recall(M, col, idx))
    lo, hi = np.percentile(b, [2.5, 97.5])
    print("   %-26s long-form %.3f   short-form %.3f   gain %+.3f [%+.3f, %+.3f]  %s" % (nm, rl, rs, rs - rl, lo, hi,
          'READS THE SHORT FORM' if lo > 0 and rs > np.percentile(null, 99) else 'no clear gain'))
sym = [e['sym'] for e in E]
print("   pairs the circle makes across blocks (nearest in another long column but same short group):")
M = Ms['circle/ball (now)']; out = []
for i in range(n):
    j = np.argmin(M[i])
    if col[i] != col[j] and sh[i] == sh[j]: out.append('%s-%s' % (sym[i], sym[j]))
print("     " + ', '.join(out))

print("\nSTRAW-MAN: merging labels raises chance too.  Two fixes: (1) chance-corrected recall (r - chance)/(1 - chance);")
print("(2) merge ONLY the A/B partners (3-7 with 13-17, 1-2 with 11-12), keep 8, 9, 10 and 18 apart (no triad merging).")
def ab(c):
    if 13 <= c <= 17: return c - 10
    if c in (11, 12): return c - 10
    return c
ab_lab = np.array([ab(c) for c in col])
def chance(lab): return np.mean([recall(Ms['circle/ball (now)'], rng.permutation(lab), allidx) for _ in range(300)])
cl, cs, ca = chance(col), chance(sh), chance(ab_lab)
for nm, M in Ms.items():
    r = [recall(M, lab, allidx) for lab in (col, sh, ab_lab)]
    k = [(x - c) / (1 - c) for x, c in zip(r, (cl, cs, ca))]
    b = []
    for _ in range(400):
        idx = np.unique(rng.choice(n, n)); b.append(recall(M, ab_lab, idx) - recall(M, col, idx))
    lo, hi = np.percentile(b, [2.5, 97.5])
    print("   %-26s corrected: long %.3f  short %.3f  A/B-only %.3f ; A/B-only raw gain %+.3f [%+.3f, %+.3f] %s" %
          (nm, k[0], k[1], k[2], r[2] - r[0], lo, hi, 'A/B pairing real' if lo > 0 else 'A/B pairing not shown'))

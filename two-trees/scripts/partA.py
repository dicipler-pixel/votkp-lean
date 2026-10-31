# SCRIPT: LN7_PARTA_BOUNDS
# Exact check of l + (L-1) delta <= d(O,wO) <= L l at z = 7 for all non-backtracking words.
import numpy as np, mpmath as mp, itertools, sys
mp.mp.dps = 60
Z = 7
c, s = Z*Z+1, Z*Z-1          # 2z B_u = [[50,48],[48,50]] ; use 7 B_u = [[25,24],[24,25]] (z odd: exact /2)
def Q(axis, sign):
    M = np.diag([7,7,7,7]).astype(object)
    M[0,0] = 25; M[axis,axis] = 25; M[0,axis] = M[axis,0] = 24*sign
    return M
letters = [(1,1),(1,-1),(2,1),(2,-1),(3,1),(3,-1)]
names = ['i','-i','j','-j','k','-k']
Qs = [Q(a,sg) for a,sg in letters]
inv = [1,0,3,2,5,4]
# Lorentz check: Q^T eta Q = 49 eta, Q_u Q_-u = 49 I
eta = np.diag([1,-1,-1,-1]).astype(object)
for u in range(6):
    assert (Qs[u].T.dot(eta).dot(Qs[u]) == 49*eta).all()
    assert (Qs[u].dot(Qs[inv[u]]) == 49*np.diag([1,1,1,1]).astype(object)).all()
ell = mp.log(7)
delta = mp.acosh(mp.mpf(9)/7)
print('ell =', mp.nstr(ell,12), ' delta =', mp.nstr(delta,12), ' delta/ell =', mp.nstr(delta/ell,12))
assert abs(mp.cosh(ell) - mp.mpf(25)/7) < mp.mpf(10)**-50 and abs(mp.sinh(ell/2)**2 - mp.mpf(9)/7) < mp.mpf(10)**-50
LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 9
# DFS over words with first letter fixed = i (the symmetry group of the octahedron acts transitively on first letters
# and preserves non-backtracking and d). Row vector r = e0^T Q_{w1} ... Q_{wL}; r[0] = 7^L cosh d.
best = {}   # L -> (min margin in d, word, min cosh d numerator)
worst_ratio = {}
mind = {}
ref = {}
def dfs(r, word, L):
    num = r[0]
    D = mp.acosh(mp.mpf(int(num)) / mp.mpf(7)**L)
    lb = ell + (L-1)*delta
    marg = D - lb
    if L not in best or marg < best[L][0]:
        best[L] = (marg, list(word))
    st = sum(1 for m in range(L-1) if word[m+1]==word[m]); tu = L-1-st
    m2 = D - (ell*(1+st) + tu*delta)
    if tu > 0 and (L not in ref or m2 < ref[L][0]):
        ref[L] = (m2, list(word))
    if L not in mind or D < mind[L][0]:
        mind[L] = (D, list(word))
    assert D <= L*ell + mp.mpf(10)**-40
    if L == LMAX: return
    last = word[-1]
    for u in range(6):
        if u == inv[last]: continue
        word.append(u)
        dfs(r.dot(Qs[u]), word, L+1)
        word.pop()
r0 = np.array([1,0,0,0], dtype=object).dot(Qs[0])
dfs(r0, [0], 1)
print('L  #words(first=i)  min[d-(l+(L-1)delta)]  min d   min d/(L l)   argmin word')
for L in range(1, LMAX+1):
    m, w = best[L]; D, w2 = mind[L]
    print(L, 5**(L-1), mp.nstr(m,10), mp.nstr(D,10), mp.nstr(D/(L*ell),8), ' '.join(names[x] for x in w2))
# best constant c with d >= l + (L-1) c over all checked words (L>=2)
print('refined bound d >= l(1+#straight) + delta(#turns): min margin per L')
print('(straight words i^L give equality d = L l exactly; listed below: words with >= 1 turn)')
for L in range(2, LMAX+1):
    print(L, mp.nstr(ref[L][0],10), ' '.join(names[x] for x in ref[L][1]))
print('overall min margin (L>=2):', mp.nstr(min(best[L][0] for L in range(2,LMAX+1)),12))
print('lower bound fails anywhere (tol 1e-40):', any(best[L][0] < -mp.mpf(10)**-40 for L in best))
print('refined bound fails anywhere (tol 1e-40):', any(ref[L][0] < -mp.mpf(10)**-40 for L in ref))
# exact identity behind the commutator: cosh(tau) = T_4(9/7)
from fractions import Fraction as F
c = F(9,7); print('T4(9/7) =', 8*c**4-8*c**2+1, '  commutator cosh(tau) = 23137/2401')

"""Numeric checks for the Peel tree view of Knot Atlas in 3D.

Every check prints PASS or FAIL. Exit code 0 only if all pass.
Needs Python 3 and numpy. These are floating-point checks of the panel
numbers and of small finite cases; they are not proofs.
"""
import itertools, math, sys
import numpy as np

results = []
def check(name, ok, detail=""):
    results.append(ok)
    print(("PASS " if ok else "FAIL ") + name + (": " + detail if detail else ""))

def close(a, b, tol=5e-5):
    return abs(a - b) <= tol

# --- 1. Quaternion side: LPS normalization, small cases --------------------
def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2,
            a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2,
            a1*d2 + b1*c2 - c1*b2 + d1*a2)
def norm(q): return sum(x*x for x in q)

norm5 = [q for q in itertools.product(range(-2, 3), repeat=4) if norm(q) == 5]
check("integer quaternions of norm 5", len(norm5) == 48, f"{len(norm5)} (expected 48)")
normalized5 = [q for q in norm5 if q[0] % 2 == 1 and all(x % 2 == 0 for x in q[1:])]
check("normalized ones (odd real part, even i,j,k) are +/- the six 1+-2u",
      len(normalized5) == 12, f"{len(normalized5)} = 2 x 6")

GENS = [(1, 2, 0, 0), (1, -2, 0, 0), (1, 0, 2, 0), (1, 0, -2, 0), (1, 0, 0, 2), (1, 0, 0, -2)]
INV = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}
def reduced_words(k):
    words = [[]]
    for _ in range(k):
        words = [w + [g] for w in words for g in range(6) if not (w and INV[w[-1]] == g)]
    return words
for k in (1, 2, 3):
    words = reduced_words(k)
    prods = set()
    for w in words:
        q = (1, 0, 0, 0)
        for g in w: q = qmul(q, GENS[g])
        prods.add(q)
    R = int(math.isqrt(5**k)) + 1
    target = set(q for q in itertools.product(range(-R, R + 1), repeat=4)
                 if norm(q) == 5**k and q[0] % 2 == 1 and all(x % 2 == 0 for x in q[1:])
                 and not all(x % 5 == 0 for x in q))
    signed = prods | set(tuple(-x for x in q) for q in prods)
    ok = len(prods) == len(words) and signed == target and len(target) == 2 * len(words)
    check(f"norm 5^{k}: {len(words)} reduced words give distinct quaternions, and +/- them are exactly "
          f"the normalized norm-5^{k} quaternions not divisible by 5", ok,
          f"words {len(words)}, distinct {len(prods)}, target {len(target)}")

# --- 2. The drawing: boosts in the hyperboloid model -----------------------
def boost(ax, d):
    B = np.eye(4); c, s = math.cosh(d), math.sinh(d)
    B[0, 0] = B[ax, ax] = c; B[0, ax] = B[ax, 0] = s; return B
def dist(M): return math.acosh(M[0, 0])
def path(seq, L):
    M = np.eye(4)
    for a in seq: M = M @ boost(a, L)
    return dist(M)

L5, L7 = math.log(5), math.log(7)
check("his step ln 5 = 1.6094", close(L5, 1.6094), f"{L5:.6f}")
check("Smith step tanh(ln5/2) = (5-1)/(5+1) = 2/3", close(math.tanh(L5/2), 2/3, 1e-12))
check("straight path 3 steps = 3 ln 5 = 4.8283", close(path((1, 1, 1), L5), 4.8283), f"{path((1,1,1),L5):.6f}")
t = path((1, 1, 2), L5)
check("turned path (i,i,j) = 4.1757, shorter by 0.6526", close(t, 4.1757) and close(3*L5 - t, 0.6526),
      f"{t:.6f}, saving {3*L5-t:.6f}")
check("turned path closed form: cosh d = cosh(2 ln5) cosh(ln5)",
      close(math.cosh(t), math.cosh(2*L5)*math.cosh(L5), 1e-9))
check("(i,j,k) = 3.5589 is a different path, not the panel's turned path",
      not close(path((1, 2, 3), L5), 4.1757), f"{path((1,2,3),L5):.4f}")
check("ln 7 option: 1.9459, straight 5.8377, turned 5.1652",
      close(L7, 1.9459) and close(3*L7, 5.8377) and close(path((1, 1, 2), L7), 5.1652))
s = path((1, 1, 2), L7)
check("ln 7 saving 0.6726 (matches the panel; check_ink.py prints 0.6725 because it subtracts a rounded value)", close(3*L7 - s, 0.6726), f"{3*L7-s:.6f}")
sx = boost(1, L5) @ boost(2, L5)
check("two boosts on different axes do not compose to a pure boost (not symmetric)",
      not np.allclose(sx, sx.T), "Theorem 15.1's 'add like velocities' is literal on one axis only")
check("depth-3 six-way tree has 1+6+30+150 = 187 nodes (panel: 187 his)",
      1 + sum(len(reduced_words(k)) for k in (1, 2, 3)) == 187)

# --- 3. Knot side: a real SL(2,R) representation of T(2,n) ----------------
def knot_rep(m, n):
    """Riley form a=[[m,1],[0,1/m]], b=[[m,0],[-t,1/m]]; solve relation for real t."""
    A = np.array([[m, 1.0], [0, 1/m]])
    def parts(t):
        B = np.array([[m, 0.0], [-t, 1/m]])
        W = np.eye(2)
        for i in range(n - 1): W = W @ (B if i % 2 == 0 else A)  # W = b a b a ...
        return A @ W @ np.linalg.inv(B) @ np.linalg.inv(W), B, W
    ts = np.linspace(-20, 20, 40001); f = [parts(t)[0][0, 1] for t in ts]
    for i in range(len(ts) - 1):
        if f[i] * f[i + 1] < 0:
            lo, hi = ts[i], ts[i + 1]
            for _ in range(100):
                mid = (lo + hi) / 2
                if parts(lo)[0][0, 1] * parts(mid)[0][0, 1] <= 0: hi = mid
                else: lo = mid
            R, B, W = parts(lo)
            if np.linalg.norm(R - np.eye(2)) < 1e-8: return A, B, W
    return None

x = 0.44; M = math.exp(x)
check("|M| = e^0.44 = 1.5527, meridian boost 2x = 0.88, tanh x = 0.4136",
      close(M, 1.5527) and close(2*x, 0.88) and close(math.tanh(x), 0.4136))
A = np.array([[M, 1.0], [0, 1/M]])
check("meridian translation length 2 ln|M| = 2x", close(2*math.acosh(abs(np.trace(A))/2), 2*x, 1e-12))
for n, steps, y_panel in ((3, 6, -2.64), (5, 10, -4.40)):
    rep = knot_rep(M, n)
    if rep is None:
        check(f"T(2,{n}) real representation found", False); continue
    A, B, W = rep
    word_len = 2 + 2 * (n - 1)
    loop = A @ W @ np.linalg.inv(B) @ np.linalg.inv(W)
    check(f"T(2,{n}) relation a W b^-1 W^-1 = 1 ({word_len} letters, panel {steps})",
          word_len == steps and np.linalg.norm(loop - np.eye(2)) < 1e-9,
          f"|loop - I| = {np.linalg.norm(loop-np.eye(2)):.1e}")
    C = np.linalg.matrix_power(A @ B, n)
    lam = C @ np.linalg.matrix_power(np.linalg.inv(A), 2*n)  # longitude (ab)^n a^(-2n)
    check(f"T(2,{n}) longitude commutes with the meridian a", np.allclose(lam @ A, A @ lam, atol=1e-9))
    y = math.log(abs(lam[0, 0]))
    check(f"T(2,{n}) y = log|L| = -{2*n}x = {y_panel}, longitude boost 2|y| = {2*abs(y_panel):.2f}",
          close(y, y_panel, 1e-6), f"y = {y:.6f}")

print(f"\n{sum(results)} of {len(results)} checks passed")
sys.exit(0 if all(results) else 1)

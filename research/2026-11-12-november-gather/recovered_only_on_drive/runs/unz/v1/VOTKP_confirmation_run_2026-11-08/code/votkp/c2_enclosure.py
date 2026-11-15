# SCRIPT: c2_enclosure
"""A rigorous constant for |R| <= C |G|^5 on the disk, by two regions with opposite tools.

Region A, |G| <= r*: the Taylor series of D in G (c2_taylor_jets.py writes the coefficient moduli
to .scratch/c2_taylor_S.json). With the coefficients to degree K, for |G| = r,

    |R(G)|/r^5 <= sum_{k=5}^{K} S_k r^{k-5} + tail,     S_k = sum_{a+b=k} |c[a,b]|,

and the tail is bounded by Cauchy's estimate in the polydisc, |c[a,b]| <= M/rho^{a+b} for every
rho < 1 (the series converges in |G| < 1), which gives, with q = 2r/(1+r),

    sum_{k>K} |P_k(G)| <= M (K+2) q^{K+1}/(1-q)^2,     M = sup |D| = 1.0149416... (classical).

Region B, |G| >= r*: boxes. At a box with centre c, a certified value of D at c and an elementary
bound on |grad D| (c2_enclosure_lib) give

    |R| <= |D(c) - P4(c)| + (|grad D| + |grad P4| |dG/dz|_max) rad,
    |G| >= 1 - sqrt3/dist(box, conj w),

and f = |R|/|G|^5 is that over r_lo^5. Boxes are subdivided until the bound is below the target or
until the depth limit, which is reported rather than hidden.
"""
import sys
sys.path.insert(0, 'code')
sys.path.insert(0, 'code/votkp')
import json
import mpmath as mp
from c2_enclosure_lib import bloch_wigner, grad_bound, W, WB, V0

mp.mp.dps = int(__import__('os').environ.get('C2_DPS', '20'))
_T = json.load(open('.scratch/c2_taylor_S.json'))
S = {int(k): mp.mpf(v) for k, v in _T['S'].items()}
COEFFS = {tuple(int(x) for x in key.split(',')): mp.mpc(mp.mpf(re), mp.mpf(im))
          for key, (re, im) in _T['coeffs'].items()}
K = max(S)
R_STAR = mp.mpf(__import__('os').environ.get('C2_RSTAR', '0.4'))
M_WIGNER = mp.mpf('1.0149416064096536')
C2 = 3*mp.sqrt(3)/4
C3 = mp.sqrt(3)/4
C4 = 3*mp.sqrt(3)/16


def _trig_coeffs(r):
    """Coefficients A_j, B_j of R(r e^{i theta}) = sum_j A_j cos(j theta) + B_j sin(j theta)."""
    A, B = {}, {}
    for (a, b), c in COEFFS.items():
        k = a + b
        if k < 5 or k > K:
            continue
        j = a - b
        # c r^k e^{i j theta}
        w = c*r**k
        A[j] = A.get(j, mp.mpf(0)) + mp.re(w)
        B[j] = B.get(j, mp.mpf(0)) + mp.im(w)
    return A, B


def bound_A(r, ntheta=720):
    """Max over theta of |R| at |G| = r, by evaluating the trig polynomial on a grid and adding a
    Lipschitz correction from its derivative -- the tail is the same Cauchy estimate as before."""
    A, B = _trig_coeffs(r)
    dmax = sum(abs(A[j])*abs(j) + abs(B[j])*abs(j) for j in A)     # |d/dtheta|
    best = mp.mpf(0)
    for i in range(ntheta):
        th = 2*mp.pi*i/ntheta
        v = sum(A[j]*mp.cos(j*th) + B[j]*mp.sin(j*th) for j in A)
        best = max(best, abs(v))
    best += dmax*mp.pi/ntheta                                        # one grid step of slack
    q = 2*r/(1 + r)
    tail = M_WIGNER*(K + 2)*q**(K + 1)/(1 - q)**2
    return (best + tail)/r**5


def _dist(pt, x0, x1, y0, y1):
    dx = mp.mpf(0) if x0 <= pt.real <= x1 else min(abs(x0 - pt.real), abs(x1 - pt.real))
    dy = mp.mpf(0) if y0 <= pt.imag <= y1 else min(abs(y0 - pt.imag), abs(y1 - pt.imag))
    return mp.sqrt(dx**2 + dy**2)


def _fdist(pt, x0, x1, y0, y1):
    """Largest distance from a point of the box to pt."""
    dx = max(abs(x0 - pt.real), abs(x1 - pt.real))
    dy = max(abs(y0 - pt.imag), abs(y1 - pt.imag))
    return mp.sqrt(dx**2 + dy**2)


def bound_B(x0, x1, y0, y1):
    # boxes entirely inside |G| <= r* need no work: region A covers them
    if _fdist(W, x0, x1, y0, y1)/_dist(WB, x0, x1, y0, y1) <= R_STAR:
        return mp.mpf(0)
    # |G| = |z-w|/|z-conj w|: bound below by min distance to w over max distance to conj w
    r_lo = _dist(W, x0, x1, y0, y1)/_fdist(WB, x0, x1, y0, y1)
    r_used = max(r_lo, R_STAR)          # points with |G| < r* are covered by region A
    dist = _dist(WB, x0, x1, y0, y1)    # for the |dG/dz| bound
    xc, yc = (x0 + x1)/2, (y0 + y1)/2
    z = mp.mpc(xc, yc)
    Dv = bloch_wigner(z)
    G = (z - W)/(z - WB)
    r = abs(G)
    P4 = V0 - C2*r**2 + C3*mp.re(G**3) + C4*r**4
    Rc = abs(Dv.v - P4) + Dv.err
    rad = mp.sqrt(((x1 - x0)/2)**2 + ((y1 - y0)/2)**2)
    Gd = grad_bound(x0, x1, y0, y1)
    Gp = (2*C2 + 3*C3 + 4*C4)*mp.sqrt(3)/dist**2
    return (Rc + (Gd + Gp)*rad)/r_used**5


def cover(target, xmax=120, ymax=120, depth_max=40, cap=4000000):
    state = {'worst': mp.mpf(0), 'box': None, 'n': 0, 'unresolved': 0, 'over': False}

    def visit(x0, x1, y0, y1, depth):
        """Record the worst bound over LEAVES -- boxes that pass or hit the depth limit -- not
        over every box visited, or the answer is just the largest coarse box."""
        state['n'] += 1
        if state['n'] > cap:
            state['over'] = True
            return
        b = bound_B(x0, x1, y0, y1)
        if b <= target or depth >= depth_max:
            if b > state['worst']:
                state['worst'], state['box'] = b, (x0, x1, y0, y1, depth)
            if b > target:
                state['unresolved'] += 1
            return
        if state['n'] % 200000 == 0:
            print(f'    ... {state["n"]} boxes, leaves so far worst {mp.nstr(state["worst"], 8)}', flush=True)
        xm, ym = (x0 + x1)/2, (y0 + y1)/2
        if x1 - x0 >= y1 - y0:                 # bisect the longer side
            visit(x0, xm, y0, y1, depth + 1)
            visit(xm, x1, y0, y1, depth + 1)
        else:
            visit(x0, x1, y0, ym, depth + 1)
            visit(x0, x1, ym, y1, depth + 1)

    xs, x = [], -xmax
    while x < xmax:
        w = 4 if abs(x) > 8 else 1
        xs.append((x, min(x + w, xmax)))
        x += w
    ys, y = [], mp.mpf('1e-5')
    while y < ymax:
        ys.append((y, min(y*1.5, ymax)))
        y = y*1.5
    for x0, x1 in xs:
        for y0, y1 in ys:
            visit(mp.mpf(x0), mp.mpf(x1), mp.mpf(y0), mp.mpf(y1), 0)
    return state


def _worker(args):
    """One column of the initial grid: returns (worst leaf bound, box count, unresolved)."""
    x0, x1, target, depth_max = args
    import mpmath as _mp
    _mp.mp.dps = mp.mp.dps
    st = {'worst': mp.mpf(0), 'box': None, 'n': 0, 'unresolved': 0}
    ys, y = [], mp.mpf('1e-5')
    ymax = 120
    while y < ymax:
        ys.append((y, min(y*1.5, ymax)))
        y = y*1.5

    def visit(a0, a1, b0, b1, depth):
        st['n'] += 1
        v = bound_B(a0, a1, b0, b1)
        if v <= target or depth >= depth_max:
            if v > st['worst']:
                st['worst'], st['box'] = v, (a0, a1, b0, b1, depth)
            if v > target:
                st['unresolved'] += 1
            return
        am, bm = (a0 + a1)/2, (b0 + b1)/2
        if a1 - a0 >= b1 - b0:
            visit(a0, am, b0, b1, depth + 1)
            visit(am, a1, b0, b1, depth + 1)
        else:
            visit(a0, a1, b0, bm, depth + 1)
            visit(a0, a1, bm, b1, depth + 1)

    for b0, b1 in ys:
        visit(x0, x1, b0, b1, 0)
    return st


if __name__ == '__main__':
    print(f'Taylor order K = {K};  region A for |G| <= {mp.nstr(R_STAR, 3)}')
    for r in ['0.05', '0.1', '0.2', '0.3', '0.4', '0.5']:
        print(f'   r = {r:5s}   |R|/|G|^5 <= {mp.nstr(bound_A(mp.mpf(r)), 9)}')
    ca = max(bound_A(R_STAR*mp.mpf(i)/100) for i in range(1, 101))
    print(f'   C_A = max over |G| <= {mp.nstr(R_STAR,3)}: {mp.nstr(ca, 10)}')
    print()
    print(f'region B, |G| >= {mp.nstr(R_STAR, 3)}: covering with target {mp.nstr(ca, 9)} ...')
    target_b = max(ca, mp.mpf(__import__('os').environ.get('C2_TARGET', '0.70')))
    print(f'   (cover target {mp.nstr(target_b, 8)})')
    st = cover(target_b)
    print(f'   boxes visited {st["n"]}, unresolved at the depth limit {st["unresolved"]}'
          + ('  [OVER THE CAP]' if st['over'] else ''))
    print(f'   worst box {st["box"]}')
    print(f'   C_B = {mp.nstr(st["worst"], 10)}')
    print()
    print(f'C = {mp.nstr(max(ca, st["worst"]), 10)}')

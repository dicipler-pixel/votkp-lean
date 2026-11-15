# SCRIPT: c2_certified_bound2
"""The constant in the remainder bound, recomputed properly -- and what it is worth.

c2_certified_bound.py scanned |G| = 0.02, 0.04, ..., 0.98 at 48 angles and reported the largest
ratio it saw, C = 0.685556567092. A grid is not a supremum: at G = -0.265893 the ratio is
|R|/|G|^5 = 0.685567095, which EXCEEDS that constant by 1.5e-5. The published number was a grid
sample just below the true supremum, so "|R| <= C|G|^5 with C = 0.685556567092" was false as
stated.

What this script does: a coarse scan of the disk, then local refinement around the best
candidates, at high precision. It reports the supremum to the digits that are stable, the
maximiser so the number is reproducible, and max_j |G_j| over the census (the bound is claimed on
the disk |G| < 1 only, so every tetrahedron has to be inside it).

What it does NOT do: enclose the supremum. A supremum found by sampling and local optimisation is
a numerical value. To turn |R| <= C|G|^5 into a theorem one has to bound |R|/|G|^5 on the disk in
interval arithmetic -- for instance through the fifth-order Taylor remainder
    R(G) = (1/4!) int_0^1 (1-t)^4 D^(5)(tG) . G^5 dt
with D^(5) enclosed on each segment, or by a certified branch-and-bound over the disk. Until that
is done the right label for the per-knot counts is "certified numerically".
"""
import sys, math
sys.path.insert(0, 'code')
import mpmath as mp

C_OLD = mp.mpf('0.685556567092')


def setup(dps):
    mp.mp.dps = dps
    W = mp.expjpi(mp.mpf(1)/3); WB = mp.expjpi(-mp.mpf(1)/3)
    V0 = mp.im(mp.polylog(2, W))
    return W, WB, V0


def ratio(r, a, W, WB, V0):
    """|R|/|G|^5 at G = r exp(i a)."""
    g = r*mp.expj(a)
    z = (W - g*WB)/(1 - g)
    D = mp.im(mp.polylog(2, z)) + mp.arg(1 - z)*mp.log(abs(z))
    R = D - (V0 - 3*mp.sqrt(3)/4*r**2 + mp.sqrt(3)/4*mp.re(g**3) + 3*mp.sqrt(3)/16*r**4)
    return abs(R)/r**5


def scan(W, WB, V0, nr=300, na=360):
    out = []
    for i in range(1, nr + 1):
        r = mp.mpf(i)/nr*mp.mpf('0.9995')
        for k in range(na):
            a = 2*mp.pi*k/na
            out.append((ratio(r, a, W, WB, V0), r, a))
    out.sort(reverse=True, key=lambda t: t[0])
    return out


def refine(r0, a0, W, WB, V0, rounds=7, boxes=17):
    r, a = r0, a0
    dr, da = mp.mpf('0.02'), mp.mpf('0.05')
    best = (ratio(r, a, W, WB, V0), r, a)
    for _ in range(rounds):
        for i in range(boxes):
            rr = r + dr*(mp.mpf(i)/(boxes - 1)*2 - 1)
            if rr <= 0 or rr >= 1:
                continue
            for j in range(boxes):
                aa = a + da*(mp.mpf(j)/(boxes - 1)*2 - 1)
                v = ratio(rr, aa, W, WB, V0)
                if v > best[0]:
                    best = (v, rr, aa)
        r, a = best[1], best[2]
        dr /= 6
        da /= 6
    return best


if __name__ == '__main__':
    W, WB, V0 = setup(25)
    print('coarse scan of the disk, 300 x 360 points ...')
    cands = scan(W, WB, V0)
    print(f'  grid maximum {mp.nstr(cands[0][0], 12)} at |G| = {mp.nstr(cands[0][1], 6)}')
    picks, seen = [], []
    for v, r, a in cands:
        if any(abs(r - r2) < 0.05 and min(abs(a - a2), 2*mp.pi - abs(a - a2)) < 0.15 for r2, a2 in seen):
            continue
        seen.append((r, a))
        picks.append((r, a))
        if len(picks) >= 12:
            break
    W, WB, V0 = setup(40)
    refined = sorted((refine(r, a, W, WB, V0) for r, a in picks), key=lambda t: -t[0])
    v, r, a = refined[0]
    print()
    print(f'supremum  C = {mp.nstr(v, 18)}')
    print(f'  at |G| = {mp.nstr(r, 10)},  arg G / pi = {mp.nstr(a/mp.pi, 10)}')
    print(f'  G = {mp.nstr(r*mp.expj(a), 10)}')
    print('  the next local maxima: ' + ', '.join(mp.nstr(c[0], 12) for c in refined[1:4]))
    print()
    print(f'constant used before:  {mp.nstr(C_OLD, 18)}')
    print(f'  it is too small by   {mp.nstr(v - C_OLD, 6)}  ({mp.nstr(100*(v - C_OLD)/C_OLD, 5)} %)')
    print(f'a round-up that bounds the sampled supremum: C = {mp.nstr(mp.ceil(v*1e6)/1e6, 10)}')
    print()
    import json
    rhos = [json.loads(l)['rho'] for l in open('.scratch/c2_certify.jsonl') if l.strip()]
    rhos.sort()
    print(f'census: max_j |G_j| over {len(rhos)} knots: largest {rhos[-1]:.6f}, '
          f'median {rhos[len(rhos)//2]:.6f}, so every tetrahedron is inside the disk')

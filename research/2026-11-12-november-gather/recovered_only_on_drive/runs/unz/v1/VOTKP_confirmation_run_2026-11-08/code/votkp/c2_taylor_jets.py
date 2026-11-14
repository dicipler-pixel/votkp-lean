# SCRIPT: c2_taylor_jets
"""The Taylor series of D in the shape coordinate G, to order N, by jet arithmetic.

Near G = 0 -- the regular tetrahedron -- a box cover is hopeless: the map z(G) = (w - G wbar)/(1-G)
sends a neighbourhood of 0 to the deep point w = e^{i pi/3}, where |z| is almost 1 and the series
for Li2 needs hundreds of thousands of terms. But the expansion of D *in G* converges
geometrically there. So the two regions need opposite tools:

    |G| <= r*   the G-expansion, exact coefficients plus a harmonic tail bound
    |G| >= r*   boxes: a certified value of D at the centre and a bound on its gradient

This script builds the first. D = Im Li2(z) + arg(1-z) log|z| with z = (w - G wbar)/(1 - G). Since
z is holomorphic in G, so are Li2(z), log(1-z) and log z; write them as univariate jets in G, use
their conjugates as jets in Gbar, and assemble

    D = [Li2(z)/(2i) + log(1-z) log(z)/(4i)] + conjugate
        + (1/(4i))[ log(1-z) conj(log z) - conj(log(1-z)) log(z) ]

The first coefficients must reproduce V0 - (3 sqrt3/4)|G|^2 + (sqrt3/4)Re(G^3) + (3 sqrt3/16)|G|^4,
which is the check that the construction is right.
"""
import sys
sys.path.insert(0, 'code')
sys.path.insert(0, 'code/votkp')
import mpmath as mp
from c2_enclosure_lib import li2, W, WB, V0

mp.mp.dps = 50
N = 40


def jzero():
    return [mp.mpc(0)]*(N + 1)


def jmul(a, b):
    c = jzero()
    for i in range(N + 1):
        if a[i]:
            for j in range(N + 1 - i):
                if b[j]:
                    c[i + j] += a[i]*b[j]
    return c


def jdiv(a, b):
    c = jzero()
    for i in range(N + 1):
        s = a[i]
        for j in range(1, i + 1):
            s -= b[j]*c[i - j]
        c[i] = s/b[0]
    return c


def jint(a):
    return [mp.mpc(0)] + [a[i - 1]/i for i in range(1, N + 1)]


def jder(a):
    return [i*a[i] for i in range(1, N + 1)] + [mp.mpc(0)]


def jets():
    """The univariate jets in G of z, log z, log(1-z), Li2(z)."""
    d = W - WB
    z = [W] + [d]*N
    zp = jder(z)
    omz = [1 - z[0]] + [-z[k] for k in range(1, N + 1)]
    logz = jint(jdiv(zp, z));                   logz[0] = mp.log(W)
    log1mz = jint([-x for x in jdiv(zp, omz)]); log1mz[0] = mp.log(1 - W)
    li2z = jint([-x for x in jmul(log1mz, jdiv(zp, z))]); li2z[0] = li2(W).v
    return z, logz, log1mz, li2z


if __name__ == '__main__':
    z, logz, log1mz, li2z = jets()
    conj = lambda a: [mp.conj(x) for x in a]

    D = {}

    def add(a, b, v):
        D[(a, b)] = D.get((a, b), 0) + v

    for k in range(N + 1):
        if li2z[k]:
            add(k, 0, li2z[k]/(2j))
            add(0, k, -mp.conj(li2z[k])/(2j))
    p = jmul(log1mz, logz)
    for k in range(N + 1):
        if p[k]:
            add(k, 0, p[k]/(4j))
            add(0, k, -mp.conj(p[k])/(4j))
    lz_c, l1mz_c = conj(logz), conj(log1mz)
    for k in range(N + 1):
        if log1mz[k]:
            for j in range(N + 1 - k):
                if lz_c[j]:
                    add(k, j, log1mz[k]*lz_c[j]/(4j))
        if l1mz_c[k]:
            for j in range(N + 1 - k):
                if logz[j]:
                    add(j, k, -l1mz_c[k]*logz[j]/(4j))

    print('D(G) = sum c[a,b] G^a Gbar^b, by total degree:')
    S = {}
    for k in range(0, N + 1):
        row = [(a, k - a, D.get((a, k - a), 0)) for a in range(k + 1)]
        if any(abs(c) > mp.mpf('1e-30') for _, _, c in row):
            print(f'  degree {k}:')
            for a, b, c in row:
                if abs(c) > mp.mpf('1e-30'):
                    print(f'    G^{a} Gbar^{b}: {mp.nstr(c, 14)}')
            S[k] = sum(abs(c) for _, _, c in row)
    print()
    print('  S_k = sum of the coefficient moduli at degree k, i.e. a bound on |P_k(G)| at |G| = 1:')
    for k in sorted(S):
        print(f'    S_{k} = {mp.nstr(S[k], 10)}')
    # the coefficients themselves, for the sharp (per-angle) bound in c2_enclosure.py
    coeffs = {f'{a},{b}': [mp.nstr(mp.re(c), 25), mp.nstr(mp.im(c), 25)]
              for (a, b), c in D.items() if abs(c) > mp.mpf('1e-30')}
    json_out = {'S': {k: mp.nstr(S[k], 20) for k in sorted(S)}, 'coeffs': coeffs}
    import json, os
    os.makedirs('.scratch', exist_ok=True)
    json.dump(json_out, open('.scratch/c2_taylor_S.json', 'w'), indent=1)
    print('  wrote .scratch/c2_taylor_S.json')
    print()
    print('check against the law:')
    print('  c[0,0] =', mp.nstr(D[(0, 0)], 12), '   V0 =', mp.nstr(V0, 12))
    print('  c[1,1] =', mp.nstr(D[(1, 1)], 12), '   -3sqrt3/4 =', mp.nstr(-3*mp.sqrt(3)/4, 12))
    print('  c[3,0] =', mp.nstr(D.get((3, 0), 0), 12), '   sqrt3/8 =', mp.nstr(mp.sqrt(3)/8, 12))
    print('  c[2,2] =', mp.nstr(D[(2, 2)], 12), '   3sqrt3/16 =', mp.nstr(3*mp.sqrt(3)/16, 12))

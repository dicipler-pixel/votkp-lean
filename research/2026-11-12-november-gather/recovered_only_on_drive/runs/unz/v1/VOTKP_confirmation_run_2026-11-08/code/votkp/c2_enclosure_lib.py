# SCRIPT: c2_enclosure_lib
"""A rigorous enclosure of D(z) and of its gradient: the pieces the C2c certificate needs.

D(z) = Im Li2(z) + arg(1-z) log|z|, the Bloch-Wigner dilogarithm (the volume of an ideal
tetrahedron of shape z in the upper half plane). What is needed for C2c is (i) a value of D at a
point that comes with an error bound, and (ii) a bound on |grad D| over a box, so that a cover of
the half plane can be checked box by box.

(ii) needs no dilogarithm: starting from

    dbar D = -(i/2) log(1-zbar)/zbar + (i/2) u/(1-zbar) + alpha/(2 zbar),   u = log|z|, alpha = arg(1-z)

(all elementary), one gets |grad D| <= 2(|log(1-z)|/|z| + |u|/|1-z| + |alpha|/|z|).

(i) reduces Li2 at a point to a series that converges fast, using the three identities

    (a) Li2(z) = pi^2/6 - log z log(1-z) - Li2(1-z)
    (b) Li2(z) = -Li2(1/z) - log(-z)^2/2 - pi^2/6
    (c) Li2(z) = -Li2(z/(z-1)) - log(1-z)^2/2

and picking, at each step, whichever image of z has the smallest modulus. Empirically the best of
{z, 1-z, 1/z, z/(z-1)} has modulus <= 0.65 for essentially every z in the upper half plane, so two
applications of an identity followed by at most a few hundred terms of sum z^k/k^2 always suffices;
the tail is bounded by rho^(N+1)/((N+1)^2 (1-rho)).

Error budget. Everything is evaluated with mpmath at 40 digits; the series tail is bounded
explicitly; the rounding errors are collected in EPS = 1e-25, which is twenty-five orders of
magnitude below anything the cover asks for. That is what "enclosed" means here, and the number
EPS is stated rather than hidden.
"""
import mpmath as mp

mp.mp.dps = 40
EPS = mp.mpf('1e-25')
PI = mp.pi
W = mp.expjpi(mp.mpf(1)/3)
WB = mp.expjpi(-mp.mpf(1)/3)
V0 = mp.im(mp.polylog(2, W))          # = 1.0149416064096536...


class Ball:
    """A complex value that is known to lie within |err| of `v`."""
    __slots__ = ('v', 'err')

    def __init__(self, v, err=EPS):
        self.v, self.err = v, err

    def __add__(self, o):
        o = o if isinstance(o, Ball) else Ball(o, mp.mpf(0))
        return Ball(self.v + o.v, self.err + o.err + EPS)

    def __sub__(self, o):
        o = o if isinstance(o, Ball) else Ball(o, mp.mpf(0))
        return Ball(self.v - o.v, self.err + o.err + EPS)

    def __mul__(self, o):
        v = self.v*o.v
        return Ball(v, abs(v)*(self.err/max(abs(self.v), mp.mpf('1e-300')) + o.err/max(abs(o.v), mp.mpf('1e-300')))
                    + self.err*o.err if self.v and o.v else abs(self.v)*o.err + abs(o.v)*self.err + self.err*o.err)

    def __rmul__(self, k):
        return Ball(k*self.v, abs(k)*self.err)

    def __neg__(self):
        return Ball(-self.v, self.err)

    def __rsub__(self, o):
        return o + (-self)

    def __pow__(self, n):
        v = self.v**n
        return Ball(v, abs(v)*abs(n)*self.err/max(abs(self.v), mp.mpf('1e-300')) + self.err)


    def __truediv__(self, o):
        o = o if isinstance(o, Ball) else Ball(o, mp.mpf(0))
        r = self.v/o.v
        return Ball(r, (self.err + abs(r)*o.err)/abs(o.v) + EPS)

    def __abs__(self):
        return abs(self.v) + self.err


def _series_li2(z):
    """Li2(z) by its series, with an explicit tail bound; |z| < 1."""
    rho = abs(z)
    if rho > mp.mpf('0.9995'):
        raise RuntimeError('series: |z| too close to 1')
    # enough terms that rho^(N+1)/((N+1)^2 (1-rho)) < 1e-28
    N = max(200, int(70/(-mp.log(rho) if rho > 0 else 1)) + 50)
    s = mp.mpc(0)
    t = mp.mpc(1)
    for k in range(1, N + 1):
        t *= z
        s += t/(k*k)
    return Ball(s, rho**(N + 1)/((N + 1)**2*(1 - rho)) + EPS)


def li2(z, depth=0):
    """Li2(z), z not on [1, inf); the value carries an error bound.

    Reduce by whichever of the three identities shrinks |z| most, but never get stuck: above the
    unit circle apply the inversion, below it fall back to the series (which always converges
    there, however slowly near the boundary).
    """
    z = mp.mpc(z)
    if abs(z - W) < mp.mpf('1e-15'):
        # the deep point: every image of w has modulus exactly 1, so no series converges there.
        # Its value is the classical constant Li2(e^{i pi/3}) = pi^2/36 + i Cl2(pi/3); it is taken
        # here from mpmath's polylog at 40 digits, an error far below anything the cover asks for.
        return Ball(mp.polylog(2, W), mp.mpf('1e-30'))
    if depth > 12:
        raise RuntimeError(f'li2: recursion too deep at {z}')
    if abs(z) <= mp.mpf('0.62'):
        return _series_li2(z)
    if abs(z) >= 1:
        b = li2(1/z, depth + 1)
        return -b - Ball(mp.log(-z), EPS)**2/2 - Ball(PI**2/6, EPS)
    opts = {'a': 1 - z, 'c': z/(z - 1)}
    k = min(opts, key=lambda k: abs(opts[k]))
    if abs(opts[k]) < mp.mpf('0.9')*abs(z):
        if k == 'a':
            b = li2(1 - z, depth + 1)
            return Ball(PI**2/6, EPS) - Ball(mp.log(z), EPS)*Ball(mp.log(1 - z), EPS) - b
        b = li2(z/(z - 1), depth + 1)
        return -b - Ball(mp.log(1 - z), EPS)**2/2
    return _series_li2(z)


def bloch_wigner(z):
    """D(z) = Im Li2(z) + arg(1-z) log|z|, with an error bound."""
    z = mp.mpc(z)
    L = li2(z)
    extra = Ball(mp.arg(1 - z), EPS)*Ball(mp.log(abs(z)), EPS)
    val = mp.im(L.v) + mp.re(extra.v)
    return Ball(val, L.err + extra.err + EPS)


def grad_bound(x0, x1, y0, y1):
    """A bound on |grad D| over the box [x0,x1] x i[y0,y1], y0 > 0.

    |dbar D| <= (1/2)(|log(1-z)|/|z| + |u|/|1-z| + |alpha|/|z|) and |grad D| <= 2 sqrt2 |dbar D|;
    every factor is evaluated at its worst corner, which over-estimates and never under-estimates.
    """
    worst = mp.mpf(0)
    for x in (x0, x1):
        for y in (y0, y1):
            z = mp.mpc(x, y)
            az, a1z = abs(z), abs(1 - z)
            if az < mp.mpf('1e-12') or a1z < mp.mpf('1e-12'):
                return mp.inf
            u = abs(mp.log(az))
            alpha = abs(mp.atan2(-y, 1 - x))
            lg = abs(mp.log(1 - z))
            v = (lg/az + u/a1z + alpha/az)/2*2*mp.sqrt(2)
            worst = max(worst, v)
    return worst

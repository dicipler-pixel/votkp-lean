"""Rational Taylor enclosures for the cubic 2.2% envelope. Python stdlib only."""

from dataclasses import dataclass
from fractions import Fraction as Q
from math import factorial


@dataclass(frozen=True)
class Interval:
    low: Q
    high: Q

    def __post_init__(self):
        assert self.low <= self.high

    def __add__(self, rhs):
        rhs = interval(rhs)
        return Interval(self.low + rhs.low, self.high + rhs.high)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.high, -self.low)

    def __sub__(self, rhs):
        return self + -interval(rhs)

    def __mul__(self, rhs):
        rhs = interval(rhs)
        corners = [a * b for a in (self.low, self.high) for b in (rhs.low, rhs.high)]
        return Interval(min(corners), max(corners))

    __rmul__ = __mul__

    def __truediv__(self, rhs):
        rhs = interval(rhs)
        assert rhs.low > 0
        return self * Interval(1 / rhs.high, 1 / rhs.low)

    def __pow__(self, n):
        assert n >= 0
        result = interval(1)
        for _ in range(n):
            result = result * self
        return result


def interval(x):
    return x if isinstance(x, Interval) else Interval(Q(x), Q(x))


def atan(unit):
    # At |x|≤1 alternating remainders lie between consecutive sums.
    total = Q(0)
    for j in range(17):
        total += (-1) ** j * unit ** (2 * j + 1) / (2 * j + 1)
    neighbor = total - unit**35 / 35
    return Interval(neighbor, total)


def positive_root(x, order):
    # Find rational outward enclosures by exact bisection of each endpoint.
    def bracket(target):
        lo, hi = Q(0), max(Q(1), target)
        for _ in range(90):
            mid = (lo + hi) / 2
            if mid**order < target:
                lo = mid
            else:
                hi = mid
        assert lo**order <= target <= hi**order
        return lo, hi

    return Interval(bracket(x.low)[0], bracket(x.high)[1])


def trig(argument, odd):
    # Degree-32 Taylor polynomial. All derivatives of sin and cos are bounded
    # in absolute value by one, so the degree-32 remainder is ≤ |x|³³/33!.
    coeff = [Q(0)] * 33
    for n in range(int(odd), 33, 2):
        coeff[n] = Q((-1) ** ((n - int(odd)) // 2), factorial(n))
    value = interval(coeff[-1])
    for a in reversed(coeff[:-1]):
        value = value * argument + a
    error = max(abs(argument.low), abs(argument.high)) ** 33 / factorial(33)
    return value + Interval(-error, error)


def outward(x, places=10):
    scale = 10**places
    low = (x.low * scale).__floor__()
    high = (x.high * scale).__ceil__()

    def fmt(n):
        sign = "-" if n < 0 else ""
        n = abs(n)
        return f"{sign}{n // scale}.{n % scale:0{places}d}"

    return f"[{fmt(low)}, {fmt(high)}]"


def main():
    # Machin's identity follows by tangent addition, with 4 atan(1/5)−atan(1/239)
    # in the first quadrant and tangent one.
    pi = 16 * atan(Q(1, 5)) - 4 * atan(Q(1, 239))
    root3 = positive_root(interval(3), 2)
    q = positive_root(6 * pi**2, 3) / 2
    x = q * root3
    f = 3 * (trig(x, True) - x * trig(x, False)) / (x**3)
    eta = Q(22, 1000)
    qp = (1 + eta) * q
    qm = (1 - eta) * q
    assert (2 * (qp**2)).high < (pi**2).low
    lower = trig(qp, False)
    upper = trig(qm / root3, False) ** 3
    width = upper - lower
    moved = interval(1 - (1 - eta) ** 3)
    amplitude_floor = f - moved * width
    assert lower.high < 0 < upper.low and amplitude_floor.low > 0
    bound = 8 * amplitude_floor**2
    assert (
        f.low >= Q(238, 1000)
        and width.high <= Q(505, 1000)
        and moved.high <= Q(65, 1000)
    )
    assert bound.low > Q(3382887, 10000000) > Q(1, 3)
    for name, value in [
        ("pi", pi),
        ("k0 a/2", q),
        ("spherical amplitude", f),
        ("spherical shell fraction", 8 * f**2),
        ("kernel lower bound", lower),
        ("kernel upper bound", upper),
        ("kernel range", width),
        ("moved fraction bound", moved),
        ("shell fraction lower bound", bound),
    ]:
        print(name, outward(value))


if __name__ == "__main__":
    main()

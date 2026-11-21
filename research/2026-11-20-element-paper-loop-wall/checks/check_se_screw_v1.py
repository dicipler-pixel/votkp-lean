# SCRIPT: CHECK-SE-SCREW-SIGN-01
# Trigonal selenium, P3_121, COD 1534711: a = 4.30 A, c = 4.89 A, u = 0.218.
# Four successive chain sites on the 3_1 screw axis through the origin. chi = (d0 x d1) . d2.
# Pass rule: chi keeps its sign when the path is reversed and flips under a spatial mirror.
import math
a, c, u = 4.30, 4.89, 0.218
P = [(a*u*math.cos(2*math.pi*j/3), a*u*math.sin(2*math.pi*j/3), j*c/3) for j in range(4)]
sub = lambda p, q: tuple(x-y for x, y in zip(p, q))
cross = lambda p, q: (p[1]*q[2]-p[2]*q[1], p[2]*q[0]-p[0]*q[2], p[0]*q[1]-p[1]*q[0])
dot = lambda p, q: sum(x*y for x, y in zip(p, q))
def chi(pts):
    d = [sub(pts[i+1], pts[i]) for i in range(3)]
    return dot(cross(d[0], d[1]), d[2])
print('bond length', round(math.dist(P[0], P[1]), 5), 'A (COD shortest contact 2.30066 A)')
print('chi forward', round(chi(P), 4))
print('chi reversed path', round(chi(P[::-1]), 4))
print('chi after mirror x -> -x', round(chi([(-p[0], p[1], p[2]) for p in P]), 4))

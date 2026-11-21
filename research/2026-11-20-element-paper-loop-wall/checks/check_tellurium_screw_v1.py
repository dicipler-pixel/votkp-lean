# SCRIPT: CHECK-TELLURIUM-SCREW-SIGN-01
# Independent check of Codex's tellurium screw signs, two ways:
# (1) explicit chain points on a 3-fold screw about the c axis, chi = (d0 x d1) . d2;
# (2) the closed form chi = s (3 sqrt3 / 2) c (a u)^2, bond^2 = 3 (a u)^2 + c^2 / 9.
# Pass rule: both routes agree, reversal keeps chi, a mirror flips it.
import math
def chain(a, c, u, s):
    r = abs(a*u)
    return [(r*math.cos(s*2*math.pi*j/3), r*math.sin(s*2*math.pi*j/3), j*c/3) for j in range(4)]
sub = lambda p, q: tuple(x-y for x, y in zip(p, q))
cross = lambda p, q: (p[1]*q[2]-p[2]*q[1], p[2]*q[0]-p[0]*q[2], p[0]*q[1]-p[1]*q[0])
dot = lambda p, q: sum(x*y for x, y in zip(p, q))
def chi(P):
    d = [sub(P[i+1], P[i]) for i in range(3)]
    return dot(cross(d[0], d[1]), d[2])
for name, a, c, u, s in [('tellurium, P3_1 21 (COD 2020222, 1989)', 4.456, 5.921, -0.2636, +1),
                         ('tellurium, P3_2 21 (COD 9008580, 1963)', 4.44693, 5.91492, 0.269, -1),
                         ('selenium, P3_1 21 (COD 1534711), control', 4.30, 4.89, 0.218, +1)]:
    P = chain(a, c, u, s)
    closed = s*1.5*math.sqrt(3)*c*(a*u)**2
    print(name)
    print('  bond', round(math.dist(P[0], P[1]), 6), 'A; closed form', round(math.sqrt(3*(a*u)**2 + c*c/9), 6))
    print('  chi', round(chi(P), 6), ' closed form', round(closed, 6), ' reversed', round(chi(P[::-1]), 6),
          ' mirror', round(chi([(p[0], -p[1], p[2]) for p in P]), 6))

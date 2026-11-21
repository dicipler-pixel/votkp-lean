# SCRIPT: LAMBERT-JUMP-CHECK-01
# Two-face rule tested by plain disk geometry, never using sinh*sinh.
# Corner at the origin of the Poincare disk; face a along the real axis, face b along the imaginary axis.
# Each face of ratio z sits at hyperbolic distance h = ln(z)/2 from the corner (Euclidean radius r = tanh(h/2)).
# Draw the geodesic through that point perpendicular to its axis (a circle orthogonal to the unit circle).
# The loop closes iff the two perpendicular geodesics meet (two circles intersect).
import math
def perp_circle(z):
    h = 0.5*math.log(z); r = math.tanh(h/2)
    c = (1+r*r)/(2*r); R = (1-r*r)/(2*r)      # centre distance and radius, from c - R = r and c^2 = 1 + R^2
    return c, R
def closes(za, zb):
    ca, Ra = perp_circle(za); cb, Rb = perp_circle(zb)
    return math.hypot(ca, cb) < Ra + Rb          # centres on perpendicular axes
# carbon: 4th to 5th removal (last 2s electron, then first 1s electron of the closed helium-like core)
# nitrogen: 5th to 6th removal (same two steps)
C, N = 392.09056/64.49352, 552.06741/97.8901   # full archive values
print('carbon helium-core opening ratio', round(C,5), ' nitrogen helium-core opening ratio', round(N,5))
for name, za, zb in [('carbon face with carbon face',C,C), ('nitrogen face with nitrogen face',N,N), ('carbon face with nitrogen face',C,N)]:
    print(name + ':', 'loop closes' if closes(za,zb) else 'loop open')
lo, hi = 1.0001, 50.0                            # sweep the second face with C held fixed
for _ in range(200):
    mid = (lo+hi)/2
    (lo, hi) = (mid, hi) if closes(C, mid) else (lo, mid)
print('carbon face held fixed, second face swept: loop opens at z =', round(lo, 6))
lo, hi = 1.0001, 50.0
for _ in range(200):
    mid = (lo+hi)/2
    (lo, hi) = (mid, hi) if closes(mid, mid) else (lo, mid)
print('equal faces: loop opens at z =', round(lo, 6), ' 3+2*sqrt2 =', round(3+2*math.sqrt(2), 6))

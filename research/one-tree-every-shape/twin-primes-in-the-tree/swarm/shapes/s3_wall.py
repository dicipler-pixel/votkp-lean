# SCRIPT: TWIN-SHAPES-WALL-01
# Part 3: where does the twin chain meet the wall z = 3 + 2 sqrt2 (G^2 = 1/2)?
# Three readings of 'meet':
#  (i)  one step: a single ratio z = a'/a with G^2 = ((z-1)/(z+1))^2 >= 1/2, i.e. z >= 5.828
#  (ii) one pair of steps on perpendicular arms: tr[A,B] = 2 - 4 sinh^2(r1/2) sinh^2(r2/2) <= -2,
#       i.e. sinh(r1/2) sinh(r2/2) >= 1 (derived in s2: the general pair wall, here gamma = 90 deg)
#  (iii) the chain as a whole: the ball radius of the chain's point, rho = tanh(d/2), crosses 1/sqrt2 (d = ln(3+2sqrt2))
#  (iv) the three books: the summed rapidities L_x, L_y, L_z of each arm, read as one boost each (the books commute
#       inside a book); the pair (L_s, L_t) reaches the wall when sinh(L_s/2) sinh(L_t/2) = 1
# Kill lines, written before the run:
#  K3a 'no single step reaches the wall below 1e9' dies if any step from 11 on has G^2 >= 1/2.
#  K3b 'no consecutive pair reaches the wall' dies if any consecutive perpendicular pair has sinh(r1/2) sinh(r2/2) >= 1.
import numpy as np, math, twinlib as t
T = t.twin_starts(); A = t.arms_digit(T); s3 = math.sqrt(3)
zw = 3 + 2 * math.sqrt(2); dw = math.log(zw)
print('wall: z = %.6f, rapidity ln z = %.6f, G^2 = 1/2' % (zw, dw))
print('early steps (3->5 and 5->11 come before the chain: 3 and 5 carry no arm digit):')
print('   a -> a\'     z        G=(z-1)/(z+1)  G^2     G^2/(1/2)   arm  Thomas turn with previous step')
pre = [(3, 5), (5, 11)]
for a, b in pre:
    z = b / a; G = (z - 1) / (z + 1); print('   %3d -> %3d  %.4f   %.4f        %.4f  %.3f       -' % (a, b, z, G, G * G, 2 * G * G))
Gp = None; ap = None
for i in range(16):
    a, b = T[i], T[i + 1]; z = b / a; G = (z - 1) / (z + 1); arm = 'xyz'[A[i + 1]]
    if Gp is None: tt = '-'
    elif ap == arm: tt = '0 (same arm: the two boosts commute)'
    else: tt = '%.3f deg  (tan(th/2) = G_prev G)' % (2 * math.degrees(math.atan(Gp * G)))
    print('   %3d -> %3d  %.4f   %.4f        %.4f  %.3f       %s    %s' % (a, b, z, G, G * G, 2 * G * G, arm, tt))
    Gp, ap = G, arm
r = np.log(T[1:] / T[:-1]); z = T[1:] / T[:-1]; G2 = ((z - 1) / (z + 1)) ** 2
k = np.argmax(z); print('largest single step from 11 on, below 1e9: %d -> %d, z = %.4f, G^2 = %.4f (wall 0.5)' % (T[k], T[k + 1], z[k], G2[k]))
print('K3a ->', 'KILLED' if (G2 >= 0.5).any() else 'survives (no single step reaches the wall)')
sh = np.sinh(r / 2); arms1 = A[1:]
perp = arms1[1:] != arms1[:-1]; prod = sh[1:] * sh[:-1]
j = np.argmax(np.where(perp, prod, 0)); print('largest consecutive perpendicular pair: sinh(r1/2) sinh(r2/2) = %.4f at %d -> %d -> %d (wall 1)' % (prod[j], T[j], T[j + 1], T[j + 2]))
print('K3b ->', 'KILLED' if (prod[perp] >= 1).any() else 'survives (no consecutive pair reaches the wall)')
# (iii) the chain's own point crosses the wall sphere
L = np.eye(4); path = 0.0; crossed = False; books = np.zeros(3); bookhit = {}
for i in range(60000):
    rr = r[i]; s = A[i + 1]; L = L @ t.boost4(np.eye(3)[s], rr); path += rr; books[s] += rr
    d = math.acosh(L[0, 0])
    if not crossed and d >= dw:
        crossed = True; _, _, R = t.polar(L); ang = math.degrees(t.rot_angle_axis(R)[0])
        print('(iii) the chain\'s point crosses the wall sphere rho = tanh(d/2) = 1/sqrt2 at step %d -> %d: d = %.4f, path L = %.4f, c = %+.4f, frame turn so far %.3f deg (of 12.27 at 1e9)' % (
            T[i], T[i + 1], d, path, d - path / s3, ang))
    for (p, q) in [(0, 1), (0, 2), (1, 2)]:
        if (p, q) not in bookhit and math.sinh(books[p] / 2) * math.sinh(books[q] / 2) >= 1:
            bookhit[(p, q)] = (T[i + 1], books.copy(), path)
for (p, q), (a, b, pth) in sorted(bookhit.items(), key=lambda x: x[1][0]):
    print('(iv) books %s,%s reach the pair wall at twin start %d: L_%s = %.4f, L_%s = %.4f (path %.3f)' % ('xyz'[p], 'xyz'[q], a, 'xyz'[p], b[p], 'xyz'[q], b[q], pth))

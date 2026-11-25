# SCRIPT: PAIR-FAMILIES-CHAIN-01
# The twin chain run on twins, cousins (p,p+4) and sexy primes (p,p+6), arm rule fixed in PREDICTION.txt:
#   arm = allowed mod-5 residues in increasing order -> x, y, z ; SEXY-6 adds sign by p mod 3 (1 -> +, 2 -> -).
# Chain = twinlib.run_chain (2x2 spinor product of boosts cosh(r/2) + sinh(r/2) e.sigma, r = ln(a'/a), arm of a').
# Readout at marks: L = ln(a'/first), d (polar split), frame turn = rotation angle of U, c = d - |P| L.
import numpy as np, math, os, time, twinlib as t
HERE = os.path.dirname(os.path.abspath(__file__))
N = 10**9; S3 = math.sqrt(3); DW = math.log(3 + 2 * math.sqrt(2))      # wall sphere: tanh(d/2) = 1/sqrt2
AX = np.eye(3); OCT = np.vstack([np.eye(3), -np.eye(3)])

def load(g, first):
    a = np.load(os.path.join(HERE, 'pairs_g%d_%d.npy' % (g, N))); return a[a >= first]

def arm3(T, allowed):
    r5 = T % 5; arm = np.full(len(T), -1, np.int64)
    for k, v in enumerate(allowed): arm[r5 == v] = k
    assert (arm >= 0).all(); return arm

FAM = {}
T = load(2, 11); FAM['twins  (g=2)'] = (T, arm3(T, (1, 2, 4)), AX)
T = load(4, 7);  FAM['cousins(g=4)'] = (T, arm3(T, (2, 3, 4)), AX)
T = load(6, 7);  a = arm3(T, (1, 2, 3)); FAM['sexy-3 (g=6)'] = (T, a, AX)
sgn = np.where(T % 3 == 1, 0, 3); FAM['sexy-6 (g=6)'] = (T, a + sgn, OCT)

# arm-rule check against the stated end-digit rule for twins and stated classes for cousins
Tt = FAM['twins  (g=2)'][0]; assert np.array_equal(FAM['twins  (g=2)'][1], t.arms_digit(Tt)), 'twin arm rule != end digit rule'
Tc = FAM['cousins(g=4)'][0]; assert np.array_equal(FAM['cousins(g=4)'][1], np.searchsorted([7, 13, 19], Tc % 30)), 'cousin rule'
print('arm rule check: twins == end-digit rule, cousins == 7,13,19 mod 30 order : OK')

dec = np.array([1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 9.99e8])
def turn(q): return math.degrees(2 * math.atan2(math.sqrt(q[1]**2 + q[2]**2 + q[3]**2), abs(q[0])))

def readout(T, arm, E, nearly=400):
    marks = np.concatenate([T[1:nearly].astype(float), dec]); order = np.argsort(marks, kind='stable')
    rec = t.run_chain(T, arm, E, marks[order], 0.0)
    rec = rec[np.argsort(order, kind='stable')]
    return rec[:nearly - 1], rec[nearly - 1:]

res = {}
for name, (T, arm, E) in FAM.items():
    t0 = time.time(); early, late = readout(T, arm, E)
    P = E[np.bincount(arm[1:], minlength=len(E)) > -1].mean(0) if False else E.mean(0); Pn = np.linalg.norm(P)
    frac = np.bincount(arm, minlength=len(E)) / len(arm)
    print('\n== %s  first start %d, %d pair starts to 1e9, arm shares %s, |P| = %.5f ==' % (name, T[0], len(T), np.round(frac, 5).tolist(), Pn))
    print('   first starts:', T[:10].tolist(), ' arms:', arm[:10].tolist())
    for row in late:
        print('   a\'=%.3e  L=%8.4f  d=%9.5f  d/L=%.5f  c=d-|P|L=%+.5f  turn=%7.4f deg' % (row[0], row[1], row[2], row[2] / row[1], row[2] - Pn * row[1], turn(row[23:27])))
    i5, i9 = 2, 6
    slope = (late[i9, 2] - late[i5, 2]) / (late[i9, 1] - late[i5, 1])
    print('   slope 1e5->1e9 = %.5f  (|P| = %.5f, miss %.1e)   d(1e9)-d(1e5) = %.4f' % (slope, Pn, abs(slope - Pn), late[i9, 2] - late[i5, 2]))
    w = np.nonzero(early[:, 2] >= DW)[0]
    if len(w):
        j = w[0]; pa = T[j] if j > 0 else T[0]
        print('   wall crossing (d >= %.4f): step %d -> %d, L* = %.4f, d = %.4f, turn so far %.3f deg' % (DW, T[j], T[j + 1], early[j, 1], early[j, 2], turn(early[j, 23:27])))
        wall = (int(T[j + 1]), early[j, 1])
    else:
        print('   wall: not crossed in the first %d steps' % len(early)); wall = (None, None)
    res[name] = dict(slope=slope, Pn=Pn, turn9=turn(late[i9, 23:27]), turn7=turn(late[4, 23:27]), c9=late[i9, 2] - Pn * late[i9, 1], wall=wall,
                     turns=[turn(r[23:27]) for r in late])
    print('   (%.1fs)' % (time.time() - t0))

# ---- drop-first control: start each 3-arm family one member later (does the small end set the turn?)
print('\n== drop-first control: chain started at the 2nd / 3rd member ==')
for name in ['twins  (g=2)', 'cousins(g=4)', 'sexy-3 (g=6)']:
    T, arm, E = FAM[name]
    s = []
    for k in (0, 1, 2):
        _, late = readout(T[k:], arm[k:], E, nearly=3); s.append('start %d: %.4f' % (T[k], turn(late[6, 23:27])))
    print('   %s  turn at 1e9 ->  %s' % (name, ' | '.join(s)))

# ---- K4 ensemble: same gap sequence to 1e7, arms iid uniform over the family's arm set
print('\n== K4: arm-scramble ensemble on the real gap sequence (to 1e7, 400 draws each) ==')
rng = np.random.default_rng(20261125)
for name, (T, arm, E) in FAM.items():
    T7 = T[T <= 10**7 + 100]; mk = np.array([9.99e6])
    real = turn(t.run_chain(T7, arm[:len(T7)], E, mk, 0.0)[0, 23:27])
    ens = np.array([turn(t.run_chain(T7, rng.integers(0, len(E), len(T7)).astype(np.int64), E, mk, 0.0)[0, 23:27]) for _ in range(400)])
    z = (real - ens.mean()) / ens.std()
    print('   %s real turn(1e7) %.4f   ensemble mean %.3f sd %.3f  [5%%,95%%] = [%.2f, %.2f]   z = %+.2f  -> K4 %s'
          % (name, real, ens.mean(), ens.std(), *np.percentile(ens, [5, 95]), z, 'KILLED' if abs(z) > 3 else 'survives'))

print('\n== summary side by side ==')
print('   family         turn(1e7)  turn(1e9)   slope    c(1e9)    wall start  L*')
for name, r in res.items():
    print('   %s  %8.4f  %8.4f   %.5f  %+.5f   %s  %s' % (name, r['turn7'], r['turn9'], r['slope'], r['c9'], r['wall'][0], None if r['wall'][1] is None else round(r['wall'][1], 4)))
print('\n   turn by decade (1e3,1e4,...,1e8,1e9):')
for name, r in res.items(): print('   %s ' % name + '  '.join('%.4f' % x for x in r['turns']))
tw, co = res['twins  (g=2)'], res['cousins(g=4)']
print('\nK1 cousins slope miss %.1e, sexy-3 slope miss %.1e -> %s' % (abs(co['slope'] - co['Pn']), abs(res['sexy-3 (g=6)']['slope'] - 1 / S3),
      'KILLED' if max(abs(co['slope'] - co['Pn']), abs(res['sexy-3 (g=6)']['slope'] - 1 / S3)) > 0.005 else 'survives'))
print('K2 |turn cousins - turn twins| at 1e9 = %.4f deg -> %s' % (abs(co['turn9'] - tw['turn9']), 'my prediction KILLED' if abs(co['turn9'] - tw['turn9']) < 0.3 else 'survives'))

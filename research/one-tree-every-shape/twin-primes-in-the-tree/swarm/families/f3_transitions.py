# SCRIPT: PAIR-FAMILIES-TRANSITIONS-01
# Why does sexy-3 settle slowly? Consecutive-arm statistics: share of steps whose arm repeats the previous arm
# (repeat steps commute: no Thomas turn), and the 3x3 transition shares, per family, for starts in [1e8, 1e9].
import numpy as np, os
HERE = os.path.dirname(os.path.abspath(__file__)); N = 10**9
for name, g, first, allowed in [('twins  ', 2, 11, (1, 2, 4)), ('cousins', 4, 7, (2, 3, 4)), ('sexy-3 ', 6, 7, (1, 2, 3))]:
    T = np.load(os.path.join(HERE, 'pairs_g%d_%d.npy' % (g, N))); T = T[T >= first]
    arm = np.searchsorted(np.array(allowed), T % 5)
    sel = T[1:] >= 10**8; a0, a1 = arm[:-1][sel], arm[1:][sel]
    M = np.zeros((3, 3)); np.add.at(M, (a0, a1), 1); M /= M.sum()
    gap = (T[1:] - T[:-1])[sel]
    print('%s  repeat share %.4f (iid 0.3333)   share of gap = 6: %.4f   transition shares (row = from x,y,z):' % (name, np.trace(M), np.mean(gap == 6)))
    for i in range(3): print('          ' + '  '.join('%.4f' % v for v in M[i]))

# SCRIPT: NU3D-CHECK-01 — are these Steve's Figure 1 runs?
# Kill line, fixed before the run: each of my diag tables must have the same number of rows as the one he archived in his repository
# (paper/figs/dyn_data.npz 'fluid' and 'nu', paper/figs/dyn_nu0535.npy) and agree with it in every column to 1e-9 (relative); and each run
# must end as his did: the fluid run and 0.535 form a horizon (status BH), 0.51 with neutrinos runs to eps = 9 without one (status undecided).
# Why it proves it: the diag rows are computed by his own diag function from his own state at the same steps; any difference in the code,
# the settings or the numerics would change them. Matching to round-off means the 3D frames come from the same runs as his figure.
import sys, numpy as np
FIG = sys.argv[1]; fails = 0
def say(ok, s):
    global fails; print(('HOLDS  ' if ok else 'KILLED ') + s); fails += (not ok)
ref = np.load(FIG + '/dyn_data.npz'); refs = { 'fluid':ref['fluid'], 'nu':ref['nu'], 'nu535':np.load(FIG + '/dyn_nu0535.npy') }
for tag in ['fluid', 'nu', 'nu535']:
    mine = np.load('diag_' + tag + '.npy'); r = refs[tag]
    same = mine.shape == r.shape; dev = np.max(np.abs(mine - r)/np.maximum(1e-12, np.abs(r))) if same else float('inf')
    say(same and dev < 1e-9, '(a) %s: my diag table %s against his archived %s, largest relative difference %.1e' % (tag, mine.shape, r.shape, dev))
    d = np.load('shells_' + tag + '.npz'); st = str(d['status'])
    want = { 'fluid':'BH', 'nu':'undecided', 'nu535':'BH' }[tag]
    say(st == want, '(b) %s ends as his run: status %s at eps %.3f (expected %s), %d frames from eps %.3f' % (tag, st, float(d['eps_end']), want, len(d['eps']), float(d['eps'][0])))
print(('%d KILLED' % fails) if fails else 'all hold')

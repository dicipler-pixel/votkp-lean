# SCRIPT: BALLS-MIXER-V4-EXPECTED-01
# Why this decides it: the two knot eyes show each number by more than one route. Here the routes are computed away
# from the page. If a route disagrees, that readout is not built.
# KILL LINES (written before the run):
#  N1 T(2,n), n = 3..13 odd, ratio t in {1.5, 2, 3, 5, 7}: symmetrised Alexander three ways:
#     polynomial sum(-1)^k t^k / t^((n-1)/2);  cosh(n r/2)/cosh(r/2), r = ln t;  t^(-(n-1)/2) (1-G1)/(1-Gn), G_L = (t^L-1)/(t^L+1).
#     kill if any pair differs by more than 1e-25 (relative). Also t -> 1/t must give the same value (blind to reversal).
#  N2 n = 7: the same quantity equals x^3 - x^2 - 2x + 1 at x = t + 1/t (the Knot Mirror handoff polynomial); kill above 1e-25.
#  N3 turn side: Levine-Tristram signature of T(2,n) from its Seifert matrix at angle theta equals 2 x (number of zeros
#     (2j+1) 180/n below theta), for n = 3..13 and 60 angles; mirror gives the negative; kill on any mismatch.
#  N4 the 20-crossing braid of Brittenham and Hermiller: signature 0, Alexander polynomial = (that of 7_1)^2,
#     determinant 49; after changing entries 0 and 1 the knot is K14a18636. kill if any of the four fails.
#  N5 7_1 # 7_1 (braid s1^7 s3^7 joined): signature magnitude 12. kill otherwise.
from mpmath import mp, mpf, cosh, log
import numpy as np, json
mp.dps = 40; out = {}
worst = 0; wrev = 0
for n in range(3, 15, 2):
    for t in ('1.5','2','3','5','7'):
        t = mpf(t); r = log(t); h = (n-1)//2
        def alex(t): return sum((-1)**k * t**k for k in range(n)) / t**h
        a = alex(t); b = cosh(n*r/2)/cosh(r/2); G = lambda L: (t**L-1)/(t**L+1); c = t**(-h)*(1-G(1))/(1-G(n))
        worst = max(worst, abs(a-b)/abs(a), abs(a-c)/abs(a)); wrev = max(wrev, abs(alex(1/t)-a)/abs(a))
        if n == 7: x = t+1/t; out.setdefault('N2', 0); out['N2'] = max(out['N2'], float(abs(x**3-x**2-2*x+1-a)/abs(a)))
print('N1 worst', mp.nstr(worst,5), 'reversal', mp.nstr(wrev,5), 'KILL' if max(worst,wrev) > mpf(10)**-25 else 'not hit')
print('N2 worst', out['N2'], 'KILL' if out['N2'] > 1e-25 else 'not hit')
bad = 0; tot = 0
for n in range(3, 15, 2):
    m = n-1; V = np.zeros((m,m))
    for i in range(m):
        V[i,i] = -1
        if i+1 < m: V[i,i+1] = 1
    for j in range(1, 61):
        th = np.pi*(j-0.37)/60; w = np.exp(1j*th); H = (1-w)*V + (1-np.conj(w))*V.T; ev = np.linalg.eigvalsh(H)
        sig = int((ev > 1e-9).sum() - (ev < -1e-9).sum()); zeros = sum(1 for q in range((n-1)//2) if (2*q+1)*np.pi/n < th)
        Hm = (1-w)*(-V.T) + (1-np.conj(w))*(-V); evm = np.linalg.eigvalsh(Hm); sm = int((evm > 1e-9).sum() - (evm < -1e-9).sum())
        tot += 1; bad += (abs(sig) != 2*zeros) or (sm != -sig)
print('N3 cases', tot, 'mismatches', bad, 'KILL' if bad else 'not hit')
import snappy, spherogram
W = [1,-4,2,3,3,3,2,3,2,2,4,-3,-3,-3,-3,-1,-3,-2,-3,-3]
L = spherogram.Link(braid_closure=W); sg = L.signature(); al = L.alexander_polynomial(); det = L.determinant()
K7 = spherogram.Link(braid_closure=[1]*7); a7 = K7.alexander_polynomial()
W2 = [-1,4] + W[2:]; L2 = spherogram.Link(braid_closure=W2); ids = [str(x) for x in L2.exterior().identify()]
ok = (sg == 0) and (str(al) == str(a7*a7) or str(al) == str((a7*a7))) and det == 49 and any('K14a18636' in s for s in ids)
print('N4 signature', sg, '| Alexander', al, '| (7_1)^2', a7*a7, '| det', det, '| after two changes', ids, 'not hit' if ok else 'KILL')
S = spherogram.Link(braid_closure=[1]*7+[3]*7+[2]); print('  components', len(S.link_components))
S2 = spherogram.Link(braid_closure=[1]*7+[2]+[3]*7+[-2]) if len(S.link_components) != 1 else S
print('N5 7_1#7_1 signature', S2.signature(), 'det', S2.determinant(), 'components', len(S2.link_components), 'not hit' if abs(S2.signature()) == 12 else 'KILL')
print('   7_1 signature', K7.signature(), 'det', K7.determinant())

# SCRIPT: BALLS-MIXER-V4-BRAID-01
# N4 and N5 without Sage. Signature from the Seifert matrix (spherogram), Alexander polynomial from the reduced Burau
# matrices evaluated at numbers, identification of the changed knot by SnapPy. Kill lines as stated in v4_expected.py.
import warnings; warnings.filterwarnings('ignore')
import numpy as np, snappy, spherogram
W = [1,-4,2,3,3,3,2,3,2,2,4,-3,-3,-3,-3,-1,-3,-2,-3,-3]
def sig_det(word):
    L = spherogram.Link(braid_closure=word); V = np.array(L.seifert_matrix(), dtype=float); ev = np.linalg.eigvalsh(V+V.T)
    return int((ev > 1e-9).sum() - (ev < -1e-9).sum()), round(abs(np.linalg.det(V+V.T))), len(L.link_components)
def burau_alex(word, n, t):
    M = np.eye(n-1, dtype=complex)
    for g in word:
        i = abs(g)-1; B = np.eye(n-1, dtype=complex); B[i,i] = -t
        if i > 0: B[i,i-1] = t
        if i < n-2: B[i,i+1] = 1
        M = M @ (B if g > 0 else np.linalg.inv(B))
    return np.linalg.det(np.eye(n-1) - M) * (1-t)/(1-t**n)
d7 = lambda t: sum((-1)**k * t**k for k in range(7))
s, d, c = sig_det(W); print('braid: signature', s, 'determinant', d, 'components', c)
rat = [burau_alex(W, 5, t)/d7(t)**2 for t in (1.7, 2.3, 0.6+0.5j, 3.1)]
ks = [np.log(abs(r))/np.log(abs(t)) for r, t in zip(rat, (1.7, 2.3, 0.6+0.5j, 3.1))]
print('Alexander(braid) / Alexander(7_1)^2 is a unit +-t^k: k =', [round(float(k), 8) for k in ks])
W2 = [-1, 4] + W[2:]; ids = [str(x) for x in spherogram.Link(braid_closure=W2).exterior().identify()]; print('after changing entries 0 and 1:', ids)
s1, d1, c1 = sig_det(W2); print('  its signature', s1, 'determinant', d1)
ok = s == 0 and d == 49 and c == 1 and max(abs(k-round(k)) for k in ks) < 1e-6 and len(set(round(k) for k in ks)) == 1 and any('K14a18636' in x for x in ids)
print('N4', 'not hit' if ok else 'KILL')
for word in ([1]*7+[2]+[3]*7+[-2], [1]*7+[2]+[-3]*7+[-2]):
    print('5 strands', 'same hand' if word[10] > 0 else 'mirror', '-> signature, det, components', sig_det(word))
print('7_1 alone', sig_det([1]*7))

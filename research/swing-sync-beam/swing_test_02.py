# SCRIPT: SWING_TEST_02
# The sea test with the cut placed in a gap. Jeromie Beasley. 16 Nov 2026. AI-assisted. Kill lines: PREREG_SWING_02.md.
import json, math
import numpy as np
OUT = {}; Z = 3.0
def Vmat(seg, zs):
    N = sum(seg); b = np.cumsum(seg)[:-1] - 1; g = [(z - 1.0)/(z + 1.0) for z in zs]; V = np.zeros((2*N, 2*N))
    for j in range(2*N):
        x = np.zeros(2*N); x[j] = 1; R, L = x[:N], x[N:]; nR = np.zeros(N); nL = np.zeros(N); nR[1:] = R[:-1]; nL[:-1] = L[1:]
        for k, rho in zip(b, g):
            tau = math.sqrt(1 - rho*rho); nR[k+1] = tau*R[k] - rho*L[k+1]; nL[k] = rho*R[k] + tau*L[k+1]
        nR[0] = -L[0]; nL[N-1] = -R[N-1]; V[:N, j] = nR; V[N:, j] = nL
    return N, V
def gapped_sea(V, flip=False):
    th = np.angle(np.linalg.eigvals(V)); grid = np.linspace(0, math.pi, 200001)[:-1]
    def margin(p): d = np.abs(np.angle(np.exp(1j*(th[None, :] - p[:, None])))); d2 = np.abs(np.angle(np.exp(1j*(th[None, :] - p[:, None] - math.pi)))); return np.minimum(d.min(1), d2.min(1))
    m = np.concatenate([margin(grid[i:i+2000]) for i in range(0, len(grid), 2000)]); phi = float(grid[int(np.argmax(m))]); mg = float(np.max(m))
    Hs = (np.exp(-1j*phi)*V - np.exp(1j*phi)*V.T)/(2j); w, U = np.linalg.eigh(Hs); sel = U[:, (w > 0) if not flip else (w < 0)]   # eigenvalue sin(theta - phi) > 0: the arc from phi to phi + pi
    return sel @ sel.conj().T, phi, mg, int(sel.shape[1])
def setup(link, flip=False):
    N, V = Vmat([6, link, 6], [Z, Z]); P, phi, mg, rk = gapped_sea(V, flip); A = list(range(6)) + list(range(N, N + 6)); B = list(range(6 + link, N)) + list(range(N + 6 + link, 2*N))
    return N, V, P, A, B, phi, mg, rk
for name, flip in (('arc', False), ('opposite_arc', True)):
    N, V, P, A, B, phi, mg, rk = setup(20, flip); r = dict(cut_angle=phi, margin=mg, runnable=mg > 1e-6, rank=rk, of=2*N)
    r['T6a'] = dict(rest_dev=float(np.max(abs(V @ P @ V.T - P))), projector_dev=float(np.max(abs(P @ P - P)))); r['T6a']['held'] = r['T6a']['rest_dev'] <= 1e-12
    X = float(np.linalg.norm(P[np.ix_(A, B)])**2); r['T6b'] = dict(weight_between_at_rest=X, held=X > 1e-12)
    K = np.eye(2*N); K[2, 2] = -1; Pt = K @ P @ K; dB = []
    for t in range(81): dB.append(float(np.linalg.norm((Pt - P)[np.ix_(B, B)]))); Pt = V @ Pt @ V.T
    r['T6c'] = dict(crossing_step=24, largest_change_before_crossing=max(dB[:24]), first_step_with_change_above_1e_12=next((t for t, x in enumerate(dB) if x > 1e-12), None), change_at_steps_23_24_25_26=dB[23:27], largest_change_by_72=max(dB[:73]))
    r['T6c']['held'] = r['T6c']['largest_change_before_crossing'] <= 1e-12 and r['T6c']['largest_change_by_72'] > 1e-9
    r['kick_size_on_A'] = float(np.linalg.norm((K @ P @ K - P)[np.ix_(A, A)])); OUT[name] = r
E2 = {}
for l in (10, 20, 40, 80):
    N, V, P, A, B, phi, mg, rk = setup(l); E2[str(l)] = dict(weight_between=float(np.linalg.norm(P[np.ix_(A, B)])**2), margin=mg, rank=rk, of=2*N)
OUT['E2'] = E2
cv = lambda o: bool(o) if isinstance(o, np.bool_) else float(o)
json.dump(OUT, open('swing_test_02.out.json', 'w'), indent=1, default=cv); print(json.dumps(OUT, indent=1, default=cv))

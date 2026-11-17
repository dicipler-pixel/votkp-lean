# SCRIPT: SWING_TEST_01
# The swing, the open end and the bigger container. Jeromie Beasley. 16 Nov 2026. AI-assisted.
# Runs the tests fixed in PREREG_SWING_01.md. Every kill line below is copied from that file; none was changed after a run.
import json, math
import numpy as np
from scipy.linalg import expm
OUT = {}
def line(seg, zs, right, sign=1):
    """A line of stretches (cell counts seg) joined by faces of step ratio zs. Left end: mirror. right: 'mirror' or 'load'."""
    N = sum(seg); b = np.cumsum(seg)[:-1] - 1; g = [(z - 1.0)/(z + 1.0) for z in zs]
    def step(R, L):
        nR = np.zeros_like(R); nL = np.zeros_like(L); nR[1:] = R[:-1]; nL[:-1] = L[1:]
        for k, rho in zip(b, g):
            tau = math.sqrt(1 - rho*rho); nR[k+1] = tau*R[k] - sign*rho*L[k+1]; nL[k] = sign*rho*R[k] + tau*L[k+1]
        nR[0] = -L[0]; ab = 0.0
        if right == 'mirror': nL[N-1] = -R[N-1]
        else: nL[N-1] = 0.0; ab = abs(R[N-1])**2
        return nR, nL, ab
    return N, step
def run(seg, zs, right, steps, sign=1):
    N, step = line(seg, zs, right, sign); R = np.zeros(N); L = np.zeros(N); R[0] = 1.0; Lc = seg[0]; held = []; tot = []; ab = 0.0
    for t in range(steps + 1):
        held.append(float(np.sum(R[:Lc]**2 + L[:Lc]**2))); tot.append(float(np.sum(R**2 + L**2)) + ab)
        R, L, a = step(R, L); ab += a
    return np.array(held), np.array(tot), (R, L)
G = 0.5; Z = 3.0; Lc = 10
# ---- T1 sealed ----
N, step = line([Lc], [], 'mirror'); R = np.zeros(N); L = np.zeros(N); R[0] = 0.6; R[3] = 0.8; R0, L0_ = R.copy(), L.copy(); dev = 0.0
for t in range(2*Lc*50):
    R, L, _ = step(R, L); dev = max(dev, abs(np.sum(R*R + L*L) - 1))
    if t + 1 == 2*Lc: ret = float(max(np.max(abs(R - R0)), np.max(abs(L - L0_))))
OUT['T1'] = dict(max_energy_dev=dev, return_error_at_2L=ret, held=dev <= 1e-12 and ret <= 1e-12)
# ---- T2 open end ----
D = 37; steps = Lc*41 + 2; h2, tot2, _ = run([Lc, D], [Z], 'load', steps)
errs = [abs(h2[Lc*(2*n - 1)] - G**(2*n)) for n in range(1, 21)]; rel = [abs(h2[Lc*(2*n - 1)]/G**(2*n) - 1) for n in range(1, 21)]
OUT['T2'] = dict(max_abs_err=max(errs), max_rel_err=max(rel), books_dev=float(np.max(abs(tot2 - 1))), held_after_1_2_3=[float(h2[Lc]), float(h2[3*Lc]), float(h2[5*Lc])],
                 held=max(errs) <= 1e-12 and np.max(abs(tot2 - 1)) <= 1e-12)
# ---- T3 bigger container ----
h3, tot3, _ = run([Lc, D], [Z], 'mirror', steps); diff = np.where(abs(h3 - h2) > 1e-15)[0]; first = int(diff[0]) if len(diff) else None
OUT['T3'] = dict(predicted_first_difference_step=Lc + 2*D, measured_first_difference_step=first, books_dev=float(np.max(abs(tot3 - 1))),
                 held=first == Lc + 2*D and np.max(abs(tot3 - 1)) <= 1e-12)
# ---- T3b in time ----
res = {}
for sg in (1, -1):
    hb, totb, _ = run([Lc, Lc], [Z], 'mirror', Lc*41 + 2, sign=sg)
    e = [abs(hb[Lc*(2*n - 1)] - (G*G if n % 2 else 1.0)) for n in range(1, 21)]; res[sg] = (max(e), float(np.max(abs(totb - 1))), [float(hb[Lc*(2*n - 1)]) for n in range(1, 5)])
OUT['T3b'] = dict(max_err_sign_plus=res[1][0], max_err_sign_minus=res[-1][0], books_dev=max(res[1][1], res[-1][1]), held_after_meetings_1_to_4=res[1][2],
                  held=res[1][0] <= 1e-12 and res[-1][0] <= 1e-12)
# ---- T4, T5 moving wall by exact rays ----
def rays(Lf, Lp, nb, w=1e-3, K=2001):
    s = (np.arange(K)/(K - 1) - 0.5)*w; f = np.exp(-0.5*(s/(w/8))**2); df2 = np.diff(f)**2; E = [float(np.sum(df2/np.diff(s)))]; W = []; per = []; Lhit = []
    for n in range(nb):
        t = s + Lf(s)
        for _ in range(200): t = s + Lf(t)
        v = Lp(t); vm = 0.5*(v[1:] + v[:-1]); W.append(float(np.sum(-2*vm/(1 + vm)*df2/np.diff(s)))); s2 = t + Lf(t); per.append(float(s2[K//2] - s[K//2])); Lhit.append(float(Lf(t[K//2]))); s = s2
        E.append(float(np.sum(df2/np.diff(s))))
    return np.array(E), np.array(W), np.array(per), np.array(Lhit)
a = 0.01; Om = math.pi; v0 = a*math.pi; D0 = (1 + v0)/(1 - v0)
mk = lambda Omega, ph: (lambda t: 1 + a*np.sin(Omega*t + ph), lambda t: a*Omega*np.cos(Omega*t + ph))
E, W, _, _ = rays(*mk(Om, 0.0), 20); OUT['T4a'] = dict(D0=D0, predicted=D0**20, measured=float(E[-1]/E[0]), rel_err=abs(E[-1]/E[0]/D0**20 - 1), held=abs(E[-1]/E[0]/D0**20 - 1) <= 0.01)
OUT['T4d'] = dict(gain=float(E[-1] - E[0]), work=float(np.sum(W)), rel_err=abs((E[-1] - E[0]) - np.sum(W))/abs(E[-1] - E[0]), held=abs((E[-1] - E[0]) - np.sum(W))/abs(E[-1] - E[0]) <= 1e-3)
E, _, _, _ = rays(*mk(Om, math.pi), 5); OUT['T4b'] = dict(predicted=D0**-5, measured=float(E[-1]/E[0]), rel_err=abs(E[-1]/E[0]*D0**5 - 1), held=abs(E[-1]/E[0]*D0**5 - 1) <= 0.01)
E, _, _, _ = rays(*mk(Om*(1 + math.sqrt(5))/2, 0.0), 200); mg = float(np.mean(np.diff(np.log(E))))
OUT['T4c'] = dict(mean_log_gain_per_meeting=mg, limit=0.1*math.log(D0), ln_D0=math.log(D0), largest_single_step=float(np.max(abs(np.diff(np.log(E))))), held=abs(mg) <= 0.1*math.log(D0))
vs = 1e-3; Lf = lambda t: np.maximum(1 - vs*np.asarray(t, float), 0.8); Lp = lambda t: np.where(1 - vs*np.asarray(t, float) > 0.8, -vs, 0.0)
E, _, per, Lh = rays(Lf, Lp, 140); er = float(E[-1]/E[0]); pr = float(per[-1]/2.0)
OUT['T5'] = dict(energy_ratio=er, predicted_energy_ratio=1.25, period_end_over_start=pr, predicted_period_ratio=0.8, energy_times_length_start=float(E[0]*1.0), energy_times_length_end=float(E[-1]*0.8),
                 held=abs(er/1.25 - 1) <= 0.01 and abs(pr/0.8 - 1) <= 0.01)
# ---- T6 the sea ----
def Vmat(seg, zs):
    N, step = line(seg, zs, 'mirror'); V = np.zeros((2*N, 2*N))
    for j in range(2*N):
        x = np.zeros(2*N); x[j] = 1; R, L, _ = step(x[:N].copy(), x[N:].copy()); V[:N, j] = R; V[N:, j] = L
    return N, V
def sea(V):
    Hs = (V - V.T)/(2j); w, U = np.linalg.eigh(Hs); neg = U[:, w < 0]; return neg @ neg.conj().T, float(np.min(abs(w))), int(neg.shape[1])
def tie(link):
    N, V = Vmat([6, link, 6], [Z, Z]); P, mn, rk = sea(V); A = list(range(6)) + list(range(N, N + 6)); B = list(range(6 + link, N)) + list(range(N + 6 + link, 2*N))
    return N, V, P, A, B, float(np.linalg.norm(P[np.ix_(A, B)])**2), mn, rk
N, V, P, A, B, X, mn, rk = tie(20)
OUT['T6a'] = dict(unitary_dev=float(np.max(abs(V @ V.T - np.eye(2*N)))), rest_dev=float(np.max(abs(V @ P @ V.T - P))), rank=rk, half=N, smallest_spectrum_distance_from_cut=mn, held=float(np.max(abs(V @ P @ V.T - P))) <= 1e-12)
OUT['T6b'] = dict(weight_between_A_and_B_at_rest=X, held=X > 1e-12)
K = np.eye(2*N); K[2, 2] = -1; Pt = K @ P @ K; dB = []
for t in range(81):
    dB.append(float(np.linalg.norm((Pt - P)[np.ix_(B, B)]))); Pt = V @ Pt @ V.T
before = max(dB[:24]); firstmove = next((t for t, x in enumerate(dB) if x > 1e-12), None)
OUT['T6c'] = dict(crossing_step=24, largest_change_before_crossing=before, first_step_with_change=firstmove, change_at_24=dB[24], largest_change_by_72=max(dB[:73]), held=before <= 1e-12 and max(dB[:73]) > 1e-9)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
dirs = [(0, 0, 1), (math.sin(.6), 0, math.cos(.6)), (0, math.sin(.9), math.cos(.9))]; dAB = math.log(3); dAC = math.log(5); dBC = math.acosh(math.cosh(dAB)*math.cosh(dAC)); H = np.zeros((6, 6), complex)
for i, n in enumerate(dirs): H[2*i:2*i+2, 2*i:2*i+2] = n[0]*sx + n[1]*sy + n[2]*sz
for (i, j, d) in ((0, 1, dAB), (0, 2, dAC), (1, 2, dBC)):
    c = 0.5/math.cosh(d/2); H[2*i:2*i+2, 2*j:2*j+2] = c*np.eye(2); H[2*j:2*j+2, 2*i:2*i+2] = c*np.eye(2)
w, U = np.linalg.eigh(H); k = int(np.argmax(np.diff(w))) + 1; Pm = U[:, :k] @ U[:, :k].conj().T; Km = np.eye(6, dtype=complex); Km[:2, :2] = sx; P1 = Km @ Pm @ Km.conj().T
def farC(t): Ut = expm(-1j*H*t); return float(np.linalg.norm((Ut @ P1 @ Ut.conj().T - Pm)[4:, 4:]))
OUT['T6d'] = dict(levels=[float(x) for x in w], filled=k, light_crossing_time=dAC, change_on_far_ball_at_0=farC(0.0), change_at_1_percent=farC(0.01*dAC), change_at_10_percent=farC(0.1*dAC), held=farC(0.01*dAC) >= 1e-8)
# ---- looks, no kill line ----
E1 = {}
for Dd in (20, 40, 60, 30, 28, 32):
    h, _, _ = run([20, Dd], [Z], 'mirror', 16000); E1[str(Dd/20)] = dict(most_the_swing_gets_back=float(np.max(h[21:])), mean_held=float(np.mean(h[21:])))
OUT['E1'] = E1; OUT['E2'] = {str(l): tie(l)[5] for l in (10, 20, 40, 80)}
OUT['all_held'] = bool(all(v.get('held', True) for v in OUT.values() if isinstance(v, dict) and 'held' in v))
cv = lambda o: bool(o) if isinstance(o, np.bool_) else float(o)   # numpy values to plain ones for the file; no test is touched
json.dump(OUT, open('swing_test_01.out.json', 'w'), indent=1, default=cv); print(json.dumps(OUT, indent=1, default=cv))

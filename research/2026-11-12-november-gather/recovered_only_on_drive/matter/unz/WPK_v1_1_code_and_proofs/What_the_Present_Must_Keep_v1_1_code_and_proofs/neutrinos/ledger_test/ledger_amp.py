# SCRIPT: LEDGER-AMP  POST-HOC variant (not preregistered): the same link written in AMPLITUDE rather than population.
# A(tau) = sum_k w_k Re a_0(k,tau)  (a_0 stays real: da_0/dtau = -i k M01 a_1 with a_1 imaginary), amplitude ledger L_A = -dA/dtau.
# Same solver, same weights, same histories as LEDGER (population S = sum w |a0|^2 is also returned as a cross-check).
import json, sys
import numpy as np
from scipy.integrate import solve_ivp
import ledger as LG
from run_burst import make_kH
def AS_curve(h, tg, rtol=1e-8, atol=1e-11):
    kH = make_kH(h); Kf = lambda t: min(kH(t), LG.CAP)/t
    edges = [LG.TAU0] + [x for x in LG.breakpoints(h) if x < tg[-1]] + [tg[-1]]
    A = np.zeros(len(tg)); S = np.zeros(len(tg))
    for k, w in zip(LG.ks, LG.wE):
        y = np.zeros(LG.NL, complex); y[0] = 1.0; A0 = -1j*k*LG.Mm; out = np.zeros(len(tg), complex)
        for a, b in zip(edges[:-1], edges[1:]):
            def Kp(t, a=a, b=b): return Kf(min(max(t, a*(1+1e-12)), b*(1-1e-12)))
            te = [x for x in tg if a <= x <= b]
            s = solve_ivp(lambda t, v: (A0 - Kp(t)*LG.Q) @ v, (a, b), y, method='BDF', jac=lambda t, v: (A0 - Kp(t)*LG.Q).tocsc(),
                          t_eval=te if te else None, rtol=rtol, atol=atol)
            assert s.success
            for x, col in zip(s.t, s.y.T): out[np.searchsorted(tg, x)] = col[0]
            y = s.y[:, -1]
        A += w*out.real; S += w*np.abs(out)**2
    return A, S
if __name__ == '__main__':
    G = LG.GRID; res = {'grid': G.tolist()}
    H = {'inst': {'base': ['inst']}, 'const1e4': {'base': ['const', 1e4]}}
    for ed in (0.25, 0.5, 1, 2, 4, 8): H['n3_%g' % ed] = {'base': ['power', ed, 3]}
    for ed in (1, 2, 3): H['n6_%g' % ed] = {'base': ['power', ed, 6]}
    H['K5B_n3_1'] = json.load(open('k5_design.json'))['n3_1']['h']
    for k, h in H.items():
        A, S = AS_curve(h, G); res[k] = dict(A=A.tolist(), S=S.tolist())
        print(k, 'A(1)=%.4f A(1.7)=%.4f A(3)=%.4f A(6)=%.4f min A=%.4f' % (*np.interp([1, 1.7, 3, 6], G, A), A.min()), flush=True)
    B = {}
    for eb in (0.25, 0.5, 1, 1.5, 2, 3, 4, 6):
        tg = np.array([eb, 1.25*eb, 1.25*eb*1.02])
        A0, _ = AS_curve({'base': ['const', 1e4]}, tg); Ab, _ = AS_curve({'base': ['const', 1e4], 'windows': [[eb, 1.25*eb, 0.0]]}, tg)
        B['%g' % eb] = float(A0[2]-Ab[2])
    for eb in (1, 2, 3):
        for f in (1.05, 1.1):
            tg = np.array([eb, f*eb, f*eb*1.02])
            A0, _ = AS_curve({'base': ['const', 1e4]}, tg); Ab, _ = AS_curve({'base': ['const', 1e4], 'windows': [[eb, f*eb, 0.0]]}, tg)
            B['%g_%g' % (eb, f)] = float(A0[2]-Ab[2])
    tg = np.array([3.75*1.02]); A0, _ = AS_curve({'base': ['const', 1e4]}, tg)
    Ab, _ = AS_curve({'base': ['const', 1e4], 'windows': [[1, 1.25, 0.0], [3, 3.75, 0.0]]}, tg); B['1+3'] = float(A0[0]-Ab[0])
    print('burst amplitude ledgers', B); res['bursts'] = B
    json.dump(res, open('ledger_amp.json', 'w'))

archive/checks/source_wall/source_wall_01.py

\# SCRIPT: SOURCE_WALL_01 \# Does the source-resolved record (Theorem 26) notice the Theorem 16 metric wall that the bare record Z cannot see? import numpy as np, json OUT = {} def Pchart(x, y):

z = x + 1j\*y; w = x + 1j\*y\*\*2 return np.array(\[\[1, w\], \[z, z\*w\]\])/(1 + z\*w) def Portho(x, y): \# opposite family: orthogonal rank-one projectors

th = np.pi/4 + x; u = np.array(\[np.cos(th), np.exp(1j\*y)\*np.sin(th)\]); return np.outer(u, u.conj()) def Hof(P, y): return (2 + y/10)\*P + (5 + y/5)\*(np.eye(2) - P) M = 200; TH = 2\*np.pi\*np.arange(M)/M; ZC = 2 + 0.4\*np.exp(1j\*TH); DZ = 0.4j\*np.exp(1j\*TH)\*(2\*np.pi/M) def Zc(H):

return sum(np.log(z)\*np.trace(np.linalg.inv(z\*np.eye(2) - H))\*d for z, d in zip(ZC, DZ))/(2j\*np.pi) def q_meas(H, b, t=1e-6):

B = np.outer(b, b.conj()); return (Zc(H + t\*B) - Zc(H - t\*B))/(2\*t) E = np.eye(2) def A_measured(H, real_only=False):

q = lambda b: (q_meas(H, b).real if real_only else q_meas(H, b)) qi = \[q(E\[i\]) for i in range(2)\]; A = np.zeros((2, 2), complex) A\[0, 0\], A\[1, 1\] = qi s = q(E\[0\] + E\[1\]) - qi\[0\] - qi\[1\] \# A01 + A10 d = -1j\*(q(E\[0\] + 1j\*E\[1\]) - qi\[0\] - qi\[1\]) \# A01 - A10 A\[0, 1\] = (s + d)/2; A\[1, 0\] = (s - d)/2 return A def gform(Pf, x, y, h=1e-5):

Dx = (Pf(x+h, y) - Pf(x-h, y))/(2\*h); Dy = (Pf(x, y+h) - Pf(x, y-h))/(2\*h) D = \[Dx, Dy\]; return np.array(\[\[0.5\*np.trace(a@b).real for b in D\] for a in D\]) herm = lambda X: (X + X.conj().T)/2

\# ---- S1 full complex readout: reconstruct P from measured source responses, then the metric ---- def P_from_sources(x, y, Pf=Pchart, real_only=False):

H = Hof(Pf(x, y), y); A = A_measured(H, real_only); lam = np.exp(Zc(H)); return lam\*A pts = \[(a, b) for a in (-0.1, 0.0, 0.1) for b in (-0.1, 0.0, 0.1)\] gerr = max(np.abs(gform(lambda x, y: P_from_sources(x, y), \*p, h=1e-4) - gform(Pchart, \*p)).max() for p in pts) Prec_err = max(np.abs(P_from_sources(\*p) - Pchart(\*p)).max() for p in pts) def detg_rec(y): return np.linalg.det(gform(lambda x, yy: P_from_sources(x, yy), 0.0, y, h=1e-4)) lo, hi = -0.05, 0.05 assert detg_rec(lo) \> 0 \> detg_rec(hi) for _ in range(40):

mid = (lo + hi)/2 if detg_rec(mid) \> 0: lo = mid else: hi = mid ywall = (lo + hi)/2 OUT\['S1'\] = dict(P_rec_err=Prec_err, g_rec_err=gerr, wall_y_reconstructed=ywall,

verdict='NOTICES' if (abs(ywall) \< 1e-5 and gerr \< 1e-5) else 'NOT ESTABLISHED') print('S1 full readout: |P_rec-P| %.1e, |g_rec-g| %.1e, reconstructed wall at y=%.2e -\> %s' % (Prec_err, gerr, ywall, OUT\['S1'\] \['verdict'\]))

\# ---- S2 real-only readout: only Herm(A) is visible ---- spot = max(np.abs(herm(A_measured(Hof(Pchart(\*p), p\[1\]), real_only=False)) - A_measured(Hof(Pchart(\*p), p\[1\]), real_only=True)).m ax() for p in pts) xs = np.linspace(-0.24, 0.24, 41); ys = np.linspace(-0.24, 0.24, 41) HP = lambda x, y: herm(Pchart(x, y)) detR = np.array(\[\[np.linalg.det(gform(HP, x, y)) for x in xs\] for y in ys\]) minR = np.array(\[\[np.linalg.eigvalsh(gform(HP, x, y)).min() for x in xs\] for y in ys\]) detG = np.array(\[\[np.linalg.det(gform(Pchart, x, y)) for x in xs\] for y in ys\]) OUT\['S2'\] = dict(real_readout_equals_Herm_A=spot, gR_min_eig_over_grid=float(minR.min()), gR_det_min=float(detR.min()),

gR_det_at_y0=\[float(detR\[20, j\]) for j in (0, 10, 20, 30, 40)\], verdict='BLIND' if minR.min() \>= -1e-12 else 'NOTICES (sign change)') print('S2 real-only readout: Re q = Herm(A) to %.1e; min eig of g_R over grid %.3e; det g_R min %.3e; det g_R on y=0 (x=-.24,-.1 2,0,.12,.24) %s -\> %s'

% (spot, minR.min(), detR.min(), np.round(OUT\['S2'\]\['gR_det_at_y0'\], 6), OUT\['S2'\]\['verdict'\])) \# where is g_R smallest? i, j = np.unravel_index(np.argmin(detR), detR.shape) print(' smallest det g_R at x=%.3f y=%.3f' % (xs\[j\], ys\[i\]))

\# ---- S3 pointwise positivity of the source measure ---- mA = np.array(\[\[np.linalg.eigvalsh(herm(Pchart(x, y)/(2 + y/10))).min() for x in xs\] for y in ys\]) row0 = mA\[20\]; zero_pts = \[(xs\[j\], ys\[i\]) for i in range(41) for j in range(41) if abs(mA\[i, j\]) \< 1e-12\] OUT\['S3'\] = dict(min_over_grid=float(mA.min()), max_over_grid=float(mA.max()), n_points_m_zero=len(zero_pts),

m_on_y0=\[float(row0\[j\]) for j in (0, 10, 20, 30, 40)\], m_on_x0=\[float(mA\[i, 20\]) for i in (0, 10, 18, 19, 20, 21, 22, 30, 40)\]) print('S3 min eig Herm(A): grid min %.3e max %.3e; zero at %d grid points; on y=0: %s; on x=0 (y=-.24,-.12,-.024,-.012,0,.012,.02 4,.12,.24): %s'

% (mA.min(), mA.max(), len(zero_pts), np.round(OUT\['S3'\]\['m_on_y0'\], 8), np.round(OUT\['S3'\]\['m_on_x0'\], 6)))

\# ---- S4 wall locus vs self-adjoint locus ---- sa = np.array(\[\[np.abs(Pchart(x, y) - Pchart(x, y).conj().T).max() for x in xs\] for y in ys\]) sign_change_rows = \[ys\[i\] for i in range(40) if np.any(np.sign(detG\[i\]) \!= np.sign(detG\[i+1\]))\] wall_cols = \[\] for j in range(41): \# along each x, locate det g zero in y

col = detG\[:, j\]; k = np.where(np.sign(col\[:-1\]) \!= np.sign(col\[1:\]))\[0\] if len(k):

\# refine a, b = ys\[k\[0\]\], ys\[k\[0\]+1\] f = lambda yy: np.linalg.det(gform(Pchart, xs\[j\], yy)) for _ in range(50):

m_ = (a+b)/2


if np.sign(f(m_)) == np.sign(f(a)): a = m_ else: b = m_ wall_cols.append((float(xs\[j\]), (a+b)/2)) sa_y0 = float(sa\[20\].max()); sa_off = float(np.delete(sa, 20, axis=0).min()) OUT\['S4'\] = dict(wall_y_by_x=wall_cols, selfadjoint_defect_on_y0=sa_y0, min_selfadjoint_defect_off_y0=sa_off) print('S4 wall y(x): %s' % ', '.join('x=%.2f:y=%.2e' % (a, b) for a, b in wall_cols\[::5\])) print(' |P-P^dag| on y=0 max %.1e ; off y=0 min %.3e' % (sa_y0, sa_off))

\# ---- S5 Z itself ---- Zs = \[(y, Zc(Hof(Pchart(0, y), y))) for y in (-0.02, -0.01, 0.0, 0.01, 0.02)\] dZ = (Zs\[3\]\[1\] - Zs\[1\]\[1\])/0.02; d2Z = (Zs\[3\]\[1\] - 2\*Zs\[2\]\[1\] + Zs\[1\]\[1\])/1e-4 OUT\['S5'\] = dict(Z=\[(y, complex(z).real) for y, z in Zs\], dZ=complex(dZ).real, d2Z=complex(d2Z).real, exact_dZ=1/20, exact_d2Z=- 1/400) print('S5 Z(0,y) at y=-.02..02: %s ; dZ/dy %.6f (exact 0.05) ; d2Z %.6f (exact -0.0025)' % (\[round(complex(z).real, 8) for _, z i n Zs\], complex(dZ).real, complex(d2Z).real))

\# ---- OPPOSITE: orthogonal family ---- detO = np.array(\[\[np.linalg.det(gform(Portho, x, y)) for x in xs\[::4\]\] for y in ys\[::4\]\]) minO = min(np.linalg.eigvalsh(gform(Portho, x, y)).min() for x in xs\[::4\] for y in ys\[::4\]) realO = max(np.abs(A_measured(Hof(Portho(\*p), p\[1\]), real_only=True) - A_measured(Hof(Portho(\*p), p\[1\]))).max() for p in pts) OUT\['OPP'\] = dict(min_eig_g=minO, det_min=float(detO.min()), real_vs_full_readout=realO) print('OPPOSITE orthogonal family: min eig g %.3e, det g min %.3e (no wall), real-only readout = full readout to %.1e' % (minO, d etO.min(), realO)) json.dump(OUT, open('source_wall_01.json', 'w'), indent=1, default=str)



archive/neutrinos/ledger_test/run_burst.py

\# SCRIPT: RUN-BURST (copy of next/runs/run_nuc_n3.py; ONLY change: kappa/H is a general function of eps given by a history spec) \# history spec (dict, picklable): \# base: ('const', C) kappa/H = C at all eps (C large = fully coupled = fluid limit) \# ('power', eps_dec, n) kappa/H = (eps_dec/eps)^n (McCormick's rate law) \# ('inst',) kappa/H = 0 (instant decoupling at eps0) \# ('table', logeps_list, log10kH_list) kappa/H interpolated in log eps (log10 values; -99 means zero) \# windows: list of (eps_a, eps_b, value): inside \[eps_a, eps_b) kappa/H = value (0 = streaming burst; C = coupling burst) \# cap: kappa/H capped at this value (as before, 5e5) import numpy as np, time

def make_kH(h):

base = h\['base'\]; win = list(h.get('windows', \[\])) if base\[0\] == 'const':

C = float(base\[1\]); f0 = lambda e: C elif base\[0\] == 'power':

ed, n = float(base\[1\]), float(base\[2\]); f0 = lambda e: (ed/e)\*\*n elif base\[0\] == 'inst':

f0 = lambda e: 0.0 elif base\[0\] == 'table':

xl = np.array(base\[1\], float); yl = np.array(base\[2\], float) def f0(e):

y = np.interp(np.log(e), xl, yl) return 0.0 if y \< -50 else 10.0\*\*y def f(e):

for a, b, v in win:

if a \<= e \< b: return float(v) return f0(e) return f from ms_nuc import rhs, state, timestep, rho_b from ms_fluid import initial_data, make_grid

def run(delta_m, fnu=0.409, N=400, K=32, rmax=9.0, beta=3.0, eps0=0.1, cfl_r=0.4, cfl_mu=0.4, cH=0.005,

eps_max=30.0, qshape=1.0, snap_eps=(), hist_every=20, stop_rule=True, disperse_rule=True, hspec=None, kapcap=5.0e5, max_s teps=10\*\*9):

kH = make_kH(hspec) r = make_grid(N, rmax, beta) t0, R, U, rho = initial_data(r, delta_m, eps0, 0.0, qshape) e = (1-fnu)\*rho mue = np.linspace(-1, 1, K+1) I = np.repeat((fnu\*rho/(4\*np.pi))\[:, None\], K, axis=1) Mi = np.concatenate(\[\[0.0\], np.cumsum((4\*np.pi/3)\*np.diff(R\*\*3)\*rho)\]) Gam = np.ones(N+1); Gam\[1:\] = np.sqrt(1.0 + U\[1:\]\*\*2 - 2\*Mi\[1:\]/R\[1:\]) t = t0 dR = np.zeros(N+1); dU = np.zeros(N+1); dG = np.zeros(N+1); de = np.zeros(N); dI = np.zeros((N, K)) peakC = -1.0; eps_peak = 0.0; hist = \[\]; snaps = {}; step = 0; status = 'undecided' snap_eps = list(snap_eps) rawmax = 0.0; capsteps = 0; eps_cap_last = 0.0; kapmax = 0.0 while True:

Ib = fnu/(1-fnu)\*e\[-1\]/(4\*np.pi) \# incoming background tied to the outer cell's fluid density if True:

raw = kH(2\*np.sqrt(t\*t0)) rawmax = max(rawmax, raw) if raw \> kapcap:

capsteps += 1; eps_cap_last = 2\*np.sqrt(t\*t0) kap = (1/(2\*t))\*min(raw, kapcap) kapmax = max(kapmax, kap\*t) try: M, Ac, ac, S, V = rhs(t, R, U, Gam, e, I, mue, fnu, Ib, kap, dR, dU, dG, de, dI) except (ZeroDivisionError, FloatingPointError):

status = 'crash'; break epsn = 2\*np.sqrt(t\*t0) twoMR = 2\*M\[1:\]/R\[1:\] C = 2\*(M\[1:\] - (4\*np.pi/3)\*rho_b(t)\*R\[1:\]\*\*3)/R\[1:\] iC = np.argmax(C) if C\[iC\] \> peakC: peakC = C\[iC\]; eps_peak = epsn if step % hist_every == 0:

dmu = mue\[1\]-mue\[0\] inner = r\[1:\] \< 3.0 hcv = np.max(np.abs(Gam\[1:\]\*\*2 - 1 - U\[1:\]\*\*2 + twoMR)\[inner\]) \# Hamiltonian-constraint check hist.append((t, epsn, C\[iC\], r\[1+iC\], e\[0\]/rho_b(t), 2\*np.pi\*I\[0\].sum()\*dmu/rho_b(t),

e\[-1\]/rho_b(t), 2\*np.pi\*I\[-1\].sum()\*dmu/rho_b(t), hcv)) if snap_eps and epsn \>= snap_eps\[0\]:

snaps\[snap_eps.pop(0)\] = dict(t=t, eps=epsn, R=R.copy(), U=U.copy(), e=e.copy(), I=I.copy(), M=M.copy()) if stop_rule:

if np.any((twoMR \>= 1.0) & (U\[1:\] \< 0)):

status = 'BH'; break if disperse_rule and epsn \> 3.0 and C\[iC\] \< 0.5\*peakC:

status = 'dispersed'; break if epsn \> eps_max: break if step \>= max_steps: status = 'stepcap'; break \# near-critical stall guard (classified undecided) try: dt = min(timestep(R, U, e, I, mue, Gam, Ac, ac, S, cfl_r, cfl_mu), cH\*2\*t, (0.5/(kap\*np.max(Ac)) if kap \> 0 else 1e3 0))

\# SSP RK3 (the outer-boundary intensity is evaluated at each stage time) R1 = R + dt\*dR; U1 = U + dt\*dU; G1 = Gam + dt\*dG; e1 = e + dt\*de; I1 = I + dt\*dI rhs(t+dt, R1, U1, G1, e1, I1, mue, fnu, fnu/(1-fnu)\*e1\[-1\]/(4\*np.pi), kap, dR, dU, dG, de, dI) R2 = 0.75\*R + 0.25\*(R1+dt\*dR); U2 = 0.75\*U + 0.25\*(U1+dt\*dU); G2 = 0.75\*Gam + 0.25\*(G1+dt\*dG) e2 = 0.75\*e + 0.25\*(e1+dt\*de); I2 = 0.75\*I + 0.25\*(I1+dt\*dI)


rhs(t+0.5\*dt, R2, U2, G2, e2, I2, mue, fnu, fnu/(1-fnu)\*e2\[-1\]/(4\*np.pi), kap, dR, dU, dG, de, dI) R = R/3 + 2/3\*(R2+dt\*dR); U = U/3 + 2/3\*(U2+dt\*dU); Gam = Gam/3 + 2/3\*(G2+dt\*dG) e = e/3 + 2/3\*(e2+dt\*de); I = I/3 + 2/3\*(I2+dt\*dI) except (ZeroDivisionError, FloatingPointError):

coll = U\[1:\] \< 0 status = 'BH' if (coll.any() and np.max(twoMR\[coll\]) \> 0.95) else 'crash' \# breakdown just before collapse break t += dt; step += 1 if np.any(e \<= 0) or not np.all(np.isfinite(U)) or not np.all(np.isfinite(I)):

status = 'crash'; break return dict(rawmax=rawmax, kapcap=kapcap, capsteps=capsteps, eps_cap_last=eps_cap_last, kapt_max=kapmax, status=status, t=t, t0=t0, eps=2\*np.sqrt(t\*t0), steps=step, peakC=peakC, eps_peak=eps_peak, hist=np.array(hist),

snaps=snaps, r=r, mue=mue, R=R, U=U, e=e, I=I, Gam=Gam)



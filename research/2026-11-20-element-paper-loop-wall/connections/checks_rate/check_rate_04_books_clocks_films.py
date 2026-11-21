# SCRIPT: RATE-WEIGHT-BOOKS-CLOCKS-FILMS-04
# Four smaller connections, each with its reason first.
#  (1) TWO BOOKS (The Weight Between, section 3: V^2 + D^2 = 1; crossed/parallel ports sin^2, cos^2).
#      With D := Gamma = tanh h and V := sech h = sqrt(1 - Gamma^2), V^2 + D^2 = 1 identically, and the
#      loop wall Gamma^2 = 1/2 is exactly V = D (equal books). The phase readout <Z_P>(theta) = sin 2theta sin Phi
#      of EqualEndpointWitness is largest at theta = pi/4, the wall angle of check 02.  Algebra is exact;
#      the identification D = Gamma is STRUCTURAL (which-way distinguishability is not a peel step).
#  (2) CLOCK RATIO (The Offset Speed Limit, section 1: projector geometry blind to H -> sH + cI; a constant
#      is read only as a difference; a clock RATIO cancels a common scale).  Each removal energy is a
#      difference of charge-state energies, IE_q = E_{q+1} - E_q, so a common shift c cancels in IE; a common
#      scale s cancels in z = IE_{q+1}/IE_q.  The check applies E -> sE + c to cumulative ladders built from
#      the archive and confirms every z and Gamma unchanged.  This is exact; the reading "a peel ratio is a
#      two-clock ratio" is STRUCTURAL.
#  (3) FILMS AND THE (+) LAW (The Weight Between eq. (13), votkp-lean Film.lean, Smith.lean smith_identity):
#      log-ratios add, ln(IE_{q+2}/IE_q) = ln z_q + ln z_{q+1}, so the two-step reflection is
#      Gamma_q (+) Gamma_{q+1} = (u+v)/(1+uv).  Exact by tanh addition; checked on every archive pair.
#  (4) GIBBS READING (The Offset Speed Limit eq. (7), two-level population gap tanh(beta Delta/2)): z plays the
#      Boltzmann ratio e^{beta Delta}; the wall is beta Delta = ln(3 + 2 sqrt2) = 2 asinh 1, populations
#      (1 +- 1/sqrt2)/2.  Numbers only; STRUCTURAL.
#  (5) The Rice-Mele offset of the paper (0.881157076) written as a peel step: Gamma = tanh(tau/2) = v/sqrt(Emin Emax).
# KILL CONDITIONS (before running): K1 V^2 + D^2 - 1 or V - D at the wall nonzero beyond 1e-15;
#   K2 any z or Gamma changed by more than 1e-12 (relative) under E -> sE + c;
#   K3 any (+) telescoping residual above 1e-12.
import sys, gzip, json, math
import numpy as np

W = 3 + 2 * math.sqrt(2)
hw = 0.5 * math.log(W)
D, V = math.tanh(hw), 1 / math.cosh(hw)
k1 = max(abs(V * V + D * D - 1), abs(V - D))
print(f'(1) at the wall: D = Gamma = {D:.15f}, V = sech h = {V:.15f}, V^2 + D^2 - 1 = {V*V + D*D - 1:.1e}')
th = np.linspace(0, math.pi / 2, 100001)
print(f'    sin(2 theta) peaks at theta = {math.degrees(th[np.argmax(np.sin(2*th))]):.4f} deg; '
      f'sin(theta)^2 there = {math.sin(th[np.argmax(np.sin(2*th))])**2:.6f}')

d = json.load(gzip.open(sys.argv[1]))
rng = np.random.default_rng(7)
worst2 = worst3 = 0.0
npairs = 0
for r in d['records']:
    if r['Z'] > 85:
        continue
    IEs = [x['IE_eV'] for x in sorted(r['thresholds'], key=lambda x: x['q']) if x.get('IE_eV') is not None]
    if len(IEs) < 3:
        continue
    E = np.concatenate([[0.0], np.cumsum(IEs)])   # charge-state energies up to a constant
    s, c = float(rng.uniform(0.1, 10)), float(rng.normal() * 1e3)
    E2 = s * E + c
    IE2 = np.diff(E2)
    z = np.array(IEs[1:]) / np.array(IEs[:-1])
    z2 = IE2[1:] / IE2[:-1]
    G = (z - 1) / (z + 1)
    G2 = (z2 - 1) / (z2 + 1)
    worst2 = max(worst2, float(np.max(np.abs(z2 / z - 1))), float(np.max(np.abs(G2 - G))))
    for q in range(len(IEs) - 2):
        u, v = G[q], G[q + 1]
        Z2 = IEs[q + 2] / IEs[q]
        Gtwo = (Z2 - 1) / (Z2 + 1)
        worst3 = max(worst3, abs((u + v) / (1 + u * v) - Gtwo))
        npairs += 1
print(f'(2) E -> sE + c on every ladder H..At: worst relative change of z or change of Gamma = {worst2:.1e}')
print(f'(3) two-step reflection = Gamma_q (+) Gamma_(q+1) on {npairs} archive pairs: worst residual {worst3:.1e}')
print(f'(4) wall as Gibbs gap: beta Delta = {math.log(W):.12f} = 2 asinh 1 = {2*math.asinh(1):.12f}; '
      f'populations {(1+1/math.sqrt(2))/2:.6f}, {(1-1/math.sqrt(2))/2:.6f}')
tau = 0.881157076037
Gt = math.tanh(tau / 2)
print(f'(5) Rice-Mele offset tau = {tau}: as a peel step Gamma = tanh(tau/2) = {Gt:.9f}, z = e^tau = {math.exp(tau):.6f}, '
      f'Gamma^2 = {Gt*Gt:.6f} (inside the wall)')
print('KILL K1', 'FIRED' if k1 > 1e-15 else 'not fired', '| K2', 'FIRED' if worst2 > 1e-12 else 'not fired',
      '| K3', 'FIRED' if worst3 > 1e-12 else 'not fired')

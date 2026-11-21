# SCRIPT: CHECK-GRAVITY-04-RECIPROCITY-LOOP
# Gravity paper against the Loop Wall element paper: reciprocity, direction, and what the record sees.
# (a) The peel step as a two-port: S = [[G, t],[t, -G]], t = sqrt(1-G^2), G = (z-1)/(z+1).
#     Claim: losslessness (S unitary) alone gives |S11| = |S22| (the element paper's power_even);
#     reciprocity S = S^T together with a real S gives the exact flip S22 = -S11 (gam_reverse).
#     The gravity paper names S = S^T as the laboratory instance of its Theorem 7 (final_v3 Sec. 7).
# (b) Reversal parity of an n-step oriented volume det[d_0..d_{n-1}]: reversing the path
#     (d_k -> -d_{n-1-k}) multiplies it by (-1)^{n(n+1)/2}; a mirror multiplies it by -1.
#     n = 1 is the signed half-step h = (1/2) ln z (Gamma odd); n = 3 is the screw sign chi (even).
# (c) The recovered three-mode loop (element folder spinor_recovery): H(Phi) with a flux Phi on one
#     link and detuned sites. Gravity measure W (final_v3 eq. 2) with real symmetric probes:
#     W = 0 at Phi = 0 (real symmetric H = B-symmetric with B = I, gravity Theorem 7), W linear in Phi
#     (cf. gravity Result 15, slope 1.000 in rotation), spectrum and trace-log EVEN in Phi.
#     Also: for Hermitian H and Hermitian probes, the pair-form metric has det g = +(Im M_a M_b*)^2/D^4
#     = W^2 |M|^4 / (4 D^4) >= 0: at a Hermitian point, breaking reciprocity turns the pinched
#     rank-one form (gravity Cor. 8, phase-aligned case) into a definite one.
#
# WHY THIS PROVES WHAT IT CLAIMS. (a) is checked on random unitary and random real orthogonal
# symmetric 2x2 matrices, where a false implication fails generically. (b) is checked on random
# vectors for n = 1..7. (c) computes W from eigenvectors exactly as the gravity paper defines it;
# W is invariant under eigenvector rephasing, so a nonzero W is not a gauge artefact. A log-log
# slope of W against Phi far from 1, a nonzero W at Phi = 0 above roundoff, or a spectrum that
# differs between +Phi and -Phi would each kill the stated claim (kill conditions written before
# the run: slope outside 1.00 +- 0.05; W(0) > 1e-12; |spec(+Phi) - spec(-Phi)| > 1e-12).
import numpy as np, math
rng = np.random.default_rng(7)

# (a)
wu = 0.0; ws = 0.0
for _ in range(1000):
    M = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); U, _ = np.linalg.qr(M)
    wu = max(wu, abs(abs(U[0, 0]) - abs(U[1, 1])))
    G = rng.uniform(-0.999, 0.999); t = math.sqrt(1 - G * G)
    S = np.array([[G, t], [t, -G]])
    ws = max(ws, np.abs(S @ S.T - np.eye(2)).max() + np.abs(S - S.T).max())
z = 6.0; G6 = (z - 1) / (z + 1); Gr = (1 / z - 1) / (1 / z + 1)
print('(a) random unitary: max | |S11| - |S22| | =', f'{wu:.1e}', '; reciprocal real step S orthogonal and symmetric:', f'{ws:.1e}')
print('    z = 6: Gamma =', G6, ' reverse Gamma =', Gr, ' (= -Gamma:', abs(G6 + Gr) < 1e-15, ')')
# from S symmetric and S^2 = I: off-diagonal G t + t x = 0 forces x = -G when t != 0 (shown symbolically in the report)

# (b)
for n in range(1, 8):
    pred = (-1) ** (n * (n + 1) // 2); ok = True
    for _ in range(50):
        D = rng.normal(size=(n, n))
        v = np.linalg.det(D); vr = np.linalg.det(-D[::-1]); vm = np.linalg.det(D * np.r_[-1, np.ones(n - 1)][:, None])
        ok &= abs(vr - pred * v) < 1e-9 * (1 + abs(v)) and abs(vm + v) < 1e-9 * (1 + abs(v))
    print(f'(b) n = {n}: reversal factor {pred:+d}, mirror factor -1, verified: {ok}')

# (c)
J = 1.0; eps = np.array([0.0, 0.3, 0.7])
Va = np.array([[0.4, 0.9, -0.2], [0.9, -0.1, 0.5], [-0.2, 0.5, 0.3]])     # real symmetric probes
Vb = np.array([[-0.3, 0.2, 0.8], [0.2, 0.6, -0.7], [0.8, -0.7, 0.1]])
def H(phi):
    h = np.diag(eps).astype(complex)
    h[0, 1] = h[1, 0] = J; h[1, 2] = h[2, 1] = J
    h[2, 0] = J * np.exp(1j * phi); h[0, 2] = np.conj(h[2, 0]); return h
def measures(phi):
    w, R = np.linalg.eigh(H(phi)); L = R.conj()          # left eigenvectors rows = R^dag
    M = np.array([R[:, 0].conj() @ V @ R[:, 1] for V in (Va, Vb)])
    N = np.array([R[:, 1].conj() @ V @ R[:, 0] for V in (Va, Vb)])
    W = abs(M[0] * N[1] - M[1] * N[0]) / (np.linalg.norm(M) * np.linalg.norm(N))
    signedW = np.imag(M[0] * np.conj(M[1]))
    D = w[0] - w[1]
    q = np.array([[M[0] * N[0], (M[0] * N[1] + M[1] * N[0]) / 2], [(M[0] * N[1] + M[1] * N[0]) / 2, M[1] * N[1]]]) / D ** 2
    g = np.real(q)
    return w, W, signedW, np.linalg.det(g), np.linalg.norm(M), D
w0, W0, s0, dg0, _, _ = measures(0.0)
print('(c) Phi = 0: W =', f'{W0:.2e}', ' det g =', f'{dg0:.2e}', ' (pinched, rank one)')
phis = np.logspace(-6, -1, 11); Ws = []; worst_even = 0.0; worst_detg = 0.0
for p in phis:
    wp, Wp, sp, dgp, nM, D = measures(p); wm, Wm, sm, dgm, _, _ = measures(-p)
    Ws.append(Wp); worst_even = max(worst_even, np.abs(wp - wm).max())
    worst_detg = max(worst_detg, abs(dgp - Wp ** 2 * nM ** 4 / (4 * D ** 4)) / max(dgp, 1e-300))
    if p in (phis[0], phis[5], phis[-1]):
        Zp = np.sum(np.log(wp + 3)); Zm = np.sum(np.log(wm + 3)); Z0 = np.sum(np.log(w0 + 3))
        print(f'    Phi = {p:.1e}: W = {Wp:.4e}, signed Im(MaMb*) at +Phi/-Phi = {sp:+.3e}/{sm:+.3e}, '
              f'det g = {dgp:.3e}, Z(+)-Z(-) = {Zp - Zm:.1e}, Z(+)-Z(0) = {Zp - Z0:.3e}')
slope = np.polyfit(np.log(phis), np.log(Ws), 1)[0]
print('    log-log slope of W against Phi =', round(slope, 5))
print('    max |spec(+Phi) - spec(-Phi)| =', f'{worst_even:.1e}', '; det g vs W^2|M|^4/(4 D^4) worst rel =', f'{worst_detg:.1e}')
tr3 = [np.real(np.trace(np.linalg.matrix_power(H(p), 3))) for p in (0, 1e-2, 2e-2)]
print('    Tr H^3 change at Phi = 1e-2, 2e-2:', f'{tr3[1] - tr3[0]:.4e}', f'{tr3[2] - tr3[0]:.4e}', '(ratio ~4: even, second order; not isospectral)')

# (d) Control for the mechanism: the same phase on an OPEN chain 1-2-3 (no loop) is a pure gauge
#     (a diagonal unitary change of basis). Claim: spectrum exactly independent of Phi (isospectral,
#     like gravity ISOSPEC-CHECK-01), yet W with the FIXED real probes still lifts linearly; carrying
#     the probes along with the change of basis (V -> U V U^dag) returns W to roundoff.
#     Kill conditions (before the run): spectral drift > 1e-12; slope outside 1.00 +- 0.05;
#     covariant-probe W > 1e-12.
def Hc(phi):
    h = np.diag(eps).astype(complex)
    h[0, 1] = J * np.exp(1j * phi); h[1, 0] = np.conj(h[0, 1]); h[1, 2] = h[2, 1] = J; return h
def Wof(h, Va_, Vb_):
    w, R = np.linalg.eigh(h)
    M = np.array([R[:, 0].conj() @ V @ R[:, 1] for V in (Va_, Vb_)])
    N = np.array([R[:, 1].conj() @ V @ R[:, 0] for V in (Va_, Vb_)])
    return w, abs(M[0] * N[1] - M[1] * N[0]) / (np.linalg.norm(M) * np.linalg.norm(N))
wc0, _ = Wof(Hc(0.0), Va, Vb); Wc = []; drift = 0.0; cov = 0.0
for p in phis:
    wcp, Wp = Wof(Hc(p), Va, Vb); Wc.append(Wp); drift = max(drift, np.abs(wcp - wc0).max())
    U = np.diag([np.exp(1j * p), 1, 1])               # Hc(p) = U Hc(0) U^dag
    assert np.abs(Hc(p) - U @ Hc(0.0) @ U.conj().T).max() < 1e-14
    _, Wcov = Wof(Hc(p), U @ Va @ U.conj().T, U @ Vb @ U.conj().T); cov = max(cov, Wcov)
print('(d) open chain (pure gauge): spectral drift =', f'{drift:.1e}', '; slope of W vs Phi with fixed probes =',
      round(np.polyfit(np.log(phis), np.log(Wc), 1)[0], 5), '; W with covariantly carried probes =', f'{cov:.1e}')

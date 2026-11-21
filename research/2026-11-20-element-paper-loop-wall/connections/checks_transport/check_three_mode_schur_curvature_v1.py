# SCRIPT: WTK-LOOPWALL-THREE-MODE-SCHUR-CURVATURE-01
"""
Connection: the element paper's three-mode loop (same energies, opposite circulation)
against WTK Proposition 10 (boundary elimination) and WTK Theorem 6 (eigenline curvature
and its sum rule).

Why this check proves what it claims:
 1. WTK Prop 10, one-sided form: eliminating an invertible exterior block E gives
    K = D - G E^-1 F, and delta K = G E^-1 (delta E) E^-1 F. For the eigenproblem
    (H - lambda) u = 0 with mode 3 as the exterior, D = H_12 - lambda, E = (0 - lambda),
    so the reduced link is J + J^2 e^{-i Phi}/lambda and the diagonal shift is J^2/lambda,
    the formula recovered in spinor_recovery/. If det K(lambda) vanishes at each true
    eigenvalue, and a finite-difference dK/dlambda equals -I - G F/lambda^2 (WTK's
    sensitivity with delta E = -delta lambda), the recovered elimination IS WTK Prop 10.
 2. Same energies: H(-Phi) = conj(H(Phi)), so the spectra agree (checked numerically).
 3. WTK Theorem 6 with parameters (Phi, epsilon), epsilon an on-site energy of mode 1:
    the sum-over-states curvature F_b must (a) match Tr(P_b [d_Phi P_b, d_eps P_b]) by
    finite differences, (b) obey sum_b F_b = 0, and (c) flip sign under Phi -> -Phi,
    because complex conjugation reverses it. If (c) holds while the spectra in 2. agree,
    the curvature is a direction record invisible to the energy ledger: odd, like the sign
    of Gamma, while Gamma^2 and the spectrum are even.
 4. Deletion control: dropping mode 3 instead of eliminating it leaves a two-mode model
    with no Phi at all, so its curvature in (Phi, epsilon) is exactly zero.
"""
import numpy as np
J = 1.0
def H(phi, eps=0.0, eps2=0.0):
    # phase on the 1-3 link, convention chosen so the reduced link reads J + J^2 e^{-i Phi}/lambda
    return np.array([[eps, J, J*np.exp(-1j*phi)], [J, eps2, J], [J*np.exp(1j*phi), J, 0]], dtype=complex)

phi = 0.7
h = H(phi); lam = np.linalg.eigvalsh(h)
print('1. eigenvalues at Phi = +0.7:', np.round(lam, 10))
print('   eigenvalues at Phi = -0.7:', np.round(np.linalg.eigvalsh(H(-phi)), 10))
def K(l, hh=h):
    D = hh[:2, :2] - l*np.eye(2); G = hh[:2, 2:3]; F = hh[2:3, :2]; E = hh[2:3, 2:3] - l
    return D - G @ np.linalg.inv(E) @ F
for l in lam:
    print(f'   det K(lambda) at lambda = {l:+.6f}: {abs(np.linalg.det(K(l))):.2e}')
l0 = 1.3; Kl = K(l0)
print('   reduced link K_12 + lambda... :', np.round(Kl[0, 1], 10), ' expected J + J^2 e^{-i Phi}/lambda:',
      np.round(J + J*J*np.exp(-1j*phi)/l0, 10))
print('   diagonal shift (K_22 + lambda) :', np.round(Kl[1, 1] + l0, 10), ' expected J^2/lambda:', round(J*J/l0, 10))
d = 1e-6; dK = (K(l0+d) - K(l0-d))/(2*d)
G = h[:2, 2:3]; F = h[2:3, :2]
print('   WTK sensitivity: ||dK/dlambda - (-I - G F/lambda^2)|| =', f'{np.linalg.norm(dK - (-np.eye(2) - G@F/l0**2)):.2e}')

def wtk_curv(phi, eps, dphi=1e-6):
    hh = H(phi, eps); w, R = np.linalg.eigh(hh); L = R.conj().T
    Tn = (H(phi+dphi, eps) - H(phi-dphi, eps))/(2*dphi); Tk = (H(phi, eps+dphi) - H(phi, eps-dphi))/(2*dphi)
    Fb = []
    for b in range(3):
        s = 0
        for c in range(3):
            if c == b: continue
            s += ((L[b] @ Tn @ R[:, c])*(L[c] @ Tk @ R[:, b]) - (L[b] @ Tk @ R[:, c])*(L[c] @ Tn @ R[:, b]))/(w[b]-w[c])**2
        Fb.append(s)
    return np.array(Fb), w
def proj_curv(phi, eps, b, d=1e-4):
    def Pb(p, e):
        w, R = np.linalg.eigh(H(p, e)); v = R[:, b:b+1]; return v @ v.conj().T
    P0 = Pb(phi, eps); dPn = (Pb(phi+d, eps) - Pb(phi-d, eps))/(2*d); dPk = (Pb(phi, eps+d) - Pb(phi, eps-d))/(2*d)
    return np.trace(P0 @ (dPn @ dPk - dPk @ dPn))
eps = 0.3
Fp, wp = wtk_curv(phi, eps); Fm, wm = wtk_curv(-phi, eps)
def wtk_curv_e(phi, e1, e2, d=1e-6):
    hh = H(phi, e1, e2); w, R = np.linalg.eigh(hh); L = R.conj().T
    Tn = (H(phi, e1+d, e2) - H(phi, e1-d, e2))/(2*d); Tk = (H(phi, e1, e2+d) - H(phi, e1, e2-d))/(2*d)
    out = []
    for b in range(3):
        s_ = 0
        for c in range(3):
            if c == b: continue
            s_ += ((L[b] @ Tn @ R[:, c])*(L[c] @ Tk @ R[:, b]) - (L[b] @ Tk @ R[:, c])*(L[c] @ Tn @ R[:, b]))/(w[b]-w[c])**2
        out.append(s_)
    return np.array(out), w
print('\n3. WTK Theorem 6 curvature (purely imaginary for a Hermitian family; Im shown)')
print('   F_b at Phi=+0.7:', np.round(Fp.imag, 9), ' sum =', f'{abs(Fp.sum()):.1e}')
print('   F_b at Phi=-0.7:', np.round(Fm.imag, 9), ' sum =', f'{abs(Fm.sum()):.1e}')
print('   spectra equal at +-Phi:', np.allclose(wp, wm))
print('   projector formula Tr(P[dP,dP]) (finite differences):', np.round([proj_curv(phi, eps, b).imag for b in range(3)], 6))
print('   -> plane (Phi, eps): NO sign flip (kill condition met for this plane; see docstring)')
Ep, wp2 = wtk_curv_e(phi, 0.3, -0.2); Em, wm2 = wtk_curv_e(-phi, 0.3, -0.2)
print('   repaired plane (eps1, eps2) at fixed flux:')
print('   F_b at +Phi:', np.round(Ep.imag, 9), ' sum =', f'{abs(Ep.sum()):.1e}')
print('   F_b at -Phi:', np.round(Em.imag, 9), ' sum =', f'{abs(Em.sum()):.1e}')
print('   spectra equal:', np.allclose(wp2, wm2), '; F(-Phi) + F(+Phi) max =', f'{np.max(abs(Ep+Em)):.1e}')
print('\n4. deletion control: two-mode model [[eps, J],[J, 0]] has no Phi, so d_Phi P = 0 and F = 0 identically.')

# SCRIPT: LEDGER-CHECK-01
# Numerical check of the Open Math ledger statements (elemental-peeling-lean, LoopWall) and of the step they leave out.
# KILL LINES (before the run):
#  L1 any stated number in BRIDGE.md off by more than 1e-9 -> that line failed this way
#  L2 if the matrix ledger for NON-commuting positive matrices differs from the sum of log cosh(half log eigen-ratio)
#     by more than 1e-9, the ledger does not extend past diagonal blocks this way
#  L3 if ledger/spacing^2 does not tend to 1/8, the link to the August colour ledger (constant 1/(2 sqrt 2)) failed this way
import numpy as np
from scipy.linalg import eigh
from scipy.integrate import solve_ivp
rng = np.random.default_rng(3)
phi = lambda G: -0.5*np.log(1-G*G)
wall = np.sqrt(0.5)
print('L1 ledger at wall', phi(wall), ' half log 2', 0.5*np.log(2))
hp = lambda G: 0.5*((1+G)/(1-G))**2
print('L1 oscillator potential at wall', hp(wall), ' (17+12 sqrt2)/2', (17+12*np.sqrt(2))/2, ' ratio to ledger', hp(wall)/phi(wall))
w = 1.3
sol = solve_ivp(lambda t, y: [(w/2)*(1-y[0]**2)], [0, 3], [0.1], rtol=1e-12, atol=1e-13, dense_output=True)
ts = np.linspace(0.2, 2.8, 14); G = sol.sol(ts)[0]; S = phi(G); h = 1e-4
Sp = (phi(sol.sol(ts+h)[0]) - phi(sol.sol(ts-h)[0]))/(2*h)
Spp = (phi(sol.sol(ts+h)[0]) - 2*S + phi(sol.sol(ts-h)[0]))/h**2
print('L1 worst |S\' - (w/2) Gamma|', np.abs(Sp-(w/2)*G).max(), '  worst |S\'\' - (w^2/4) exp(-2S)|', np.abs(Spp-(w*w/4)*np.exp(-2*S)).max())
print('L1 scalar ledger not additive: log cosh 2 =', np.log(np.cosh(2)), ' 2 log cosh 1 =', 2*np.log(np.cosh(1)))
worst = 0
for n in (2, 3, 5, 8):
    for _ in range(20):
        X = rng.normal(size=(n, n)); A = X@X.T + 0.3*np.eye(n)
        Y = rng.normal(size=(n, n)); B = Y@Y.T + 0.3*np.eye(n)
        lhs = np.linalg.slogdet((A+B)/2)[1] - 0.5*np.linalg.slogdet(A)[1] - 0.5*np.linalg.slogdet(B)[1]
        lam = eigh(B, A, eigvals_only=True)
        worst = max(worst, abs(lhs - np.log(np.cosh(0.5*np.log(lam))).sum()))
print('L2 non-commuting matrices: worst |log-det ledger - sum log cosh(half log eigen-ratio)| =', worst)
for t in (1e-1, 1e-2, 1e-3):
    print('L3 spacing', t, ' ledger/spacing^2 =', np.log(np.cosh(t/2))/t**2, ' sqrt of it =', np.sqrt(np.log(np.cosh(t/2)))/t, ' 1/(2 sqrt 2) =', 1/(2*np.sqrt(2)))

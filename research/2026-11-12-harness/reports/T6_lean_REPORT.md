# T6_lean REPORT (12 Nov 2026)

## Results first
- Lean runs here: toolchain 4.34.1 installed from GitHub releases (lean-4.34.1-linux.tar.zst, 580 MB, github.com + release-assets.githubusercontent.com both allowed). `lean --version` = 4.34.1 (commit 5045d00). Linked in elan as leanprover/lean4:v4.34.1.
- Mathlib cache: BLOCKED. Host cache.mathlib.org:443 answers CONNECT 403 (proxy status log). Mathlib sources from github.com are fine.
- Whole-project build (`lake build` of votkp-lean): NOT DONE. All 14 project files use `import Mathlib` (8,529 modules, 2 cores, 7 GB); no cache, so not attempted. The repo has no lake-manifest.json; `lake update mathlib` was needed to create one (mathlib rev v4.34.1 resolved from GitHub). Consequence: the 140 VOTKP theorems, the 15 FalseControls and `#print axioms` on them remain uncompiled; the earlier static audit stands.
- Instead I built the narrow closure needed by the new file: 1,842 jobs (about 1,550 Mathlib modules plus Batteries/Aesop/etc.), from source, in background pieces; one piece was cut off by the usage limit and resumed from built files. Compute time of the build: about 60 minutes.
- NewProps.lean COMPILES: `lake env lean NewProps.lean` gives 0 errors, 0 warnings. 43 theorems, no sorry, no axiom declarations; `#print axioms` on every one of the 43 gives only [propext, Classical.choice, Quot.sound].
  (Three lint options are switched off at the top; they only silenced style warnings.)

## What NewProps.lean proves (namespace NewProps; imports are narrow Mathlib modules, not `import Mathlib`)
- 22.1: `prop22_1_weight` (||P H (1-P)||_F^2 = ||B||_F^2), `prop22_1_commutator` ((1/2)||[H,P]||_F^2 = ||B||_F^2), `prop22_1_trace` (Re Tr(B B^H) = ||B||_F^2, the lag-zero reading). General finite index types p, q, complex matrices, H = fromBlocks A B B^H D.
- 22.2: `prop22_2` (the four coefficients (di-dj)/(di+dj), E-/E+, E-/(E-+E+), (E+-E-)/E+ against Gamma = peel(di/dj), peel z = (z-1)/(z+1)); `budget`, `difference`; `half_line` (Gamma^2 = 1/2 at z = 3+2 sqrt 2); `half_line_share` (Gamma^2 = 1/2 iff E+ = 2 E-).
- 22.3: `prop22_3` (k-fold oplus of Gamma = peel(z^k), z > 0, all k); `peel_inv` (peel z^-1 = -peel z); `prop22_3_charge` ((Zc^2-Zv^2)/(Zc^2+Zv^2) = r oplus r).
- 24.1: `prop24_1_touch` (dim ker N = 1, dim ker N^2 = 2 gives N nonzero on ker N^2, i.e. one Jordan block's non-zero nilpotent part); `prop24_1_split` (dim ker N = 2 = dim ker N^2 gives N = 0 on ker N^2). Finite-dimensional, any field.
- 25.1: the loop as explicit SL2(C) matrices (boosts Bx, By with half-angle (c,s), c^2-s^2 = 1, loop = Bx By Bx^-1 By^-1): `loopW_trace` (tr W = 2 - 4 s^4); at the wall s^2 = 1: `loopW_wall_trace` (tr W = -2), `loopW_wall_nilpotent` ((W+1)^2 = 0), `loopW_wall_ne` (W+1 != 0): one Jordan block. K: `K_eq_inv_T_sub_R`, `K_eq_inv_sin_sq`, `K_pair` (Gamma Gamma' = 1/2 gives equal K below and beyond the wall). Exact rationals: `peel_3/5/7` (1/2, 2/3, 3/4), `pair_5_7` (G5*G7 = 1/2), `K_3` (2), `K_5` (9), `K_7` (9), `z5_trace` (R/T = 4/5, tr W = -14/25, cos(theta/2) = -7/25, (tr W)^2 = 196/625), `z5_cos_turn` (cos theta = -527/625 from cos(theta/2) = -7/25), `z7_trace` (R/T = 9/7, tr W = -226/49), `z5_centre` (s = 1/3, rho^2 = 1/2, cosh eta = 3), `z3_centre` (rho = sqrt 2 - 1), `rho_sq_half_iff` (rho^2 = 1/2 iff Gamma = 2/3, i.e. z = 5 only, for 0 < Gamma, Gamma^2 < 1/2).
- 25.2 (arithmetic of the formula only): `share_mem` (0 <= c_n <= 1), `share_fixed_line` (sin phi = 0 gives c_n = 1/2, no signal), `share_peel` (1 - 2 c_n = -sin(n theta) sin phi), `third_axis_z5` (2 Gamma^2 = 8/9), `third_axis_half_line` (2 Gamma^2 = 1/2 with Gamma > 0 iff z = 3).

## Stated in prose only (left out of the file)
- 22.1 third reading beyond lag zero: K(t) = B exp(-iDt) B^H (matrix exponential not imported; only Tr K(0) is in Lean).
- 22.2/22.3 tanh form: Gamma = tanh(ln z / 2) and Gamma(z^k) = tanh((k/2) ln z) (needs log; already in the repo as Smith.theorem 8.1 / tanh_add'; the new file proves the algebraic peel form). Half power Gamma(z^(1/2)) and the matter-wave reading.
- 24.1: the "cyclic summand Z[t^+-1]/(f^2)" statement and the module-theoretic equivalence with the second Alexander polynomial; the knot counts (376/199, 121/77) are data.
- 25.1: (a) the link between the loop and the Lorentz/ball picture (turn angle theta, centre of turn as a point of the ball, cosh eta = 1/s as a distance), (b) Petermann factor as an eigenvector angle, (d) the exact decay w -> e^{-lambda} w beyond the wall and the distance formula d_n, (e) the fixed-direction angle alpha (only its K-algebra is in Lean). The explicit matrices prove trace and Jordan-block facts; that these matrices model "two perpendicular steps of ratio z" with Gamma = tanh(r/2), s = sinh(r/2), is the paper's definition and is not re-derived here.
- 25.2: the formula c_n = (1/2)[1 + sin(n theta) sin phi] itself (needs the geometry), kappa = theta/2, the direction-count cap N(n, eps) (arcsin and floor, 144 numerical cases), the 8/17 and cap 29 to 21 numbers in the ball frame, the irrationality of the turn (Niven-type step; rational cosine -527/625 is not in the file), the 0.301 body-diagonal value.

## Untested / caveats
- The project's own 140 theorems were not compiled here. The two-trees/ files (core Lean, no Mathlib: comm5_trace etc.) were also not compiled in this run; I did not use them.
- No error was met that needed a statement to be dropped; unproved statements were never written into the file.
- Not pushed anywhere.

## Paths
- /home/claude/harness/workers/T6_lean/NewProps.lean (final, compiled)
- /home/claude/harness/workers/T6_lean/NewProps.draft.lean (identical apart from the lint switches)
- Project copy with built Mathlib closure: /home/claude/harness/workers/T6_lean/proj (lake-manifest.json newly created there; the original clone is untouched). Check command: `cd proj; export PATH=$HOME/.elan/bin:$PATH; lake env lean ../NewProps.lean`
- Toolchain: /home/claude/harness/workers/T6_lean/tc/lean-4.34.1-linux
- Logs: build_closure.log, build_closure_part1.log. Scratch: s25.lean, tools/.

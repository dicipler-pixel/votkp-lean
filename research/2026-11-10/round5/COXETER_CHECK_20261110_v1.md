# Coxeter repo check (coxeter-rank2-lean @ 96948be) — 10 Nov 2026

Read in full: 3 Lean modules (58 theorems, regex count 22+22+14), gate.py, verify.py, CI, all swarm files,
16 model readings, 6 submissions. CI green on 6574232 (the two new theorems).

Prose defects (no Lean wrong):
1. RankTwoClassification.lean titsForm docstring: Gram "diag b 1 * A * diag 1 a" is wrong (not symmetric,
   does not give titsForm); correct is diag(b,a)*A. Checked with sympy.
2. Three docstrings still say psd at ab=4 / indefinite above are unformalized (proved in 6574232).
3. "Open converses" are corollaries of proved theorems for a,b>=1. Radical: B((a,2),(x,y)) = -a*y*(ab-4).
4. Library file defines its own cartan/titsForm instead of importing swarm/Targets.lean (identical today).
5. Reading counts disagree across AUDIT §1, §5a, REVIEW-PACKET, review/README; RESULT.md "Still open" stale.

Links to Yang–Mills (checked symbolically):
- diag(b,a)*cartan has LDL pivots 2b and -a(ab-4)/2: the trichotomy is one Schur-pivot sign.
- inverse(cartan 1 1) = (1/3)[[2,1],[1,2]] is the Casimir Gram; 1/2<L,L+2rho> = c(p,q).
  Gives the ONE-LINK floor only; graph floors 28/3, 40/3, 43/3 need gauge invariance (Green, ink).
- Mathlib CoxeterMatrix.I 1 = I2(3), order 6, the SU(3) Weyl group.
- yang-mills-lean SchurInertiaCount.one_negative_index_of_opposite_subspaces can turn statement 14 into
  signature (1,1) in Lean.

Yang–Mills Lean added this session: PR #10, WindowWallCells.lean (5 certified cells into
WindowWallFinite.no_window), plus config audit of the window-wall modules: 107 theorems, 3 false controls,
CI run 42949390594 green.

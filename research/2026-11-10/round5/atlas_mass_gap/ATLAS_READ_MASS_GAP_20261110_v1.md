# The atlas, read for the mass gap: what we need and where it already sits

Jeromie Beasley · 10 November 2026

Source: atlas card set v7, B1–B207, Zenodo 10.5281/zenodo.23590925. The card text was taken from relational-atlas-lean/atlas/coverage/coverage.json, whose checksums match that record.

Coverage of the read:
- B1–B69: read in full by the main session (notes in MY_READ_B1_B69.md).
- B70–B138 and B139–B207: read in full, all fields, by two reading agents. Each reported complete coverage and no unparsed card.

Not in this read:
- B208–B216.
- The Atlas II W-cards.

## What the mass gap needs (the problem as set)

H = κ Σ C₂ + λ Σ (3 − Re χ) on an SU(3) lattice. What exists: window-wall exclusions, the retained-geometry Schur certificate, tail floors, and the one-link √λ picture, all on finite lattices.

What is missing:
1. A gap bound uniform in volume.
2. Correct scaling into the continuum.
3. An honest bridge from the finite certified algebra to 1 or 2.

## The finding: the route is one chain, and every link is already a card

### Link A. The gap is an inner gap, so retain rank 2 (B113, B120, B105)
- B113 [theorem]: a cluster held as one subspace is protected by its outer gap, ‖X‖ ≤ ‖Q′EP‖/δ. The members of the cluster are not protected. B120 says an individual level needs its own resolved inner gap.
- E₁ − E₀ is exactly such an inner gap. So the retained block of the Schur certificate must hold the vacuum and the first excited level together (rank 2), and the gap is read inside it.
- B105 [theorem, Lean `reduced_associator`]: what the discard returns to the retained record is an associator, P[xQ(yz) − Q(xy)z]. That is the exact bookkeeping of what the Schur shape keeps.

### Link B. Concavity reaches the gap through the sum E₀ + E₁ (B75)
- B75 [theorem, Lean `middle_cancels`]: in an ordered spectrum the extremal level's terms add and a middle level's terms cancel.
  - So E₀(κ) is concave, which is the window-wall concavity.
  - E₁(κ) by itself is not concave. That is exactly why the window-wall secants cannot reach E₁ − E₀ directly.
- The repair: E₀ + E₁ is concave in κ for a family linear in κ. This is the minimum over two-dimensional subspaces of a linear function: a standard theorem, not a card.
  - It gives the gap bound E₁ − E₀ ≥ secant-lower(E₀ + E₁) − 2·(upper bound on E₀).
  - It uses the same exact rational secant machinery that is already in Lean.
- B126 gives the multiplicative fork: log λ₀ + log λ₁ for H − c, with c below E₀. Build both forks and compare them.

### Link C. Glue blocks by Schur complements, and the chain is in Lean (B48, B175, B104)
- B48 [derived]: K_Σ = D_Σ − C A⁻¹ B − G E⁻¹ F. The seam keeps the loading from both sides. Changing the interior block moves the seam only through E⁻¹ (δE) E⁻¹.
- B175 [theorem, Lean light-ledger-lean `schur_boundary_residual` … `passive_boundary_chain`]: boundary eliminations compose. Here this means: reduce a block to its seam, glue, and reduce again.
  - The uniform-volume statement becomes: the certified floor of the seam operator does not fall when the lattice doubles.
- B104 [theorem in its discrete form, Lean `silent_forever_iff`]: with local terms, the coupling between regions X and Y through the discarded sector starts at order d(X, Y). The Schur coupling between distant blocks is suppressed by locality to a known order.

### Link D. A floor in the well that adds up over plaquettes (B128)
- B128 [theorem, Lean upg-lean `unit_defect_add_guard`]: δ + g² ≤ 4, with the winding w held while g > 0.
- Checked here (B128-FLOOR-CHECK-01):
  - For U ∈ SU(3), the card's defect is δ = (2/3)(3 − Re χ(U)) exactly (error 1.8e-15).
  - On the w = ±1 sector, 3 − Re χ ≥ 4: the minimum is 4.000000000000 on a 1201² grid. The bound is reached only at g = 0 (an eigenvalue at −1).
- The analytic reason: Σθ = ±2π with |θ| ≤ π. The stationary points are (2π/3)×3, giving 4.5, and the boundary points (π, a, π − a), giving 4.
- What it gives: a per-plaquette operator inequality, (3 − Re χ) ≥ 4·1{w ≠ 0}, that is additive over plaquettes. It is a floor that does not dilute with volume, for configurations carrying winding.
- What it does not give: w is a region of the group, not a conserved number. The electric term κC₂ moves across g = 0 freely. This is a floor on the potential, not a protection.

### Link E. The contour count as the gap witness (B35, B65, B140)
- B35: the enclosed count stays an exact integer while amplitudes diverge.
- B65 and B140: ‖P‖ ≤ ℓ(Γ) sup‖R‖ / 2π.
- Put a circle around E₀. "The gap stays open" becomes: the count is exactly 1, and the resolvent is certified bounded on that one circle.

### Link F. The continuum side (item 2)
- B160 [theorem, Lean dirac-time-lean `common_gap_scaling`]: a scaling window is where every gap ratio (E_j − E₀)/(E₁ − E₀) is constant. Shape (projector) data alone cannot set the unit: one scale must come from outside the projector geometry.
- B63 [reading] and B80 [measured]: rescaling shows only as a running, log ξ, and the census measures log ξ independently of any eigenvalue solve. This gives a second estimator of the gap for the continuum check.
- B189 [theorem, Lean votkp-lean `smith_identity`]:
  - Γ = tanh(½ ln d_i/d_j), and the boost keeps the product d_i d_j.
  - With d_i = κ and d_j = λ, the leading one-link gap √(2κλ) depends only on the product κλ.
  - ½ ln(κ/λ) is the running coordinate. This is a reading for SU(3), and exact in the harmonic limit.

## The edges, marked so nobody walks off them
- B144: the cheap route, gluing while the seam is small against the block gap, holds only at strong coupling. In this setup ‖V_seam‖ ≤ (9/2)λ n_seam against a gap of about √(2κλ). Its constant doubles at every gluing. Untested numbers, from the card's hypothesis.
- B193: a floor made by a twist spreads around a ring and decays as 1/N. A uniform floor must come from something that does not spread. B194, a floor from holonomies with no shared invariant subspace, is the candidate kind.
- B130, B131, B72: probe and response bounds are upper bounds on the gap as the probe sees it. A level the probe cannot couple to is invisible. They cannot certify a gap from below.
- B141: gap ⇒ area law only in that direction. A census can contradict a gap but cannot prove one.
- B182: the limits "volume to infinity" and "λ to infinity" need not commute. The order must be declared.

## The one first run, for Jeromie to call
On the lattices already certified (two squares at λ = 8 first), certify a lower bound on E₁ − E₀ two ways, side by side:
- (i) the rank-2 retained Schur block (Link A);
- (ii) the concave sum E₀ + E₁ with the existing exact rational secants (Link B).

Kill line, written before the run: if both lower bounds are ≤ 0 on two squares at λ = 8, where the gap is known to be positive, neither route certifies a gap in this setup.

If either survives, the volume step is Link C: one doubling of the strip, compared at the seam.

Nothing here proves the mass gap. It is the route the atlas already holds, laid out in order, with one checked identity added (Link D).

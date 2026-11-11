# Atlas v7, cards B1–B69: read for the mass gap

Coverage: I read B1–B69 in full. For B1–B16 that covered every field. For B17–B69 I read the content fields (claim, explanation, Carry/Check/Arrive, closed-when, source, audit notes). The proof-reference and next-obligation fields are ledger boilerplate and are the same on every card.

## Moves that bear on the problem

### 1. B58 + B16 + B31: gluing, with the seam term paid in principal angles (local gap to global gap, item 1)
- B58 [conjecture as a cone statement; the subadditivity is a theorem]:
  - O(A ∪_Σ B) = O(A) + O(B) + Σ_k log(1 − μ_k) ≤ O(A) + O(B).
  - The seam term is a sum over the overlap channels μ_k across the cut.
- B16 [theorem] ½‖P_u − P_v‖² = sin²θ: the projector distance is the principal angle.
- B31 [theorem] F = ΠW(1−Π) + (1−Π)WΠ: change lives only between a subspace and its complement.
- The move: for local low-energy projectors P_A and P_B on overlapping blocks, the quantity that decides whether a local gap survives gluing is the principal angle between their ranges, measured on the overlap. In his coordinate that is a census of seam channels: μ_k = cos² of the seam angles.
- The mainstream form is the martingale / angle criterion for uniform gaps of frustration-free Hamiltonians. It needs ‖P_A P_B − P_{A∩B}‖ ≤ ε with ε small against the number of overlaps, and it is exactly a bound on the largest μ_k.
- The hypothesis it carries, which must not be dropped (the alloy rule): frustration-freeness, meaning the local ground spaces intersect. The SU(3) Kogut–Susskind H is not frustration-free: the electric and magnetic terms have no common zero.
- Aimed where: at the retained (Schur) block operators rather than at H itself. Equivalently, at H − Σ(local floors), the "local energy floors" dependency already flagged in the YM file.
- Unrun:
  - The one thing: on the strip of plaquettes, compute the largest seam overlap μ_max(ℓ) between the low-energy projectors of two overlapping blocks of length ℓ, as ℓ grows.
  - Kill line: if μ_max(ℓ) does not fall below the criterion's threshold for any ℓ, this route fails in this setup.

### 2. B48: the seam is a Schur complement (local to global by iteration, items 1 and 3)
- B48 [derived]:
  - K_Σ = D_Σ − C A⁻¹ B − G E⁻¹ F.
  - δK_Σ = G E⁻¹ (δE) E⁻¹ F.
- This is already the engine of the retained-geometry certificate. What the card adds is the response formula: changing the interior block E moves the seam only through E⁻¹ on both sides.
- The move: iterate it. Reduce a block of plaquettes to its seam operator, glue two seams, and reduce again. That is a Feshbach–Schur renormalization step written in his block form.
- A gap bound that is uniform in volume follows if the reduced seam operator at step n+1 has a floor no smaller than at step n. δK shows the change is controlled by ‖E⁻¹‖² times ‖δE‖.
- Unrun:
  - The one thing: two reductions on the ladder (2 blocks, then 4), comparing the certified floor of the seam operator.
  - Kill line: if the floor falls by a fixed fraction at each doubling, the iteration does not give uniformity in this setup.

### 3. B35 + B65: the contour ledger as a gap witness that survives volume (item 1, certification side)
- B35 [measured]: Tr Π_blk = (1/2πi)∮ Tr (z − A)⁻¹ dz stays an exact integer through a wall while individual eigenprojectors diverge.
- B65 [theorem]: ‖P‖ ≤ length(Γ)·sup_Γ‖R‖/2π for a fixed contour.
- The move:
  - Put a circle of radius r around E₀ only. If the enclosed count reads exactly 1 and the resolvent is certified bounded on the circle, the gap is at least r.
  - The count is the integer ledger, the "phase crosses what amplitude cannot" record. It cannot drift: it is either 1 or a level has entered.
  - So the gap statement becomes a certified integer plus a certified resolvent bound on one circle.
- Unrun:
  - The one thing: certified resolvent bounds on the circle for the two-square and strip lattices already done.
  - Kill line: if sup‖R‖ on a fixed-radius circle grows with lattice size, the circle must shrink, and that is the gap closing in that setup.

### 4. B63 + B5/B6: a rescaling is seen only as a running (continuum limit, item 2)
- B63 [reading]: A = (c/π²) log(ξ/a) log(1/ε). Scale invariance leaks only through log ξ.
- B5/B6: with no boundary there is no census, and the entropy lives in the undecided channels.
- The move: in lattice units the correlation length is ξ/a ~ 1/(gap·a). His census coefficient therefore reads log ξ, which is an independent estimator of the gap with no eigenvalue solve. This is the "ξ·gap ≈ const" instrument control in his toolkit.
- For the continuum limit, the gap in lattice units must fall like exp(−1/(2β₀g²)). That is exactly a logarithmic running, the only channel B63 allows.
- Grade: a reading and an estimator, not a proof.
- Unrun:
  - The one thing: the census of the strip ground state at two values of λ, checking log ξ against −log(gap).
  - Kill line: if the slope d log ξ / d log(1/gap) is far from 1 (the toolkit control rejected 0.368 before), the census does not measure the gap here.

### 5. B22 + B24/B25: leakage, ledger and susceptibility kept apart (supporting the Schur certificate)
- B22 [theorem]: Σ_{n∈Π, m∉Π} |⟨m|E|n⟩|² = Tr(ΠE†QE) = ½‖[E,Π]‖² for Hermitian E.
- Applied to Π = the electric ground state and E = the plaquette term, this gives the exact leakage of the magnetic term out of the strong-coupling vacuum, with no eigenbasis. It is the numerator of the second-order shift and is computable per plaquette.
- B24: the log-det ledger has product weights and stays finite. B25: the inverse-gap weights belong to the susceptibility, which diverges as a gap closes.
- The move: watch the fidelity susceptibility of the ground state as the lattice grows. Its divergence is the sign that a gap is closing; the ledger is blind to it.
- Unrun:
  - The one thing: χ_F per plaquette against lattice size on the certified lattices.
  - Kill line: if χ_F per plaquette grows with volume at fixed λ, a level is approaching in that setup.

### Weaker links, noted so the coverage is honest
- B30/B39: |v⊥| ∝ 1/√(2λ). The same 1/√(2λ) is the zero-point width of the √λ pendulum. Untested beyond the coincidence of form.
- B42: secular interlacing confines defects to the divisor. Interlacing bounds how much one added plaquette can move E₁ − E₀ (Weyl/Cauchy). That is already used implicitly by the window wall's concavity.
- B44: a small invariant block drives the large operator. This concerns transient growth, not gaps; not useful here.
- B68: paired spectrum. No chiral grading in the pure-gauge H; not used.

## My ranking for B1–B69
1. B48 iterated (Feshbach–Schur on his seam). It extends the certificate that already works and attacks volume directly.
2. B58/B16 seam angles. They are the exact quantity in the local-to-global gap criterion, but they carry the frustration-free hypothesis, which must be named.
3. B35/B65 contour ledger. It turns "the gap stays open" into an integer plus one resolvent bound.

# Required reading, notes 1 of 2: IQGT

Reader: Session A, alone, no agents. 24 November 2026.
Text read: `iqgt_grassmannian_v7_3_1.html` from the public repository `iqgt-grassmannian-lean` (paper folder), every section 1 to 13, appendices A to D, references. The page stores its equations as drawings, so they were turned back into text with `mjx2txt.py` (in this folder) and read with the prose.
Not read tonight: the June 2026 first versions (Drive only), where the contractive-operator form lives. That is the "first vision" half and is still owed.

The notes keep to two things, as asked: how the tensor is made, and what bears on the periodic table.

## A. How the tensor is made, in the order the paper builds it

1. **The object is a projector, not a vector.** Π is a rank-k orthogonal projector: Π† = Π = Π², Tr Π = k. The space of all such is the Grassmannian Gr(k,H). (Section 2.)
2. **A move of Π is forced to cross the boundary.** Differentiating Π² = Π gives V = ΠV + VΠ, hence ΠVΠ = 0 and (I−Π)V(I−Π) = 0. Every tangent vector is block off-diagonal, with one block X from the complement into the subspace (2.1). "There are no intra-subspace contributions to the geometry."
3. **One form, defined on the complexified tangent space:** Q_Π(A,B) = Tr(Π A† B) (2.2). It is positive semi-definite because Q(A,A) = ‖AΠ‖². On two real tangent vectors with blocks X, Y it is Tr(X Y*).
4. **The split.** Q = g − (i/2)Ω with g(V,W) = ½Tr(VW) = Re Tr(XY*) and Ω(V,W) = i Tr(Π[V,W]) = −2 Im Tr(XY*) (2.3). The metric is the symmetric part, the curvature the skew part, of the one form.
5. **Remark 2.3, the line that matters most for recognising other tensors:** ½Tr(VW) looks as if it forgot Π. "The dependence has migrated from the formula into its domain." The projector is in which V are allowed, not in the formula.
6. **The factor ½ is forced** by agreement with the Bloch sphere value g_θθ = ¼ (Remark 2.4).
7. **Where Π comes from:** the Riesz contour integral Π = (1/2πi)∮(zI−Σ)⁻¹dz round the levels kept (2.4). The contour must sit in the gap.
8. **Response:** ⟨m|V|n⟩ = ⟨m|δΣ|n⟩/(λ_in − λ_out) for one level inside and one outside; zero for two on the same side (Lemma 3.1). "Each pair straddling it contributes its coupling divided by its own gap."
9. **Spectral form:** g and Ω are sums over cross-gap pairs of products of couplings over the gap squared (3.3), (3.4). Remark 3.7: the weights sit pair by pair; without them the curvature numerator would be a plain commutator.
10. **Gap bound:** ‖V‖ ≤ √(2k)‖δΣ‖/Δ (Proposition 3.5).
11. **Pullback:** a family Σ(a) is a map γ into the Grassmannian; the usual parameter-space tensor is γ*Q (4.4). "The parameter manifold does not generate the geometry; it merely selects a trajectory." Two opposite failures: gap closes (metric blows up), or the map folds with the gap open (metric degenerate) (Proposition 4.1).
12. **Silent directions:** a direction with no cross-gap block does not move Π at first order but changes the metric at second (Proposition 4.3).
13. **Redistribution:** F(Ω,Π) = (I−Π)ΩΠ + ΠΩ(I−Π) = [[Ω,Π],Π] (4.7). It is the gradient of Tr(ΩΠ) in the intrinsic metric; its flow is Brockett's and carries Π to the top-k subspace of Ω (4.8).
14. **Sharp bound:** |Ω(V,W)| ≤ 2√(g(V,V)g(W,W) − g(V,W)²) (6.1), from the 2×2 Gram determinant of Q. Equality exactly when Y = cX, a complex line; the partner is the block iX (Corollary 6.2). Deficit identity (6.3): the shortfall equals g(V,V)·g(W⊥,W⊥).
15. **One pair sum, many weights (Section 7.2):** metric weight 1; static response 2Δ; Berry connection polarizability −2/Δ; zero-temperature friction 2cΔ; curvature weight 1; orbital moment Δ. Powers of the gap choose the reading.
16. **Distance:** ‖Π₁−Π₂‖² = 2Σ sin²ϑ_i over principal angles (Proposition 8.2). So √g is the sine of a principal angle, and "sin² appears because the Hilbert–Schmidt metric is itself a sum of squared sines".
17. **Refraction:** g_∥ sin²θ = const along a geodesic (8.1), index n = √g_∥, "the rate at which the occupied subspace rotates". Polar stratum (subspace stops rotating) reflects; narrowing gap guides; a fold is silent at first order and moves at second (Propositions 8.3, 8.6).
18. **Mixed states:** Q_ρ = ¼Tr(ρ L_V L_W) with L the symmetric logarithmic derivative; reduces exactly to Q_Π (Section 9).
19. **Tip and tail (Sections 10.2, 12):** gap identity (10.4); a single vector is held by its inner gap, the cluster subspace by its outer gap (12.1). Mixing angle tan 2θ = 2g/Δ (10.6); 22.5° at coupling = half the splitting.
20. **Cards (Section 12.4):** for a permutation U with graph projector P_U, Hamming distance = (1/n)‖P_U−P_V‖² = (2/n)Σ sin²θ_j (12.2); intrinsic length L = √(Σθ_j²) (12.3); sandwich d_H/2 ≤ (1/n)Σθ² ≤ (π²/8)d_H, upper bound met only by involutions (Proposition 12.3).

## B. What makes it this tensor and not another (the recognition list)

- It is a **Gram form of cross-boundary blocks**. Positivity comes from Q(A,A) = ‖AΠ‖², nothing else.
- Its inputs are **only** moves that cross the gap. A functional that also charges for motion inside a sector is a different object.
- It is **not** multiplicative under tensor product and has no restriction order. A spectral point in the sense of the Anthropic release is the opposite kind of object: a number φ(t) per tensor, multiplicative, monotone under restriction. The meeting place is narrow and exact: both give a **distance between labelled places**. A spectral point gives d_φ(u,v) through a wire; IQGT gives the chordal distance between two projectors.
- The chordal distance d = ‖P−R‖/√2 is a **Euclidean** distance (projectors are points of a real vector space), so by itself it is a flat configuration. The intrinsic length √(Σθ²) is not.
- When every principal angle is 0 or 90°, squared chordal distance **counts** the 90° angles. That is the equality case of Proposition 12.3. The limiting price of the release (squared distance = rank, their Appendix D Step 7) and the building cone of the retest have that same form: a squared distance that is a count. Mapping to try, not yet a result: place the 16 matrices as graph projectors and read both distances.

## C. What bears on the periodic table

- **tanh in the two-level friction.** ζ_rot = 2c(Δ)Δ tanh(βΔ/2) g (Theorem 5.3 (i)). The population difference of a two-level system is a tanh of half a log-ratio, the same shape as the peel coordinate Γ = tanh(½ ln(IE_{k+1}/IE_k)) of VOTKP §8.1.
- **Gap powers.** The table of Section 7.2 is the tool for asking which power of the gap an atomic observable reads: polarizability sits at −2/Δ per pair, static response at 2Δ. The table wave found log polarizability ≈ 10.28 − 3.04 log(ionization energy); the paper's own ladder would give the exponent to compare against. Not yet compared.
- **Every spin.** Appendix C: the lowest band of d·S in spin j has g = (j/2)h, |Ω| = j sin θ, Chern number 2j, and meets the bound with equality at every point; "the lowest Landau level on a sphere carrying 2j flux quanta". A subshell of orbital angular momentum l is a spin-l multiplet. Lead, untested: read a subshell's direction geometry with j = l.
- **Tip and tail.** Subshell levels that sit together "fuse into one object; the gap decides where one object ends and the next begins" (Section 12.1). This is the paper's own rule for where a row of the table starts.
- **Locking threshold.** Coupling over splitting = ½ gives 22.5° (Remark 12.1, Example 12.2). Same ratio test as a peel step crossing a shell wall.
- **Fold seen through distances.** Example 8.8: three bodies read only through squared distances have a fold on the collinear circle; the lost direction is orientation. This is his squared-distance map, in the paper itself.

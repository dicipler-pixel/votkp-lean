# Read record 01 — IQGT (Jeromie Beasley), constructions with formulas

Source read in full: GitHub dicipler-pixel/iqgt-grassmannian-lean, paper/build, section files s1 to s13 and appendices A to C
(the newest cut of each section: s1 v7, s2 v1, s3 v4, s4 v2, s5 v4, s6 v4, s7 v3, s8 v5, s9 v2, s10 v7, s11 v6, s12 v8, s13 v2, app v6).
NOT read: the last part of Appendix D (lattice/Krylov benchmarks), the references file, the full-paper HTMLs v6 to v7.3.1 as separate versions,
the 13 June and 20 June originals. Equation numbers are the paper's own.

## A. The object
- Tangent law (2.1): V = ΠV + VΠ, so V = [[0,X],[X*,0]], X = ΠV(I−Π). Rank X ≤ k, so every trace converges.
- Lemma 2.1: every such V is a velocity; Π(t) = e^{itA} Π e^{−itA}, A = [[0,iX],[−iX*,0]].
- Tensor (2.2)-(2.3): Q_Π(A,B) = Tr(Π A†B); Q = g − (i/2)Ω; g = ½Tr(VW) = Re Tr(XY*); Ω = i Tr(Π[V,W]) = −2 Im Tr(XY*).
- Remark 2.4: g_θθ = 1/4 on the Bloch sphere fixes the factor ½.
- Riesz projector (2.4): Π_k = (1/2πi)∮(zI−Σ)⁻¹dz.

## B. Spectral realisation
- Lemma 3.1 (3.2): ⟨m|V|n⟩ = ⟨m|δΣ|n⟩/(λ_in − λ_out) for cross-gap pairs, zero otherwise.
- Prop 3.5 gap bound: ‖V‖_HS ≤ √(2k)‖δΣ‖/Δ.
- Thm 3.6 (3.3)-(3.4): g and Ω are cross-gap pair sums with weight 1/(λ_n−λ_m)².
- Remark 3.10: many-body form is quasi-adiabatic continuation, ∂Π = [Y,Π].

## C. Pullback, silence, second order
- (4.3): g_ij = Re Tr(Π∂_iΠ∂_jΠ), Ω_ij = −2 Im Tr(Π∂_iΠ∂_jΠ). (4.4): γ*Q.
- Prop 4.1: g_ij is a Gram matrix; it degenerates when γ fails to be an immersion — opposite limit to a closing gap.
- Prop 4.3: first order factors through the cross-gap block; a block-diagonal direction is SILENT (∂_BΠ = 0) but still changes the metric at second order.
- (4.5)-(4.6): ∂_k g_ij = ½Tr(∂_k∂_iΠ ∂_jΠ + ∂_iΠ ∂_k∂_jΠ), with the second-order Riesz formula (three resolvents).
- (4.7)-(4.8) redistribution: F(Ω,Π) = [[Ω,Π],Π]; gradient of Tr(ΩΠ) in g; flow Π̇ = [[Ω,Π],Π] (Brockett).

## D. Speed and cost
- Lemma 5.1: for ρ = Π/k, L = 2Π̇, F_Q = (4/k) g(Π̇,Π̇).
- Thm 5.2: t_f − t_i ≥ Δ_min 𝓛 / (√k sup‖∂_tΣ‖).
- (5.2)-(5.3): ζ_mn = 2 c_mn (p_m − p_n)(E_n − E_m) g_mn, c_mn = τ/(1 + χ²τ²(E_m−E_n)²).
- Thm 5.3: two levels ζ_rot = 2c(Δ)Δ tanh(βΔ/2) g; zero temperature band (5.4); W_ex ≥ (min 2cΔ) 𝓛²/T (5.5).
- Two-level split: ζ = τβ sech²(βΔ/2) ṙ² + 2c(Δ)Δ tanh(βΔ/2) g; |ḋ|² = ṙ² + Δ² g.

## E. Curvature bound and rigidity
- Thm 6.1 (6.1): |Ω(V,W)| ≤ 2√(g(V,V)g(W,W) − g(V,W)²). (6.2): ≤ 2√(gg)|sin θ_G|.
- Cor 6.2: equality iff Y = cX; extremal partner is the block iX (complex structure J).
- (6.3) exact deficit: g(V,V)g(W,W) − g(V,W)² − ¼Ω² = g(V,V) g(W⊥,W⊥), W⊥ block Y − cX, c = Tr(YX*)/Tr(XX*).
- Prop 6.4 (6.4): tr_h g ≥ 2√(det g/det h) ≥ |Ω_12|/√det h.
- Example 6.5: loop at polar angle 60°: projector returns exactly, phase −π(1−cos θ₀) = −π/2 does not.

## F. One pair sum, many weights (Section 7.2)
- g_n = |⟨0|∂_xΣ|n⟩|²/Δ_n², Ω_n = −2 Im(…)/Δ_n².
- Weights: metric 1; static response 2Δ; Berry connection polarizability −2/Δ; rotation friction 2cΔ; curvature 1; orbital-moment kernel Δ.
- Response function: α(x) = Σ_n 2Δ_n³ g_n/(Δ_n² − x²); ζ_rot = τ α(0) (relaxation), τ[α(0) − α(i/τ)] (with precession).
- Dipole (7.1)-(7.3): two-index form plus the rotation (three-state) terms R^{ik}_mn.
- Divergence rates at a closing gap: g, Ω as Δ⁻²; dipole Δ⁻³; T=0 friction Δ⁻¹; finite-T friction none.
- (7.5): iη regularisation gives a retarded response, not a tangent vector; peak at Δ = η/√3.

## G. Refraction (Section 8)
- Prop 8.1 (8.1): √g∥ sin θ = const, i.e. g∥ sin²θ = const. Index n = √g∥, NOT λ_min.
- Prop 8.2: ‖Π₁ − Π₂‖²_HS = 2Σ sin²ϑ_i; the index is the subspace rotation rate.
- Prop 8.3: turning point at g∥ = C; a stratum with g∥ → 0 is repulsive.
- Remark 8.4 (8.2): Γ_ij,k = ½(G_ik,j + G_jk,i − G_ij,k); the bending force is the metric dipole.
- Lemma 8.5: g∥ ≡ 0 on a stratum iff Π is constant along it (polar stratum = one projector).
- Prop 8.6 (8.3): at a silent direction, first moving order m: d(ε) = |ε|^m/m! · √g(∂^mΠ,∂^mΠ). Even m = fold (two sheets meet); odd m = parametrisation artefact.
- Remark 8.7: at a fold the degenerate metric does not determine geodesics; a kernel direction must be supplied.
- Example 8.8: three bodies, Π = ψψ*/|ψ|², shape sphere; distances see w₁,w₂ not sign of w₃; collinear circle is a fold.
- 8.6: narrowing gap raises the index and GUIDES; g∥ = 9/(4(1+6.25y²)) example.

## H. Mixed states (Section 9)
- (9.1)-(9.3): V = ½(L_Vρ + ρL_V); Q_ρ = ¼Tr(ρL_VL_W); g_ρ = Bures; Ω_ρ = mean Uhlmann curvature. Reduces exactly at ρ = Π (k=1), factor 1/k for Π/k.

## I. Data standard and the gap law (Sections 10, 12)
- Three levels: raw angle, geometric angle (10.1), interpretation. (10.2): |Ω| ≤ 2√(C(V)C(W)) sin θ_G.
- (10.3): δθ ≈ √(λ₁λ₂)/((λ₁−λ₂)√N).
- Prop 10.1 (10.4): (Q'A'Q')(Q'P) − (Q'P)(PAP) = Q'EP. (10.5): ‖sin Θ‖ ≤ ‖Q'EP‖/δ.
- (10.6): tan 2θ = 2g/Δ — an eigenvector angle is a coupling-to-gap ratio; 90° turn inside a window of width ~g.
- (12.1): tail held by Δ_out, tip by δ_in. Remark 12.1: locking at |Δω| ≤ 2K, mixing angle 22.5° at threshold.
- (12.2): d_H(U,V) = (1/n)‖P_U − P_V‖² = (2/n)Σ sin²θ_j, with sin²θ_j = sin²(φ_j/2) over eigenphases φ_j of U*V.
- (12.3): 𝓛 = (Σθ_j²)^{1/2}. Prop 12.3: upper bound met iff U*V is an involution.
- Example 12.4: doubling on Z/9, angles 30,30,60,60,90,90; count 4; length 2.7706.

## J. Two-band and spin-j (Appendices B, C)
- (B.1): g = δ₁d⊥·δ₂d⊥/(4|d|²), Ω = d·(δ₁d×δ₂d)/(2|d|³). (B.3): g_θθ = ¼, g_φφ = ¼sin²θ, Ω_θφ = ½sin θ, Chern 1.
- Two-band saturation is forced (X, Y are numbers).
- (C.1): g_Π₁ = g_Π₂ = |δd⊥|²/(2|d|²); g_Π = g_{I−Π} always. Spin-j lowest band: g = (j/2)h, |Ω_θφ| = j sin θ, Chern 2j (Veronese / lowest Landau level).

## K. Leads this read raises for the vacuum-disk work — ALL UNTESTED
1. (12.2) turns an eigenphase into a principal angle, θ = φ/2. For a meridian with eigenphases ±2πα the graph-projector angle is πα, so an arc end step k sits at θ = πk/(2pq). The "count" reads sin²θ and the intrinsic length reads θ². Whether the carried-over direction −k²/(pq) is the θ² reading of the step is untested.
2. Section 7.2's α(x) = Σ 2Δ³g/(Δ² − x²) and VOTKP 5.3's Σ(z) = B(z−D)⁻¹C are both one-pole-per-hidden-level forms. For a Hermitian hidden level the residue has a fixed sign. Whether g in z(a) = κ − g/(a−d) has that sign is untested and would separate "hidden level" from "just a Möbius map".
3. Prop 8.6 (first moving order, even = fold) and Remark 8.7 (a fold needs a supplied kernel direction) are the IQGT statements closest to "direction" at a degenerate end point. Untested against the arc ends.
4. Example 6.5: projector returns, phase does not. This is the IQGT form of "the direction is kept only in the phase". Untested against the torus arcs.

# "Universal Projector Geometry" (UPG) — upg_final_v3_2.pdf (FULL READ)

Author: Jeromie Beasley. Dated Sept 2026, 32 pp. Source: Drive fileId 1Tsps6NmIgF9XNBOImfr0Cjk40pdIvJq9, read as Drive text through the last page including Appendix B. Nothing truncated. The PDF has no verbatim output blocks, only scripts (so numbers below are as stated in the prose/tables, not re-run).

## Grades (his, Sec 0)
[T] exact/proved, [V] verified numerically, [C] cited, [D] data-reported, [H] hypothesis. Quote: grades are "never silently promoted. Where a chain mixes grades, the weakest link is named."

## Sec 1 Redistribution operator
- Def 1.1: structural transition generator Ω. F(Ω,Π) = (I−Π)ΩΠ + ΠΩ(I−Π) = ΩΠ + ΠΩ − 2ΠΩΠ = [Ω,Π]Π + Π[Π,Ω].
- Thm 1.2 [T]+[V]: equivalent forms; F traceless and block off-diagonal.
- Thm 1.3 [T]+[V]: F = 0 iff [Ω,Π] = 0. Cor 1.4: T(Ω,Π) = ||F||_F.
- Gate: 200 random trials, 9e-16.
- Prop 1.5 [T]+[V]: H = [[A,B],[B†,D]], K(t) = B e^{−itD} B†, K(0) = BB†, T² = ||F||² = ||[H,Π]||² = 2 Tr K(0).
- Lean: 40 theorems; complex case checked to 6e-14 over 500 blocks.
- Hypothesis 1 (hysteresis), Hypothesis 2 (correlation with T): [H].

## Sec 2 Dirac foundation
- Three integers: index, asymmetry, winding.
- Two-band metric–curvature equality for the Dirac class [T].
- Kagome three-band example at bond phase π/6.
- Graphene ladder E_n = vF sqrt(2ħeBn), vF = 1.10e6 m/s, E1(10 T) = 126 meV.
- Chiral ledger Z/M = (1/2)∫ρ ln(1+λ²); half-Cauchy Z/M = ln(1+a), a* = e^{π²/12} − 1 = 1.276108; chiral Gaussian a* = 2.665.

## Sec 3 Admissible bulk: five conditions (as listed in the paper).

## Sec 4
- Thm 4.1 phase transport law: dΦ/dt = ((m+α)β̇ − (n+β)α̇)/((m+α)²+(n+β)²); integer windings to 1e-6.
- Thm 4.2 persistence of the global bound: O(γ) > 2aϵ; O_min = (16/15)a⁵ + 2aϵ; gate 1.086667 = 16/15 + 0.02, falling to 0.0268.
- Thm 4.3 interface anomaly: Δ_interface = Tr log(I − ϵ†(I+R_A)⁻¹ϵ(I+R_B)⁻¹) ≤ 0; 273 seams to 3e-13; skew control gives the opposite sign on all 400 draws.
- Def 4.4 noncommutative anchor: R = UVU†V†, δ = ||R−I||²_F/d, g = min|λ_j+1|, w = (1/2π)Σ arg λ_j.
- Thm 4.5 integrality and invariance. Thm 4.6 δ + g² ≤ 4. Cor 4.7. Thm 4.8 |w| ≤ (d/4)√δ, so w ≠ 0 ⇒ δ ≥ 16/d².
- Prop 4.9 clock-shift: δ = 4 sin²(π/d), g = 2 cos(π/d), w = 1; constant sharp, ratio 0.841 at d=5, 0.985 at d=65.
- Gate: w = 1.000000000 at d = 3,5,7,11,17,31,53,97, with δ falling 3.000 to 4.194e-3.
- Scope: operator-norm obstruction, not Hamming or Hilbert–Schmidt. Exel–Loring = Bott index; normalisation to the loop integral is [H].

## Sec 5 Knot-complement realization
- A-polynomial of 4_1: L²M⁴ + L(−M⁸ + M⁶ + 2M⁴ + M² − 1) + M⁴ = 0.
- Cor 5.1 chirality forcing [T] (symmetric start stays put; ±1e-6 seeds run to ±0.9946).
- Def 5.2 minimality; Thm 5.4 lattice split [T] (trichotomy selection at [H]).
- Stress candidates Φ(C) = (1/2)||[C,Cᵀ]||² and S_ij = ∂iρ∂jρ + Δ²g_ij + χη∂iη∂jη.
- Thm 5.5 realization by knot complements, Lemmas 5.6, 5.7.

## Sec 6 Module III: THE INTRINSIC METRIC ON THE PROJECTOR BUNDLE
- Data: Uusnäkki transmon engine, 3 cycles × 6 strokes × 29 amplitudes × 9949 shots. Principal angles at k=4: 32.33°, 23.29°, 13.22°, 4.72° [D].
- Capacity C(V) = g = (1/2)Tr V². Ω = +i Tr(Π[V,W]). Tr(Π V†W) = g − (i/2)Ω. Sign fixed so the calibrated lower band gives Chern −1.
- Rigidity R_η = 1/(σ_min² + η). Declared transport operator A(H) = TH + HT − 2Tr(TH)G with T = G⁻¹ vs congruence form left open; no rigidity value reported.
- Persistence P = Tr(ΠΠ') = Σcos²θ_i; IPR ≈ 0.1251.
- Thm 6.1 [T]+[V]: |Ω| ≤ 2 sqrt(g_VV g_WW − g_VW²) = 2 sqrt(C(V)C(W)) sin θ_G; 1000 trials, 0 violations.
- Prop 6.2 refraction: R1(E−V1) sin²θ1 = R2(E−V2) sin²θ2, critical angle arcsin sqrt(R2/R1); Euler–Lagrange flow reproduces to 1e-11; Clairaut n = sqrt(g_∥) [T]; rigidity-as-optical-index [H].
- 6.4 refraction independence protocol: reported θ_ref = 14.22° against window [14.21°, 14.23°] is graded [D] pending the odd/even split protocol.
- 6.5 Yi et al. Raman-lattice band (t0=0.09, tso=−0.05, δ=−0.2): winding currency gives Chern −0.99931 vs published −1.00 ± 0.02; saturation grid mean 0.99996; vol_g = 1.145 > |C|; rigidity sweeps 1.0e2 at δ=−0.4 to 4.0e6 at δ=−0.719 (η=1e-12), with η=1e-4 cap of 1e4.
- 6.6 collapse of d_eff to 1. 6.7 friction shield T_anti ~ 1e-4 giving 1e-8 [D+H]. Protocol 1 weak-value [H] (conjectural). 6.9 literature convergence.

## Sec 7 Khovanov spectral complex
D_Kh = d + d*, D² = Δ; harmonic sector [T]; the alignment is [H].

## Sec 8
Thm 8.1 Lipschitz persistence [T]: ||Π'−Π|| ≤ K_Γ ε, K_Γ = ℓ(Γ)C_Γ²/(2πδ(δ−εC_Γ)); 50 matrices, ≤ 0.16 K_Γ ε; non-normal Riesz projectors are oblique.

## Sec 9 conclusion; App A canonical generator.
## App B scripts
UPG-GATE-01..05, UPG-PROVE-01a/02B, DIRAC-SPINE-01; B.8 Lean modules: UPGFeedback 5, UPGBlockFeedback 7, UPGProjectorMetric 7, UPGProjectorDynamics 3, UPGResolventFeedback 3, UPGPositiveFeedback 3, UPGInterfacePersistence 6, UPGInterfaceSpectrum 6 (total 40); Lean 4 v4.33.0; repo github.com/dicipler-pixel/upg-lean commit 9a9604a.

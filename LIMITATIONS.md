# Limitations

This repository proves the exact, finite parts of *VOTKP* v1.1. Lean proves exactly the
statements written, under exactly the hypotheses written.

**Not formalized.**

- Every computation on data: the peel runs on NIST ionization energies, the film tests on
  tabulated optical constants, the gold metamer, the knot censuses (HOMFLY, Jones, coloured
  Jones, Khovanov, knot Floer, signature function), the A-polynomial volumes, the nuclear and
  particle rounds, and the test ledger of Appendix D. These are the paper's [Exact] results,
  computed by the scripts in its package; Lean checks none of them.
- 5.6 is proved per channel in `Peel` and in matrix form in `Channels` for real symmetric forms
  `Kₘ`; complex Hermitian forms are not stated.
- 6.2's "surviving matches" equivalences and the oblique-incidence statements.
- The hyperbolic-disk reading of Corollary 15.2 is proved as the identity
  `(1 + Γ)/(1 − Γ) = z`; the Poincaré metric itself is not formalized.
- Theorem 8.2 is an exact split of the hydrogenic form `IE = Ry Z²/n²`, with `Z` the effective
  charge that this form defines. The wall values `3/5, 5/13, …, 13/85` are those of the shell
  part `tanh(−Δ ln n)` alone, the Smith reflection of the ratio `(n/(n − 1))²`. They are not
  the measured reflection of a step across a real shell wall, which also includes the screening
  part `tanh(Δ ln Z)`.
- The film reflection `r = (Γ + x)/(1 + Γx)` (the normal-incidence Airy form) is the model, not
  derived, so `film_is_oplus` holds by definition. Theorem 6.2's rise-or-fall criterion is
  proved in two steps that are not combined into one statement: `echo_circle` (the identity,
  with `A = 1 − |a|⁴` and `C = ā(1 − a²)`) and `circle_criterion` (for arbitrary `A > 0` and
  `C`). `interface_smith` and `stack_telescopes` are proved for real positive indices.
- Of 5.9 (the reduced-record impossibility bound), Lean proves the witness: the closed form, the
  shared records `T(0) = T(√2) = 1/2`, the later outcomes and their gap. No statement about
  predictors or a worst-case error bound is formalized.

**Stated with explicit hypotheses.** `⊕`-associativity assumes the two inner denominators are
nonzero. The film identities assume `1 + Γx ≠ 0`, and the echo series `‖Γx‖ < 1`. The
reduced-product associator holds for any additive map `P`, not only a projector.

## Energy-ledger extension

VOTKP/Energy.lean proves finite real-arithmetic identities conditional on supplied thresholds. Data completeness and arithmetic checks do not turn mixed evaluated/semi-empirical/theoretical inputs into wholly experimental data. Wavefunctions, excitation strengths, kinetics, isotope-resolved masses and feedback dynamics are not reconstructed by the threshold ledger. Section 21 separates these proposed extensions from the proved ledger.

## Version 2.2 additions: how each result is stated

- **Theorem 3.1** reads futures along the discrete evolution `v ↦ Lv`: identical futures means
  `R(Lᵏv) = R(Lᵏw)` for every `k`. For the flow `e^{tL}` these are its Taylor coefficients; that
  analytic step (Appendix A.1) is not formalized.
- **Theorem 4.1** pins the curvature by an explicit two-sided bound
  `|U(a) − U(0) − μ_eff a²/2| ≤ (|λ|/4 + |1 − 2r| c⁴/8δ³) a⁴`. The metric is computed from the
  slope of the Bloch direction; the ground projector itself is not built as a matrix.
- **5.4** assumes `x` and `y` are differentiable solutions of the coupled system on all of `ℝ`,
  with complete normed state spaces. Existence of solutions is not proved.
- **5.5** states silence without inverses: at every `z` with `χ_D(z) ≠ 0`, every solution of
  `(zI − D)y = Ce` has `By = 0`. The sharpness example is checked over `ℤ` by `decide`.
- **Theorem 6.3** is proved as first-order agreement: the exact characteristic-matrix
  reflection and the shunt law have the same value and the same derivative at `d = 0`, and
  their difference is `O(d²)` as the real thickness `d → 0`. The whole-`N²` sheet comparison is
  not formalized.
- **Proposition 11.1**: the determinant factorization and the parity statement are proved. The
  parity theorem takes as a hypothesis that `det H(t) = (t − t₀)^m g(t)` with `g` of one sign
  on the two sides; deriving that from the root multiplicity of the Alexander polynomial, and
  the exact `±2` jump at a simple root (which uses Rellich's analytic eigenvalue branches),
  are not formalized. Mathlib provides no analytic perturbation theory for eigenvalues (Rellich,
  Kato), so the `±2` jump is not stated in Lean.
- **Theorem 15.4** is proved as the pointwise intertwining `H_λ ψ(λ·) = λ(Hψ)(λ·)` for `C²`
  wavefunctions, with the kinetic operator written as second directional derivatives along a
  chosen family of coordinate directions. The dilation `(U_λ f)(x) = λ^{n/2} f(λx)` is proved to
  preserve every `∫ conj f · g` against an additive Haar measure and to be inverted by
  `U_{1/λ}`; operator domains are not formalized.
- **Proposition 19.3** uses the explicit three-level family of §19.4. The ground state is
  shown by an explicit unit vector annihilated by `H_b`, and the metric
  `½ Tr((∂P)²) = b²` is computed entrywise.
- **Proposition 19.4** takes the leading excess-work density bound `ζ ≥ w* h ρ̇²` as a
  hypothesis (it is IQGT's spectral weighting; the finite-sum step is `spectral_weighting`).
  The slow-driving expansion, the bath model and the RP-WEIGHT/RP-POLAR numerics are not
  formalized.
- **§20.3** is proved for finite matrices: the retained-resolvent identity needs `z − D` and
  the Schur complement invertible, and contour selection takes a finite channel sum
  `Σₖ Wₖ/(z − eₖ)` and a circle avoiding every `eₖ`; continua are not formalized.
- **§20.5** is proved on the one-excitation basis `{|10⟩, |01⟩}` with the state written as
  `(1, e^{iφ})` of squared norm `2`; the equality of the two local reductions `I/2` is computed in
  the paper, not in Lean. The signed offset is stated through the determinant ratio; entropies
  are not formalized.
- **§8.7's in-shell stagger** is a computation on the archived ladders, not a Lean statement.

# Limitations

This repository proves the exact, finite parts of *VOTKP* v1.1. Lean proves exactly the
statements written, under exactly the hypotheses written.

**Not formalized.**

- Every computation on data: the peel runs on NIST ionization energies, the film tests on
  tabulated optical constants, the gold metamer, the knot censuses (HOMFLY, Jones, coloured
  Jones, Khovanov, knot Floer, signature function), the A-polynomial volumes, the nuclear and
  particle rounds, and the test ledger of Appendix D. These are the paper's [Exact] results,
  computed by the scripts in its package; Lean checks none of them.
- Theorem 3.1 (finite linear predictive quotient) and Theorem 4.1 (occupation sets a response
  curvature).
- 5.4 (memory kernel), 5.5 (transfer silence), and the matrix form of 5.6. The four-reading
  certificate is proved per channel: the coefficient formula and its sign on each side of a pole.
- 6.2's "surviving matches" equivalences, Theorem 6.3 (the thin end as a shunt admittance), and
  the oblique-incidence statements.
- Theorem 15.4 is proved only in its ratio form; the unitary equivalence `H_λ ≅ λH` is not.
- The hyperbolic-disk reading of Corollary 15.2 is proved as the identity
  `(1 + Γ)/(1 − Γ) = z`; the Poincaré metric itself is not formalized.
- Of Proposition 11.1, only the unit-circle identity of Appendix A.12 is proved.
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

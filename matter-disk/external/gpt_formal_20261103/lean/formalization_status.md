# Machine-checked scope — Matter, Gases and VOTKP

Status: **34 positive theorem declarations compile under Lean 4.34.1 and pinned Mathlib; five intentionally false controls are rejected.** The final executable verification record is `logs/verification.json`. Exact theorem statements are in `theorem_manifest.json`, and Lean's own elaborated types plus each declaration's axiom dependencies are printed in `logs/axioms.log`.

This is a formalization of a defined mathematical core. It does not certify every statement of the manuscript, the physical applicability of a model, empirical data, scientific novelty, or priority. No original VOTKP historical Lean suite is claimed to have been rebuilt here.

## Checked mathematical content

| Source module | Exact coverage | Manuscript relationship |
|---|---|---|
| `MatterGas/Boundary.lean` | Complex finite-matrix block defect identity; positive defect for a positive contraction; positive restricted defect and cross block product; `0 ≤ BB* ≤ A−A² ≤ I/4`; pure-projector reduction; disconnected zero; trace zero iff cross block zero | Full algebra/positivity core of B1–B2, algebraic part of B4, zero criterion in B5. Singular-value identification, ordered spectral comparisons and Gaussian interpretation remain manuscript proofs. |
| `MatterGas/Scalar.lean` | Cayley ratio scale invariance, strict bounds, inverse and anchored reconstruction; scalar covariance factorization, threshold equivalence and quarter bound; finite nonnegative-list threshold-count bound; disconnected scalar witness | Scalar ingredients of G1, B4–B5. The list bound is not presented as a standalone formalization of the matrix spectral theorem. |
| `MatterGas/Saha.lean` | Positive three-charge mean denominator; strict decrease of mean charge with electron density; uniqueness among positive neutral solutions; `0 < meanCharge < 2`; two population-ratio cancellation identities | Three-charge specialization of the uniqueness argument, plus the exact rational algebra of the §8 gas-peeling inverse. General finite-Z existence, derivative/variance identities and LTE physics remain manuscript arguments. |
| `MatterGas/Witness.lean` | A finite-difference vector annihilates every quadratic polynomial; two explicit positive distributions on velocities `(-3,-1,1,3)` share moments 0, 1, 2 and differ in moment 3 by `3/2` | Exact finite witness used in M1–M2. It does not prove the general order-p finite-difference theorem or a transport dynamics model. |
| Additional declarations in `Boundary.lean` | `1−4ν(1−ν)=(1−2ν)²` over complex numbers; every square matrix A embeds into idempotent `[[A,I],[A−A²,I−A]]` | Algebraic core supporting D1/D3/D5. It does not supply branch-independent spectral counts, positivity of a non-Hermitian idempotent, or the full Cayley branch theorem. |

B3, B6–B13, remaining spectral parts of D1–D7, the collision/dynamical results K1–K4, general-Z gas results, response laws R1–R4 and Petermann statements P1–P2 are **not claimed machine-checked by this package**. Their manuscript proof and test status must be reported separately.

## Trust and negative controls

Positive sources contain no `sorry`, `admit`, custom `axiom`, or `native_decide`. The verifier scans those sources, builds the package, requests `#print axioms` for every manifest declaration, checks exact coverage and rejects dependencies outside `propext`, `Classical.choice`, and `Quot.sound`. These are standard Lean/Mathlib foundational axioms, not additional physical assumptions.

The five false-control files must fail with an **unsolved mathematical goal**. A missing import or toolchain error does not count as a passing control. The rejected alterations claim that a common scale changes the Cayley ratio, disconnected thermal variance is zero, the maximum covariance defect is at most 1/5, the equal first three moments determine the third, or mean charge increases with electron density. The last control is stated at explicit exact positive parameters.

The ordinary build intentionally excludes `FalseControls/`. Its files are only run separately by the verifier, where failure is required. Positive definitions and all 34 theorem statements remain inspectable, rather than hidden behind an opaque numerical-success flag.

## Pinned environment and runtime note

- Lean: `leanprover/lean4:v4.34.1`, official commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib: tag `v4.34.1`, exact commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- Transitive dependency revisions: `lake-manifest.json`.
- Host: Linux, official release binaries and official Mathlib cache.

This execution container permits `/proc/self/exe` but does not resolve `/proc/<the same process's numeric PID>/exe` for Lean's path lookup. The documented optional `tools/self_exe_compat.c` redirects only that exact own-process alias to `/proc/self/exe`. It does not change Lean's kernel, axioms, tactic code or theorem statements, and it does not redirect another process's path. The verification JSON records whether this compatibility shim was present. Standard environments should run without it.

The toolchain binaries, cache, temporary setup attempts and build artifacts are not part of the distributable source package. A fresh standard environment must obtain the pinned public dependencies once, then run the provided verifier.

/-
# VOTKP: the main results, stated

This file is the one a reader has to trust. It imports only Mathlib, defines every notion it
uses, and states the headline results of *VOTKP* (Jeromie Beasley). It contains no proofs.

`Showcase_WithProofs.lean` proves `MainTheorem` from the library in `VOTKP/`. Lean accepts that
proof only if its statement is this `MainTheorem`, so the library cannot be proving something
weaker than what is written here. The continuous-integration check confirms it on every push
(`scripts/verify.py`), and a false control shows that an altered statement is rejected.
-/
import Mathlib

namespace Showcase

/-! ## Notions used in the statements -/

/-- Einstein's addition law `u ⊕ v = (u + v)/(1 + uv)`. -/
noncomputable def oplus (u v : ℝ) : ℝ := (u + v) / (1 + u * v)

/-- The centre `x_c = −C̄/A` of the film's decision circle, in coordinates. -/
noncomputable def circleCentre (A : ℝ) (C : ℂ) : ℂ := ⟨-C.re / A, C.im / A⟩

/-- Power sums `p_k = a^k + b^k + c^k` of three channel transmissions. -/
def pw (k : ℕ) (a b c : ℝ) : ℝ := a ^ k + b ^ k + c ^ k

/-- Transmission through the first site when the second is hidden, for `s = ±1`. -/
noncomputable def transmission (s x : ℝ) : ℝ := (x - s) ^ 2 / (x ^ 4 - 2 * s * x ^ 3 + 2)

/-- The delay-`τ` rise pattern of a list: `true` where `x i < x (i+τ)`. -/
def rises (τ : Nat) (xs : List Nat) : List Bool :=
  (List.range (xs.length - τ)).map fun i => decide (xs.getD i 0 < xs.getD (i + τ) 0)

/-- Zero normalized permutation entropy at dimension 2: one ordinal pattern throughout. -/
def singlePattern (τ : Nat) (xs : List Nat) : Bool :=
  (rises τ xs).all id || (rises τ xs).all not

/-- The clean ladder, and the same ladder with one adjacent transposition. -/
def clean : List Nat := [1, 2, 3, 4, 5, 6]
def swapped : List Nat := [1, 2, 4, 3, 5, 6]

/-! ## The statements -/

/-- **Theorem 8.1.** A ratio `z > 0` sits on the reflection chart at `tanh(½ ln z)`. -/
abbrev SmithIdentity : Prop :=
  ∀ z : ℝ, 0 < z → (z - 1) / (z + 1) = Real.tanh (Real.log z / 2)

/-- **Theorem 15.1.** Peel steps add like velocities: the reflection of the block from `k` to
`k + m + 1` is the reflection of the block to `k + m`, `⊕` the reflection of the next step. -/
abbrev BlocksAddLikeVelocities : Prop :=
  ∀ IE : ℕ → ℝ, (∀ j, 0 < IE j) → ∀ k m : ℕ,
    Real.tanh (Real.log (IE (k + (m + 1)) / IE k) / 2) =
      oplus (Real.tanh (Real.log (IE (k + m) / IE k) / 2))
        (Real.tanh (Real.log (IE (k + m + 1) / IE (k + m)) / 2))

/-- **Order drops out.** The ladders `1, 2, 6` and `1, 3, 6` have different first steps and the
same composite `5/7`. -/
abbrev OrderDropsOut : Prop :=
  oplus ((2 - 1) / (2 + 1)) ((3 - 1) / (3 + 1)) = (6 - 1) / (6 + 1) ∧
    oplus ((3 - 1) / (3 + 1)) ((2 - 1) / (2 + 1)) = (6 - 1) / (6 + 1) ∧
    ((2 - 1) / (2 + 1) : ℝ) ≠ (3 - 1) / (3 + 1)

/-- **Theorem 8.2, the shell wall.** At a shell wall the reflection is `(2n − 1)/(n² + (n − 1)²)`,
the odd leg over the hypotenuse of a Pythagorean triple. -/
abbrev ShellWall : Prop :=
  (∀ n : ℝ, 1 < n →
      ((n / (n - 1)) ^ 2 - 1) / ((n / (n - 1)) ^ 2 + 1) = (2 * n - 1) / (n ^ 2 + (n - 1) ^ 2)) ∧
    ∀ n : ℤ, (2 * n - 1) ^ 2 + (2 * n * (n - 1)) ^ 2 = (n ^ 2 + (n - 1) ^ 2) ^ 2

/-- **Theorem 6.2.** For a film with bulk reflection `a` and echo `x`,
`|r|² − |a|² = ((1 − |a|⁴)|x|² + 2 Re[ā(1 − a²)x]) / |1 + ax|²`. -/
abbrev EchoIdentity : Prop :=
  ∀ a x : ℂ, 1 + a * x ≠ 0 →
    Complex.normSq ((a + x) / (1 + a * x)) - Complex.normSq a =
      ((1 - Complex.normSq a ^ 2) * Complex.normSq x + 2 * ((starRingEnd ℂ) a * (1 - a * a) * x).re) /
        Complex.normSq (1 + a * x)

/-- **Theorem 6.2, the criterion.** With `A > 0`, the film reflects more than its bulk exactly
when the echo lies outside one circle, and that circle passes through the origin. -/
abbrev EchoCircle : Prop :=
  (∀ A : ℝ, 0 < A → ∀ C x : ℂ,
      0 < A * Complex.normSq x + 2 * (C * x).re ↔
        Complex.normSq (circleCentre A C) < Complex.normSq (x - circleCentre A C)) ∧
    ∀ (A : ℝ) (C : ℂ), Complex.normSq (0 - circleCentre A C) = Complex.normSq (circleCentre A C)

/-- **One radius cannot decide.** With `a = 1/2`, the echo `x = 1/5` raises the reflectance to
`49/121` and `x = −1/5` lowers it to `1/9`, against the bulk `1/4`. -/
abbrev OneRadiusCannotDecide : Prop :=
  ((1 / 2 + 1 / 5) / (1 + 1 / 2 * (1 / 5)) : ℝ) ^ 2 = 49 / 121 ∧ (1 / 2 : ℝ) ^ 2 < 49 / 121 ∧
    ((1 / 2 - 1 / 5) / (1 - 1 / 2 * (1 / 5)) : ℝ) ^ 2 = 1 / 9 ∧ (1 / 9 : ℝ) < (1 / 2) ^ 2

/-- **Section 15.2.** At zero phase a stack telescopes: `r₀₁ ⊕ r₁₂ = r₀₂`. -/
abbrev StackTelescopes : Prop :=
  ∀ N0 N1 N2 : ℝ, 0 < N0 → 0 < N1 → 0 < N2 →
    oplus ((N0 - N1) / (N0 + N1)) ((N1 - N2) / (N1 + N2)) = (N0 - N2) / (N0 + N2)

/-- **Section 5.8.** Conductance and Fano factor do not fix the channels: `{1/5, 1/2, 4/5}` and
`{3/10, (6 + √6)/10, (6 − √6)/10}` share `c₁ = 3/2` and `c₂ = 57/100`, but `c₃` is `0`
against `3/50`. -/
abbrev CumulantWitness : Prop :=
  pw 1 (1 / 5) (1 / 2) (4 / 5) = 3 / 2 ∧
    pw 1 (3 / 10) ((6 + Real.sqrt 6) / 10) ((6 - Real.sqrt 6) / 10) = 3 / 2 ∧
    pw 1 (1 / 5) (1 / 2) (4 / 5) - pw 2 (1 / 5) (1 / 2) (4 / 5) = 57 / 100 ∧
    pw 1 (3 / 10) ((6 + Real.sqrt 6) / 10) ((6 - Real.sqrt 6) / 10) -
      pw 2 (3 / 10) ((6 + Real.sqrt 6) / 10) ((6 - Real.sqrt 6) / 10) = 57 / 100 ∧
    pw 1 (1 / 5) (1 / 2) (4 / 5) - 3 * pw 2 (1 / 5) (1 / 2) (4 / 5) +
      2 * pw 3 (1 / 5) (1 / 2) (4 / 5) = 0 ∧
    pw 1 (3 / 10) ((6 + Real.sqrt 6) / 10) ((6 - Real.sqrt 6) / 10) -
      3 * pw 2 (3 / 10) ((6 + Real.sqrt 6) / 10) ((6 - Real.sqrt 6) / 10) +
      2 * pw 3 (3 / 10) ((6 + Real.sqrt 6) / 10) ((6 - Real.sqrt 6) / 10) = 3 / 50

/-- **Section 5.9.** A reduced record cannot fix the future: both hidden states give
`T(0) = T(√2) = 1/2`, yet at `x = 1` they transmit `0` and `4/5`. -/
abbrev ReducedRecord : Prop :=
  (transmission 1 0 = 1 / 2 ∧ transmission (-1) 0 = 1 / 2 ∧
      transmission 1 (Real.sqrt 2) = 1 / 2 ∧ transmission (-1) (Real.sqrt 2) = 1 / 2) ∧
    (transmission 1 1 = 0 ∧ transmission (-1) 1 = 4 / 5 ∧
      transmission (-1) (1 / 10) - transmission 1 (1 / 10) = 79600000 / 400039601)

/-- **Appendix A.12.** On the unit circle, `(1 − ω)/(1 − ω̄) = −ω` for `ω ≠ 1`. -/
abbrev UnitCircleRatio : Prop :=
  ∀ ω : ℂ, Complex.normSq ω = 1 → ω ≠ 1 → (1 - ω) / (1 - (starRingEnd ℂ) ω) = -ω

/-- **Control 41.** Zero permutation entropy at delay 2 holds for both the clean ladder and the
transposed one, so it does not identify the defect; delay 1 does. -/
abbrev ZeroEntropyNotIdentifying : Prop :=
  singlePattern 2 clean = true ∧ singlePattern 2 swapped = true ∧ swapped ≠ clean ∧
    singlePattern 1 swapped = false

/-- **The main theorem of the showcase:** all of the above. -/
abbrev MainTheorem : Prop :=
  SmithIdentity ∧ BlocksAddLikeVelocities ∧ OrderDropsOut ∧ ShellWall ∧ EchoIdentity ∧
    EchoCircle ∧ OneRadiusCannotDecide ∧ StackTelescopes ∧ CumulantWitness ∧ ReducedRecord ∧
    UnitCircleRatio ∧ ZeroEntropyNotIdentifying

end Showcase

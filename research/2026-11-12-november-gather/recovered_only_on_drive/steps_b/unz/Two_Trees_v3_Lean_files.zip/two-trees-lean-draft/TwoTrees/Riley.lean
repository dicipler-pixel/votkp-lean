/-
Two Trees in One Ball (Jeromie Beasley). The knot's tree with Mathlib's matrices (§6).

The Riley meridians of a 2-bridge knot are `a = !![s, 1; 0, s⁻¹]` and `b = !![s, 0; -v, s⁻¹]`.
Multiplying each by `s` makes every entry a polynomial, so the statements below hold over every
commutative ring:

  `A = s·a = !![s², s; 0, 1]`, `B = s·b = !![s², 0; −vs, 1]`,
  `A' = s·a⁻¹ = !![1, −s; 0, s²]`, `B' = s·b⁻¹ = !![1, 0; vs, s²]`.

* `merA_mul_merAi`, `merB_mul_merBi`: `A A' = B B' = s²·I`.
* `merA_det` … `merB_discr`, `meridian_discr`: determinant `s²`, trace `s² + 1`, discriminant `(s² − 1)²`
  (Theorem 6.1: each meridian is a boost of translation length `2 ln |s|`).
* `merA_isHyperbolic`, `merB_isHyperbolic`, `meridian_isHyperbolic`: for real `s` with `s² ≠ 1`
  the meridians are hyperbolic in Mathlib's sense (`Matrix.IsHyperbolic`: discriminant `> 0`).
* `trefoil_relation`, `figure_eight_relation` (Theorem 6.2): `A W − W B` is the Riley polynomial
  times a fixed matrix, so the knot relation holds exactly on the Riley curve.
* `trefoil_longitude` (Theorem 6.4): on the trefoil's curve the scaled longitude is upper
  triangular with diagonal `−s²`, `−s¹⁴`.
-/
import Mathlib

namespace TwoTrees.Riley

variable {R : Type*} [CommRing R]

/-- `s` times the Riley meridian `a = !![s, 1; 0, s⁻¹]`. -/
def merA (s : R) : Matrix (Fin 2) (Fin 2) R := !![s * s, s; 0, 1]

/-- `s` times the Riley meridian `b = !![s, 0; -v, s⁻¹]`. -/
def merB (s v : R) : Matrix (Fin 2) (Fin 2) R := !![s * s, 0; -(v * s), 1]

/-- `s` times `a⁻¹`. -/
def merAi (s : R) : Matrix (Fin 2) (Fin 2) R := !![1, -s; 0, s * s]

/-- `s` times `b⁻¹`. -/
def merBi (s v : R) : Matrix (Fin 2) (Fin 2) R := !![1, 0; v * s, s * s]

/-- The scaled trefoil longitude `B A A B A'⁴ = s⁸ · (b a a b a⁻⁴)`. -/
def trefoilLongitude (s v : R) : Matrix (Fin 2) (Fin 2) R :=
  merB s v * merA s * merA s * merB s v * (merAi s * merAi s * (merAi s * merAi s))

/-! ## Inverses, determinant, trace, discriminant -/

/-- `A A' = s² I`. -/
theorem merA_mul_merAi (s : R) : merA s * merAi s = !![s * s, 0; 0, s * s] := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals first
    | (simp [merA, merAi, Matrix.mul_apply, Fin.sum_univ_two]; done)
    | (simp [merA, merAi, Matrix.mul_apply, Fin.sum_univ_two] <;> ring1)
    | (simp [merA, merAi, Matrix.mul_apply, Fin.sum_univ_two] <;> grind)

/-- `B B' = s² I`. -/
theorem merB_mul_merBi (s v : R) : merB s v * merBi s v = !![s * s, 0; 0, s * s] := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals first
    | (simp [merB, merBi, Matrix.mul_apply, Fin.sum_univ_two]; done)
    | (simp [merB, merBi, Matrix.mul_apply, Fin.sum_univ_two] <;> ring1)
    | (simp [merB, merBi, Matrix.mul_apply, Fin.sum_univ_two] <;> grind)

theorem merA_det (s : R) : (merA s).det = s * s := by
  rw [merA, Matrix.det_fin_two_of]; ring

theorem merB_det (s v : R) : (merB s v).det = s * s := by
  rw [merB, Matrix.det_fin_two_of]; ring

theorem merA_trace (s : R) : (merA s).trace = s * s + 1 := by
  rw [merA, Matrix.trace_fin_two_of]

theorem merB_trace (s v : R) : (merB s v).trace = s * s + 1 := by
  rw [merB, Matrix.trace_fin_two_of]

/-- **Theorem 6.1, scaled.** `trace² − 4 det = (s² − 1)²`. -/
theorem merA_discr (s : R) : (merA s).discr = (s * s - 1) ^ 2 := by
  rw [merA, Matrix.discr_fin_two, Matrix.trace_fin_two_of, Matrix.det_fin_two_of]; ring

theorem merB_discr (s v : R) : (merB s v).discr = (s * s - 1) ^ 2 := by
  rw [merB, Matrix.discr_fin_two, Matrix.trace_fin_two_of, Matrix.det_fin_two_of]; ring

/-! ## Hyperbolic in Mathlib's sense -/

/-- For real `s` with `s² ≠ 1` the scaled meridian `A` is hyperbolic. -/
theorem merA_isHyperbolic (s : ℝ) (hs : s ^ 2 ≠ 1) : (merA s).IsHyperbolic := by
  show (0 : ℝ) < Matrix.discr (merA s)
  rw [merA_discr]
  have hne : s * s - 1 ≠ 0 := by
    intro h
    apply hs
    linear_combination h
  exact lt_of_le_of_ne (sq_nonneg _) (Ne.symm (pow_ne_zero 2 hne))

/-- For real `s` with `s² ≠ 1` the scaled meridian `B` is hyperbolic, for every `v`. -/
theorem merB_isHyperbolic (s v : ℝ) (hs : s ^ 2 ≠ 1) : (merB s v).IsHyperbolic := by
  show (0 : ℝ) < Matrix.discr (merB s v)
  rw [merB_discr]
  have hne : s * s - 1 ≠ 0 := by
    intro h
    apply hs
    linear_combination h
  exact lt_of_le_of_ne (sq_nonneg _) (Ne.symm (pow_ne_zero 2 hne))

/-- The unscaled meridian `!![s, 1; 0, 1/s]` has discriminant `(s − 1/s)²`. -/
theorem meridian_discr (s : ℝ) : Matrix.discr !![s, 1; 0, 1 / s] = (s - 1 / s) ^ 2 := by
  rw [Matrix.discr_fin_two, Matrix.trace_fin_two_of, Matrix.det_fin_two_of]; ring

/-- **Theorem 6.1.** For real `s ≠ 0` with `s² ≠ 1`, the unscaled meridian `!![s, 1; 0, 1/s]` is
hyperbolic: its discriminant is `(s − 1/s)² > 0`. -/
theorem meridian_isHyperbolic (s : ℝ) (hs : s ≠ 0) (hs1 : s ^ 2 ≠ 1) :
    Matrix.IsHyperbolic !![s, 1; 0, 1 / s] := by
  show (0 : ℝ) < Matrix.discr !![s, 1; 0, 1 / s]
  rw [meridian_discr]
  have hinv : s * (1 / s) = 1 := mul_one_div_cancel hs
  have hne : s - 1 / s ≠ 0 := by
    intro h
    apply hs1
    linear_combination s * h + hinv
  exact lt_of_le_of_ne (sq_nonneg _) (Ne.symm (pow_ne_zero 2 hne))

/-! ## The knot relations factor through the Riley polynomial -/

/-- **Theorem 6.2, trefoil** (2-bridge `3/1`, `W = b a`): `A W − W B = R₃ · !![0, s; s v, 0]` with
`R₃ = s⁴ − s² v − s² + 1`. -/
theorem trefoil_relation (s v : R) :
    merA s * (merB s v * merA s) - merB s v * merA s * merB s v =
      !![0, (s * s * s * s - s * s * v - s * s + 1) * s;
        (s * s * s * s - s * s * v - s * s + 1) * (s * v), 0] := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals first
    | (simp [merA, merB, Matrix.mul_apply, Fin.sum_univ_two]; done)
    | (simp [merA, merB, Matrix.mul_apply, Fin.sum_univ_two] <;> ring1)
    | (simp [merA, merB, Matrix.mul_apply, Fin.sum_univ_two] <;> grind)

/-- **Theorem 6.2, figure-eight** (2-bridge `5/3`, `W = b a⁻¹ b⁻¹ a`):
`A W − W B = R₄ · !![0, s³; s³ v, 0]` with `R₄ = s² v² + (3 s² − s⁴ − 1) v + (3 s² − s⁴ − 1)`. -/
theorem figure_eight_relation (s v : R) :
    merA s * (merB s v * merAi s * merBi s v * merA s) -
        merB s v * merAi s * merBi s v * merA s * merB s v =
      !![0, (s * s * v * v + (3 * s * s - s * s * s * s - 1) * v + (3 * s * s - s * s * s * s - 1)) *
          (s * s * s);
        (s * s * v * v + (3 * s * s - s * s * s * s - 1) * v + (3 * s * s - s * s * s * s - 1)) *
          (s * s * s * v), 0] := by
  ext i j
  fin_cases i <;> fin_cases j
  all_goals first
    | (simp [merA, merB, merAi, merBi, Matrix.mul_apply, Fin.sum_univ_two]; done)
    | (simp [merA, merB, merAi, merBi, Matrix.mul_apply, Fin.sum_univ_two] <;> ring1)
    | (simp [merA, merB, merAi, merBi, Matrix.mul_apply, Fin.sum_univ_two] <;> grind)

/-! ## The trefoil longitude -/

/-- Three entries of the scaled trefoil longitude, as polynomials in `s` and `v`. -/
theorem trefoilLongitude_entries (s v : R) :
    trefoilLongitude s v 1 0 = -(s ^ 7 * v) + s ^ 5 * v ^ 2 + s ^ 3 * v ^ 2 - s * v ∧
    trefoilLongitude s v 0 0 = s ^ 8 - s ^ 6 * v - s ^ 4 * v ∧
    trefoilLongitude s v 1 1 = s ^ 14 * v - s ^ 12 * v ^ 2 - 2 * s ^ 10 * v ^ 2 - 2 * s ^ 8 * v ^ 2 +
      2 * s ^ 8 * v + s ^ 8 - 2 * s ^ 6 * v ^ 2 + s ^ 6 * v - s ^ 4 * v ^ 2 + s ^ 4 * v +
      s ^ 2 * v := by
  refine ⟨?_, ?_, ?_⟩
  all_goals first
    | (simp [trefoilLongitude, merA, merB, merAi, Matrix.mul_apply, Fin.sum_univ_two]; done)
    | (simp [trefoilLongitude, merA, merB, merAi, Matrix.mul_apply, Fin.sum_univ_two] <;> ring1)
    | (simp [trefoilLongitude, merA, merB, merAi, Matrix.mul_apply, Fin.sum_univ_two] <;> grind)

/-- **Theorem 6.4.** On the trefoil's Riley curve `R₃ = 0` the scaled longitude `s⁸ L` is upper
triangular with diagonal `−s²`, `−s¹⁴`, so `L` has eigenvalues `−s⁻⁶`, `−s⁶`: a boost of
length `12 ln |s|`. -/
theorem trefoil_longitude (s v : R) (h : s * s * s * s - s * s * v - s * s + 1 = 0) :
    trefoilLongitude s v 1 0 = 0 ∧ trefoilLongitude s v 0 0 = -(s * s) ∧
      trefoilLongitude s v 1 1 = -(s * s * s * s * s * s * s * s * s * s * s * s * s * s) := by
  obtain ⟨h10, h00, h11⟩ := trefoilLongitude_entries s v
  refine ⟨?_, ?_, ?_⟩
  · rw [h10]
    linear_combination (-(s * v * (s ^ 2 + 1))) * h
  · rw [h00]
    linear_combination (s ^ 2 * (s ^ 2 + 1)) * h
  · rw [h11]
    linear_combination (s ^ 2 * (s ^ 2 + 1) * (s ^ 6 * v + s ^ 6 + s ^ 4 * v + s ^ 2 * v + v)) * h

end TwoTrees.Riley

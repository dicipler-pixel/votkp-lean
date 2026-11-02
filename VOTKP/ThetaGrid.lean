import Mathlib.Algebra.Polynomial.Roots
import Mathlib.Tactic

/-!
# Exact rectangular-grid certificates for the theta work

This module proves the completeness of the finite-grid argument.  A bivariate
polynomial is represented by `Polynomial (Polynomial K)`, with outer variable
`x` and coefficient-polynomial variable `y`.  Over an integral domain, more
than `dx` distinct x-values and more than `dy` distinct y-values determine a
polynomial whose separate degrees are at most `dx` and `dy`.

The theta specialization uses the claimed cleared-polynomial degree bounds
`2*n+4` and `2*n+3`.  These bounds remain explicit hypotheses.  This module
does not derive them from the theta formula, implement the PD-to-upright
conversion, or replay any knot's grid cells.  It therefore does not by itself
certify any row of the external knot certificate tables or Conjecture 21.

The false control shows why the earlier three evaluation points cannot replace
a complete degree-bounded grid.
-/

namespace VOTKP.ThetaGrid

open Polynomial

variable {K : Type*} [CommRing K] [IsDomain K]

/-- Evaluate the inner coefficient variable at `y`, then the outer variable at `x`. -/
noncomputable def evalXY (P : Polynomial (Polynomial K)) (x y : K) : K :=
  (P.map (Polynomial.evalRingHom y)).eval x

omit [IsDomain K] in
@[simp]
theorem evalXY_zero (x y : K) : evalXY (0 : Polynomial (Polynomial K)) x y = 0 := by
  simp [evalXY]

/-- A complete rectangular grid is an exact zero certificate.  The finite sets
enforce distinct sample coordinates, rather than merely counting repeated samples. -/
theorem rectangular_grid_zero
    (P : Polynomial (Polynomial K)) (xs ys : Finset K)
    (hx : P.natDegree < xs.card)
    (hy : ∀ i, (P.coeff i).natDegree < ys.card)
    (hgrid : ∀ x ∈ xs, ∀ y ∈ ys, evalXY P x y = 0) : P = 0 := by
  have hrow : ∀ y ∈ ys, P.map (Polynomial.evalRingHom y) = 0 := by
    intro y hy_mem
    apply Polynomial.eq_zero_of_natDegree_lt_card_of_eval_eq_zero' _ xs
    · intro x hx_mem
      exact hgrid x hx_mem y hy_mem
    · exact lt_of_le_of_lt Polynomial.natDegree_map_le hx
  apply Polynomial.ext
  intro i
  rw [Polynomial.coeff_zero]
  apply Polynomial.eq_zero_of_natDegree_lt_card_of_eval_eq_zero' _ ys
  · intro y hy_mem
    have hi := congrArg (fun q : Polynomial K => q.coeff i) (hrow y hy_mem)
    simpa only [Polynomial.coeff_map, Polynomial.coeff_zero,
      Polynomial.coe_evalRingHom] using hi
  · exact hy i

/-- Degree bounds and one more distinct sample in each coordinate suffice. -/
theorem bounded_rectangular_grid_zero
    (P : Polynomial (Polynomial K)) (dx dy : ℕ) (xs ys : Finset K)
    (hx : P.natDegree ≤ dx)
    (hy : ∀ i, (P.coeff i).natDegree ≤ dy)
    (hxs : xs.card = dx + 1) (hys : ys.card = dy + 1)
    (hgrid : ∀ x ∈ xs, ∀ y ∈ ys, evalXY P x y = 0) : P = 0 := by
  apply rectangular_grid_zero P xs ys
  · omega
  · intro i
    have := hy i
    omega
  · exact hgrid

/-- The same complete grid certifies equality of independently constructed
polynomials; it need not be used only to test a stored zero. -/
theorem rectangular_grid_eq
    (P Q : Polynomial (Polynomial K)) (xs ys : Finset K)
    (hx : max P.natDegree Q.natDegree < xs.card)
    (hy : ∀ i, max (P.coeff i).natDegree (Q.coeff i).natDegree < ys.card)
    (hgrid : ∀ x ∈ xs, ∀ y ∈ ys, evalXY P x y = evalXY Q x y) : P = Q := by
  apply sub_eq_zero.mp
  apply rectangular_grid_zero (P - Q) xs ys
  · exact lt_of_le_of_lt (Polynomial.natDegree_sub_le P Q) hx
  · intro i
    rw [Polynomial.coeff_sub]
    exact lt_of_le_of_lt (Polynomial.natDegree_sub_le (P.coeff i) (Q.coeff i)) (hy i)
  · intro x hx_mem y hy_mem
    simpa only [evalXY, Polynomial.map_sub, Polynomial.eval_sub, sub_eq_zero]
      using hgrid x hx_mem y hy_mem

/-- Specialization to the theta report's proposed separate degree bounds.
Both the bounds and every grid evaluation are required proof inputs. -/
theorem theta_grid_zero
    (P : Polynomial (Polynomial K)) (n : ℕ) (xs ys : Finset K)
    (hx : P.natDegree ≤ 2 * n + 4)
    (hy : ∀ i, (P.coeff i).natDegree ≤ 2 * n + 3)
    (hxs : xs.card = 2 * n + 5) (hys : ys.card = 2 * n + 4)
    (hgrid : ∀ x ∈ xs, ∀ y ∈ ys, evalXY P x y = 0) : P = 0 := by
  apply bounded_rectangular_grid_zero P (2 * n + 4) (2 * n + 3) xs ys hx hy
  · omega
  · omega
  · exact hgrid

omit [CommRing K] [IsDomain K] in
/-- The number of distinct Cartesian cells, not the number of repeated evaluations. -/
theorem theta_grid_cell_count
    (n : ℕ) (xs ys : Finset K)
    (hxs : xs.card = 2 * n + 5) (hys : ys.card = 2 * n + 4) :
    (xs ×ˢ ys).card = (2 * n + 5) * (2 * n + 4) := by
  rw [Finset.card_product, hxs, hys]

/-- A cleared-polynomial certificate implies zero of the original function only
where its clearing multiplier is nonzero.  The identity connecting the function
and polynomial is explicit, so a formal polynomial theorem cannot silently be
treated as a proof about an unformalized theta implementation. -/
theorem theta_zero_where_clearer_ne_zero
    (P : Polynomial (Polynomial K)) (theta clearer : K → K → K)
    (n : ℕ) (xs ys : Finset K)
    (hx : P.natDegree ≤ 2 * n + 4)
    (hy : ∀ i, (P.coeff i).natDegree ≤ 2 * n + 3)
    (hxs : xs.card = 2 * n + 5) (hys : ys.card = 2 * n + 4)
    (hgrid : ∀ x ∈ xs, ∀ y ∈ ys, evalXY P x y = 0)
    (hclear : ∀ x y, evalXY P x y = clearer x y * theta x y) :
    ∀ x y, clearer x y ≠ 0 → theta x y = 0 := by
  have hP := theta_grid_zero P n xs ys hx hy hxs hys hgrid
  intro x y hnonzero
  have hproduct : clearer x y * theta x y = 0 := by
    rw [← hclear, hP, evalXY_zero]
  exact (mul_eq_zero.mp hproduct).resolve_left hnonzero

/-- A nonzero polynomial missed by the three earlier sample points. -/
noncomputable def threePointFalseControl : Polynomial (Polynomial ℚ) :=
  (X - C (C 2)) * (X - C (C 3))

theorem three_point_false_control :
    evalXY threePointFalseControl 2 3 = 0 ∧
    evalXY threePointFalseControl 3 2 = 0 ∧
    evalXY threePointFalseControl 2 5 = 0 ∧
    evalXY threePointFalseControl 4 5 = 2 := by
  norm_num [threePointFalseControl, evalXY]

/-- Passing three spot checks does not establish a polynomial identity. -/
theorem three_point_test_not_sound :
    ¬ (∀ P : Polynomial (Polynomial ℚ),
      evalXY P 2 3 = 0 → evalXY P 3 2 = 0 → evalXY P 2 5 = 0 → P = 0) := by
  intro h
  rcases three_point_false_control with ⟨ha, hb, hc, hd⟩
  have hz := h threePointFalseControl ha hb hc
  rw [hz, evalXY_zero] at hd
  norm_num at hd

end VOTKP.ThetaGrid

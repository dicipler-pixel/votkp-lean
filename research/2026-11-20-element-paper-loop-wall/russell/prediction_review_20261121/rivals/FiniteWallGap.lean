/-
Jeromie Beasley's element paper, November 2026. Finite-gap identifiability.
Core Lean 4.34.1. A face's coordinate here is its squared reflection.
The unshifted two-face decision is 1 < x+y. All values below are rational.
-/
namespace Beasley.WallGap

def StrictInc (f : Rat → Rat) : Prop := ∀ x y, x < y → f x < f y

/-- Glue strictly increasing functions where their values agree. -/
def splice (cut : Rat) (left right : Rat → Rat) (x : Rat) : Rat :=
  if x ≤ cut then left x else right x

theorem splice_increases {l r : Rat → Rat} (cut : Rat)
    (hl : StrictInc l) (hr : StrictInc r) (join : l cut = r cut) :
    StrictInc (splice cut l r) := by
  intro x y hxy
  unfold splice
  split <;> rename_i hx <;> split <;> rename_i hy
  · exact hl x y hxy
  · have hcy : cut < y := by grind
    have hy' := hr cut y hcy
    by_cases heq : x = cut
    · subst x
      grind
    · have hx' := hl x cut (by grind)
      grind
  · grind
  · exact hr x y hxy

/-- The affine map carrying [a,b] to [A,B]. -/
def segment (a b A B x : Rat) : Rat :=
  A + ((B-A)/(b-a))*(x-a)

theorem segment_at_left (a b A B : Rat) : segment a b A B a = A := by
  unfold segment
  grind

theorem segment_at_right {a b : Rat} (A B : Rat) (hab : a < b) :
    segment a b A B b = B := by
  have hd : b-a ≠ 0 := by grind
  have heq := Rat.div_mul_cancel (a := B-A) hd
  unfold segment
  grind

theorem segment_increases {a b A B : Rat} (h : a < b) (k : A < B) :
    StrictInc (segment a b A B) := by
  have hd : 0 < b-a := by grind
  have hs : 0 < (B-A)/(b-a) := (Rat.lt_div_iff hd).2 (by grind)
  intro x y hxy
  have diff : x-a < y-a := by grind
  exact Rat.add_lt_add_left.mpr (Rat.mul_lt_mul_of_pos_left diff hs)

/-- Home of the breakpoints L, t, H. The new wall t is sent to 1/2.
Outside [L,H] this map leaves the face power unchanged. -/
def regrade (L t H : Rat) : Rat → Rat :=
  splice L id (splice t (segment L t L (1/2))
    (splice H (segment t H (1/2) H) id))

structure Admissible (L t H : Rat) : Prop where
  Lt : L < t
  tH : t < H
  Lwall : L < 1/2
  wallH : 1/2 < H

theorem regrade_increases {L t H : Rat} (h : Admissible L t H) :
    StrictInc (regrade L t H) := by
  have hind : StrictInc (id : Rat → Rat) := by intro x y hxy; exact hxy
  have left := segment_increases h.Lt h.Lwall
  have right := segment_increases h.tH h.wallH
  have hi := splice_increases H right hind (segment_at_right (1/2) H h.tH)
  have hm : segment L t L (1/2) t =
      splice H (segment t H (1/2) H) id t := by
    rw [segment_at_right L (1/2) h.Lt]
    unfold splice
    rw [ite_eq_left (show t ≤ H by have := h.tH; grind),segment_at_left]
  have mid := splice_increases t left hi hm
  apply splice_increases L hind mid
  unfold splice
  rw [ite_eq_left (show L ≤ t by have := h.Lt; grind),segment_at_left]
  rfl

theorem regrade_at_t {L t H : Rat} (h : Admissible L t H) :
    regrade L t H t = 1/2 := by
  unfold regrade splice
  rw [ite_eq_right (show ¬ t ≤ L by have := h.Lt; grind),ite_eq_left (show t ≤ t by grind)]
  exact segment_at_right L (1/2) h.Lt

theorem regrade_fixes_observed {L t H x : Rat} (h : Admissible L t H)
    (gap : x ≤ L ∨ H ≤ x) : regrade L t H x = x := by
  rcases gap with hx | hx
  · unfold regrade splice
    rw [ite_eq_left hx]
    rfl
  · have lt := h.Lt
    have th := h.tH
    by_cases top : x = H
    · subst x
      unfold regrade splice
      rw [ite_eq_right (by grind : ¬ H ≤ L),ite_eq_right (by grind : ¬ H ≤ t),
        ite_eq_left (by grind : H ≤ H)]
      exact segment_at_right (1/2) H th
    · unfold regrade splice
      rw [ite_eq_right (by grind : ¬ x ≤ L),ite_eq_right (by grind : ¬ x ≤ t),
        ite_eq_right (by grind : ¬ x ≤ H)]
      rfl

def mixed (f : Rat → Rat) (x y : Rat) : Prop := 1 < f x + f y

/-- The same monotone symmetric rival agrees on all pairs outside the gap.
On every equal input the rival has the preselected cutoff t. -/
theorem alternative_on_gap {L t H : Rat} (h : Admissible L t H) :
    ∃ f : Rat → Rat, StrictInc f ∧
      (∀ x, (mixed f x x ↔ t < x)) ∧
      (∀ x y, (x ≤ L ∨ H ≤ x) → (y ≤ L ∨ H ≤ y) →
        (mixed f x y ↔ 1 < x+y)) := by
  refine ⟨regrade L t H,regrade_increases h,?_,?_⟩
  · intro x
    have inc := regrade_increases h
    have fixed := regrade_at_t h
    unfold mixed
    have half : (1/2 : Rat)+(1/2) = 1 := by decide +kernel
    rw [← half, ← fixed]
    constructor
    · intro hx
      by_cases pos : t < x
      · exact pos
      · by_cases eq : t = x
        · subst x
          grind
        · have opp := inc x t (by grind)
          grind
    · intro hx
      have pos := inc t x hx
      grind
  · intro x y hx hy
    unfold mixed
    rw [regrade_fixes_observed h hx,regrade_fixes_observed h hy]

def g (z : Rat) : Rat := (z-1)/(z+1)
def power (a b : Rat) : Rat := (g a)^2+(g b)^2
def trace (a b : Rat) : Rat := 2-4*((a-1)^2/(4*a))*((b-1)^2/(4*b))

/-- The controlled equal-face experiment at 35/6. -/
theorem diagonal_35_6 :
    g (35/6) = 29/41 ∧ power (35/6) (35/6) = 1682/1681 ∧
    1 < power (35/6) (35/6) ∧ trace (35/6) (35/6) = -354481/176400 := by
  decide +kernel

/-- If both independently calibrated inputs are below the shifted diagonal,
every coordinatewise increasing two-face instrument must call them closed
provided its shifted diagonal is closed at that upper bound. -/
theorem rectangle_from_upper {R : Rat → Rat → Rat} {threshold : Rat}
    (mono : ∀ a a' b b', a ≤ a' → b ≤ b' → R a b ≤ R a' b')
    {u a b : Rat} (ha : a ≤ u) (hb : b ≤ u)
    (atUpper : R u u < threshold) : R a b < threshold := by
  have bound := mono a u b u ha hb
  grind

/-- The two class-defining silver and silicon inputs, with the source decimals
written as rational numbers. Their arithmetic midpoint is the raw-z rival. -/
def ag : Rat := (7576234/1000000) / (130447/100000)
def si : Rat := (815168/100000) / (13895212/10000000)
def fitted : Rat := (ag+si)/2

def beFace : Rat := (153896205/1000000) / (1821115/100000)
def rbFace : Rat := (18305886/1000) / (4356865/1000)

/-- The formal non-identifiability construction applies to the exact adopted endpoints. -/
theorem element_gap_fits : Admissible ((g ag)^2) ((g fitted)^2) ((g si)^2) := by
  constructor <;> decide +kernel

/-- Distinguish the historical shifted-quadrature model from a mixed correction
that preserves every one-face decision but flips Be/Rb to open. -/
theorem be_rb_sensitive_to_mixing :
    1 < power beFace rbFace ∧ power beFace rbFace < 2*(g fitted)^2 ∧
    2*(g fitted)^2 < power beFace rbFace + (1/40)*(g beFace-g rbFace)^2 := by
  decide +kernel

/-- A 35/6 diagonal is definitely below the fitted single-face cutoff. -/
theorem fitted_closes_diagonal : g (35/6) < g fitted := by decide +kernel

/-- Counterexample to the proposed reversed sign of the exact diagonal control. -/
theorem wrong_diagonal_sign_refuted : ¬ (trace (35/6) (35/6) ≥ -2) := by decide +kernel

#print axioms alternative_on_gap
#print axioms diagonal_35_6
#print axioms rectangle_from_upper
#print axioms element_gap_fits
#print axioms be_rb_sensitive_to_mixing
#print axioms fitted_closes_diagonal
#print axioms wrong_diagonal_sign_refuted

end Beasley.WallGap

/-
  BallJoins.lean — the exact joints of the One Ball mixer.
  Jeromie Beasley. Lean 4.34.1 with Mathlib. No sorry.

  J1  A ratio of two books is a peel step: (W₋ − W₊)/(W₋ + W₊) = Γ(W₋/W₊).
  J2  The equal-gap rung ceilings 1/(2k+1) are the peel steps of ratio (k+1)/k.
  J3  Garrett's line Γ² = 1/2 is the peel ratio 3 + 2√2.
  J4  The perpendicular commutator trace in reflect/transmit form: 2 − 4 sinh⁴(r/2) = 2 − 4 (R/T)².
  J5  Euclid's square is the Thomas-turn triple: a²(1 − t², 2t, 1 + t²) = (a² − b², 2ab, a² + b²), t = b/a.
  J6  Twin starts past 5 end in 1, 7 or 9: three shafts for three axes (Elizabeth Johnson's theorem, re-proved).
  J7  Reversing two symmetric steps reverses the turn: if AB = LR then BA = (RᵀLR)Rᵀ.
  J8  The prime current is a Smith point: (F − B)/(F + B) = Γ(F/B).
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Data.Nat.Prime.Basic

/-!  Every statement is over an arbitrary field (ordered where needed), so it holds in ℚ and ℝ alike.
  Hyperbolic functions enter only through c = cosh, s = sinh with c² − s² = 1, and √2 through s² = 2. -/

namespace BallJoins

variable {K : Type*} [Field K]

/-- The Smith (peel) coordinate of a ratio. -/
def gam (z : K) : K := (z - 1) / (z + 1)

/-! ## J1 and J8: a ratio of two counts is a peel step -/

theorem book_is_peel (Wp Wm : K) (hp : Wp ≠ 0) (hs : Wm + Wp ≠ 0) :
    (Wm - Wp) / (Wm + Wp) = gam (Wm / Wp) := by
  unfold gam
  have h2 : Wm / Wp + 1 ≠ 0 := by
    rw [div_add_one hp]; exact div_ne_zero hs hp
  field_simp

/-- The prime current (forward minus backward over the total) is the same statement. -/
theorem current_is_peel (F Bk : K) (hB : Bk ≠ 0) (hs : F + Bk ≠ 0) :
    (F - Bk) / (F + Bk) = gam (F / Bk) := book_is_peel Bk F hB hs

/-! ## J2: the rung ceilings are peel steps -/

theorem ceiling_is_peel {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (k : ℕ) (hk : 0 < k) : gam (((k:F) + 1) / k) = 1 / (2 * k + 1) := by
  unfold gam
  have hk' : (0:F) < k := by exact_mod_cast hk
  have h1 : (k:F) ≠ 0 := hk'.ne'
  have h2 : (2 * (k:F) + 1) ≠ 0 := by linarith
  have h3 : ((k:F) + 1) / k + 1 ≠ 0 := by
    rw [div_add_one h1]; exact div_ne_zero (by linarith) h1
  field_simp
  ring

/-! ## J3: Garrett's line Γ² = 1/2 is the ratio 3 + 2√2 -/

theorem line_ratio {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]
    (r : F) (hr : 0 < r) (hs : r ^ 2 = 2) : gam (3 + 2 * r) ^ 2 = 1 / 2 := by
  unfold gam
  have h4 : (3 + 2 * r + 1) ≠ 0 := by linarith
  rw [div_pow, div_eq_div_iff (pow_ne_zero 2 h4) (by norm_num)]
  nlinarith [hs]

/-- Norm 5 sits inside the line, Garrett's drawn step 7 outside it. -/
theorem five_inside_seven_outside : gam (5:ℚ) ^ 2 < 1 / 2 ∧ 1 / 2 < gam (7:ℚ) ^ 2 := by
  unfold gam; norm_num

/-! ## J4: the commutator trace in reflect/transmit form.
  With c = cosh(r/2), s = sinh(r/2) and tanh = s/c: R = tanh², T = 1 − R, and R/T = s².
  Hence 2 − 4 sinh⁴(r/2) = 2 − 4 (R/T)². -/

theorem trace_reflect_transmit (c s : K) (hc : c ≠ 0) (hid : c ^ 2 - s ^ 2 = 1) :
    let R := (s / c) ^ 2
    2 - 4 * s ^ 4 = 2 - 4 * (R / (1 - R)) ^ 2 := by
  intro R
  have hT : 1 - R = 1 / c ^ 2 := by
    simp only [R, div_pow]; field_simp; exact hid
  have hRT : R / (1 - R) = s ^ 2 := by
    rw [hT]; simp only [R, div_pow]; field_simp
  rw [hRT]; ring

/-! ## J5: Euclid's square is the Thomas-turn triple -/

theorem euclid_is_thomas (a b : K) (ha : a ≠ 0) :
    a^2 * (1 - (b/a)^2) = a^2 - b^2 ∧ a^2 * (2 * (b/a)) = 2 * a * b ∧
    a^2 * (1 + (b/a)^2) = a^2 + b^2 := by
  refine ⟨?_, ?_, ?_⟩ <;> field_simp

theorem euclid_pythagorean (a b : ℤ) : (a^2 - b^2)^2 + (2*a*b)^2 = (a^2 + b^2)^2 := by ring

/-- Garrett's norm-5 step: Γ² = 4/9, the pair (9, 4), the triple (65, 72, 97). -/
theorem garrett_pair : gam (5:ℚ) ^ 2 = 4 / 9 ∧
    ((9:ℤ)^2 - 4^2, 2*9*4, (9:ℤ)^2 + 4^2) = (65, 72, 97) := by
  unfold gam; norm_num

/-! ## J6: three shafts (Elizabeth Johnson's twin-start theorem, re-proved here) -/

theorem twin_start_digit {a : ℕ} (ha : Nat.Prime a) (ha2 : Nat.Prime (a + 2)) (h5 : 5 < a) :
    a % 10 = 1 ∨ a % 10 = 7 ∨ a % 10 = 9 := by
  have hodd : a % 2 = 1 := by
    by_contra h
    have : 2 ∣ a := Nat.dvd_of_mod_eq_zero (by omega)
    rcases (Nat.dvd_prime ha).mp this with h' | h' <;> omega
  have n0 : a % 5 ≠ 0 := by
    intro h
    rcases (Nat.dvd_prime ha).mp (Nat.dvd_of_mod_eq_zero h) with h' | h' <;> omega
  have n3 : a % 5 ≠ 3 := by
    intro h
    have : 5 ∣ a + 2 := Nat.dvd_of_mod_eq_zero (by omega)
    rcases (Nat.dvd_prime ha2).mp this with h' | h' <;> omega
  have h5' : a % 5 = 1 ∨ a % 5 = 2 ∨ a % 5 = 4 := by omega
  rcases h5' with h | h | h <;> omega

/-! ## J7: reverse the order, reverse the turn.
  Stated for any monoid with a product-reversing involution τ (the transpose on matrices).
  If the steps A, B are symmetric and AB = L·R with L symmetric and R·τR = 1,
  then BA = (τR·L·R)·τR with τR·L·R symmetric: the reverse order has the inverse turn. -/

theorem reverse_turn {M : Type*} [Monoid M] (τ : M → M)
    (hmul : ∀ x y, τ (x * y) = τ y * τ x) (hinv : ∀ x, τ (τ x) = x)
    (A B L R : M) (hA : τ A = A) (hB : τ B = B) (hL : τ L = L)
    (hR : R * τ R = 1) (hAB : A * B = L * R) :
    B * A = (τ R * L * R) * τ R ∧ τ (τ R * L * R) = τ R * L * R := by
  constructor
  · have h1 : B * A = τ (A * B) := by rw [hmul, hA, hB]
    rw [h1, hAB, hmul, hL, mul_assoc, mul_assoc, hR, mul_one]
  · rw [hmul, hmul, hinv, hL, mul_assoc]

end BallJoins

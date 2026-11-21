/-
  Two Trees Theorem 8.6, the real band criterion, over ℚ.
  Core Lean 4, no Mathlib.

  For s ≠ 0, tr[a,b] = 2 − v ((s − s⁻¹)² − v),
  so |tr[a,b]| < 2 ↔ 0 < v ((s − s⁻¹)² − v) < 4.
  When s = exp x, (s − s⁻¹)² = 4 sinh² x. The paper's hypothesis s ≠ ±1 is kept;
  the equivalence uses s ≠ 0.
-/
namespace PeelTrees5

structure M2 where
  a : Rat
  b : Rat
  c : Rat
  d : Rat

def M2.mul (X Y : M2) : M2 := ⟨X.a*Y.a + X.b*Y.c, X.a*Y.b + X.b*Y.d, X.c*Y.a + X.d*Y.c, X.c*Y.b + X.d*Y.d⟩
def M2.tr (X : M2) : Rat := X.a + X.d

def rA (s : Rat) : M2 := ⟨s*s, s, 0, 1⟩
def rB (s v : Rat) : M2 := ⟨s*s, 0, -(v*s), 1⟩
def rAi (s : Rat) : M2 := ⟨1, -s, 0, s*s⟩
def rBi (s v : Rat) : M2 := ⟨1, 0, v*s, s*s⟩

def comm (s v : Rat) : M2 := M2.mul (M2.mul (M2.mul (rA s) (rB s v)) (rAi s)) (rBi s v)

theorem comm_trace (s v : Rat) :
    (comm s v).tr = 2*(s*s*s*s) - v*(s*s)*((s*s - 1)*(s*s - 1) - v*(s*s)) := by
  simp only [comm, M2.tr, M2.mul, rA, rB, rAi, rBi]; grind

theorem abs_two_sub (u : Rat) : Rat.abs (2 - u) < 2 ↔ 0 < u ∧ u < 4 := by
  cases (inferInstance : Decidable (2 - u < 0)) with
  | isTrue hlt =>
    simp [Rat.abs]
    grind
  | isFalse hge =>
    simp [Rat.abs]
    grind

/-- **Theorem 8.6.** The absolute value of `tr[a,b]` is less than 2
    iff `0 < v ((s - s⁻¹)² - v) < 4`. -/
theorem band_criterion (s v : Rat) (hs : s ≠ 0) (_hs1 : s ≠ 1) (_hs2 : s ≠ -1) :
    Rat.abs ((comm s v).tr / (s * s * s * s)) < 2 ↔
      0 < v * ((s - s⁻¹) * (s - s⁻¹) - v) ∧
        v * ((s - s⁻¹) * (s - s⁻¹) - v) < 4 := by
  have h := comm_trace s v
  have hs4 : s * s * s * s ≠ 0 := by grind
  rw [h]
  have hdiv :
      (2*(s*s*s*s) - v*(s*s)*((s*s - 1)*(s*s - 1) - v*(s*s))) / (s*s*s*s)
        = 2 - v * ((s - s⁻¹) * (s - s⁻¹) - v) := by grind
  rw [hdiv]
  exact abs_two_sub _

end PeelTrees5

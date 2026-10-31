/-
  PeelTrees4 — the knot commutator band (Two Trees v4, problem 1). Core Lean 4, no Mathlib.
  Riley meridians a = [[s,1],[0,1/s]], b = [[s,0],[-v,1/s]], scaled by s: A = s a, B = s b, A' = s a⁻¹, B' = s b⁻¹.
  C = A B A' B' = s⁴ [a,b] and T = tr(AB) = s² tr(ab). Every statement holds over any commutative ring.
-/
namespace PeelTrees4

structure M2 (R : Type) where
  a : R
  b : R
  c : R
  d : R

variable {R : Type} [Lean.Grind.CommRing R]

def M2.mul (X Y : M2 R) : M2 R := ⟨X.a*Y.a + X.b*Y.c, X.a*Y.b + X.b*Y.d, X.c*Y.a + X.d*Y.c, X.c*Y.b + X.d*Y.d⟩
def M2.sub (X Y : M2 R) : M2 R := ⟨X.a - Y.a, X.b - Y.b, X.c - Y.c, X.d - Y.d⟩
def M2.tr (X : M2 R) : R := X.a + X.d

def rA (s : R) : M2 R := ⟨s*s, s, 0, 1⟩
def rB (s v : R) : M2 R := ⟨s*s, 0, -(v*s), 1⟩
def rAi (s : R) : M2 R := ⟨1, -s, 0, s*s⟩
def rBi (s v : R) : M2 R := ⟨1, 0, v*s, s*s⟩

/-- Scaled commutator C = A B A' B' and scaled T = tr(AB). -/
def comm (s v : R) : M2 R := M2.mul (M2.mul (M2.mul (rA s) (rB s v)) (rAi s)) (rBi s v)
def T (s v : R) : R := (M2.mul (rA s) (rB s v)).tr

/-- tr(AB) = s⁴ + 1 − v s², i.e. tr(ab) = s² + s⁻² − v. -/
theorem T_eq (s v : R) : T s v = s*s*s*s + 1 - v*s*s := by
  simp only [T, M2.tr, M2.mul, rA, rB]; grind

/-- The commutator trace identity:  s⁴ tr[a,b] = 2 s⁴ − v s² ((s²−1)² − v s²),
    i.e. tr[a,b] = 2 − v((s − 1/s)² − v). -/
theorem comm_trace (s v : R) :
    (comm s v).tr = 2*(s*s*s*s) - v*(s*s)*((s*s - 1)*(s*s - 1) - v*(s*s)) := by
  simp only [comm, M2.tr, M2.mul, rA, rB, rAi, rBi]; grind

/-- The same identity through tr(ab):  tr[a,b] − 2 = −v (tr(ab) − 2)  (scaled by s⁴). -/
theorem comm_trace_ab (s v : R) :
    (comm s v).tr - 2*(s*s*s*s) = -(v*(s*s)) * (T s v - 2*(s*s)) := by
  rw [comm_trace, T_eq]; grind

/-- v is determined by tr(ab):  s² v = (s² − 1)² + (2 s² − T).  For real s ≠ 0 this reads
    v = (s − 1/s)² + (2 − tr ab): so tr(ab) < 2 forces v > 0. -/
theorem v_from_T (s v : R) : v*(s*s) = (s*s - 1)*(s*s - 1) + (2*(s*s) - T s v) := by
  rw [T_eq]; grind

/-! ### Torus knots T(2,n): the Riley polynomial is a polynomial in T alone. W = (BA)^((n−1)/2). -/

def W3 (s v : R) : M2 R := M2.mul (rB s v) (rA s)
def W5 (s v : R) : M2 R := M2.mul (W3 s v) (W3 s v)
def W7 (s v : R) : M2 R := M2.mul (W5 s v) (W3 s v)
def rel (s v : R) (W : M2 R) : M2 R := M2.sub (M2.mul (rA s) W) (M2.mul W (rB s v))

/-- Trefoil: A W − W B = (T − s²)·[[0, s],[s v, 0]]: the Riley curve is tr(ab) = 1. -/
theorem trefoil_T (s v : R) :
    let D := rel s v (W3 s v)
    D.a = 0 ∧ D.b = (T s v - s*s) * s ∧ D.c = (T s v - s*s) * (s*v) ∧ D.d = 0 := by
  simp only [rel, W3, T, M2.tr, M2.mul, M2.sub, rA, rB]; refine ⟨?_,?_,?_,?_⟩ <;> grind

/-- T(2,5): A W − W B = (T² − s²T − s⁴)·[[0, s],[s v, 0]]:  tr(ab)² − tr(ab) − 1 = 0,
    tr(ab) = 2cos(π/5) or 2cos(3π/5). -/
theorem torus5_T (s v : R) :
    let D := rel s v (W5 s v)
    let P := T s v * T s v - s*s * T s v - s*s*s*s
    D.a = 0 ∧ D.b = P * s ∧ D.c = P * (s*v) ∧ D.d = 0 := by
  simp only [rel, W5, W3, T, M2.tr, M2.mul, M2.sub, rA, rB]; refine ⟨?_,?_,?_,?_⟩ <;> grind

/-- T(2,7): A W − W B = (T³ − s²T² − 2s⁴T + s⁶)·[[0, s],[s v, 0]]:  t³ − t² − 2t + 1 = 0,
    t = 2cos(π/7), 2cos(3π/7), 2cos(5π/7). -/
theorem torus7_T (s v : R) :
    let D := rel s v (W7 s v)
    let t := T s v
    let P := t*t*t - s*s*t*t - 2*(s*s*s*s)*t + s*s*s*s*s*s
    D.a = 0 ∧ D.b = P * s ∧ D.c = P * (s*v) ∧ D.d = 0 := by
  simp only [rel, W7, W5, W3, T, M2.tr, M2.mul, M2.sub, rA, rB]; refine ⟨?_,?_,?_,?_⟩ <;> grind

/-- Trefoil commutator on its curve: tr(ab) = 1 gives tr[a,b] = 2 + v (scaled: s⁴ tr = 2s⁴ + v s⁴),
    with s² v = (s²−1)² + s², so v ≥ 1 for real s: always a boost, never in the band. -/
theorem trefoil_comm (s v : R) (h : T s v = s*s) :
    (comm s v).tr = 2*(s*s*s*s) + v*(s*s*s*s) ∧ v*(s*s) = (s*s - 1)*(s*s - 1) + s*s := by
  have h1 := comm_trace_ab s v; have h2 := v_from_T s v
  rw [h] at h1 h2; constructor <;> grind

/-- On every torus branch tr(ab) = t with 0 < 2 − t: then tr[a,b] − 2 = v(2 − t) with v = (s−1/s)² + (2−t) > 0,
    a product of positives — a boost. Scaled algebraic form: s⁴(tr[a,b] − 2) = v s² (2s² − T). -/
theorem torus_comm (s v : R) :
    (comm s v).tr - 2*(s*s*s*s) = v*(s*s) * (2*(s*s) - T s v) := by
  rw [comm_trace_ab]; grind

/-! ### The band criterion. Put A = (s² − 1)² and w = v s² (so A/s² = (s − 1/s)² = 4 sinh² x and w/s² = v).
    Then s⁴ (2 − tr[a,b]) = w (A − w): the commutator is a rotation iff 0 < w(A − w) < 4 s⁴. -/

/-- s⁴ (2 − tr[a,b]) = w (A − w) with A = (s²−1)², w = v s².  Positive iff 0 < v < (s − 1/s)²,
    which is the condition that the axes of a and b cross. -/
theorem band_k (s v : R) :
    2*(s*s*s*s) - (comm s v).tr = (v*(s*s)) * ((s*s - 1)*(s*s - 1) - v*(s*s)) := by
  rw [comm_trace]; grind

/-- The bound 4 w (A − w) = A² − (2w − A)² ≤ A²: so 2 − tr[a,b] ≤ (s − 1/s)⁴/4 = 4 sinh⁴ x, with equality at
    v = 2 sinh² x. When sinh x < 1 (Γ² = tanh² x < 1/2, the Schottky line) this is below 4: crossing axes force
    an elliptic commutator. -/
theorem band_bound (s v : R) :
    4 * ((v*(s*s)) * ((s*s - 1)*(s*s - 1) - v*(s*s))) =
      ((s*s - 1)*(s*s - 1)) * ((s*s - 1)*(s*s - 1)) - (2*(v*(s*s)) - (s*s - 1)*(s*s - 1)) * (2*(v*(s*s)) - (s*s - 1)*(s*s - 1)) := by
  grind

/-- The peak value: at w = A/2 the bound is attained, 4 w (A − w) = A². -/
theorem band_peak (s : R) (w : R) (h : 2*w = (s*s - 1)*(s*s - 1)) :
    4 * (w * ((s*s - 1)*(s*s - 1) - w)) = ((s*s - 1)*(s*s - 1)) * ((s*s - 1)*(s*s - 1)) := by
  grind

end PeelTrees4

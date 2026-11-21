/-
  False controls for the knot commutator band. The twelve true lemmas
  (`T_eq`, `comm_trace`, `comm_trace_ab`, `v_from_T`, `trefoil_T`, `torus5_T`,
  `torus7_T`, `trefoil_comm`, `torus_comm`, `band_k`, `band_bound`, `band_peak`)
  are proved in `PeelTrees4.lean` and are not repeated here.
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

def comm (s v : R) : M2 R := M2.mul (M2.mul (M2.mul (rA s) (rB s v)) (rAi s)) (rBi s v)
def T (s v : R) : R := (M2.mul (rA s) (rB s v)).tr

def W3 (s v : R) : M2 R := M2.mul (rB s v) (rA s)
def W5 (s v : R) : M2 R := M2.mul (W3 s v) (W3 s v)
def rel (s v : R) (W : M2 R) : M2 R := M2.sub (M2.mul (rA s) W) (M2.mul W (rB s v))

-- FALSE CONTROLS: each must be rejected.
theorem bad_sign (s v : R) :
    (comm s v).tr = 2*(s*s*s*s) + v*(s*s)*((s*s - 1)*(s*s - 1) - v*(s*s)) := by
  simp only [comm, M2.tr, M2.mul, rA, rB, rAi, rBi]; grind
theorem bad_torus5 (s v : R) :
    let D := rel s v (W5 s v)
    let P := T s v * T s v + s*s * T s v - s*s*s*s
    D.b = P * s := by
  simp only [rel, W5, W3, T, M2.tr, M2.mul, M2.sub, rA, rB]; grind
theorem bad_trefoil (s v : R) (h : T s v = s*s) :
    (comm s v).tr = 2*(s*s*s*s) - v*(s*s*s*s) := by
  simp only [comm, T, M2.tr, M2.mul, rA, rB, rAi, rBi] at h ⊢; grind
end PeelTrees4

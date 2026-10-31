/-
  PeelTrees3.lean — the ln 5 commutator is a rotation; the ln 7 one is not.
  Jeromie Beasley. Core Lean 4.34.1, no Mathlib, no sorry, no native_decide.
  Definitions repeated from PeelTrees.lean so the file stands alone.
-/
namespace PeelTrees3
set_option maxRecDepth 200000

structure M4 where
  a00 : Int
  a01 : Int
  a02 : Int
  a03 : Int
  a10 : Int
  a11 : Int
  a12 : Int
  a13 : Int
  a20 : Int
  a21 : Int
  a22 : Int
  a23 : Int
  a30 : Int
  a31 : Int
  a32 : Int
  a33 : Int
deriving DecidableEq, Repr

def M4.mul (A B : M4) : M4 :=
  ⟨A.a00 * B.a00 + A.a01 * B.a10 + A.a02 * B.a20 + A.a03 * B.a30,
   A.a00 * B.a01 + A.a01 * B.a11 + A.a02 * B.a21 + A.a03 * B.a31,
   A.a00 * B.a02 + A.a01 * B.a12 + A.a02 * B.a22 + A.a03 * B.a32,
   A.a00 * B.a03 + A.a01 * B.a13 + A.a02 * B.a23 + A.a03 * B.a33,
   A.a10 * B.a00 + A.a11 * B.a10 + A.a12 * B.a20 + A.a13 * B.a30,
   A.a10 * B.a01 + A.a11 * B.a11 + A.a12 * B.a21 + A.a13 * B.a31,
   A.a10 * B.a02 + A.a11 * B.a12 + A.a12 * B.a22 + A.a13 * B.a32,
   A.a10 * B.a03 + A.a11 * B.a13 + A.a12 * B.a23 + A.a13 * B.a33,
   A.a20 * B.a00 + A.a21 * B.a10 + A.a22 * B.a20 + A.a23 * B.a30,
   A.a20 * B.a01 + A.a21 * B.a11 + A.a22 * B.a21 + A.a23 * B.a31,
   A.a20 * B.a02 + A.a21 * B.a12 + A.a22 * B.a22 + A.a23 * B.a32,
   A.a20 * B.a03 + A.a21 * B.a13 + A.a22 * B.a23 + A.a23 * B.a33,
   A.a30 * B.a00 + A.a31 * B.a10 + A.a32 * B.a20 + A.a33 * B.a30,
   A.a30 * B.a01 + A.a31 * B.a11 + A.a32 * B.a21 + A.a33 * B.a31,
   A.a30 * B.a02 + A.a31 * B.a12 + A.a32 * B.a22 + A.a33 * B.a32,
   A.a30 * B.a03 + A.a31 * B.a13 + A.a32 * B.a23 + A.a33 * B.a33⟩

def M4.tr (A : M4) : M4 := ⟨A.a00, A.a10, A.a20, A.a30, A.a01, A.a11, A.a21, A.a31, A.a02, A.a12, A.a22, A.a32, A.a03, A.a13, A.a23, A.a33⟩
def M4.smul (c : Int) (A : M4) : M4 := ⟨c * A.a00, c * A.a01, c * A.a02, c * A.a03, c * A.a10, c * A.a11, c * A.a12, c * A.a13, c * A.a20, c * A.a21, c * A.a22, c * A.a23, c * A.a30, c * A.a31, c * A.a32, c * A.a33⟩
def M4.red (m : Int) (A : M4) : M4 := ⟨A.a00 % m, A.a01 % m, A.a02 % m, A.a03 % m, A.a10 % m, A.a11 % m, A.a12 % m, A.a13 % m, A.a20 % m, A.a21 % m, A.a22 % m, A.a23 % m, A.a30 % m, A.a31 % m, A.a32 % m, A.a33 % m⟩
def I4 : M4 := ⟨1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1⟩
def eta : M4 := ⟨1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1⟩

/-- The six step directions of Garrett's tree: +i, -i, +j, -j, +k, -k. -/
inductive Dir | pi | mi | pj | mj | pk | mk
deriving DecidableEq, Repr

def Dir.inv : Dir → Dir
  | .pi => .mi | .mi => .pi | .pj => .mj | .mj => .pj | .pk => .mk | .mk => .pk

def allDirs : List Dir := [.pi, .mi, .pj, .mj, .pk, .mk]
theorem mem_allDirs (d : Dir) : d ∈ allDirs := by cases d <;> decide

/-- z times the boost of peel ratio z along direction d: c = (z^2+1)/2, s = (z^2-1)/2, z elsewhere. -/
def boost (c s z : Int) : Dir → M4
  | .pi => ⟨c, s, 0, 0, s, c, 0, 0, 0, 0, z, 0, 0, 0, 0, z⟩
  | .mi => ⟨c, (-s), 0, 0, (-s), c, 0, 0, 0, 0, z, 0, 0, 0, 0, z⟩
  | .pj => ⟨c, 0, s, 0, 0, z, 0, 0, s, 0, c, 0, 0, 0, 0, z⟩
  | .mj => ⟨c, 0, (-s), 0, 0, z, 0, 0, (-s), 0, c, 0, 0, 0, 0, z⟩
  | .pk => ⟨c, 0, 0, s, 0, z, 0, 0, 0, 0, z, 0, s, 0, 0, c⟩
  | .mk => ⟨c, 0, 0, (-s), 0, z, 0, 0, 0, 0, z, 0, (-s), 0, 0, c⟩

/-- Peel ratio 5 (rapidity ln 5, Smith step 2/3) and peel ratio 7 (rapidity ln 7, Garrett's drawing). -/
def B5 : Dir → M4 := boost 13 12 5
def B7 : Dir → M4 := boost 25 24 7

/-- The scaled matrix of a word (applied left to right, starting at the identity). -/
def word (B : Dir → M4) (w : List Dir) : M4 := w.foldl (fun M d => M4.mul M (B d)) I4

/-- Its first column is z^L times the point reached, (cosh d, sinh d * direction). -/
def pt (M : M4) : List Int := [M.a00, M.a10, M.a20, M.a30]


/-- The commutator i j i^-1 j^-1 at peel ratio z, scaled by z^4. -/
def comm (B : Dir → M4) : M4 := word B [.pi, .pj, .mi, .mj]

/-- Peel ratio 5: the commutator fixes the timelike point p = (3, 2, 2, 0) (Minkowski norm 9 - 4 - 4 = 1),
    so it is a rotation of hyperbolic space about p; its trace is 196/625 = 2 + 2 cos phi with
    cos phi = -527/625. -/
theorem comm5_fixes_p : pt (M4.mul (comm B5) ⟨3,0,0,0, 2,0,0,0, 2,0,0,0, 0,0,0,0⟩) = [1875, 1250, 1250, 0] := by decide
theorem comm5_p_unit : (3 : Int) * 3 - 2 * 2 - 2 * 2 - 0 * 0 = 1 := by decide
theorem comm5_trace : (comm B5).a00 + (comm B5).a11 + (comm B5).a22 + (comm B5).a33 = 196 := by decide
theorem comm5_cos : (196 : Int) - 2 * 625 = 2 * (-527) := by decide
/-- The rotation angle has cos phi = -527/625, i.e. cos(phi/2) = 7/25 up to sign: 2*49 - 625 = -527. -/
theorem comm5_half : 2 * (7 * 7) - 625 = (-527 : Int) := by decide
/-- Peel ratio 7: trace 51076/2401 > 4, so the commutator is not a rotation (it is loxodromic). -/
theorem comm7_trace : (comm B7).a00 + (comm B7).a11 + (comm B7).a22 + (comm B7).a33 = 51076 ∧ 51076 > 4 * 2401 := by decide

end PeelTrees3

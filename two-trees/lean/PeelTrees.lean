/-
  PeelTrees.lean — Two Trees in One Ball: Norm Ladders, Peel Steps and Knot Boosts.
  Jeromie Beasley. Core Lean 4.34.1, no Mathlib, no sorry, no axioms beyond Lean's own.
  Every finite check is decided by the kernel (`decide`), never by compiled code (`native_decide`).

  Contents
    1. Lipschitz quaternions of norm 5 (Garrett's six generators, the LPS count, reduced words).
    2. The peel ladder: Gamma = (z-1)/(z+1), Einstein addition, Gamma_L = (5^L-1)/(5^L+1) for every L,
       the boost entries cosh = (1+G^2)/(1-G^2), sinh = 2G/(1-G^2), and the Schottky threshold G^2 > 1/2.
    3. Exact Lorentz boosts with rational entries (peel ratios 5 and 7, scaled to integers):
       Lorentz identity, inverse pairs, exact points, straight path farthest, Thomas rotation exact.
    4. Freeness for every word length: 5^L cosh d(w) is never divisible by 5 (and 7^L cosh d(w) never by 7),
       so no reduced word is the identity and no reduced word returns to the origin.
    5. Knot side: Riley meridians over any commutative ring, the trefoil and figure-eight relations
       factor through their Riley polynomials, and the trefoil longitude on its curve.
-/

namespace PeelTrees

set_option maxRecDepth 200000

/-! ## 1. Quaternions -/

structure Q where
  a : Int
  b : Int
  c : Int
  d : Int
deriving DecidableEq, Repr

def Q.mul (p q : Q) : Q :=
  ⟨p.a*q.a - p.b*q.b - p.c*q.c - p.d*q.d,
   p.a*q.b + p.b*q.a + p.c*q.d - p.d*q.c,
   p.a*q.c - p.b*q.d + p.c*q.a + p.d*q.b,
   p.a*q.d + p.b*q.c - p.c*q.b + p.d*q.a⟩

def Q.conj (p : Q) : Q := ⟨p.a, -p.b, -p.c, -p.d⟩
def Q.norm (p : Q) : Int := p.a*p.a + p.b*p.b + p.c*p.c + p.d*p.d

/-- Euler's four-square identity: the norm is multiplicative, so a word of L generators has norm 5^L. -/
theorem norm_mul (p q : Q) : (p.mul q).norm = p.norm * q.norm := by
  cases p; cases q; simp only [Q.mul, Q.norm]; grind

/-- Garrett's six generators 1 ± 2i, 1 ± 2j, 1 ± 2k. -/
def gens : List Q := [⟨1,2,0,0⟩, ⟨1,-2,0,0⟩, ⟨1,0,2,0⟩, ⟨1,0,-2,0⟩, ⟨1,0,0,2⟩, ⟨1,0,0,-2⟩]

theorem gens_norm : ∀ g ∈ gens, g.norm = 5 := by decide

/-- The backward step is the conjugate: g times its conjugate is the scalar 5. -/
theorem gens_conj : ∀ g ∈ gens, g.mul g.conj = ⟨5,0,0,0⟩ := by decide

/-- The conjugate of each generator is again a generator (the tree is closed under stepping back). -/
theorem gens_conj_mem : ∀ g ∈ gens, g.conj ∈ gens := by decide

def rng : List Int := [-2, -1, 0, 1, 2]
def box : List Q := rng.flatMap fun a => rng.flatMap fun b => rng.flatMap fun c => rng.map fun d => ⟨a,b,c,d⟩

theorem sq_le_five (x : Int) (h : x * x ≤ 5) : -2 ≤ x ∧ x ≤ 2 := by
  constructor
  · apply Classical.byContradiction; intro hc
    have h3 : 3 ≤ -x := by omega
    have : 3 * 3 ≤ (-x) * (-x) := Int.mul_le_mul h3 h3 (by omega) (by omega)
    rw [Int.neg_mul_neg] at this; omega
  · apply Classical.byContradiction; intro hc
    have h3 : 3 ≤ x := by omega
    have : 3 * 3 ≤ x * x := Int.mul_le_mul h3 h3 (by omega) (by omega)
    omega

theorem sq_nonneg' (x : Int) : 0 ≤ x * x := by
  rcases Int.le_total 0 x with h | h
  · exact Int.mul_nonneg h h
  · exact Int.mul_nonneg_of_nonpos_of_nonpos h h

/-- Every coordinate of a norm-5 quaternion lies in [-2, 2], so `box` holds all of them. -/
theorem norm5_bound (q : Q) (h : q.norm = 5) :
    (-2 ≤ q.a ∧ q.a ≤ 2) ∧ (-2 ≤ q.b ∧ q.b ≤ 2) ∧ (-2 ≤ q.c ∧ q.c ≤ 2) ∧ (-2 ≤ q.d ∧ q.d ≤ 2) := by
  unfold Q.norm at h
  have ha := sq_nonneg' q.a; have hb := sq_nonneg' q.b
  have hc := sq_nonneg' q.c; have hd := sq_nonneg' q.d
  exact ⟨sq_le_five _ (by omega), sq_le_five _ (by omega), sq_le_five _ (by omega), sq_le_five _ (by omega)⟩

/-- There are exactly 8 (5 + 1) = 48 integer quaternions of norm 5. -/
theorem norm5_count : (box.filter (fun q => q.norm == 5)).length = 48 := by decide

/-- Of the 48, exactly six have a odd and positive with b, c, d even, and they are Garrett's generators
    (the Lubotzky–Phillips–Sarnak normalisation, p + 1 = 6). -/
theorem lps_six : ∀ q ∈ box,
    (q.norm = 5 ∧ 0 < q.a ∧ q.a % 2 = 1 ∧ q.b % 2 = 0 ∧ q.c % 2 = 0 ∧ q.d % 2 = 0) ↔ q ∈ gens := by decide

/-- Reduced words: never a generator followed by its own conjugate. -/
def qwords : Nat → List (List Q)
  | 0 => [[]]
  | n + 1 => (qwords n).flatMap fun w => (gens.filter fun g => w.head?.map Q.conj != some g).map fun g => g :: w

def qprod (w : List Q) : Q := w.foldr Q.mul ⟨1,0,0,0⟩
def qsign (q : Q) : Q := if q.a < 0 || (q.a == 0 && (q.b < 0 || (q.b == 0 && (q.c < 0 || (q.c == 0 && q.d < 0))))) then ⟨-q.a,-q.b,-q.c,-q.d⟩ else q

theorem qwords_three_count : (qwords 3).length = 150 := by decide

/-- The 150 reduced words of length 3 give 150 different quaternions, even up to sign. -/
theorem qwords_three_distinct : ((qwords 3).map fun w => qsign (qprod w)).Nodup := by decide

/-- None of them is divisible by 5, so none collapses to a shorter word times a scalar. -/
theorem qwords_three_primitive : ∀ w ∈ qwords 3, ¬ (qprod w).a % 5 = 0 ∨ ¬ (qprod w).b % 5 = 0 ∨
    ¬ (qprod w).c % 5 = 0 ∨ ¬ (qprod w).d % 5 = 0 := by decide

/-! ## 2. The peel ladder (VOTKP Theorem 8.1, Theorem 15.1, Corollary 15.2) -/

/-- Smith (peel) coordinate of a peel ratio z. -/
def gam (z : Rat) : Rat := (z - 1) / (z + 1)
/-- Einstein (rapidity) addition on the Smith disk. -/
def oplus (x y : Rat) : Rat := (x + y) / (1 + x * y)

/-- Steps compose by multiplying ratios: Gamma(A) ⊕ Gamma(B) = Gamma(AB). -/
theorem gam_mul (A B : Rat) (hA : 0 ≤ A) (hB : 0 ≤ B) : oplus (gam A) (gam B) = gam (A * B) := by
  unfold oplus gam
  have h1 : A + 1 ≠ 0 := by grind
  have h2 : B + 1 ≠ 0 := by grind
  have h0 : 0 ≤ A * B := Rat.mul_nonneg hA hB
  have h3 : A * B + 1 ≠ 0 := by grind
  grind

theorem gam_five : gam 5 = 2 / 3 := by unfold gam; grind
theorem gam_seven : gam 7 = 3 / 4 := by unfold gam; grind

/-- The peel walk: L steps of 2/3 combined by ⊕. -/
def peel : Nat → Rat
  | 0 => 0
  | n + 1 => oplus (peel n) (2 / 3)

theorem five_pow_nonneg (n : Nat) : (0 : Rat) ≤ 5 ^ n := by
  induction n with
  | zero => grind
  | succ n ih => rw [Rat.pow_succ]; exact Rat.mul_nonneg ih (by grind)

/-- The norm ladder is the peel ladder: after L steps the Smith coordinate is (5^L - 1)/(5^L + 1),
    for every L. -/
theorem peel_ladder (n : Nat) : peel n = gam (5 ^ n) := by
  induction n with
  | zero => show (0 : Rat) = (1 - 1) / (1 + 1); grind
  | succ n ih =>
    simp only [peel]
    rw [ih, ← gam_five, gam_mul _ _ (five_pow_nonneg n) (by grind), Rat.pow_succ]

/-- The boost entries in the Smith coordinate: cosh = (1+G^2)/(1-G^2) = (z^2+1)/(2z) and
    sinh = 2G/(1-G^2) = (z^2-1)/(2z). -/
theorem cosh_from_gam (z : Rat) (hz : 0 < z) :
    (1 + gam z * gam z) / (1 - gam z * gam z) = (z * z + 1) / (2 * z) := by
  unfold gam
  have h1 : z + 1 ≠ 0 := by grind
  have h2 : z ≠ 0 := by grind
  grind

theorem sinh_from_gam (z : Rat) (hz : 0 < z) :
    (2 * gam z) / (1 - gam z * gam z) = (z * z - 1) / (2 * z) := by
  unfold gam
  have h1 : z + 1 ≠ 0 := by grind
  have h2 : z ≠ 0 := by grind
  grind

/-- Schottky threshold in the peel coordinate: G^2 > 1/2. The norm-5 step sits below it,
    Garrett's ln 7 step above it. -/
theorem schottky_five_below : gam 5 * gam 5 < 1 / 2 := by rw [gam_five]; grind
theorem schottky_seven_above : 1 / 2 < gam 7 * gam 7 := by rw [gam_seven]; grind
/-- The same threshold for the ratio itself: z > 3 + 2 sqrt 2, i.e. (z - 3)^2 > 8 with z > 3. -/
theorem schottky_ratio : (5 - 3) * (5 - 3) < (8 : Int) ∧ (8 : Int) < (7 - 3) * (7 - 3) := by decide

/-! ## 3. Exact boosts. A boost of peel ratio z, multiplied by z, has integer entries
    c = (z^2+1)/2, s = (z^2-1)/2 on the axis and z on the other two space directions. -/

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

/-- Every scaled boost is Lorentz: B^T eta B = z^2 eta. -/
theorem lorentz5 : ∀ d ∈ allDirs, (M4.mul (M4.tr (B5 d)) (M4.mul eta (B5 d))) = M4.smul 25 eta := by decide
theorem lorentz7 : ∀ d ∈ allDirs, (M4.mul (M4.tr (B7 d)) (M4.mul eta (B7 d))) = M4.smul 49 eta := by decide

/-- The backward step is the inverse boost: B_d B_{-d} = z^2 I. -/
theorem inverse5 : ∀ d ∈ allDirs, M4.mul (B5 d) (B5 d.inv) = M4.smul 25 I4 := by decide
theorem inverse7 : ∀ d ∈ allDirs, M4.mul (B7 d) (B7 d.inv) = M4.smul 49 I4 := by decide

/-- A pure boost is a symmetric matrix. -/
theorem boost5_symm : ∀ d ∈ allDirs, M4.tr (B5 d) = B5 d := by decide

/-- The scaled matrix of a word (applied left to right, starting at the identity). -/
def word (B : Dir → M4) (w : List Dir) : M4 := w.foldl (fun M d => M4.mul M (B d)) I4

/-- Its first column is z^L times the point reached, (cosh d, sinh d * direction). -/
def pt (M : M4) : List Int := [M.a00, M.a10, M.a20, M.a30]

/-- Straight path +i +i +i: z^3 cosh d = 7813 = (5^6 + 1)/2, so d = 3 ln 5 exactly (lengths add). -/
theorem straight5 : pt (word B5 [.pi, .pi, .pi]) = [7813, 7812, 0, 0] := by decide
theorem straight5_is_three_ln5 : 2 * 7813 = 5 ^ 6 + 1 ∧ 2 * 7812 = 5 ^ 6 - 1 := by decide
/-- Two orthogonal steps: cosh d = cosh^2 (ln 5) = 169/25 (hyperbolic Pythagoras). -/
theorem turn5 : pt (word B5 [.pi, .pj]) = [169, 156, 60, 0] := by decide
/-- The turned paths of the earlier check. -/
theorem turned5 : pt (word B5 [.pi, .pi, .pj]) = [4069, 4056, 300, 0] ∧
    pt (word B5 [.pi, .pj, .pi]) = [2917, 2808, 780, 0] ∧
    pt (word B5 [.pi, .pj, .pk]) = [2197, 2028, 780, 300] := by decide
/-- Garrett's ln 7 numbers: straight 3 ln 7, and the word +i +j +i with cosh d = 19657/343 (d = 4.7415). -/
theorem garrett7 : pt (word B7 [.pi, .pi, .pi]) = [58825, 58824, 0, 0] ∧
    pt (word B7 [.pi, .pj, .pi]) = [19657, 19200, 4200, 0] ∧
    pt (word B7 [.pi, .pi, .pj]) = [30025, 30000, 1176, 0] ∧
    pt (word B7 [.pi, .pj, .pk]) = [15625, 15000, 4200, 1176] := by decide

/-- Reduced words of length n (no step followed by its own reverse). -/
def rwords : Nat → List (List Dir)
  | 0 => [[]]
  | n + 1 => (rwords n).flatMap fun w => (allDirs.filter fun d => w.getLast?.map Dir.inv != some d).map fun d => w ++ [d]

theorem rwords_three_count : (rwords 3).length = 150 := by decide

/-- Among all 150 reduced words of length 3, the straight paths are the farthest: every other word
    has strictly smaller cosh d. Turning always shortens. -/
theorem straight_farthest5 : ∀ w ∈ rwords 3, (word B5 w).a00 ≤ 7813 ∧
    ((word B5 w).a00 = 7813 ↔ w ∈ [[.pi,.pi,.pi],[.mi,.mi,.mi],[.pj,.pj,.pj],[.mj,.mj,.mj],[.pk,.pk,.pk],[.mk,.mk,.mk]]) := by decide

/-- Thomas rotation, exact (peel ratio 5): B_i B_j = L R with L a pure boost (symmetric, Lorentz)
    and R a rotation about k with cos = 65/97, sin = 72/97.  Scaled: Lz * Rz = 9409 * (B_i B_j). -/
def Lz5 : M4 := ⟨16393, 15132, 5820, 0, 15132, 14593, 4680, 0, 5820, 4680, 4225, 0, 0, 0, 0, 2425⟩
def Rz5 : M4 := ⟨97, 0, 0, 0, 0, 65, 72, 0, 0, -72, 65, 0, 0, 0, 0, 97⟩
theorem thomas5 : M4.mul Lz5 Rz5 = M4.smul 9409 (M4.mul (B5 .pi) (B5 .pj)) := by decide
theorem thomas5_boost : M4.tr Lz5 = Lz5 ∧ M4.mul (M4.tr Lz5) (M4.mul eta Lz5) = M4.smul 5880625 eta := by decide
theorem thomas5_rotation : M4.mul (M4.tr Rz5) Rz5 = M4.smul 9409 I4 ∧ pt Rz5 = [97, 0, 0, 0] := by decide
/-- So the product of two boosts is not a boost: it is not symmetric. -/
theorem two_boosts_not_boost5 : M4.tr (M4.mul (B5 .pi) (B5 .pj)) ≠ M4.mul (B5 .pi) (B5 .pj) := by decide

/-- Thomas rotation, exact (peel ratio 7): B_i B_j = L R with L a pure boost (symmetric, Lorentz)
    and R a rotation about k with cos = 175/337, sin = 288/337.  Scaled: Lz * Rz = 113569 * (B_i B_j). -/
def Lz7 : M4 := ⟨210625, 202200, 56616, 0, 202200, 196513, 50400, 0, 56616, 50400, 30625, 0, 0, 0, 0, 16513⟩
def Rz7 : M4 := ⟨337, 0, 0, 0, 0, 175, 288, 0, 0, -288, 175, 0, 0, 0, 0, 337⟩
theorem thomas7 : M4.mul Lz7 Rz7 = M4.smul 113569 (M4.mul (B7 .pi) (B7 .pj)) := by decide
theorem thomas7_boost : M4.tr Lz7 = Lz7 ∧ M4.mul (M4.tr Lz7) (M4.mul eta Lz7) = M4.smul 272679169 eta := by decide
theorem thomas7_rotation : M4.mul (M4.tr Rz7) Rz7 = M4.smul 113569 I4 ∧ pt Rz7 = [337, 0, 0, 0] := by decide
/-- So the product of two boosts is not a boost: it is not symmetric. -/
theorem two_boosts_not_boost7 : M4.tr (M4.mul (B7 .pi) (B7 .pj)) ≠ M4.mul (B7 .pi) (B7 .pj) := by decide

/-- Thomas half-angle in the peel coordinate: tan(theta/2) = sin/(1 + cos) = Gamma^2. -/
theorem thomas_half_angle : (72 : Int) * 9 = 4 * (97 + 65) ∧ (288 : Int) * 16 = 9 * (337 + 175) := by decide

/-! ## 4. Freeness for every length. Mod p (p = 5 or 7) each scaled boost is c * w w^T with w = (1, -sign, ...)
    a rank-one matrix; a product of rank-one matrices is rank one with a factor that is a product of
    dot products w_g . w_h, which is 2 (same step) or 1 (turn), and 0 only for a backtrack. -/

def wv : Dir → List Int
  | .pi => [1,-1,0,0] | .mi => [1,1,0,0] | .pj => [1,0,-1,0] | .mj => [1,0,1,0] | .pk => [1,0,0,-1] | .mk => [1,0,0,1]

def outer (m : Int) (c : Int) (f g : Dir) : M4 :=
  match wv f, wv g with
  | [f0,f1,f2,f3], [g0,g1,g2,g3] => M4.red m ⟨c * f0 * g0, c * f0 * g1, c * f0 * g2, c * f0 * g3, c * f1 * g0, c * f1 * g1, c * f1 * g2, c * f1 * g3, c * f2 * g0, c * f2 * g1, c * f2 * g2, c * f2 * g3, c * f3 * g0, c * f3 * g1, c * f3 * g2, c * f3 * g3⟩
  | _, _ => I4

/-- Reduction mod m respects products (entrywise: sums and products commute with taking residues). -/

theorem dot_emod5 (a1 b1 a2 b2 a3 b3 a4 b4 : Int) :
    (a1*b1 + a2*b2 + a3*b3 + a4*b4) % 5 = ((a1%5)*(b1%5) + (a2%5)*(b2%5) + (a3%5)*(b3%5) + (a4%5)*(b4%5)) % 5 := by
  have h1 := Int.mul_emod a1 b1 5; have h2 := Int.mul_emod a2 b2 5
  have h3 := Int.mul_emod a3 b3 5; have h4 := Int.mul_emod a4 b4 5
  omega

theorem red_mul5 (A B : M4) : M4.red 5 (M4.mul A B) = M4.red 5 (M4.mul (M4.red 5 A) (M4.red 5 B)) := by
  simp only [M4.red, M4.mul]
  simp only [M4.mk.injEq]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> apply dot_emod5

theorem dot_emod7 (a1 b1 a2 b2 a3 b3 a4 b4 : Int) :
    (a1*b1 + a2*b2 + a3*b3 + a4*b4) % 7 = ((a1%7)*(b1%7) + (a2%7)*(b2%7) + (a3%7)*(b3%7) + (a4%7)*(b4%7)) % 7 := by
  have h1 := Int.mul_emod a1 b1 7; have h2 := Int.mul_emod a2 b2 7
  have h3 := Int.mul_emod a3 b3 7; have h4 := Int.mul_emod a4 b4 7
  omega

theorem red_mul7 (A B : M4) : M4.red 7 (M4.mul A B) = M4.red 7 (M4.mul (M4.red 7 A) (M4.red 7 B)) := by
  simp only [M4.red, M4.mul]
  simp only [M4.mk.injEq]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> apply dot_emod7

/-- Invariant for peel ratio 5: mod 5 the word matrix is c * w_f w_g^T with c a nonzero residue,
    f the first step and g the last step. -/
def Inv5 (M : M4) (g : Dir) : Prop := ∃ c ∈ ([1,2,3,4] : List Int), ∃ f ∈ allDirs, M4.red 5 M = outer 5 c f g

theorem gen_red5 : ∀ d ∈ allDirs, M4.red 5 (B5 d) = outer 5 3 d d := by decide

/-- The finite closure step: rank-one state times a non-backtracking step stays rank one, nonzero. -/
theorem closure5 : ∀ c ∈ ([1,2,3,4] : List Int), ∀ f ∈ allDirs, ∀ g ∈ allDirs, ∀ h ∈ allDirs, h ≠ g.inv →
    ∃ c' ∈ ([1,2,3,4] : List Int), M4.red 5 (M4.mul (outer 5 c f g) (outer 5 3 h h)) = outer 5 c' f h := by decide

theorem outer_red5 : ∀ c ∈ ([1,2,3,4] : List Int), ∀ f ∈ allDirs, ∀ g ∈ allDirs, M4.red 5 (outer 5 c f g) = outer 5 c f g := by decide

theorem step5 (M : M4) (g h : Dir) (hM : Inv5 M g) (hh : h ≠ g.inv) : Inv5 (M4.mul M (B5 h)) h := by
  obtain ⟨c, hc, f, hf, hred⟩ := hM
  obtain ⟨c', hc', hcl⟩ := closure5 c hc f hf g (mem_allDirs g) h (mem_allDirs h) hh
  refine ⟨c', hc', f, hf, ?_⟩
  rw [red_mul5, hred, gen_red5 h (mem_allDirs h), hcl]

/-- Non-backtracking from g. -/
def RedFrom : Dir → List Dir → Prop
  | _, [] => True
  | g, h :: t => h ≠ g.inv ∧ RedFrom h t

def lastStep : Dir → List Dir → Dir
  | g, [] => g
  | _, h :: t => lastStep h t

theorem walk5 (l : List Dir) : ∀ (M : M4) (g : Dir), Inv5 M g → RedFrom g l →
    Inv5 (l.foldl (fun M d => M4.mul M (B5 d)) M) (lastStep g l) := by
  induction l with
  | nil => intro M g h _; exact h
  | cons h t ih =>
    intro M g hM hr
    exact ih _ h (step5 M g h hM hr.1) hr.2

theorem corner5 : ∀ c ∈ ([1,2,3,4] : List Int), ∀ f ∈ allDirs, ∀ g ∈ allDirs, (outer 5 c f g).a00 ≠ 0 := by decide

theorem mul_I4 (A : M4) : M4.mul I4 A = A := by
  cases A; simp only [M4.mul, I4]; simp

/-- MAIN (peel ratio 5): for every non-backtracking word of every length L >= 1, the scaled time
    coordinate 5^L cosh d(w) is not divisible by 5. -/
theorem time_not_div5 (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    (word B5 (g :: l)).a00 % 5 ≠ 0 := by
  have h0 : Inv5 (B5 g) g := ⟨3, by decide, g, mem_allDirs g, gen_red5 g (mem_allDirs g)⟩
  have hw := walk5 l (B5 g) g h0 hr
  obtain ⟨c, hc, f, hf, hred⟩ := hw
  have hword : word B5 (g :: l) = l.foldl (fun M d => M4.mul M (B5 d)) (B5 g) := by
    simp only [word, List.foldl_cons, mul_I4]
  rw [hword]
  have h1 := congrArg M4.a00 hred
  simp only [M4.red] at h1
  rw [h1]
  exact corner5 c hc f hf _ (mem_allDirs _)

theorem pow_emod5 (n : Nat) : ((5 : Int) ^ (n + 1)) % 5 = 0 := by
  rw [Int.pow_succ]; exact Int.mul_emod_left _ _

/-- No non-backtracking word returns to the origin: its time coordinate is never 5^L (cosh d = 1). -/
theorem no_return5 (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    (word B5 (g :: l)).a00 ≠ 5 ^ (l.length + 1) := by
  intro h; have := time_not_div5 g l hr; rw [h, pow_emod5] at this; exact this rfl

/-- No non-backtracking word is the identity: the boost group is free on the three steps. -/
theorem free5 (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    word B5 (g :: l) ≠ M4.smul (5 ^ (l.length + 1)) I4 := by
  intro h; apply no_return5 g l hr; rw [h]; simp [M4.smul, I4]

/-- Invariant for peel ratio 7: mod 7 the word matrix is c * w_f w_g^T with c a nonzero residue,
    f the first step and g the last step. -/
def Inv7 (M : M4) (g : Dir) : Prop := ∃ c ∈ ([1,2,3,4,5,6] : List Int), ∃ f ∈ allDirs, M4.red 7 M = outer 7 c f g

theorem gen_red7 : ∀ d ∈ allDirs, M4.red 7 (B7 d) = outer 7 4 d d := by decide

/-- The finite closure step: rank-one state times a non-backtracking step stays rank one, nonzero. -/
theorem closure7 : ∀ c ∈ ([1,2,3,4,5,6] : List Int), ∀ f ∈ allDirs, ∀ g ∈ allDirs, ∀ h ∈ allDirs, h ≠ g.inv →
    ∃ c' ∈ ([1,2,3,4,5,6] : List Int), M4.red 7 (M4.mul (outer 7 c f g) (outer 7 4 h h)) = outer 7 c' f h := by decide

theorem outer_red7 : ∀ c ∈ ([1,2,3,4,5,6] : List Int), ∀ f ∈ allDirs, ∀ g ∈ allDirs, M4.red 7 (outer 7 c f g) = outer 7 c f g := by decide

theorem step7 (M : M4) (g h : Dir) (hM : Inv7 M g) (hh : h ≠ g.inv) : Inv7 (M4.mul M (B7 h)) h := by
  obtain ⟨c, hc, f, hf, hred⟩ := hM
  obtain ⟨c', hc', hcl⟩ := closure7 c hc f hf g (mem_allDirs g) h (mem_allDirs h) hh
  refine ⟨c', hc', f, hf, ?_⟩
  rw [red_mul7, hred, gen_red7 h (mem_allDirs h), hcl]

theorem walk7 (l : List Dir) : ∀ (M : M4) (g : Dir), Inv7 M g → RedFrom g l →
    Inv7 (l.foldl (fun M d => M4.mul M (B7 d)) M) (lastStep g l) := by
  induction l with
  | nil => intro M g h _; exact h
  | cons h t ih =>
    intro M g hM hr
    exact ih _ h (step7 M g h hM hr.1) hr.2

theorem corner7 : ∀ c ∈ ([1,2,3,4,5,6] : List Int), ∀ f ∈ allDirs, ∀ g ∈ allDirs, (outer 7 c f g).a00 ≠ 0 := by decide

/-- MAIN (peel ratio 7): for every non-backtracking word of every length L >= 1, the scaled time
    coordinate 7^L cosh d(w) is not divisible by 7. -/
theorem time_not_div7 (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    (word B7 (g :: l)).a00 % 7 ≠ 0 := by
  have h0 : Inv7 (B7 g) g := ⟨4, by decide, g, mem_allDirs g, gen_red7 g (mem_allDirs g)⟩
  have hw := walk7 l (B7 g) g h0 hr
  obtain ⟨c, hc, f, hf, hred⟩ := hw
  have hword : word B7 (g :: l) = l.foldl (fun M d => M4.mul M (B7 d)) (B7 g) := by
    simp only [word, List.foldl_cons, mul_I4]
  rw [hword]
  have h1 := congrArg M4.a00 hred
  simp only [M4.red] at h1
  rw [h1]
  exact corner7 c hc f hf _ (mem_allDirs _)

theorem pow_emod7 (n : Nat) : ((7 : Int) ^ (n + 1)) % 7 = 0 := by
  rw [Int.pow_succ]; exact Int.mul_emod_left _ _

/-- No non-backtracking word returns to the origin: its time coordinate is never 7^L (cosh d = 1). -/
theorem no_return7 (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    (word B7 (g :: l)).a00 ≠ 7 ^ (l.length + 1) := by
  intro h; have := time_not_div7 g l hr; rw [h, pow_emod7] at this; exact this rfl

/-- No non-backtracking word is the identity: the boost group is free on the three steps. -/
theorem free7 (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    word B7 (g :: l) ≠ M4.smul (7 ^ (l.length + 1)) I4 := by
  intro h; apply no_return7 g l hr; rw [h]; simp [M4.smul, I4]

/-! ## 5. The knot side. Riley meridians a = [[s,1],[0,1/s]], b = [[s,0],[-v,1/s]], scaled by s so that
    every entry is a polynomial: A = s a, B = s b, A' = s a^-1, B' = s b^-1. The statements hold over
    every commutative ring, in particular for real s and v on the real peripheral curve. -/

structure M2 (R : Type) where
  a : R
  b : R
  c : R
  d : R

variable {R : Type} [Lean.Grind.CommRing R]

def M2.mul (X Y : M2 R) : M2 R := ⟨X.a*Y.a + X.b*Y.c, X.a*Y.b + X.b*Y.d, X.c*Y.a + X.d*Y.c, X.c*Y.b + X.d*Y.d⟩
def M2.sub (X Y : M2 R) : M2 R := ⟨X.a - Y.a, X.b - Y.b, X.c - Y.c, X.d - Y.d⟩

def rA (s : R) : M2 R := ⟨s*s, s, 0, 1⟩
def rB (s v : R) : M2 R := ⟨s*s, 0, -(v*s), 1⟩
def rAi (s : R) : M2 R := ⟨1, -s, 0, s*s⟩
def rBi (s v : R) : M2 R := ⟨1, 0, v*s, s*s⟩

/-- The scaled inverses are inverses: A A' = s^2 I and B B' = s^2 I. -/
theorem riley_inverses (s v : R) :
    (M2.mul (rA s) (rAi s)) = ⟨s*s, 0, 0, s*s⟩ ∧ (M2.mul (rB s v) (rBi s v)) = ⟨s*s, 0, 0, s*s⟩ := by
  simp only [M2.mul, rA, rAi, rB, rBi, M2.mk.injEq]; refine ⟨⟨?_,?_,?_,?_⟩,⟨?_,?_,?_,?_⟩⟩ <;> grind

/-- Each meridian has determinant 1 and trace s + 1/s (scaled: det s^2, trace s^2 + 1), and
    trace^2 - 4 det = (s^2 - 1)^2: for real s ≠ ±1 it is a boost of translation length 2 ln|s|. -/
theorem meridian_boost (s v : R) :
    (rA s).a * (rA s).d - (rA s).b * (rA s).c = s*s ∧
    (rB s v).a * (rB s v).d - (rB s v).b * (rB s v).c = s*s ∧
    ((rA s).a + (rA s).d) * ((rA s).a + (rA s).d) - 4 * (s*s) = (s*s - 1) * (s*s - 1) ∧
    (rB s v).a + (rB s v).d = (rA s).a + (rA s).d := by
  simp only [rA, rB]; refine ⟨?_,?_,?_,?_⟩ <;> grind

/-- Trefoil (2-bridge 3/1, W = b a): A W - W B = R3(s,v) * [[0, s], [s v, 0]],
    R3 = s^4 - s^2 v - s^2 + 1. The relation holds exactly on the Riley curve R3 = 0. -/
theorem trefoil_relation (s v : R) :
    let W := M2.mul (rB s v) (rA s)
    let D := M2.sub (M2.mul (rA s) W) (M2.mul W (rB s v))
    let R3 := s*s*s*s - s*s*v - s*s + 1
    D.a = 0 ∧ D.b = R3 * s ∧ D.c = R3 * (s * v) ∧ D.d = 0 := by
  simp only [M2.mul, M2.sub, rA, rB]; refine ⟨?_,?_,?_,?_⟩ <;> grind

/-- Figure-eight (2-bridge 5/3, W = b a^-1 b^-1 a): A W - W B = R4(s,v) * [[0, s^3], [s^3 v, 0]],
    R4 = s^2 v^2 + (3 s^2 - s^4 - 1) v + (3 s^2 - s^4 - 1). -/
theorem figure_eight_relation (s v : R) :
    let W := M2.mul (M2.mul (M2.mul (rB s v) (rAi s)) (rBi s v)) (rA s)
    let D := M2.sub (M2.mul (rA s) W) (M2.mul W (rB s v))
    let R4 := s*s*v*v + (3*s*s - s*s*s*s - 1)*v + (3*s*s - s*s*s*s - 1)
    D.a = 0 ∧ D.b = R4 * (s*s*s) ∧ D.c = R4 * (s*s*s*v) ∧ D.d = 0 := by
  simp only [M2.mul, M2.sub, rA, rB, rAi, rBi]; refine ⟨?_,?_,?_,?_⟩ <;> grind

/-- Trefoil longitude on its curve: with R3 = 0 the scaled longitude B A A B A'^4 = s^8 L is upper
    triangular with diagonal -s^2, -s^14, i.e. L has eigenvalues -s^-6, -s^6: a boost of length 12 ln s = 2|y|
    with y = -6x. -/
theorem trefoil_longitude (s v : R) (h : s*s*s*s - s*s*v - s*s + 1 = 0) :
    let A4 := M2.mul (M2.mul (rAi s) (rAi s)) (M2.mul (rAi s) (rAi s))
    let Lg := M2.mul (M2.mul (M2.mul (M2.mul (rB s v) (rA s)) (rA s)) (rB s v)) A4
    Lg.c = 0 ∧ Lg.a = -(s*s) ∧ Lg.d = -(s*s*s*s*s*s*s*s*s*s*s*s*s*s) := by
  simp only [M2.mul, rA, rB, rAi]; refine ⟨?_,?_,?_⟩ <;> grind

end PeelTrees

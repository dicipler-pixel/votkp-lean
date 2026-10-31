/-
  PeelTrees2.lean — Two Trees in One Ball, second file: the general peel ratio.
  Jeromie Beasley. Core Lean 4.34.1, no Mathlib, no sorry, no axioms beyond Lean's own,
  no native_decide. Standalone: the definitions it shares with PeelTrees.lean are repeated here.

  Contents
    A. Freeness for every peel ratio z with an odd divisor m > 1 (every z >= 2 that is not a power
       of 2), for every word length. With Q_u = 2z B_u (integer entries z^2+1, ±(z^2-1), 2z) one has
       Q_u = W_u + z E_u exactly over Int, W_u = w_u w_u^T. By induction over non-backtracking words,
       the word product equals 2^a W_{first,last} + z E. So (2z)^L cosh d(w) ≡ 2^a (mod m) for every
       m | z, which is not 0 when m is odd and m > 1. Hence no non-backtracking word returns to the
       origin and none is the identity.
    B. The Thomas rotation of two perpendicular steps for symbolic z: L R = B_i B_j with L a pure boost
       and R a rotation about k with cos = (1-t^2)/(1+t^2) = 4z(z^2+1)/(z^4+6z^2+1),
       sin = 2t/(1+t^2) = (z^2-1)^2/(z^4+6z^2+1), t = Gamma^2, Gamma = (z-1)/(z+1);
       the Pythagorean triple (1-t^2)^2 + (2t)^2 = (1+t^2)^2; tan(theta/2) = Gamma^2.
    C. Small exact facts: the figure-eight Riley polynomial in the variable c, its discriminant,
       and the Smith double step Gamma ⊕ Gamma = 2 Gamma/(1 + Gamma^2), 2/3 ⊕ 2/3 = 12/13.
-/

namespace PeelTrees2

set_option maxRecDepth 200000

/-! ## Integer 4 x 4 matrices -/

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

def M4.add (A B : M4) : M4 :=
  ⟨A.a00 + B.a00, A.a01 + B.a01, A.a02 + B.a02, A.a03 + B.a03,
   A.a10 + B.a10, A.a11 + B.a11, A.a12 + B.a12, A.a13 + B.a13,
   A.a20 + B.a20, A.a21 + B.a21, A.a22 + B.a22, A.a23 + B.a23,
   A.a30 + B.a30, A.a31 + B.a31, A.a32 + B.a32, A.a33 + B.a33⟩

def M4.tr (A : M4) : M4 := ⟨A.a00, A.a10, A.a20, A.a30, A.a01, A.a11, A.a21, A.a31, A.a02, A.a12, A.a22, A.a32, A.a03, A.a13, A.a23, A.a33⟩
def M4.smul (c : Int) (A : M4) : M4 := ⟨c * A.a00, c * A.a01, c * A.a02, c * A.a03, c * A.a10, c * A.a11, c * A.a12, c * A.a13, c * A.a20, c * A.a21, c * A.a22, c * A.a23, c * A.a30, c * A.a31, c * A.a32, c * A.a33⟩
def I4 : M4 := ⟨1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1⟩
def eta : M4 := ⟨1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1⟩

theorem mul_I4 (A : M4) : M4.mul I4 A = A := by
  cases A; simp only [M4.mul, I4]; simp

theorem smul_one (A : M4) : M4.smul 1 A = A := by
  cases A; simp only [M4.smul]; simp

theorem smul_smul (c d : Int) (A : M4) : M4.smul c (M4.smul d A) = M4.smul (c * d) A := by
  cases A; simp only [M4.smul, M4.mk.injEq]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> grind

/-- The one ring identity behind the induction:
    (c W + z E)(W' + z E') = c (W W') + z (c W E' + E W' + z E E'). -/
theorem ring_step (c z : Int) (W E W' E' : M4) :
    M4.mul (M4.add (M4.smul c W) (M4.smul z E)) (M4.add W' (M4.smul z E')) =
    M4.add (M4.smul c (M4.mul W W'))
      (M4.smul z (M4.add (M4.add (M4.smul c (M4.mul W E')) (M4.mul E W')) (M4.smul z (M4.mul E E')))) := by
  cases W; cases E; cases W'; cases E'
  simp only [M4.mul, M4.add, M4.smul, M4.mk.injEq]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> grind

/-! ## Step directions and the rank-one pieces -/

/-- The six step directions of Garrett's tree: +i, -i, +j, -j, +k, -k. -/
inductive Dir | pi | mi | pj | mj | pk | mk
deriving DecidableEq, Repr

def Dir.inv : Dir → Dir
  | .pi => .mi | .mi => .pi | .pj => .mj | .mj => .pj | .pk => .mk | .mk => .pk

def allDirs : List Dir := [.pi, .mi, .pj, .mj, .pk, .mk]
theorem mem_allDirs (d : Dir) : d ∈ allDirs := by cases d <;> decide

/-- The null vectors w_{±i} = (1, ∓1, 0, 0), w_{±j} = (1, 0, ∓1, 0), w_{±k} = (1, 0, 0, ∓1). -/
def w0 : Dir → Int := fun _ => 1
def w1 : Dir → Int | .pi => -1 | .mi => 1 | _ => 0
def w2 : Dir → Int | .pj => -1 | .mj => 1 | _ => 0
def w3 : Dir → Int | .pk => -1 | .mk => 1 | _ => 0

/-- W_{f,g} = w_f w_g^T. -/
def Wm (f g : Dir) : M4 :=
  ⟨w0 f * w0 g, w0 f * w1 g, w0 f * w2 g, w0 f * w3 g,
   w1 f * w0 g, w1 f * w1 g, w1 f * w2 g, w1 f * w3 g,
   w2 f * w0 g, w2 f * w1 g, w2 f * w2 g, w2 f * w3 g,
   w3 f * w0 g, w3 f * w1 g, w3 f * w2 g, w3 f * w3 g⟩

/-- Dot products of the null vectors: 2 for the same step, 0 for the backtrack, 1 for a turn. -/
def dotw (g h : Dir) : Int := w0 g * w0 h + w1 g * w1 h + w2 g * w2 h + w3 g * w3 h

theorem dotw_values : ∀ g ∈ allDirs, ∀ h ∈ allDirs,
    dotw g h = (if h = g then 2 else if h = g.inv then 0 else 1) := by decide

/-- The finite check: W_{f,g} W_{h,h} = (w_g . w_h) W_{f,h}, and for a non-backtracking step the
    factor is 2 (straight on) or 1 (turn). -/
theorem W_dot : ∀ f ∈ allDirs, ∀ g ∈ allDirs, ∀ h ∈ allDirs, h ≠ g.inv →
    M4.mul (Wm f g) (Wm h h) = M4.smul (if h = g then 2 else 1) (Wm f h) := by decide

theorem W_corner (f g : Dir) : (Wm f g).a00 = 1 := by
  cases f <;> cases g <;> rfl

/-! ## The scaled boosts Q_u = 2z B_u for symbolic z -/

/-- 2z times the boost of rapidity ln z along u: z^2+1 on the time and axis diagonal,
    ±(z^2-1) off the diagonal there, 2z on the other two spatial diagonals. -/
def Qz (z : Int) : Dir → M4
  | .pi => ⟨z*z+1, z*z-1, 0, 0, z*z-1, z*z+1, 0, 0, 0, 0, 2*z, 0, 0, 0, 0, 2*z⟩
  | .mi => ⟨z*z+1, -(z*z-1), 0, 0, -(z*z-1), z*z+1, 0, 0, 0, 0, 2*z, 0, 0, 0, 0, 2*z⟩
  | .pj => ⟨z*z+1, 0, z*z-1, 0, 0, 2*z, 0, 0, z*z-1, 0, z*z+1, 0, 0, 0, 0, 2*z⟩
  | .mj => ⟨z*z+1, 0, -(z*z-1), 0, 0, 2*z, 0, 0, -(z*z-1), 0, z*z+1, 0, 0, 0, 0, 2*z⟩
  | .pk => ⟨z*z+1, 0, 0, z*z-1, 0, 2*z, 0, 0, 0, 0, 2*z, 0, z*z-1, 0, 0, z*z+1⟩
  | .mk => ⟨z*z+1, 0, 0, -(z*z-1), 0, 2*z, 0, 0, 0, 0, 2*z, 0, -(z*z-1), 0, 0, z*z+1⟩

/-- The z-part: Q_u = W_u + z E_u. -/
def Ez (z : Int) : Dir → M4
  | .pi => ⟨z, z, 0, 0, z, z, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2⟩
  | .mi => ⟨z, -z, 0, 0, -z, z, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2⟩
  | .pj => ⟨z, 0, z, 0, 0, 2, 0, 0, z, 0, z, 0, 0, 0, 0, 2⟩
  | .mj => ⟨z, 0, -z, 0, 0, 2, 0, 0, -z, 0, z, 0, 0, 0, 0, 2⟩
  | .pk => ⟨z, 0, 0, z, 0, 2, 0, 0, 0, 0, 2, 0, z, 0, 0, z⟩
  | .mk => ⟨z, 0, 0, -z, 0, 2, 0, 0, 0, 0, 2, 0, -z, 0, 0, z⟩

theorem Q_split (z : Int) (u : Dir) : Qz z u = M4.add (Wm u u) (M4.smul z (Ez z u)) := by
  cases u <;> simp only [Qz, Ez, Wm, M4.add, M4.smul, w0, w1, w2, w3, M4.mk.injEq] <;>
    refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> grind

/-- Each Q_u is Lorentz up to the scale (2z)^2: Q^T eta Q = (2z)^2 eta, for every z. -/
theorem Q_lorentz (z : Int) (u : Dir) :
    M4.mul (M4.tr (Qz z u)) (M4.mul eta (Qz z u)) = M4.smul ((2*z)*(2*z)) eta := by
  cases u <;> simp only [Qz, eta, M4.mul, M4.tr, M4.smul, M4.mk.injEq] <;>
    refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> grind

/-- The backward step is the inverse: Q_u Q_{-u} = (2z)^2 I, for every z. -/
theorem Q_inverse (z : Int) (u : Dir) :
    M4.mul (Qz z u) (Qz z u.inv) = M4.smul ((2*z)*(2*z)) I4 := by
  cases u <;> simp only [Qz, Dir.inv, I4, M4.mul, M4.smul, M4.mk.injEq] <;>
    refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> grind

/-! ## The induction over non-backtracking words -/

/-- The scaled matrix of a word (applied left to right, starting at the identity). -/
def word (B : Dir → M4) (w : List Dir) : M4 := w.foldl (fun M d => M4.mul M (B d)) I4

/-- Non-backtracking from g. -/
def RedFrom : Dir → List Dir → Prop
  | _, [] => True
  | g, h :: t => h ≠ g.inv ∧ RedFrom h t

def lastStep : Dir → List Dir → Dir
  | g, [] => g
  | _, h :: t => lastStep h t

/-- The invariant: M = 2^a W_{f,g} + z E, with g the last step. -/
def InvZ (z : Int) (M : M4) (g : Dir) : Prop :=
  ∃ a : Nat, ∃ f : Dir, ∃ E : M4, M = M4.add (M4.smul ((2 : Int) ^ a) (Wm f g)) (M4.smul z E)

theorem invZ_of (z c : Int) (b : Nat) (hb : c = (2 : Int) ^ b) (f h : Dir) (X : M4) :
    InvZ z (M4.add (M4.smul c (Wm f h)) (M4.smul z X)) h := ⟨b, f, X, by rw [hb]⟩

theorem stepZ (z : Int) (M : M4) (g h : Dir) (hM : InvZ z M g) (hh : h ≠ g.inv) :
    InvZ z (M4.mul M (Qz z h)) h := by
  obtain ⟨a, f, E, rfl⟩ := hM
  rw [Q_split, ring_step, W_dot f (mem_allDirs f) g (mem_allDirs g) h (mem_allDirs h) hh, smul_smul]
  by_cases hg : h = g
  · exact invZ_of z _ (a + 1) (by rw [ite_eq_left hg, Int.pow_succ]) f h _
  · exact invZ_of z _ a (by rw [ite_eq_right hg, Int.mul_one]) f h _

theorem walkZ (z : Int) (l : List Dir) : ∀ (M : M4) (g : Dir), InvZ z M g → RedFrom g l →
    InvZ z (l.foldl (fun M d => M4.mul M (Qz z d)) M) (lastStep g l) := by
  induction l with
  | nil => intro M g h _; exact h
  | cons h t ih =>
    intro M g hM hr
    exact ih _ h (stepZ z M g h hM hr.1) hr.2

/-- MAIN FORM: for every integer z and every non-backtracking word g :: l, the product of the scaled
    boosts is 2^a W_{f, last} + z E for some a, some first-step vector f and some integer matrix E. -/
theorem word_form_general (z : Int) (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    ∃ a : Nat, ∃ f : Dir, ∃ E : M4,
      word (Qz z) (g :: l) = M4.add (M4.smul ((2 : Int) ^ a) (Wm f (lastStep g l))) (M4.smul z E) := by
  have h0 : InvZ z (Qz z g) g := ⟨0, g, Ez z g, by rw [Int.pow_zero, smul_one]; exact Q_split z g⟩
  have hword : word (Qz z) (g :: l) = l.foldl (fun M d => M4.mul M (Qz z d)) (Qz z g) := by
    simp only [word, List.foldl_cons, mul_I4]
  rw [hword]
  exact walkZ z l (Qz z g) g h0 hr

/-- The time entry: (2z)^L cosh d(w) = 2^a + z e for integers a >= 0, e. -/
theorem time_entry_general (z : Int) (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    ∃ a : Nat, ∃ e : Int, (word (Qz z) (g :: l)).a00 = (2 : Int) ^ a + z * e := by
  obtain ⟨a, f, E, hE⟩ := word_form_general z g l hr
  refine ⟨a, E.a00, ?_⟩
  rw [hE]; simp only [M4.add, M4.smul, W_corner, Int.mul_one]

/-- So (2z)^L cosh d(w) ≡ 2^a (mod m) for every divisor m of z. -/
theorem time_mod_general (z m : Int) (hm : m ∣ z) (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    ∃ a : Nat, m ∣ (word (Qz z) (g :: l)).a00 - (2 : Int) ^ a := by
  obtain ⟨a, e, he⟩ := time_entry_general z g l hr
  refine ⟨a, ?_⟩
  rw [he]
  have : (2 : Int) ^ a + z * e - (2 : Int) ^ a = z * e := by omega
  rw [this]
  exact Int.dvd_trans hm ⟨e, rfl⟩

/-- An odd m dividing 2x divides x. -/
theorem odd_dvd_of_dvd_two_mul (m x : Int) (hodd : m % 2 = 1) (h : m ∣ 2 * x) : m ∣ x := by
  obtain ⟨k, hk⟩ := h
  have hm : m = 2 * (m / 2) + 1 := by omega
  generalize m / 2 = j at hm
  refine ⟨x - j * k, ?_⟩
  subst hm
  grind

/-- An odd m > 1 never divides a power of 2. -/
theorem odd_not_dvd_pow_two (m : Int) (hodd : m % 2 = 1) (h1 : 1 < m) : ∀ a : Nat, ¬ m ∣ (2 : Int) ^ a := by
  intro a
  induction a with
  | zero =>
    intro h
    rw [Int.pow_zero] at h
    have := Int.le_of_dvd (by decide) h
    omega
  | succ n ih =>
    intro h
    rw [Int.pow_succ, Int.mul_comm] at h
    exact ih (odd_dvd_of_dvd_two_mul m _ hodd h)

/-- MAIN (every z with an odd divisor m > 1): for every non-backtracking word of every length L >= 1,
    the scaled time coordinate (2z)^L cosh d(w) is not divisible by m. -/
theorem time_not_dvd_general (z m : Int) (hm : m ∣ z) (hodd : m % 2 = 1) (h1 : 1 < m)
    (g : Dir) (l : List Dir) (hr : RedFrom g l) : ¬ m ∣ (word (Qz z) (g :: l)).a00 := by
  intro hdiv
  obtain ⟨a, ha⟩ := time_mod_general z m hm g l hr
  have h2 := Int.dvd_sub hdiv ha
  have : (word (Qz z) (g :: l)).a00 - ((word (Qz z) (g :: l)).a00 - (2 : Int) ^ a) = (2 : Int) ^ a := by omega
  rw [this] at h2
  exact odd_not_dvd_pow_two m hodd h1 a h2

theorem dvd_two_z_pow (z m : Int) (hm : m ∣ z) (n : Nat) : m ∣ (2 * z) ^ (n + 1) := by
  refine Int.dvd_trans hm ⟨(2 * z) ^ n * 2, ?_⟩
  rw [Int.pow_succ]
  grind

/-- No non-backtracking word returns to the origin: its time coordinate is never (2z)^L (cosh d = 1). -/
theorem no_return_general (z m : Int) (hm : m ∣ z) (hodd : m % 2 = 1) (h1 : 1 < m)
    (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    (word (Qz z) (g :: l)).a00 ≠ (2 * z) ^ (l.length + 1) := by
  intro h
  apply time_not_dvd_general z m hm hodd h1 g l hr
  rw [h]
  exact dvd_two_z_pow z m hm l.length

/-- No non-backtracking word is the identity: the three boosts of ratio z generate a free group. -/
theorem free_general (z m : Int) (hm : m ∣ z) (hodd : m % 2 = 1) (h1 : 1 < m)
    (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    word (Qz z) (g :: l) ≠ M4.smul ((2 * z) ^ (l.length + 1)) I4 := by
  intro h
  apply no_return_general z m hm hodd h1 g l hr
  rw [h]; simp [M4.smul, I4]

/-- Every n >= 1 that is not a power of 2 has an odd divisor m > 1. -/
theorem exists_odd_divisor (n : Nat) : 0 < n → (∀ k : Nat, n ≠ 2 ^ k) →
    ∃ m : Nat, m ∣ n ∧ m % 2 = 1 ∧ 1 < m := by
  induction n using Nat.strongRecOn with
  | ind n ih =>
    intro hn hp
    by_cases hpar : n % 2 = 1
    · refine ⟨n, Nat.dvd_refl n, hpar, ?_⟩
      have : n ≠ 1 := by have := hp 0; simpa using this
      omega
    · have hlt : n / 2 < n := by omega
      have hpos : 0 < n / 2 := by
        apply Classical.byContradiction; intro hc
        have : n = 1 := by omega
        exact hp 0 (by simp [this])
      have hp' : ∀ k : Nat, n / 2 ≠ 2 ^ k := by
        intro k hk; apply hp (k + 1); rw [Nat.pow_succ]; omega
      obtain ⟨m, hmd, hmo, hm1⟩ := ih (n / 2) hlt hpos hp'
      exact ⟨m, Nat.dvd_trans hmd ⟨2, by omega⟩, hmo, hm1⟩

/-- FREENESS FOR EVERY PEEL RATIO z >= 2 THAT IS NOT A POWER OF 2: no non-backtracking word returns
    to the origin and no non-backtracking word is the identity. -/
theorem free_not_pow_two (z : Nat) (hz : 2 ≤ z) (hp : ∀ k : Nat, z ≠ 2 ^ k)
    (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    (word (Qz (z : Int)) (g :: l)).a00 ≠ (2 * (z : Int)) ^ (l.length + 1) ∧
    word (Qz (z : Int)) (g :: l) ≠ M4.smul ((2 * (z : Int)) ^ (l.length + 1)) I4 := by
  obtain ⟨m, hmd, hmo, hm1⟩ := exists_odd_divisor z (by omega) hp
  have hmd' : (m : Int) ∣ (z : Int) := Int.natCast_dvd_natCast.mpr hmd
  have hmo' : (m : Int) % 2 = 1 := by omega
  have hm1' : 1 < (m : Int) := by omega
  exact ⟨no_return_general _ _ hmd' hmo' hm1' g l hr, free_general _ _ hmd' hmo' hm1' g l hr⟩

/-- Instances below the Schottky threshold z > 3 + 2 sqrt 2: peel ratios 3 and 5, and ratio 6 (odd divisor 3),
    are free for every word length. Powers of 2 (z = 2, 4, 8, ...) are not covered by this argument. -/
theorem free3 (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    word (Qz 3) (g :: l) ≠ M4.smul ((2 * 3) ^ (l.length + 1)) I4 :=
  free_general 3 3 (by decide) (by decide) (by decide) g l hr

theorem free6 (g : Dir) (l : List Dir) (hr : RedFrom g l) :
    word (Qz 6) (g :: l) ≠ M4.smul ((2 * 6) ^ (l.length + 1)) I4 :=
  free_general 6 3 (by decide) (by decide) (by decide) g l hr

/-- Consistency with PeelTrees.lean: Q_u at z = 5 and z = 7 is twice the boosts B5, B7 used there. -/
def boost (c s z : Int) : Dir → M4
  | .pi => ⟨c, s, 0, 0, s, c, 0, 0, 0, 0, z, 0, 0, 0, 0, z⟩
  | .mi => ⟨c, (-s), 0, 0, (-s), c, 0, 0, 0, 0, z, 0, 0, 0, 0, z⟩
  | .pj => ⟨c, 0, s, 0, 0, z, 0, 0, s, 0, c, 0, 0, 0, 0, z⟩
  | .mj => ⟨c, 0, (-s), 0, 0, z, 0, 0, (-s), 0, c, 0, 0, 0, 0, z⟩
  | .pk => ⟨c, 0, 0, s, 0, z, 0, 0, 0, 0, z, 0, s, 0, 0, c⟩
  | .mk => ⟨c, 0, 0, (-s), 0, z, 0, 0, 0, 0, z, 0, (-s), 0, 0, c⟩

theorem Q_five_seven : ∀ d ∈ allDirs, Qz 5 d = M4.smul 2 (boost 13 12 5 d) ∧ Qz 7 d = M4.smul 2 (boost 25 24 7 d) := by
  decide

/-! ## B. The Thomas rotation for symbolic z -/

def Dz (z : Int) : Int := z*z*z*z + 6*z*z + 1

/-- 4 z^2 D times the pure boost L to the point B_i B_j o. -/
def Lint (z : Int) : M4 :=
  ⟨(z*z+1)*(z*z+1)*Dz z, (z*z-1)*(z*z+1)*Dz z, 2*z*(z*z-1)*Dz z, 0,
   (z*z-1)*(z*z+1)*Dz z, 4*z*z*Dz z + (z*z-1)*(z*z-1)*((z*z+1)*(z*z+1)), 2*z*(z*z-1)*(z*z-1)*(z*z+1), 0,
   2*z*(z*z-1)*Dz z, 2*z*(z*z-1)*(z*z-1)*(z*z+1), 4*z*z*Dz z + 4*z*z*(z*z-1)*(z*z-1), 0,
   0, 0, 0, 4*z*z*Dz z⟩

/-- D times the rotation about k with cos = 4z(z^2+1)/D, sin = (z^2-1)^2/D. -/
def Rint (z : Int) : M4 :=
  ⟨Dz z, 0, 0, 0,
   0, 4*z*(z*z+1), (z*z-1)*(z*z-1), 0,
   0, -((z*z-1)*(z*z-1)), 4*z*(z*z+1), 0,
   0, 0, 0, Dz z⟩

/-- THOMAS, symbolic z, cleared of denominators: L R = D^2 Q_i Q_j, i.e. B_i B_j = (L/(4z^2 D)) (R/D). -/
theorem thomas_general (z : Int) :
    M4.mul (Lint z) (Rint z) = M4.smul (Dz z * Dz z) (M4.mul (Qz z .pi) (Qz z .pj)) := by
  simp only [Lint, Rint, Qz, Dz, M4.mul, M4.smul, M4.mk.injEq]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> grind

/-- L is a pure boost: symmetric and Lorentz, L^T eta L = (4 z^2 D)^2 eta. -/
theorem thomas_boost_general (z : Int) :
    M4.tr (Lint z) = Lint z ∧
    M4.mul (M4.tr (Lint z)) (M4.mul eta (Lint z)) = M4.smul ((4*z*z*Dz z) * (4*z*z*Dz z)) eta := by
  constructor
  · simp only [Lint, M4.tr]
  · simp only [Lint, Dz, eta, M4.mul, M4.tr, M4.smul, M4.mk.injEq]
    refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> grind

/-- R is a rotation fixing time: R^T R = D^2 I and R o = D o. -/
theorem thomas_rotation_general (z : Int) :
    M4.mul (M4.tr (Rint z)) (Rint z) = M4.smul (Dz z * Dz z) I4 ∧
    (Rint z).a00 = Dz z ∧ (Rint z).a10 = 0 ∧ (Rint z).a20 = 0 ∧ (Rint z).a30 = 0 := by
  refine ⟨?_, rfl, rfl, rfl, rfl⟩
  simp only [Rint, Dz, I4, M4.mul, M4.tr, M4.smul, M4.mk.injEq]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> grind

/-- The integer Pythagorean triple of the Thomas angle: (4z(z^2+1))^2 + ((z^2-1)^2)^2 = D^2. -/
theorem thomas_triple_int (z : Int) :
    (4*z*(z*z+1)) * (4*z*(z*z+1)) + ((z*z-1)*(z*z-1)) * ((z*z-1)*(z*z-1)) = Dz z * Dz z := by
  simp only [Dz]; grind

/-- Clearing t = Gamma^2 = (z-1)^2/(z+1)^2 by (z+1)^4: 1 - t^2, 2t, 1 + t^2 become
    8z(z^2+1), 2(z^2-1)^2, 2D. -/
theorem thomas_t_cleared (z : Int) :
    (z+1)*(z+1)*((z+1)*(z+1)) - (z-1)*(z-1)*((z-1)*(z-1)) = 8*z*(z*z+1) ∧
    2*((z-1)*(z-1))*((z+1)*(z+1)) = 2*((z*z-1)*(z*z-1)) ∧
    (z+1)*(z+1)*((z+1)*(z+1)) + (z-1)*(z-1)*((z-1)*(z-1)) = 2 * Dz z := by
  simp only [Dz]; refine ⟨?_, ?_, ?_⟩ <;> grind

/-- At z = 5 and z = 7 these are 32 and 8 times the exact matrices of PeelTrees.lean (thomas5, thomas7). -/
def Lz5 : M4 := ⟨16393, 15132, 5820, 0, 15132, 14593, 4680, 0, 5820, 4680, 4225, 0, 0, 0, 0, 2425⟩
def Rz5 : M4 := ⟨97, 0, 0, 0, 0, 65, 72, 0, 0, -72, 65, 0, 0, 0, 0, 97⟩
def Lz7 : M4 := ⟨210625, 202200, 56616, 0, 202200, 196513, 50400, 0, 56616, 50400, 30625, 0, 0, 0, 0, 16513⟩
def Rz7 : M4 := ⟨337, 0, 0, 0, 0, 175, 288, 0, 0, -288, 175, 0, 0, 0, 0, 337⟩
theorem thomas_matches_five_seven :
    Lint 5 = M4.smul 32 Lz5 ∧ Rint 5 = M4.smul 8 Rz5 ∧ Lint 7 = M4.smul 32 Lz7 ∧ Rint 7 = M4.smul 8 Rz7 := by
  decide

section Generic
variable {R : Type} [Lean.Grind.CommRing R]

/-- (1 - t^2, 2t, 1 + t^2) is a Pythagorean triple, over any commutative ring. -/
theorem thomas_triple (t : R) : (1 - t*t)*(1 - t*t) + (2*t)*(2*t) = (1 + t*t)*(1 + t*t) := by grind

/-! ## C. Small exact facts -/

/-- Figure-eight: with c s^2 = s^4 - 3 s^2 + 1, the Riley polynomial is s^2 (v^2 - c v - c). -/
theorem fig8_riley_c (s v c : R) (h : c*(s*s) = s*s*s*s - 3*(s*s) + 1) :
    s*s*(v*v - c*v - c) = s*s*v*v + (3*s*s - s*s*s*s - 1)*v + (3*s*s - s*s*s*s - 1) := by grind

/-- The discriminant of v^2 - c v - c is c^2 + 4c = c(c + 4). -/
theorem fig8_disc (c : R) : (-c)*(-c) - 4*(-c) = c*c + 4*c ∧ c*c + 4*c = c*(c + 4) := by
  constructor <;> grind

end Generic

/-! ## B over Rat: the identity with the rational entries themselves -/

structure MQ where
  a00 : Rat
  a01 : Rat
  a02 : Rat
  a03 : Rat
  a10 : Rat
  a11 : Rat
  a12 : Rat
  a13 : Rat
  a20 : Rat
  a21 : Rat
  a22 : Rat
  a23 : Rat
  a30 : Rat
  a31 : Rat
  a32 : Rat
  a33 : Rat
def MQ.mul (A B : MQ) : MQ :=
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

/-- Smith (peel) coordinate and Einstein addition, as in PeelTrees.lean. -/
def gam (z : Rat) : Rat := (z - 1) / (z + 1)
def oplus (x y : Rat) : Rat := (x + y) / (1 + x * y)

/-- The boosts of rapidity ln z along i and j, with C = cosh = (z^2+1)/(2z), S = sinh = (z^2-1)/(2z). -/
def Bqi (C S : Rat) : MQ := ⟨C, S, 0, 0, S, C, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1⟩
def Bqj (C S : Rat) : MQ := ⟨C, 0, S, 0, 0, 1, 0, 0, S, 0, C, 0, 0, 0, 0, 1⟩
/-- The pure boost to the point p = B_i B_j o = (C^2, SC, S, 0): [[gamma, u^T], [u, I + u u^T/(gamma+1)]]. -/
def Lq (C S : Rat) : MQ := ⟨C*C, S*C, S, 0, S*C, 1 + S*C*(S*C)/(C*C+1), S*C*S/(C*C+1), 0,
   S, S*C*S/(C*C+1), 1 + S*S/(C*C+1), 0, 0, 0, 0, 1⟩
/-- The rotation about k with cos = (1-t^2)/(1+t^2), sin = 2t/(1+t^2). -/
def Rq (t : Rat) : MQ := ⟨1, 0, 0, 0, 0, (1 - t*t)/(1 + t*t), 2*t/(1 + t*t), 0,
   0, -(2*t/(1 + t*t)), (1 - t*t)/(1 + t*t), 0, 0, 0, 0, 1⟩
/-- cosh^2(ln z) + 1 = (z^4 + 6z^2 + 1)/(4z^2). -/
theorem cosh_sq_add_one (z : Rat) (h1 : z ≠ 0) : (z*z+1)/(2*z) * ((z*z+1)/(2*z)) + 1 = (z*z*z*z + 6*z*z + 1) / (4*z*z) := by grind
/-- t = Gamma^2 = (z-1)^2/(z+1)^2. -/
theorem gam_sq (z : Rat) (h2 : z + 1 ≠ 0) : gam z * gam z = (z-1)*(z-1) / ((z+1)*(z+1)) := by unfold gam; grind
/-- 1 + t^2 = 2(z^4 + 6z^2 + 1)/(z+1)^4. -/
theorem one_add_t_sq (z : Rat) (h2 : z + 1 ≠ 0) : 1 + (z-1)*(z-1) / ((z+1)*(z+1)) * ((z-1)*(z-1) / ((z+1)*(z+1))) = 2 * (z*z*z*z + 6*z*z + 1) / ((z+1)*(z+1)*((z+1)*(z+1))) := by grind
/-- 1 - t^2 = 8z(z^2+1)/(z+1)^4. -/
theorem one_sub_t_sq (z : Rat) (h2 : z + 1 ≠ 0) : 1 - (z-1)*(z-1) / ((z+1)*(z+1)) * ((z-1)*(z-1) / ((z+1)*(z+1))) = 8 * z * (z*z + 1) / ((z+1)*(z+1)*((z+1)*(z+1))) := by grind
/-- z^4 + 6z^2 + 1 is not zero for z > 0. -/
theorem D_ne_zero (z : Rat) (hz : 0 < z) : z*z*z*z + 6*z*z + 1 ≠ 0 := by
  have hz2 : 0 < z * z := Rat.mul_pos hz hz
  have hz4 : 0 < z * z * (z * z) := Rat.mul_pos hz2 hz2
  grind
/-- cos theta = (1-t^2)/(1+t^2) = 4z(z^2+1)/(z^4+6z^2+1), t = Gamma^2. -/
theorem thomas_cos (z : Rat) (hz : 0 < z) :
    (1 - gam z * gam z * (gam z * gam z)) / (1 + gam z * gam z * (gam z * gam z)) = 4*z*(z*z+1) / (z*z*z*z + 6*z*z + 1) := by
  have h2 : z + 1 ≠ 0 := by grind
  have h22 : (z + 1) * (z + 1) ≠ 0 := by grind
  have h24 : (z + 1) * (z + 1) * ((z + 1) * (z + 1)) ≠ 0 := by grind
  have h3 := D_ne_zero z hz
  have h25 : 2 * (z*z*z*z + 6*z*z + 1) / ((z+1)*(z+1)*((z+1)*(z+1))) ≠ 0 := by
    intro h
    have : 2 * (z*z*z*z + 6*z*z + 1) = 2 * (z*z*z*z + 6*z*z + 1) / ((z+1)*(z+1)*((z+1)*(z+1))) * ((z+1)*(z+1)*((z+1)*(z+1))) := by grind
    rw [h] at this; grind
  rw [gam_sq z h2, one_add_t_sq z h2, one_sub_t_sq z h2]
  grind
/-- sin theta = 2t/(1+t^2) = (z^2-1)^2/(z^4+6z^2+1), t = Gamma^2. -/
theorem thomas_sin (z : Rat) (hz : 0 < z) :
    2 * (gam z * gam z) / (1 + gam z * gam z * (gam z * gam z)) = (z*z-1)*(z*z-1) / (z*z*z*z + 6*z*z + 1) := by
  have h2 : z + 1 ≠ 0 := by grind
  have h22 : (z + 1) * (z + 1) ≠ 0 := by grind
  have h24 : (z + 1) * (z + 1) * ((z + 1) * (z + 1)) ≠ 0 := by grind
  have h3 := D_ne_zero z hz
  have h25 : 2 * (z*z*z*z + 6*z*z + 1) / ((z+1)*(z+1)*((z+1)*(z+1))) ≠ 0 := by
    intro h
    have : 2 * (z*z*z*z + 6*z*z + 1) = 2 * (z*z*z*z + 6*z*z + 1) / ((z+1)*(z+1)*((z+1)*(z+1))) * ((z+1)*(z+1)*((z+1)*(z+1))) := by grind
    rw [h] at this; grind
  rw [gam_sq z h2, one_add_t_sq z h2]
  grind
/-- THOMAS, symbolic z over Rat (z > 0): L R = B_i B_j, with L the pure boost to B_i B_j o and R the
    rotation about k by the angle with cos = (1-t^2)/(1+t^2), sin = 2t/(1+t^2), t = Gamma(z)^2. -/
theorem thomas_rat (z : Rat) (hz : 0 < z) :
    MQ.mul (Lq ((z*z+1)/(2*z)) ((z*z-1)/(2*z))) (Rq (gam z * gam z)) =
    MQ.mul (Bqi ((z*z+1)/(2*z)) ((z*z-1)/(2*z))) (Bqj ((z*z+1)/(2*z)) ((z*z-1)/(2*z))) := by
  have h1 : z ≠ 0 := by grind
  have h3 := D_ne_zero z hz
  have h5 : 2 * z ≠ 0 := by grind
  have h6 : 4 * z * z ≠ 0 := by grind
  have h7 : (z*z*z*z + 6*z*z + 1) / (4*z*z) ≠ 0 := by grind
  simp only [MQ.mul, Lq, Rq, Bqi, Bqj, MQ.mk.injEq]
  rw [cosh_sq_add_one z h1, thomas_cos z hz, thomas_sin z hz]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> grind

/-- Half angle: sin/(1 + cos) = t for t >= 0; with t = Gamma^2 this is tan(theta/2) = Gamma^2. -/
theorem thomas_half_angle_t (t : Rat) (ht : 0 ≤ t) :
    (2*t/(1 + t*t)) / (1 + (1 - t*t)/(1 + t*t)) = t := by
  have h0 : 0 ≤ t * t := Rat.mul_nonneg ht ht
  have h1 : 1 + t*t ≠ 0 := by grind
  grind

/-- cos^2 + sin^2 = 1 for the Thomas angle written in t. -/
theorem thomas_unit_t (t : Rat) (ht : 0 ≤ t) :
    ((1 - t*t)/(1 + t*t)) * ((1 - t*t)/(1 + t*t)) + (2*t/(1 + t*t)) * (2*t/(1 + t*t)) = 1 := by
  have h0 : 0 ≤ t * t := Rat.mul_nonneg ht ht
  have h1 : 1 + t*t ≠ 0 := by grind
  grind

/-- Velocity versus Smith step: Gamma ⊕ Gamma = 2 Gamma/(1 + Gamma^2), and 2/3 ⊕ 2/3 = 12/13 = Gamma(25). -/
theorem oplus_self (g : Rat) : oplus g g = 2*g/(1 + g*g) := by
  unfold oplus; grind

theorem oplus_two_thirds : oplus (2/3) (2/3) = 12/13 ∧ gam 25 = 12/13 := by
  unfold oplus gam; constructor <;> grind

end PeelTrees2

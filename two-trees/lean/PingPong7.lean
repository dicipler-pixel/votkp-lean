/-
  PingPong7.lean — Two Trees in One Ball: the Schottky ping-pong at peel ratio z = 7, on the light cone.
  Jeromie Beasley. Core Lean 4.34.1, no Mathlib, no sorry, no native_decide.

  Setting. Vectors v = (t, x, y, z) over Int. The six steps u in {±i, ±j, ±k} act by the integer
  matrices 7 B_u (B_u the boost of rapidity ln 7 along u: cosh = 25/7, sinh = 24/7), e.g.
      7 B_{+i} (t, x, y, z) = (25 t + 24 x, 24 t + 25 x, 7 y, 7 z).
  comp u v is the coordinate of v along u (x, -x, y, -y, z, -z). A future null vector has
  t > 0 and t^2 = x^2 + y^2 + z^2. The cap of u on the light cone is
      X_u = { future null v : comp u v > 0 and t^2 < 2 (comp u v)^2 }      (comp u v / t > 1/sqrt 2),
  written without sqrt 2.

  Contents
    1. The steps are Lorentz up to the scale 49 and 7 B_{-u} . 7 B_u = 49 id.
    2. The six caps are pairwise disjoint.
    3. Ping-pong inclusion: for every u, 7 B_u maps every future null vector outside X_{-u} into X_u.
       Route: everything reduces to the plane (t, b) with b = comp u v. The nonlinear step is
       closed by explicit algebraic identities, e.g.
         2 (24t + 25b)^2 - (25t + 24b)^2 = 527 t^2 + 1200 t b + 674 b^2,
         432 (527 t^2 + 1200 t b + 674 b^2) = 41040 (t^2 - 2 b^2) + (432 t + 600 b)^2 + 13248 b^2,
       verified by grind, then linear reasoning over the monomials as atoms.
    4. The ping-pong lemma, abstractly (any letter type with an inversion, any action, any sets).
    5. Freeness: for every non-empty non-backtracking word w, the integer word map sends the null
       vector p0 = (3, 1, 2, 2) (outside every cap) into the cap of the first letter, hence it is not
       c . id for any c > 0; in particular B_w is not the identity.
-/

namespace PingPong7

/-! ## 1. Vectors, steps, caps -/

structure V4 where
  t : Int
  x : Int
  y : Int
  z : Int
deriving DecidableEq, Repr

inductive Dir | pi | mi | pj | mj | pk | mk
deriving DecidableEq, Repr

def Dir.inv : Dir → Dir
  | .pi => .mi | .mi => .pi | .pj => .mj | .mj => .pj | .pk => .mk | .mk => .pk

/-- The integer step 7 B_u. -/
def step : Dir → V4 → V4
  | .pi, ⟨t, x, y, z⟩ => ⟨25 * t + 24 * x, 24 * t + 25 * x, 7 * y, 7 * z⟩
  | .mi, ⟨t, x, y, z⟩ => ⟨25 * t - 24 * x, -24 * t + 25 * x, 7 * y, 7 * z⟩
  | .pj, ⟨t, x, y, z⟩ => ⟨25 * t + 24 * y, 7 * x, 24 * t + 25 * y, 7 * z⟩
  | .mj, ⟨t, x, y, z⟩ => ⟨25 * t - 24 * y, 7 * x, -24 * t + 25 * y, 7 * z⟩
  | .pk, ⟨t, x, y, z⟩ => ⟨25 * t + 24 * z, 7 * x, 7 * y, 24 * t + 25 * z⟩
  | .mk, ⟨t, x, y, z⟩ => ⟨25 * t - 24 * z, 7 * x, 7 * y, -24 * t + 25 * z⟩

/-- The coordinate of v along the step u. -/
def comp : Dir → V4 → Int
  | .pi, v => v.x | .mi, v => -v.x | .pj, v => v.y | .mj, v => -v.y | .pk, v => v.z | .mk, v => -v.z

/-- The Minkowski quadratic form t^2 - x^2 - y^2 - z^2. -/
def qf (v : V4) : Int := v.t * v.t - v.x * v.x - v.y * v.y - v.z * v.z

/-- Future null: t > 0 and t^2 = x^2 + y^2 + z^2. -/
def Null (v : V4) : Prop := 0 < v.t ∧ v.t * v.t = v.x * v.x + v.y * v.y + v.z * v.z

/-- The cap of u: future null with comp u v > 0 and t^2 < 2 (comp u v)^2. -/
def X (u : Dir) (v : V4) : Prop := Null v ∧ 0 < comp u v ∧ v.t * v.t < 2 * (comp u v * comp u v)

/-- Squares are nonnegative (core Lean has no `mul_self_nonneg` for Int under this name). -/
theorem msn (a : Int) : 0 ≤ a * a := by
  by_cases h : 0 ≤ a
  · exact Int.mul_nonneg h h
  · have h' : 0 ≤ -a := by omega
    have := Int.mul_nonneg h' h'
    have e : (-a) * (-a) = a * a := by grind
    omega

/-- Each step is Lorentz up to the scale 49: qf (7 B_u v) = 49 qf v, for every v. -/
theorem step_lorentz (u : Dir) (v : V4) : qf (step u v) = 49 * qf v := by
  obtain ⟨t, x, y, z⟩ := v
  cases u <;> simp only [step, qf] <;> grind

/-- 7 B_{-u} . 7 B_u = 49 id: the backward step is the inverse. -/
theorem step_inv (u : Dir) (v : V4) : step u.inv (step u v) = ⟨49 * v.t, 49 * v.x, 49 * v.y, 49 * v.z⟩ := by
  obtain ⟨t, x, y, z⟩ := v
  cases u <;> simp only [step, Dir.inv, V4.mk.injEq] <;> refine ⟨?_, ?_, ?_, ?_⟩ <;> grind

/-- The step along u, read in the plane (t, comp u): t' = 25 t + 24 b, b' = 24 t + 25 b. -/
theorem step_plane (u : Dir) (v : V4) :
    (step u v).t = 25 * v.t + 24 * comp u v ∧ comp u (step u v) = 24 * v.t + 25 * comp u v := by
  obtain ⟨t, x, y, z⟩ := v
  cases u <;> simp only [step, comp] <;> refine ⟨?_, ?_⟩ <;> grind

theorem comp_inv (u : Dir) (v : V4) : comp u.inv v = - comp u v := by
  cases u <;> simp only [comp, Dir.inv] <;> grind

/-! ## 2. The six caps are pairwise disjoint -/

theorem caps_disjoint (u w : Dir) (v : V4) (hu : X u v) (hw : X w v) : u = w := by
  obtain ⟨t, x, y, z⟩ := v
  obtain ⟨⟨ht, hn⟩, hu1, hu2⟩ := hu
  obtain ⟨_, hw1, hw2⟩ := hw
  have sx : 0 ≤ x * x := msn x
  have sy : 0 ≤ y * y := msn y
  have sz : 0 ≤ z * z := msn z
  cases u <;> cases w <;> simp only [comp] at hu1 hu2 hw1 hw2 hn ⊢ <;>
    first | rfl | (exfalso; grind)

/-! ## 3. The ping-pong inclusion -/

/-- The plane lemma: for t > 0 and (t, b) outside the backward cap ¬(-b > 0 ∧ t^2 < 2 b^2),
    the image (25t + 24b, 24t + 25b) has positive time, positive axis coordinate, and
    t'^2 < 2 b'^2. -/
theorem plane_core (t b : Int) (ht : 0 < t) (hn : ¬ (0 < -b ∧ t * t < 2 * ((-b) * (-b)))) :
    0 < 25 * t + 24 * b ∧ 0 < 24 * t + 25 * b ∧
    (25 * t + 24 * b) * (25 * t + 24 * b) < 2 * ((24 * t + 25 * b) * (24 * t + 25 * b)) := by
  have hq : 2 * ((24 * t + 25 * b) * (24 * t + 25 * b)) - (25 * t + 24 * b) * (25 * t + 24 * b)
      = 527 * (t * t) + 1200 * (t * b) + 674 * (b * b) := by grind
  have htt : 0 < t * t := Int.mul_pos ht ht
  by_cases hb : 0 ≤ b
  · -- the forward half: every term of 527 t^2 + 1200 t b + 674 b^2 is >= 0 and t^2 > 0
    have htb : 0 ≤ t * b := Int.mul_nonneg (Int.le_of_lt ht) hb
    have hbb : 0 ≤ b * b := msn b
    refine ⟨by omega, by omega, ?_⟩
    omega
  · -- the backward half: b < 0, so the hypothesis gives 2 b^2 <= t^2
    have hb' : b < 0 := by omega
    have hneg : (-b) * (-b) = b * b := by grind
    have h2 : 2 * (b * b) ≤ t * t := by
      have : ¬ (t * t < 2 * (b * b)) := fun h => hn ⟨by omega, by rw [hneg]; exact h⟩
      omega
    have hbb : 0 < b * b := by
      have := Int.mul_pos (show 0 < -b by omega) (show 0 < -b by omega)
      omega
    -- axis coordinate: if 24 t + 25 b <= 0 then (-24t - 25b)(24t - 25b) >= 0, i.e. 625 b^2 >= 576 t^2,
    -- against 1250 b^2 <= 625 t^2 and t^2 > 0
    have hx : 0 < 24 * t + 25 * b := by
      apply Classical.byContradiction
      intro hc
      have p := Int.mul_nonneg (show 0 ≤ -24 * t - 25 * b by omega) (show 0 ≤ 24 * t - 25 * b by omega)
      have e : (-24 * t - 25 * b) * (24 * t - 25 * b) = 625 * (b * b) - 576 * (t * t) := by grind
      omega
    -- the cap inequality: the sum-of-squares certificate
    have cert : 432 * (527 * (t * t) + 1200 * (t * b) + 674 * (b * b))
        = 41040 * (t * t - 2 * (b * b)) + (432 * t + 600 * b) * (432 * t + 600 * b) + 13248 * (b * b) := by
      grind
    have sq : 0 ≤ (432 * t + 600 * b) * (432 * t + 600 * b) := msn _
    refine ⟨by omega, hx, ?_⟩
    omega

/-- (comp u v)^2 <= t^2 on the null cone. -/
theorem comp_sq_le (u : Dir) (v : V4) (hv : Null v) : comp u v * comp u v ≤ v.t * v.t := by
  have sx := msn v.x
  have sy := msn v.y
  have sz := msn v.z
  have hn := hv.2
  cases u <;> simp only [comp] <;> grind

/-- The step preserves future null vectors. -/
theorem step_null (u : Dir) (v : V4) (hv : Null v) : Null (step u v) := by
  have hq := step_lorentz u v
  simp only [qf] at hq
  have hp := step_plane u v
  have hc := comp_sq_le u v hv
  obtain ⟨ht, hn⟩ := hv
  constructor
  · -- 25 t + 24 b > 0 because b^2 <= t^2
    rw [hp.1]
    apply Classical.byContradiction
    intro hneg
    have p := Int.mul_nonneg (show 0 ≤ -(25 * v.t + 24 * comp u v) by omega)
      (show 0 ≤ 25 * v.t - 24 * comp u v by omega)
    have e : (-(25 * v.t + 24 * comp u v)) * (25 * v.t - 24 * comp u v)
        = 576 * (comp u v * comp u v) - 625 * (v.t * v.t) := by grind
    have htt : 0 < v.t * v.t := Int.mul_pos ht ht
    omega
  · omega

/-- THE PING-PONG INCLUSION. For every step u, 7 B_u maps every future null vector that is not in
    the backward cap X_{-u} into the cap X_u. -/
theorem pingpong_step (u : Dir) (v : V4) (hv : Null v) (hout : ¬ X u.inv v) : X u (step u v) := by
  have hp := step_plane u v
  have hci := comp_inv u v
  have hn : ¬ (0 < -(comp u v) ∧ v.t * v.t < 2 * ((-(comp u v)) * (-(comp u v)))) := by
    intro ⟨h1, h2⟩
    exact hout ⟨hv, by rw [hci]; exact h1, by rw [hci]; exact h2⟩
  have core := plane_core v.t (comp u v) hv.1 hn
  refine ⟨step_null u v hv, ?_, ?_⟩
  · rw [hp.2]; exact core.2.1
  · rw [hp.1, hp.2]; exact core.2.2

/-! ## 4. The ping-pong lemma (abstract) -/

/-- Non-backtracking from g: the next letter is never the inverse of the current one. -/
def RedFrom {L : Type} (inv : L → L) : L → List L → Prop
  | _, [] => True
  | g, h :: t => h ≠ inv g ∧ RedFrom inv h t

/-- The word g_1 g_2 ... g_n acting on p: g_1 (g_2 (... (g_n p))). -/
def act {L α : Type} (f : L → α → α) : List L → α → α
  | [], p => p
  | g :: l, p => f g (act f l p)

/-- THE PING-PONG LEMMA. Letters L with an inversion, an action f, a domain D, and sets X a ⊆ D,
    pairwise disjoint, with f a carrying D \ X (inv a) into X a. Then for every base point p in D
    outside every X a, every non-empty non-backtracking word g :: l sends p into X g. -/
theorem pingpong {L α : Type} (inv : L → L) (f : L → α → α) (D : α → Prop) (X : L → α → Prop)
    (hdisj : ∀ a b v, X a v → X b v → a = b)
    (hXD : ∀ a v, X a v → D v)
    (hpp : ∀ a v, D v → ¬ X (inv a) v → X a (f a v))
    (p : α) (hp : D p) (hfree : ∀ a, ¬ X a p) :
    ∀ (l : List L) (g : L), RedFrom inv g l → X g (act f (g :: l) p) := by
  intro l
  induction l with
  | nil => intro g _; exact hpp g p hp (hfree _)
  | cons h t ih =>
    intro g hr
    obtain ⟨hne, hr'⟩ := hr
    have hin := ih h hr'
    apply hpp g _ (hXD h _ hin)
    intro hbad
    exact hne (hdisj h (inv g) _ hin hbad)

/-! ## 5. Freeness of the three boosts at z = 7 -/

/-- The base point (3, 1, 2, 2): future null (9 = 1 + 4 + 4) and in no cap (2 * 4 = 8 < 9). -/
def p0 : V4 := ⟨3, 1, 2, 2⟩

theorem p0_null : Null p0 := by simp only [Null, p0]; decide

theorem p0_free (u : Dir) : ¬ X u p0 := by
  cases u <;> simp only [X, Null, comp, p0] <;> decide

/-- Every non-empty non-backtracking word sends p0 into the cap of its first letter. -/
theorem word_in_cap (l : List Dir) (g : Dir) (hr : RedFrom Dir.inv g l) : X g (act step (g :: l) p0) :=
  pingpong Dir.inv step Null X caps_disjoint (fun _ _ h => h.1) pingpong_step p0 p0_null p0_free l g hr

/-- No positive multiple of p0 lies in a cap. -/
theorem scaled_p0_free (u : Dir) (c : Int) (hc : 0 < c) : ¬ X u ⟨c * 3, c * 1, c * 2, c * 2⟩ := by
  intro ⟨_, h1, h2⟩
  have hcc : 0 < c * c := Int.mul_pos hc hc
  cases u <;> simp only [comp] at h1 h2 <;> grind

/-- FREENESS. For every non-empty non-backtracking word over the six steps, the integer word map
    7^n B_w is not c . id for any c > 0 (it moves the null ray of p0). Taking c = 7^n: B_w ≠ id. -/
theorem word_ne_scalar (l : List Dir) (g : Dir) (hr : RedFrom Dir.inv g l) (c : Int) (hc : 0 < c) :
    act step (g :: l) p0 ≠ ⟨c * 3, c * 1, c * 2, c * 2⟩ := by
  intro h
  have := word_in_cap l g hr
  rw [h] at this
  exact scaled_p0_free g c hc this

theorem word_ne_id (l : List Dir) (g : Dir) (hr : RedFrom Dir.inv g l) :
    act step (g :: l) p0 ≠ ⟨7 ^ (l.length + 1) * 3, 7 ^ (l.length + 1) * 1,
                            7 ^ (l.length + 1) * 2, 7 ^ (l.length + 1) * 2⟩ :=
  word_ne_scalar l g hr _ (Int.pow_pos (by decide))

end PingPong7

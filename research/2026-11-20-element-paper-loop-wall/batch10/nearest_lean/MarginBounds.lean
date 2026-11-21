import Std

namespace VOTKP.NearestPair
structure Face where
  a : Rat
  ua : Rat
  b : Rat
  ub : Rat

def g (a b : Rat) : Rat := (b-a)/(b+a)
def power (a b : Rat) : Rat := (g a b)^2

/-- Full independent intervals for the two energies of one opening. -/
def Admits (f : Face) (a b : Rat) : Prop :=
  f.a-f.ua≤a ∧ a≤f.a+f.ua ∧ f.b-f.ub≤b ∧ b≤f.b+f.ub

private theorem gMono {a b c d : Rat} (hc : 0<c) (hb : 0<b)
    (hca : c≤a) (hbd : b≤d) : g a b ≤ g c d := by
  have X := Rat.mul_le_mul_of_nonneg_right hca (show 0≤b by grind)
  have Y := Rat.mul_le_mul_of_nonneg_left hbd (show 0≤a by grind)
  have ha : 0<b+a := by grind
  have hd : 0<d+c := by grind
  have h₁ : g a b * (b+a)=b-a := Rat.div_mul_cancel (by grind)
  have h₂ : g c d * (d+c)=d-c := Rat.div_mul_cancel (by grind)
  have hh := Rat.mul_pos ha hd
  by_cases h : g a b ≤ g c d
  · exact h
  have hp := Rat.mul_lt_mul_of_pos_right (show g c d < g a b by grind) hh
  have e₁ : g a b * ((b+a)*(d+c)) = (b-a)*(d+c) := by
    rw [← Rat.mul_assoc, h₁]
  have e₂ : g c d * ((b+a)*(d+c)) = (d-c)*(b+a) := by
    rw [Rat.mul_comm (b+a) (d+c), ← Rat.mul_assoc, h₂]
  rw [e₁,e₂] at hp
  have diff : (b-a)*(d+c) - (d-c)*(b+a) = 2*(c*b-a*d) := by grind
  grind

private theorem sqMono {x y : Rat} (hx : 0≤x) (hxy : x≤y) : x^2≤y^2 := by
  have h₁ := Rat.mul_le_mul_of_nonneg_left hxy hx
  have h₂ := Rat.mul_le_mul_of_nonneg_right hxy (show 0≤y by grind)
  grind

def sqLo (l u : Rat) := if 0≤l then l^2 else if u≤0 then u^2 else 0
def sqHi (l u : Rat) := if l^2≤u^2 then u^2 else l^2

private theorem sqBounds {l x u : Rat} (h : l≤x) (h' : x≤u) :
    sqLo l u≤x^2 ∧ x^2≤sqHi l u := by
  have a : 0≤l → l^2≤x^2 := fun hpos => sqMono hpos h
  have b : u≤0 → u^2≤x^2 := by
    intro hneg
    have := sqMono (x := -u) (y := -x) (by grind) (by grind)
    grind
  have c : 0≤x → x^2≤u^2 := fun hpos => sqMono hpos h'
  have d : x≤0 → x^2≤l^2 := by
    intro hneg
    have := sqMono (x := -x) (y := -l) (by grind) (by grind)
    grind
  have hz := Rat.mul_nonneg (a:=x) (b:=x)
  have hn := Rat.mul_nonneg (a:=-x) (b:=-x)
  unfold sqLo sqHi
  grind (splits := 12)

def gLo (f : Face) := g (f.a+f.ua) (f.b-f.ub)
def gHi (f : Face) := g (f.a-f.ua) (f.b+f.ub)
def pLo (f : Face) := sqLo (gLo f) (gHi f)
def pHi (f : Face) := sqHi (gLo f) (gHi f)
def valid (f : Face) : Bool := decide (0<f.a-f.ua ∧ 0<f.b-f.ub ∧ 0≤f.ua ∧ 0≤f.ub)

theorem powerBounds {f : Face} (v : valid f = true) {a b : Rat} (h : Admits f a b) :
    pLo f ≤ power a b ∧ power a b ≤ pHi f := by
  simp [valid] at v
  obtain ⟨ha, hA, hb, hB⟩ := h
  apply sqBounds
  · apply gMono (show 0<a by grind) (show 0<f.b-f.ub by grind) hA hb
  · apply gMono (show 0<f.a-f.ua by grind) (show 0<b by grind) ha hB

structure OpeningPair where
  core : Nat
  leftZ : Nat
  a : Face
  b : Face

def target (p : OpeningPair) : Bool := p.core == 2 && p.leftZ == 6
def low (p : OpeningPair) := pLo p.a + pLo p.b - 1
def high (p : OpeningPair) := pHi p.a + pHi p.b - 1

/-- Exact rational separating cuts, chosen inside the observed open gap. -/
def certify (p : OpeningPair) : Bool :=
  valid p.a && valid p.b &&
  (if target p then decide (0 < low p ∧ high p < 31/10000)
   else decide (high p < -(37/1000) ∨ 37/1000 < low p))

def AdmissibleMargin (p : OpeningPair) (m : Rat) : Prop :=
  ∃ a b c d : Rat, Admits p.a a b ∧ Admits p.b c d ∧ m = power a b + power c d - 1

theorem certifiedCut {p : OpeningPair} (ok : certify p = true) {m : Rat}
    (hm : AdmissibleMargin p m) :
    (target p = true → m.abs < 31/10000) ∧ (target p = false → 37/1000 < m.abs) := by
  obtain ⟨a,b,c,d,h₁,h₂,rfl⟩ := hm
  simp only [certify, Bool.and_eq_true] at ok
  have p₁ := powerBounds ok.1.1 h₁
  have p₂ := powerBounds ok.1.2 h₂
  constructor
  · intro h
    have chk := ok.2
    simp [h, low, high] at chk
    rw [Rat.abs_of_nonneg (by grind)]
    grind
  · intro h
    have chk := ok.2
    simp [h, low, high] at chk
    by_cases hn : power a b + power c d - 1 ≤ 0
    · rw [Rat.abs_of_nonpos hn]; grind
    · rw [Rat.abs_of_nonneg (by grind)]; grind

/-- Simultaneous arbitrary realizations of both energy boxes preserve this strict ranking. -/
theorem nearestFromCuts {p q : OpeningPair} (hp : certify p = true) (hq : certify q = true)
    (tp : target p = true) (tq : target q = false) {m n : Rat}
    (hm : AdmissibleMargin p m) (hn : AdmissibleMargin q n) : m.abs < n.abs := by
  have lo := (certifiedCut hp hm).1 tp
  have hi := (certifiedCut hq hn).2 tq
  grind

end VOTKP.NearestPair

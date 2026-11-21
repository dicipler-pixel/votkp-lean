import Std

namespace ElementPaper.XenonContrast


abbrev Reading := Rat × Rat

def lo (x : Reading) := x.1 - x.2
def hi (x : Reading) := x.1 + x.2
def admits (x : Reading) (v : Rat) := lo x ≤ v ∧ v ≤ hi x

structure Window where
  first : Reading
  second : Reading
  third : Reading
  fifth : Reading

def allows (w : Window) (a b c e : Rat) :=
  admits w.first a ∧ admits w.second b ∧ admits w.third c ∧ admits w.fifth e

private theorem productMono {x y x' y' : Rat} (hx : 0≤x) (hY : 0≤y')
    (hX : x≤x') (hy : y≤y') : x*y ≤ x'*y' := by
  have h := Rat.mul_le_mul_of_nonneg_left hy hx
  have k := Rat.mul_le_mul_of_nonneg_right hX hY
  grind

private theorem squareMono {x y : Rat} (hx : 0≤x) (hxy : x≤y) : x*x ≤ y*y :=
  productMono hx (by grind) hxy hxy

/-- Compute x⁸ by repeated squaring for the ordered rational proof. -/
def oct (x : Rat) := let s := x*x; let t := s*s; t*t

theorem octIsEighthPower (x : Rat) : oct x = x^8 := by
  simp only [oct]
  grind

private theorem octMono {x y : Rat} (hx : 0≤x) (h : x≤y) : oct x ≤ oct y := by
  have h2 := squareMono hx h
  have p2 := Rat.mul_nonneg hx hx
  have h4 := squareMono p2 h2
  exact squareMono (Rat.mul_nonneg p2 p2) h4

private theorem octNonnegative {x : Rat} (h : 0≤x) : 0 ≤ oct x := by
  have a := Rat.mul_nonneg h h
  have b := Rat.mul_nonneg a a
  exact Rat.mul_nonneg b b

def valid (w : Window) : Bool := decide
  (0<lo w.first ∧ 0<lo w.second ∧ 0<lo w.third ∧ 0<lo w.fifth ∧ hi w.first < lo w.fifth)

def positiveCorner (w : Window) := lo w.second * lo w.second - hi w.first * hi w.third

def scaledCorner (w : Window) := decide
  (oct (hi w.first*hi w.third) * hi w.first < oct (lo w.second*lo w.second) * lo w.fifth)

private theorem levelsBounded {w : Window} (v : valid w = true) {a b c e : Rat}
    (h : allows w a b c e) :
    0 < a ∧ 0 < b ∧ 0 < c ∧ a < e ∧
    a*c ≤ hi w.first*hi w.third ∧ lo w.second*lo w.second ≤ b*b := by
  simp only [valid, decide_eq_true_eq] at v
  rcases h with ⟨⟨a0,a1⟩,⟨b0,_⟩,⟨c0,c1⟩,⟨e0,_⟩⟩
  have prod := productMono (show 0≤a by grind) (show 0≤hi w.third by grind) a1 c1
  have sq := squareMono (show 0≤lo w.second by grind) b0
  grind

/-- This strict lower bound makes the real logarithmic numerator positive. -/
theorem positiveThroughout {w : Window} (v : valid w = true) (corner : 0 < positiveCorner w)
    {a b c e : Rat} (h : allows w a b c e) : 0<a ∧ a<e ∧ a*c < b*b := by
  have bnd := levelsBounded v h
  dsimp [positiveCorner] at corner
  grind

/-- Sufficient condition for D > −1/8 under any positive four-step total variation.
The logarithmic implication is set out in the accompanying note. -/
theorem scaledThroughout {w : Window} (v : valid w = true) (corner : scaledCorner w = true)
    {a b c e : Rat} (h : allows w a b c e) :
    0<a ∧ a<e ∧ oct (a*c)*a < oct (b*b)*e := by
  have bnd := levelsBounded v h
  simp only [valid,decide_eq_true_eq] at v
  simp only [scaledCorner,decide_eq_true_eq] at corner
  rcases h with ⟨⟨a0,a1⟩,_,_,⟨e0,_⟩⟩
  have hprod := Rat.mul_nonneg (show 0≤a by grind) (show 0≤c by grind)
  have hsquare := Rat.mul_nonneg (show 0≤lo w.second by grind) (show 0≤lo w.second by grind)
  have lhs := productMono (octNonnegative hprod) (show 0≤hi w.first by grind)
    (octMono hprod bnd.2.2.2.2.1) a1
  have rhs := productMono (octNonnegative hsquare) (show 0≤e by grind)
    (octMono hsquare bnd.2.2.2.2.2) e0
  grind

-- Four inputs per row. The fourth energy in the five-energy data window can be
-- arbitrary positive, because the variation lower bound uses only endpoints.
def cerium : Window := ⟨(20.1974,0.0025),(36.906,0.009),(65.55,0.25),(91,2)⟩
def praseodymium : Window := ⟨(38.981,0.025),(57.53,0.05),(82,4),(112,6)⟩
def neodymium : Window := ⟨(60,0.3),(84,4),(99,5),(136,7)⟩

theorem threeWindowsVerified :
    [cerium,praseodymium,neodymium].all valid = true ∧
    [cerium,praseodymium,neodymium].all scaledCorner = true ∧
    positiveCorner cerium = 32.235189 ∧ positiveCorner neodymium = 128.8 ∧
    positiveCorner praseodymium = -50.5656 := by decide +kernel

theorem ceriumPositive {a b c e : Rat} (h : allows cerium a b c e) :
    0<a ∧ a<e ∧ a*c < b*b :=
  positiveThroughout (by decide +kernel) (by decide +kernel) h

theorem neodymiumPositive {a b c e : Rat} (h : allows neodymium a b c e) :
    0<a ∧ a<e ∧ a*c < b*b :=
  positiveThroughout (by decide +kernel) (by decide +kernel) h

theorem praseodymiumCanChangeSign :
    allows praseodymium 39.006 57.48 86 106 ∧
    (57.48:Rat)^2 < 39.006*86 ∧
    allows praseodymium 38.956 57.58 78 118 ∧
    (38.956:Rat)*78 < 57.58^2 := by
  dsimp [allows,admits,lo,hi,praseodymium]
  decide +kernel

theorem scaledForAllThree {w : Window} (hw : w ∈ [cerium,praseodymium,neodymium])
    {a b c e : Rat} (h : allows w a b c e) :
    0<a ∧ a<e ∧ (a*c)^8*a < (b*b)^8*e := by
  have ok := threeWindowsVerified
  have base := scaledThroughout (List.all_eq_true.mp ok.1 w hw) (List.all_eq_true.mp ok.2.1 w hw) h
  simpa only [octIsEighthPower] using base

-- Exact rational forms of the frozen binary64 centres printed by the predictor.
def centerZero : Rat := 868737452360385/18014398509481984
def centerTwo : Rat := -6775490280607259/18014398509481984

theorem fixedCenters : (centerZero + centerTwo)/2 < -1/8 ∧ centerTwo < -1/8 ∧ centerTwo < centerZero := by
  decide +kernel

/-- For such contrasts center zero is strictly closer than center two, irrespective of center one. -/
theorem twoCannotWin {d : Rat} (h : -(1:Rat)/8 < d) :
    (d-centerZero).abs < (d-centerTwo).abs := by
  have h0 := fixedCenters
  rw [Rat.abs_of_nonneg (show 0≤d-centerTwo by grind)]
  by_cases hz : 0≤d-centerZero
  · rw [Rat.abs_of_nonneg hz]; grind
  · rw [Rat.abs_of_nonpos (show d-centerZero≤0 by grind)]; grind

#print axioms octIsEighthPower
#print axioms positiveThroughout
#print axioms scaledThroughout
#print axioms threeWindowsVerified
#print axioms ceriumPositive
#print axioms neodymiumPositive
#print axioms praseodymiumCanChangeSign
#print axioms scaledForAllThree
#print axioms fixedCenters
#print axioms twoCannotWin

end ElementPaper.XenonContrast

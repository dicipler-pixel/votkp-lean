/- Exact algebra of the oblique two-face comparison.
   x,y are signed reflections, c is the cosine of the comparison-disk angle.
   The note derives geometry and transfer traces. This file checks their
   cleared polynomial discriminators over the rationals. -/
namespace ElementPaper.ObliqueFaces

def disk (x y c : Rat) := c*c - 2*x*y*c + x*x + y*y - 1

def scale (x y : Rat) := (1-x*x)*(1-y*y)

def word (x y c : Rat) := x*x*y*y*(1-c*c) - scale x y

/-- Cleared discriminant for the full two-face matrix product. -/
theorem faceProductDiscriminant (x y c : Rat) :
    (c-x*y)*(c-x*y) - scale x y = disk x y c := by
  unfold scale disk
  grind

theorem rightAngle (x y : Rat) : disk x y 0 = word x y 0 := by
  unfold disk word scale
  grind

theorem diskSignOfTilt (x y c : Rat) :
    disk x y (-c) - disk x y c = 4*x*y*c := by
  unfold disk
  grind

theorem commutatorEvenTilt (x y c : Rat) : word x y (-c) = word x y c := by
  unfold word
  grind

theorem bothClockSigns (x y c : Rat) :
    disk (-x) (-y) c = disk x y c ∧ word (-x) (-y) c = word x y c := by
  unfold disk word scale
  constructor <;> grind

/-- 9 and 4 are unequal faces whose right-angle pair is marginal. -/
theorem rationalSignedControl :
    disk (4/5) (3/5) 0 = 0 ∧
    disk (4/5) (3/5) (3/5) = -27/125 ∧
    disk (4/5) (3/5) (-3/5) = 117/125 ∧
    word (4/5) (3/5) (3/5) = -1296/15625 ∧
    word (4/5) (3/5) (-3/5) = -1296/15625 := by
  unfold disk word scale
  grind

def be : Rat := (153896205 - 18211150) / (153896205 + 18211150)
def rb : Rat := (18305886 - 4356865) / (18305886 + 4356865)

/-- At a small acute tilt, the two calibrated inputs produce opposite signs. -/
theorem beRbAcuteTilt :
    disk be rb (1/1000) < 0 ∧ 0 < word be rb (1/1000) ∧
    0 < be - rb*(1/1000) ∧ 0 < rb - be*(1/1000) := by
  unfold disk word scale be rb
  grind

/-- A universal oblique equivalence is false even with valid forward faces,
    a legitimate cosine and a positive forward-sector intersection. -/
theorem noUniversalObliqueEquivalence :
    ¬ (∀ x y c : Rat, 0 < x → x < 1 → 0 < y → y < 1 →
       -1 < c → c < 1 → 0 < x-c*y → 0 < y-c*x →
       (0 < disk x y c ↔ 0 < word x y c)) := by
  intro hall
  have he := hall (4/5) (3/5) (-3/5) (by grind) (by grind)
    (by grind) (by grind) (by grind) (by grind) (by grind) (by grind)
  have hw : ¬ (0 < word (4/5) (3/5) (-3/5)) := by unfold word scale; grind
  exact hw (he.mp (by unfold disk; grind))


/-- Rational two-by-two matrices for the trace construction. -/
structure Mat where
  a : Rat
  b : Rat
  c : Rat
  d : Rat

def mul (p q : Mat) : Mat :=
  ⟨p.a*q.a+p.b*q.c, p.a*q.b+p.b*q.d, p.c*q.a+p.d*q.c, p.c*q.b+p.d*q.d⟩

def det (p : Mat) : Rat := p.a*p.d-p.b*p.c
def tr (p : Mat) : Rat := p.a+p.d
def normal (t u v : Rat) : Mat := ⟨u, t+v, v-t, -u⟩
def E : Mat := ⟨1, 0, 0, -1⟩

theorem normalDet (t u v : Rat) (h : u*u+v*v-t*t=1) :
    det (normal t u v) = -1 := by
  unfold det normal
  dsimp
  grind

theorem normalTraceProduct (t u v T U V : Rat) :
    tr (mul (normal t u v) (normal T U V)) = 2*(u*U + v*V - t*T) := by
  unfold tr mul normal
  dsimp
  grind

theorem properFactorization (p q : Mat) :
    mul (mul p E) (mul E q) = mul p q := by
  cases p
  cases q
  simp [mul, E]
  grind

theorem bothStagesProper (p q : Mat) (hp : det p = -1) (hq : det q = -1) :
    det (mul p E) = 1 ∧ det (mul E q) = 1 := by
  simp [det, mul, E] at *
  constructor <;> grind

theorem commutatorTrace (p q u v w : Rat) (hs : p*q = 1) (hb : u*w-v*v = 1) :
    let A : Mat := ⟨p,0,0,q⟩
    let B : Mat := ⟨u,v,v,w⟩
    let Ai : Mat := ⟨q,0,0,p⟩
    let Bi : Mat := ⟨w,-v,-v,u⟩
    tr (mul (mul A B) (mul Ai Bi)) = 2-(p-q)*(p-q)*v*v := by
  dsimp [tr, mul]
  grind

end ElementPaper.ObliqueFaces
#print axioms ElementPaper.ObliqueFaces.faceProductDiscriminant
#print axioms ElementPaper.ObliqueFaces.rightAngle
#print axioms ElementPaper.ObliqueFaces.diskSignOfTilt
#print axioms ElementPaper.ObliqueFaces.commutatorEvenTilt
#print axioms ElementPaper.ObliqueFaces.bothClockSigns
#print axioms ElementPaper.ObliqueFaces.rationalSignedControl
#print axioms ElementPaper.ObliqueFaces.beRbAcuteTilt
#print axioms ElementPaper.ObliqueFaces.noUniversalObliqueEquivalence
#print axioms ElementPaper.ObliqueFaces.normalDet
#print axioms ElementPaper.ObliqueFaces.normalTraceProduct
#print axioms ElementPaper.ObliqueFaces.properFactorization
#print axioms ElementPaper.ObliqueFaces.bothStagesProper
#print axioms ElementPaper.ObliqueFaces.commutatorTrace

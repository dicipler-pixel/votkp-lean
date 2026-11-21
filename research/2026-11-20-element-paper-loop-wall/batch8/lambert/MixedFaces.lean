/- Mixed-face identities for the rational arithmetic layer of the element atlas.
   A and B denote the two squared reflections. Geometry is derived in mixed_faces.md. -/
namespace ElementPaper.MixedFaces

def refl (z : Rat) : Rat := (z - 1) / (z + 1)

def margin (x y : Rat) : Rat := refl x * refl x + refl y * refl y - 1

/-- Each cleared sinh²-product comparison is a sum of the two reflected powers. -/
theorem clearedMargin (a b : Rat) :
    a * b - (1 - a) * (1 - b) = a + b - 1 := by grind

/-- With the physical upper bounds, the denominator is positive. -/
theorem denominatorPos (a b : Rat) (ha : a < 1) (hb : b < 1) :
    0 < (1 - a) * (1 - b) := Rat.mul_pos (by grind) (by grind)

/-- Power sum below one is exactly the strict disk closure inequality. -/
theorem closes (a b : Rat) (ha : a < 1) (hb : b < 1) :
    (a * b) / ((1 - a) * (1 - b)) < 1 ↔ a + b < 1 := by
  rw [Rat.div_lt_iff (denominatorPos a b ha hb)]
  constructor <;> intro h <;> grind

/-- Power sum above one is exactly the strict separation inequality. -/
theorem opens (a b : Rat) (ha : a < 1) (hb : b < 1) :
    1 < (a * b) / ((1 - a) * (1 - b)) ↔ 1 < a + b := by
  rw [Rat.lt_div_iff (denominatorPos a b ha hb)]
  constructor <;> intro h <;> grind

theorem tangent (a b : Rat) (ha : a < 1) (hb : b < 1) :
    (a * b) / ((1 - a) * (1 - b)) = 1 ↔ a + b = 1 := by
  have hc := closes a b ha hb
  have ho := opens a b ha hb
  grind

theorem symmetry (x y : Rat) : margin x y = margin y x := by
  unfold margin
  grind

theorem unequalIdeal : margin 9 4 = 0 := by unfold margin refl; grind

theorem unequalIdealNeitherStrict : ¬ (margin 9 4 < 0 ∨ 0 < margin 9 4) := by unfold margin refl; grind

/-- A forward ratio always gives a reflected power strictly below one. -/
theorem powerUpper (z : Rat) (hz : 1 ≤ z) : refl z * refl z < 1 := by
  unfold refl
  have h : 0 < z + 1 := by grind
  have hh := Rat.mul_pos h h
  have eq : (z - 1) / (z + 1) * ((z - 1) / (z + 1)) =
      (z - 1) * (z - 1) / ((z + 1) * (z + 1)) := by grind
  rw [eq, Rat.div_lt_iff hh]
  grind

end ElementPaper.MixedFaces

#print axioms ElementPaper.MixedFaces.clearedMargin
#print axioms ElementPaper.MixedFaces.denominatorPos
#print axioms ElementPaper.MixedFaces.closes
#print axioms ElementPaper.MixedFaces.opens
#print axioms ElementPaper.MixedFaces.tangent
#print axioms ElementPaper.MixedFaces.symmetry
#print axioms ElementPaper.MixedFaces.unequalIdeal
#print axioms ElementPaper.MixedFaces.unequalIdealNeitherStrict
#print axioms ElementPaper.MixedFaces.powerUpper

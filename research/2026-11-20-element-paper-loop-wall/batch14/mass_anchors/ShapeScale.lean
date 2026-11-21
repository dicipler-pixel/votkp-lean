-- The reflection of each step is homogeneous of degree zero.
namespace ElementPaper.MassAnchors

def reflect (a b : Rat) : Rat := (b-a)/(b+a)

theorem scaleRatio (a b c : Rat) (hc : 0 < c) :
    (c*b)/(c*a) = b/a := by grind

theorem scaleReflection (a b c : Rat) (hc : 0 < c) :
    reflect (c*a) (c*b) = reflect a b := by
  unfold reflect
  grind

theorem anchoredStep (a b : Rat) (ha : 0 < a) : a * (b/a) = b := by grind

-- Even a common rescaling of both energy ladders can flip the charge-q mass sign.
theorem massSignNeedsScale :
    0 < (2863.2 : Rat) + (1/100 : Rat)*(-7381.793561) ∧
    (2863.2 : Rat) + 1*(-7381.793561) < 0 := by decide +kernel

end ElementPaper.MassAnchors

#print axioms ElementPaper.MassAnchors.scaleRatio
#print axioms ElementPaper.MassAnchors.scaleReflection
#print axioms ElementPaper.MassAnchors.anchoredStep
#print axioms ElementPaper.MassAnchors.massSignNeedsScale

import BoundaryAgreement
open ElementPaper.BoundaryAgreement
-- false, as the two margins have opposite signs on this concrete pair
example : ThreeClasses
    (additive (1/3) (1/9) (11/18))
    (product (1/3) (1/9) (11/18)) := by
  unfold ThreeClasses additive product
  grind

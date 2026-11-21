import OpeningMap
-- False control: must be rejected. The upper end of francium's interval is outside, not inside.
theorem Fr_upper_inside : inside (24.3 / 4.0727400 : Rat) := by
  first | (unfold inside; grind) | decide +kernel | grind

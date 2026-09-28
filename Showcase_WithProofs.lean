/-
# VOTKP: the main results, proved

Every statement of `Showcase.lean` is proved here by a theorem of the library in `VOTKP/`.
Lean accepts each step only if the library theorem's statement is the showcase statement,
unfolded, so nothing weaker can stand in for it.
-/
import Showcase
import VOTKP.Smith
import VOTKP.Film
import VOTKP.Peel
import VOTKP.Knot
import VOTKP.Ordinal

namespace Showcase

theorem main_theorem : MainTheorem := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · exact VOTKP.Smith.smith_identity
  · exact VOTKP.Smith.block_succ
  · exact VOTKP.Smith.ladders_same_composite
  · exact ⟨VOTKP.Smith.shell_wall, VOTKP.Smith.pythagorean⟩
  · exact VOTKP.Film.echo_circle
  · exact ⟨VOTKP.Film.circle_criterion, VOTKP.Film.circle_through_origin⟩
  · exact VOTKP.Film.one_radius_cannot_decide
  · exact VOTKP.Film.stack_telescopes
  · exact VOTKP.Peel.cumulant_witness
  · exact ⟨VOTKP.Peel.shared_records, VOTKP.Peel.later_outcomes⟩
  · exact VOTKP.Knot.unit_circle_ratio
  · exact ⟨VOTKP.Ordinal.clean_single_pattern, VOTKP.Ordinal.swapped_single_pattern,
      VOTKP.Ordinal.swapped_ne_clean, VOTKP.Ordinal.delay_one_sees_swap⟩

end Showcase

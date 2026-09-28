import Showcase_WithProofs
-- Deliberately false: the showcase's shell wall altered from 2n − 1 to 2n + 1.
-- The proved main theorem cannot stand in for the altered statement, so this is a type mismatch.
example : ∀ n : ℝ, 1 < n →
    ((n / (n - 1)) ^ 2 - 1) / ((n / (n - 1)) ^ 2 + 1) = (2 * n + 1) / (n ^ 2 + (n - 1) ^ 2) := by
  obtain ⟨-, -, -, ⟨hw, -⟩, -⟩ := Showcase.main_theorem
  exact hw

# Exact critical partner in square-root clocks

Use t=√z₁ and u=√z₂ for forward energy ratios greater than one. The earlier batch-8 mixed-face note derived the algebraic partner formula. Its accompanying Lean file proved the reflected-power rule and the 9/4 unequal-face example. FixedFace.lean proves the critical partner map and its sensitivity for an arbitrary linearly ordered field in core Lean’s type classes.

Write M(t)=(t+1)/(t−1). The cleared equality (t−1)(u−1)=2 is equivalent to u=M(t) when t>1. The map carries t>1 into itself, reverses strict order and is its own inverse. Its fixed points obey t²−2t−1=0; any positive s satisfying s²=2 gives the fixed clock t=1+s and the original energy ratio 3+2s. The theorem assumes a positive square root when it uses one. In particular, it does not assert that the rational numbers contain √2. This is an ordered-field development without an explicit Mathlib real-number instantiation or analytic derivative theorem.

For all t,u>1, including t=u, the exact finite perturbation identity is

    [M(t)−M(u)] (t−1)(u−1) = 2(u−t).

This makes one uncertainty rectangle easy to test. If the smallest observed u exceeds M at the smallest t, the whole rectangle lies on the open side. If the largest u is below M at the largest t, the whole rectangle closes. When neither sufficient strict test holds, a rectangle may touch or straddle the boundary. The Lean proof connects these statements directly to the sign of the cleared original mixed-face polynomial for energy ratios t²,u².

Two exact rational controls show why an increasing or constant-slope partner law would fail. M(2)=3, M(3)=2 and M(4)=5/3. Run `lean -j1 FixedFace.lean` with the repository toolchain. All 12 public declarations and their axioms are in lean_run.txt.

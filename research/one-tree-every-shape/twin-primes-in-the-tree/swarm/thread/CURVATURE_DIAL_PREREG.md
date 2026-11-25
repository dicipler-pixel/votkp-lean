# TWIN-CURVATURE-DIAL-01 — written before any run (2026-11-25T02:58:21Z)

Question: the wall-bite test (TWIN-WALL-BITE-01) could not tell "the wall" from "the big early steps".
Dial: scale every rapidity r -> lam*r. This is the same chain in a ball whose curvature is lam^2 times
stronger (lengths measured in the curvature radius). The steps stay where they are (big ones early),
but the twin start where the walker crosses the wall sphere rho^2 = 1/2 moves (far out for small lam).

Measure, for each lam in {0.25, 0.35, 0.5, 0.75, 1, 1.5, 2}, end at 1e8:
- a_w(lam): twin start where the walker first crosses rho^2 = 1/2 (rho = tanh(d/2)).
- Turn runout (sd of final turn over 200 arm scrambles, counts kept) in a window of 13 steps
  ending at the wall (BEFORE) and a window of 13 steps starting at the wall (AFTER).
- Same for a fixed early window, twin starts 11..227, for every lam (big-step baseline).

Prediction (wall is the bite): BEFORE/AFTER runout ratio stays large (>= 3) at every lam, including
lam where the wall sits far out among small steps.
Big-steps reading: where the wall sits far out (a_w > 1e4), BEFORE/AFTER ratio is near 1.

KILL (wall as bite): if at every lam with a_w > 1e4 the BEFORE/AFTER ratio is < 1.5, the wall is not
the bite; the big early steps are.

## Opposite setup TWIN-CURVATURE-DIAL-02 — written before run (2026-11-25T03:00:10Z)
After -01 killed "wall as bite", try it backwards: curvature fixed (lam = 1), start the walk late
(first twin start >= 1e4, 1e5) so no step is big. Same before/after windows at the wall crossing and
the first-13-step window. KILL (wall as bite, again): before/after ratio < 1.5 at both starts.

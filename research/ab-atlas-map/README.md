# Aharonov–Bohm, weak values and the atlas cards — mapping record (24 Nov 2026)

Author: Jeromie Beasley

Coverage of the read: all 207 cards B1–B207 (title, claim, explanation, closing condition) from
`relational-atlas-lean/atlas/coverage/coverage.json`; plus `DiracTime/WeakValue.lean` and
`DiracTime/PhaseSilence.lean`. Carry/check/arrive fields and source references were not read in this pass.

Script `ab_atlas_map.py` (AB-ATLAS-MAP-01), kill lines written in the file before the run. All five held:

1. Weak value of the which-arm projector in a two-arm loop with flux Phi equals (1 + Gamma)/2,
   Gamma = (z - 1)/(z + 1), z = exp(i Phi). Gamma = i tan(Phi/2): the flux is a point on the rim axis of the Smith disc.
2. Card B158 bound holds at every flux.
3. On an odd ring the signless Laplacian (the opposite book, B192) has the same spectrum as the
   Laplacian with half a flux quantum (B193). On an even ring it equals the zero-flux one.
4. Flat-torus level = 2 pi x distance from the holonomy point to the integer lattice (B8); zero only on the lattice.
5. Ring zeta of the bundle itself: det(I - uB) = 1 - 2 cos(Phi) u^N + u^(2N) (B195, B197): the first prime keeps the flux.

Not run: the quantum Cheshire cat arrangement in the same coordinate.

## Cheshire cat in the Smith-disc coordinate (CHESHIRE-GAMMA-01), run after the mapping

Seven kill lines written in the file before the run; none fired (4000 random arrangements).

- Cat arm weak values are (1 - Gamma)/2 and (1 + Gamma)/2.
- Grin arm weak values are the same two shares for a second coordinate Gamma_s, times the total grin weak value.
- Gamma_s = Gamma (+) Gamma_b (+) (-Gamma_a) under the addition law of card B98.
- Flux moves cat and grin together; it never separates them.
- The original arrangement is Gamma = -1 with Gamma_s = +1: opposite ends of the diameter.
- Card B158 holds for all four arm observables.
- A mirror-fixed (linear) arm polarization gives a twist on the rim, |Gamma_x| = 1. A handed one gives a real twist;
  the opposite handedness is the inverse point 1/Gamma_x, outside the disc.

The divide warning in the output is the exact limit where the grin amplitude in arm L is zero (z_s infinite, Gamma_s = 1).

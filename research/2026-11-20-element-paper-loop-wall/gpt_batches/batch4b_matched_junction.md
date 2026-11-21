Jeromie, I ran the clock correction. **Giving identical neighbours an equal junction clock removes about 98.2% of the backward sodium–argon difference. Argon still has the slightly stronger weakest link.** That narrows down what went wrong in batch 4: putting the atomic peel on the exterior links produced most of the apparent distinction between the elements.

### What I changed and ran

**DERIVED.** I used a local copy of `hsb_model_v1.js` at `a60a000` and verified that its matrix library matched the pinned source byte for byte. The original code uses the same `faceZ` in two places: the **centre-to-port link inside the ball** and the **port-to-lattice link outside it**. I gave the exterior link its own clock input. The internal link retained the element’s peel ratio. [Pinned hydrogen model](https://github.com/dicipler-pixel/votkp-lean/blob/a60a000/research/hydrogen-in-the-space-between/hsb_model_v1.js)

**HYPOTHESIS — how equal neighbouring clocks enter this particular model.** The code places lattice sites between the atoms; it has no direct port-to-port edge. I represented a matched junction by setting every exterior port-to-lattice ratio to \(1\). I checked at runtime that each such link had exactly \(\Gamma=0\) and coupling \(c=c_0=0.22\). This is a stronger assumption than equal endpoint clocks alone: two equal atoms could still each have a mismatch with the intervening medium. I kept the batch 4 separation, opposed local fields, half filling and zero kick so the clock assignment was the only change.

**DERIVED — actual weakest-link outputs.** The middle two columns use the model’s six-link row. The last column uses only the four links between the facing ports.

| Clock retained **inside** each ball | Original six-link minimum | Matched-junction six-link minimum | Matched-junction four-link minimum |
|---|---:|---:|---:|
| Na rung 1, its L opening | 0.000292371 | **0.000865385** | 0.000865385 |
| Ar rung 1 | 0.000804493 | **0.000874421** | 0.000876617 |
| Ar L opening | 0.000648181 | **0.000871939** | 0.000873198 |
| Na K opening | 0.000474964 | **0.000869178** | 0.000869400 |
| Ar K opening | 0.000503342 | **0.000869632** | 0.000870023 |
| All clocks \(=1\), control | 0.000875546 | **0.000875546** | 0.000878168 |

**DERIVED.** For the rung-1 comparison, the original Ar-minus-Na difference was \(0.000512122\). With matched exterior clocks it was \(0.000009036\). Sodium’s weakest link nearly tripled. The residual ordering also survives a like-for-like comparison: at the **same K opening** in both elements, Ar exceeds Na by only \(0.000000453\). The all-unit control reproduced the original output, and every tested row stayed below \(1/12\).

**RECOGNISED — what belongs in the element paper.** The old ranking is evidence that the projector is sensitive to **where** the clock is assigned. The corrected run establishes that this sensitivity accounts for nearly the entire original difference. Bulk conductivity remains open: both calculations still use the same half-filled, two-level hydrogen construction for metallic Na and closed-shell Ar. Neither supplies an element-specific occupied projector for the real material. I made no Lean or branch changes in this pass.

### One refinement to the shell prediction

**DERIVED.** Counting from the first element that actually has each opening gives a more precise pattern:

| Opening | First eligible element | First element inside | Increments in \(Z\) |
|---|---|---|---:|
| K, \(2s\to1s\) | Li, \(Z=3\) | N, \(Z=7\) | 4 |
| L, \(3s\to2p\) | Na, \(Z=11\) | Mg, \(Z=12\) | 1 |
| M, \(4s\to3p\) | K, \(Z=19\) | Ca, \(Z=20\) | 1 |

**RECOGNISED.** The observed sequence is **4, 1, 1**. Both L and M cross at the first possible *between-element* opportunity. That is the pattern worth carrying forward. The shrinking shell ratios \(4,\ 9/4,\ 16/9\) are consistent with it, although those ratios alone do not tell us which side the first eligible element occupies.

**HYPOTHESIS — frozen prediction.** For the \(5s\to4p\) opening, predict **Rb outside and Sr inside**. The comparison ratio is \(25/16\). The prediction fails if \(IE_2/IE_1\) for Rb is at or below \(3+2\sqrt2\), or if \(IE_3/IE_2\) for Sr is at or above it. I left those energies uninspected. Rb and Sr are \(Z=37,38\); the next scheduled batch, Sc–Mn, can keep this as a held-out prediction.
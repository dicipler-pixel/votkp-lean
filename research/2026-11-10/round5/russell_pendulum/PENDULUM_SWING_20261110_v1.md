# The pendulum swing — What Russell Saw, re-read 10 November 2026

Jeromie Beasley

Sources read in full for this note:
- *What Russell Saw* v1 (26 Sept 2026), §2 and Plate 1.
- *Russell, Corrected* (3 Nov 2026), Plate I.
- what-russell-saw-lean @ 258d89f: RussellRebuild.lean, RussellOrbits.lean (theorem list), RussellPhyslib.lean, LIMITATIONS.md, FalseControls.

## What Russell wrote
The Universal One, p. 15: the energy spent in any two opposite swings of the cosmic pendulum is always constant, and only the "dimension" of the two swings varies. Chart, p. 11: the pendulum drawn as a wheel.

## The reading
With position across and momentum up, the oscillator's history is one closed curve, E = ½kx² + p²/2m. When the axes are scaled by A and mωA, that curve is a circle, and the wheel is this phase portrait.

## What Lean proves (CI green at 258d89f)
- `pendulum_energy_constant`: for x = A cos ωt, ½kx² + p²/2m = ½kA² at all t.
- `RussellPhyslib.paired_motion_constant`: kinetic + potential energy is constant along **every** solution of Physlib's harmonic oscillator.

## What Lean does not prove
- That the phase curve is the closed ellipse x²/A² + p²/(mωA)² = 1. This is the same algebra as `pendulum_energy_constant`, but it is not stated as its own theorem.
- That the two stores have equal time-averaged shares (½ and ½). Plate I of *Corrected* asserts this; it is not formalized.
- Anything about the real (nonlinear) pendulum θ'' = −sin θ.
- The reading itself, as LIMITATIONS.md already says.

## New check: PENDULUM-SWING-01 (real pendulum, ω₀ = 1)
Why it proves the claim: the script integrates θ'' = −sin θ over one exact period, 4K(sin²(θ₀/2)), and measures three things:
- the energy drift;
- the return to the start;
- the time-average of KE/E.

Kill conditions:
- (a) drift greater than 1e-9 kills "constant sum";
- (b) |⟨KE⟩/E − ½| greater than 1e-3 kills "equal shares";
- (c) a return error greater than 1e-8 means the period formula is wrong.

| θ₀ | period / 2π | energy drift | return error | ⟨KE⟩/E |
|---:|---:|---:|---:|---:|
| 5° | 1.000476 | 4.3e-11 | 1.9e-12 | 0.4999 |
| 30° | 1.017409 | 9.0e-12 | 2.4e-12 | 0.4957 |
| 60° | 1.073182 | 7.7e-12 | 4.1e-12 | 0.4820 |
| 90° | 1.180341 | 8.6e-12 | 4.8e-12 | 0.4569 |
| 120° | 1.372881 | 5.8e-12 | 4.3e-12 | 0.4154 |
| 150° | 1.762204 | 5.3e-12 | 6.7e-12 | 0.3450 |
| 170° | 2.439363 | 5.0e-12 | 1.7e-11 | 0.2587 |
| 179° | 3.901065 | 4.9e-12 | 1.5e-10 | 0.1632 |

Results:
- **Constant sum: survives at every amplitude.** Russell's axiom holds for the real pendulum, not only the small-swing one.
- **Equal shares: killed above small swings.** It is 0.4957 at 30° and falls to 0.163 at 179°. The v1 paper restricts itself to "small angles". Plate I of *Corrected* states ½–½ without that limit and grades the plate "corrected: nothing". That plate needs the qualifier.
- **The swing's time grows with its size.** The period grows from 1.0005 to 3.90 small-swing periods and diverges as θ₀ → 180°, where the swing reaches the inverted top. This fits his "the apparent variation is in the dimension of the two opposing swings". That is a reading, not a theorem.
- (c) Return error is at most 1.5e-10 at 179°, inside the 1e-8 kill line; the period formula holds.

## Open, and untested
1. **Where his dead centre sits.** v1 and Plate I put Russell's "dead centre" at x = 0, which is all motion with zero force. In engine language, a dead centre is the end of the stroke, where the motion is zero. I have not seen his p. 11 chart in this pass, so I can't say which points on his wheel he labelled "dead centre". Checking the chart settles it.
2. **The inverted top against the ISCO.** Both make the time to come back infinite. The mechanisms differ:
   - at the pendulum top, the linearised coefficient is −1 (a saddle);
   - at the ISCO, the coefficient is 0 (Plate III's nilpotent).

   Any link between Plate I and Plate III through this point is untested.
3. **Lean.** Three statements could be added: the phase ellipse; ⟨KE⟩ = ⟨PE⟩ over one period for A cos ωt (∫cos² = ∫sin² on a period); and a statement for the nonlinear pendulum. None are written.

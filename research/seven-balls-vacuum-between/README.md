# Seven Balls, the Vacuum Between — v4 (18 Nov 2026)

Jeromie Beasley's seven balls, built on his page *Seven Balls, One Container v3*. AI-assisted.

**New in v4: the vacuum in the gaps between the balls.** Everything from v3 is kept as it was: the balls, the dents, the breathing and his light.

## What is new
- **Where the vacuum is.** It sits in the twelve gaps between side balls on perpendicular axes. These come in three kinds (x–y, y–z, x–z), four of each, always equal.
  - Two equal neighbours touch exactly at his wall, z = 3 + 2√2. Below the wall they overlap; above it the gap opens.
  - With his 3, 5, 7 breathing, the y–z gaps open and shut. The x–z gaps open only briefly, and the x–y gaps never open.
- **The pull.** This is the Casimir pull between two of his faces: Lifshitz, with each face taken as his split at index ratio z_gap.
  - At the wall it is η = 0.456 of the perfect-mirror pull. At the plain normal-incidence level it is exactly Li₄(½)/ζ(4) = 0.478.
  - Between two balls it uses the proximity-force rule, which holds for s ≪ r.
- **The gap's own light.** The standing modes across the gap are ω_k = kπ/s. They leak through his faces at κ = −ln(R_f²)/2s.
- **Light made by the breathing (dynamic Casimir).** This uses the exact single-mode equations from the vacuum. The light made is booked as paid for by the breathing, so the vacuum books close.
- **The pump test.** One gap of his faces is pumped at twice its own light.

## Findings (all from the checks; numbers in `vac_check_01_output.txt`)
1. At his drive (periods 8, 13, 21) the gaps change slowly next to their own light. The walls move at about 1–4% of c, and the gap light stays at about 10⁻⁵ photons per mode, which is (wall speed / c)². The pull is real and large near touching.
2. Resonance needs the gap pumped at twice its own light. For s = 0.05 and P = 8 that is about 160× faster breathing.
3. With his faces (R_f = ½ at the wall) the gap light leaks fast: κ/ω₁ = ln4/2π = 0.221. Light only builds from the vacuum if the gap width swings by more than about 22% at 2ω₁ (measured 0.216).
   - Better faces lower that threshold: z_gap = 7 gives 0.175, and z_gap = 20 gives 0.048.
   - Below the threshold the light leaks into the balls as fast as it is made.

## Checks
All 42 page checks pass (Run full checks), and so does `vac_check_01.js` in node:
- η against an independent high-precision run;
- the pull against the textbook value;
- the wall touch;
- the twelve gaps against the three kinds;
- the moment equations against the mode function itself, to 1e-9 in the page;
- the vacuum books.

## Labelled models
- No dispersion.
- The proximity-force pull.
- One-axis gap modes.
- Gaps under 0.02 r treated as shut.
- The pull does not move the balls.
- The breath speed ×k only scales his drive's time (k = 1 is his drive).

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
1. At his drive (periods 8, 13, 21) the gaps change slowly next to their own light. The walls move at about 1–4% of c, and the gap light stays at about 2×10⁻⁵ photons per mode. That is (v/c)²/4π², with v the gap's rate of change: the adiabatic parameter is λ/ω₁ = ṡ/2π. The pull is real and large near touching.
2. Resonance needs the gap pumped at twice its own light. For s = 0.05 and P = 8 that is about 160× faster breathing.
3. With his faces (R_f = ½ at the wall) the gap light leaks fast: κ/ω₁ = ln4/2π = 0.221. Light only builds from the vacuum if the gap width swings at 2ω₁ by more than about κ/ω₁.
   - The onset of growth, measured from the growth rate between 200 and 400 pump periods, is 0.226 at the wall, 0.185 at z_gap = 7 and 0.062 at z_gap = 20. The first-order values κ/ω₁ are 0.221, 0.183 and 0.064.
   - The earlier search (60 against 120 periods) reported 0.216, 0.175 and 0.048. It counted the slow rise towards a steady level as growth, so those were too low.
   - Below the threshold the light leaks into the balls as fast as it is made.

## Checks
All of the page's full checks pass (Run full checks), and so does `vac_check_01.js` in node. It runs from any folder; the files it needs are here: `lh_math_v1_from_page.js` (his LH-MATH-V1, as embedded in the page) and `seven_balls_v4_page.js`. It checks:
- η against an independent high-precision run;
- the pull against the textbook value;
- the wall touch;
- the twelve gaps against the three kinds;
- the moment equations against the mode function itself: the page measures a difference of 6×10⁻⁹ (its pass line is 1e-3), and node measures 1e-4 at the coarser step;
- the vacuum books.

## Labelled models
- No dispersion.
- The proximity-force pull.
- One-axis gap modes.
- Gaps under 0.02 r treated as shut.
- The pull does not move the balls.
- The breath speed ×k only scales his drive's time (k = 1 is his drive).

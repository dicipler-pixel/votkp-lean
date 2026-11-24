# Swarm 4 — precision to 10¹² and the digit-balance condition

Jeromie Beasley · swarm notes · 24 November 2026

## Method
- Walker: `twinwalk.c` (TWIN-WALK-SL2C-01). It uses SL(2,ℂ), long double, and a segmented sieve; twin starts are streamed.
- Chunks are combined in 40-digit arithmetic.

### Checks
- It reproduces the earlier harness turns from 1e5 to 1e9 (12.204756 at 1e8, 12.269506 at 1e9).
- Twin counts agree with π₂ at 1e9 through 1e12. At 1e10: 27,412,677 starts ≥ 11, consistent with π₂ = 27,412,679.
- |det| − 1 < 7e-13.
- Wall-clock: about 48 minutes in total. The walk to 1e10 alone takes 18 s.

## Turn (degrees)

| mark | turn |
|---|---|
| 1e9 | 12.2695 |
| 3.16e9 | 12.2894 |
| 1e10 | 12.2969 |
| 3.16e10 | 12.3083 |
| 1e11 | 12.3197 |
| 3.16e11 | 12.3335 |
| 1e12 | 12.3442 |

At 1e12 the axis is (0.105, −0.994, −0.031).

## The tilt (H3)
- Fit per decade: S_s = βL + γ. The tilt is real, at least ten times the remainder.
- |β| = 0.00446, 0.00352, 0.00291, 0.00240 for the decades 1e8–1e9 through 1e11–1e12.
- |β| × (mean gap between twin starts) = 1.15, 1.15, 1.18, 1.17, which is flat. So the tilt falls like 1/(mean gap), the Hardy–Littlewood 1/L² law with its first correction.
- Kill condition, written beforehand: the last decade's |β| must be below 0.5 of its 1e6–1e7 value.
  - Through 1e12 the ratio is 0.47, so it passes.
  - With data only to 1e11 it was 0.57, and the kill fired.
- H3 with a fixed P = (⅓, ⅓, ⅓) is borderline: the tail falls only like 1/L.
- The workable form centres the noise on the local mean P(L). The remainder then has rms 3e-5, about random-walk size. The direction of P(L) has a finite total turn left, under 0.25°.

## The limit
- Six curve fits put the limit anywhere from 12.33 to 12.53. Their spread trips the kill, so no limit is claimed from fits.
- After 1e10 the noise scale is 0.013°, but the turn moved 0.047°. The motion is systematic, not noise.
- **Mechanism.** The heading sits on the tilted mean, not on the diagonal: 0.28° off, against √3|β| = 0.24°. As the tilt dies, the frame must make the minimal rotation that carries the diagonal onto the heading.
- **"Turn if the tilt dies" readout.** 12.46594 (1e6), 12.46514 (1e8), 12.46507 (1e10), 12.46508 (1e11 and 1e12).
  - Scatter: 5.5e-6 from 1e10 on.
  - The actual turn lags the readout by 0.476 × (angle from heading to diagonal).
- **Synthetic checks** use the real gaps with arms redrawn:
  - After an exactly balanced tail, the turn lands on the readout to within 0.0006°.
  - A chain whose tilt never dies stays 0.67° off.
  - Two pre-written kills fired because the chains had not finished relaxing by 1e8. Both are recorded in the script header.
- **Limit:** turn → **12.4651° ± 0.0001°**, approached from below roughly like 1/L². This is conditional on the tilt dying, which Hardy–Littlewood predicts and four decades of data show. The ± is estimated, not proved.

## The constant c in d = L/√3 + c
- Values: 0.108528 (1e8), 0.108568 (1e9), 0.108590 (1e10), 0.108607 (1e11), 0.108618 (1e12). So c = 0.1086 to four digits.
- The drift of +9e-6 per unit L is explained by the tilt: the mean step gain is 1/√3 + (√3/2)|β|².
- Limit about 0.10866 ± 0.00003. Derived, not run.

## Not yet known
- The constant 1.17 is not derived. The first mod-30 heuristic gets the sign wrong.
- The 1/(mean gap) law is measured over only four decades.

## Files
- Scripts: twinwalk.c, run_chunks.py, combine.py, analyse.py, synth_check.py
- Outputs:
  - out/walk_1e12.csv: every checkpoint
  - out/analysis_1e12.txt
  - out/synth_check.txt

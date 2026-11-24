# The twin chain as a cut thread

Jeromie Beasley · 24 November 2026

## The thread
- **Turn:** 30 integers. Twin starts can sit only at 11, 17 and 29 (mod 30), so this is a three-start thread.
- **Starts:** spaced 6, 12 and 12 apart.
- **Path:** in log length, the pitch gets finer as size grows (one turn = 30/a).

## Test
TWIN-THREAD-FORM-01 and TWIN-THREAD-NOISE-01. Kill conditions were written before the runs.

Method:
- Cut the thread with the small primes up to P (Granville-type sieve model).
- For each cut, measure dev_j × G, where dev_j is the gap-weighted end-digit share minus the count share, and G is the mean gap.
- Compare against the real twin starts in (1e8, 1e9]: dev×G for digits 1/7/9 = −0.924, +0.839, +0.085 (se 0.041, 0.034, 0.054).

| thread cut | model dev×G (1/7/9) | match within 2 se |
|---|---|---|
| mod 30 (2·3·5) | +0.662, −0.645, −0.017 | no: wrong sign |
| mod 210 (adds 7) | −0.942, +0.974, −0.032 | digit 1 yes, digit 7 off by 2.4 se |
| mod 30030 (to 13) | −1.177, +1.142, +0.034 | no: overshoots |
| to 17, to 19 (one seed each) | −0.88, +0.86, +0.02 and −1.04, +0.88, +0.15 | within noise of the real values |

## Findings
- **Sign:** cutting the thread by 7 flips the tilt to the real sign. The mod-30 screw alone gives the wrong sign.
- **Size:** about 0.9–1.2 for every cut from 7 on, so the order of magnitude is right.
- **Kill as written fires:** no single cut matches all three digits within 2 se. The size is not yet nailed; the model holds density fixed at 10^8.5, while the real data run over a decade.
- **Not the first flank:** the exact nearest clearance before each start does not show the flip (digit 1 stays +). The tilt comes from longer-range structure across the roughly 20 slots one gap spans.

# Swarm 2 — opposite ways and other chains

Jeromie Beasley · swarm notes · 24 November 2026

Predictions were written before the runs (see PREDICTIONS.md). The walker was checked three ways:
- against plain matrix products, to 1e-10;
- against 60-digit arithmetic at distance 48.85, to 8e-16;
- against the earlier reference: c = 0.1085 and turn 12.205° at 1e8.

## Result table (largest cut-off)

Column notes:
- "c/L fit" is |P| + c/L, with c taken as the mean of the 1e6 and 1e7 values.
- "Frame change" is the change over the last decade.
- "Lock angle" is the angle between the body heading and P̂.

| Variant | \|P\| | d/L | c/L fit | Free slope | Turn | Frame change | Lock angle | Verdict |
|---|---|---|---|---|---|---|---|---|
| Twins by end digit (1e8) | 0.57735 | 0.58412 | 0.58412 | 0.5774 | 12.205° | 0.20° (shrinking) | 0.56° | pass |
| Twins mod 30 | same labels as end digit | | | | | | | pass (identical) |
| Twins mod 9 | 0.57735 | 0.58152 | 0.58153 | 0.5773 | 9.29° | 0.37° | 0.09° | pass |
| Twins mod 7, five arms | 0.44721 | 0.46889 | 0.46887 | 0.4473 | 34.6° | 0.67° | 1.59° | pass |
| Twins reversed | the product is Lᵀ, so d and turn are identical | | | | | | | identity |
| Cousins | 0.57735 | 0.58850 | 0.58850 | 0.5774 | 14.8° | 0.22° | 0.64° | pass |
| Sexy | 0.57735 | 0.58344 | 0.58300 | 0.5796 | 10.0° | 0.85° (not shrinking) | 4.85° | slope passes; frame not settling |
| All primes, four orthogonal axes (1e9) | 0.5 | 0.50274 | 0.50264 | 0.5003 | 10.1° | 0.30° (flat) | 1.93° | slope passes; frame undecided |
| All primes, tetrahedron (1e9) | 0 | 0.0368 | — | 0.018 | 3.38° | 0.11° | — | "bounded" prediction killed; d ≈ 0.326 ln L passed |
| Cramér random chains (×5) | 0.57735 | 0.588–0.626 | match | 0.5772–0.5773 | 10–42° | 0.19–0.45° | 0.13–0.30° | pass |
| Blocks of 0.25 | 0.57735 | 0.58308 | 0.58257 | 0.5799 | 18.8° | 3.3° (flat) | 5.8° | slope barely passes; frame never settles |
| Blocks of 1 | 0.57735 | 0.62058 | 0.61020 | 0.6236 | 84.6° | 36° | 24° | kill |
| Blocks of 4 | 0.57735 | 0.86898 | 0.80185 | 0.8448 | 85.8° | 18–70° | 52° | kill |
| Geometric blocks | 0.57735 | 0.77727 | 0.70707 | 0.8565 | 89.9° | 10–77° | 54° | kill |
| Fixed ln 5 steps, twin arms | — | 0.76363 | n/a | 0.7637 | 43.6° | 42–133° | 41–52° | kill (predicted) |
| Fixed ln 5 steps, random arms | — | 0.77152 | n/a | 0.7716 | 62° | 54–142° | 34–52° | kill |

## Findings
1. **The slope law d/L → |P| survives** every chain whose steps shrink and whose arms balance. The ideal |P| matches the free slope to 0.4%.
2. **The constant c is not universal.** It depends on the labels and on the first few dozen steps:
   - end digit 0.1085;
   - mod 9 0.067;
   - mod 7 0.347;
   - cousins 0.184;
   - random chains 0.17–0.78.
3. **Arm blocks break it.** Even blocks of path length 0.25 stop the frame from settling: it moves about 3.5° per decade, flat. Balance on average is not enough; the noise-tail condition (H3) is needed.
4. **Fixed steps (ln 5) read the digit order.**
   - Twin arms give 0.76363. Random arms give 0.7712–0.7713, and shuffled twin arms 0.7710–0.7716.
   - Consecutive twin starts repeat their end digit less often than chance (0.307 against 1/3). A chain built with that repeat rate gives 0.7642.
5. **Zero mean (tetrahedron).** Distance grows like ln L: 0.544, 0.602, 0.650, 0.691 at 1e6–1e9.
   - A law fitted before the 1e9 run, d ≈ 0.326 ln L, predicted a rise of 0.043. The rise was 0.0415.
6. **All primes: the path-weighted shares are biased like 1/L, while the counts are balanced.**
   - Deviation × L for end digits 1/3/7/9 is +0.080, −0.196, +0.174, −0.058. The values match to 3 digits for 1e6–1e7 and 1e7–1e8.
   - Cause: each end digit forbids one class of incoming gap. For example, no prime ending in 7 follows a gap of 2.
   - The lock angle falls only like 1/L (2.88°, 2.59°, 2.24°, 1.93°).
   - The frame keeps turning at 0.12–0.17° per unit of path, so whether it converges is undecided.
7. **Sexy primes have the same 1/L bias.** Deviation × L is +0.59, −0.28, −0.31. The frame is not settling.
8. **Twin primes and cousins settle.** Half-decade frame changes fall from 4.8° to about 0.2° for twins, and from 1.8° to 0.06° for cousins.
   - The twin path-share deviation is −0.004, +0.003, +0.001 at 1e7–1e8.
   - Its decay rate is not decided at this range: deviation × L² for digit 1 goes −0.46, −0.57, −0.86.
   - This agrees with the proof report: whether the tilt dies away or persists is open.

## Scripts
Each script carries `# SCRIPT: NAME` and has a matching .out file:
- owalk.py
- check_walker.py
- check_walker_mp.py
- v_twin_c.py
- v_a_b.py
- v_a_1e9.py
- share_drift.py
- frame_fine.py
- v_d_e.py
- e_fix_spread.py

The sieve caches were deleted to save disk; they regenerate on rerun.

# T3b_cap_word: exact first-reach n from the three-gap word

## Result first
No closed-form law passes the factor-2 kill line. What was obtained is one new proven lower envelope that is far tighter than the earlier laws, and an exact reformulation.
- Exact statement (derived on paper, section 1): n_first(m) = 1 + (smallest index span of a set of m integers whose points k*alpha mod 1 are delta-separated). Here alpha = theta/2pi, delta = d/2pi, sigma' = 1 - m*delta.
- Law F1 (new, rigorous, lower envelope): n_first(m) >= n_L(m) = 1 + max over r = 1..m-1 of j_min(r), where j_min(r) is the smallest |j| with frac(j*alpha) in [r*delta, r/m]. Proof side held in all 330 targets (0 violations, none censored).
- Kill line "n_L/n_meas in [0.5, 1]": KILLED. Outside in 110 of 330 targets (BASE 44/123, FRESH 40/104, new set Z4 = z 2.3, 3.7, 4.2, 5.3, 5.75: 26/103). Cap-only subset: 55 of 157. Median ratio 0.56, 10th percentile 0.31, minimum 0.035. For comparison the earlier upper law A missed by a median 3.9 times; F1 is within about 2 of the measured value in 2/3 of the cases, from below, with no constant.
- Opposite readings run under the same line and also killed: F5 (every arc lies in [delta, delta + sigma'], a closed walk needs a forward and a backward step; n_5 = 1 + max(a_+, a_-)) 268/330 outside; F6 (two-step walk, n_6 = 1 + a_+ + a_- - gcd) 264/330 outside, never above 1.57 times the measured value, i.e. it fails only by being too small (median 0.11). The window W is too wide to constrain anything.
- Where first-reach sits in the three-gap blocks (n = j q_k + q_{k-1} + r, 0 <= r < q_k): at the block start in only 34 of 330 targets; position r/q_k is spread flat (quartiles 0.25, 0.55, 0.80). So the gap LENGTHS of a block do not decide the first reach; the COUNTS inside the block (which slide with r) matter. A law built on lengths alone cannot be exact.
- Lab frame: not run (the own frame did not pass; instruction was lab only if it passes). Untested whether F1 transfers by replacing gaps by mapped lengths; the necessary-window argument itself needs only that points lie on one circle with a rotation-ordered chord rule, but the lab points are not a rotation orbit so "frac(j alpha)" has no meaning there (only the three-gap word of the mapped gaps is available).

## 1. Derivation (paper, written before the run)
Notation: alpha = theta/2pi irrational, delta = d/2pi, d = 2 arcsin(sqrt(eps/2)/sin phi), m the target count (cap or cap-1), sigma' = 1 - m*delta >= 0.
1. N(n) >= m means some m of the points k alpha, 1 <= k <= n, have all circular separations >= delta. Shifting every index by a constant rotates the set, so n_first(m) = 1 + min span (max K - min K) over delta-separated m-sets K.
2. List the chosen points in circular order. Consecutive arcs a_i = frac(j_i alpha) where j_i is the index difference; a_i >= delta; the arcs sum to 1; the signed j_i sum to 0 (indices telescope).
3. For each r, the m cyclic runs of r consecutive arcs have total exactly r (r arcs sum average r/m after summing all runs: sum over runs = r * 1). Each run is >= r*delta, and at least one run is <= r/m. A run of r arcs joins two chosen points with index difference j; so frac(j alpha) lies in [r delta, r/m] for some |j| <= n - 1. This holds for every r from 1 to m-1. Hence n >= 1 + max_r j_min(r) (law F1).
4. The window [r delta, r/m] has width r sigma'/m: tiny when the cap has little slack, which is why n_L grows as the slack shrinks (continued fraction of delta against alpha).
5. Block ends, three-gap theorem. At n = q_k: points are (i p_k)/q_k lattice plus k e, e = alpha - p_k/q_k, |k e| < 1/q_{k+1}. Gap lengths: small s = eta_{k-1} (count q_k - q_{k-1}) and large l = eta_{k-1} + eta_k (count q_{k-1}), eta_j = ||q_j alpha||. A run of r consecutive gaps sums to r s + t (l - s), t = number of large gaps, which takes two consecutive values by Sturmian balance. A tiling by m runs needs each run >= delta, total 1: ignoring the perturbation, N(q_k) >= m needs an integer r with r/q_k in [delta, 1/m]; with the perturbation the interval widens by about 1/(q_k q_{k+1}). Prediction form: the cap is reached at a convergent block when an integer r satisfies q_k delta <= r <= q_k / m, i.e. a p/cap-type approximation of delta by r/q_k. This block-end sufficiency was NOT tested separately (only the necessary pair-window consequence, F1, was run). Section "blocks" shows the actual first reach is almost never at a block end.
6. Why the necessary condition is loose: it checks each r separately, while a real set must use the same few integer steps for all r and close the cycle (sum of j_i = 0). Exploration (x_explore.py, not a law test) showed optimal sets mixing two or three step sizes of both signs (for z = 2, eps = 0.1: forward steps 26 and 1; z = 5.5, eps = 0.02: 1236 and three backward steps). The missing piece is the joint (closure + counts) condition, an inhomogeneous Diophantine statement, not a function of one block's gap lengths.

## 2. Kill lines and counts
All written in STATE.md before the corresponding run. Own frame, targets cap and cap-1, zero-slack cap excluded (class K-0 of T3, unchanged).
| law | line | outside |
|---|---|---|
| F1 n_L | ratio in [0.5, 1] | 110/330 (BASE 44, FRESH 40, Z4 26) KILLED |
| F5 n_5 | ratio in [0.5, 1] | 268/330 KILLED |
| F5b max(n_L, n_5) | ratio in [0.5, 1] | 110/330 (same as F1) KILLED |
| F6 n_6 | ratio in [0.5, 2] | 264/330 KILLED |
BASE and FRESH n_meas are the earlier worker's post-fix first-reach values (exact circular greedy, bisection valid because prefix sets nest); Z4 n_meas measured here with the same code. Z4 was the never-used set; the F1 form was chosen before seeing any F1 numbers, though the exploratory step-structure printout (6 cases) was seen first.

## 3. What is established
- Envelope for every case run: n_L <= n_meas <= min(n_A, n_E) (E and A from T3, sufficient). F1 closes from below to a median factor 1.8 of the measured value; the whole spread now sits in the closure/counts of the word.
- Next exact step (untested): minimise span over closed walks with steps from the finite step set {j : frac(j alpha) in [delta, delta + sigma']} subject to arc total 1, i.e. an integer program on the three-gap word at the block of the candidate n; this is the direct route to an exact rule and to compare against measured values.

## Files
/home/claude/harness/workers/T3b_cap_word/: STATE.md, REPORT.md, t3_common.py (copy), x_explore.py, t3b_law.py (+ t3b_results.jsonl, t3b_law.out), t3b_judge.py, t3b_law2.py (+ t3b_results2.jsonl), t3b_judge2.py (t3b_judge2.out), t3b_blocks.py (t3b_blocks.out).

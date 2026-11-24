# Predictions written before any variant was run (Jeromie Beasley swarm, worker "opposite", 24 Nov 2026)

Law under test: d = |P| L + c, P = sum_s p_s e_s (weights p_s = limiting share of path carried by arm s), frame turn converges when sum r = inf, sum r^2 < inf and the arm noise tail decays.
Standard kill (all law variants): fit c = mean of (d - |P| L) at the 1e6 and 1e7 cut-offs; KILL if d/L at the largest cut-off differs from |P| + c/L by more than 1 % (relative).
Frame convergence read: angle of R_k R_(k-1)^T between successive decade cut-offs; "converges" = these shrink decade on decade.

| id | variant | arms / space | |P| predicted | predicted outcome |
|---|---|---|---|---|
| T0 | twin chain, end digit 1/7/9 (reference) | 3 orthogonal, SO(1,3) | 1/sqrt3 = 0.5774 | law holds, c ~ 0.109, turn converges |
| a-i | all primes p>5, end digit 1/3/7/9 | tetrahedron vertices in R^3 (sum 0), SO(1,3) | 0 | NOT linear: d stays bounded (converges to a finite limit d_inf of order sqrt(sum r^2)); the whole product L_n converges; frame turn converges. Kill for this row: d(1e8)-d(1e7) > 0.01*(L(1e8)-L(1e7)) or decade changes of d not shrinking |
| a-ii | all primes, 1/3/7/9 | 4 orthogonal, SO(1,4) | 1/2 | law holds, turn (SO(4)) converges |
| b-cous | cousin starts p (p+4 prime), end digit 3/7/9 | 3 orthogonal | 1/sqrt3 | law holds, converges |
| b-sexy | sexy starts p (p+6 prime), end digit 1/3/7 | 3 orthogonal | 1/sqrt3 | law holds, converges |
| c-30 | twin chain, residue mod 30 in {11,17,29} | 3 orthogonal | 1/sqrt3 | IDENTICAL to T0 (11<->1, 17<->7, 29<->9 is a relabelling) |
| c-7 | twin chain, residue mod 7 in {1,2,3,4,6} | 5 orthogonal, SO(1,5) | 1/sqrt5 = 0.4472 | law holds, converges |
| c-9 | twin chain, residue mod 9 in {2,5,8} | 3 orthogonal | 1/sqrt3 | law holds, converges |
| c-rev | twin chain, product in reversed order B_N...B_1 | SO(1,3) | 1/sqrt3 | d exactly identical (cosh d = L_00 and B_n symmetric => reversed product = L^T); frame = R^T, so turn angle identical; heading = body heading of T0 |
| d-cram | Cramer random twins (cand. m=5 mod 6, prob 12 C2/ln^2 m), arms iid uniform | 3 orthogonal | 1/sqrt3 | law holds, turn converges in each realisation |
| d-blk | real twin steps, arms in blocks of fixed path length Lambda (cycle x,y,z) | 3 orthogonal | 1/sqrt3 on average | noise tail does not decay (H3 fails): body heading keeps cycling, frame keeps turning (decade frame changes do NOT shrink); d/L converges to a value at or below 1/sqrt3 (deficit grows with Lambda) -> expect KILL of the law for large Lambda |
| e-fix | every step r = ln 5, twin end-digit arms | 3 orthogonal | (1/sqrt3 if the law applied) | sum r^2 diverges: NO lock, frame does NOT converge (each step turns the frame by an O(1) Wigner angle); d/L -> a Lyapunov exponent / ln5 that differs from 1/sqrt3 by more than 1 % -> expect KILL |

## Added after the 1e8 runs, before the 1e9 all-primes run (second round of predictions)
Finding at 1e8: for ALL primes the path-weighted arm shares are biased like kappa_s / L (dev*L steady: +0.08, -0.20, +0.17, -0.06 for digits 1,3,7,9), although the COUNT shares are balanced. Mechanism: the step before a prime q is the gap q - prev(q); a digit-7 prime can never follow a gap of 2 (q-2 ends in 5), a digit-3 prime can never follow a gap of 8 mod 10, etc., which shifts the mean preceding gap by O(1) against a mean gap ~ ln x, i.e. a relative bias ~ 1/L. Same for sexy starts (q-6 can be the previous sexy start only when q is not = 1 mod 5): one extra prime, so 1/L again. Twins and cousins need two new primes, so their bias is ~ 1/L^2.
Predictions for 1e8 -> 1e9 (all primes):
 P1 (a-i, tetrahedron): d keeps growing like |kappa| ln L, |kappa| = 0.326 (from the 1e7-1e8 decade): predicted d(1e9) - d(1e8) = 0.043 (kill if outside 0.033..0.053).
 P2 (a-ii): d/L law holds (rel diff < 1 %); lock angle falls like 1/L: predicted 1.97 deg at 1e9 (kill if outside 1.6..2.4).
 P3 (a-ii): frame rotation rate per unit L falls (lag mechanism, rate ~ |kappa|/(|P| L^2)): predicted about 0.11 deg per unit L over 1e8..1e9 (kill if >= 0.15, i.e. no fall from the 1e7..1e8 level).

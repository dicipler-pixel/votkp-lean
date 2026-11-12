# T5_band_mean REPORT (2026-11-12)

## Results first

1. k(z) in closed form, checked. The loop fixes one band quantity, m = |v+w e^{ik}|^2 / u^2 (the overall real scale is free, and K does not see it):
   - inside the wall (G^2 < 1/2): m = 1/(2G^2)
   - past the wall (G^2 > 1/2): m = 2G^2
   - so cos k(z) = (u^2 m - v^2 - w^2) / (2 v w), with G = (z-1)/(z+1).
   One formula covers both sides: K = m/(m-1) always (1/(1-2G^2) inside, 2G^2/(2G^2-1) past).
   Checked at 60 digits at z = 1.5, 2, 3, 4, 5, 5.5, 5.8, 6.5, 7, 8, 16.8177, 206.768, on his four exit bands (u = 0.5, 0.25, 0.45, 0.65 with w = 1, v = 0.468213192462, 0.747401425428, 0.529150262213, 0.235726207892): K from the band at k(z) against K computed from W's biorthogonal eigenvectors, and m from the band against m from |a|,|b| of log(-W). Worst relative residual is about 1e-58 (the whole run's worst, including the k tests below, is 8e-25). Kill line 1e-12: PASS. Output: s1_out.txt.
2. z = 3, z = infinity (the rim) and the pair-partners across the wall all pick the same k. On any of his exit bands, k(3) = k(rim) = k*, where E(k*) = u and K(k*) = 2: k* = 2.4465890553 (u=0.5), 2.8544682180 (0.25), 2.5441862369 (0.45), 2.0337964287 (0.65). k(3) - k* = 1e-61; k(1e25) - k* = 3e-25 (it approaches k* as 1/z).
3. Is the map onto the band? Not the whole z range. On his exit band u = 0.5, v = 0.4682:
   - in band (real k): z = 2 (k = 1.6716), 3 (2.4466), 4 (2.7685), 8 (2.9363), 16.8177 (2.6492), 206.768 (2.4627);
   - off band, k = pi - i x (real E(pi) gap too small for that K): z = 5, 5.5, 5.8, 6.5, 7; and z = 1.5 is off the other end (k = i x).
   The band's range of m is [(w-v)^2/u^2, (w+v)^2/u^2] = [1.1312, 8.6226], so the loop z = 1 end (m -> infinity) needs u/w -> 0 (Hermitian limit) and the wall end (m -> 1) needs a closed gap, E(pi) -> 0, i.e. w - v = u. To cover every z in (1, infinity) one needs the family w - v = u with v/u -> infinity (the critical SSH band approaching Hermitian). No single gapped (u,v,w) covers all z. For his band at the exit line, the inside-wall z-window it covers is exactly z in [z0, z1] with G0^2 + G1^2 = 1/2: u=0.5: z in [1.6344, 4.9673]; u=0.25: [1.2251, 5.6629]; u=0.45: [1.5255, 5.1689]; u=0.65: [2.1844, 4.0173].
   Each K in (1, K(pi)) is hit twice: once inside the wall (G) and once past it (G' = 1/(2G), which needs G in [1/2, 1/sqrt2)); both give the same k.
4. What the mean <K> = 2 is in the tree. Passed readings:
   - EXIT IDENTITY (the finding): for a band whose k = 0 and k = pi ends sit at peel positions G0 and G1 (inside the wall), <K> = 1 + 2 G0 G1 / sqrt((1 - 2 G0^2)(1 - 2 G1^2)) (40 random pairs, quadrature vs formula worst 5e-40). Hence <K> = 2 exactly when G0^2 + G1^2 = 1/2: the squares of the two end positions add to the wall value G^2 = 1/2 (40 random pairs on that circle, worst |<K> - 2| = 4e-37). Equivalent forms: 1/K(0) + 1/K(pi) = 1 (since 1/K = 1 - 2G^2 inside), and the geometric mean of the Petermann excesses sqrt((K(0)-1)(K(pi)-1)) = 1. All pass to 1e-40 on all four bands, with G0 + G1 values 0.2408 / 0.6648 (u=0.5), 0.1012 / 0.6998, 0.2081 / 0.6758, 0.3719 / 0.6014.
   - (a) mean of K over z with measure dk induced by k(z), over [z0,z1]: 2.0000000000 on all four bands (to 1e-20). This is the change of variable back to uniform dk, so it is the band mean restated, not an independent hit.
   - (b) pair across the wall, G G' = 1/2: K(G) = K(G') identically (checked at G = 0.5, 0.55, 0.6, 0.65, 0.7, diffs <= 2e-38). So the pair mean in any weight is K itself; it equals 2 only for the pair (G = 1/2, G' = 1), i.e. z = 3 and the rim.
   - (c) three perpendicular pairs ij, jk, ki: identical K (spread <= 7e-40 at z = 2,3,4,5). Mean is K(z): 2 only at z = 3 (z=5 gives 9).
   - (e opposite) full turn of the loop-fed signal, Gamma_n = -sin(phi) sin(n theta): for the arms +z and -z, sin^2(phi) = 2G^2 exactly (worst error 1.2e-15 over 27 values of z inside the wall). So the turn-mean of Gamma_n^2 is G^2 and the turn-mean of 1/(1 - 2 Gamma_n^2) is 1 - 2G^2 = 1/K_W(z). This is a real relation in the tree (the signal average returns the loop's own 1/K), but its value is 1/2 at z = 3, same as K = 2; it does not give the band mean.
5. Failed readings (value vs 2, exit band u = 0.5; the other three bands fail the same way, numbers in s2_out.txt):
   - mean of K, uniform in G over [G0,G1]: 2.3101; uniform in z: 3.0018; uniform in ln z: 2.5247; uniform in loop turn angle theta: 3.3926; uniform in 2G^2: 2.6445.
   - mean of 1/K with dk(z): 0.6798 (closed form 1 - u^2/(w^2 - v^2)), not 1/2.
   - end values K(0) + K(pi) = 9.754, K(0) K(pi) = 9.754 (equal, a curiosity: (K0-1)(K1-1)=1), sqrt(K0 K1) = 3.123: none is 2.
   - (e) mean of K(Gamma_n) over one turn = 1/sqrt(1 - 2 sin^2 phi) for 2 sin^2 phi < 1, divergent otherwise. None of the 7 prepared arms at z = 2,3,4,5 gives 2 (z=2 arm z: 1.3416; arm (1,1,1): 1.6429; z=3 arm (1,1,1): 1.0746; z=5 arm (1,1,0)-like: 1.5854; the rest diverge, sin^2 phi = 1). K-mean = 2 would need sin^2 phi = 3/8: no tree arm tested has it. Arms uniform on the sphere: mean sin^2 phi = 2/3, so mean 1/K = 1/3 (analytic only, untested numerically).
   - mean of K over three pairs at z = 5: 9, not 2.
6. z = 3 on the band. Yes, a special place, but only as a definition-level one: at z = 3 the loop has K = 2 = 1/(1-2G^2) with G = 1/2, R = 1/4 (R = G^2). On his exit band the band mean is also 2, and K(k) = <K> holds at the single k where E(k)^2 = E(0)E(pi) (for ANY band: K(k) = <K> iff E(k)^2 = E(0)E(pi)); on an exit band E(0)E(pi) = u^2 so that k is k*, and z = 3 and the rim both land there. Positions: k*/pi = 0.7788 (u=0.5), 0.9086 (0.25), 0.8098 (0.45), 0.6474 (0.65). Not the band centre and not a fixed fraction. Off the exit line, z = 3 still picks the k with K = 2 (if K = 2 lies in [K(0),K(pi)]) but that k is not the mean-point and <K> is not 2.

## What is not shown / untested
- I did not find an independent tree quantity that equals <K> = 2 apart from the end-pair circle G0^2 + G1^2 = 1/2 (which is the exit condition E0 Epi = u^2 written in the peel coordinate; it is exact and new in that form but I did not look for it in his papers: grep of his exit-line files shows E(0)E(pi) = u^2 and gamma = 1 only).
- The loop-to-band map is one k per z; I did not check whether his edge ladder (Thm 5.4) has any link to the z-axis.
- Arms: only 7 prepared directions; analytic sphere averages untested numerically.
- Past-wall: the arm relation sin^2 phi = 2G^2 was tested inside the wall only (the anatomy used there is defined inside).

## His definitions used (quoted)
- /home/claude/notes/NOTES_15_DRIVE_LIGHT_WEIGHT_OFFSET.md line 55: "PT-symmetric SSH, h(k) = [[iu, v + w e^{-ik}],[v + w e^{ik}, -iu]], E(k)^2 = v^2 + w^2 - u^2 + 2 v w cos k, u,v,w > 0, v < w".
- line 56: "K(k) = Tr P^dagger P = 1 + u^2/E(k)^2; <K> = 1 + u^2/(E(0)E(pi)); <K> = 2 iff E(0)E(pi) = u^2 iff (w^2 - v^2)^2 = 2 u^2 (w^2 + v^2). At w = 1 ... u = 0.5 gives v_exit = 0.4682 ... exits at u = 0.25, 0.45, 0.65: v = 0.7474014, 0.5291503, 0.2357262".
- line 58: Lemma 5.1, Hermitian band |v' + w' e^{ik}| with v' = (E0 - Epi)/2, w' = (E0 + Epi)/2.
- /home/claude/nov/matter/EXTRACT.md line 17 (G2): "gamma^2 = u^2/(E(0)E(pi)) = K-bar - 1 exactly".
- /home/claude/closure/loop2/REPORT.md sec. 3 (map u = |b-part|, |v + w e^{ik}| = |a-part|; K_h = K_W).

## Files
/home/claude/harness/workers/T5_band_mean/ : s1_kz.py, s1_out.txt, s2_readings.py, s2_out.txt, s3_arm.py, s3_out.txt, STATE.md

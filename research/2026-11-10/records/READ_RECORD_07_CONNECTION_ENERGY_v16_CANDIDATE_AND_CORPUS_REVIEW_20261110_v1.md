# Read record 07 — Connection Energy v16 candidate, its corrections to v15, and the Corpus Review
Jeromie Beasley's corpus. Record made 10 November 2026.
Sources (attached 10 Nov): Connection_Energy_v16_Sources_and_Audit.zip, nonnormality_v15_code_and_sources.zip.

## Coverage, exactly
READ IN FULL: README.md; MERGE_DECISIONS.json (17 decisions); Combined_Review.html; v16 tex lines 164-337 (flow theorem, proposition, scope) and 669-690 (permutation-cycle bridge); companion_routes/Corpus_Review.txt; scripts/exploratory/REGISTRATION.md and RESULTS_helper.md; RECONCILIATION_LEDGER_v15.md header and all 81 FIXED / LEFT OUT rows.
NOT READ: the 193 IN rows of the ledger (statements of v15, read in record 06); the six section patches in review_evidence/ (line-level v15 -> v16 differences for primes, arith, wall, records, penrose); the four agent audits; the four shell derivations in companion_routes/; the scripts; nonnormality_connection_energy_complete_v1_1.pdf Parts II on (pages 95-229: statement map, theorems, source, verification, numerics).

## v16 corrects v15. Each line below overrides the matching line of record 06.
1. EQUAL BOOKS IS NOT THE WALL. One edge, D0 = sigma_z, D1 = sigma_x, U = I: E_- = E_+ = 4, (DA)^2 != 0, H has four distinct eigenvalues 2^(-1/4)(+-1 +- i). Balance gives only Re Tr X^2 = 0. Nilpotence at balance holds ONLY in the real traceless 2x2 family.
2. FLOW, now proved (Theorem + Proposition): for K' = -2[C,K], C = [K,K*]:
   dE_-/dt = -||[C,K]||^2,  dE_+/dt = -||CK + KC||^2,  CK + KC = [K^2, K*].
   E_- stationary iff K normal; E_+ stationary iff K^2 normal (weaker). Every traceless 2x2 has K^2 scalar, so E_+ is CONSTANT on it. Example K = [[1+i,2],[0,-1-i]]: E_- = 12, E_+ = 4, rates -1536 and 0.
   8 int Phi dt = ||K(0)||^2 - sum |lambda_j|^2 (Henrici budget, exact). lim E_+ = (1/2) sum (Im lambda_j^2)^2. The flow selects neither equal books, nor an exceptional point, nor Koide.
3. Koide preimages on 37a1: 47 primes, not 162.
4. Clock rate: pure operator scaling scales both books quartically; scaling D at fixed unitary edges scales them quadratically. A fixed scalar offset makes the ratio depend on rate: G = s[[1,1],[-1,2]] + I has books (1,25) at s = 1, (16,256) at s = 2.
5. Reversal: an inverse-reversal gain needs rho_ji = rho_ij*; the raw skew matrix has A_ji = -A_ij*; the adjoint connection erases that minus.
6. Negative companion branch c < -2: M^N/||M^N|| alternates sign; stress still tends to 4/c^2. At the bound the TRACELESS part is nilpotent; the full determinant-one companion is invertible.
7. TWO DIFFERENT B's. For a spectral projector Pi: C - C^2 = B_Pi B_Pi*. The Hamiltonian block B_H = PHQ governs the compression defect PH^2P - (PHP)^2 and the hidden memory. Scaling H leaves Pi unchanged and scales B_H. Rank(B_H) does not bound the number of fractional occupations (4x4 example: rank B_H = 1, occupations 1/5 and 4/5, rank B_Pi = 2).
8. Route recovery: scalar paths (1,2,1) and (2,1,2) have the same books (1,9) on both edges.
9. Interface log det needs the whole Hermitian block positive.
10. Penrose: algebra kept; the fold is leading order only.
11. Arithmetic runs: archived, not reproduced; the 0.468 failure stands; inference from murmuration statistics downgraded.
12. RESTORED: permutation-cycle -> projector compression -> odd zeta (complete-complex paper v7, Props 18, 20):
    det(I - tU) = prod (1 - t^l)^(a_l);  K_U = Q_U*(I - P_I)Q_U = (2I - U - U*)/4, eigenvalues sin^2(pi j/l) on an l-cycle;
    D_l = 2 log 2 - 1 - S_l/l = sum over m >= 1 with l | 2m of 1/(m(4m^2 - 1));  l^3 D_l -> 2 zeta(3) (even l), zeta(3)/4 (odd l);  D_l = D_2l for odd l.
    Checked there to 2e-60 for l = 3,4,7,8,31,32,63,64.

## Corpus Review (22 October) — what it says about the knot work
- Dirac Time Thm 13.2 (arc count = half |signature| away from end points) was independently checked on 248 coprime torus pairs, 27,697 arcs, 55,642 open intervals, in rational arithmetic. Not checked: every APS normalisation; a boundary-to-bulk gluing map.
- REVERSALS MUST BE NAMED, they are different operations: sector sign; transpose; complex conjugation; complement P -> 1 - P; sheet inversion; lambda -> -lambda; lambda -> 1/lambda; knot mirror (reverses signature, keeps the Alexander polynomial up to units; a unit-circle root permits but need not force a signature jump).
- T = [[Sigma, M+Q],[M-Q, -Sigma]]: T^2 = (M^2 + Sigma^2 - Q^2) I. A null charge vector is a nonzero nilpotent.
- Critical damping does not minimise finite-tolerance settling: 2% settling time 3.755841 at zeta = 0.8 against 5.833922 at zeta = 1.
- Version history: the IQGT constant-one operator-norm subspace estimate needs stronger spectral-separation hypotheses (interlaced-spectrum counterexample; unrepaired in the v7.3.1 HTML). Price's printed Fourier-projector assembly has an extra conjugation. Directional's old universal negative trace-log correction for a skew perturbation is false (correct: nonnegative).
- VOTKP Thm 3.1: a reduced readout R closes under L only when ker R is L-invariant. K_eff = A - B D^-1 B*.

## Ledger rows LEFT OUT of v15 that touch the knot work
- S155: the old claims for 8_19 = T(3,4) — Alexander polynomial "3 - 5t + 3t^2" and a hyperbolic volume — are FALSE (a torus knot has no hyperbolic volume).
- R70: Levine-Tristram signature changes at an Alexander root by 2j with j = m (mod 2). Left out as "not connected". It IS the step rule behind Dirac Time Thm 13.2.
- R68: knot invariants under mirror; triangle distances lose the oriented-area sign.
- R44: triangle defect = moved points of the S3 holonomy; 2 - 2 cos 2x = 4 sin^2 x.
- S42/S139: the refraction law R1 sin^2(theta1) = R2 sin^2(theta2) of the black-hole paper is UNDER AUDIT (the sin -> sin^2 step). IQGT's g_par sin^2(theta) = const with index sqrt(g_par) is Snell squared and is not that law; the two must not be merged.
- S122: branch findings-v3 (commit 80b2316, 56 pages) was not on disk for that session.

## Exploratory results (helper)
- T3 climb or swap: with generic gains all moving Hashimoto eigenvalues lie in ONE monodromy orbit; swaps are typical, climbs (cycles of length >= 3) a minority on loops enclosing 2-3 exceptional points; symmetry (trivial gains) splits orbits and gives pure swaps. Loop around w = 0 on C6 gives [6,6]: a Puiseux climb, not an exceptional-point effect.
- T4: the mirror needs U_ji = U_ij^-1, not unitarity; unitarity only puts the poles on the circle.
- T5: no mirror in graph murmuration for sign det A_s; a positive split for (-1)^(frustration index) on cubic graphs, mechanism open.

## What this changes for the vacuum-disk work — UNTESTED unless marked
A. Record 06 lead 6 ("the complete structure sits on the wall q = 0") must be stated in the restricted form: parabolic peripheral holonomy means the TRACELESS PART of a real 2x2 block is a nonzero nilpotent. It is not a statement about equal books in general (correction 1).
B. K_U = (2I - U - U*)/4 with eigenvalues sin^2(pi j/l) is the count form of IQGT 12.2 (theta = phi/2, count sin^2) on a cycle. The arc ends of Dirac Time Thm 13.1 are alpha+- = k/(2pq) with k = uaq +- vbp, so sin^2(pi alpha) = sin^2(pi k/(2pq)): the arc end is the j = k eigenvalue of the compression of a 2pq-cycle. This follows by arithmetic from the two statements; it is a relabelling and by itself predicts nothing. What would make it more than that: the entropy deficit D_l of the SAME cycle is fixed by l alone, so if the 2pq-cycle is the right object, a quantity of the torus knot should equal D_2pq = D_pq (pq odd) or its even-l form. No such quantity has been identified. Not run.
C. D_l = D_2l for odd l is an exact odd/even doubling. The torus law carries (-1)^a and the staircase step k = uaq +- vbp mixes parities. Whether the direction -k^2/(pq) respects l <-> 2l is a one-line check. Not run.
D. The corrections separate B_Pi from B_H. In the vacuum-disk work the same care applies: the volume/direction pair is read from the projector side (overlaps), the decay from the Hamiltonian side.

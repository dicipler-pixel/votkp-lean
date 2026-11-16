# Open questions across the VOTKP work — tests run 10 November 2026 (v3: sections 10-12 added)
Jeromie Beasley's corpus. Each test: the question, why the check decides it, the kill line written before the run, the result. Scripts are in the same delivery; each carries its SCRIPT name.

## 1. The missing torus-knot roots (vacuum disk, open problem 1) — ANSWERED
Question: 8_19 = T(3,4) and 10_124 = T(3,5) showed one direction each; the component count says 3 and 4.
Prediction written first (from the arc ends of Dirac Time Thm 13.1, direction -k^2/(pq), k = aq +- bp): the components are 3 and 4 but the DISTINCT directions are two each: 8_19 {11/12, 2/3}; 10_124 {14/15, 11/15}.
Check: the paper's own solver, unchanged, more starts, plus a second drawing (the torus braid closure). Kill: any non-degenerate rational root outside the predicted set.
Result (TORUS-ROOTS-01):
- 8_19, KnotInfo drawing, 6,000 starts: 11/12 only (881 times).
- 8_19, braid drawing (s1 s2)^4, 6,000 starts: 11/12 (579 times) AND 2/3 (106 times). Nothing else.
- 10_124, KnotInfo drawing, 5,000 starts: 14/15 (266 times) AND 11/15 (once). Nothing else.
- 10_124, braid drawing (s1 s2)^5, 5,000 starts: 14/15 (238 times) AND 11/15 (45 times). Nothing else.
Both predicted roots found; no root outside the set. The one-k join (piecing map section 4) now holds on T(3,4) and T(3,5) as well as T(2,q).
New fact from the run: the KnotInfo drawing of 8_19 never reaches 2/3 in 6,000 starts while the braid drawing reaches it 106 times. For torus knots the root list depends on the drawing at any fixed budget; the 13-of-13 drawing-independence result was on hyperbolic knots. TORUS-ROOTS-02 looked at the solutions the filter drops: on 8_19 they hold no 2/3, so the filter is not what hides it; that drawing does not reach the component (2,2).

## 2. The silent double walls (vacuum disk open problem 6; VOTKP Table 6) — READING KILLED AS STATED, REPAIRED
Reading under test: a silent double wall is two opposite hands cancelling, that is, two eigenvalues of H(omega) crossing zero in opposite directions.
Check: KnotInfo lists the signature left / AT / right of each root and the nullity. Two opposite crossings give nullity 2 and the side value at the root; one eigenvalue touching zero gives nullity 1 and side value +-1. Kill: a silent double wall with nullity 1.
Result (SILENT-WALLS-02), all 575 double unit-circle roots:
- jump +-4: 81, all nullity 2.
- silent: 494, of which 376 have NULLITY 1 (one eigenvalue touches zero and turns back) and 118 have nullity 2 (two opposite crossings).
- the 61 silent walls in infinite-order knots: 45 touch, 16 are opposite crossings. Finite order: 44 touch, 21 opposite.
- 8_20, the trefoil's square, is a TOUCH (signature 0, 1, 0; nullity 1), not an opposite crossing.
So there are two kinds of silent wall. The opposite-hands picture holds for 118 of 494. The other 376 are a single level that reaches zero and reflects. In IQGT terms (section 8) the first is two sheets meeting, the second is a wall where the motion stops and turns back. The touches are lopsided: 233 from above (at-side -1) against 143 from below.
What this leaves open: why a given squared factor gives a touch or a crossing. Concordance order does not decide it.

## 3. Do the never-turning knots stand apart in direction? (piecing map 5a; Two Trees section 9) — KILLED
Check: Chern-Simons of the 26 two-bridge knots, folded so mirrors agree. Kill: the four hyperbolic never-turners (6_3, 7_5, 8_7, 8_8) sit inside the spread of the nineteen that turn.
Result (NEVER-TURN-01): never-turners 0, 0.121, 0.132, 0.117; turners from 0 to 0.222. Inside. Direction does not separate them.
Lead-finding over every KnotInfo field (26 knots, many fields, so a lead only): the strongest splitter is braid index (never-turners 2-4, turners 3-5), and it does not separate cleanly. What the four share is still not identified.

## 4. Is there a feature of the bowl at |G|^2 = 1/2? (piecing map section 3) — NO FEATURE IN THE BOWL; A FACT ABOUT THE KNOTS
Check: the exact volume averaged round each circle |G| = r, and the bowl error of real knot tetrahedra by radius. Kill: nothing changes at 1/2.
Result (BOWL-HALF-01): the circle average is smooth through 1/2 (0.4430 there, 43.7% of V0); the series converges out to the rim. No feature. But 99.7% of the 2,777 tetrahedra of knots to 10 crossings lie INSIDE |G|^2 = 1/2 (8 outside). With OPTICS-01 (metals 35/35 outside) the line separates knot pieces from metals almost completely. That is a statement about where things sit, not about the bowl.

## 5. Colour inside the disk: dielectrics (vacuum disk open problem 4) — PARTLY
Statement: clear materials live inside the disk and would fill the bowl region.
Check: all 94 compounds of the refractiveindex.info main shelf with tabulated n, k across the visible, placed by G = (1 - N)/(1 + N). Filling needs radius inside AND angle spread; a transparent material has real N and can only draw the real diameter. Kill for "fill": over 90% of points within 10 degrees of the real axis.
Result (DIELECTRICS-01): 91 of 94 compounds lie inside the line (53% of points inside |G|^2 = 1/4). 80% of points are within 10 degrees of the axis, 96% within 30. So they are inside, and mostly on a diameter. The ones that enter the bowl in two dimensions are 17 absorbing compounds: TiN, VN, TiC, VC, Ti3C2, TiH2, MgH2, MoO2, MoOCl2, SnSe, PtSe2, PdSe2, NbSe2, WTe2, InSb, GaSb, As2Se3. Outside the line: Bi2Se3, Ge2Sb2Te5, PbSe.
Limit: only tabulated sets were read; glasses and oxides given by formula are not in this count and would add to the diameter.

## 6. The twin chain's turning (Two Trees, One Scale test) — rerun and its opposite (earlier today)
No order beyond one step, in the unsigned and the signed turn; a one-step hand about (1,1,1) that reverses with the chain.

## 7. What decides touch against crossing at a silent double wall — ANSWERED (SILENT-WALLS-03)
Proposal written first: the knot's Alexander module at the factor f. A cyclic part Z[t]/(f^2) is one Jordan block: one level touches zero (nullity 1). A split part Z[t]/(f) + Z[t]/(f) is two independent levels (nullity 2). KnotInfo's SECOND Alexander polynomial contains f exactly in the split case.
Check: nullity (from the signature column) against "root of the second Alexander polynomial" (an independent column). Kill: any disagreement.
Result: 575 of 575 agree. Nullity 1: 376, none a root of the second polynomial. Nullity 2: 199, all roots of it.
So the two kinds of silent wall are the two kinds of double root: DEFECTIVE (one Jordan block; the level touches and reflects) and SPLIT (two levels). A defective double root can never jump; all 81 jumps of +-4 and the 118 opposed crossings are split roots. This is standard theory once stated (the nullity counts the module's summands), so it is a reproduction; what it does is close open problem 6: the 61 silent walls in infinite-order knots ARE covered. 45 are defective; 16 are split with opposite signs.
Join to Non-Normality v15 section 10: the touch wall is a nonzero nilpotent at a double root — the wall of that paper, found in the knot's own form. The opposed crossing is the mirror-fusion picture of BRANCH-CUT-01. Both readings were right, each for its own kind.
What is left of the question: among the 199 split roots, what sets the two signs equal (81) or opposite (118).
Direction of the touches: where the side signature is not zero, 99 move toward zero and 33 away.

## 8. The whole twin chain stepped by its true ratios (CHAIN-WHOLE-03)
Each pair steps by the peel ratio a'/a along the arm of its end digit; 107,405 twin pairs to 2 x 10^7.
Frame turn of the whole product: 9.87 deg at 10^5, 11.62 at 10^6, 12.07 at 10^7, 12.08 at 2 x 10^7; axis close to -j (+0.107, -0.993, -0.052) and still creeping. Distance over path length 0.585, falling slowly.
Reading: the turn settles because late steps are tiny; it is set by the first few pairs. Shuffling the arms gives 23-29 degrees about other axes, and the same distance ratio (0.59). So the settled turn is a number of the early chain, not a new record of the primes, and the distance ratio does not see the order at all.

## 9. Recent GitHub, checked 10 November
- companion-matrix-lean (pushed 9-10 Nov): Lemma A, Lemma B, Theorems 1 and 2 of the companion-matrix paper in Lean; Lemma A(ii) Phi(x y^T) = 1 - (x.y)^2 is the same identity as Non-Normality v15 (53).
- votkp-lean: branch claude/votkp-research-20261107 (7 Nov, path notes, vacuum disk v1, old Grok chats salvage); claude/matter-disk (4 Nov); theta-colour-formalization (1 Nov); main at Two Trees v4 (31 Oct).
- EJ-base-prime-pattern, revision 7 (4-5 Nov), with Elizabeth Johnson: the base-10 prime pattern, the colour wheel Z/W (viable exactly for W = 2p), census 3^(n+1) - 2^(n+1) of admissible words, Lean. Its own final statement already records: equal consecutive twin gaps are SUPPRESSED (0.64 of chance); a Snell-type refraction at the joints is null; the colour wheel says nothing about prime gaps (the sieve's symmetry fixes them). Its literature file names Lemke Oliver-Soundararajan. The one-step hand found today in the chain's frame (i -> j -> k preferred) is the same suppression of repeats seen through the tree.
- No BallJoins file with J9 or J10 is on GitHub yet; One Tree, One Ball and Two Trees, One Scale are not in any repository I can see.

## 10. The touch wall is a Jordan block, checked on the Seifert matrices (WALL-NILPOTENT-04)
For every double root whose knot has an invertible Seifert matrix listed (198 of 575), the monodromy h = V^-1 V^T was built and the kernels of (h - lambda) and (h - lambda)^2 measured. Kill: a kernel dimension that differs from the listed nullity.
Result: 198 of 198 agree. All 121 touches have kernel dimensions 1 then 2: one Jordan block, (h - lambda) a nonzero nilpotent on the root space. All 77 split roots have 2 then 2. The other 377 roots have no usable Seifert matrix in the table and rest on section 7.

## 11. Why the commutator limits take the values they do (Two Trees section 9, question 4) — HALF ANSWERED, by a result already in UPG
k = 2 - tr[a,b] equals |lambda - 1|^2 for a turning commutator: UPG's relator defect delta, with delta + g^2 = 4 (UPGTorusAnchor.unit_defect_add_guard, Lean). The rotation band 0 < k < 4 is UPG's admissible domain.
Check (DEFECT-JOIN-01): each printed limit value against 4 sin^2(pi j/d), d up to 30. Kill: an m = 1 value with no match.
Result: 1, 2, 3 = d 6, 4, 3. phi^-2, phi^2 = d 10 (j = 1, 3). (2cos(j pi/7))^2 = d 14 (j = 5, 3, 1). All eight m = 1 values are clock-and-shift defects (UPG Prop 4.9). The values 1/2, 1/4, 1/9, phi^2/4, phi^-2/4 match no clock value: the division by m^2 is still open.
Lead, not tested on a new knot: in the census d = 10 occurs with q = 5 (6_1, 7_2) and d = 14 with q = 7 (8_1): d = 2q.

## 12. Which two-bridge knots never turn (Two Trees section 9, question 3) — CENSUS EXTENDED, NOT SOLVED
NEVER-TURN-02 redoes the band test at 40 digits for all 50 two-bridge knots of up to nine crossings. It reproduces the paper's 7 never / 19 turn, and finds four more never-turners at nine crossings: T(2,9); 27/5 = [5,2,2]; 29/9 = [3,4,2]; 55/21 = [2,1,1,1,1,1,2].
Families read off that list, then tested on knots outside it (NEVER-TURN-03, with 80-120 digit rechecks):
- [a, 2, 2], a odd (17/5, 27/5): 37/5 and 47/5 predicted never — both never. HELD.
- [a, 1, 1, 2], a even (13/5, 23/5): 33/5 and 43/5 predicted never — both never (43/5 showed a false turn at 40 digits and none at 80; the cancellation the paper warns about). HELD.
- [a, m, 2]: m even never, m odd turns: 41/13 and 47/9 never, 35/11 turns. HELD (three of three).
- golden [2, 1^n, 2]: guessed never for n = 2, 5, 8 and turn for n = 0, 3, 6. 89/34 (n = 6) is NEVER at 120 digits. FAILED as guessed. Known so far: n = 0, 3 turn; n = 2, 5, 6 never.
  The 200-digit run on 233/89 (n = 8) had not finished when this was written; its 40-digit 'turn' is not trusted.
What the never-turners share is still not a single rule. The three families that held all end in 2 with an even block before it, or in 1, 1, 2 after an even entry.

## Not run, and why
- The sign of g in z(a) = kappa - g/(a - d): the fitted kappa, g, d are not in any file I hold.
- Thomas rotation per edge; the 120-degree corner against a pi^2/3 shift on 7_4 and 7_7: no statement of this in v1.2, v5, the path notes or the code archive to test against.
- Two Trees section 9: a return to the origin at a power-of-2 ratio (search already at length 14); the zero set of the relator area. (The limit values are now half answered, section 11.)
- VOTKP v2.0 section 17 items that need measurements or outside data (measured film curves, Og second ionisation energy, cluster tables, glueball spectra at other N).
- The arithmetic of P_K through the trace field; prior art on the circuit polynomial and the sl(N) climb.

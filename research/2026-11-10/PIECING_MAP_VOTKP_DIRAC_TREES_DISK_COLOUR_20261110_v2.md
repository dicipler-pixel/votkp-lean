# Piecing map v2 — VOTKP, Dirac Time, Two Trees, the vacuum disk, colour
Jeromie Beasley's corpus. Made 10 November 2026 from full reads; every line names its source. "CHECKED" = run today. "UNTESTED" = not run.

## Read in full for this map
Dirac Time v3.1; vacuum disk v5; Two Trees in One Ball v4 (body, sections 1-9; Lean and script appendices not line by line); research path notes of 7 November (votkp-lean branch claude/votkp-research-20261107, all 60 k characters); IQGT v6-v7.3.1; What the Present Must Keep v1.1; Non-Normality v15 and the v16 corrections.
Now also read in full: VOTKP v2.0 (sections 1-18, appendices). NOT read yet by me: VOTKP v2.9 sections 19-22; Colour Selects the Leader v1.2 itself (only the path-notes account of it); The Weight Between; Matter, Then On Down; the confirmation run report v2; the one-tree material (not yet located under that name).

## 1. One coordinate runs through all five
Gamma = (z - 1)/(z + 1) = tanh(tau/2); steps multiply ratios and add by x (+) y = (x + y)/(1 + xy); distance from the centre is ln z. (VOTKP Thm 8.1, 15.1, Cor 15.2.)
- Peel step: ratio z between two levels.
- Garrett's tree: norm step 5, Gamma = 2/3, a boost of rapidity ln 5 along the quaternion axis (Two Trees 2.5, 4.1).
- A knot's meridian on its real peripheral curve: boost of length 2x, Gamma = tanh x (Two Trees 6.1). Longitude: boost of length 2|y| (6.4).
- Colour: reflection Gamma = (1 - N)/(1 + N); centre = vacuum/index match, rim -1 = the conductor (path notes P1, OPTICS-01).
- Vacuum disk: G = (z - w)/(z - w-bar), w = e^(i pi/3); centre = regular tetrahedron, rim = flat, mirror outside (vacuum disk v5 Prop 1). This one is a half-plane-type map, not (z-1)/(z+1); the two must not be mixed.
- Scalar edge of the two books: r = tanh((1/2) ln(d_i/d_j)), the signed record the books lose (Non-Normality v15 eq. 20, section 11).

## 2. Straight steps add, turns leave a rotation
- Two perpendicular steps of Smith size Gamma leave a rotation with tan(theta/2) = Gamma^2 (Two Trees 4.7, Lean).
- Order matters only through a phase (VOTKP 15.2).
- The same split everywhere: climb = continuous, kept by even records; turn = kept only in a phase or an integer.
  - knot: volume = distance from the vacuum; Chern-Simons = Neumann's winding integers (vacuum disk v5; path notes WINDING-CS-01: 1 of 79 without the integers, 454/454 with them).
  - film colour: lightness follows |Gamma|; chroma follows the integer film order; hue the fractional phase (path notes COLOUR BRIDGE).
  - two books: route |r_j| kept, signs (endpoint) lost (Non-Normality v15 eq. 97).

## 3. The line Gamma^2 = 1/2 appears four times
- Garrett's boosts: Schottky above, free but not discrete below (Two Trees 5.3, 5.4).
- Knot meridians: below it, crossing axes always give a rotating commutator (Two Trees 8.6).
- Elements: metals 35/35 above, non-metals 0/6 (path notes OPTICS-01).
- Colour bridge: 96% of metals lie beyond |G|^2 = 1/2 in the vacuum-disk frame; knot tetrahedra sit inside (median 0.50).
UNTESTED: whether the vacuum-disk bowl has a feature at |G|^2 = 1/2 (the bowl series is known to quartic order; nothing has been looked for at that radius).

## 4. TORUS KNOTS: one integer k, three papers. CHECKED today (JOIN-K-01, T(2,3), T(2,5), T(2,7): all match)
- Two Trees Thm 8.7: on a torus knot the product ab of the two meridians is a ROTATION of finite order, tr(ab) = 2 cos(k pi/q), k odd. The meridian axes never cross; the commutator never turns.
- Vacuum disk v5: torus knots have zero decay and direction -k^2/(pq) mod 1.
- Dirac Time Thm 13.1: the arc ends sit at alpha = k/(2pq), k = uaq +- vbp the staircase step; lift beta = a/2 - pq alpha.
The same odd k gives the printed roots of the Riley relation in t = tr(ab) AND the printed directions: k = 1 for 3_1; 1, 3 for 5_1; 1, 3, 5 for 7_1.
Reading, in the corpus's own terms: a torus knot is the case where two peel boosts (the meridians) compose to a PURE turn of finite order — all turn, no climb — and that is why it has zero volume and a pure direction. The direction is -4pq alpha_end^2 = -(alpha_end) x (4pq alpha_end): the END-POINT PRODUCT of the arc-end angle with the lift slope. This is the repair proposed for carried item 3 (the total turn along the arc is linear; the direction is the product at the end, i.e. the area of the triangle under the linear lift).
Limits: the product form is arithmetic once alpha_end = k/(2pq); the content is that ONE k serves all three. Only T(2,q) is checked, because Two Trees proves the t-polynomial only for n = 3, 5, 7. For T(3,4), T(3,5) it is UNTESTED.

## 5. What this predicts for hyperbolic knots — UNTESTED, stated so it can be run
On a hyperbolic knot ab is not a pure rotation. Two Trees gives tr[a,b] - 2 = -v(tr(ab) - 2) and a census of 26 knots (19 turn, 7 never). The vacuum disk gives each knot a decay and a direction. If section 4 is the right join, then:
 (a) the seven knots whose commutator never turns (three torus knots, 6_3, 7_5, 8_7, 8_8) should stand apart in direction from the nineteen that do. No evidence yet either way: 6_3 has direction 0, but so does 4_1, which turns — both are amphichiral, so that zero is forced. The test needs 7_5, 8_7, 8_8 against chiral knots that turn.
 (b) the limit values k_inf of Two Trees census 8.8 (1, 2, 3, 1/2, 1/4, 1/9, phi^2, ... all of the form (2cos(j pi/n)/m)^2, "why these values appear is open") are squares of traces of finite-order rotations — the same kind of number as tr(ab) on a torus knot. Open question 4 of Two Trees section 9 and the torus directions may be one question.

## 6. Where colour stands
From the path notes only (the colour paper itself is still to be read): Colour Selects the Leader splits the colour metric into a brightness line and a chromatic sphere, and has two complementary ports. The path notes' own verdict (P4): no card bridges knots and seen colour; the CIE eye is a Gram-type reading and cannot carry handedness. What does carry over is the frame, not the eye: the film's integer order beside its continuous lightness is the same integer-beside-continuous split as windings beside volume. UNTESTED as more than that. Dielectrics to fill the disk interior were named as the next colour step on 7 November and not run.

## 7. Carried items, status
1. Staircase step and direction -k^2/(pq): staircase = Dirac Time 13.1(3); direction equal at both arc ends (TORUS-DIRS-03); now tied to tr(ab) (section 4).
2. z(a) = kappa - g/(a - d) as VOTKP 5.3 with one hidden level: not re-examined — needs VOTKP read in full.
3. Linear total turn: explained by beta = a/2 - pq alpha; repair = end-point product (section 4). The offset a/2 and the sign (-1)^a have not been put through a check.
4. Thomas rotation per edge; 120-degree corner vs pi^2/3 on 7_4 and 7_7: UNTESTED. Note 7_4 and 7_7 both have a "0+" branch in Two Trees census 8.8 (a rotating commutator whose angle shrinks to 0).
No failed construction has been found today, so nothing was added to the equation file.

## 8. Added from the full read of VOTKP v2.0
- TORUS = PURE TURN is stated three times in the corpus: VOTKP A.10 (on a branch L = eps M^-k the volume form vanishes identically, "the potential vanishes while topology and loading do not"); Two Trees 8.7 (ab is a finite rotation); vacuum disk (zero decay).
- TREFOIL ARC: VOTKP 13.7 prints the arc 1/12 < alpha < 5/12 with L = -M^-6. Dirac Time 13.1 ends k/(2pq) = k/12 give k = 1 and k = 5; -k^2/6 mod 1 = 5/6 at both ends; the vacuum disk prints 5/6. CHECKED by arithmetic on the printed numbers.
- ORDER LIVES ONLY IN THE PHASE (VOTKP 15.2): the (+)-sum is commutative, so a composite carries no order; a stack at zero phase telescopes; the phase between additions is a Thomas rotation. Gluing edges: product of shapes = 1 is the (+)-sum closing to 0 (an identity); the logarithms close to 2 pi i, and that integer is what (+) cannot see. This is the corpus's own reason the twist is in the winding integers.
- CARRIED ITEM 2: z(a) = kappa - g/(a - d) matches VOTKP 5.3 with one hidden level, kappa = A, g = -BC. For a Hermitian coupling g must be negative real. That is a test the fitted g can fail; UNTESTED (fitted values not in hand). VOTKP 5.9: the sign of the hidden level is exactly what a shared record cannot see.
- INSIDE / OUTSIDE ONE CIRCLE: film reflects more than bulk iff the echo is outside a circle fixed by the front surface (VOTKP Thm 6.2); geometric solution inside the vacuum disk, mirror outside, flat on the rim. Structural; UNTESTED.
- FIFTH APPEARANCE OF Gamma^2 = 1/2 (CHECKED from printed tau): alkali first steps are above it for Li, Na, K, Rb, Cs (0.75, 0.65, 0.58, 0.55, 0.51); Fr is below (0.48), and Fr is where the column line breaks. Every pure shell wall is below (largest 9/25).
- VOTKP v2.0 itself says: "no correspondence between elements and knots" and lists "the elemental-knot bridge itself" as open. The joins above are between the KNOT side of VOTKP, Dirac Time, Two Trees and the disk; the atom side shares the coordinate and the line only.

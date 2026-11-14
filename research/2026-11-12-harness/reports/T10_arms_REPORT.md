# T10_arms: do the arms of the trees on 5, 7, 11, 13 give the crystal coordination shells, and how do two balls join?

Work: Jeromie Beasley, "Two Trees in One Ball". All numbers exact (integers, fractions, sympy) or mpmath at 60 digits. Scripts and raw outputs sit beside this file (s1_*, s2_*, s3_*, s4_*, s5_*). No web, no fitting.

## 0. Results first

The conversation claim, checked sentence by sentence:

| Sentence | Verdict |
| :-- | :-- |
| A tree on a prime p has p+1 arms at every node | TRUE as a count of normal-form quaternions, for all eight primes (3, 5, 7, 11, 13, 17, 19, 23). As distinct DIRECTIONS it is p+1 only when no quaternion has real part 0; at p = 3, 11, 19 (real part 0 occurs) the arms double when the inverse is included: 8, 24, 32. |
| 5: axes, octahedron, 6 neighbours, simple cubic | TRUE for the arm set (his own six generators, PeelTrees.lean:45). FALSE as a lattice at depth 2 (section 3). |
| 7: body diagonals, cube, 8 neighbours, body-centred cubic | TRUE only for the eight LPS quaternions 2 + (+-1,+-1,+-1) (the 8-arm tree). His papers do NOT use these: the ln 7 tree in the paper and the Lean files has the same six axes as ln 5 (paper l.167, PeelTrees.lean:235). |
| 11: face diagonals, cuboctahedron, 12 neighbours, face-centred cubic | FALSE in the normal form of his papers. The 12 quaternions of norm 11 in that form (real part 0) have imaginary directions (+-1,+-1,+-3) and permutations: 24 directions with the inverse, combinatorially a rhombicuboctahedron (8 triangles, 18 squares), not a cuboctahedron. The face-diagonal set (+-1,+-1,0) appears at 11 only as the real-part-3 shell (12 quaternions 3 + (+-1,+-1,0)), which that normal form does not select. TRUE in that one alternative selection. |
| 5 and 7 are dual solids | TRUE for octahedron (5) and cube (7-LPS-8): face normals of one are exactly the vertices of the other. Not true inside his six-axis ln 7 tree, where 7 is the same octahedron as 5. |
| 5 and 7 are the pair across the wall | TRUE: (2/3)(3/4) = 1/2 and 1/(2 G5) = 3/4 = G7 exactly. Extra fact: (z-3)(z'-3) = 8, so the only integer pairs across the wall are (5,7) and (4,11). |
| 13 = 6 axes + 8 diagonals (bcc first plus second shell, 14) | TRUE: real part 3 gives the 6 axes, real part 1 gives the 8 diagonals, and the set equals the union of the 5 and 7 sets exactly. |

Shells that appear and do not appear (arm sets of the parity normal form, p up to 23):

| Shell | Appears? |
| :-- | :-- |
| 4 (tetrahedron, diamond) | Only at p = 3, only by a sign choice (the real-part-0 elements carry a free sign, q and -q); needs alternating arm sets (bipartite words). Not forced. |
| 6 (octahedron, sc first) | p = 5; also inside 13 and 17 |
| 8 (cube directions, bcc first) | p = 7 (LPS-8 form), p = 3 (doubled form), inside 13 and 19 |
| 12 (cuboctahedron, fcc first) | Never as the whole arm set. Only as a sub-shell: real part 3 at p = 11 and 17, real part 1 at p = 3 and 19. |
| 12 (anticuboctahedron, hcp) | Never as an arm set. Its symmetry group has order 12 (D3h), which is not inside the octahedral group, so no octahedrally closed set equals it. Found once only as a 12-point subset of the 36-direction real-part-1 shell at p = 19 (exact copy given below); no normal form selects it. |
| 14 (bcc first + second) | p = 13 |
| 18 (sc first + fcc first) | p = 17 |

Depth 2 (section 3): the second-level nodes of the 5-tree and 7-tree do NOT reproduce the second neighbour shell of the matching lattice, in any of the three readings of radius. The mismatch is exact and has a closed form; it vanishes only in the flat limit z -> 1.

Two balls (section 4): (5,5) and (7,7) joins are forced; (5,7) is impossible as a pair of translates; (11,11) is forced in the doubled form and in the face-diagonal reading, and in the half-set form of the parity normal form it needs the conjugate copy. Gap at depth n is exactly 2/(p^n + 1), never zero.

B99 side check (section 5): the identity is one line; the paper already states it, but in section 8.7, not 8.4.

## 1. Conventions taken from his files

- PeelTrees.lean:45: `gens = [1+2i, 1-2i, 1+2j, 1-2j, 1+2k, 1-2k]`, six Lipschitz quaternions of norm 5.
- PeelTrees.lean:84-88 (`lps_six`): norm 5, a > 0 odd, b, c, d even, if and only if the quaternion is in `gens` ("the LPS normalisation, p + 1 = 6"). 48 integer quaternions of norm 5 in all (l.83).
- PeelTrees.lean:215-235: `Dir` = six axis directions; `B5 = boost 13 12 5`, `B7 = boost 25 24 7`. The ln 7 tree uses the same six axes.
- Paper v4 text (Two_Trees_in_One_Ball_v4_20261030_1.txt) l.167: "The step ln 7 with six branches is a drawing choice: the LPS tree for the prime 7 branches eight ways (p + 1 = 8), so the six boosts at ln 7 are not that tree."
- Placement (Def 4.1, l.117; notes part 1 section 2): generator 1 + 2u maps to the Lorentz boost B_u of rapidity ln z along the quaternion's own imaginary axis; the conjugate maps to the inverse boost; word g1...gL maps to B_g1...B_gL o; ball point x/(1+t). The paper calls this a choice.
- My extension to a general p (not in his text, untested against it): quaternion a + v of norm p maps to a boost of ratio p along v/|v|.
- The rule "positive odd real part, even imaginary parts" gives nothing for p = 3 mod 4 (a odd and b, c, d even forces the norm to be 1 mod 4). So for 3, 7, 11, 19, 23 I extend with the Lubotzky-Phillips-Sarnak form: a even and > 0, b, c, d odd; if a = 0, take the first nonzero imaginary coordinate positive. This is the form that gives exactly p + 1 for every p (check below). Two alternatives are shown for dependence: NF-B (any a > 0, a = 0 with first nonzero imaginary coordinate positive) and NF-U (all norm-p quaternions).

## 2. Step 1 table: quaternions of norm p, by normal form

NF-A is the parity form above. "dirs" = distinct imaginary directions after adding the inverse (the conjugate), since the boost along -v is the inverse of the boost along v. Octahedral closure: invariant under the 48 signed permutations. All sets below have full symmetry group of order 48 on the sphere.

| p | all norm-p integer quaternions | NF-A count (expect p+1) | real parts in NF-A | NF-A directions (inverse-closed) | angles between arms (degrees: pairs) | hull | closed under octahedral group |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 3 | 32 | 4 (yes) | 0 | 8: (+-1,+-1,+-1); the 4 raw elements are (1,+-1,+-1) | 70.5288: 12, 109.4712: 12, 180: 4 | cube, 8 vertices | yes (raw 4: no) |
| 5 | 48 | 6 (yes) | 1 | 6 axes | 90: 12, 180: 3 | octahedron, 6 vertices | yes |
| 7 | 64 | 8 (yes) | 2 | 8: (+-1,+-1,+-1) | 70.5288: 12, 109.4712: 12, 180: 4 | cube, 8 vertices | yes |
| 11 | 96 | 12 (yes) | 0 | 24: (+-3,+-1,+-1) perms | 35.0968: 24, 50.4788: 36, 62.9643: 24, 84.7841: 48, 95.2159: 48, 117.0357: 24, 129.5212: 36, 144.9032: 24, 180: 12 | 24 vertices, 8 triangles + 18 squares (rhombicuboctahedron type, not uniform) | yes (raw 12: no) |
| 13 | 112 | 14 (yes) | 1, 3 | 14: 6 axes + 8 diagonals | 54.7356: 24, 70.5288: 12, 90: 12, 109.4712: 12, 125.2644: 24, 180: 7 | 14 vertices, 24 triangles (tetrakis-hexahedron type, not uniform) | yes |
| 17 | 144 | 18 (yes) | 1, 3 | 18: 6 axes + 12 face diagonals (+-1,+-1,0) | 45: 24, 60: 24, 90: 48, 120: 24, 135: 24, 180: 9 | 18 vertices, 32 triangles | yes |
| 19 | 160 | 20 (yes) | 0, 4 | 32: 8 diagonals + 24 of type (+-3,+-3,+-1) | 19 distinct angles, smallest 22.0017 (24 pairs) | 32 vertices, 24 triangles + 6 octagons | yes (raw 20: no) |
| 23 | 192 | 24 (yes) | 2 | 24: (+-3,+-3,+-1) perms | 26.5254: 12, 37.8636: 24, 61.7263: 48, 80.9153: 24, 86.983: 24, 93.017: 24, 99.0847: 24, 118.2737: 48, 142.1364: 24, 153.4746: 12, 180: 12 | 24 vertices, 8 triangles + 6 octagons (truncated-cube type, not uniform) | yes |

Dependence on the normal form (counts of quaternions, directions):

| p | NF-A | NF-B | NF-U |
| :-- | :-- | :-- | :-- |
| 5 | 6 q, 6 dirs | 24 q, 30 dirs | 48 q, 30 dirs |
| 7 | 8 q, 8 dirs | 32 q, 32 dirs | 64 q, 32 dirs |
| 11 | 12 q, 24 dirs | 48 q, 60 dirs | 96 q, 60 dirs |
| 13 | 14 q, 14 dirs | 56 q, 62 dirs | 112 q, 62 dirs |

Kill lines (written before running, STATE.md): count p+1 for every p survived; p = 5 axes survived (this is the Lean-checked lps_six); p = 7 cube survived; p = 13 axes + diagonals survived; 11 = cuboctahedron was killed.

Real part by real part (s1b_shells.py), which shows where each standard shell sits:

| p | shells by real part a (number of quaternions with that a > 0; a = 0 counted whole) |
| :-- | :-- |
| 3 | a=0: 8 (cube); a=1: 12 of type (1,1,0) = cuboctahedron |
| 5 | a=0: 24 of type (2,1,0); a=1: 6 axes; a=2: 6 axes |
| 7 | a=1: 24 of type (2,1,1); a=2: 8 diagonals |
| 11 | a=0: 24 of type (3,1,1); a=1: 24 of type (3,1,0); a=3: 12 of type (1,1,0) = cuboctahedron |
| 13 | a=1: 8 diagonals; a=2: 6 axes + 24 of type (2,2,1); a=3: 6 axes; a=0: 24 of type (3,2,0) |
| 17 | a=1: 6 axes; a=3: 12 face diagonals (2,2,0); a=4: 6 axes; a=2: 24; a=0: 48 |
| 19 | a=4: 8 diagonals; a=1: 36 = 24 of type (4,1,1) + 12 of type (3,3,0); a=3: 24; a=0: 24 |
| 23 | a=1: 24; a=2: 24 of type (3,3,1); a=3: 48 |

Diamond and HCP tests (s2_claim.py, s2b_shells.py): a regular tetrahedron sits inside the p = 3, 7, 13, 19 sets, but only as a 4-subset of the cube. At p = 3 the real-part-0 elements satisfy conjugate = minus the element, so the 4 chosen elements point to 4 of the 8 cube corners and the choice is free: (1,+-1,+-1) gives a square, "even number of minus signs" gives the tetrahedron. The diamond reading needs the two tetrahedra to alternate along a path, which his words do not state. HCP: the anticuboctahedron has 12 vertices on a sphere, edge-to-edge distance equal to the radius, and symmetry order 12; the containment search over every orthogonal map found a copy at p = 19 inside the real-part-1 shell (all 36 directions have the same length, the square root of 18): hexagon (3,-3,0)-type, top triangle (4,1,1)-type, bottom triangle (0,-3,-3)-type, all norm 18, squared edge 18, eclipsed (the 60 degree twist of the cuboctahedron is absent). Positive controls: the cuboctahedron was found where expected (3, 11, 17, 19 in the right shells) and not found where it should not be.

## 3. Depth 2 (s3_depth.py, s3b_limit.py)

Readings of radius, declared before the run (a node at depth n, from the centre): R1 = G = |x|/(1+t), the Smith coordinate (this is also the Euclidean distance from the centre in the Poincare ball); R2 = hyperbolic length d = 2 artanh G = arcosh t (ratios equal those of artanh G); R3 = tanh d = |x|/t (the Euclidean chord from the centre in the straight-line model). Nodes are computed with the actual action B_g1 B_g2 o.

Depth 1: G = 2/3 (5), 3/4 (7, six axes or eight diagonals).

Depth 2, exact:

| Tree | class | nodes | G^2 | direction | R1 ratio to depth 1 | R2 ratio | R3 ratio |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 5, six axes | turned | 24 | 72/97 | (13, 5, 0) = (z^2+1, 2z, 0) | 1.29232 | 1.61463 | 1.07141 |
| 5, six axes | straight | 6 | 144/169 | axis | 1.38462 | 2 | 1.07987 |
| 7, six axes (his) | turned | 24 | 288/337 | (25, 7, 0) | 1.23259 | 1.66377 | 1.03846 |
| 7, six axes | straight | 6 | 576/625 | axis | 1.28 | 2 | 1.04080 |
| 7, eight diagonals (LPS) | turned, class 1 | 24 | 192/241 | (13, 6, 6) | 1.19009 | 1.47430 | 1.03498 |
| 7, eight diagonals | turned, class 2 | 24 | 384/433 | (19, 19, 12) | 1.25563 | 1.80176 | 1.03979 |
| 7, eight diagonals | straight | 8 | 576/625 | diagonal | 1.28 | 2 | 1.04080 |

Lattice second shells: sc second shell is 12 face diagonals (1,1,0) at ratio sqrt2 = 1.41421; fcc second shell is 6 axes at sqrt2; bcc second shell is 6 axes at 2/sqrt3 = 1.15470.

Fixed match rule (written before the run): both the direction of every depth-2 node and the ratio in at least one reading. Result: no, for all three trees. Reason: for a turn between perpendicular axes, t = c^2 and x = (s c, s) with c = (z^2+1)/(2z), s = (z^2-1)/(2z), so the turned node leaves the first arm at angle atan(2z/(z^2+1)): 21.04 degrees at z = 5, 15.64 degrees at z = 7, not 45 degrees. Straight depth-2 nodes lie on the arms, R2 ratio exactly 2 (the fourth shell of sc, 2:1), but they are not the second shell.

Opposite setup (the flat limit, s3b): at z = 1001/1000 the angle is 44.99998 degrees and R1, R2, R3 are all 1.41421. Table of the R1/R2/R3 ratios and angle against z (in s3b_out.txt): at z = 2: 38.66 degrees, 1.4056 / 1.4663 / 1.2806; at 11: 10.22 degrees, 1.1616 / 1.7177 / 1.0161; at 100: 1.15 degrees, 1.0198 / 1.8495 / 1.0002. 45 degrees needs c = 1, i.e. z = 1. So the sc/fcc second shell is recovered only as z tends to 1 (small steps, flat space); at the ratios 5 and 7 the curvature turns it away. Reversed word order gives the mirror set. The one numerical near-coincidence, R1 ratio 1.1901 at 7-LPS-8 against the bcc 1.1547, fails the direction test and is not a match.

## 4. Two balls (s4_join.py, s4b_proper.py)

Definitions fixed before the run: ball 2 is a copy, turned by any of the 48 octahedral elements. Facing: some arm a of ball 1 and arm -a of ball 2. Translation-compatible: point inversion through the midpoint swaps the two centres, i.e. -A_P = R(A_Q). FORCED = facing and compatible with one orbit of facing arms; IMPOSSIBLE = compatible fails for every rotation.

| Pair | facing arms | orbits | rotations of ball 2 giving compatibility | verdict |
| :-- | :-- | :-- | :-- | :-- |
| (5,5) | 6 of 6 | 1 | 48 of 48 | forced |
| (7,7) with the 8 diagonals | 8 of 8 | 1 | 48 of 48 | forced |
| (5,7) | 0 of 6 | none | 0 of 48; sizes 6 and 8 so no rotation at all | impossible as a pair of translates |
| (11,11), parity form inverse-closed (24 directions) | 24 of 24 | 1 | 48 of 48 | forced |
| (11,11), parity form raw (12 half set), same copy | 0 | none | 8 of 48 map A to -A (4 proper rotations) | same copy cannot face |
| (11,11), raw set against its conjugate copy | 12 | 2 (8 and 4) | 8 of 48 | possible (alternating two-sublattice) |
| (11,11), face-diagonal reading (real part 3 shell) | 12 of 12 | 1 | 48 of 48 | forced |

Notes. A5 union A7 = A13 exactly (6 + 8 = 14), so the two sublattices of a body-centred (CsCl-like) arrangement together have the 13 set as their arm set; this is why (5,7) fails as a pair of translates but not as an interpenetrating pair. The radii do not fit a body-centred lattice: bcc needs the diagonal arm to be the shorter, the ratio of diagonal to axis being sqrt3/2 = 0.8660; here the axis arm (5) is the shorter, with G5/G7 = 8/9 = 0.8889, d ratio ln 5/ln 7 = 0.8271, Klein chord ratio 0.9615. No reading gives the lattice ratio, and nothing was fitted.

Gap at depth n (ball cut at depth n, G_n = tanh(n ln p / 2) = (p^n - 1)/(p^n + 1), gap to the rim 1 - G_n = 2/(p^n + 1), exact):

| p | n = 1 | n = 2 | n = 3 |
| :-- | :-- | :-- | :-- |
| 5 | G 2/3, gap 1/3 | G 12/13, gap 1/13 | G 62/63, gap 1/63 |
| 7 | G 3/4, gap 1/4 | G 24/25, gap 1/25 | G 171/172, gap 1/172 |
| 11 | G 5/6, gap 1/6 | G 60/61, gap 1/61 | G 665/666, gap 1/666 |

The gap is positive at every depth, so a layer of gap is always left, shrinking by a factor near p per level. Between two balls the layer along the join is the sum of the two gaps, e.g. (5,5) at depths (1,1): 2/3; (7,7): 1/2; (5,7): 7/12; (11,11): 1/3; at depth (3,3): 2/63, 1/86, 235/10836 for (5,7) mixed (n=3,m=3), 1/333 for (11,11). The full 3-by-3 tables for each pair are in s4_out.txt. Exact search for 1 - G_n(p) = G_m(q) with p, q in {5, 7, 11} and n, m up to 8 found none, so no level where the cut surface of one ball meets the cut surface of the other. The same-depth products G_n(5) G_n(7) are 1/2, 288/325, 589/602: the wall value 1/2 occurs at depth 1 only.

## 5. B99 side check (s5_b99.py)

One line: with a = n and b = n - 1, a^2 + b^2 is the hypotenuse, a^2 - b^2 = (a - b)(a + b) = 2n - 1 and 2ab = 2n(n - 1), and (a^2 - b^2)^2 + (2ab)^2 = (a^2 + b^2)^2. So (2n - 1, 2n(n - 1), n^2 + (n - 1)^2) is a Pythagorean triple, and 1 - G_shell^2 = (2n(n - 1)/(n^2 + (n - 1)^2))^2 is a rational square. Sympy confirms the difference is identically zero; the shell step ratio is z = (n/(n - 1))^2 exactly.

| n | G_shell | sqrt(1 - G^2) | z | partner g = 1/(2G) | partner z |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 2 | 3/5 | 4/5 | 4 | 5/6 | 11 (prime) |
| 3 | 5/13 | 12/13 | 9/4 | 13/10 | -23/3 |
| 4 | 7/25 | 24/25 | 16/9 | 25/14 | -39/11 |
| 5 | 9/41 | 40/41 | 25/16 | 41/18 | -59/23 |
| 6 | 11/61 | 60/61 | 36/25 | 61/22 | -83/39 |
| 7 | 13/85 | 84/85 | 49/36 | 85/26 | -111/59 |

Only the first partner lies inside the disk (G < 1): it is z = 11, an integer and a prime. The others have G > 1 (outside the rim), which as a ratio is negative and not an integer. So the first shell term 3/5 (z = 4) pairs with 11 across the wall, and with 5 and 7 these are the only integer pairs across the wall: (z - 3)(z' - 3) = 8 gives (4,11) and (5,7). Of these only (5,7) has both ratios prime.

Paper check (VOTKP_ELEMENTAL_PEELING_PAPER_v3_3_20261112.html, tags stripped): the word "Pythag" occurs once, in section 8.7, "The step splits into a shell wall and a screening step": "These are the odd leg over the hypotenuse of the Pythagorean triples (2n-1, 2n(n-1), n^2+(n-1)^2). The form is Euclid's: tanh ln(p/q) = (p^2-q^2)/(p^2+q^2) ... So the triples carry no physics beyond the hydrogen-like ratio (n/(n-1))^2." Section 8.4 is "The ridge census" and does not contain it. The paper does not state that 1 - G^2 is a rational square, and does not list the partners across the wall of the shell terms. Both are new here.

## 6. Untested or open

- The rule that a quaternion of norm p acts as a boost of ratio p along its imaginary axis, for any p other than 5, is my extension. For real part 0 the quaternions q and -q give boosts B_v and B_-v, so the placement does not descend to quaternions modulo sign at p = 3, 11, 19.
- Arms at a node other than the centre are the centre set carried by that node's isometry (exact in the hyperbolic metric); I did not check how the Euclidean ball picture distorts the angles.
- The two-ball tests compare direction sets and radii; no full lattice was built. The bipartite alternating-word rule (needed for diamond and for the raw 11 set) is not in his papers.
- The ln 7 six-axis tree of his papers and the eight-diagonal LPS tree are different objects; I kept both for the depth test.

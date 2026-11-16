# Reading notes: VOTKP vacuum disk paper (v6)

Source: Google Drive file 13jWlLT10-eVyfRqwd0SK9NvrUfIqK9Eh, "votkp_vacuum_disk_v6.pdf".
How read: the Drive text reader returned mangled maths and stopped mid-sentence on p.23 ("Open (2) 1. ... The knot side is a theorem: the ke"). I then downloaded the PDF itself (23 pages, 329,672 bytes, created Tue Nov 10 02:31:21 2026 CST, LaTeX via pandoc) and read all 23 pages from pdftotext -layout. Three regions were also checked as page images (p.4 Figure 1 + Theorem 2; p.8 crossing potential; p.14 action).
Coverage: 23 of 23 pages of text. Figures 2, 3, 4 were read by CAPTION ONLY (not viewed as images); Figure 1 was viewed.
"REBUILT" below marks an equation whose text extraction was broken and which I reassembled from the surrounding text and/or the page image.
The paper has no numbered equations (no (1), (2)...). It has Proposition 1, Theorem 2, and unnumbered displays. Appendices are lettered D and E only; there is no Appendix A, B or C in this PDF.

---

## 1. What the paper is

- Title (as printed): "The Volume of the Knot Potential: Decay and Direction on the Vacuum Disk"
- Author: Jeromie Beasley
- Date/version line (as printed): "10 November 2026 (v6)"
- AI line (as printed, above the abstract): "AI-assisted: computations, drafting and literature checks were carried out with Claude (Anthropic) and helper agents, from the author's ideas and earlier papers; all numbers come from scripts listed in Appendices D and E and the attached archive."
- What it says it is: VOTKP "began as the volume of the knot potential, an attempt to read the volume of the space around a knot from its polynomials. It then became the vector of traits kept under peeling. This paper joins the two meanings through the two books of the intrinsic quantum geometric tensor Q = g - (i/2) Omega: a climb (metric, size) and a turn (curvature, phase). The reading is set on a Smith-type disk whose centre is the vacuum and whose rim is ground."
- Sections: Abstract; 1 Where this comes from; 2 The vacuum disk for knot pieces; 3 Decay: the vacuum bowl; 4 Every geometry, and the one nearest the vacuum; 5 Direction: the twist lives in integers; 6 Our polynomial, read off the drawing; 7 Light strings: Jones and HOMFLY; 8 Lessons from surfaceology; 9 Colour: the elements on the same disk; 10 The electron; 11 Knots that build themselves; 12 Ledger: what is ours; 13 Open problems; References; Appendix D Full script list; Appendix E The braided-spinor salvage - verification.
- Three papers it says feed it: IQGT (Intrinsic Quantum Geometric Tensor, v7.3.1); Dirac Time (Dirac Time of the Gigantefermion, v3.1); VOTKP (Elemental Peeling, v2.9). The reference list also has "J. Beasley, Two Trees in One Ball, v4, Zenodo" (listed, not discussed in the body).

---

## 2. Objects and definitions (his names, his definitions)

From Section 1 (imported from IQGT v7.3.1):
- Two books: "For a projector path, the tensor Q = g - (i/2) Omega splits into two books."
  - The metric g = (1/2) Tr(V W) "measures how far a state moves: the climb."
  - The curvature Omega = +i Tr(Pi [V, W]) = -2 Im Q "measures how it turns: the turn."
  - "A loop that comes back still remembers, through its phase (IQGT Ex. 6.5)."
  - Note: text extraction prints "Q = g - 2i Omega"; the page image shows Q = g - (i/2) Omega. Use the image.
- Smith coordinate: Gamma = (z-1)/(z+1) = tanh((1/2) ln z) "puts any impedance-like quantity on a disk: the centre Gamma = 0 is the matched point (vacuum) and the rim |Gamma| = 1 is total reflection (ground)."
- From Dirac Time v3.1: "Torus knots, their arcs and signatures, and the chiral pairing Gamma P+ Gamma = P-. The torus knots return here as the pure-direction roots."
- From VOTKP (Elemental Peeling v2.9): "Peeling kept a vector of traits, Levine-Tristram walls and colour; v2.9 Table 6 has 575 double roots. Its first meaning, the volume of the knot potential, mixing HOMFLY and coloured Jones to map volume, is the question this paper answers."
- The tennis racket: "A body spun about its middle axis flips over and over (the Dzhanibekov effect). The angular momentum keeps its size and its direction in space. What builds up is a turn, a geometric phase set by the area the switching sweeps (Montgomery)." Organising rule: "the axis switches, the direction stays". Earlier-research facts quoted: the climb rate of that switch "matched the Connection Energy formula (0.577350)", and "the memory was a lune 4 arctan k that reaches 45 deg when the middle level sits midway."

From Section 2:
- Shape z: each ideal tetrahedron of a hyperbolic knot complement "has a shape z with Im z > 0, a cross-ratio of its four ideal vertices."
- Volume of a piece: the Bloch-Wigner dilogarithm D(z) = Im Li2(z) + arg(1-z) log|z|.
- w = e^{i pi/3}, "the shape of the regular ideal tetrahedron", V0 = D(w) = 1.0149416064..., "the largest possible".
- THE VACUUM DISK: G(z) = (z - w)/(z - w-bar).
- Vacuum point: G = 0 (the regular tetrahedron).
- Rim: |G| = 1 (real z, flat tetrahedron, D = 0). The abstract calls the rim "ground".
- Mirror: shape z-bar; lies outside the disk, |G(z-bar)| = 1/|G(z)|.
- Axis switch: T(z) = 1/(1-z), relabels the tetrahedron's edges (z -> z' -> z''); z' = 1/(1-z).
- The dashed circle in Figure 1: |G|^2 = 1/2.

From Section 3:
- omega = e^{2 pi i/3} (the three-fold turn).
- Bowl / vacuum bowl / bowl law: the series of D around G = 0.
- Decay book: "A knot's volume is its pieces at full volume, minus how far each one sits from the vacuum. This is the decay book."
- R: the remainder after the quartic term.

From Section 4:
- A geometry: a solution of the knot's gluing equations (edges plus meridian completeness): the true hyperbolic structure, its mirror, flat solutions, Galois-conjugate ones. "Each is a different way of putting a geometry on the knot."
- Ladder: the within-knot ordering of solutions, Sum|G_j|^2 against volume.
- Mirrored count for outside pieces: G-tilde = 1/G-bar, epsilon = -1 outside.

From Section 5:
- Direction: the Chern-Simons half of the complex volume Vol + i CS.
- Windings: the integers p, q in the log-parameters of each tetrahedron (a flattening; Zickert Def. 6.1).
- Branching order: "a vertex order with order-preserving gluings".
- Two books in the knot: "Decay (volume) is continuous: distance from the vacuum. Direction (twist) is integer: how many half-turns each piece's phase winds."

From Section 6:
- The potential (Cho-Kim-Kim 2013) of a knot diagram; one variable z_k per side.
- Modified potential V0 = V - Sum_k (z_k d_k V) log z_k (NOTE: the symbol V0 is reused here; it is not the tetrahedron volume V0 = 1.0149... of Section 2).
- "This is, literally, the volume of the knot potential."
- Decay-direction polynomial P_K(x) = Prod_rho (x - e^{lambda V0(rho)}), "one root per geometry, with lambda chosen to map the pi^2 period to a full turn."
- Root reading: imaginary part of V0 = decay (volume of that geometry); real part = direction (-CS mod pi^2).
- Pure-direction roots: torus-knot roots, decay 0, direction a rational multiple of pi^2.
- Arc: T(p,q) "carries (p-1)(q-1)/2 arcs of rotation-valued holonomy, indexed by a pair (k,l). Each arc ends where the two generators begin to commute, at a meridian angle alpha_end (in units of a full turn)."

From Section 7:
- Jones string: t = e^{i theta} runs once round the circle, "as colour runs from violet to red", following the Jones polynomial V(t); since V(1) = 1 the string leaves one point and returns to it.
- Climb (of a string) = the Mahler measure (mean of log|V|).
- Turn (of a string) = the signed area swept, divided by the mean of |V|^2.
- sl(N) lines ("light lines") of HOMFLY: v = t^{-N/2}, z = t^{1/2} - t^{-1/2}; N = 0 is Alexander, N = 2 is Jones.
- Circuit polynomial Q(z): shade the diagram; shaded regions are nodes, crossings are branches; a right-handed crossing has admittance z, a left-handed one 1; Q(z) counts spanning trees by right-handed branches.

From Section 9:
- Reflection track: Gamma = (1 - N)/(1 + N) of each element across the visible band, traced on the Smith disk (41 elements, refractiveindex.info). (N is not defined in the text beyond this formula; the data source is a refractive-index database.)
- Schottky line: |Gamma|^2 = 1/2 averaged over the visible.
- "2/3 vacuum-mix line" / "the space between": the line molecular solids cross under squeeze (no formula given in this paper).
- Film winding: "an integer index of the substrate".

From Section 10:
- Chain: light -> electron -> knot, through one group (SL(2,C) / PSL(2,C)).
- Spin lift: lifting a knot's geometry from PSL to SL(2,C), "a choice of spin structure: the electron's 720 deg return, the -1 of Dirac Time 5.2."
- "chiral vortex knot of memory": the object the action carries. Chiral = the Weyl left/right split (mass term the only entry passing between them). Vortex = the winding phase and the 720 deg return, the double cover SU(2) -> SO(3). Knot = a knotted field configuration of the Faddeev-Niemi type. Memory = "the geometric phase the field keeps around a loop (Berry), and on this disk that kept phase is the direction book, the Chern-Simons turn."
- Braided-spinor electron: "a chiral spinor with winding and a kept phase", reached through knots, rest mass and braiding.
- Kept phase: the flat bundle's Cheeger-Chern-Simons class.
- The hinge: "a clock and a kept record are one winding." "Time in one reading is the kept record in the other."
- P_L = (I - gamma^5)/2, P_R = (I + gamma^5)/2; alpha_i = gamma^0 gamma^i (Dirac velocity operator); B_i = (1 + g_{i+1} g_i)/sqrt2 (braid generators from Majorana operators g_a).

From Section 11:
- Privileged knots (Micheletti 2018 survey): 3_1, 4_1, 5_1, 8_19, plus 10_124 and 15n_41185.
- "make no space": torus knots (zero decay).

---

## 3. Equations in order (none are numbered in the paper)

Abstract / Section 1
- E1. Q = g - (i/2) Omega. [REBUILT from page image; text extraction shows "2i".]
- E2. g = (1/2) Tr(V W).
- E3. Omega = +i Tr(Pi [V, W]) = -2 Im Q.
- E4. Gamma = (z-1)/(z+1) = tanh((1/2) ln z). Centre Gamma = 0 matched point (vacuum); rim |Gamma| = 1 total reflection (ground).
- E5. Chiral pairing (Dirac Time): Gamma P+ Gamma = P-.
- E6. Racket memory (earlier research): a lune 4 arctan k, reaching 45 deg when the middle level sits midway.

Section 2
- E7. D(z) = Im Li2(z) + arg(1-z) log|z|.
- E8. w = e^{i pi/3}; V0 = D(w) = 1.0149416064...
- E9. G(z) = (z - w)/(z - w-bar).
- E10. Proposition 1: (a) G(w) = 0. (b) real z => |G| = 1. (c) |G(z-bar)| = 1/|G(z)|; proof line: G(z-bar) = (z-bar - w)/(z-bar - w-bar) = conj[(z - w-bar)/(z - w)] = conj(G(z))^{-1}. [REBUILT: the extraction prints "G(z-bar) = ... = G(z)^-1" with the bars scattered; the modulus statement in (c) is clear.] (d) T(z) = 1/(1-z); G(Tz) = e^{2 pi i/3} G(z), while D(Tz) = D(z).
- E11. Proof steps of (d): T is Mobius of order 3 with fixed points the roots of z^2 - z + 1 = 0, namely w and w-bar; in the coordinate G (w -> 0, w-bar -> infinity) it is multiplication by its multiplier at w; T'(w) = 1/(1-w)^2 = 1/e^{-2 i pi/3} = e^{2 pi i/3}; D(z) = D(1/(1-z)) = D(1 - 1/z).

Section 3
- E12. Theorem 2 (bowl series): D(z) = V0 - (3 sqrt3/4)|G|^2 + (sqrt3/8)(G^3 + G-bar^3) + (3 sqrt3/16)|G|^4 + O(|G|^5). [Confirmed against page image.]
- E13. Since 1 - w = w-bar: z = w(1 - omega-bar G)/(1 - G), 1 - z = w-bar(1 - omega G)/(1 - G). [Confirmed against page image.] So log z and log(1-z) are series in G with coefficients (1 - omega-bar^n)/n and (1 - omega^n)/n.
- E14. D = Sum c_ab G^a G-bar^b; for a, b >= 1: c_ab = Im[(1 - omega^a)(1 - omega^b)] / (2ab), which is -3 sqrt3/(4ab) when a = b = 1 (mod 3), +3 sqrt3/(4ab) when a = b = 2 (mod 3), 0 otherwise. [The +/- 3 sqrt3/(4ab) values REBUILT from broken extraction; consistent with c11 and c22 below.]
- E15. Pure terms: c_n0 = conj(c_0n) = (1/(4 i n)) Sum_{j=1}^{n-1} (2j - n)(1 - omega^j)(1 - omega-bar^{n-j}) / (j(n-j)). [REBUILT from layout.]
- E16. c11 = -3 sqrt3/4, c22 = 3 sqrt3/16, c30 = c03 = sqrt3/8 ("the bowl law").
- E17. |1 - omega|^2 = 3, so 3 sqrt3/4 = |1 - omega|^3/4.
- E18. "Only terms with a = b (mod 3) appear, and the reflection z -> 1 - z-bar, which sends G -> G-bar and keeps D, makes every coefficient real."
- E19. R = D - [V0 - (3 sqrt3/4)|G|^2 + (sqrt3/4) Re G^3 + (3 sqrt3/16)|G|^4]; |R| <= 0.70 |G|^5 on |G| <= 0.9999.
- E20. Knot law: Vol(K) = Sum_j D(z_j) ~ Sum_j [V0 - (3 sqrt3/4)|G_j|^2 + ...].

Section 4
- E21. Mirrored count: epsilon_j [V0 - k|G-tilde_j|^2] with G-tilde = 1/G-bar and epsilon = -1 outside. (k is not given a value at this spot; the quadratic bowl coefficient is 3 sqrt3/4.)
- E22. All-real solutions: Sum|G_j|^2 = n exactly.

Section 5
- E23. Log-parameters: w0 = log z + p pi i, w1 = log z' + q pi i, w2 = -w0 - w1, z' = 1/(1-z), integers p, q chosen so every edge and both cusp curves have total log-parameter 0.
- E24. i(Vol + i CS) = Sum_j epsilon_j R(z_j; p_j, q_j).
- E25. R(z; p, q) = Li2(z) + (1/2) log z log(1-z) + (pi i/2)(q log z + p log(1-z)) - pi^2/6. [REBUILT from two-line extraction.] (This R is Neumann's function, not the remainder R of Section 3.)
- E26. Relabelling defect: R(z'; q, r) - R(z; p, q) = (1 + 3q) pi^2/6.

Section 6
- E27. Crossing term for sides (a,b,c,d): Li2(z_b/z_a) - Li2(z_b/z_c) + Li2(z_d/z_c) - Li2(z_d/z_a). [Confirmed against page image.]
- E28. Hyperbolicity equations: exp(z_k dV/dz_k) = 1, products of (1 - ratio)^{+/-1}.
- E29. Modified potential: V0 = V - Sum_k (z_k d_k V) log z_k, which gives i(Vol + i CS) at the geometric solution (CKK Thm 1.2).
- E30. P_K(x) = Prod_rho (x - e^{lambda V0(rho)}).
- E31. Torus-knot directions all fit -k^2/(pq) mod 1.
- E32. direction = -4 p q alpha_end^2 (mod 1). Trefoil: alpha_end = 1/12, "which is the vacuum point itself, s^2 = w, where Delta_{3_1}(w) = 0; the direction is -24/144 = 5/6."

Section 7
- E33. sl(N) lines: v = t^{-N/2}, z = t^{1/2} - t^{-1/2}.
- E34. Q(1) = det K (circuit polynomial).

Section 8
- E35. u_C + Prod u_D = 1 (Figueiredo's u-variables; checked to 4e-16).
- E36. Shifted 4-point amplitude leading term: -(X13 + X24).

Section 9
- E37. Gamma = (1 - N)/(1 + N).
- E38. Film winding jumps across the circle |r12| = |r01|.

Section 10
- E39. S = Integral d^4x [ psi-bar (i gamma^mu d_mu - m) psi + g psi-bar psi psi_R ]. [Read from page image; the Yukawa term is printed exactly as "g psi-bar psi psi_R".]
- E40. gamma^0 P_L = P_R gamma^0, so m psi-bar psi = m(psi-bar_L psi_R + psi-bar_R psi_L).
- E41. {gamma^mu, gamma^nu} = 2 eta^{mu nu} I; (gamma.p)^2 = (p.p) I.
- E42. [alpha_i, gamma^5] = 0 and {beta, gamma^5} = 0; ||[alpha_i, H]|| = 2.74.
- E43. Braid relation B_i B_{i+1} B_i = B_{i+1} B_i B_{i+1}; B_i^2 = g_{i+1} g_i, |B_i^2 - I| = 1.414.
- E44. SU(2) trefoil word: U V U = V U V.
- E45. omega_Zit = 2 m c^2 / hbar.
- E46. The hinge display: "720 deg return [a tick, time] = the phase the knot keeps [the record, memory]". [REBUILT from underbrace extraction.]
- E47. {Gamma, D} = 0 from Gamma P+ Gamma = P- (here D is a Dirac operator, not the Bloch-Wigner D), spectrum in +/- pairs, eta = 0.

Appendix E
- E48. B_i = (1 + g_{i+1} g_i)/sqrt2; {g_a, g_b} = 2 delta_ab; B1 g1 B1^dagger = g2, B1 g2 B1^dagger = -g1; B1^2 = g2 g1.
- E49. 3 x 3 = 5 + 3 + 1 (J^2 spectrum 6 x5, 2 x3, 0 x1).
- E50. Framed knot invariant: (-A^3)^{-w} cancels the first Reidemeister curl.
- E51. Cl(4,1) inversion: conformal sandwich maps x -> x/|x|^2.

---

## 4. Results with the grade the paper gives

Section 2
- Proposition 1 (vacuum, rim, mirror, racket). Status as printed: "(a)-(c) are elementary; (d) is a new reading of a classical symmetry; the racket interpretation is ours." Numerical check: z = 0.3 + 1.1i, three labels at radius 0.1557583601, angles 34.715, 154.715, -85.285 deg, identical D = 0.9832288623.

Section 3
- Theorem 2 (bowl series). "Status: derived, and confirmed numerically: (V0 - D)/|G|^2 -> 1.2990 against 3 sqrt3/4 = 1.29904."
- Closed form of every coefficient: "Checked exactly through degree 4 and in ball arithmetic on all 860 pairs through degree 40, largest difference 3e-34 (c2_closed_form.py)."
- Remainder bound: "Status: the coefficients are derived; the bound is proved." Proved in Arb ball arithmetic (c2_arb_enclosure.py).
- Knot law, nothing fitted (table, reproduced in full):
  - pieces all at full volume n V0: 243 knots, median error 10.9%
  - bowl, quadratic only: 243 knots, median 0.27%, 90th pct 0.96%, worst 13% (10_1)
  - bowl, quadratic only: 12,954 knots, median 0.21%, 90th pct 0.62%, worst 19.9% (12a_803)
  - bowl + cubic: 12,954 knots, median 0.39%, 90th pct 0.90%, worst 27%
  - bowl + cubic + quartic: 12,954 knots, median 0.076%, 90th pct 0.31%, worst 11.4% (11a_247)
  - opposite: hyperbolic distance: 12,954 knots, median 1.3%, 90th pct 3.2%, worst >200%
- "The cubic needs the quartic. The racket term alone over-corrects; it only helps once the quartic term is included. With both, 12a_803 improves from -19.9% to -4.5%."
- "Most pieces sit near the vacuum... 1,391 of 2,777 tetrahedra lie within hyperbolic distance 0.5. That is why the bowl works."
- Term meanings: quadratic = round bowl ("volume drops with squared distance from the vacuum"); cubic = "the racket written exactly. It has the three-fold symmetry of Proposition 1(d) and nothing else"; quartic = next radial correction.

Section 4 (31 hyperbolic knots up to 8 crossings, 291 solutions; damped Newton from 3,000 random starts)
- true geometry = smallest Sum|G_j|^2 (nearest the vacuum): 31 of 31
- true geometry = largest volume: 31 of 31 (known: Francaviglia; Cho)
- mirrors outside the disk: always
- all-real solutions: Sum|G_j|^2 = n exactly (on the rim, Prop. 1b)
- within-knot order Sum|G|^2 against volume: median Spearman -0.905
- ladder breaks between two fully-inside solutions: none of 136 inversions
- Every break involves a flat solution or a mixed one (pieces on both sides of the rim); counting outside pieces as mirrored restores the order: median Spearman 0.995.
- Example 6_1: Sum|G|^2 = 0.74, 5.1, 28.9, 47.3 against volumes 3.164, 1.415, -1.415, -3.164.
- Grade: "It is known that the geometric solution maximises volume; that it is the one nearest the vacuum, with the bowl law as the reason, is our reading." Ledger: "NEW READING with new tests (31/31; rho = 0.995)".

Section 5
- Null result first: CS "was not found in the angles of the pieces: the summed three-fold angle of G against CS gives rho = 0.02."
- Integer system solved exactly (PARI matsolvemod) for 79 hyperbolic knots of 4-9 crossings.
- Volume needs no integers: matches SnapPy to 5e-14.
- CS with windings first matched only up to +/- pi^2/6 on 54 knots; cause E26; fix = branching order (found on all 79), odd permutations invert the shape and negate the integers (epsilon = -1).
- With that, CS exact in 454 of 454 runs (79 knots x up to 6 branchings), to 2.7e-14, modulo SnapPy's period pi^2/2.
- Windings essential: dropped, the continuous part alone matches 1 of 79.
- Status: "reproduction of Neumann's theorem; the branching fix is standard. The two-book reading is ours."

Section 6
- Placement rule: all 64 placements tested against SnapPy; "One rule survives, up to the term's symmetry (a<->c, b<->d): (b,d) is the under-strand pair of the PD crossing X[i,j,k,l], the same for both signs." A kinked crossing X[i,j,j,l] is singular and must be removed.
- Solutions come in continuous families; only V0 is constant on each family; one complex number per family = per boundary-parabolic geometry.
- top root = SnapPy complex volume (vol to 1e-6, CS to 1e-5): 79 of 79 hyperbolic knots, 4-9 crossings
- same full spectrum from three different drawings (one with 2 extra crossings): 13 of 13 knots
- spectrum volumes = the ladder of Section 4: exact
- "The search is a budget question, not a convergence question: on hard knots about one random start in a thousand reaches the geometric family."
- Every geometry as (decay, direction), with SnapPy value:
  - 4_1: (2.02988, 0); mirror. SnapPy (2.02988, 0)
  - 5_2: (2.82812, -3.0241), (0, 1.1135); mirror. SnapPy (2.82812, -3.0241)
  - 6_1: (3.16396, 3.0789), (1.4151, 0.211); mirrors. SnapPy (3.16396, 3.0789)
  - 6_2: (4.40083, -3.997), (1.53058, 0.3291), (0, 2.4011); mirrors. SnapPy (4.40083, -3.997)
  - 6_3: (5.69302, 0), (0.9243, +/-1.8906); mirrors. SnapPy (5.69302, 0)
- Caveat: SnapPy's named manifold is the mirror of the KnotInfo drawing for 42 of the 79 knots; signed comparisons must use the exterior of the drawing itself.
- Torus knots, pure direction: on 3_1, 5_1, 7_1, 8_19, 10_124 every valid root has decay 0 (to 1e-15), every direction an exact rational multiple of pi^2. Directions (fraction of pi^2, mod 1): 3_1 = T(2,3): 5/6. 5_1 = T(2,5): 1/10, 9/10. 7_1 = T(2,7): 3/14, 5/14, 13/14. 8_19 = T(3,4): 2/3, 11/12. 10_124 = T(3,5): 11/15, 14/15. Status: reproduction (Kirk-Klassen; Dubois-Kashaev; Murakami).
- Arc table (knot, arc (k,l), alpha_end, direction, found by the disk):
  - T(2,3) (1,1) 1/12 -> 5/6 yes
  - T(2,5) (1,1) 1/20 -> 9/10 yes; (1,3) 3/20 -> 1/10 yes
  - T(2,7) (1,1) 1/28 -> 13/14 yes; (1,3) 3/28 -> 5/14 yes; (1,5) 5/28 -> 3/14 yes
  - T(3,4) (1,1) 1/24 -> 11/12 yes; (1,3) 5/24 -> 11/12 yes (same value); (2,2) 1/12 -> 2/3 yes
  - T(3,5) (1,1) 1/30 -> 14/15 yes; (2,4) 2/15 -> 14/15 yes (same value); (1,3) 7/30 -> 11/15 yes; (2,2) 1/15 -> 11/15 yes (same value)
- Prediction then found: "The arc formula gave 2/3 for 8_19 and 11/15 for 10_124 before either had been seen on the disk. A search over more drawings then found both: 2/3 on the braid drawing (sigma1 sigma2)^4 (50 of 3,650 starts), 11/15 on (sigma1 sigma2)^5 and two other drawings (21 of 13,000 starts in all). Each has decay 0 and residual, both below 2e-14."
- "No other valid root appeared on either knot in 30,800 starts: nothing irrational, nothing with decay, no mirror value (1/3, 4/15)."
- Status: "the formula is a new reading of the Kirk-Klassen values through the arc end points; the match is exact on all five knots as sets of values."

Section 7 (2,970 hyperbolic knots up to 12 crossings; 9,985 at 13 crossings in an independent run)
- climb vs volume: rho = 0.854 (independent run 0.8542)
- climb, after log det, vs volume left over: rho = 0.50; R^2 0.708 (log det alone) -> 0.810
- turn (swept area) vs |signature|: rho = 0.83
- turn counted as roots inside the circle vs volume or signature: nothing
- any of these, and the angles of Alexander or Jones zeros, vs Chern-Simons: no correlation found (bears on an open question of Friedl-Jackson)
- Prior art: Mahler measure of Jones vs volume known (Champanerkar-Kofman), determinant known (Dunfield; Champanerkar-Kofman-Purcell). "Combining them, and the turn-signature split, were not found in those sources."
- HOMFLY: on the plain two-phase torus |v| = |z| = 1 it "carries nothing (rho = 0.036)". On the sl(N) lines, Jones slice reproduces the Jones climb to 3e-13. On 12,955 knots the climb carries volume at rho = 0.60 (N=0), 0.86 (N=2), 0.78-0.86 for N = 3..8. All lines with log det reach R^2 = 0.838, against 0.795 for log det + Jones. The surface the lines sweep gives rho = 0.864. "VOTKP's first meaning, a HOMFLY and coloured-Jones mix mapping volume, is borne out on these lines. Prior art to check: sl(N) volume conjectures."
- Circuit polynomial "(first attempt)": Q(1) = det K on 1,846 of 1,846 alternating knots; Q unchanged on 180 of 180 reduced alternating redrawings; proof SKETCH (flype = Whitney twist on the Tait graph, keeps every spanning tree and every crossing's handedness; by Tait's flyping theorem Q is an invariant of alternating knots). "It is coarse: knots with all crossings of one hand give a constant." Lesson: "on the diagram alone, the only fully invariant circuit weights lead back to the Kauffman bracket, that is, to Jones."

Section 8 (reproductions of Figueiredo / Arkani-Hamed / Cao / Dong / He)
- 6-point amplitude vanishes exactly on its hidden-zero locus; shifted 4-point leading term -(X13 + X24); shifted 6-point equals the NLSM amplitude (ratio 1 at three random points).
- u-variables are cross-ratios; u_C + Prod u_D = 1 (to 4e-16); unchanged by Mobius maps. "They are the same kind of number as the tetrahedron shapes, and Mobius maps are the Smith chart's own moves."
- Lessons taken: "find the zeros first"; "a denominator-only object, like the circuit polynomial, needs a shift to gain numerators."

Section 9
- Schottky line |Gamma|^2 = 1/2 (visible average) separates metals (35 of 35 above) from non-metals (0 of 6 above).
- Hidden phase: "Bulk colour hides the phase of Gamma, and a thin film writes it back." Over 39 metal pairs the eye cannot tell apart in bulk, the phase gap predicts the colour gap under a film at rho = 0.64. Pairs riding the rim under-read (rho = -0.52, p = 0.0007): "near ground the phase is present but pinned."
- One handedness: every element's track winds the same way (38 of 41, the other three about 0); "Status: recognised physics."
- The space between: molecular solids crossing the 2/3 vacuum-mix line under squeeze rank their measured metallization pressures at rho = 0.89 (Te, P, Se, I, Br, S). Network solids (Si, Ge, B) already sit on the line and "need a flip, a change of structure, not a squeeze."
- Film winding: an integer index of the substrate, exact to 1e-15, grows by one per 247 nm of film, jumps across |r12| = |r01|; selenium is the one element inside it. Lightness follows bulk reflection (continuous); chroma follows the integer order; hue follows the leftover phase. "The shape matches volume beside windings; the physics is Newton's colour orders."
- Knots as colours: Jones strings rendered as colours carry volume through lightness (rho = 0.96; R^2 0.707 -> 0.878), "but that colour is a compression of |V|."
- Not yet joined: "The knot pieces fill the inside of the disk; the metals sit near the rim (Figure 1). The bowl region is barely reached by the elements. Clear materials (oxides, salts, glasses) live inside the disk and are the next colour test."

Section 10
- One group: SL(2,C) double cover of Lorentz; PSL(2,C) = Mobius maps (the Smith chart's moves) = symmetries of hyperbolic 3-space where the knot's volume lives; every geometry of Section 4 is a representation of the knot group into it. "Status: standard mathematics; its use as the spine of the chain is ours."
- "The electron decides where matter sits on the disk. Free electrons push reflection to the rim (ground); bound electrons keep it near the vacuum. The metal/non-metal line and the 2/3 space-between line are the electron's choice to conduct." (no status line printed)
- Longitude sign (computed): in every SL(2,C) lift of the geometric representation the meridian has trace +/-2 and the longitude trace -2: 79 of 79 hyperbolic knots of 4-9 crossings (longitude_sign_01.py). "known theorem (Calegari), reproduced here."
- Two classes in H^2(M, dM; Z/2): class 0 (unipotent on whole boundary), class 1 (carries the -1). Solved exactly for 4_1 and 5_2: class 0 has no solution; every geometry of Section 4 sits in class 1. For 4_1 the coordinate of the geometric solution in class 1 is e^{i pi/3} = w: the vacuum point.
- Reading: "a spinor carried once around the longitude comes back with its sign reversed. Status: reproduction of a known theorem; the reading as the electron's sign on the disk is ours."
- Dirac + Yukawa checks: Clifford algebra to zero deviation; (gamma.p)^2 = (p.p)I to 1.9e-16; mass couples L to R, zero deviation. "Status: the four structures are standard and cited (Faddeev-Niemi; Berry); their combination into one object, and its identification with the electron chain above, are ours."
- One electron, three ways (knots; rest mass = Zitterbewegung, alpha_i spectrum {+1,+1,-1,-1}, ||[alpha_i,H]|| = 2.74; braiding = Ivanov 2001, rebuilt, |B_i^2 - I| = 1.414). "Status: each component is the field's and cited...; the convergence of all three reaches on one object is ours."
- Hinge: clock (Dirac time; braid relation U V U = V U V; tick rate omega_Zit = 2mc^2/hbar) and kept record (the Chern-Simons phase of the direction book) "are the same winding read two ways". No status line; presented as the "memory-first reading of the whole disk".
- What the lift closes: kept phase well defined for PSL(2,C) modulo pi^2 (Neumann; regulator in C/pi^2 Z). 4_1: CS = 0. 5_2: CS = -3.0241284, stable across six retriangulations to 4e-15, sign-reversing under the mirror (spin_lift_cs_02.py). Interval arithmetic (SnapPy inside Sage, enclosures to 55 digits) verifies the 5_2 value modulo pi^2/2 as 1.9106738..., differing from -3.0241284... by exactly pi^2/2.
- Conjecture (open): whether the spin lift refines the direction book beyond pi^2 for a knot. "The earlier form of this conjecture, that the lift removes a residual pi^2/2, is set aside in the archive (notes/SET_ASIDE_v6.md)."
- Kept phase vs fermion phase: "theorem on the knot side; conjecture on the field side." Not a single loop (peripheral holonomies parabolic, a pure shear with no rotation, so one peripheral loop carries no phase while CS != 0). Decay half exact: Vol = Sum D(z_j) to 4e-16 on 4_1 and to zero on 5_2 (spinor_berry_cs_01.py). Field side: 3D Dirac fermion gives Chern-Simons at level 1/2, determinant phase = APS eta-invariant (Redlich; Witten), theorems for compact gauge group on closed manifold; the knot's bundle is non-compact SL(2,C) on a cusped manifold; "a structural correspondence, stated here as a conjecture."
- Which Dirac operator: chiral pairing gives {Gamma, D} = 0, +/- paired spectrum (sf_symmetry_01.py, on a model operator), so eta = 0 and no spectral flow. "A paired operator keeps no phase... the pairing cancels the even record and only the odd datum survives." So the candidate is "the unpaired one, the two-component Dirac operator in three dimensions, which has no chirality. The kept phase is the odd, unpaired record."
- "If it holds, the two books meet: the climb is the fermion's amplitude and the turn is the phase it keeps."
- Provenance: braided-spinor material "salvaged from my older research conversations, with an earlier numerological framing removed"; "two inherited claims found to be circular" set aside in notes/SET_ASIDE_v6.md.

Section 11
- Prediction "made before the lookup: the knots that self-assemble are those that make no space, the torus knots."
- Checks: 10_124 = T(3,5), not hyperbolic, cyclic covers (2-6) match the braid-built torus knot: yes. 15n_41185 = T(4,5), not hyperbolic, covers match: yes. T(4,5) is the only non-alternating 15-crossing torus knot.
- Result: five of the six privileged knots are torus knots (zero decay, pure direction); the exception 4_1 has the smallest volume of any hyperbolic knot. "Status: the fingerprint match is strong but not a formal identification; the law is untested beyond these six."

Section 12 Ledger (item -> status, verbatim grades)
1. Volume = Sum D(z_j); CS from flattenings; torus-knot CS; max volume picks the geometry; potential of a diagram -> REPRODUCTION (Thurston, Milnor, Neumann, Zickert, Kirk-Klassen, Francaviglia, Cho, Cho-Kim-Kim)
2. Vacuum disk G; racket = exact 120 deg rotation; rim = flat; mirror outside -> NEW READING (elementary proofs, Prop. 1)
3. Bowl series and the no-fit knot law (median 0.076%, 12,954 knots) -> NEW RESULT in our frame (the series is a Taylor expansion; the law and its error budget are ours)
4. Nearest-the-vacuum rule; orientation-aware ladder -> NEW READING with new tests (31/31; rho = 0.995)
5. Placement rule for reading CKK off any PD drawing; 79/79; 13/13 diagram independence -> NEW RESULT (method)
6. Decay-direction polynomial P_K -> NEW DEFINITION; arithmetic of its coefficients open
7. Jones climb + log det; turn <-> signature; HOMFLY sl(N) lines carry extra volume -> NEW RESULTS (empirical)
8. Circuit polynomial Q, flype invariance -> NEW (prior-art check pending: clock states, Crowell)
9. Self-assembly <-> zero decay -> NEW OBSERVATION, untested as a law
10. Closed form of every bowl coefficient; 3 sqrt3/4 = |1 - omega|^3/4 -> NEW in our frame (derived; exact through degree 4, ball arithmetic through degree 40)
11. Remainder bound |R| <= 0.70|G|^5 on |G| <= 0.9999 -> PROVED (ball arithmetic)
12. Direction root from the Dirac-time arc: -4pq alpha_end^2 mod 1 -> NEW READING of Kirk-Klassen; exact on 5 torus knots; 2/3 (8_19) and 11/15 (10_124) predicted, then found
13. Spinor sign in the knot: longitude trace -2 in every lift (79 of 79); class 0 empty for 4_1, 5_2 -> REPRODUCTION (Calegari); reading ours
14. Kept phase = Cheeger-Chern-Simons class of the flat bundle -> REPRODUCTION (Neumann)
15. Kept phase = phase of a Dirac determinant on the knot; spin lift refines the twist beyond pi^2 -> CONJECTURE (open)
16. Braided-spinor electron: one object reached three ways (knot, rest mass, braiding) -> NEW SYNTHESIS (components cited; 11 checks to machine precision, Appendix E)

Appendix E tables
- "Verified to machine precision (11)" (the table prints these rows): gamma matrices as braiding operators (deviations 0, 0; |B^2 - I| = 1.414); Clifford algebra 0.00e+00; squares to Klein-Gordon 1.9e-16; chiral seam sewn by the mass term 0.00e+00; Zitterbewegung velocity {+1,+1,-1,-1}; trembling 2.74; two Weyl halves one seam 0 and 0; spin-2 from two spin-1, 3x3 = 5+3+1 (6 x5, 2 x3, 0 x1); framed knot invariant to 0; Cl(4,1) inversion 1.5e-14; torus-knot turns = -k^2/(pq) mod 1, all 10 exact.
- Braiding anchor: Clifford relations to 0.00e+00; generators unitary to 2.22e-16; braid relations to deviation 0 with far generators commuting, "a full B4 representation".
- "Reproduced against published results (1)": SU(3) Polyakov-loop endpoint, susceptibility peak, L = 12 Metropolis: tau = 0.1330 vs published 0.1331 (Delgado Mercado-Gattringer).
- "Open (2)": the fermion reading of the kept phase; whether the spin lift refines the twist beyond pi^2.
- "Added in v6": spinor sign on the longitude (-2 on 79 of 79); boundary-unipotent lifts (exact solution of the N = 2 Ptolemy equations, class 0: none for 4_1, 5_2); geometries carry the -1 (class 1: 2 solutions (4_1), 3 (5_2); 4_1 coordinate = w); bowl coefficients closed form (860 pairs, 3e-34); remainder bound (14,806 cells, 606,204 squares, none unresolved); direction root from the Dirac-time arc (10 of 10).
- What belongs to the field and is cited: Ivanov; Schrodinger-Penrose zig-zag; Dirac field with Yukawa coupling; Berry phase; Polyakov loop as confinement order parameter of the SU(3) spin model; conformal geometric algebra Cl(4,1); Kelvin's vortex-atom programme with Tait's knot tables. "they are not extended."
- What is ours: "Only the synthesis: one braided-spinor electron, reached three ways, carrying knot volume - decay and direction - on one lattice, and read as the bridge between the clock picture and the kept-record picture."

---

## 5. Numbers (value, unit, source in the paper)

Constants
- V0 = D(w) = 1.0149416064... (hyperbolic volume units; regular ideal tetrahedron) - Sec 2
- 3 sqrt3/4 = 1.29904; measured (V0 - D)/|G|^2 -> 1.2990 - Sec 3
- Bowl coefficients: -3 sqrt3/4, sqrt3/8 (on G^3 + G-bar^3), 3 sqrt3/16 - Sec 3
- Remainder: bound constant 0.70; true supremum of |R|/|G|^5 = 0.685567..., at G = -0.265893; domain |G| <= 0.9999 - Sec 3
- Arb proof: 14,806 cells on |G| <= 1/2; 606,204 squares on 1/2 <= |G| <= 0.9999; none unresolved - Sec 3
- Closed-form check: 860 pairs through degree 40, largest difference 3e-34 - Sec 3
- Connection Energy formula match: 0.577350 (climb rate of the racket switch; earlier research) - Sec 1
- Racket lune 4 arctan k reaching 45 deg - Sec 1
- VOTKP v2.9 Table 6: 575 double roots (Sec 1); 61 silent double walls in infinite-order knots (Sec 13)
- Prop 1 check: z = 0.3 + 1.1i; radius 0.1557583601; angles 34.715, 154.715, -85.285 deg; D = 0.9832288623 - Sec 2
- Figure 1: tetrahedra of knots with 4-8 crossings; dashed circle |G|^2 = 1/2

Knot-law counts and errors (Sec 3): see table in section 4 of these notes. 243 knots; 12,954 knots; 1,391 of 2,777 tetrahedra within hyperbolic distance 0.5; 12a_803 from -19.9% to -4.5%.
Count mismatch stated by the paper: 12,954 (this table), 12,955 (Section 7), 12,942 (separate confirmation run) - "have not been reconciled."

Section 4: 31 knots (up to 8 crossings), 291 solutions, 3,000 random starts, Spearman -0.905 and 0.995, 136 inversions, 6_1 values 0.74/5.1/28.9/47.3 vs 3.164/1.415/-1.415/-3.164.

Section 5: 79 knots (4-9 crossings); volume to 5e-14; +/- pi^2/6 on 54 knots; 454 of 454 runs to 2.7e-14 modulo pi^2/2; 1 of 79 without windings; rho = 0.02 for angles vs CS.

Section 6: 64 placements; 79 of 79; vol to 1e-6, CS to 1e-5; 13 of 13; about 1 start in 1000; mirror caveat 42 of 79; torus decay 0 to 1e-15; 50 of 3,650 starts; 21 of 13,000 starts; residual below 2e-14; 30,800 starts; excluded mirror values 1/3, 4/15; complex volumes for 4_1, 5_2, 6_1, 6_2, 6_3 (see section 4 above).

Section 7: 2,970 knots (to 12 crossings); 9,985 at 13 crossings; rho 0.854 / 0.8542; 0.50; R^2 0.708 -> 0.810; rho 0.83; HOMFLY plain torus rho 0.036; Jones slice to 3e-13; 12,955 knots; rho 0.60 (N=0), 0.86 (N=2), 0.78-0.86 (N=3..8); R^2 0.838 vs 0.795; surface rho 0.864; Q(1) = det K on 1,846 of 1,846; 180 of 180 redrawings.

Section 8: 4e-16; ratio 1 at three random points.

Section 9: 41 elements; 35 of 35 metals above, 0 of 6 non-metals above |Gamma|^2 = 1/2; 39 metal pairs, rho 0.64; rim pairs rho -0.52, p 0.0007; 38 of 41 one handedness; rho 0.89 for Te, P, Se, I, Br, S; film winding exact to 1e-15, +1 per 247 nm of film; knots as colours rho 0.96, R^2 0.707 -> 0.878.

Section 10 / Appendix E: 79 of 79 longitude trace -2; 5_2 CS = -3.0241284 (and 1.9106738... modulo pi^2/2); 4_1 CS = 0; six retriangulations to 4e-15; enclosures to 55 digits; Vol = Sum D to 4e-16 (4_1) and zero (5_2); 1.9e-16; 2.74; 1.414; 2.22e-16; 1.5e-14; tau = 0.1330 vs published 0.1331 (L = 12); class 1 solutions: 2 (4_1), 3 (5_2).

Section 11: six privileged knots, five torus; cyclic covers 2-6.

---

## 6. Limits, failures and open items stated by the paper

Stated failures / null results
- CS not found in the angles of the pieces (rho = 0.02).
- Bowl + cubic alone is WORSE than quadratic alone (median 0.39% vs 0.21%); "the racket term alone over-corrects".
- Worst cases remain large: 11.4% (11a_247) with the full law; 19.9% (12a_803) quadratic only.
- "opposite: hyperbolic distance" law: median 1.3%, worst >200%.
- The ladder breaks whenever a flat or mixed solution is involved (fixed only by the mirrored count).
- CS first matched only up to +/- pi^2/6 on 54 knots before the branching fix; comparison is modulo pi^2/2, not pi^2.
- Windings dropped: 1 of 79.
- Turn counted as roots inside the circle: nothing. Nothing tested correlates with Chern-Simons.
- HOMFLY on the plain two-phase torus carries nothing (rho = 0.036).
- Circuit polynomial is coarse (constant on knots with all crossings of one hand); it is labelled a "first attempt"; its invariance is a proof sketch.
- The solver's reach depends on the drawing; SnapPy drawings of 8_19 and 10_124 never reached the second direction.
- Arcs can share a direction; "The direction alone does not tell those arcs apart, and it does not fix k (mod 12, k = 2 and k = 4 both give 2/3)."
- Knots-as-colours lightness is "a compression of |V|".
- Elements barely reach the bowl region; knots and metals are "not yet joined" on the disk.
- Self-assembly: "not a formal identification; the law is untested beyond these six."
- Earlier conjecture (lift removes a residual pi^2/2) set aside; two inherited claims found circular, set aside (notes/SET_ASIDE_v6.md). Contents of that file: NOT READ (not in the PDF).
- sf_symmetry_01.py runs "on a model operator", not on the knot.
- Mirror caveat: 42 of 79 SnapPy named manifolds are mirrors of the KnotInfo drawing.

Section 13 Open problems (verbatim list)
1. Telling apart the torus arcs that share a direction (two on 8_19, two pairs on 10_124): a second label read on the disk, beside the direction, that separates them. Untested.
2. The fermion reading of the kept phase (Section 10): the Dirac-determinant phase on a cusped manifold with non-compact SL(2,C), for the unpaired three-dimensional operator; and whether the spin lift, with its -1 on the longitude, refines the twist beyond pi^2. Both rest on the rigor of complex Chern-Simons, the field's open frontier.
3. The arithmetic of P_K: its coefficients through the trace field, with LMFDB labels.
4. Colour inside the disk: dielectrics and the bowl.
5. Prior art on the circuit polynomial and on the sl(N) climb.
6. The 61 silent double walls of VOTKP v2.9 Table 6, in infinite-order knots, not covered by theory.
7. The parity of the Section 5 flattenings, to carry that comparison from pi^2/2 to pi^2.
8. The knot counts 12,954, 12,955 and 12,942 of three separate runs, to be reconciled.

Things the paper does not define or give (gaps, not filled)
- lambda in P_K: only "chosen to map the pi^2 period to a full turn"; no numeric value printed.
- k in the mirrored count epsilon_j[V0 - k|G-tilde_j|^2]: not given a value at that spot.
- N in Gamma = (1-N)/(1+N): not defined in words.
- "2/3 vacuum-mix line": named, no formula.
- "hyperbolic distance" on the disk: used (distance 0.5; the "opposite" law) but no formula printed.
- s in "s^2 = w" (trefoil arc end): not defined in this paper.
- Dirac Time arcs, signatures, section 5.2: referred to, not restated.
- Appendices A, B, C: not present in this PDF.
- Script contents and the attached archive: NOT READ (only file names are in the PDF).

Script names tied to results: c2_closed_form.py, c2_arb_enclosure.py, longitude_sign_01.py, spin_lift_cs_02.py, spinor_berry_cs_01.py, sf_symmetry_01.py, v6/torus_arc_roots_02.py, v6/torus_roots_search_01.py, majorana_braid_01.py, salvage_tests_master_01.py, cs_closure_probe_01.py, old_keys_checks_01.py, su3_spin_mc_01.py, bubble_ladder_01.py. Appendix D lists 79 script names in all (72 base + 7 under v6/), including silent_walls_01.py, pressure_line_01.py, film_phase_01.py, handedness_01.py, optics_01.py, shape_disk_01/02.py, roots_disk_01/02.py, roots_ladder_01/02.py.

---

## 7. What bears on the team's questions

### 7a. The disk / ball (Poincare) picture
- The words "Poincare" and "ball" do NOT appear in the body. ("Ball" appears only in "ball arithmetic" (Arb) and in the reference title "Two Trees in One Ball, v4".) The paper's object is a DISK: "a Smith-type disk whose centre is the vacuum and whose rim is ground."
- There are two disks, of the same Mobius kind:
  1. The Smith coordinate Gamma = (z-1)/(z+1): centre Gamma = 0 = matched point (vacuum); rim |Gamma| = 1 = total reflection (ground). Used for the elements (Gamma = (1-N)/(1+N)).
  2. The vacuum disk G(z) = (z - w)/(z - w-bar) for tetrahedron shapes: centre = regular tetrahedron (maximum volume V0), rim = flat tetrahedra (volume 0), outside = mirrors.
  Figure 1 draws both on "the same disk".
- The disk is hyperbolic in use: the paper measures "hyperbolic distance" from the vacuum (1,391 of 2,777 tetrahedra within 0.5) and tests it as an alternative law (it loses to the bowl: median 1.3% vs 0.076%). So in this paper the working distance from the vacuum is |G|^2 (the bowl), NOT hyperbolic distance.
- 3-space appears only as: PSL(2,C) = "the Mobius maps (the Smith chart's moves) and the symmetries of hyperbolic 3-space, where the knot's volume lives."
- Mobius maps are "the Smith chart's own moves"; cross-ratios (tetrahedron shapes, Figueiredo's u-variables) are the numbers that live on it.

### 7b. Steps r = ln z
- The paper gives Gamma = (z-1)/(z+1) = tanh((1/2) ln z) once, in Section 1, as the IQGT Smith coordinate. That is the only place ln z enters the disk coordinate.
- A variable named r, and "steps" in ln z, are NOT in this paper. (The letter r appears only as r12, r01, film reflection coefficients, and as an integer in R(z'; q, r).)
- Logs elsewhere: the log-parameters w0 = log z + p pi i, w1 = log z' + q pi i, w2 = -w0 - w1, where the integer windings p, q count half-turns (multiples of pi i). That is where integers attach to a logarithm of the shape in this paper: "Direction (twist) is integer: how many half-turns each piece's phase winds."
- Another integer step: the film winding "grows by one per 247 nm of film".

### 7c. Reflection Gamma = (z-1)/(z+1)
- Stated exactly, with centre = matched = vacuum and rim = total reflection = ground.
- For elements it is written Gamma = (1 - N)/(1 + N).
- |Gamma|^2 = 1/2 is the Schottky line (metals above, non-metals below). The same value |G|^2 = 1/2 is the dashed circle in Figure 1.
- "Bulk colour hides the phase of Gamma, and a thin film writes it back." "near ground the phase is present but pinned."
- "Free electrons push reflection to the rim (ground); bound electrons keep it near the vacuum."
- Every element's track winds one way (38 of 41): causality and passivity.
- The vacuum disk G has the same form with the matched point moved to w: G(z) = (z-w)/(z-w-bar).

### 7d. Walls
- "Walls" in this paper means the Levine-Tristram walls of VOTKP v2.9 ("Peeling kept a vector of traits, Levine-Tristram walls and colour; v2.9 Table 6 has 575 double roots"), and open problem 6: "The 61 silent double walls of VOTKP v2.9 Table 6, in infinite-order knots, not covered by theory." No new wall result is in this paper.
- Boundaries that act like walls on the disk, in his words: the rim (ground; flat pieces; |G| = 1); the Schottky line |Gamma|^2 = 1/2; the "2/3 vacuum-mix line"; the circle |r12| = |r01| across which the film winding jumps. The ladder "breaks" only for solutions with "pieces on both sides of the rim"; crossing the rim is handled by mirroring (G-tilde = 1/G-bar, epsilon = -1).

### 7e. Placing several equal balls on a hyperbolic field so light/energy passes from one to the next
- NOT IN THIS PAPER. There are no balls, no arrangement of several disks, and no transfer of light or energy between them.
- Pieces the paper does supply that such a construction could lean on (my listing of what is printed, not a claim the paper makes about balls):
  - Many pieces on ONE disk add: Vol(K) = Sum_j D(z_j) ~ Sum_j [V0 - (3 sqrt3/4)|G_j|^2 + ...]; each piece contributes full volume minus its squared distance from the vacuum.
  - The three-fold exact rotation G(Tz) = e^{2 pi i/3} G(z) with volume unchanged ("the axis switches, the direction stays").
  - Inside/outside: a mirror sits at 1/G-bar outside the rim and counts with sign -1.
  - Matching: centre = matched point (no reflection), rim = total reflection.
  - Mobius maps as the disk's moves, shared by light (Smith chart), electron (SL(2,C)) and knot (hyperbolic 3-space).

### 7f. What the vacuum is in his terms (and "between")
- Vacuum = the centre of the disk. On the Smith disk: "the centre Gamma = 0 is the matched point (vacuum)". On the vacuum disk: "G(w) = 0: the regular tetrahedron is the vacuum point", the piece of largest possible volume V0.
- The vacuum is the top of a bowl: volume falls away from it as (3 sqrt3/4)|G|^2. "A knot's volume is its pieces at full volume, minus how far each one sits from the vacuum."
- "the knot's geometry is the root nearest the vacuum."
- The trefoil's single arc ends "at alpha_end = 1/12, which is the vacuum point itself, s^2 = w". For 4_1 the class-1 coordinate of the geometric solution is w, "the vacuum point".
- Ground = the rim = total reflection = flat (zero volume).
- "The space between" in this paper is a materials statement, not a vacuum-between-bodies statement: molecular solids crossing "the 2/3 vacuum-mix line under squeeze"; "The metal/non-metal line and the 2/3 space-between line are the electron's choice to conduct."
- Space made by a knot: torus knots "make no space" (zero decay, pure direction); hyperbolic knots have volume (decay).
- A statement of what the vacuum BETWEEN separate balls is does NOT appear in this paper.

### 7g. The Sun and planets
- NOT IN THIS PAPER. No Sun, planets, orbits, gravity or astronomy anywhere in the 23 pages. The only mechanics is the tennis racket (Dzhanibekov effect; Montgomery's phase).

### 7h. Other items likely to be asked about
- Light: "Light strings" = Jones/HOMFLY polynomials followed as t = e^{i theta} runs round the circle "as colour runs from violet to red"; climb = Mahler measure, turn = swept area / mean |V|^2.
- Memory/time: "A loop that comes back still remembers, through its phase"; the kept phase = direction book = Chern-Simons turn; "Time in one reading is the kept record in the other."
- Pairing law: "the pairing cancels the even record and only the odd datum survives"; "The kept phase is the odd, unpaired record."
- Connection energy: only the single number 0.577350 (racket climb rate matching "the Connection Energy formula").

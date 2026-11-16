# Handoff notes — vacuum-disk rethink (Jeromie Beasley), 10 November 2026, v1
Read this first after any compression or in any new session. Then open the three read records.

## 0. The rule above all others
IQGT is the frame. Every object is a subspace held by a gap, read through the projector, never through single eigenvectors and never through an imported metric. Anything brought in from outside is a labelled input, not the frame.

## 1. IQGT anchors (from the build source, sections 1-13, App A-C)
- Tangent law: V = PiV + VPi, block off-diagonal, block X.
- Q = g - (i/2) Omega. g = (1/2) Tr(VW) = Re Tr(XY*). Omega = +i Tr(Pi[V,W]) = -2 Im Tr(XY*). The 1/2 is forced (g_theta-theta = 1/4).
- Cross-gap pair sums, weight 1/gap^2 (Lemma 3.1, Thm 3.6). A gap counts only for a COUPLED pair.
- Curvature bound |Omega| <= 2 sqrt(gg - g^2); equality iff Y = cX (complex line); exact deficit (6.3).
- Silent direction (Prop 4.3): leaves Pi fixed at first order, moves the metric at second.
- Refraction: g_parallel sin^2(theta) = const; index = sqrt(g_parallel) = subspace rotation rate. NOT lambda_min.
- Strata: polar (Pi constant along it, repels) vs fold (kernel across it, needs a supplied kernel direction). First moving order m: even = fold, odd = parametrisation artefact (Prop 8.6).
- Narrowing gap GUIDES; stopping rotation REFLECTS.
- One pair sum, many weights (7.2); response alpha(x) = sum 2 Delta^3 g/(Delta^2 - x^2).
- Tip and tail (10.2, 12.1): tail held by outer gap, tip by inner gap. tan 2 theta = 2g/Delta.
- Eigenphase to principal angle: theta = phi/2; count reads sin^2, intrinsic length reads theta^2 (12.2, 12.3).
- Example 6.5: projector returns, phase does not.
- Data standard: Level 0 raw angle, Level 1 geometric angle, Level 2 interpretation.

## 2. Where mainstream can blend in and skew the work
1. METRICS. His g lives on the projector bundle. Do not swap it with: a spacetime metric; the hyperbolic metric of H^3; the Poincare-disk metric. In the vacuum-disk paper the "hyperbolic distance" law was the OPPOSITE test and did worse (1.3% against 0.076%).
2. THREE DISKS, THREE CENTRES. Smith Gamma_S = (z-1)/(z+1) (centre z = 1). Vacuum disk G = (z-w)/(z-w-bar) (centre the regular tetrahedron). Chiral grading Gamma (not a disk at all). Gamma_diss is a fourth thing. Never carry a statement from one to another without redoing it.
3. SMITH DISK AS POINCARE DISK holds only for real Gamma (VOTKP 15.3): for complex Gamma the film map is not a hyperbolic isometry.
4. CHERN-SIMONS UNITS. His direction is in turns of pi^2: -k^2/(pq) mod 1. Literature forms differ by factors (k^2/(4pq), pi^2/2 period in SnapPy, 2 pi^2). SnapPy's manifold is the mirror of the KnotInfo drawing for 42 of 79 knots. Convert explicitly every time.
5. TORUS-ARC CONVENTIONS. alpha (meridian phase, 0 to 1/2) vs x = 2 alpha; omega = M^2 = e^{4 pi i alpha}; the (u,v) choice with uq + vp = 1 changes the listed k but not the direction.
6. KNOWN THEOREMS IN HIS COORDINATE. Determinant inequality, Davis-Kahan, Brockett flow, Clairaut, Neumann's CS formula, Kirk-Klassen torus CS, Bloch-Wigner. He already marks these REPRODUCTION. They stay marked; they are never promoted, and they never go in as filler.
7. IMMERSION ASSUMPTION. The band-geometry literature assumes det g != 0. His contribution is exactly where that fails. Importing a Kahler/ideal-band result imports that assumption.
8. ORIENTATION IN THE SCALAR SPECTRUM. Mainstream eta / spectral-flow language puts the sign in eigenvalues. His One Law (Dirac Time 5.3): under chiral pairing every odd scalar record vanishes; orientation lives only at projector level. rho = -sigma is an identity of COUNTS; the gluing to the boundary record is not proved.
9. THERMODYNAMICS. Metric is not entropy production. Cost needs a declared bath; SLD metric vs Kubo-Mori metric are different.
10. REGULARISATION AND NON-HERMITIAN. i-eta gives a response, not a tangent vector; positivity, Gram and real angles do not apply. Same for biorthogonal idempotents.
11. FIELD-THEORY IMPORTS IN THE VACUUM-DISK PAPER, SECTION 10. Parity anomaly, APS eta as fermion phase, complex Chern-Simons (Redlich, Witten) are compact-group or physics-level results used for a non-compact SL(2,C) statement. This is the largest mainstream import in v5 and the place most likely to carry outside assumptions. Raised once here; his call.
12. VOLUME CONJECTURE / sl(N) LITERATURE. The Jones and HOMFLY climbs are empirical correlations; do not let volume-conjecture asymptotics stand in for them.
13. PROCESSED DATA. He works from raw data. KnotInfo, SnapPy, refractiveindex.info, NUBASE are other people's computed or measured tables: inputs with provenance, never his measurements. Model-fitted products (cosmology pipelines) are context only.
14. GRAVITY AND COSMOLOGY. Projector metric is not spacetime metric; horizon is not a metric wall; rate gradient is not curvature; dark energy and dark matter stay out.
15. WEAK VALUES are instruments, not mechanisms.
16. SINGLE EIGENVECTORS. Any outside method that tracks one eigenvector through a near-tie breaks the tail/tip rule.
17. MEMORY NOTES AND AI VERDICTS. Past session verdicts are not his work. Read the paper.

## 3. State of the reading
READ IN FULL: IQGT build (s1-s13, App A-C); Dirac Time v3.1 (all); Vacuum disk v5 (all 25 pp).
Records: READ_RECORD_01_IQGT, _02_DIRAC_TIME_v3_1, _03_VACUUM_DISK_v5 — in the top level of Drive, titles starting "2026-11-10 Read record".
NOT READ: Two Trees v4 (437k chars); What the Present Must Keep v1.1 (47k); confirmation run report v2 (27 pp); Knot Atlas page; four code zips; vacuum disk v6 (not reachable); UPG (July originals, v3 tex, v3.2); VOTKP v2.0 source (only 5 and 15.2 read), v2.1 package and v2.9 (not reachable in full); IQGT June originals and v6-v7.3.1 as versions; tail of IQGT App D.
Local copies this session: /home/claude/text (clean texts), /home/claude/corpus, /home/claude/src (four repos), /mnt/user-data/uploads (his attachments). These vanish with the session; Drive records do not.

## 4. Results so far (all from his own theorems)
- Arc end steps: Dirac Time Thm 13.1(3), k = uaq +- vbp.
- Direction -k^2/(pq) is the same at both ends of an arc (difference 4uvab*pq). Checked, zero disagreements.
- 8_19: arcs (1,1),(1,3) -> 11/12; (2,2) -> 2/3. 10_124: (1,1),(2,4) -> 14/15; (1,3),(2,2) -> 11/15. So open problem 1 of v5 should expect ONE new direction per knot. Not yet run against the root search.
- Direction alone does not separate arcs (47 of 53 torus knots collapse).
- A total turn along an arc is linear because beta = a/2 - pq*alpha (Thm 13.1(1)) and the affine readout has a constant numerator (9.2).

## 5. Open, untested
- End-point product repair for the UPG eq.(3) total turn.
- Is the direction the theta^2 reading (IQGT 12.3) of the end step? theta = pi k/(2pq) gives theta^2 proportional to k^2/(pq)^2, not k^2/(pq): the powers of pq do not match as it stands.
- Sign of g in z(a) = kappa - g/(a-d) as a hidden-level test (VOTKP 5.3).
- Thomas rotation per edge; 120-degree corner turn against the pi^2/3 shift on 7_4 and 7_7 (defined in v6, not seen).
- Fold / first-moving-order reading of the arc ends (IQGT 8.6, 8.7).

## 6. Next step
What the Present Must Keep v1.1, then the confirmation run report v2, then Two Trees v4 alone, each read in full with its own record.

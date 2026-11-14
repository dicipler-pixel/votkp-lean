# The Standard Model in the ball, and what happens at the walls — notes, 11 November 2026 (v3)

Jeromie Beasley. Working notes, prepared with AI assistance (Claude, Anthropic).
Grades: PROVED (exact algebra), CHECKED (computed, size given), RECOGNISED (established physics, cited), READING (interpretation), ASSIGNMENT (a choice, not derived), FAILED THIS WAY (kill fired in that setup).

## The question (his words)
"Plug all the particles, the whole Standard Model, in the ball tree setup, and also consider different ends to the tree — usually if it hits a wall it changes to a phase. Think how it works and try to build that out." Then: "do both" (both readings of the arms) "and keep notes of this".

## What was read first
- research/2026-11-10 on votkp-lean (branch claude/votkp-research-20261110): ZOOM_OUT_20261110_v1, FOUR_HOLES_20261110_v2, READ_RECORD_09 (One Tree, One Ball; Two Trees, One Scale; BallJoins J1–J8), outputs of LADDER-WALL-01, PHASE-LADDER-02, DEFECT-WALL-01, PLASMA-WALL-01.
- Atlas (relational-atlas-lean): full text of the 93 cards held locally (B1–B96 range), titles of all 207. Cards that already hold this path: B9 (around a defect the winding survives), B35 (phase crosses what amplitude cannot), B55 (where the geometry fails is a wall of its own), B79 (when the vector is unavailable, take the phase); by title only: B172 (the cover keeps a sign), B177 (the ISCO is a spectral wall, a Jordan block), B199 (one wall where the trace form vanishes). NOT read in full: B97–B207 (the v7 card zip is on Zenodo, not in the repo).

## The map (in the ball's own terms)
| the ball | the Standard Model | grade |
|---|---|---|
| the ball is the velocity space of one massive particle; one tree edge is a boost of rapidity ln 5 | γ = 13/5, v = 12/13 c — the 5-12-13 triangle (BallJoins J5) | PROVED |
| inside the ball | massive particles; spin is a full turn record (little group O(3)) | RECOGNISED (Wigner 1939) |
| the rim, the parabolic wall | massless particles (photon, gluons); only the helicity phase survives (little group E(2), parabolic) | RECOGNISED; = B35, B79, B177, B199 |
| just inside the rim | neutrinos: 0.05 eV (drawing value; not measured) at 1 MeV sits 10.88 tree levels out, 1 − 5.0e-8 from the rim | CHECKED |
| crossing the wall inward | the Higgs mechanism: W, Z leave the rim, gain a third (longitudinal) state; photon and gluons stay | RECOGNISED |
| Seiberg–Witten cusps / walls of marginal stability | a BPS state goes massless at a cusp (the monodromy integer survives); across a wall where central-charge phases align, bound states decay | RECOGNISED (Seiberg–Witten 1994; wall-crossing literature) |

Placement used in the mixer: give every particle one common energy E; rapidity η = arccosh(E/m); radius tanh(η/2). Heavy near the centre, light at the rim, massless on it.

## Different ends of the tree (from his 10 Nov classes)
1. Runs to the rim and never closes (free group; Lean free5/free7): a massive particle pushed forever.
2. Reaches the parabolic wall: massless; vector dies, phase kept.
3. Closes as a pure turn (elliptic): spin; torus-knot rows.
4. Climbs and turns (loxodromic): hyperbolic-knot rows.

## Exact numbers (run SM-BALL-CHECKS-01)
- One edge: γ = cosh ln 5 = 13/5, v = 12/13, ball radius tanh(ln5/2) = 2/3. PROVED.
- Koide: Q = 0.666664463, so cos² of the angle between (√m_e, √m_μ, √m_τ) and (1,1,1) = 1/(3Q) = 0.500001652. Distance from 2/3 is 2.2e-6; one sigma of the τ mass moves Q by 5.1e-6. Inside one sigma of Γ² = ½, his wall value. Koide 1981; 45° reading Foot. The fact is old; the coincidence with the wall line is the reading. A matching fraction does not make two invariants the same. READING.
- Generation steps as peel steps, all past the wall z = 3+2√2 = 5.828: μ→τ 16.82, d→s 19.89, s→b 44.74, c→t 135.6, e→μ 206.8, u→c 589.4 (Γ 0.888 to 0.997). Garrett's step 5 is inside. CHECKED. Reading: at the tree's step a loop of two perpendicular steps closes as a pure turn; at a generation step it would not.
- Lipschitz quaternions of norm 5: 48 = 6 arms × 8 units = 3 generations × 16 Weyl fermions, but only if right-handed neutrinos exist (45 without). Prior art: Lambek (24 Hurwitz units for one generation plus gauge bosons, baryon number along i+j+k); Gsponer–Hurni (math-ph/0511047) proposing the octahedral group Q48 for three generations. CHECKED count; ASSIGNMENT if used.
- The wall for the loop: the commutator of two equal perpendicular boosts has trace 2 − 4 sinh⁴(r/2) (BallJoins J4), parabolic at r = ln(3+2√2) = 1.7627, v = 2√2/3. PROVED.

## The two readings of the arms (built both, his call)
- A — arms are generations. Generation-blind bosons on the (1,1,1) diagonal. Koide's vector lives in arm space and sits on the 45° cone about (1,1,1), the wall angle.
- B — arms are colours (r, g, b; minus arms the anticolours). Seen down (1,1,1) the six arms are exactly the SU(3) 3 ⊕ 3̄ hexagon (PROVED: the projections of ±e_a onto the plane perpendicular to (1,1,1) are the six weights). Charged gluons are colour differences e_a − e_b (perpendicular to (1,1,1)); the two neutral gluons have zero colour vector; leptons and colour-neutral bosons sit on the diagonal (Lambek's baryon direction).
Open: neither reading is derived; both are assignments. Which (if either) the tree prefers is untested.

## The test of "the end changes to a phase"
SM-END-PHASE-01 (as first proposed). A spin carried along a tree end, each step a ln 5 boost along the next arm in the particle's own frame; polar split L = B(p)R. Prediction: the spin–travel angle (helicity cosine) freezes near the rim. Kill: mean |Δh| over the last 10 steps > 0.5 × first 10.
Result: FAILED THIS WAY on every non-straight end (ratios 1.073 twin-prime chain, 0.78, 0.82 random, 0.96 periodic). Opposite control (one arm only): no change, as it must.
What the run showed instead: the travel direction freezes (its per-step lab turn falls from 0.055 to about 1e-17 rad) while the spin keeps turning against it.

SM-END-PHASE-02 (the opposite reading, his rule "try the opposite"). Prediction written before the run: ln(lab turn of travel) falls with slope −1 against rapidity; the turn in the particle's own frame stays full size. Kill: own-frame turn last 10 < 0.1 × first 10, or slope not negative.
Result: survives on all three ends. Slopes −1.0061 (twin-prime chain), −0.9998 (random), −1.0002 (periodic i j k). Own-frame turn last 10 / first 10: 1.000, 1.097, 1.039 (twin-prime chain mean 0.815 rad per step both ends of the run). CHECKED at 80 digits, 40 steps (rapidity to 48.9).
Reading: at the rim the climb's direction dies as e^(−η) and the turn goes on at full size — B35 on the tree. The constant own-frame turn is the tree being the same from every ball (structure, not a discovery); the e^(−η) rate is how a path converges to its end in hyperbolic space (standard). What is his: the wall rule picks the right side once the test is pointed at the right book.

## Built
- SM_in_the_Ball_Mixer_v1.html — one ball, Garrett's tree, switch A/B. Eyes: (1) the end becomes a phase (the run above, with chart); (2) every particle in the ball (common energy slider, antiparticles); (3) the wall and the generations (loop slider with trace, Koide cone in A); (4) crossing the wall inward: the Higgs (v slider, W/Z states 2 → 3).

## Next, in turn (kept by his instruction, "don't forget these"; none run)
0. Which reading the tree prefers: a test that could fail — does the colour reading (B) make the gluon steps (arm changes) the tree's own edges with the right SU(3) commutators, or only the right weights?
1. The generation steps past the wall: is there a reading of z = 16.8 … 589 in Garrett levels (1.75 … 3.96) that is not numerology? Kill line needed before any run.
2. Koide in the tree's coordinate: does the 45° cone about (1,1,1) appear anywhere in the tree itself (the chain's signed turn is about (1,1,1), CHAIN-TURN-02), or only in the masses?
3. B97–B207 full text, before calling any of this new.

## Set aside (for the equation file)
- "The spin–travel angle freezes at the rim": FAILED THIS WAY (SM-END-PHASE-01). Failure condition: per-step helicity change does not shrink with rapidity for body-frame steps; the freezing is on the travel direction instead.

## His reading of the set-aside (11 Nov 2026, his words)
"Think what could cancel or null spin and what can it change into if it hit a wall. I sometimes think it's like orbital mechanics and sometimes dancing or racing." He gave this as his reading of the set-aside above ("the spin–travel angle freezes at the rim", failed this way).

Mapped onto the set-aside (READING; each line marks what is proved and what is untested):
- The failed form assumed the spin LOCKS to the travel direction at the wall. His picture has three outcomes at a wall, not one: the spin is CANCELLED by a partner, it LOCKS into a resonance with the orbit, or it CONVERTS into something else that keeps the record.
- What the runs showed is the third, conversion: the travel direction froze (lab turn falls as e^(−η), slope −1.00) and the turn carried on at full size in the particle's own frame (SM-END-PHASE-02). In his racing picture: the heading change around the track (the holonomy) is what is left once the straight-line speed stops mattering. In his orbital picture: past the wall the walk is a flyby, and a flyby keeps one number, its deflection, a phase.
- Cancel (dancing, partners): BallJoins J7 (PROVED) — reverse the order, reverse the turn. A spin carried along a word and a partner carried along the reversed word should cancel as a pair (total spin zero, like an electron pair or a Cooper pair). UNTESTED on whole tree ends.
- Lock (orbital resonance, tidal locking 1:1, Mercury 3:2): on a periodic end (i j k i j k …) the turn per lap should repeat lap after lap, a fixed turn per period, the spin phase-locked to the lap. UNTESTED.
- Null (straight line): one arm only gives exactly zero turn (CHECKED, the control in SM-END-PHASE-01): a pure climb carries no turn record (spin 0, the Higgs; amphichiral knots, pure climb).
- The three classes are the orbit classes by name: elliptic (bound, turns), parabolic (escape speed, the wall Γ² = ½), hyperbolic (flyby, leaves). Structural match only; reading the wall as zero orbital energy is untested.
- Physics where spin converts at walls (RECOGNISED): Einstein–de Haas and Barnett (spin ↔ rotation of the body); the spin Hall effect of light (handedness → a sideways shift at an interface); total internal reflection (|r| = 1, only the phase changes; the Smith-chart rim); the massless limit (sideways spin states become gauge, only helicity is kept).

Repaired statement of the set-aside, for the equation file: at the rim the spin does not lock to the travel direction; the turn record is kept and converts — it is cancelled only by a partner on the reversed word (untested), locked only on a periodic end (untested), and absent only on a straight end (checked).

## Round 2 — the tests run together (11 Nov 2026, his "let's run these")
Scripts and outputs: run2/ (each script carries its SCRIPT name; the kill line is in the script header, written before the run). The atlas read of B97–B207 was done by a second reader in parallel (section below).

### Cancel (dancing partners) — SM-CANCEL-LOCK-01/02
Why it proves it: every pure boost matrix is symmetric, so the reversed word's matrix is the transpose, L(w^R) = L(w)^T = R^T B(p), and the polar split is unique; the reversed word's own-frame rotation is therefore R^T = R^(-1).
- Exact check in integers (every boost is (13,12)/5): 5^n L(w reversed) = transpose(5^n L(w)) in 2000 of 2000 random words, lengths 1–39. PROVED for every word, CHECKED exactly.
- Note on the instrument: the first numeric run "fired" at 3.4e-56 against a 1e-60 line; entries reach 1e17 at 80 digits, so that line was tighter than the precision. The exact integer check replaces it.
- Reading (his picture): a spin carried along a word and its partner carried along the reversed word cancel exactly, like an electron pair in one orbital. BallJoins J7 holds for every word, not only two steps.

### Lock (orbital resonance) — SM-LOCK-03
Prediction: on a periodic end u u u …, the own-frame turn per lap converges to the twist θ of the loop, read independently from the 2×2 spin matrix, tr M(u) = 2 cosh((ℓ + iθ)/2). KILL: spread of laps 16–20 > 1e-8 or miss > 1e-8.
- Survives on all six ends: i j k (θ = 0.6237383551), i j (0), i j −i k (1.7065275791), i i j (0), i −j k −i j (2.8710335059), the twin-prime chain's first six arms (0.8625571466). Agreement 1e-20 to 1e-58.
- Instrument note: a first run at 120 digits "fired" at lap 60 because entries reach e^200; inside the resolved laps the turns had already converged. Run at 400 digits, 20 laps.
- Reading: a periodic end locks; the locked turn per lap is exactly the twist part of the loop's complex length. Standard geometry of screw motions; in his picture, the orbital lock.

### Item 0 — which reading the tree prefers — SM-SU3-CONE-01
KILL for "reading B gets the SU(3) gluon algebra": the Lie algebra generated by the tree's moves is not su(3) (dimension 8).
- FAILED THIS WAY: the three arm boosts generate dimension 6 (the Lorentz algebra); the turns between arms close on dimension 3 (rotations).
- What B does get, exactly: the six arms seen down (1,1,1) are a regular hexagon (0°, 60°, …, 300°, equal lengths) — the SU(3) 3 ⊕ 3̄ weights; the Hurwitz unit (1+i+j+k)/2 cycles i → j → k and a second octahedral unit swaps two arms: together S3, the Weyl group of SU(3). So B carries the colour labels and their symmetry, not the force. PROVED / CHECKED.

### Item 1 — the generation steps past the wall — SM-GEN-STEPS-01
Three scales: PDG low-scale; M_Z (arXiv:0905.1425 Table A.1 and its lepton running factors); GUT 2×10^16 GeV (arXiv:1206.5909 Table II, quarks only).
- H1 "whole Garrett levels (z = 5^n)": FAILED THIS WAY. The quark levels move with scale (c→t: 3.05, 3.51, 3.58; spread 0.53); mean distance to a whole level 0.19 / 0.33 / 0.28. A reading that changes with the measuring scale is not a property of the particles.
- H2 "every generation step is past the wall": survives at all three scales. Honest weight: this is the known strong hierarchy restated in his coordinate; it predicts nothing alone.
- OPPOSITE (neutrinos, SM-NU-WALL-01, NuFIT 6.0): with m1 = 0 (normal ordering) the step m3/m2 = 5.8165 ± 0.079 against the wall 5.8284: −0.15 σ (Δm²31/Δm²21 = 33.83 against (1+√2)^4 = 33.97). It needs m1 below about 2 meV (at 2 meV −1.99 σ, at 5 meV −9.7 σ); inverted ordering gives 1.015, deep inside.
- PRIOR ART (found and read): I. Alikhanov, arXiv:2601.18781 (26 Jan 2026), proposes (√Δm²31 + √Δm²21)/(√Δm²31 − √Δm²21) = √2, i.e. (m3+m2)/(m3−m2) = √2 with m1 = 0 — which is exactly m3/m2 = 3+2√2. The number is his, not new here.
- What is ours: in his coordinate that √2 relation is a peel step Γ = (z−1)/(z+1) = 1/√2, Γ² = ½ — the half-line wall. So the neutrinos' top step sits on the same wall where two equal perpendicular steps go parabolic (BallJoins J3/J4). Reading: the charged fermions step past the wall (hyperbolic); the neutrinos' heaviest step sits on it (parabolic); the neutrinos are the particles at the wall — which matches where they sit in the ball (just inside the rim) and his neutrino paper's subject. Prediction carried by this reading (untested, testable by others): normal ordering and m1 below about 2 meV.

### Item 2 — Koide's cone in the tree — SM-SU3-CONE-01, SM-CONE-TURN-02
KILL for "the 45° cone about (1,1,1) is in the tree itself": no exact hits and ½ not singled out.
- Positions: 117,186 nodes to depth 7, exact integer test: 0 on the cone; near ½: 1128 against 948 and 2004 at its neighbours. FAILED THIS WAY.
- Opposite, the turn book: 23,100 own-frame turn axes to depth 6: 0 on the cone; near ½: 24 against 0 and 120. FAILED THIS WAY.
- What the turn axes do single out: along an arm (4,828), exactly on the (1,1,1) diagonal (96 — the axis the twin-prime chain turns about, CHAIN-TURN-02), perpendicular to it (312).
- Reading: Koide's 45° lives in the masses, not in the tree's positions or turns (to depth 6–7). What the masses and the tree share is the number ½: Koide's cos² = ½ (charged leptons, an angle), Alikhanov's Γ² = ½ (neutrinos, a step), the wall Γ² = ½ (the tree). A matching fraction does not make these one invariant; that the same ½ appears three ways is the open question.

### Set aside this round (for the equation file)
- "Reading B makes the gluon steps the tree's own edges with SU(3) commutators": the tree's moves generate the Lorentz algebra (dim 6), not su(3) (dim 8). B gives weights and the Weyl group only.
- "Generation steps are whole Garrett levels": quark levels move by up to 0.53 between scales.
- "Koide's 45° cone is in the tree": 0 exact hits in positions (117,186 nodes) and in turn axes (23,100); ½ not singled out.

### Item 3 — atlas cards B97–B207, read in full (second reader, full text from the Drive copy of the continuous edition v4; all 111 ids present; 231,121 characters; only text drawn inside figures not read). Full record: atlas/ATLAS_B97_B207_READ_20261111_v1.md
Cards that already hold this path (key lines quoted exactly):
- B200 holds Koide: "Q = 0.6666644634, ρ K = 0.5000016525, centered books (0.999997, 1.000003)" — the two centred books balanced, h = s, critical damping. The lepton ½ was already his before today.
- B98 / B97 hold the tree's step: "0.25 ⊕ 0.50 = 0.75/1.125 = 2/3; artanh(2/3) = 0.8047"; "Γ = (I′ − I)/(I′ + I) = tanh(τ/2)" — the ratio-5 edge and the ball radius.
- B189: "E⁻/E⁺ = Γ², Γ = (d i − d j )/(d i + d j ) = tanh(½ ln d i /d j )" — each tree edge is one scalar edge with two books.
- B172 / B180: "An eigenline holonomy of −1 that only an orientation-keeping observer records" — the turn kept only by the oriented cover (the lab reading loses it; matches END-PHASE).
- B199: "positive gives a growing and a decaying mode, negative gives turning, zero with T ≠ 0 gives a Jordan block" — the elliptic / parabolic / hyperbolic wall rule (ISCO, critical damping, the spinning key).
- B128: a group commutator whose wall is the eigenvalue −1 ("At g = 0 (R has −1 in its spectrum, as at δ = 4) …") — the same place the boost commutator reaches trace −2 (B128 is for unitaries, not boosts).
- B197: three arms at 120° seen down (1,1,1), "The circulant's eigenvalues are d + 2t cos(φ + 2πj/3)", C₃ = 2cos 3φ the free cubic record; and "No prime here generates masses".
- B203: "Out by 0.4 and back by 0.4 has route 1.6 and endpoint 0" — the cancel: the signed record cancels on the reversed word, the route length does not.
Limits the cards set (carried into the readings above):
- TWO DIFFERENT HALVES. The wall Γ² = ½ is E⁻/E⁺ = ½ (B189). Koide's ½ in B200 is E⁻ = E⁺, the books equal. Different book conditions; nothing yet maps one onto the other. So: Koide sits with BALANCED BOOKS (B200); Alikhanov's neutrino step sits ON THE WALL (B189, BallJoins J3). The earlier line "Koide's 45° is the wall value" is corrected to this.
- B200 calls itself "a conditional reformulation, not a derivation"; with full dephasing the weight is ⅓; running masses are a different object; e₃ (the triangle's C₃) stays free.
- B199: "Equal books on a graph are not the wall"; its wall rule is for real traceless 2×2 blocks — a boost commutator in SL(2,C) needs its own reduction first.
- B189: the books cannot tell which end of an edge is larger — which way the Higgs crosses must come from the signed record (B203) or the response (B202).
- B177 / B179 keep the orbit wall (Jordan block) apart from the horizon (fold).
Not in the cards at all: the colour / SU(3) reading; the Higgs, helicity and 2 → 3 spin states (B118 counts 2j+1 states only); Wigner's little groups; the e^(−η) law (it follows from B97's coordinate, 1 − Γ ≈ 2e^(−τ), slope −1 — derived by the reader, on no card).
Untested coincidence the reader flagged: (3+2√2)² = (√2+1)⁴, the neutrino ratio's square, is the Apéry/Catalan root on B149.

## Next, in turn (after round 2)
1. Map the neutrino wall step onto B189's books: at the neutrino step E⁻/E⁺ = ½ exactly (if m1 = 0); what is the second book doing, and does the oriented cover (B172) give the neutrinos a sign the charged fermions lack?
2. Koide as balanced books (B200) against the neutrinos on the wall (B189): is there one map taking the charged-lepton triple to the neutrino pair? Kill line before any run.
3. B149: why the neutrino ratio squared is the Apéry/Catalan root — coincidence test with a control.

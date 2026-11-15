# The Standard Model in the ball, and what happens at the walls — notes, 11 November 2026 (v2)

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

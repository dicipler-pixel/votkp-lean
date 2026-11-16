# The four holes, worked — 10 Nov 2026

Jeromie Beasley. Working record (two workers: the main session took holes 1–3, a second worker took hole 4).
Grades: PROVED (exact algebra), CHECKED (numerics, size given), READING (interpretation), FAILED (kill condition fired).

## Headline

The half line Γ² = ½ is one number seen from five places.

| Where | Statement | Grade |
|---|---|---|
| Two Trees | commutator of two equal perpendicular steps is parabolic at z = 3+2√2 | his theorem 5.4 |
| UPG | the meridian's defect δ = 2 − (s² + s⁻²) has \|δ\| = 4 exactly there | PROVED (DEFECT-WALL-01) |
| Two Trees knots | k = −v(v + δ); on the real slice k reaches 4 iff \|δ\| ≥ 4 | PROVED |
| Atoms | of 5,737 ladder steps only 8 lie beyond it: Li, Na, K, Rb, Cs first steps; Be, B, C K-shell openings | CHECKED (LADDER-WALL-01) |
| A fade | the bend of log-brightness, (gap/2)²(1 − Γ²), has halved exactly there | PROVED, CHECKED to 20 digits (TIME-WALL-01) |

Earlier appearances already on record: the vacuum-disk metal / non-metal line (35 of 35 against 0 of 6) and the bowl.

## Hole 2 — colour

Read: *Colour Selects the Leader* v1.2 in full (READ_RECORD_10).

**2a. Two channels are one peel step.** PROVED and CHECKED (COLOUR-PEEL-01, 20,000 pairs, worst error 1e‑11).

- ratio z = x₁/x₂; share balance s₁ − s₂ = (z−1)/(z+1) = Γ
- Hilbert's projective distance = |ln z − ln z′| = peel distance τ
- Schrödinger's chromatic distance = |φ − φ′| with cos φ = Γ = tanh(τ/2), so dφ = ½ sech(τ/2) dτ

So the paper's two rulers ("Hilbert's ruler governs the selecting; Schrödinger's metric describes where the colour ends up") are the climb coordinate τ and its angle φ. The whole climb line has Schrödinger length π.

**2b. What it predicts.** For two channels a pass stretches Schrödinger's metric on a close pair exactly when c·cosh(τ/2)/cosh(τ′/2) > 1, which forces the pair to be carried toward white. CHECKED: formula right on 20,000 of 20,000 passes; 22 stretches, 22 toward white, 0 away.

**2c. Three channels.** The strict rule does not carry. FAILED in its strict form: with the paper's sampler and Exner's weights, stretches are 5.0–5.8% of toward-white passes and 3.0–3.4% of away passes (COLOUR-PEEL-03). The lean is there; the rule is not.

**2d. A correction for the colour paper.** The "955 of 20,000" count needs Exner's weights. Same sampler: Exner 861 / 882 / 933; unit weights 0 / 0 / 0. CHECKED (three seeds each).

**2e. The crystal is the defect.** Colour eq. (6): crossed port = |1−u|²/4. UPG: defect δ = |λ−1|², δ + g² = 4. So crossed fraction = δ/4. At the trefoil's two walls (α = 1/12, 5/12, ω = M²) the crossed fraction is ¼, defect 1, the clock d = 6. PROVED.

**2f. Positive channels cannot turn.** A strictly positive 2×2 map has discriminant (a−d)² + 4bc > 0, so it is always hyperbolic. Theorem 2's three cases are: settles exponentially (hyperbolic), settles as 1/n (parabolic, the Jordan tie), never settles (elliptic, the swap). PROVED; 0 of 200,000 in the random search for a counterexample.

**What this settles.** Hue is a climb-side record. It can pick a leader and it cannot carry a hand. The turn-side record of light is the pair of polarisation ports, and the paper already says so in its own words (§13: "one port cannot see an orientation; two can"). READING.

**Still open.** A pure phase θ is the same at every wavelength, so a turn gives a grey split sin²(θ/2), not a colour. A colour needs a length (retardance in nanometres). The knot supplies the phase and nothing supplies the length.

## Hole 1 — atom to knot

**1a. The ladder against the half line.** CHECKED (LADDER-WALL-01; 109 elements, 5,737 steps z = IE₍q+1₎/IE_q).

- Beyond the line (z > 5.828): 8 steps, all at a closed core.
- First step of the alkali atoms: Li 14.03, Na 9.20, K 7.29, Rb 6.53, Cs 5.95. Fr 5.50 is inside.
- K-shell opening: Li 14.03, Be 8.45, B 6.84, C 6.08; N 5.64 is inside; the bare limit is 4 (VOTKP Thm 8.2, Γ = 3/5).
- "The half line marks shell openings" FAILED: 8 of 694 closed-core openings are beyond it.

So no bare shell opening reaches the half line. A step is beyond it only when one electron sits alone outside a closed core and the core screens it well.

**1b. The optical wall energy is not in the ladder.** FAILED (PLASMA-WALL-01, 30 elements with a final crossing in range): Spearman of E_wall against IE₁ +0.06, against z₁ −0.28, against the valence sum +0.26.

**1c. The optical phase is.** CHECKED (PHASE-LADDER-02, 41 elements). The five atoms beyond the line on the ladder hold 5 of the top 6 optical phases at 1.5, 2.0 and 2.5 eV (Ca is the one intruder); one-sided rank-sum p = 2.7e‑6 each time. Within the five the order is reversed exactly: nearer the line on the ladder, larger phase (Cs > Rb > K > Na > Li). The even reading |Γ|² does not separate them (p ≈ 0.09).

Caution, stated once: five atoms. And the physics underneath is known (the alkalis are the free-electron metals with the lowest plasma energies). What is new here is only that the ladder's half line picks them and the odd reading finds them where the even reading does not.

**What this settles.** The atom does have a record that carries a phase, it is the optical one, and it is tied to the ladder through the half line. That is the atom side of a bridge. READING for the knot side: the same line is where a knot's meridian pair can first reach the top of the turning band. No atom-to-knot map is claimed.

## Hole 3 — time

**3a. Recovery.** VOTKP 13.7: "No Hamiltonian here makes a knot's meridian phase the driven parameter; that bridge is open." Dirac Time 9.4 and Colour §12 prove the other half: projector geometry is blind to H → sH + cI, so no rate can come from the geometry (Lean: `rescale_same_eigenvectors`, `rate_shift_unique`). The missing drive is therefore not hidden in the knot. What the knot fixes is the gear, L = (−1)ᵃ M^(−pq) (Dirac Time Thm 13.1), and a constant is read only between two branches.

**3b. What can be read with no calibrated clock.** PROVED, CHECKED at 50 digits (TIME-WALL-01).

- Colour eq. (7) for two parts is a peel step: τ = gap · t.
- Colour eq. (8) then reads (ln I)″ = (gap/2)² (1 − Γ²). 1 − Γ² is the transmitted fraction of the step.
- From an equal start the bend halves at ratio 3+2√2, at t · gap = 1.7627. The ratio "bend now / largest bend" needs no gap.
- Three parts: no single ratio (opposite test, counted).

One formula for both books: z(t) = e^((Δγ + iΔω)t) gives τ = Δγ·t on the climb side (the leaf clock) and θ = Δω·t on the turn side (the beat). READING.

**Still open.** A declared drive. Nothing here supplies one.

## Hole 4 — signs

See SIGNS_REPORT_20261110_v1.md (second worker), summarised below when returned.

## Set aside with failure conditions (for the equation file)

1. E_wall(element) read from the ladder: |ρ| < 0.5 on IE₁, z₁, valence sum. n = 30.
2. "Stretch only toward white" in three channels: 3.0–3.4% of away passes stretch.
3. "Half line = shell opening": 8 of 694.

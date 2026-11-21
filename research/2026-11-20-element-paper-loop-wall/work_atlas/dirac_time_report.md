# Dirac Time of the Gigantefermion: what connects to the loop wall

Seed file: `/home/claude/atlas/seed/dirac_time.json`. It has 86 entries:
- 31 PROVED-LEAN
- 30 DERIVED-IN-PAPER
- 13 STATED
- 7 COMPUTED
- 5 RECOGNISED (prior art)

## Which version was read

v3.1 (6 November 2026) is not on Drive in any form I could reach. I searched by title (Dirac Time, Gigantefermion, v3_1, 20261106, Research_Package, CHANGE_LEDGER), by full text, and checked the "nov 26 updates" zips. The Read record says its source was `Dirac_Time_Gigantefermion_v3_1_Research_Package_20261106.zip`, which was probably a chat attachment. The newest full text I could reach is v3.0.1 (25 September 2026), so:

- **v3.0.1 was read in full**: all 4,890 lines of `companion_sources/Dirac_Time_v3_0_1.txt` inside Drive's `Light_Framework_Source_Reading_20261111.zip`. A copy is at `/home/claude/atlas/src/paper/Dirac_Time_v3_0_1.txt`. The Lean repo's PROVENANCE also cites v3.0.1 (DOI 10.5281/zenodo.22978630).
- **v3.1 additions** come from two sources, and their entries are marked "v3.1 text not reachable":
  - the Drive Read record 02, read in full;
  - the 13 November session notes (`/home/claude/votkp-lean/research/2026-11-13-space-step/T14_dirac_time/NOTES.md` and `REPORT.md`), which were made from a full read of the v3.1 text.

  The v3.1 additions are:
  - §9.4 offset speed limit
  - §10.5 neutrino kept population
  - §13 two-strand recursion and the θ census
  - §17.1 Smith coordinate, exit line and nuclei
  - §18 three bounds
  - the App. A.0 notation

  I read the REPORT and the NOTES sections on §8–§26, the appendices and the ledgers. I skimmed the parts on §0–§7.
- **If he attaches the v3.1 zip**, the v3.1-only entries should be re-checked against it. Section numbers match between the two versions for everything that also exists in v3.0.1.

## The loop wall in Dirac Time

The paper never states Γ² = ½, z = 3+2√2, sinh a sinh b = 1, tr[A,B] = −2 or 45° as a wall. Where the wall shows up, it shows up through the same formula, Γ = (z−1)/(z+1) = tanh h with h = ½ ln z. I checked each identity numerically (script DT-WALL-CHECKS-01, `/home/claude/atlas/scratch/dt_wall_checks.py`).

**Same formula (tagged `loop-wall`):**
1. **Two-level friction weight, §12.6.** p₋ − p₊ = tanh(β∆/2), proved in Lean (`two_level_population_gap`). With z = p₋/p₊ = e^{β∆}, this is exactly (z−1)/(z+1). The wall Γ² = ½ falls at β∆ = ln(3+2√2) = 1.7627 (checked). This is the strongest link: a Lean-proved instance of the Γ map in his own thermodynamics.
2. **Smith coordinate, §17.1 (v3.1).** Γ_S = (z−1)/(z+1) = tanh(ε/2), with |Γ_S| < 1 exactly when Re z > 0. This is the peel coordinate of the element paper. The paper names the rim |Γ| = 1, not the inner wall.
3. **Nuclei, §17.1 (v3.1, from VOTKP v2.9).** ⁴He sits at |Γ_S| = 0.579, which gives Γ² = 0.335, inside the wall. ⁵He, ⁵Li and ⁸Be are at 1.074, 1.220 and 1.025: outside the rim, so past the wall too. This is the direct bridge to the element paper's peel ratios. The wall is not mentioned there.
4. **Neutrinos, §10.5 (v3.1).** The Smith coordinate is (r−1)/(r+1), with rapidity ½ ln r and r = κ₂/κ₁. This is the h = ½ ln z form exactly. Warning: here G is a share in (0,1), not the peel coordinate.
5. **Offset speed limit, §9.4 (v3.1).** At rank one, τ_off = ln((1−C)/C). With C = (1+G)/2 the bound becomes (Ġ)² ≤ 4g(1−G²). That dictionary is untested for the peel.
6. **Saturating pair, §18 (v3.1).** τ_off = 2σ artanh(sin 2Ωt) means Γ = sin 2Ωt, which crosses Γ² = ½ at 45°. This is my reading of the formula, not something the paper says. The §18 bundle is tagged [framework; proposed] and is Claude's version per the v3.1 change ledger, so it should not be cited as his.

**Forms from the wall list that Dirac Time does contain (tagged `wall-adjacent`):**
- **The −1 return.** §5.2 gives holonomy −1 per winding with the spectrum fixed. The 720° return follows from it but is never written out. v3.1 adds "half the unit monopole flux".
- **Chiral pairing.** §5.3 gives ΓP₊Γ = P₋, and Lean covers its η-killing half (`eta_eq_zero_of_chiral`). Convention trap: this Γ is the chiral grading σ₃, not the Smith Γ. v3.1 App. A.0 separates the two symbols.
- **Arc end points α_end.** Theorem 13.1(2)–(3): each arc runs between α± = ‖½(ua/p ± vb/q)‖, and its ends are Alexander roots ω = e^{±2πik/pq} with k = uaq ± vbp. The congruences k ≡ a (mod p) and k ≡ ±b (mod q) are proved in Lean (`end_index_mod_p`, `end_index_mod_q`).
  - These end points are exactly what the vacuum-disk formula direction = −4pq α_end² mod 1 uses. With α_end = k/(2pq), that gives −k²/pq.
  - The trefoil arc runs over (1/12, 5/12), which I checked. Its lower end has ω = e^{iπ/3}, the vacuum point s² = w.
  - Lean `alex31_wall_at_sixth` puts the trefoil root at x = 1/6 in the ω variable, which is α = 1/12.
  - Direction at that end: −24/144 ≡ 5/6, checked.
- **Torus knots and signatures.** Theorem 13.1 is the peripheral law L = (−1)^a M^{−pq} plus the silence law; the silence law is in Lean. Theorem 13.2 says the number of arcs over α equals ½|σ_K(e^{4πiα})| = ½|ρ|.
- **A Jordan block, §10.3.** It appears only as a "same trace, different dynamics" control. The wall is never called an exceptional point.
- **"The ledger can survive a metric wall", §17.1.** This is a template for the loop work, not the Γ² = ½ wall.
- **Exit line, §17.1 (v3.1).** Its Petermann factor of 2 sits on the rim crossing, not on the wall, where 1/(1−2G²) diverges.

**Checked and not present:**
- On the trefoil SU(2) arc, tr[X,Y] runs over (−1, 2) and never reaches −2. So the tr[A,B] = −2 form of the wall is not on the trefoil generators. Peripheral pairs commute (trace 2).
- Nothing in the paper has sinh a sinh b = 1 or z = 3+2√2.
- "Wall" in Dirac Time always means a unit-circle Alexander root, or in §17.1 a metric rim. It never means Γ² = ½.

## What is proved and what is stated

**Lean, `dicipler-pixel/dirac-time-lean`** (branch main, HEAD e8a4c86; README: 86 theorems, no sorry). It covers:
- §2 predictive quotient (three headline theorems), §3.1 memory filtration
- Theorem P1 tangent, positivity, block formulas and metric-curvature inequality
- Theorem P2 weak-value bound
- Theorem P3 path ledger, plus positive reachability running both ways
- Theorem P4 instantaneous identity and Corollaries P4.1–P4.3
- Theorem P5 discrete and continuous forms
- Theorem P6, with unitarity via Physlib
- §9.2 affine readout, §11.4 equal-endpoint witness
- §12.6 pairwise friction algebra, tanh and zero-temperature band
- Theorem 13.1(3)–(4), §15.5 sector reduction

**Lean, `dicipler-pixel/dirac-time-d25-lean`** (branch master, HEAD ba5b23f; the Count Me as One paper cites commit 6c34d2c2). It covers:
- finite-dimensional chiral η-killing law, η(−D) = −η(D) and the torus symbol
- trefoil and figure-eight Alexander walls on the circle
- the circle odometer
- a Bringmann–Hikami–Lovejoy q-series check, which is not in the Dirac Time text

**Not in Lean:**
- Theorem 13.1(1)–(2), the SU(2) arcs
- Theorem 13.2
- the §12.6 slow-driving derivation
- the Theorem P4 propagator form
- §16.4
- §15.3
- every physical hypothesis

**Derived in the paper but not proved in Lean:** §5.3 item 3, §13.4, §15.3, §16.4, §22–23.

**Imported from companions** (stated here, proved elsewhere): the offset speed limit, the neutrino bound, connection energy and the peel control.

**Open in the paper:**
- the gluing from the boundary record to the bulk ρ
- the exterior APS problem (T7)
- the arrow model (T10)
- a Davies bath
- a stationary Maxwell–Dirac solution with linked field lines
- an analytic derivation of the exit line

## Files read

| File | Read in full? |
|---|---|
| Dirac_Time_v3_0_1.txt (v3.0.1, 4,890 lines; Drive zip `Light_Framework_Source_Reading_20261111.zip`) | yes |
| Drive "2026-11-10 Read record 02 — Dirac Time v3.1 …md" | yes |
| T14_dirac_time/REPORT.md (local, 13 Nov) | yes |
| T14_dirac_time/NOTES.md (local, 111 KB) | no: §8 to the end and the ledgers read; §0–§7 skimmed |
| dirac-time-lean: README, LIMITATIONS, PROVENANCE; PhaseSilence, FrictionMetric, Headline in full; declarations and statements of every other DiracTime/*.lean and FalseControls file | statements yes, every proof body no |
| dirac-time-d25-lean: README, AlexanderWall, ChiralEta, CircleOdometer; BhlBoundaryTest headers and statements; Axioms.lean | statements yes |
| vacuum-disk v6 (local), the α_end / direction passage only | no (lines 215–245 and grep) |
| Drive v3.1 package zip | not found |

Nothing was written to GitHub or Drive. Both repos were cloned read-only into `/home/claude/atlas/src/`.

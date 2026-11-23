# OG scan: original VOTKP and Dirac Time work, read against the table and shape work

Jeromie Beasley · scan notes · 23 November 2026

Read in full: `our math.txt` (8 Mar 2025, first resonance / 3-6-9 thread), Knot_Memory_Torsion_Volume_Research.md (7 Sep),
Knot_Field_Strongest_Current_Form.md (7 Sep), dirac_time_gigantefermion_v1.pdf (17 Sep), GIGANTEFERMION_ALL_IDEAS_AND_QUESTIONS_LEDGER (18 Sep),
VOTKP v0.2 (23 Sep, Parts I–III to §12).
Not found on Drive under those names: the July 9/10/11 "Relational Transport Geometry … Twisted Dirac Systems" PDFs and the 23 Aug Sofic–Torsion–Atlas note.

Grades: **derived** (follows from the math), **measured** (run on data, script exists), **untested**.

## Already in the originals, and the current work should say so

| Original | Where | Bears on | Grade |
|---|---|---|---|
| Γ_k = tanh(½ ln IE_{k+1}/IE_k): peel shape is a Smith log-impedance; the ionization onion is a reflection atlas | VOTKP v0.2 §8.1, Thm 8.1 | The peel step in every table and shape tool starts here, 23 Sep | derived |
| Run 01: peel vector vs static ln IE, static with level removed, Z alone, shuffled peel; held-out group accuracy 0.95 at K=10 (shuffled 0.04) | v0.2 §8.2 | Half of the fair baseline asked of Codex on 23 Nov already exists. Still missing: Magpie/mat2vec/Atom2Vec, and the same scoring as the column-recall table | measured |
| Depth ladder: short windows miss exactly the elements whose outer shell is past the window (62 of 65 misses) | v0.2 §8.3 | Explains low recall at shallow rungs in the shapes table; a shape cannot fix a window problem | measured |
| Shape carries family, level (ln IE₁) carries response: ln α = 10.28 − 3.04 ln IE₁, R² 0.906 | v0.2 §8.5 | Every chart in the shapes work reads shape only. The address diamond is shape × shape. Level is a missing second axis | measured |
| Ridge census: Ar/Kr closures shrink about tenfold, Xe-like vanishes, Ni-like 28 grows with charge | v0.2 §8.4 | Not shown in v2.2. Natural layer for the deep-rung rows | measured |
| Snell / orbital-subspace refraction test failed; refraction ≠ reflection after detrending (r 0.02–0.03) | v0.2 §9 | The Smith–Snell work this month should cite this as the earlier negative | measured (negative) |
| Metal films: one Smith radius \|Γ\| ≈ 0.93 splits bump vs no-bump in 99.4% of 171 cases | v0.2 §6.4 | See lead L1 | measured |
| Observability kernel: ker O_{r+1} ⊆ ker O_r; coarsening only adds blindness | Ledger §4; v0.2 Thm 3.1 | Same theorem behind "counts are invariant across shapes": a shape is a readout of the same record | derived |
| "Same exterior, different interior": equal peripheral eigenvalues, different traces; same knot, Hopf charge 7/10/11/13/15 | Ledger §7; knot checkpoints | Same pattern as one Γ position on different shapes | derived |
| Projector metric g = ½ Tr(∂P ∂P); old eigenvalue stress misses isospectral projector motion | Ledger §12 | GRAD-PROJECTOR-01 is this line continued | derived |
| Trefoil gearing: LM⁶ = −1 gives 6 dθ_M + dθ_L = 0; one collective coordinate; a silent sector exists | Dirac Time v1 §3 | A derived 6 from the trefoil peripheral relation. See lead L2 | derived |
| A torsion Laurent unit can counterfeit two turns | Dirac Time v1 §4.3 | Any winding or turn count read off a shape chart needs the same normalization check | derived |
| 8₁₉ = T(3,4) is a torus knot, not hyperbolic | Ledger §27 | Permanent negative control, still standing | derived |

## What dropped out and is worth bringing back

1. **The level axis.** The shapes table charts only the peel shape. The original split was shape (family) and level (response). Proposed: the second coordinate of the address diamond is ln IE₁ (or Γ of IE₁ against a reference), not a second shape reading. Untested.
2. **The metal-film disk.** v0.2 put atoms (positive real radius) and metal surfaces (lower-left of the disk) on one Smith disk. The shape work dropped the surface side.
3. **Ridge census as a layer** in the v2.2 table drawer.
4. **The Run 01 controls.** Tell Codex the static/level-removed/shuffled scaffold exists and should be reused, so the fair baseline is one table.

## Leads (untested, kill conditions written first)

- **L1. Film threshold vs the wall in the physical map.** The wall Γ = 1/√2 drawn in the Klein (physical) map sits at 2Γ/(1+Γ²) = 2√2/3 = 0.9428. The film split was fitted near 0.93. Test: refit the threshold on the 171 cases with a bootstrap interval. **Kill:** if 0.9428 lies outside the 95% interval, or a threshold at 0.9428 scores more than 1 point below the best, drop it. Needs the v0.2 film script and data.
- **L2. A home for 6.** The trefoil T(2,3) longitude is −M⁻⁶, and pq = 6 for T(2,3). For T(p,q) the peripheral relation gives L = ±M^{−pq}, so 3-6-9 would need knots with pq = 3 or 9, and there are none with p,q ≥ 2 coprime giving 3; pq = 9 fails coprimality. **As stated this kills the knot home for 3 and 9.** Only 6 has one.

## The March 2025 thread

`our math.txt` is the first seed: Tesla's 25 Hz winding, 3-6-9 as harmonic octaves, Russell's two-way universe, ground/water/air-ether as three media, Dirac's symmetry. The percentages in it ("90.2% close", "100% fit") came from the chat model, with no tests behind them. The programme from July on replaced them with kill conditions. What carries forward from it is the questions: scales of media (Plato's elements as scales), 3-6-9 as a ladder, and two-way motion (the two rails in the Dirac Time ledger, the open/short mirror in the shapes work).

# The Standard Model in the ball — notes v4 (11 Nov 2026)
Jeromie Beasley

v4 adds two things to v3:
- A full read of every old VOTKP / Elemental Peeling build, earliest first, by eight small readers. Their reports are in `votkp_reads/READ_A1…A8.md`; the brief they worked from is `BRIEF.md`.
- Every element's ladder run through the ball, in `elements/`.

Everything in v1–v3 stands.

## 1. The ball was in the old builds; the wall was not, until the light
The pieces turn up in this order:

| Build | What it already has |
|---|---|
| Elemental Peeling v1 (13 pp) | T₋ − T₊ = 4x(2−x²)/[…], a sign change at x = √2. Not yet tied to the step ratio (untested). |
| v0.2 (dropped later) | The Doppler reading: a step's β = (z−1)/(z+1) = Γ, a velocity. |
| v0.3 / v0.4, Thm 8.1 | IE ratios as Smith reflections, τ = 2 artanh Γ = ln z. Alkali τ₁ = 2.641 (Li) … 1.705 (Fr). |
| v0.3 (dropped later) | One reflection law r = −tanh(τ/2) for light at a metal, an electron leaving an ion, and a matter wave at a step. |
| v0.5 Thm 15.1, Cor 15.2–15.3 | Peel steps add as rapidities; echo weight 1 − Γ² = sech²(τ/2) = 1/γ². This is the two-book weight. |
| v0.7 (dropped later) | Peel composition is Einstein velocity addition, with slope 1 − Γ² at zero. |
| v0.8 / v1.x | "Successive peel steps compose as successive boosts." v0.8 §15.2 records that no prior use of this law for ionisation ladders was found. |
| Vacuum disk v6 §9, the Schottky line | \|Γ\|² = ½ averaged over the visible separates metals (35/35 above) from non-metals (0/6 above). |
| Matter Formal ed. D1 | Γ_b = √(1−4λ); λ = 1/8 sits on Γ_b² = ½. |
| Atlas II, Past the Wall | The rim \|Γ\| = 1: unbound nuclei (⁵He 1.074, ⁵Li 1.220, ⁸Be 1.025) sit outside it as half-turn peels, with rim distance 2s/(S_next − s). |

No version draws Γ² = ½ on the ionisation chart. Yet every version's alkali list already straddles it:

| | Li | Na | K | Rb | Cs | Fr |
|---|---|---|---|---|---|---|
| Γ (v1.x) | 0.867 | 0.804 | 0.759 | 0.735 | 0.712 | 0.692 |

1/√2 = 0.7071 falls between Cs and Fr.

## 2. Three zones of the ball
- **|Γ| < 1/√2.** Two equal perpendicular peel loops close as a pure turn. This holds for almost every atomic step and for every non-metal film.
- **1/√2 < |Γ| < 1.** Bound, but past the half-line wall. The loops do not close, so the amplitude cannot cross and the phase carries the record. This zone holds:
  - the alkali first steps;
  - the K-shell openings of Be, B and C;
  - every metal's visible reflectance (Schottky line).
- **|Γ| > 1.** Unbound. This is Atlas II's zone of half-turn peels.

The light reading and the ionisation reading put the same circle in the same place. In light, metals are past the wall. In ionisation, a lone electron over a closed core is past it.

## 3. How each element plays out (`elements/`)
Scripts:
- `element_ball_01.py` runs 118 elements: 103 full ladders, 5,328 contiguous steps.
- `core_open_02.py` and `iso_cross_03.py` cover the core openings and the isoelectronic lines.

Kill lines were written in each header before the run.

**K1, largest step at a noble core. Passes.** 101 of 101 elements.

**K2, a whole shell peeled as one boost sits at the wall. Failed this way.** The median |Γ²−½| is 0.404, against 0.297 for random blocks. The opposite reading (a whole shell sits past the wall) also failed: 0.296 against 0.338. The wall belongs to single steps.

**One crossing per core.** Each core-opening isoelectronic line crosses the wall exactly once. The hydrogenic limit (n_out/n_core)² is always inside the wall.

| Core | Last past the wall | First inside |
|---|---|---|
| He | C³⁺ 6.080 | N⁴⁺ 5.640 |
| Ne | Na 9.20 | Mg⁺ 5.33 |
| Ar | K 7.29 | Ca⁺ 4.29 |
| Kr | Rb 6.53 | Sr⁺ 3.89 |
| Xe | Cs 5.95 | Ba⁺ 3.58 |
| Rn | none | Fr 5.50 |

- Neutral atoms: period 2 is past the wall for valence 1–4 (Li, Be, B, C). Periods 3–6 have only the alkali past it. Period 7 has none.

**Francium is the open prediction.** Fr IE2 = 22.4 ± 1.9 eV is a semi-empirical value (grade S). Francium is past the wall if and only if Fr⁺ IE > 23.74 eV. Cs is past it by 2% (Γ² = 0.5071), and it is the only step within 0.01 of the wall.

**Step counts.**
- 5,328 contiguous steps in this run.
- 5,737 in the 10 Nov round (all listed thresholds).
- 3,655 (to Z = 86) and 5,714 (to Z = 110) in v1.x.

The counts differ by cutoff only. The 8 past-wall steps are the same in each.

## 4. Open contradictions (kept, not resolved)
- **v0.2 §8.1, v0.3 line 268 and v1.x Thm 8.1 say "the atomic chart carries no phase".** The wall reading needs phase at the wall. A real Γ is phase 0 or π, so the reading has to say where the phase lives: in the turn of the closing loop, not in Γ itself. That turn is untested on ladders.
- **v0.5 / v0.8 test H-01 killed 1 − Γ² as a group separator** (0.743–0.778, against |Γ| at 0.96–0.99). The separator job is a different job from the wall. The wall uses Γ² = ½, which is where E⁻/E⁺ = Γ² = ½ (the B189 books), so it is not 1 − Γ² as a ranker.
- **The colour report:** visible colour follows the IE₁ level (AUC 0.946), not the peel shape. Colour lives on the level, the wall on the step.

## 5. Leads from the reads (untested)
- **The vacuum v6 "2/3 vacuum-mix line".** Γ = 2/3 is one edge of Garrett's ratio-5 tree. v6 never defines the line. Te, P, Se, I, Br and S crossing it under pressure rank their metallization pressures at ρ = 0.89, and Si, Ge and B already sit on it. Next: recover its definition from v6's source and test whether it is z = 5.
- **Elemental Peeling v1's √2 sign change:** what x is in the ladder language.
- **v0.8 Thm 6.2's exact boundary-circle proof** (A.11) is the method to reuse for a proof of the Γ² = ½ circle.
- **v2.9's LS-to-jj stagger read from thresholds:** 84% of p subshells, against 40% by chance. The f version was killed, 0 of 36. Spin–orbit on the ladder is a natural place to look for the "convert" reading.

## 6. Reading gaps
- v2.9 was read only from §6.4 to mid-§15.10, because the Drive export was refused for size and the html is truncated. §15.10 to Appendix G is unread.
- v0.3/v0.4 were read in full in markdown; the html was checked structurally.
- Figures were not viewed by any reader; their captions were read.

## 7. Printed slips found (for the ledger, not the papers)
- Elemental Peeling v3 §7.1: "d = 2" should be √2.
- v0.8 §8.9: the row-swing identity fails at a = 2, b = 1 as printed, probably a dropped bracket.
- Matter v3/v4: Γ_b = 1 − 4λ is missing its root, "6c ln" should be (c/6), and v3's "bracket 1/π²" is corrected in v4.
- v2.0/v2.1 are headed "Claude's version", so they are not his text.
- v2.9 cites AI-written OpenAI 2026a/b for the Thomas–Fermi law.
- Bylines read "Jeromie N. Beasley" in Elemental Peeling v1–v3 and Combined.

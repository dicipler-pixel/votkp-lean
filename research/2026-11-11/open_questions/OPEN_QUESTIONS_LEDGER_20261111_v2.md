# Open questions: notes and tests, 11 November 2026 (v2)

Jeromie Beasley · working ledger

Every test below had its kill line written before it was run. Every script named here is in this folder, so every item reruns from this folder alone:
- items 1–6: open_tests_05.py and the rerun JSON;
- items 7 and 12: large_field_floor_02.py and one_plaquette_phase_01.py;
- items 8–9: one_plaquette_phase_01.py and small_field_gap_03.py;
- items 10–11: snell_smith_trees_04.py;
- the B189 follow-up: b189_constant_06.py.

Scripts 03 and 04 take the paths to the yang-mills-lean research folders as arguments. Anything that fails is kept here with its failure conditions, not dropped.

Changes from v1:
- every script is now in this folder;
- the Ky Fan wording is fixed (item 3);
- the torus scaling is stated separately for μ_min and for the gap (item 9);
- B189 is settled (item 5).

## Tested tonight

| # | Open question | Test | Result |
|---|---|---|---|
| 1 | Does the old 19-state two-square certificate still certify a gap? | Rerun `two_plaquette_19.py` | **Holds.** 694 exact checks, 2 refusals as designed. Certified gaps: 5.284 (λ=0.1), 5.103 (0.5), 4.909 (1), 4.274 (2), 2.467 (3), 0.991 (4). This is atlas Link A (rank-2 retained block) and already exists. |
| 2 | B75: E₀ concave in κ but the middle level E₁ not? | One plaquette, λ = 8, κ ∈ [0.2, 3], second differences | E₀ concave (max d² = −0.57). E₀+E₁ concave (max −1.46). **E₁ also concave here** (max −0.89). B75's obstruction does not show on one plaquette at λ = 8. It may show on larger graphs; untested there. |
| 3 | Ky Fan route: gap ≥ chord(E₀+E₁) − 2E₀ | One plaquette, λ = 8, chord from κ = 0.5 to 2 | **Not a certified bound yet.** The test uses the exact E₀ where a proven upper bound must go. So "no violations" measures how much the chord loses (15 to 33%: 3.22 to 5.48 against true gaps 4.39 to 6.24). It does not certify anything. A certificate needs the endpoint values certified and E₀ replaced by a Rayleigh–Ritz upper bound. |
| 4 | B160 scaling window: do gap ratios settle? | One plaquette, r = (E₂−E₀)/(E₁−E₀) | **Holds.** r = 1.612, 1.541, 1.518, 1.509, 1.504 at λ = 2, 8, 32, 128, 512. It tends to 3/2, the oscillator singlet ladder (two quanta, then three). |
| 5 | B189: does the leading gap depend only on κλ? | One plaquette, κλ = 64 fixed, κ from 0.25 to 4 | **Settled.** The gap is exactly homogeneous, gap(κ, λ) = κ·G(λ/κ), so c depends only on λ/κ, not on κλ. Rerun at κλ = 16, 64 and 256 (b189_constant_06.py, cutoffs converged to 2e-12): the same c appears at the same λ/κ in every family. The small-κ values 0.6271, 0.6261 and 0.6255 at the smallest κ agree within 0.002. Richardson on c(x) ≈ c∞ + a/√x gives c∞ = 0.6250, i.e. 5/8 to four digits (an estimate, not a proof). So gap = 2√(κλ) − (5/8)κ + O(κ^{3/2}/√λ). (The U(1) toy's κ/4 does not carry over to SU(3).) |
| 6 | Does the large-λ gap on a fixed graph go to the small-field box gap? | U(1) on two squares and on a 1×3 strip, exact flux basis, converged in the cutoff to 1e-11 | **Holds.** gap / √(2λμ_min) = 0.940, 0.904, 0.954, 0.978 (two squares) and 0.952, 0.905, 0.954, 0.978 (strip) at λ = 4, 16, 64, 256. On a fixed graph, weak coupling measures the box. The SU(3) version, 2√(λμ_min), is still untested directly. |
| 7 | B128 / large-field floor | grid, 2001² | **Holds**: m(δ) = (1−cos δ) + 2(1−cos δ/2), with 4 at δ = π. |
| 8 | Electric cutoffs at weak coupling | one plaquette | **Fails, and the failure is the finding.** Vacuum weight above C₂ = 40/3 is 48% at λ = 64. Electric retention cannot follow the vacuum. Kept as the reason the window wall closes. |
| 9 | Small-field seam under doubling (Link C, Gaussian version) | curl spectra | Strip: μ_min → 2 (holds at every length). Torus: μ_min = 4 sin²(π/L), which shrinks like 1/L². The small-field gap 2√(λμ_min) therefore closes like 1/L (**fails**). |
| 10 | Strong-coupling gap = cheapest closed word | girth on the five graphs | **Holds**: (4/3) × girth = 16/3 on all five graphs, matching the theta lowest level. |
| 11 | Smith reading of a transfer step | exact algebra plus strip check | Γ² = (\|tr\|−2)/(\|tr\|+2), exact. Evanescent if and only if Γ² > 0. |
| 12 | One-plaquette gap tends to 2√λ (κ = 1) | character basis | **Holds**: 0.980 of it at λ = 256, from below. |

## Not testable tonight, with the reason

| Open question | Why not tonight | What would test it |
|---|---|---|
| SU(3) two-square gap at large λ against 2√(3λ) | The exact Haar machinery stops at degree 6 per variable, so the 19-state basis is too small at large λ | A spin-network basis with SU(3) recoupling (6j) to higher cutoff, or a Gelfand–Tsetlin numerical build |
| Volume-uniform gap at weak coupling | This is the Millennium problem itself: the gap must come from outside the small-field (Gaussian) picture, and with asymptotic freedom the box must grow like e^{c/g²} | A renormalization step (Balaban-type); not a finite certificate |
| Strong-coupling volume-uniform gap in Lean | Prior art proves it (Osterwalder–Seiler; Yarotsky 2005). The formal version is a large build | The room's floors are the hypotheses; formalize Yarotsky's expansion |
| B194 bow-tie floor against arm length | Needs the card's connection-energy setup, which is not rebuilt here | Minimize E⁻ on bow ties with arm lengths 3, 6, 12 |
| Russell's dead-centre placement (UO p. 11) | Needs his chart image | Read the page-11 chart labels |
| Two Trees §9 opens (Lean for Thm 8.1; return at powers of 2; which knots never turn; why k∞ = (2cos(jπ/n)/m)²; zero set of the area) | Each is its own project; not rerun tonight | As listed in the paper's §9 |

## The room's own opens (theirs, tracked here)
- SU(3) gauge support rule: regrouping by vertex, and Peter–Weyl as a named assumption.
- GPT's double-cube 0.9867 test (unverified).
- Strip and corner close in (5, 5.25].
- Bridge from SmallSupportCycle to SmallSupportsAreCycles.
- Merges #6, #10, and #12 to #16 when green.

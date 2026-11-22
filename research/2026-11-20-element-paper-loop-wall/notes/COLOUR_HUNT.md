# Colour hunt — dicipler-pixel GitHub (41 repos, every branch) and EJ's material — 22 Nov 2026

Method: shallow clones of all 41 non-fork repos with every branch (209,811 files listed); filename search and full-text search
(Bujack, diminishing returns, Mixin, Michel-Lévy, conoscope, Schrödinger colour, ledger curve, LANL, colour selects); the hits read.
EJ's own GitHub: a user `ellyrox110` exists, but this session can only reach named repositories, so her repos are not listed here.
Her material that is on Jeromie's GitHub: `mixin-colors` (private) and `EJ-base-prime-pattern`.

## A. The answer to the non-Riemannian question was already in his own paper (Aug 2026)
- FOFT v2 (8 Aug 2026) abstract: "the trace-log ledger equips them with a non-Riemannian, diminishing-returns comparison geometry".
  §13.3 "Ledger perception geometry": S(A,B) = log det((A+B)/2) − ½ log det A − ½ log det B; local constant 1/(2√2) = 0.353553;
  accumulated/direct 1.005 → 1.192 as log κ 1 → 8; cites Sra, Proc. AMS 144, 2787 (2016) [the √S-is-a-metric source] and Bujack PNAS 2022.
  Grade [V]+[C], gate COLOR-LEDGER-01. Source: operator-first, branch research/elemental-foundations, sources/text/foft_v2.txt.
- So the word "non-Riemannian" belongs to the LEDGER comparison, in his own words, since August.

## B. Colour Selects the Leader v1.2 (2 Nov 2026, Zenodo 10.5281/zenodo.23876186) — his main colour paper; full read in votkp-lean
   branch claude/matter-disk, matter-disk/corpus-notes/colour_v12.md
- §2 Schrödinger split: (1/h)Σ a_i dx_i²/x_i = (d log h)² + Σ dp_i²/p_i; sphere of radius 2; brightness = how much, colour = which way.
- §3 waveplate between polarizers: crossed port E⁻ = sin²(δ/2), parallel E⁺ = cos²(δ/2): the two books of one unit eigenvalue.
- §4 Mixin as polarization (a proposal): primaries at 0/45/90/135°; secondaries DOP 1/√2; the label forgets the amount; Theorem 1
  surviving matches (Lean VOTKP.Colour).
- §5 LOS ALAMOS — CORRECTED in v1.2: logarithm beats the ledger curve on GREY (+0.000805 nats/response, CI [+0.00027,+0.00136]);
  ledger has a small green–pink advantage (−0.000401); blue–orange whole-triad interval spans zero.
  "These results supersede the earlier claim that ledger wins all three datasets." (mixin-colors deep-dive and the 24 Oct review
  still carry the older, superseded ledger-wins numbers.)
- §8 the ledger curve is log cosh(½ log(I/J)) and its derivative ½ tanh(x/2) is the balance map of §12.
- §12 eq 16 balance map (m−p)/(m+p) = tanh(½ log(m/p)) = Smith reflection (z−1)/(z+1) = two-book balance = the PEEL Γ.
  => my "S = −½ ln(1−Γ²)" today is this same identity rewritten (cosh² = 1/(1−tanh²)); not new.

## C. Colour ↔ peel bridge already built (votkp-lean, branch claude/votkp-research-20261110, research/2026-11-10/round4/colour_peel_01–03)
- COLOUR-PEEL-01: for two channels, share balance = Smith point Γ; Hilbert projective distance = peel distance |ln z − ln z'|;
  Schrödinger chromatic angle φ has cos φ = Γ = tanh(τ/2). Identities to 1e-11..1e-16 on 20,000 pairs.
  Prediction checked: a Schrödinger stretch needs c·cosh(τ/2)/cosh(τ'/2) > 1 and only happens while carried TOWARD white:
  22 stretches, all toward white, formula right on 20,000/20,000.
- COLOUR-PEEL-03: the paper's 955 stretches come from the Exner weights: unit weights give 0 of 20,000 (three seeds);
  Exner gives 861–936; weights 10,10,1 give 220.
- Reading for the element paper: at the peel wall Γ² = ½, cos φ = 1/√2, φ = 45°: the wall is the 45° chromatic angle on the
  two-channel Schrödinger circle. (Arithmetic from C; not yet written in any paper.)

## D. Element colour data already on GitHub
- operator-first, branch research/elemental-foundations, tools/compound-eye/projects/elemental_peel/FINDINGS.md (8 Sep 2026):
  Au/Ag/Cu/Pt reflectance from Johnson–Christy and Rakić: R(450/550/650) Au 0.408/0.792/0.957, Ag 0.980/0.983/0.990,
  Cu 0.538/0.624/0.935, Pt 0.588/0.641/0.678; Cu/Ag/Au shell jump after 11 removals, Pt after 10; isospectral control
  (levels fixed at ±1, optical strength 0→1, conductance 0→0.1479 G₀, metric 1/4); COLOR-PROJECTOR-CHECK-01 all pass.
- votkp-lean READ_B4 (Full Table package, 11 Nov): a preregistered rule "observed visible ground line iff IE1 < 6.82 eV" on
  65 test elements (Z 14–118): accuracy 0.831 vs majority 0.569, AUC 0.946; 11 errors (Ti, Mn, Fe, Mo, Tc, Ru, Hf, Ta, W, Ir, Tl);
  Hf and Ti within 0.01 eV of the cut. Gold metamer: match before gold (ΔE 9e-14), ΔE2000 8.27 after one gold reflection.
  Ridge check: the Kr-like ridge stays positive at high charge, so "the selected colour-onset coincidence fails to generalize".
  The package files themselves (colour_delivery/, master.xlsx) are NOT on GitHub — only this read record.

## E. EJ's colour wheel (EJ-base-prime-pattern, 03-docs/COLOUR_WHEEL.md, colour_z10.py)
- Theorem: orbits of (Z/W)× on Z/W are the divisor classes. At W=10: primaries {1,3,7,9} (units, primitive 10th roots),
  secondaries {2,4,6,8} = doubles of the primaries, grey {5} = kernel of doubling, base {0}; Φ10(x) = Φ5(−x).
- A colour wheel of this kind is viable iff W = 2p, p an odd prime (checked W = 6..30): 2, 4, 6, 10, 12 … primaries.
- Complements = negation x → 10 − x; the only self-complementary colours are 0 and 5.

## F. Smaller finds
- three-body-lean 369: the Mixin/polarizer angles 22.5k° have digit sum ≡ 0 mod 9 only in degrees (gradians, turns break it): a unit artefact.
- votkp-lean branch theta-colour-formalization: VOTKP/Colour.lean (surviving matches, retained amount, bounded metamers) + docs.
- iqgt-grassmannian-lean paper/checks/polariton_check.py; mixer v6–v8 colour eyes.
- maxwell-lean results/swarm/art634/Art634Stokes.lean (Stokes, in the Maxwell swarm).

## What this changes for "What the Peel Keeps"
1. If the ledger remark goes in, it must carry the v1.2 CORRECTED Los Alamos result (log wins grey), cite FOFT v2 §13.3 as the
   origin, Colour Selects the Leader v1.2 §§8, 12 for the balance-map identity, and Sra 2016 for √S being a metric.
2. COLOUR-PEEL-01 is the clean, checked bridge: the peel Γ is the two-channel colour share balance; Hilbert distance is the peel
   distance; the wall sits at chromatic angle 45°.
3. The IE1 < 6.82 eV visible-ground-line classifier and the Au/Ag/Cu/Pt reflectance are element-colour results already in hand.

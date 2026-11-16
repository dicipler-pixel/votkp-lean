# W — Watcher report, phase 1 (reports L1, L2, L3)

Watcher pass, 16 Nov 2026. Jeromie Beasley. AI-assisted. Read-only on every file of the hands; my own scripts are in `/home/claude/balls/breakdown/scratch/watcher/`. L4 and P had not landed when this was written (only scratch for L4 existed); they are not audited here.

## 0. Verdict in plain words

L1, L2 and L3 are sound. Every one of the 90-odd file:line quotes I opened matched the file text (a few line numbers are off by one or two, listed in section 5). Every numerical claim I re-ran with my own scripts reproduced. No grade was upgraded. There is no LaTeX, no hype, no "after the big bang", no dark energy or dark matter in the three reports.

One real defect in the Flock code is confirmed from first principles (the arm–arm face signs). Three kill lines are weaker than their text says. The most important thing for the next gate is not in the reports at all: the Flock's long-time exploration numbers (shares, order parameter r) are not converged in the step size and the order parameter barely exceeds a random-phase baseline. The page and film must not quote those as results yet.

---

## 1. Findings, ranked

### F1 (HIGH, confirmed). Arm–arm face signs contradict the centre–arm face signs (`fl_math_v1.js` lines 50–51)

**First-principles derivation (mine, not copied from L1 or L2).**
1. Take only the Fresnel rule from `step_matching` and `reciprocity`: light going from side 1 to side 2 returns r = (Y₁ − Y₂)/(Y₁ + Y₂), light going from side 2 to side 1 returns −r.
2. Fix the side convention from the code's own centre–arm link (line 47): light leaving the centre cell outward returns +tanh(r/2). So side 1 is the centre cell (Y_centre/Y_arm = z).
3. The scatterer (lines 81–82) returns forward-running light with +ρ: `bin[k-1] = rho*Uf + tau*bR`.
4. Then on the arm–arm link a → b: the first face (light going from ball a's side into the centre cell) must return −Γ_a. The last face (light leaving the centre cell toward b) must return +Γ_b.
5. The code has +Γ_a at line 50 and −Γ_b at line 51. Both are reversed.
6. The opposite convention does not rescue the code: if "arm side = side 1", then the arm–arm marks are right and all the centre–arm marks (line 47) are wrong. Either way the same face carries two opposite signs on its two links.

**Run.** `scratch/watcher/w10_signs.js` reads every face mark in N = 7 worlds (z = 3,5,7 and z = 7,9,13) and compares it with the Fresnel expectation from steps 1–4. Result: 60 faces checked; 12 centre–arm faces agree; all 48 arm–arm faces differ in sign. Example, z = 7,9,13, link (1,2): code marks +0.750000, gap +0.750000, −0.800000; Fresnel expects −0.750000 and +0.800000.

**Does it change the run? Yes.** `w11_signrun.js` and `w13_l2num.js` (scratch copy `fl_math_signflip_copy.js`, which differs from the original in exactly the two sign lines, checked by `diff`). N = 3, z = 7,9,11, kick B, torque 0 (linear run), light in B at t = 3: as built 0.03254, reversed 0.42116 (L1's numbers reproduced). N = 3, z = 3,5,7, kick A, t = 40: as built 0.1445 0.0135 0.0107, reversed 0.4314 0.1298 0.0515 (L2's numbers reproduced). Books stay 1.0000000000 in both, so no books check can see this.

**Why no K line sees it.** K3 and K4 measure squared first-pass fractions, so a sign cannot show. K2 is satisfied by any real rotation.

**Both L1 (section 3A) and L2 (section 4 item 1) have this right.** One wording issue: L1's summary (line 17) says the signs "are not fixed by any source". Section 3A says the opposite (the centre–arm convention fixes them). The accurate statement is: the absolute convention is a reading (PLAN:54, CLAIMS V4 is a Proposal), but consistency between the two link kinds is not optional.

**Smallest repair.** Lines 50–51: `rho:-Math.tanh(balls[a].r/2)` and `rho:Math.tanh(balls[b].r/2)`; correct the comment at line 51; re-run `fl_check_01.js` and regenerate the exploration table. Or keep the signs and state, in the header, a different convention for both link kinds. The call is the owner's. Until he decides, no arm–arm run number (shares, r, light in B and C at late times) goes onto the page or the film. L1's untested sentence "Reason: the sign sets whether the echo ... in step or out of step" is an explanation without a check; mark it "untested".

**Related, open (L1 item B).** The gap mark has the same kind of freedom: film theory gives r = −i·tanh(κδ) from both sides; the code uses real +tanh from one side. A "gap negated" run changes light in B at t = 10 from 0.02311 to 0.37572 (L1; reproduced in `L1/l1_sign_check_02.out`). Moduli are fixed by K4; phase is a model choice and should say so on the page.

### F2 (HIGH for the next gate). The Flock's exploration numbers are not converged and do not yet show synchrony

Not an error in L1–L3, but they point at it (L2 section 6 item 1, L3 section 3.2) and the page spine part 7 ("Swinging together?") will rest on it. Evidence: `scratch/watcher/w02.out`.

- **Step size.** N = 3, kick A, defaults. Light in A at t = 50: h = 0.01 gives 0.247, h = 0.005 gives 0.208, 0.0025 gives 0.210, 0.00125 gives 0.208. r at t = 50: 0.653, 0.462, 0.461, 0.463. At t = 100 light in A: 0.394, 0.361, 0.359, 0.344, and r: 0.870, 0.862, 0.845, 0.828. Even the linear part alone (torque 0) drifts at t = 100 (light in B 0.0850, 0.1001, 0.1010, 0.1098). K7 only compares t = 6.
- **The order parameter against a baseline.** For t in [200, 300] (sampled every 0.1), N = 3 clocks z: r weighted 0.828; the same weights with random phases give 0.762. N = 4 z: 0.790 against 0.634. N = 7 z: 0.616 against 0.538. N = 3 equal clocks: 0.621 against 0.665 (below). The weights are concentrated on ball A, so r is mostly a measure of how much light sits in A. Measured phase rates for N = 3 z are 2.644, 1.764, 0.748 against own rates 2.000, 0.667, 0.400: they are not locked.
- **Smallest repair.** Quote exploration numbers only where they are converged (t ≤ 20 passes: A at t = 20 is 0.2387, 0.2336, 0.2343, 0.2344). For r, state the random-phase baseline next to it. Do not use the words "swinging together" or "synchronised" for N = 3, 4, 7 on the strength of this table. Say what the run shows: light spreads into the gap and returns; r exceeds the baseline by 0.04 to 0.15 for clocks z and is not above it for equal clocks.

### F3 (MEDIUM). K6 can only fail from 1.5e-8, and its own kill line (1e-9) is already exceeded

`fl_check_01.js` K6: "Kill: any ball field turns more than 1e-9 by t = 50", measured with `acos`. The smallest angle `acos` can report is acos(1 − 1.1e-16) = 1.49e-8, so the line reads exactly 0 or at least 1.5e-8 and can never see 1e-9 to 1e-8. With a cross-product measure (`w01.out`): largest turn at N = 7, t = 50 is 2.54e-9, above the 1e-9 line, with rest residual 8.07e-10. So the stated kill line, properly measured, would be killed. This is a mismatch between the stated line and the instrument, not a physics problem (drift is about three times the converged residual).
Smallest repair: measure with |a × b|/(|a||b|) and set the kill at 1e-8, saying why (rest residual 8e-10 over t = 50).
Related: a ball tipped by 1e-3 rad under the static push does not relax: 1.0e-3 grows to 1.4e-3 by t = 200 at h = 0.005, and the growth scales with h (1.96e-3, 1.40e-3, 1.18e-3 for h = 0.01, 0.005, 0.0025 at t = 200). That is integrator error, not instability, but "rest is exactly still" (header line 15) should read "still to the rest residual".

### F4 (MEDIUM). K7 tolerance (0.02) is 20 percent of the value it guards

K7 compares light in B at t = 6: 0.10301, 0.10176, 0.10206 (h = 0.01, 0.005, 0.0025). The changes are −0.00125 then +0.00030; the sign change means it is not "halves with h", the stated expectation. A kill line of 0.02 would pass a 20 percent error. Smallest repair: 2e-3, and check at t = 20 too.

### F5 (MEDIUM). L3's speed-limit check cannot catch an error smaller than about a factor of 7

L3 section 2.10: ratio τ̇²/(4gS) at most 0.021 to 0.026, "far from saturated". L3 says so itself. A bound that is reached at 0.02 passes even if τ̇ is wrong by a factor of 6. The theorem has an equality case (WPMK Theorem 8). My test, `w14_equality.py`: with Ṗ = [P,[P,F]], F = E W E†, W = −(C(I−C))⁻¹, the ratio is 1.000000000000; the formula for τ̇ matches a finite difference of log det(I − C) − log det C (433.01652319 against 433.01652950); a random driven direction gives 0.0100. In 500 random driven families (my `w12_numeric.py`, N10) the largest ratio is 0.4562, below 1.
Smallest repair: add the equality direction to L3's script as the line that can fail (must reach 1 to 1e-9 with MM's `tauDot`, `seaSpeed`, `ballCensus`).

### F6 (LOW). Citation drift (quotes were exact; the numbers moved)

| Report | Cited | Actual |
|---|---|---|
| L1 (2.3, 2.4) | `fl_math_v1.js:42` for `MMr.linkDistance`, `su2` | line 41 (line 42 is the comment) |
| L3 (2.3) | TB README line 9 for "loop ... 0.7110545751" | line 10 |
| L3 (2.5, 3.2) | TB README line 10 "rest: nothing held on any face" | line 11 |
| L3 (2.4) | TB README line 15 "Model choices" | line 16 |
| L3 (2.11) | `CommonClock.lean:62` `rescale_same_eigenvectors`, `:67` `rescale_scales_gaps` | `:60` and `:66` (docstring "Corollary P4.3" at `:59`) |
| L2 (2.1) | "All seventeen named theorems" | the table has 18 rows |
| L2 (2.2) | card claims quoted with spaces between sentence parts | the JSON has them joined with no space ("R₂ sin²θ₂L = ..."); the content is the same |

Smallest repair: edit the numbers. None changes a conclusion.

### F7 (LOW). Grade and wording notes

- L3 2.9: "Γ bridge LEAN · tanh_half_log_odds". The Lean statement (`Admissible.lean:177`) is tanh(½ log(s/(1 − s))) = 2s − 1, which is −Γ for s = ν. Γ = tanh(τ/2) with τ = log((1 − ν)/ν) needs tanh odd. One line; state it, keep the grade LEAN with that note.
- L1 2.19: Proposition 1 graded PROVED. The paper's own status line (`votkp_vacuum_disk_v1.md:67`) says (a)–(c) elementary, (d) a new reading, "the racket interpretation is ours". The page should carry that line next to the grade.
- L2 and the card for B30: the card grade is "theorem" and the ledger scope is "conditional scalar refraction/turning algebra". On the page use "CARD · B30 (theorem)" plus the scope, not "LEAN".
- L2 omits that the page-level self-test file `lh_selftest_v1.out` reads "80 of 82 lines hold" with two K15 lines KILLED (2.35e-8, 1.91e-9). `LEDGER_build_v2.md:45–50` explains the cause (the test, 2×10⁵ summed steps) and `lh_k15_rerun.out` holds. L2 only says "K15 CHECKED after re-run". Add the kill and its cause to L2 section 6 item 14.
- Possessives that read third-person: L1 lines 17 ("his two repositories", "his film theorem"), 60, 135, 302; L3 lines 147, 180 ("his papers"). The brief says to speak of the work directly. Smallest repair: "the two repositories", "the film theorem", "the papers". Not hype and not wrong.
- Not found anywhere in L1–L3: LaTeX, "big bang", dark energy, dark matter, "your idea", hype words.

---

## 2. Spot-checks of cited quotes (exact text compared with the real files)

All matched unless listed in F6.

**L1 (24 checked):** `Edition10.lean` 47, 59, 69, 77, 81, 86, 102, 108, 183, 35 and docstring 44–46; `Smith.lean` 28, 31, 42, 61–64, 65, 72, 89, 134, 208; `Film.lean` 29, 42, 53, 61, 86–90, 116, 124; `PingPong7.lean` 3, 77, 87; `Directed.lean` 48, 77; `ThinFilm.lean` 105; `PLAN` 17, 54, 58, 82, 83, 84, 310, 323; `REQUIREMENTS_v1.md` 76; `LIMITATIONS.md` 18; `CLAIMS.md` 31–34; vacuum disk paper 45–55 and 67; `fl_math_v1.js` 6, 47, 50, 51, 81, 82; `fl_check_01.out` 1–12 (also rerun: identical to the stored file). The "no sorry, no native_decide" statement: I grepped all five files plus the Two Trees files; every "sorry" is in a "no sorry" header.

**L2 (30 checked):** `PeelTrees.lean` 163, 164, 166, 258, 284, 285, 294, 295, 301, 302; `PeelTrees2.lean` 357, 365; `PeelTrees4.lean` 35 and 101–103; `PingPong7.lean` 64, 77, 87, 97, 179; `HypersurfaceSquareLineage.lean` 12–15, 40, 148–155, 155; `UPGDiracRefraction.lean` 120, 128, 137; `RadiationPressure.lean` 82–86; `BallJoins.lean` 59, 74, 121 (header "No sorry"); `PLAN` 70, 112, 122, 123, 125, 126, 136, 320; `coverage.json` card ids at 842, 1147, 2987, 5297, 5651 and the B30 and B39 text; `lh_math_v1.js` 28, 35, 41, 46, 50, 73, 98, 105, 107, 163, 170, 173, 205, 212, 247; `fl_layer_v1.js:140`; `fl/README.md` lines 25–26. "Not found" claims checked: grep of `coverage.json` for "2e-11" and "22.5210" finds nothing, so the B30 witness numbers are indeed not on disk. `LH.selftest()` run from node: 24 of 24 lines within tolerance.

**L3 (32 checked):** `mm_math_v1.js` 3–5, 12, 17, 38, 40, 80, 88, 124, 126, 140, 145–147, 193, 195; `tb_math_v1.js` 5, 6, 7, 14, 28; `fl_math_v1.js` 37, 39, 57, 58, 60, 88, 102, 103; `gap_clock_check_01.out` 1, 4–7, 10, 18–32; `NN_v15.txt` 457, 458, 517–518, 544–545; `SelfCommutator.lean` 112, 137–141, 182, 257; `Admissible.lean:177`; `Holonomy.lean:234`; IQGT `Rebuild.lean` 31, 112, 320 and `Basic.lean` 30, 67, 105, 107; `ProjectorBlocks.lean` 68, 75; `Memory.lean` 49, 56, 65; `WPMK_v1_1.txt` 171, 180, 337, 346, 362–363, 381; `COLOUR_v1_2.txt` 637, 2201; `DIRAC_v3_1.clean.md` 16, 68, 755, 757, 761, 3535; `REQUIREMENTS_v1.md` 50, 75, 79; `fl_layer_v1.js:142`.

---

## 3. Numerical claims re-run with my own scripts

Method independent of the lineage scripts in every case. All in `scratch/watcher/` (`w12_numeric.py`, `w14_equality.py`, `w15_stretch.py`, `w10_signs.js`, `w11_signrun.js`, `w13_l2num.js`).

| Claim | Report | My method | Result |
|---|---|---|---|
| Gap film: \|t\|² = sin²φ/(sinh²κd + sin²φ); at φ = π/2, \|t\| = sech κd, r = −i·tanh κd | L1 §2.16 | slab by 2×2 transfer matrix (L1 used three-region matching), 3000 random cases | worst 1.0e-15; φ = π/2 worst 9.7e-15 |
| K4 first-pass numbers 0.2363040123, 0.0689062500, 0.0194005102; gap passes 1/g² | L1 §2.17, K4 | closed form | all match; sech²(arccosh g) = 1/g² to 10 digits |
| Echoes: back 0.6896551724 = tanh(ra/2 + δ − rb/2); on 0.7241379310 = sech; no gap −0.125 | L1 §2.12, §2.15 | zero-phase transfer-matrix product (L1 used time-domain) | match to 10 digits |
| δ = arccosh g is the least distance between the two face planes | L2 G4 | Nelder–Mead on the hyperboloid, 12 starts, formula for g not used inside the search | 0.168236118, 0.972955075, 1.434959913, 0.738997944 equal arccosh g; worst diff 4.7e-13 |
| Thomas turn = triangle area = 2·arctan(Γ_aΓ_b); z = 5: 65/97, 72/97, 47.925° | L2 G7 | polar decomposition of the 4×4 product; area as π minus three angles | match to 10 digits for (5,5), (7,7), (3,5), (5,7), (3,7); cos, sin = 0.670103092784, 0.742268041237 |
| Square at z = 5: cos φ = −527/625; wall z = 3 + 2√2 gives Γ² = ½, g = 1 | L2 G5, G8 | trace of the 4×4 commutator | −0.8432 both; Γ² = 0.500000000000 |
| Refraction 50° from R = 1 into R = 4 leaves at 22.5210° | L2 G10 | arcsin(sin 50°/2) | 22.5210° |
| Geodesic meets face a, then face b, 0 < s₁ < s₂ < d on 2209 pairs; shortest stretch 0.0226; stretch − δ ≥ 0.1284 | L2 §5.2 | bisection on the hyperboloid, no closed form | 0 violations; 0.0226; 0.1284 |
| Connection energy: (1/8)‖[H,H*]‖² = Σ_edges w‖D_i − U_jD_jU_j†‖² | L3 §2.5 | random Hermitian traceless blocks, random SU(2), random graphs on 7 vertices, random weights | worst relative 8.2e-16 |
| The light matrix (Hermitian hop) has zero self-commutator; K = D + i·hop gives the weighted identity with w = c² | L3 §2.5 | 3 balls, c = 0.4, 0.3, 0.2 | 0.0 and 4.005813272929 on both sides |
| Rest connection energy with clocks z, 3 balls: 2.204444444 | L3 §3.2 | by hand: 2·Σ(|dᵢ| − |dⱼ|)² with |d| = 1, 1/3, 1/5 | 2.204444444; and ‖Dᵢ − UDⱼU†‖² ≥ 2(|dᵢ| − |dⱼ|)² over 20000 random cases (minimum +1.3e-4) |
| 2·arctan(ΓΓ) = 0.6435011088 and 0.7110545751 | L3 §2.3 | direct | match |
| τ̇² ≤ 4gS | L3 §2.10 | random projector families, dimension 6, rank 2 or 3 | 0.456 maximum; equality direction 1.000000000000 (see F5) |
| U(d·σ)U† = (R d)·σ, not R transposed | L3 §2.2 | `w01_frames_rest.js` | 7.2e-15 against 1.28 for the transpose |
| K1–K7 outputs | L1, L3 | reran `fl_check_01.js` | identical to the stored output, "all kill lines hold" |
| 3-ball Three Balls numbers (4.48386946121, 88.5631038472, 6.16547097585, ν = 0 at rest, τ = Infinity) | L3 §2.5, §2.6, §4 | reran `l3_run_01.js` | match |
| Gap element continuous through the wall | L1, L2 | `w01.out` (3): first-pass T 0.250060671, 0.250000061, 0.250000000, 0.249999818 across g = 1; δ = 7e-4 at z + 1e-6 | continuous |

---

## 4. Do the kill lines really fail?

| Check | Can it fail? | Note |
|---|---|---|
| K1 (nothing in B before d − 2h) | Yes | any early light trips it |
| K2 (books 1e-10) | Yes, but it cannot see a sign or a phase | F1 |
| K3, K4 (first-pass fractions vs formula, 1e-12) | Yes, for moduli; blind to signs | F1 |
| K5 (clock rates) | Yes | measured from the phase, not from the setting |
| K6 (rest, 1e-9) | Not below 1.5e-8, and the stated line is already exceeded | F3 |
| K7 (step size, 0.02) | Only for errors above 20 percent | F4 |
| L1 T1–T5 | Yes; two routes differ in method | reproduced independently |
| L1 T2c, T2d | They are identities; a failure would mean algebra slip | fine, labelled as identities |
| L2 G1–G12 | Yes; each builds the number from the matrix or a search, not from the formula | reproduced |
| L3 nnceCheck at the three-ball rest state | 0 = 0, disclosed by L3 | the random-d rows are the test |
| L3 control, one U replaced by I | Breaks it by 1.4 to 2.0 percent only | passes the purpose, weak margin |
| L3 speed limit | Cannot fail below factor 7 | F5 |

No lineage check was found whose kill line is written after the run or cannot in principle fail, except as listed.

---

## 5. Grades: any upgrade?

None found. Cases that are close and were read against the source: L1 2.12–2.15 (LEAN only where a named theorem exists; the combined echo-circle statement is stated as not proved, `Film.lean:88–90`); L1 2.16 table (|t|² formula CHECKED, not LEAN; φ = π/2, κ = 1 MODEL CHOICE; gap layer HYPOTHESIS); L2 H table (every "what stays hypothesis" entry unchanged); L2 Thomas (LEAN for 5, 7 and equal integer z; CHECKED for unequal steps, as PLAN:123); L3 2.3 (unequal-step Thomas CHECKED, not LEAN); L3 2.10 (LEAN for one mode only, PROVED in the papers); L3 2.11 (header sentence graded READING). The only grade notes are in F7.

---

## 6. For the next gate (G2, the breakdown page)

1. Do not show any arm–arm late-time run number until F1 is decided; show K3, K4 (signs cannot matter there).
2. State in the page that the gap phase and sign are a model choice (L1 item B), that the gap and the in-cell stretch are two different lengths (L1 D, L2 item 2), and that z against cosh r as the clock ratio is open (L2 §5.3).
3. Part 7 ("Swinging together?") must carry the F2 baseline and the h-convergence limit.
4. K6 and K7 lines should be quoted with their repaired tolerances or not quoted.
5. L4 (new maths, prior art) and P (pipeline proof) are still to be audited when they land.

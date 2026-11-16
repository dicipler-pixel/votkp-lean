# W — Watcher report, phase 2 (breakdown page, L4, P)

Watcher pass, 16 Nov 2026. Jeromie Beasley. AI-assisted. Read-only on the page and on every file of the hands. My scripts are in `/home/claude/balls/breakdown/scratch/watcher2/` (`w2_signs_v2.js`, `w2_k7.js`, `w2_root.py`, `w2_sweep.py`, each with its `SCRIPT` line and kill line). Phase 1 is in `W_watch_phase1.md`.

## 0. Verdict in plain words

The page is mostly sound. Every number I traced to a report or reran matched, except those listed below. No grade is upgraded anywhere. There is no LaTeX, no "after the big bang", no dark energy or dark matter, and no "his/him" on the page. L4 and P hold up: I reran seven of the L4 scripts (outputs identical to the stored files, apart from the `time` trailer) and recounted the L4 sweep and the P pipeline numbers from the raw files.

The page has two real problems and several wording or scope problems.

1. The pages the film will be captured from (the Mixer and White pages, and P's proof clip) still contain the v1 arm–arm face signs. The page says v2 is built, but v2 exists only as `fl_math_v2.js` and `fl_check_02.js`. (F1)
2. L4's headline count "1,920 ball pairs with different free rates" is wrong. The correct figure is 1,728. The conclusion (none locked) is unchanged. The page repeats the wrong count. (F3)

Items already known from phase 1 (sign defect, step-size convergence, K6 and K7 weakness) are carried correctly in the page except where listed.

---

## 1. Findings, ranked

### F1 (HIGH). The page says the sign repair is built, but every shipped page and the film capture source still carry the v1 signs

**Evidence.**
- `grep -c armSign` on `Flock_of_Balls_on_the_Field_Mixer_v1_20261116.html` and on the `White` page: 0 in both. Mixer page lines 1157–1158 hold the v1 marks (`rho:Math.tanh(balls[a].r/2)`, then `rho:-Math.tanh(balls[b].r/2)`).
- `fl_build_v1.py` reads `fl_math_v1.js` only.
- P's proof clip was captured from that Mixer page (P section b). Its scene "kick the centre ball, light sets out across the gaps" uses links that include arm–arm links.
- My run `w2_signs_v2.js` reproduces the page's 4.1 numbers from the two code versions: N = 3, z = 7,9,11, kick B, torque 0, light in B at t = 3: v1 and v2 `asBuiltV1` both 0.0325; v2 default 0.4212. N = 3, z = 3,5,7, kick B, t = 2: 0.1136 against 0.3250. Books 1.0000000000 in all.

**Consequence.** Film scenes 4, 5 and 6 of the page's section 8 ("a pulse on a link", "instant against travelling", "the flock of clocks") show the v1 convention unless the page is rebuilt.

**Smallest repair.**
- Page 4.1 or section 8: one sentence, "the shipped pages still use the v1 signs; the film scenes that cross an arm–arm link wait for the owner's call on the sign".
- Or, once the owner decides, run `fl_build_v1.py` against `fl_math_v2.js` as `fl_build_v2.py` (a new filename, nothing overwritten) and recapture.
- Until then, film shots should show centre–arm links (K3) or the first pass only (K4). Those do not depend on the sign.

### F2 (MEDIUM). Section 5 results mix v2 numbers into a table that does not say which version

**Evidence.** The page's K2 row (1.1e-12, 9.9e-13) and K7 row (0.07100, 0.07114, 0.07098) are `fl_check_02.out` (v2). The stored `fl_check_01.out` (v1, "as built", which I reran and which is identical) reads K2 1.0e-12 and 8.3e-13, and K7 0.10301, 0.10176, 0.10206. The two outputs differ in exactly those lines and in the exploration table. Section 4.1 calls v1 "as built", so a reader will take the section 5 numbers as v1.

Also: the page's section 3 says books "≤ 1.2e-12". The largest K2 value in either output is 1.1e-12 (to t = 200). L4's wider sweep reaches 1.4e-11 (with loss and sinks, t = 400). The figure 1.2e-12 has no source line.

**Smallest repair.** Head the table "K1–K7, Flock v2 (v1 numbers differ only in K2 and K7: 1.0e-12, 8.3e-13; 0.10301, 0.10176, 0.10206; all kill lines hold in both)". Change "≤ 1.2e-12" to "≤ 1.1e-12 to t = 200".

### F3 (MEDIUM). "1,920 ball pairs with different free rates" is 1,728

**Evidence.** `w2_sweep.py` over `sweep2.jsonl`: 384 cells, 192 z-clock cells (64 each for N = 3, 4, 7). All pairs in those cells: 3·64 + 6·64 + 21·64 = 1,920. Pairs whose free rates differ by more than 0.02: 1,728. The missing 192 are the three mirror pairs (+I and −I, and so on) in each of the 64 N = 7 cells, which share one z and so one free rate. Pairs agreeing within 0.02 in both windows: 0 (my recount). The smallest larger-window gap is 0.0208, only just above the 0.02 line.

L4 section 2.3 and `l4_zagree_02.out` both call 1,920 "unequal-free-rate". Page section 4.2 repeats it. L4's film idea 1 ("pairs locked: 0 of 1920") repeats it too.

**Related scope points on the same sentence.**
- The page says the hunt covered "torque reversed and up to 10". The 384 cells hold torque −1, 0 and 1 only (counts 24, 108, 252). Torque 3 and 10 are 12 separate runs (L4 section 2.5).
- Of the 1,728 pairs, 486 are in torque-0 cells, where the readout is clean, and 1,134 are in torque-1 cells, where the page itself says `FL.clockPhase` mismeasures. The page says "a frame-free spectral check was used instead". L4 added the spectral check as a second eye for shared lines. The rate count still uses `clockPhase` in the torque-on cells.
- "27 percent of pairs share lines" is 59 of 216 heavy unequal-rate peak comparisons, not of all pairs.

**Smallest repair.** "Of 1,728 pairs with different free rates (486 of them with the torque off, where the readout is clean) none had rates agreeing within 0.02 in both windows; the closest missed by 0.0008." Torque 3 and 10: "tried separately". "27 percent of the 216 heavy pairs compared".

### F4 (MEDIUM). Heading "The flock does not lock" is stronger than the result

L4 section 2.6 says what it does not claim: kicks in other balls (one variant), a driven flock, N above 7, single-mode selection. The page lists the last three but not the kicks. The heading and the README both say it flatly. Grade CHECKED fits the count, not the sentence.

**Smallest repair.** Heading "4.2 No locking found in the runs so far (CHECKED)". Add "kicks in balls other than A" to the not-scanned list. Spine step 7 "Swinging together" should read "Swinging together? not found so far".

### F5 (MEDIUM). Two numbers in 2.4 are attached to the wrong worlds

- "CHECKED on 3 and 7 balls: both sides 4.48386946121." L3's table: 4.48386946121 is the 3-ball random-d case. The 7-ball initial radial case is 88.5631038472. One number cannot serve both. Also note both sides are zero at the three-ball rest state, which L3 discloses, so the random-d rows are the real test.
- "0.7110545751 for the three-ball case" and film scene 3 "Turn = area = 0.7110545751". L3 section 2.3: that value belongs to the surprise-ball steps (ln 3, 1.9125468038), not to z = 3, 5, which gives 0.6435011088 (36.87°, the value the page's table row gives). The page shows two different "triangle turn" numbers without saying why.

**Smallest repair.** "4.48386946121 (3 balls, random fields) and 88.5631038472 (7 balls)". "0.7110545751 (steps ln 3 and 1.9125)", or use 0.6435011088 for z = 3, 5 in film scene 3.

### F6 (MEDIUM). Convergence statement in section 7 contradicts the page's own 4.2

Section 7: "first order in step size (good to about 1e-3 at h = 0.005)". L4 measured that at t ≤ 6. `w02.out` (phase 1) for N = 3, kick A, v1: light in B at t = 20 is 0.06067 at h = 0.005 and 0.05931 at h = 0.00125 (2 percent). Light in A at t = 50: 0.247, 0.208, 0.210 for h = 0.01, 0.005, 0.0025.

**Smallest repair.** "good to about 1e-3 at h = 0.005 for t up to 6, about 1e-2 at t = 20, and not converged by t = 50".

### F7 (MEDIUM). Film pipeline sentence overstates what was tested, and omits the known crash

Page section 8: frames "identical on repeat". P: the repeat test was one 1-second spec (30 frames); "determinism of the whole 12.8 s run or across machines" is stated as not tested. I confirmed 384 unique frame hashes in `page_p_clock.csv`.

Also omitted: the first full run crashed at frame 294 (host_tau 10.0). I confirmed in the page source (Mixer page line 414–415) that `q = Math.min(3.999999, f*4)` has no lower clamp. `page_patched_copy.html` differs by exactly that one line. Any film shot past τ = 10 needs this repair.

All P arithmetic checked: 384 frames = 12.8 s; 0.806 s per frame; 24.2 min of work per film minute; 8.2 min of machine time for 15 s; 5 minutes about 2.7 h; ffprobe h264 1920×1080 30 fps, 450 frames, 15.000 s; books maximum 4.9e-14 (recomputed from the csv: 4.929e-14). One slip in P: the tail after the last sentence is 1.58 s (wav 13.785 s), not 1.2 s. P's DOI placeholder is correctly left unset. I did not view the frame sheets (not asked).

**Smallest repair.** "identical on repeat for a one-second test; the full run is not yet repeated". Add: "the Mixer page needs a one-line clamp at `partialSquare` before shots past τ = 10".

### F8 (MEDIUM). v1 signs are relabelled "MODEL CHOICE" (4.1 and section 6)

Phase 1 F1 derived that the v1 arm–arm signs contradict the code's own centre–arm convention. A defect, not a free choice. Only the global convention (which side is side 1) is a reading (PLAN:54), and flipping it breaks the centre–arm faces instead. The header of `fl_math_v2.js` and the page call v1 "a MODEL CHOICE". That is a softer grade than the evidence supports, though the page does keep 4.1 under OPEN.

**Smallest repair.** In section 6: "Arm–arm face signs: v1 is inconsistent with the centre–arm faces (OPEN); v2 is consistent. The owner decides." Keep MODEL CHOICE only for "which side carries +Γ".

### F9 (MEDIUM). Missing: the gap phase and sign are a model choice

Phase 1 gate item 2 asked for it. The page has no sentence on it. L1 item B (reproduced, `l1_sign_check_02.out` line 10): "gap negated" changes light in B at t = 10 from 0.02311 to 0.37572. The page's gap row and hypothesis row speak of amplitude sech(κδ) only.

**Smallest repair.** Add to the section 6 gap row: "the film theorem gives r = −i·tanh(κδ) at φ = π/2; the Flock uses +tanh(κδ) as a real number. Modulus fixed by K4, phase a model choice that changes the run."

Also in 4.1, the two example worlds are different (z = 7,9,11 at t = 3; z = 3,5,7 at t = 2) and are unnamed. Name them.

### F10 (MEDIUM). Voice and form against the standing rules

- Second person where the work is spoken of in third: spine step 7 "Your picture", 4.1 "The choice between them is yours", section 6 "Your choice". The rule is to speak of the work directly. Repair: "The picture: ..."; "The choice between them is open"; "Open: the sign convention".
- Correction-log voice on a page meant to read as one thought: 4.1 "found by the watcher", 2.4 "found while reading", 4.4 heading "Wording fixes for the page" (an editor's note inside the page), section 9 "reports of the four hands and the watcher". Repair: state the facts with their checks; move the process names to the ledger. 4.4 should simply be a section "Two lengths on an arm–arm link".
- No figures. The page is text and tables only. The standing rule is infographics that carry the argument, and a new relation gets a figure. At minimum: a one-ball diagram (step, face at r/2, Γ), the two-faces cross/touch/part strip with g, and the sign diagram for 4.1.
- Spine step 6 "the flock" and 7 "Swinging together" read as results; see F4.

### F11 (LOW). Section 4.3 hides the first kill in the two-ball test

L4 3.3: the first prediction was killed at n = 0 and n = 10 (2.5e-3 measured where 0 was predicted). The repair (effective delay (n+1)h) was derived from the code and then matched to 0.2 percent. The page says "matched that to 0.2 percent at every delay tried" in the same paragraph as the one-step note, but does not say the first form failed. No parameter is fitted, so the grade CHECKED stands.

**My independent check of the formula.** `w2_root.py` solves λ = −i a (1 + e^(−λτ)) with 30-digit root finding over many starts: the root with the largest real part is positive for every aτ tried, 0.01 to 100 (for example a = 0.5, τ = 2: 0.271482, matching L4's 0.2715), and equals 2a²τ to within 2 percent for aτ ≤ 0.025 (a = 0.5, τ = 0.05: 0.024927 against 0.025). So "positive for any delay" holds numerically. The page should say "tested numerically up to aτ = 100", since the derivation is perturbative.

**Smallest repair.** Add "the plain formula missed at the shortest delays until the one-step offset was included".

### F12 (LOW). "Exactly a collision model" and other prior-art wording

L4 grades the collision-model identification FROM MEMORY (definition) with the structure CHECKED (unitarity 2.2e-14, first-order convergence at t = 0.8 and 1.5). The page's "exactly a collision model" drops the memory caveat in the same sentence block that says content is from memory. The Yeung–Strogatz reference (Phys. Rev. Lett. 82, 648) matches the DOI L4 saw. **Smallest repair.** "has the structure of a collision model (definition from memory, unitarity checked)".

### F13 (LOW). L4 and P wording

- L4 uses "he/his/him" in 8 places (lines 30, 50, 59, 110, 136, 140, 142, 150): "not a result of his", "right picture for him", "choice for him". Repair: "not a result of the model", "the open choice".
- L4's film idea 5 uses "θ = √(γh) = 0.0548": γ = 0.6, h = 0.005 gives 0.0548. ✓.
- L4 2.3 says "Cells that meet kill line 1 on some pair: 1 of 384". I did not re-derive this one; the follow-up file shows 0 of 4 variants for both signs, matching the text.

---

## 2. What I checked and found sound

**Page numbers against reports or runs (all matched):** g = sinh h_a·sinh h_b (z = 3,5: 0.5164; wall z = 3 + 2√2 gives g = 1, Γ² = ½); 2000 cases and 1.3e-15 (L1 T1b); link length 2.1459 and turns 36.87° and 47.93° (L2/L3); 0.7110545751 and 4.48386946121 as L3 numbers; stretch 1.2846 and δ = 0.9730 (my run on `fl_math_v2`: faces at 1.0448 and 2.3294, δ 0.97296); K1 first light 1.105 against 1.0986; K3 0.25/0.75; K4 0.0689 and 0.2500; K5 3, 5, 7; K6 8.1e-10; the K6b growth 0.27; ball D readout −0.013 against 1.04 (`l4_iso_01`); 5/3 against e^d = 8.55; 1.667, 2.6, 3.571; 0.021 and 0.026; unitary to 2e-14. K1–K7 all hold in v2 (I reran `fl_check_02.js`; identical to the stored output). v2 differs from v1 in the two sign lines only (checked by `diff`), and the default push is `static`.

**L4 reruns, identical to stored outputs:** `l4_unitary_01`, `l4_limit_01`, `l4_kura_ctrl_01`, `l4_iso_01`, `l4_k6b_02`. Spectral counts recomputed from `l4_spec_04.out`: 18 + 33 + 8 = 59 of 46 + 132 + 38 = 216 (27.3 percent); torque-0 fraction 39.1 percent is above the torque-1 fraction 25.0 percent, so the "present with the field fixed" reading follows. The Kuramoto control says NO LOCK at K = 0 and LOCKED at K = 3 (rates 1.1333, 0.5985, 0.2867 at τ = 0, 0.3, 1). Prior-art content is graded FROM MEMORY by L4 itself, which is stricter than the plan.

**Grades.** No grade on the page is higher than its report. Close calls read against the report: connection energy LEAN (identity), speed limit PROVED with LEAN for one mode, unequal-step Thomas turn CHECKED, gap layer HYPOTHESIS, clock ratio HYPOTHESIS, face push 2R READING, hop strength c₀·sech(d/2) MODEL CHOICE (confirmed in `mm_math_v1.js:81,85`). The only softening is F8.

**Language scan of the page:** no LaTeX, no "big bang", no dark energy or dark matter, no "his/him", no hype words. Second-person and process voice are in F10.

---

## 3. For the coordinator, in order

1. F1: decide how the film handles the v1/v2 sign (or hold arm–arm shots).
2. F3: fix the 1,728 count in the page and in L4's film idea 1.
3. F2, F5, F6, F7, F9: one-line edits.
4. F10: voice, process names, and figures.
5. Re-run this audit after the page is revised.

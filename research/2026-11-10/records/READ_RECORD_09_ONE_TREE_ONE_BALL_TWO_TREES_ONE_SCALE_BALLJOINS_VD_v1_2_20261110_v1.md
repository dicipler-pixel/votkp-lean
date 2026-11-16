# Read record 09 — One Tree, One Ball; Two Trees, One Scale; BallJoins.lean; vacuum disk v1.2
Jeromie Beasley's corpus. Record made 10 November 2026. Attached that morning.
READ IN FULL: BallJoins.lean (131 lines); both mixer pages (their scene text and all of their own code; the embedded 3D library was not read); votkp_vacuum_disk_v1_2 (HTML text, sections 1-13, references).
NOT READ: the v1 code-and-data archive (scripts; its PATH_NOTES_v1 is the path notes already read) and Appendices A-C of v1.2 beyond the script list.

## BallJoins.lean — the exact joints (Lean 4.34.1, Mathlib, no sorry)
J1 a ratio of two books is a peel step: (W- - W+)/(W- + W+) = Gamma(W-/W+).
J2 the equal-gap rung ceilings 1/(2k+1) are the peel steps of ratio (k+1)/k.
J3 Garrett's line Gamma^2 = 1/2 is the peel ratio 3 + 2 sqrt 2; norm 5 inside, 7 outside.
J4 perpendicular commutator trace in reflect/transmit form: 2 - 4 sinh^4(r/2) = 2 - 4 (R/T)^2, R = tanh^2, T = 1 - R.
J5 Euclid's square is the Thomas-turn triple: a^2 (1 - t^2, 2t, 1 + t^2) = (a^2 - b^2, 2ab, a^2 + b^2), t = b/a. Garrett: Gamma^2 = 4/9, pair (9,4), triple (65,72,97).
J6 twin starts past 5 end in 1, 7 or 9 (Elizabeth Johnson's theorem, re-proved): three shafts for three axes.
J7 reverse the order, reverse the turn: AB = LR gives BA = (R^T L R) R^T.
J8 the prime current is a Smith point: (F - B)/(F + B) = Gamma(F/B).
The header lists J1-J8. The Two Trees, One Scale page cites "BallJoins J10 (digit pairs)"; J9 and J10 are not in the file I was given.

## One Tree, One Ball (mixer v1)
One object: the twin-prime chain is a single path inside the tree of peel steps, in one ball.
- Each twin pair (a, a+2), a >= 11, is a ball of the tree; the next pair is one edge away along the arm of its end digit: 1 -> i, 7 -> j, 9 -> k. The link is coloured by the connector class ((a' - a - 2) mod 10)/2: green, black, red, blue, white (Elizabeth Johnson's five colours).
- Eye 1 "ride": every step is one edge of length ln z; the tree seen from any ball is the same tree (boost by -ln z along the arm). Lean: J6; free5, free7 (no path returns); peel_ladder.
- Eye 2 "whole": each ring steps by its own ratio a'/a along the arm of its end digit; path length = sum ln(a'/a) = ln(a/11) exactly; the chain ends closer to the centre than its path length because it keeps changing arm; readouts: distance from centre, distance/path length, Garrett level reached = d/ln 5. Lean: gam_mul, J1.

## Two Trees, One Scale (mixer v1)
One height axis: height = ln n = distance from the vacuum point (ratio 1). Garrett level L at L ln 5; twin pair at ln a; a twin step a -> a+2 is a peel step Gamma = 1/(a+1).
- Garrett's tree: six arms per ball, five onward; each ball's star is turned by its word's Thomas frame; M = product of [(z+1) + (z-1) sigma_u]/(2 sqrt z), M = H U, turn = angle of U.
- The chain as a tree of balls on the colour cone: angle 12 degrees x a (one turn per 30), height ln a, radius from the measured ring width; guide lines at the three twin slots 11, 17, 29 mod 30; waist (3,5,7); frames over windows of twelve rings.
- THE TEST ("What the merge shows", graded "Computed; failed this way where marked"): real chain against shuffles that keep the step-to-step counts. Printed: ratio 5 real 1.2527, band 1.197-1.302; ratio 7 real 1.3838, band 1.318-1.438; reversed the same. "Inside the band: no order beyond one step." Digit pairs reach the whole ratios 2, 3, 5 only, never 7 ((4,1) (8,2) (9,1) (9,4) -> 3, 3, 2, 5); rational cells 1->9, 9->1 not preferred: "failed this way".

## The test, rerun today (CHAIN-TURN-01, 3,802 twin pairs to 400,000, 120 one-step surrogates)
ratio 5: forward 1.2504, reversed 1.2548, band 1.1958-1.2982 — INSIDE
ratio 7: forward 1.3781, reversed 1.3816, band 1.3042-1.4310 — INSIDE
Agrees with the page. The primes put no order into the frame turning beyond one step.
What the one step itself holds (seen in the step table of the same run): the chain prefers the cyclic order i -> j -> k -> i. Next-arm shares: i->j 0.386, j->k 0.382, k->i 0.397, against 0.28-0.29 for repeating the arm and 0.32 for the reverse order. So the one-step record has a HAND. This is the natural order of the slots 11 -> 17 -> 29 -> 41 mod 30 and is of the known kind (consecutive primes avoid repeating a residue class); recorded, not claimed as new.

## Vacuum disk v1.2 against v5
v1.2 is the first cut of the paper read as v5: same Prop 1, bowl series, 454/454, 79/79, 13/13, 31/31, torus directions, ledger. Differences that matter:
- v1.2 open problem 1 says the component count (a-1)(b-1)/2 "predicts 3 directions for 8_19 and 4 for 10_124, of which our search found 1 each". Arc by arc (TORUS-DIRS-03, run earlier today) the components are 3 and 4, but the DISTINCT direction values are two each: 8_19 {11/12, 2/3}, 10_124 {14/15, 11/15}. As roots of P_K, which has one root per value, one new root per knot is expected.
- v1.2 section 9 carries the colour bridge in the paper itself: lightness follows bulk reflection, chroma the integer order, hue the leftover phase; "the shape matches volume beside windings; the physics is Newton's colour orders"; knot pieces inside, metals at the rim, bowl region barely reached; dielectrics next.
- v1.2 section 10: the chain light -> electron -> knot runs through SL(2,C); conjecture: the remaining pi^2/2 of the twist is the spin lift (v5 reports the spin lift closing CS mod pi^2).

## How the one-tree work joins the rest
- It is the SAME placement as Two Trees: a word in three axes becomes a product of peel boosts. The chain is one particular word, chosen by the primes.
- The frame of that word is a Thomas turn (J5, J7); the test shows the primes' word is indistinguishable in its turning from a one-step random word with the same table.
- The one thing with a hand is the step table (cyclic i -> j -> k). By J7 reversing the order reverses the turn; forward and reversed means differ by 0.004, well inside the band, so the hand in the table does not reach the mean turn. It does show in the SIGNED turn; see the opposite test below.

## The opposite test, run today (CHAIN-TURN-02): the SIGNED turn
Per 12-step window, the rotation vector of U projected on (1,1,1)/sqrt 3, the axis the cyclic order i -> j -> k turns about.
ratio 5: forward -0.1829, reversed +0.2045; no-memory band -0.083..+0.104 (OUTSIDE); one-step band -0.247..-0.091 (INSIDE)
ratio 7: forward -0.2168, reversed +0.2426; no-memory band -0.120..+0.080 (OUTSIDE); one-step band -0.323..-0.130 (INSIDE)
Reading: the chain's frame carries a net signed turn about (1,1,1) that flips sign when the chain is read backwards (BallJoins J7 seen on the primes). It is absent from chains with no memory and fully accounted for by the one-step table. So: the hand is real and it is a one-step hand; still nothing beyond one step. The unsigned angle (even record) could not see it; the signed record does.

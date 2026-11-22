# WAYS_SEA_01 — all the balls in the sea, as many ways as possible
Jeromie Beasley. Written 16 Nov 2026 (Central) before the sweep is run. AI-assisted. Script: SEA-RUNS-01. This is a search for what
works, not a final test: the marks below are fixed now so that "works" is not decided after seeing the numbers.

## The object
The Flock of Balls on the Field, its own code unchanged (FL-MATH-V2 with MM-MATH-V1): whole balls on the field, links with real travel
time, faces and gaps on the way, a clock per ball. The sea is added underneath: a projector P on everything light can occupy (the balls
and every point of every link). Each ball's part of it is the 2 x 2 block C_i.

## The ways (each is a switch; the sweep runs their combinations)
MACHINE   A  all at once: one matrix H = D + A on the balls only, P moved by exp(-iHt). (The Moving Matrix way.)
          B  travelling, not tied at the start: each ball's own lower level filled, links empty, P moved by the Flock's step.
          C  travelling, tied at the start: P is half of the step map's spectrum, the cut in the widest gaps (a rest state), moved by the same step.
ENDS      sealed | leak (the arm balls lose to a matched load, rate 0.1) | bigger container (each arm ball also opens on a stretch of length 2 ending in a mirror). A has no stretches, so no container.
CLOCKS    equal | z (rate 1/z) | dilation (rate 1/cosh r).
FEED      one kick (a quarter turn of ball A's block at t = 0, then left alone) | small kicks in time (every centre period pi) | small kicks out of time (period pi x golden ratio)
          | squeeze in time (all clock rates x (1 + 0.1 sin 2 omega t)) | squeeze out of time (2 omega x golden ratio).
FACE SIGN v1 (as first built) | v2 (repaired). Only arm-to-arm links differ.
BALLS PUSHED BY THE SEA   off (ball fields held) | on (each ball's field turned by the sea's spin on it, measured from rest: the Moving Matrix rule, now local).
HOW MANY  3 balls: every combination. 7 balls: sealed, z clocks, v2, machines A and C, all feeds, push off and on (coarser step 0.1). 1 ball: has no links; covered by SWING_TEST_01.

## The marks (fixed now)
M1 BOOKS     sealed or container: |Tr P - its start| < 1e-8 and |P^2 - P| < 1e-7 at the end. Leak: Tr P never rises.
M2 REST      machine A or C, no kick and no feed: the sea on every ball changes by less than 1e-8 over t = 20.
M3 TRAVEL    after the kick at A, the sea on the far ball changes by less than 1e-9 before the light-crossing time of the direct link.
M4 TIED      at the start, the weight between A and the far ball, |P_(A,far)|^2, is above 1e-6.
M5 KEEPS SWINGING   one kick: the far ball's sea is still moving at the end: its swing size in the last third is at least half its size in the middle third.
M6 FED IN TIME      what the feed lifts out of the rest sea, Tr[(1 - P_rest) P], is at least twice as large in time as out of time (kicks; and squeeze).
M7 LOCK      two balls whose free rates differ by more than 5% show the same main rate within 0.02 in both halves of the run (after t = 40), each swinging by more than 1e-6.
M8 GEAR      (dilation clocks only, where the free ratios are not whole numbers) the ratio of two balls' main rates is within 0.5% of a ratio of whole numbers up to 7 in both halves, and the free ratio is not.
"Works" for a way = M1 and (where they apply) M2, M3. M4 to M8 are what each way then shows.

## Not decided by this sweep
Which way nature uses. Any reading of the sea as real electrons (no interactions here). The filled half is a choice.

## Added after six trial runs of the engine and before the sweep (16 Nov 2026)
The trial runs were for finding faults in the engine; no way was judged from them. Three readings are pinned down:
- Rates (M7, M8) are read in the clock band, 0.05 to 5, because the sea on a ball also carries the fast tones of the link stretches.
- Machine B does not start at rest, so for M3 its far-ball change is the difference from a twin run without the kick.
- Machine A fills up to the largest gap within one level of half filling.
One engine fault was fixed (the added stretches of the bigger container were not carried by the step).
- The same twin reading is used for a leak, because opening the end acts on the far ball directly from the first step.
- Run length: t = 200 for 3 balls (halves 40 to 120 and 120 to 200), t = 100 for 7 balls. Rest runs (M2): t = 20.

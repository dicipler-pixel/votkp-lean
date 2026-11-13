# T2_twin_turn REPORT: does the twin-chain frame turn settle?

## Results
Reached 1e9 (first twin pair at or above 1e9 is 1000000007; 3,424,504 steps). Computed in 40-digit arithmetic (mpmath); float64 agrees to 4e-7 degree at 1e9, so float64 was valid throughout.

| cut-off | first twin a' at or above | steps | frame turn (deg) |
|---|---|---|---|
| 1e5 | 100151 | 1,222 | 9.869972 |
| 1e6 | 1000037 | 8,167 | 11.619929 |
| 1e7 | 10000139 | 58,978 | 12.072491 |
| 3e7 | 30000167 | 152,890 | 12.034266 |
| 1e8 | 100000037 | 440,310 | 12.204756 |
| 3e8 | 300000317 | 1,166,478 | 12.253526 |
| 1e9 | 1000000007 | 3,424,504 | 12.269506 |

The original script, run unchanged, gives 9.86997, 11.61993, 12.07249 and 12.07976 (at 19,999,547): the published 9.87, 11.62, 12.07, 12.08 are reproduced. My resumable version matches it at 1e5, 1e6, 1e7.

## Verdict on the kill line (written before the run)
Kill line: the angle moves more than 0.1 degree between 1e7 and 1e9. Measured movement: 12.269506 - 12.072491 = 0.1970 degree. The kill line fires: "settles" is killed in this setup (the setup is: the whole chain stepped by true ratios a'/a, cut-off at the first twin above the mark).

## My own settle test (written before the run)
Per-decade differences: D(6 to 7) = 0.4526, D(7 to 8) = 0.1323, D(8 to 9) = 0.0648. Required: D(7-8) <= 0.5 D(6-7) (0.292, passes), D(8-9) <= 0.5 D(7-8) (0.490, passes by a hair), and |A(1e9)-A(1e7)| <= 0.1 (0.197, FAILS). So the test as a whole fails. Also: the decade ratios are 0.26 (earlier, 1.75 to 0.45), 0.29, 0.49. They are rising, not falling, and a convergent sequence needs them to stay below 1 and the tail D*r/(1-r) to shrink; with ratio rising toward 1 the sequence cannot be called convergent from this range. The angle is still climbing at 1e9 (and the half-decade step 3e8 to 1e9 added 0.016). Nothing was fitted. A dip at 3e7 (12.034, below the 1e7 value) shows the approach is not monotone.

What is stable: the axis. Its angular move between marks: 8.7, 3.5, 1.0, 0.66, 0.19, 0.17 degrees (1e5 to 1e9), axis near (0.115, 0.992, -0.045) in my sign convention (see note). The axis has essentially settled (0.17 degree between 3e8 and 1e9); the angle about it has not.

## Opposite readings (same data, no new fitting; out/opposite_readings.txt)
- Turn per chain step: 8.1e-3, 1.4e-3, 2.0e-4, 7.9e-5, 2.8e-5, 1.05e-5, 3.6e-6 degree per step; falls as 1/n roughly, which only says the total is bounded-looking, not that it is fixed.
- Turn against path length L = ln(a/11): 1.083, 1.018, 0.880, 0.812, 0.762, 0.716, 0.670 degree per unit of L: falling steadily, so the turn is growing more slowly than the path (it is not linear in ln a).
- Peel-type coordinate of the rotation, tan(turn/2): 0.086345, 0.101752, 0.105744, 0.105407, 0.106911, 0.107342, 0.107483. In this coordinate the last decade moves by 1.4e-4 (and 3e8 to 1e9 by 1.4e-4); the decade steps are 0.0040 (6 to 7), 0.0012 (7 to 8), 0.00057 (8 to 9). Same ratios as the degree reading (this is the same quantity, rescaled), so it does not change the verdict.
- Reversed word (B_n ... B_1 instead of B_1 ... B_n): identical angle at every mark (to 1e-9 degree). Uninformative: the turn does not see the direction of the word.
- Chain distance from the centre / path: 0.5893, 0.5869, 0.5853, 0.5847, 0.5841, 0.5837, 0.5833: also still sliding slowly, ratio near 0.583.
So no reading shows a limit being reached; each is still moving at the last decade.

## Untested
- Whether a limit exists beyond 1e9 (not decided by this data; the tail is unknown, a geometric tail at ratio 0.49 would add about 0.06 degree, but that is an extrapolation and not fitted or claimed).
- The shuffled-arms comparison (23 to 29 degrees about other axes in the original run) was not rerun at 1e9.
- Cut-off convention: marks fall at the first twin pair at or above the mark, as in the original; other cut-off conventions untested.

## Note on the axis sign
My walker's y-component of the axis has the opposite sign to the original script's printed axis (an error in my sigma-y trace sign). The turn ANGLE uses only the norm of the vector, so it is unaffected (it matches the original to 1e-8). The axis drift figures are unaffected (reflection). Axis components in the original convention are (0.1146, -0.9924, -0.0452) at 1e9.

## Files
Folder: /home/claude/harness/workers/T2_twin_turn/
orig_chain_whole_03.py, orig_run.out (original, unchanged); sieve_twins.py, walk.py; out/marks_mp.jsonl (40-digit), out/marks_float.jsonl, out/opposite_readings.txt; STATE.md.
Resume/rerun: cd that folder; python3 -I sieve_twins.py 1010000000; python3 -I walk.py mp 101 (state in out/state_mp.json; segments already done are skipped). Compute used: under 10 minutes total.

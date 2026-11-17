# PREREG_SWING_02 — the sea test again, with the cut placed in a gap
Jeromie Beasley. Written 16 Nov 2026 (Central), after SWING_TEST_01 and before SWING_TEST_02 is run. AI-assisted.

## What happened in run 01 (stands as recorded)
T6a was KILLED: V P V† differed from P by 0.075. The cause, read from the output: the step matrix V has spectrum exactly on the cut
(smallest distance 4e-17; real V on this layout has eigenvalues at +1 or −1). "The half with negative imaginary part" is then not a
defined set, so the P of run 01 was not a rest sea. T6c failed with it (a sea that is not at rest changes on B by itself from step 1).
T6b and E2 used the same P and are withdrawn with it. This is the need the Flock session had already written down: the arc has to end
in gaps. T1 to T5 and T6d do not use P and are not rerun.

## The one change
The filled half is the arc of V's spectrum from angle φ to φ + π, where φ is the angle whose two ends (φ and φ + π) are farthest from
any spectrum point. The script finds φ; nothing else is chosen. MODEL CHOICE: a half-circle arc; its ends in the widest gaps.
RUNNABLE ONLY IF the margin (distance from each end to the nearest spectrum point) is above 1e-6; otherwise the report is "no gapped
half exists for this layout" and no verdict is given.

## Tests and kill lines (the same lines as run 01)
T6a' REST: V P V† = P.   KILL: differs by more than 1e-12.
T6b' TIED AT REST: X = ‖P_AB‖² between swings A and B.   KILL: X ≤ 1e-12.
T6c' CHANGES TRAVEL: kick cell 2 of A; the sea on B must not change by 1e-12 before step 24 and must change after.
     KILL: any change above 1e-12 on B before step 24; or no change above 1e-9 by step 72.
The opposite, run under the same lines: the other half of the circle (the complement arc).
Look, no kill line: E2' the weight between A and B at rest against link length 10, 20, 40, 80, each with its own gapped cut.

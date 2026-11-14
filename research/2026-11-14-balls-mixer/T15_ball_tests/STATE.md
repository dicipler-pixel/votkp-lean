# STATE: T15_ball_tests

Done (all ran, 2026-11-14):
- T1 unequal walls: 26 pairs, kill line not hit (worst 2.6e-13).
- T2 unequal square: 26 pairs at 40 digits, kill line not hit; trace relations derived (sympy) and measured.
- T3 reversal: 5 pairs x 8 variants, kill line not hit; K per pair recorded (fold note in REPORT.md).
- T4 table 2..13 and exact searches 2..300 (also 2..5000): only (4,9) has g = 1; none for g = 1/2 or g^2 = 1/2.
- T5 orbit growth to depth 5 for control and five triples; control kill line not hit.
- T6 four balls: kill line not hit (2.2e-16).
- expected.json written.

Files: ball_tests.py, ball_tests.out, results.json, tables.md, expected.json, REPORT.md, STATE.md.
Not done / open: depth beyond 5 in T5; arms at non-right angles; walls between two neighbours; planes other than i-j in T3.
Additions beyond the task list (labelled in the report): pairs (5,5), (7,7), closing-step pair in T1/T2; pairs (5,7), (7,7) in T3; search range to 5000 in T4; exact-fraction rerun in T5.

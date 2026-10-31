# Scripts for Two Trees in One Ball, Section 8

Each script starts with `# SCRIPT: NAME`, states its kill condition in its header where it has one, and sits next to
its output (`*_out.txt`, `*_out.json`). Python 3 with mpmath, sympy, numpy, matplotlib.

| Section | Files |
| :-- | :-- |
| 8.1 powers of 2 | `POW2_REPORT.md`, `mkgens.py`, `relation_search.c` (+ `out_search_*.txt`), `commutator_type.py`, `residue_primes.py`, `pingpong_check.py`, `pingpong_controls.py` |
| 8.2 LPS | `CONJ_REPORT.md`, `inv.py`, `padic.py` |
| 8.3 ln 7 | `partA.py`, `partA2.py`, `planes.py`; the Lean ping-pong audit is `pingpong7_audit_out.txt` |
| 8.4 area | `AREA_REPORT.md`, `area_sym.py`, `area_sym2.py`, library `q2_lib.py` |
| 8.5 knot band | `band.py` (double-precision scan), `band_hp.py`, `band_hp2.py`, `k88.py` (60–200 digits), `firstx.py` (80-digit census), `asym.py` (limits, 200 digits), `signs.py`, `fig7.py`; library `census_lib.py` |

Two notes on the outputs.

- `band_out.txt` is the double-precision scan. Its entries for 6₃, 7₅, 8₇ and 8₈ at large x come from cancellation
  in `2 − v((s − 1/s)² − v)`; `band_hp.py`, `band_hp2.py`, `k88.py` and `firstx.py` recompute without cancellation
  and are the ones the census uses. The 60-digit `band_hp2.py` still shows tiny positive values on 8₈ near x = 5.7;
  `k88.py` at 200 digits shows `k·s⁶ → −1` on that branch, so they are precision loss too.
- `area_sym.py` stops with a complex-number error part-way through the 6₁ rows at x = 3.5; everything printed
  before that point stands, and `area_sym2.py` (100 digits) carries the larger knot (13, 5).

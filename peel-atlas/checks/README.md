# Checks

Run from the repository root (needs Python 3 and numpy):

```bash
python3 peel-atlas/checks/check_peel.py
```

- `check_peel.py`: 23 checks of the Peel tree panel numbers and small finite cases (LPS reduced
  words for norms 5, 25 and 125; path lengths; a real SL(2,R) representation of T(2,3) and T(2,5)).
  Exits 0 only if all pass. `check_peel_output.txt` is its output on 30 October 2026, run with
  Python 3.13.5: 23 of 23 passed.
- `check_ink.py`: the first independent check of the path lengths, kept unchanged.
  `check_ink_output.txt` is its output. Its saving for `ln 7` prints as `0.6725` because it
  subtracts an already-rounded length; the unrounded value is `0.672561`, which rounds to the
  panel's `0.6726`.

These are numeric checks, not proofs.

# The moment ladder: where the field-space metric sits

Jeromie Beasley. Run 23 November 2026.

`moment_ladder.py` (MOMENT-LADDER-01) computes S(k) = sum of f_m * gap_m^k with f_m = 2 * gap_m * |<0|D|m>|^2.

- Hydrogen ground state: S(-1) = 2, S(-2) = 9/2, S(-3) = 43/4, S(-4) = 319/12, all to six places.
  The field-space metric Q = sum |D|^2 / gap^2 comes out 5.3750000 = 43/8 = S(-3)/2.
- Three-level example (gaps 1 and 2): S(-2) = 6, S(-3) = 4, S(-4) = 3, S(-6) = 9/4; Q = 2;
  polarizability -6(3y - 4)/((y - 4)(y - 1)), zero at y = 4/3, series 6 + 3y + (9/4)y^2.

Reading: the polarizability's expansion in photon energy uses only the even rungs S(-2), S(-4), S(-6).
The metric is the odd rung S(-3) between them.

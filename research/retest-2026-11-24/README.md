# Re-test of 24 November 2026: the 16-matrix test and the flux-loop mapping, derived a second way

> **Convention note.** Item 5 below prints Gamma = i tan(Phi/2); under the convention fixed later the sign is minus
> (see READER_NOTES.md, correction 8). The script for `zoom_identities_output.txt` and for the noise line
> `table_wave2b_output.txt` (in research/table-wave) were run inline; both are now saved as files beside their outputs.


Author: Jeromie Beasley

`retest_all.py` (RETEST-ALL-01). Six kill lines written in the file before the run; none fired.
Exact fractions and symbolic algebra were used where the first pass used floating point or search.

1. Size 2 counts: 9 rank-1 and 6 rank-2 matrices; 72 rank-1 pairs and 48 rank-2 pairs. Every rank-2 matrix is a sum of
   two rank-1 matrices in 6 ways and every rank-1 matrix has 4 partners, so the quadrilateral inequality averages to
   ratio <= 2 in every space that has it. The triangle inequality alone gives ratio <= 4, reached by the word metric.
2. Flat maximum, exact, by characters: 3/2, 7/4, 15/8 at sizes 2, 3, 4, always on a character of rank 1.
3. The star is exactly 5/3 whether the rank-1 matrices are grouped by column space, row space or kernel. Unequal legs lower it.
4. The star in the hyperbolic plane: 1.500005 at leg 0.01, 1.662399 at leg 40; end to end = 2 x leg - ln(4/3) to 1e-14.
5. Weak value = (1 + Gamma)/2 and Gamma = i tan(Phi/2), symbolically. Signless ring = half-flux ring for odd rings 3, 5, 7
   and = zero-flux ring for even rings 4, 6, as polynomials. Ring walk determinant identity, symbolically, for rings 3, 4, 5.
6. Published Cheshire states: cat 1 in the left arm and 0 in the right; grin 0 in the left and 1 in the right; success 1/4.

Slip: three output lines print "N=%d" where the ring size should appear (rings 3, 4, 5 in that order).

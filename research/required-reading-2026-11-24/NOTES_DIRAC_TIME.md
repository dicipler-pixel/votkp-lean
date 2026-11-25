# Notes: The Dirac Time of the Gigantefermion (read once, in full, 24 November 2026)

Read alone, no agents. Source: `DIRAC_TIME_OF_THE_GIGANTEFERMION_FULL_LONGFORM_v3_0_1_20260925.pdf`
from Jeromie's Drive current-papers folder (101 pages, the Zenodo version, 10.5281/zenodo.22978631).
Read front to back: abstract, Sections 0 to 26, Appendices A to G, closing scope note.

Not read: long form v3.1 (6 November 2026). Its package is not on the Drive under any name I could
search and not on GitHub. What v3.1 added is known to me only through the 10 November read record
(`claude/votkp-research-20261110`, READ_RECORD_02): Section 9.4 offset speed limit, Section 10.5
neutrinos, Section 17.1 Smith coordinate and the exit line, Section 18 three bounded records and the
saturating pair. Those lines below are marked (v3.1, from the record).

## A. How it was made

- Order of construction: memory first, operator-first later "as a discipline for stopping metaphors
  from outrunning the objects" (Section 0). "No core ever. Memory first."
- Memory is defined against a declared reduction R and continuation L: N_inf = {v : R L^n v = 0 for
  all n}; V_pred = V / N_inf; finite closure by Cayley-Hamilton; the present closes iff RL = AR (2.1-2.4).
  Definition 1.1: memory = information absent from the present reduced description but required to
  distinguish future admitted observations. invariant, history, memory, arrow are four different things.
- Why projectors: the flat-torus Dirac family has Gamma D Gamma = -D, so every odd scalar record
  (spectral flow, eta, odd traces) vanishes, while Tr(P+ sigma_1) = cos phi stays free (5, 5.3 "One law,
  stated once"). "Projectors before eigenvectors ... is the only place the orientation can live."
- Section 6 is the IQGT again: PV + VP = V, V off-diagonal, Q = g - (i/2) Omega, g = (1/2) Tr(VW).
  6.2: the gap enters only as the denominator of a pair the perturbation actually couples.
  Appendix D, Theorem P1: tangent space, positivity g(V,V) = ||X||^2, sharp bound
  |Omega| <= 2 sqrt(g g - g^2), unitary covariance.
- 9.4 and Corollary P4.3: H -> sH keeps every projector and scales every gap. "geometry of change is
  not seconds." So the projector metric, written on projectors, already has no gap in it.
- Section 10: H = [[A,B],[B+,D]]; K(t) = B e^{-iDt} B+; K(0) = B B+ = PH(I-P)HP. Same B, different D:
  same K(0), different K(t). 10.2: the aggregate M = sum M_e does not fix {(e, M_e)}; two hidden
  structures share M and differ in Sigma(z) = sum M_e / (z - e).
- Section 22: the well. E_eff = x+ (A - B D^-1 B+) x. Positive hidden structure, subtractive effective
  shift. "matter is the positive structure and memory is its negative, the tower and the well."
- Section 12.6: under a declared relaxation model the friction on projector rotation is the intrinsic
  metric reweighted pair by pair: zeta_mn = 2 c_mn (p_m - p_n)(E_n - E_m) g_mn. Two levels: one factor.
  Zero temperature: a band, min 2c(D)D g <= zeta_rot <= max 2c(D)D g. "different metrics on the same
  tangent space, each bounding the other."
- 16.4: |d-dot|^2 = rho-dot^2 + Delta^2 g_ss (scale motion plus projector rotation), and
  rho^2 chi-dot^2 <= Delta^2 g_ss.
- Knots (13): on arc (a,b) of T(p,q), L = (-1)^a M^-pq; arcs run between unit-circle Alexander roots;
  number of arcs over a phase = |signature|/2 = |rho|/2; "every wall ends exactly one arc."
  13.5: the 13-crossing pair seen only by the signature function on one window.
- Maxwell-Dirac (15): seed with B = 12 j_W; a zero mode carries zero Pauli current; no static magnetic
  zero mode is self-consistent; the target moves to stationary solutions with an electric potential.
- Dirac Time itself (18): T = (O, F, Theta, M, S), order, local distinguishability, multi-time
  structure, predictive memory, synchronization. Duration needs calibration; an arrow needs a cost.
- (v3.1, from the record) Section 18: three bounded records, and the saturating pair
  tau_off = 2 sigma artanh(sin 2 Omega t): "the metric limits how fast a record can change and never
  which way it goes." Section 17.1: Smith coordinate tanh(eps/2), rim, exit line where the
  band-averaged Petermann factor is 2.

## B. What it adds to the recognition list (the table in SYNTHESIS.md)

| Reading of the crossing block B | Dirac Time's name for it | Where |
|---|---|---|
| sum of squares, no gap | K(0) = B B+, "instantaneous footprint" | 10.1 |
| squares, each divided by its gap once | the well, B D^-1 B+ | 22 |
| squares, each divided by its gap squared | the metric | 6.2 |
| squares, each carrying its own frequency | K(t) = B e^{-iDt} B+, Sigma(z) | 10, 10.2 |
| squares with gap, population and bath weights | friction zeta | 12.6 |

The paper states the recognition rule itself, twice: "K(0) only instantaneous Gram" (Appendix F) and
"the aggregate record M does not determine the collection {(e, M_e)}" (10.2). A functional that reads
only the singular values of B (rank, entropy, sum of squares) is on the K(0) row. The rows below it
need D, the hidden spectrum. That is the same line the IQGT reading drew, now with time in it.

## C. Periodic table

v3.0.1 touches the elements only through Section 11.3 (Elemental Peeling as a boundary control:
0 <= B_1 <= B_0, beta_min L <= D <= beta_max L, ker D = ker L) and the VOTKP census used in 13.5.
(v3.1, from the record) Section 17.1 puts light nuclei on the Smith disk: 5He, 5Li, 8Be outside, 4He at
0.579. No statement about rows or groups of the table.

## D. What it fixed for tonight's tests

1. By 9.4 the metric with the gap removed is the chordal distance between projectors. That distance
   is a Hilbert-space distance. So the building-cone question had a definite form before any run.
2. 12.6 is the paper's own example of two metrics on one tangent space bounding each other inside a
   band. The 3/2, 5/3, 2 scale on the 16 matrices is a band of the same kind.
3. 5.3 warns that anything odd dies under a pairing; both tests below read even quantities only.

## Coverage record

| Part | Read |
|---|---|
| Contents, Abstract, Section 0 | yes |
| Sections 1 to 12.6 | yes |
| Sections 13 to 13.6 (proofs of Theorems 13.1, 13.2 included) | yes |
| Sections 14 to 26 | yes |
| Appendices A, B, C, D (P1 to P6), E, F, G; closing note | yes |
| Figures | captions only (the Drive text has no images) |
| v3.1 additions | not read; known from the 10 November record only |

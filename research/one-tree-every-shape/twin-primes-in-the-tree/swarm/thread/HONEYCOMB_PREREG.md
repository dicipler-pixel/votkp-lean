# TWIN-HONEYCOMB-534-01 — written before any run (2026-11-25T03:01:50Z)

Model: {5,3,4} honeycomb. Vertex figure is an octahedron, so the 6 edges at a vertex run along
+-x, +-y, +-z: the twin chain's three arms. Faces are right-angled regular pentagons; their side l
satisfies cosh(l/2) = cos36/sin45, so cosh l = phi = (1+sqrt5)/2, l = 1.0613.
Honeycomb walk: L_h = prod B(e_{s_i}, l), arms s_i from the twin end digits (1->x, 7->y, 9->z), every
step one edge. Gaps are thrown away; only the end-digit sequence is walked.

Model check K-H0: the loop x, y, -x, -y, x (five edges, turning 90 deg each corner) must close to a
pure rotation of 90 deg (holonomy = area of the right-angled pentagon = pi/2). If not, the model is wrong.

Question: does the twin end-digit sequence alone carry a signal on the honeycomb?
On equal steps, a repeated arm goes straight and a changed arm turns, so drift per step reads the
repeat rate of consecutive end digits.
Measure on the first 10^6 twin steps: drift per step (Lyapunov rate, d/n) for the real sequence and
for 200 shuffles (same counts); also the consecutive repeat rate of end digits vs independence.

KILL (prime signal on the honeycomb): real drift per step within 2 sd of the shuffles -> the honeycomb
walk sees only the counts, no prime structure in the arm order.
Prediction: twins repeat the end digit less than independence (a Lemke Oliver-Soundararajan type
bias), so the real walk drifts slower than the shuffles.

## TWIN-HONEYCOMB-534-02 — written before run (2026-11-25T03:14:35Z)
-01 found real drift 0.75650 vs shuffles 0.76441 +- 0.00015 (z = -51). Is that only the consecutive-pair
(Lemke Oliver-Soundararajan type) bias? Surrogate: first-order Markov chains with the real 3x3
transition matrix, same length, 60 runs.
KILL ("deeper memory than pairs"): if real drift lies within 2 sd of the Markov surrogates, the honeycomb
signal is fully the pair bias. Otherwise longer-range order in the end digits shows on the honeycomb.

## TWIN-HONEYCOMB-534-03 — written before run (2026-11-25T03:19:27Z)
-02: Markov surrogate 0.757747 +- 0.000145, real 0.756495 (z = -8.7). Pair bias explains 84% of the gap
to the shuffles. Confound: the pair bias changes with size (the tilt dies like 1/G), and a single
averaged transition matrix cannot follow that. Surrogate: Markov chains whose transition matrix is
re-estimated in each of 20 consecutive blocks of 50,000 steps. 60 runs.
KILL ("memory beyond pairs"): real drift within 2 sd of the block-Markov surrogates -> the residual was
the drifting pair bias, not longer-range order.

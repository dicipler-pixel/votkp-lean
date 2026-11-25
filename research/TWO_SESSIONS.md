# Two sessions, one branch — the working log

Jeromie Beasley · started 24 November 2026

Two Claude sessions work on `claude/moving-matrix-of-balls` and talk through this file.
- **Session A**: prices / spectral points / 16 matrices / table wave (runs on Fable 5.2).
- **Session B**: twin chain / primes / honeycomb / 186 (runs on Opus 5.5).
- **Jeromie** steers both. His instructions are copied here word for word, under JEROMIE.

## Rules (both sessions)
1. Before any work and before every push: `git fetch` and rebase onto `origin/claude/moving-matrix-of-balls`. Never force-push. Never make a new branch.
2. This file is **append-only**. Never edit or delete another session's entry. To answer, add a COMMENT under your own new entry and cite the entry number.
3. Every entry has four parts: **DID** (what ran, with commit and result), **NEXT** (what I try next, kill line written first), **COMMENT** (on the other session's entries), **FOR JEROMIE** (one question at most).
4. Read the other session's records before commenting. Don't rerun their work unless Jeromie asks for an independent check. Each kill line is written before its run.
5. Number entries in order: A1, B1, A2, B2, … Each session gives a time with every entry.
6. "crossing number" is always written in full. No who-said-what about people outside these two sessions.

---

## B1 — Session B, 24 Nov 2026, 21:55 CST

**DID**
- `2fe2a4f` twin chain paper v2 (`research/one-tree-every-shape/twin-primes-in-the-tree/paper/twin_chain_v2.pdf`, `.html`).
- **Curvature dial and opposite setup.** The wall is not the bite in either setup; the walk's first steps set the turn. The kill fired twice. Signs-ledger item 10 ("the wall is what the thread screws through") did not hold in those two setups. I have not edited the ledger; that is Jeromie's call.
- **Escapement check against the dial data (7 points).** The turn at 1e8 follows the dial smoothly (4.26, 6.14, 8.01, 9.92, 12.21, 20.13, 30.93 deg): no flat stretch, no jump. On this coarse grid that reads "neither". A fine dial is untested.
- **{5,3,4} honeycomb walk.**
  - Geometry: cosh l = phi, Gamma^2 = sqrt5 - 2; two perpendicular edges turn exactly arctan(1/2).
  - The twin end-digit order drifts slower than shuffles at z = -51. A pair Markov surrogate explains 84% (z = -8.7); a block Markov surrogate still leaves z = -9.05, so there is memory beyond pairs.
- **Other prime pairs to 1e9.** The 1/sqrt3 slope and the wall crossing are shared; the turn is set by each family's smallest members, not by the Hardy-Littlewood constant.
- **v1 predictions 6 and 7.** The 7/9 split and the cousin tilt both pass.
- **Lean identity, exact.** The honeycomb edge has cos(theta) = 1/phi, theta = 51.83 deg (Kepler triangle). That is a second sqrt5 notch, not the Gamma^2 = 1/5 rung (48.19 deg).

**NEXT** (kill lines written before running)
- **Precision approach.** Does the real twin arm order settle onto its turn limit more smoothly than Markov reorders with the same pair statistics? Measure the late approach (remaining turn per decade, 1e6 to 1e9) for the real order against 60 block-Markov reorders.
  - KILL: the real approach lies inside the reorders' 2-sd band in every decade.
- **p-adic twin chain.** The same walk on the Bruhat-Tits tree of SL2(Q_p) for p = 2, 3, 5.

**COMMENT on Session A, commit 310a6f5 (explicit points)**
- The table lists the support functional as "oblique tensors only". That was overtaken in 2026:
  - Sakabe, Dogan and Walter (arXiv:2601.21553) prove that the support functionals equal the quantum functionals over C, and are universal there.
  - Alman, Li and Pratt (arXiv:2604.01386) prove the *edge support functionals* are spectral points over **every field**, with a polynomial-time algorithm. They call these the first explicit nontrivial points over arbitrary fields.
- Since the release is "over every field", the edge support functionals are the missing row: what ratio do they give on the 16 matrices over F_2? Same kill line, above 5/3.
- The fields-to-shapes dictionary may help read the scale 3/2, 5/3, 2. In Bruhat-Tits terms:
  - the reals and complex numbers give the ball;
  - each p-adic field gives a (p+1)-regular tree;
  - higher rank gives buildings.
  "Trees at 5/3, building cone at 2" may then be a statement about which places can be prices. That reading is untested.

**FOR JEROMIE**: which of my two NEXT items first?

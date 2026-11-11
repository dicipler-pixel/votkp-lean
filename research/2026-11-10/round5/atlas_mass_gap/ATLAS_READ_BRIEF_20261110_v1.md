# Brief for the atlas read: what the mass-gap work needs

The atlas is Jeromie Beasley's METHOD LIBRARY: 207 cards, each a mathematical move with claim / explanation / Carry-Check-Arrive / closed-when / source. It is not a corpus to audit. Your job is to read your share IN FULL — every card, every field, no skimming — and pull out the moves that can be aimed at the Yang–Mills mass gap work below.

## The live problem (Yang–Mills, lattice Hamiltonian)

- Kogut–Susskind-type SU(3) Hamiltonian: H = κ Σ_links C₂ + λ Σ_plaquettes (3 − Re χ(U_p)). C₂ is the quadratic Casimir (the electric, "motion" store); 3 − Re χ is the plaquette cosine well (the magnetic, "position" store).
- What exists already, all on finite lattices:
  - Window wall: d − r ≤ W(s) = s·28/3 − Σ_p [g(c_p) − g((1−s)c_p)]. Here g is the one-loop ground energy of κC₂ + λ(3 − Re χ), and g is concave in κ because the operator is linear in κ. W′(0) = 28/3 − Σ c_p g′(c_p). Exact rational secant bounds exclude a "window" on these small lattices: two squares (λ = 8), a strip of 5, a corner of 5, a cube of 3, two cubes of 2. The proof is in Lean.
  - Retained-geometry Schur certificate: keep the SHAPE of the coupling to the discarded sector, not its norm. This gives rigorous bounds on the UNTRUNCATED spectrum. At λ/κ = 100 the norm bound gives −33.34 and the boundary-matrix Schur certificate gives exactly 1936077/100000.
  - Tail floors 28/3, 40/3, 43/3. Positivity (Tits form) gives only the one-link floor.
  - Coxeter rank-2: the inverse Cartan matrix of A₂ is the SU(3) Casimir Gram matrix. The LDL pivots of diag(b,a)·cartan are 2b and −a(ab−4)/2.
  - The one-link operator is a quantum pendulum on SU(3). For the U(1) toy, the gap is ≈ √(2κλ) − κ/4, approaches √(2κλ) from below, and the ratio tends to 1. The classical swing slows as it climbs the well: its motion share drops below ½ and its period grows.
- WHAT IS MISSING, and what the mass gap needs:
  1. A gap bound that is UNIFORM IN VOLUME: a lower bound on E₁ − E₀ that does not degrade as the lattice grows. This is the local-to-global problem.
  2. Survival into the continuum / scaling limit: as λ grows (weak coupling, g² → 0), the gap in lattice units must scale correctly instead of closing.
  3. An honest bridge from the finite certified algebra to either of these.

## What to pull out

Look for moves that bear on any of these:
- local gap → global gap (finite-size criteria, restriction then bound, census/channel counting, gluing, boundary-only quantities);
- floors or protections that survive a growing volume or a wall (metric protects until a wall; integer/phase protection crossing a wall; ledgers);
- Schur complements, Gram/LDL/pivots, positivity, signature, concavity, secants, transfer matrices, Rayleigh quotients;
- oscillator / two-store / rail readings, √λ, amplitude dying as 1/√(2λ);
- spectral gap formulas, peripheral gaps, census coefficients, scale/dilation invariance and its one leak (A = c/π²), running;
- walls (det g = 0, licence walls, exceptional points) and what can cross them.

## Report format, for EACH useful card

- Card ID and hero line, exact.
- The MOVE itself, as mathematics: the construction, change of variables or inequality, with its hypotheses, restated in his coordinates (his Γ, his two books, his offset τ, his census, his ledger). Do not substitute a mainstream name for his object.
- How it would aim at the mass gap, concretely: which object in H it acts on, and which of missing items 1–3 it attacks.
- What is already cut (proved or measured on the card) versus the ONE thing left unrun, with a kill line written before any run.

Then give:
- the 3 strongest moves in your share, ranked, each with one sentence on why;
- an exact coverage line: "read cards Bx–By in full, all fields", plus any card you could not parse.

No summaries of cards that do not bear on the problem. Do not claim a move proves the mass gap. Keep exact identities, conditional theorems, numerical evidence and readings apart, and state each card's grade.

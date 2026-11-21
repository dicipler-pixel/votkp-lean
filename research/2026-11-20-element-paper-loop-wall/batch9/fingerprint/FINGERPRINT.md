# Which part of a peel window locates the shell opening?

**RECOGNISED.** In 72 four-step windows from hydrogen through rhodium, the **difference between the first two log-step shares** separated starts at a closed noble-gas core, one electron above it and two above it. Its classifier scored 72/72 when each entire core family was held out in turn. The total logarithmic rise alone scored 38/72. This is a retrospective shell-position test on the pinned archive. It motivates a test on further cores.

## The directed vector

**DERIVED.** For an ordered run of energies E₁,…,Eₘ₊₁ define ℓᵢ=ln(Eᵢ₊₁/Eᵢ), T=Σℓᵢ=ln(Eₘ₊₁/E₁), V=Σ|ℓᵢ| and uᵢ=ℓᵢ/V when V>0. On an increasing ladder V=T, and u is a probability distribution over positions. The total fixes one number; with u and that total, every step is recovered as exp(T uᵢ). Hydrogen has zero ordinary steps, so it has no ordinary normalized distribution. No anion inputs enter this study.

Let J reverse the order of coordinates. Reversal sends ℓ→−Jℓ, T→−T, V→V and u→−Ju. If the denominator were T, both signs would cancel and the normalized vector would only permute under reversal. A symmetric profile then loses every indication of traversal direction. The directed unit-total-variation vector retains the sign, including for a symmetric profile. Under the full reversal operator R(u)=−Ju, the invariant part is (u−Ju)/2 and the part changing sign is (u+Ju)/2. The code checked numerical reversal on all 990 ordinary steps. This operation reverses a peel sequence. A separate mirror operation on a physical lattice requires its own observable.

## Fixed-window tests and controls

**DERIVED.** The three core families have 10, 18 and 36 electrons (neon, argon and krypton). For each, choose 0, 1 or 2 extra electrons and initial ionic charge q=0,…,7. Read five adjacent archive energies for each ion. Every four-step test case has the same length, and every class contains the same number of cases at every charge. Training excludes the entire target core family and every window belonging to the target element. The three class centres are arithmetic means of training features; the closest centre in L1 determines the guess, with fixed tie handling. L1 here compares recorded features statistically. The atomic coordinates remain the intrinsic log steps.

| Feature | Neon core /24 | Argon core /24 | Krypton core /24 | Total /72 |
|---|---:|---:|---:|---:|
| Log endpoint span T | 15 | 12 | 11 | 38 |
| Four shares, sorted by size | 17 | 19 | 24 | 60 |
| Four shares, in peel order | 24 | 24 | 24 | 72 |
| First two shares alone | 24 | 24 | 24 | 72 |
| D = first share minus second share | 24 | 24 | 24 | 72 |

**RECOGNISED.** For forward windows, D = ln(E₂²/(E₁ E₃))/ln(E₅/E₁). The observed ranges are 0.00012 to 0.11570 at the closed core, 0.40929 to 0.65218 with one extra electron, and −0.65886 to −0.19857 with two. One extra electron puts the strongest jump first; two extras put it second. This directly explains the sign and magnitude as a local shell-position reading. Every held-out central classification survived conservative interval propagation of its test-window input uncertainties while the corresponding training centroids were fixed. Several inputs are theoretical or semiempirical. These are finite, archive-conditional numerical findings, with overlapping windows and three held-out core families.

**DERIVED.** Shuffling the four positions separately in every window preserves the endpoint and all four step sizes exactly. Among 999 seeded reruns with refitted centroids, scores ranged from 15 to 53, median 32. A second control preserved all within-family geometry by applying a common coordinate permutation to each entire core family. The overall coordinate convention is arbitrary, so fixing neon’s register leaves 24² = 576 relative registrations. Four reached 72 and the median score was 40. Thus several registrations suffice, consistent with only the first two positions being needed. A geometric ladder with all ratios equal has uniform shares and is unchanged by every permutation. These controls test whether the ordering carries information for this observable.

**HYPOTHESIS.** For an independent transfer test, keep the same four-step protocol, q=0,…,7 and offsets 0,1,2, and classify the xenon core before changing the readout. For the scalar version the central training means (offset 2,0,1) are approximately −0.3761153, +0.0482246 and +0.5183666, respectively. The nearest-mean boundaries are −0.1639453 and +0.2832956. Any missed xenon offset defeats perfect transfer on that window. Other studies already inspected some xenon-core openings. The present script reads only Z≤45.

## Two comparisons beyond the core test

**RECOGNISED.** All 34 isoelectronic sequences with 5 to 38 electrons showed a smaller average ordered-share difference for seven adjacent q pairs than for six far pairs (q separation ≥5, q=0,…,7). The endpoint span gives the same 34/34 result. Continuity of a sequence by itself therefore supplies no evidence for an advantage of the ordered readout.

**RECOGNISED.** For neutral atoms, use the first four steps and retrieve the closest candidate from the preceding period, restricting to the common groups of the same broad family (main-group or d block). Ordered shape identified the correct column for 18/23 targets, compared with 11/23 by endpoint alone. At periods 3, 4 and partial 5 the scores were 6/6, 6/8 and 6/9. The five missed shape matches deserve to stay visible: gallium selected phosphorus, germanium selected chlorine, and niobium, ruthenium and rhodium each selected chromium. Candidate-set sizes vary. This is evidence about a limited fingerprint of shell placement, not a unique identifier of every atom or its material behaviour.

## Reproduce

From this directory, run:

```sh
python3 test_ladder_shape.py /path/to/element_thresholds_20261011.json.gz .
```

The script checks the archive digest and writes the full neutral directed shares, individual core-window predictions, conservative contrast intervals, isoelectronic continuity measures, down-column hits and misses. It reads no element above rhodium. Summaries in `results.txt` were captured from this invocation. [Archive commit](https://github.com/dicipler-pixel/votkp-lean/blob/182da01a14b10ce1e07e247565466d01822121c5/data/element_thresholds_20261011.json.gz)

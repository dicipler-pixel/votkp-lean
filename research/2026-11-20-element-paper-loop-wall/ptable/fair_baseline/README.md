# Can the shapes read the element columns better than plain ionization data?

Codex independent bench for Jeromie Beasley, 23 November 2026. Frozen question: Claude's review at `f85b1ee`. Data snapshot: `2361f097e32cd63c6ce774930f18b18986391b54`. [Review](../../CLAUDE_REVIEW.md) · [Original eight-step score](../shapes/pt_shapes_01b.py) · [Short-form A/B control](../shapes/pt_shapes_02.py)

The triangle-family (simplex) reading recovers the encoded column for **60 of 77**, against **52 of 77** for plain log ratios. When the neighbour pool is redrawn by Claude's published recipe, the 95% difference interval reaches zero. Under Claude's stated decision rule, the evidence supports the shapes as a way of drawing the ladders. A long-form advantage over plain log ratios remains unestablished. The simplex does outperform standardized log energies and the frozen mat2vec control on this benchmark.

For A/B-paired labels, the simplex recovers **63 of 77**, against **54 of 77** for plain log ratios. Its gain survives the deletion check in the original cohort. Removing La–Lu brings that check down to zero. This is a reconstruction of known labels from existing data. None of these distances uses the value of the loop-wall cutoff.

## What was scored

Each query chooses its nearest **other** element among the same 77. A hit means their labels match. This statistic is a fraction of queries (micro-average), rather than an average giving every column equal weight. Starting with H–At and requiring nine energies yields F–At inclusive. Each ladder uses removals 1 through 9 and ratios 1 through 8. The source contains at least three elements per encoded long column here, so all 77 can score a hit. No method produced any tied nearest neighbours, even with a relative tolerance of 10⁻¹² and absolute tolerance of 10⁻¹⁴. All seven methods use the same query and candidate identities.

**Labels.** The long target is the mixer's stored `col`. Its separate lanthanide row gives Ce–Lu display positions 4 through 17, while La is in column 3. Thus Ce–Ti counts as a match in this particular score. For the requested short target, columns 11–17 merge with 1–7 respectively, and 8, 9, 10, 18 remain distinct. This gives eleven labels. The separate 62-element analysis drops La–Lu entirely and recomputes every nearest neighbour and the feature standardization. [Source layout](../build_ptable_data.py)

| Reading | Long, of 77 | A/B, of 77 | Long excluding La–Lu, of 62 | A/B excluding La–Lu, of 62 |
|---|---:|---:|---:|---:|
| Circle | 53 (0.688) | 55 (0.714) | 52 (0.839) | 54 (0.871) |
| Diamond | 52 (0.675) | 53 (0.688) | 51 (0.823) | 52 (0.839) |
| Cube | 48 (0.623) | 53 (0.688) | 47 (0.758) | 52 (0.839) |
| Simplex | 60 (0.779) | 63 (0.818) | 58 (0.935) | 61 (0.984) |
| Euclidean log ratios | 52 (0.675) | 54 (0.701) | 51 (0.823) | 53 (0.855) |
| Standardized log energies | 26 (0.338) | 30 (0.390) | 27 (0.435) | 30 (0.484) |
| mat2vec cosine | 36 (0.468) | 36 (0.468) | 37 (0.597) | 37 (0.597) |

## How much the difference moves

Each cell is **shape recall minus baseline recall**, followed by its central 95% spread under the original deletion-and-reselection recipe. Each of 10,000 paired replicates draws 77 queries with replacement, keeps the distinct elements, and finds new neighbours within that subset for every method. The same subset applies on both sides. Discarding duplicate draws changes the estimand and gives variable subset sizes. Treat the spread as sensitivity to which elements and neighbours remain. It is not a population confidence interval for discovering new elements. Feature maps stay fixed within a cohort across these perturbations.

| Labels | Reading | Euclidean log ratios | Standardized log energies | mat2vec cosine |
|---|---|---:|---:|---:|
| Long | Circle | +0.013 [+0.000, +0.044] | +0.351 [+0.200, +0.462] | +0.221 [+0.065, +0.367] |
| Long | Diamond | +0.000 [-0.021, +0.119] | +0.338 [+0.227, +0.490] | +0.208 [+0.093, +0.400] |
| Long | Cube | -0.052 [-0.111, +0.020] | +0.286 [+0.128, +0.420] | +0.156 [+0.000, +0.314] |
| Long | Simplex | +0.104 [+0.000, +0.220] | +0.442 [+0.260, +0.574] | +0.312 [+0.163, +0.460] |
| A/B | Circle | +0.013 [-0.020, +0.043] | +0.325 [+0.196, +0.457] | +0.247 [+0.152, +0.438] |
| A/B | Diamond | -0.013 [-0.043, +0.061] | +0.299 [+0.196, +0.449] | +0.221 [+0.137, +0.440] |
| A/B | Cube | -0.013 [-0.061, +0.041] | +0.299 [+0.176, +0.440] | +0.221 [+0.128, +0.426] |
| A/B | Simplex | +0.117 [+0.019, +0.213] | +0.429 [+0.277, +0.571] | +0.351 [+0.255, +0.533] |

A second calculation freezes all 77 neighbours and resamples paired hit differences over the 77 queries, keeping repetitions. For simplex versus log ratios the fixed-neighbour intervals are **[+0.013, +0.195]** long and **[+0.039, +0.195]** A/B. The discrepancy between these and the previous table matters: losing a reference element can change another query's nearest neighbour. These are descriptive resampling results for one finite periodic table. Selection among four shapes on this table and correlations among elements limit a prospective claim. All paired intervals, discordant counts, nearest-neighbour identities, and cohort-specific deletion spreads are in [results.json](results.json).

Against plain log ratios, ten long-label queries gain a hit using the simplex: Co, Ni, Cu, Rh, Pd, Ce, Ir, Pt, Au, Hg. Two lose one: Hf and Ta. Ce's win depends on the stored display convention. For example, the simplex pairs Ni with Pd while Euclidean logs pair Ni with Co. For Hf, plain logs recover Zr while the simplex chooses Tb. These concrete choices can be checked in the table.

## Data, calculations, and controls

- **Peel maps.** With eight ratios per element and `g = (z−1)/(z+1)`, the circle uses Poincaré-ball distance on `0.999 g/√8`. The diamond uses half the L¹ distance between log-ratio vectors. The cube uses half the range of pairwise differences in the logs of its sixteen face distances `(1−g,1+g)`. The simplex takes the range of the eight coordinate differences in `ln(ln z)`. Its value is unchanged if all eight positive log steps of either element are multiplied by the same constant. Thus its score tests a relative ladder profile.
- **Baselines.** Plain log ratios use Euclidean distance on the eight successive `ln(IE[k+1]/IE[k])` without standardization. The log-energy baseline uses the nine `ln IE[k]`, each coordinate centered and divided by its population standard deviation across the cohort. No labels enter either transformation. This is transductive descriptive scaling. Mat2vec uses one minus cosine of the 200-dimensional fixed text-derived vectors. A separate dot-product implementation reproduced both 36/77 scores. Known chemistry may already be encoded in its training literature. [Published feature provenance](published_features.md)
- **Shuffled-label control.** Each of 10,000 permutations preserves group sizes and the nearest-neighbour graph. For 77 queries the exact shuffle mean is Σ nᵍ(nᵍ−1)/(77×76), giving 0.04443 long and 0.08920 A/B. The empirical 99th percentiles for the four shapes are 0.130 long and 0.195 A/B. Every method, including both ionization baselines and mat2vec, exceeds its own shuffle's 99th percentile on both labels. Randomization tests whether neighbours carry label information; it does not decide which geometry wins.
- **Threshold cross-check.** Comparing all 77×9 input energies numerically against the pinned raw archive yielded **660 exact matches and 33 differences**. The largest relative difference was 4.26×10⁻⁷. The affected F ninth removal, for example, is 1103.118 eV in the table and 1103.1175302 eV in the archive. Recomputing from the raw values changed **zero** full-cohort nearest neighbours for every reading. Each discrepant symbol, removal index and pair of input values appears under `archive.differences`. [Table input](../v2/ptable_v2_data.json) · [Archive](../../../../data/element_thresholds_20261011.json.gz)

## Reproduce offline

Run `python3 compare.py` from this directory. The only third-party requirement is NumPy. The recorded run used Python 3.12 and NumPy 2.3.5 with PCG64 seed 20261123. The JSON fingerprints both source files and the published feature CSV. The four original long counts are executable assertions. A re-run on the same files and environment should reproduce `results.json` byte for byte.

# Which forward cutoffs survive the five-element extension?

**DERIVED.** Caesium supplies the first new constraint on the ordinary-rung window: its first removal followed by opening the xenon core gives z = 23.15745/3.89390572743 = 5.947100834227…, outside. The previous tightest outside ordinary step was carbon at 6.079534191962…. Nitrogen still supplies the tightest inside ordinary step. When bound-anion rungs are included, silver and silicon supply both extrema exactly as before.

| Rungs in hydrogen through caesium | Largest value classified inside | Smallest value classified outside |
|---|---|---|
| Ordinary, central | Nitrogen k=5, 5.639665400281… | Caesium k=1, 5.947100834227… |
| Ordinary, complete reported boxes | Nitrogen k=5, upper bound 5.639689262507… | Caesium k=1, lower bound 5.947085425274… |
| All, central | Silver k=0, 5.807902059840… | Silicon k=0, 5.866538776091… |
| All, complete reported boxes | Silver k=0, upper bound 5.808010272529… | Silicon k=0, lower bound 5.866514230542… |

With independent positive input boxes A±u, B±v, we compute the exact bounds (B−v)/(A+u), (B+v)/(A−u). For a strict outside test z>c, each inside row supplies a *lower* constraint on c and each outside row an *upper* constraint. Their extremal interval is left-closed and right-open. Here there are 1,529 central rungs, of which 44 are outside. There are 1,509 pairs of complete error boxes. The other 20 rungs, including antimony k=2 and 3, support central-value statements only without additional assumptions. These reported uncertainties are input widths. The test gives a conditional bound when true inputs lie within them. Silicon uses the paper's cross-element reference value. Isotope-specific EA substitutions are tabulated in [the previous analysis](../../batch10/robust/CUTOFF_INTERVALS_H_SN.md).

**DERIVED — fixed comparators.** Batch 10 had already reported c = 5, 5.8, 5.82, 5.83, 5.85, 5.9 and 6. This test reused the whole set without retuning. The comparator set was frozen before batch 11, though this analyst had already been told the caesium value. Of the seven, only c=6 disagrees with the reference wall on the 264 new rungs, misclassifying caesium k=1 even at both interval endpoints. The caesium interval is [5.947085425274…, 5.947116243180…]. On the full 1,529 central rungs, 5.82, 5.83 and 5.85 all agree with the wall. The reference wall does not uniquely identify its own numerical cutoff from these classes. An independent physical observable could test specificity.

| c | Disagreements on hydrogen–tin | New disagreements, antimony–caesium |
|---|---:|---|
| 5 | 7 | 0 |
| 5.8 | 1, silver anion | 0 |
| 5.82, 5.83, 5.85 | 0 at each | 0 at each |
| 5.9 | 1, silicon anion | 0 |
| 6 | 1, silicon anion | 1, caesium k=1 |

**DERIVED.** Measured by absolute distance in the forward ratio z from 3+2√2, silver k=0 remains the closest anion, distance 0.020525064906…. Among the five new elements, tellurium k=0 is closest at z=4.571476121012…, distance 1.256951003734…. Neither a fitted cutoff nor a binary label identifies an independent mechanism.

Reproduce from the repository root:

```sh
paper=research/2026-11-20-element-paper-loop-wall
python3 "$paper/batch11/robust/cutoff_holdout.py" data/element_thresholds_20261011.json.gz "$paper/batch10/robust/affinities_h_sn.csv" "$paper/batch11/ladder/batch11_rungs_detailed.csv"
```

The script reads the archive once, verifies its pinned SHA-256, takes the old documented affinity inputs and the four serialized new affinities, and compares all 264 central ratios and every available endpoint against the detailed new ledger before testing cutoffs.

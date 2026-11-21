# Carbon with nitrogen is uniquely closest among 427 archived adjacent pairs

For adjacent Z and Z+1 at fixed noble-core occupancy N, write M=g₁²+g₂²−1 with g=(b−a)/(b+a). Each input pair a,b comprises successive ionization energies at charges q=Z−N−1 and q+1. The carbon–nitrogen pair has N=2 and the first atomic number Z=6. The data contain 433 distinct faces and 427 consecutive pairs across six observed series. The admissible uncertainty boxes use exactly the tabulated energy ± uncertainty. The finite result concerns this margin, this archive, and this choice of adjacency.

For every allowed combination of rational energies in the boxes, the strict gap certified by Lean is

    |M(carbon,nitrogen)| < 31/10000 < 37/1000 < |M(any other listed pair)|.

The gap holds simultaneously even when all input energies vary. Allowing independent variation in shared faces only enlarges the admissible set. The two separating constants are simple exact rational witnesses inside the gap; none of the 1,732 source energy and uncertainty literals was rounded in the proof. The generic bound treats a reflection interval containing zero separately, so the lower power can be zero at an interior point.

The generated file is 19 KiB of text. Each core's list carries its starting atomic number; each row carries a, δa, b, δb as decimal rational literals in eV, in consecutive Z order. The verifier independently reopens the archive, scans every available charge, infers core occupancy from the charge, and compares every (N,Z)-keyed tuple to a fresh parse of the emitted Lean source. It compares every adjacent pair to the mixed-map CSV. Generation refuses to bridge a missing element. Independently of that input audit, Lean proves list length 427 and that the single target key is (2,6).

The generic statements powerBounds, certifiedCut and nearestFromCuts prove the implication from rectangular bounds to strict ordering, with rational input variables. Six finite kernel checks apply them to the whole dataset. The concrete theorem uniquelyNearest quantifies over both pair memberships and both admissible realizations. A wrong winner taking the argon-core potassium–calcium pair as lying inside the winner's envelope is proved false; a separate source mutation asserting it is true is rejected. These results quantify over rational perturbations; every catalogued endpoint is rational. The same interval argument applies mathematically to real perturbations since its extrema for the squared reflection occur at endpoint energies, or at zero when the interval crosses zero.

From the repository root and the pinned Lean 4.34.1 toolchain:

```sh
base=research/2026-11-20-element-paper-loop-wall/batch10
python3 "$base/nearest_lean/verify_nearest.py" data/element_thresholds_20261011.json.gz "$base/mixed_map/adjacent_pairs.csv"
```

The saved run lists the 13 public theorem declarations and all their axioms. Compiled modules and the negative control are written under a temporary directory.

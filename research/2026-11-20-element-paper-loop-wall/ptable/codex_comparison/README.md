# Periodic Table of Elemental Peels — Codex comparison edition

Jeromie Beasley's full v2.2 table opens as a standalone HTML file. Use **Compare neighbours** in the navigation, or append `#neighbours` to the file URL. The new view compares each element's first nine removal energies with those of its nearest neighbour under a selected rule. Each element can be queried under both scoring conventions.

The 77-element comparison uses the authored mixer’s column assignments, including its display columns for the lanthanides. The 62-element comparison removes La–Lu before finding neighbours. Reversing the label selector scores the same nearest neighbour against the other grouping. The paired and deletion intervals describe different resampling schemes and can give different conclusions. The upper wall line on the ratio chart provides a geometric reference. The nearest-neighbour contest does not test that cutoff.

The energy table shows both mixer and archive precision. Within the 77-element comparison, the archived precision changes 33 of 693 displayed energies and changes zero nearest neighbours. See the [paired comparison data](../fair_baseline/results.json) for each discrepancy and replay.

The builder verifies the hash of the table used by the benchmark, checks the embedded energies and group labels against those inputs, and recomputes every displayed hit count from the neighbour records. The standalone embeds the benchmark result hash. [Jeromie’s v2.2 source table](../v2_2) and the [prediction register](../../PREDICTIONS_REGISTER_20261123.md) remain available separately.

## Rebuild and check

From this directory, run `python build.py` with Python 3.10 or later. It reads the committed v2.2 standalone, the v2 element JSON and the neighbouring fair-baseline results. Run `node check.cjs` with jsdom available to Node for the offline DOM replay. The check exercises 84 combinations of cohort, group definition, element and distance rule, validates the stored results hash, and switches between the new view and the existing table. It does not exercise WebGL.

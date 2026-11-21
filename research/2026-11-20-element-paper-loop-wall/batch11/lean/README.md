# What cesium changes in the cutoff window

The new central inputs contain 265 archived successive energies, 260 ordinary comparisons, and four measured bound-anion affinities. Cesium rung one is the only new ordinary comparison outside the loop wall. Its exact ratio is 23.15745/3.89390572743, approximately 5.947100834. Its stated input box gives 5.947085425 to 5.947116243 (displayed rounding). It opens the xenon core. The antimony and cesium anion comparisons also lie outside. Tellurium and iodine anion comparisons lie inside. Xenon's first ordinary input has no preceding bound ground-state anion crossing.

**Ordinary comparisons alone.** A rational forward cutoff c fits a ledger if the strict test z>c reproduces every central wall label. The formal statements windowHydrogenTin and windowHydrogenXenon characterize every such cutoff as

    552.06741/97.8901 ≤ c < 392.09056/64.49352.

The first bound is nitrogen's helium-core opening. The old exclusive upper bound is carbon's. Adding cesium changes exactly that upper bound:

    552.06741/97.8901 ≤ c < 23.15745/3.89390572743.

The proof checks all 1,431 central ordinary crossings through xenon and all 1,485 through cesium, including the attaining witnesses. Thus six reproduces every ordinary central label from hydrogen through xenon. At cesium it first disagrees, at rung one.

**Ordinary plus anion comparisons.** The earlier silver–silicon central interval of approximately [5.807902060,5.866538776) survives. All new inside central rows lie below silver, and all new outside rows lie above silicon. For each of the 262 rows with complete uncertainties, the same comparisons hold using the relevant outer endpoint: inside compares its upper ratio with silver's central value, outside compares its lower ratio with silicon's central value. Thus the earlier narrower complete-box interval [7576259/1304450,6270500/1068863) also survives all newly specified boxes. The new antimony rungs two and three involve IE3 with unspecified uncertainty. Their central classifications hold, while their rectangular comparisons remain missing. The earlier 18 incomplete hydrogen–tin boxes remain subject to their earlier qualifications. No absent uncertainty is replaced by zero.

The verifier checks the pinned archive hash, compares all new energy literals with the delivered CSV, and independently reparses every new ordinary energy and uncertainty literal from the generated Lean source. The compact historical lists are generated directly from the same validated archive. Run from the repository root with Lean 4.34.1:

```sh
base=research/2026-11-20-element-paper-loop-wall/batch11
python3 "$base/lean/verify.py" data/element_thresholds_20261011.json.gz "$base/ladder/batch11_sb_cs.csv"
```

The negative control falsely predicts that the cesium opening exceeds six. The argument is arithmetic on encoded thresholds and their stated uncertainty boxes. It does not assign a physical transition to a chosen classifier cutoff.

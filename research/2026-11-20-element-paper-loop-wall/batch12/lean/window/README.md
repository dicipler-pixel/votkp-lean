# Which numerical cutoffs still reproduce the full ledger through neodymium?

The equal-face wall fixes a forward reference ratio of 3 + 2√2 before the comparison. A separate question asks which rational cutoffs (c) make the **same calls on this finite ledger** when a ratio is classified outside exactly if (z>c). We check two datasets. One has one central value per rung. The other contains every value in the independent rectangle of two quoted input energies, whenever both inputs have a reported uncertainty. For each cutoff the theorem tests it against every row in the chosen dataset.

| Ledger | Rungs | Inclusive lower bound | Exclusive upper bound | Rows attaining the endpoints |
|---|---:|---:|---:|---|
| Ordinary, central | 1,770 | 55206741/9789010 | 771915000000/129796857581 | Nitrogen k=5, caesium k=1 |
| Ordinary, complete boxes | 1,751 | 55206749/9788970 | 57893475000/9734764319 | Nitrogen k=5, caesium k=1 |
| Ordinary and anion, central | 1,819 | 3788117/652235 | 20379200/3473803 | Silver k=0, silicon k=0 |
| Ordinary and anion, complete boxes | 1,799 | 7576259/1304450 | 6270500/1068863 | Silver k=0, silicon k=0 |

The lower endpoint is the maximum inside value. At equality the classifier still calls that rung inside, so the lower endpoint is included. The upper endpoint is the minimum outside value. At equality that rung would be called inside, making the upper endpoint exclusive. For a complete input rectangle the lower and upper possible ratios are ((B-v)/(A+u)) and ((B+v)/(A-u)), with positive inputs. The strict squared-reflection wall classification is stable on all 1,799 complete rectangles, including any rectangle containing (z=1). The proof quantifies over rational choices of both inputs. The finite end values in this table are exact.

Across 1,819 central rungs, 49 are outside: eight ordinary steps and 41 anion steps. There are 49 anion rungs in total. Technetium’s archived accompanying affinity table lists an estimated central affinity with unspecified uncertainty. The theorem names all 20 missing-box keys. None is assigned zero uncertainty. Archive grades and the selection of historical reference affinities stay as documented.

**Directed uncertainty test.** The condition that would refute strict forward sign everywhere is a single admissible complete box containing (z=1) or less. Of the 1,799 complete ratio intervals exactly one has a lower endpoint at one, and none falls below it. That one is neodymium k=10, which allows ((160,160)) eV at the joining edges of two T-grade ranges. Its central (Gamma) is (1/20). The other 1,798 complete rectangles stay strictly forward. Quantifying over all 1,819 rectangles would require widths for the missing pairs.

**Cutoff control.** The exact upper and lower bounds for the combined complete set are about 5.808010273 and 5.866514231. All three fixed values 5.82, 5.83 and 5.85 reproduce every central label for every complete box. The comparators 5.8 and 5.9 fail. Agreement alone leaves a continuum of admissible numerical cutoffs and cannot identify a unique physical wall.

The proof imports the earlier ordinary central windows and reconciles their energy literals with the archive. The Python entry point checks 1,830 ionization energies and 1,830 uncertainty fields, including explicit missing widths. It reads the previously documented affinities and preserves the original wavenumber-to-eV conversion for selenium. On the Lean side, `stabilityMeaning` gives the squared-wall call for each admitted input pair. The separate theorem `sharpRangeWindow` characterizes every strict forward cutoff that fits a ledger of intervals.

Run with Python 3 and Lean 4.34.1 from the repository root:

```sh
paper=research/2026-11-20-element-paper-loop-wall
python3 "$paper/batch12/lean/window/verify_window.py" --lean /path/to/lean
```

[Batch 11 cutoff analysis](../../../batch11/robust/CUTOFF_H_CS.md) · [Historical affinity choices](../../../batch10/robust/affinities_h_sn.csv) · [New affinity choices](../../ladder/affinities.csv)

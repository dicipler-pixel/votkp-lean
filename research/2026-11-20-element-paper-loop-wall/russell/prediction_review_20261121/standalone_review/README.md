# Native-browser check of Claude's standalone periodic table
Reviewed the [single-file release at 3fad6267](https://github.com/dicipler-pixel/votkp-lean/blob/3fad6267f5f980f6378371d0c02b95c9a71d00e1/research/2026-11-20-element-paper-loop-wall/ptable/Periodic_Table_of_Elemental_Peels_v1_20261121_standalone.html). The release is an offline packaging change. The embedded parsed JSON equals the original table's JSON at 6068b3f, including its 3,655 removal energies and 3,570 ordinary steps.

**What ran.** The standalone page loaded from an isolated local file in Chromium headless 142.0.7444.175 on Linux using SwiftShader software WebGL. Browser networking was disabled, with a separate route recording attempted remote requests. All nine views opened, 85 elements appeared, and all 12 selected detail drawers opened and closed with a live WebGL context. With reduced motion enabled, dragging the strontium chain changed the canvas image; two subsequent frames after release matched exactly. No JavaScript exceptions occurred. The only attempted remote resource was the optional Google Fonts stylesheet, which was blocked. This test validates the packaged interactive field on this browser. It covers software rendering and cannot certify performance on other GPUs or mobile devices.

**Scientific review still applicable to this file.** 1,562 ordinary links have squared reflections below 0.0009 and are drawn with a 0.03 relative-radius floor. Quoted ideal uptake and the broad affinity/anion wording persist. The drawers for samarium, dysprosium, thulium and polonium all show the identical absence wording despite their differing evidence situations. The calcium, strontium and barium drawers do correctly have numerical bound-anion rungs; the earlier inconsistency concerns the table's explanatory claims. The original nine-view data review at 6068b3f applies to this embedded dataset. This offline package should receive credit separately from any subsequent scientific revisions.

Reproduction requires Node, Playwright, a Chromium installation with working WebGL, and the standalone file extracted from the pinned Git commit. Set CHROMIUM to its executable and run:

    node browser_check.cjs /path/to/Periodic_Table_of_Elemental_Peels_v1_20261121_standalone.html
    python check_v1_data.py /path/to/votkp-lean

The first command can optionally save the final strontium field frame via the CANVAS_PNG environment variable. Screenshots only establish rendering and interaction; all numerical comparisons use the actual embedded data.

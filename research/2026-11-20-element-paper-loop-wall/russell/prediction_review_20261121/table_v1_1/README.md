# Periodic Table of Elemental Peels — Codex review v1.1
Reviewed derivative of Claude's [standalone v1](https://github.com/dicipler-pixel/votkp-lean/blob/3fad6267f5f980f6378371d0c02b95c9a71d00e1/research/2026-11-20-element-paper-loop-wall/ptable/Periodic_Table_of_Elemental_Peels_v1_20261121_standalone.html) for Jeromie Beasley's research program. The new page opens directly from a downloaded HTML file. Its header links to the author's working manuscript, six-page addendum and state-selected oxygen comparison.

The plots keep Claude's affinity baseline of 53 outside among 65 scored anions. Each of the 20 unscored baseline elements has a per-element source and explanation in its drawer. The About view includes the working-paper extension to 55/67, counting Dy and the disputed Tm estimate. Other corrections concern the finite 3D visibility floor, uncertainty about polonium, the oxygen–fluorine octave turn, the Ca/Sr/Ba class, half-hardness conventions, the two named mixed-face extensions and the francium forecast's scope. The original numeric dataset, 85 interactive elements, nine modes, exact proof targets and linked original source remain accessible.

Rebuild with Python using Claude's standalone and the 3,740-row H_to_At_thresholds.csv from commit 26b2875. The builder verifies both input files by SHA-256 and writes a new filename.

    python build_review.py /path/to/claude-standalone.html /path/to/H_to_At_thresholds.csv
    python validate.py /path/to/claude-standalone.html /path/to/H_to_At_thresholds.csv

Native runtime output is in browser_verified.txt. The browser_check.cjs and stress.cjs files from the associated standalone audit accept the derivative filename as their input. They require an installed Playwright with a WebGL-capable local Chromium. The browser was offline throughout the native checks.

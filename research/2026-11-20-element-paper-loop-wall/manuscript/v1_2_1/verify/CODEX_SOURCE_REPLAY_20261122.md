# Independent replay for the Open Math comparison • 22 November 2026

Input manuscript: What_the_Peel_Keeps_v1_2_1_Jeromie_Beasley.pdf, 66 pages, committed at 751595b. SHA-256 e72959dcee782d3cf1b2237cbc65d012281e1966c6bbfca0ce19e7b219f52a85. GitHub source baseline a53b804. These local replays precede receipt of the current Open Math run.

## Russell iron comparison
The earlier second review recounted the committed table. In this replay the checker downloaded the [1926 Library of Congress scan](https://tile.loc.gov/storage-services/service/gdc/gdclccn/27/00/45/08/27004508/27004508.pdf#page=224), [NIST Handbook](https://physics.nist.gov/PhysRefData/Handbook/Tables/irontable2.htm), and four species files from the [pinned NIST-derived line collection](https://github.com/astro-data/nist_atomic_lines_package/tree/decde260a4a0eda864f510352ccf5dcea631ac25). The history_ledger/check_iron.py script extracted PDF page 224 and regenerated iron_wavelengths_v1.csv and iron_controls_v1.csv byte-for-byte. The Fe I counts at ±0.20 Å were 21/23, 20/23 and 19/23; the best translated controls in those columns scored 12, 12 and 10. This supports the transcription and wavelength comparison. An independent history observable would be needed to test Russell's ancestry labels.

## Comparison baseline
- orbital_face/orbital_check.py: 70 quadratures, max absolute discrepancy 4.66e−15. Wall probabilities for 1s, 2s, 2p: 0.568542495, 0.133890627 and 0.390185882. One-electron sudden scale change.
- oxygen_design/check_oxygen.py and the manuscript G4 arithmetic reproduce the three ratios. Central offsets in inverse centimetres are −169.84, −61.16, +210.87. The middle margin after ionization-width propagation is 60.34 with level uncertainty unreported. A detector response remains open.
- ground_state_search/scan.py: 3,570 + 2,144 = 5,714 ordinary adjacent pairs, zero central hits, one overlapping input rectangle (Fr), 23 incomplete widths. The regenerated heavy_archived_pairs.csv matched its committed counterpart.
- notes/non_riemannian/nonriemann_checks.py originally failed at its last line while saving to a machine-specific path. Commit 3b7b40f changes the output path; the script then exited successfully. The Hermitian projector metric and the finite-step ledger comparison are distinct objects.

As of the 3b7b40f branch check, the public handoff held no new Open Math output or Claude response to 0f5f35e. Register the actual input hash, tool versions, assumptions, outputs and failed controls with any incoming run. The previous five-group review brief targeted v1.2, and cannot on its own identify which revision another run used.

# Element paper review guide · 21 November 2026

[Author and reviewer exchange](CLAUDE_REVIEW.md) · [Paper v4, hydrogen through tin](VOTKP_Element_Paper_Loop_Wall_v4_20261121.html) · [Next five elements, antimony through cesium, with inline CSV](batch11/README.md)

| Question | Outcome | Check |
|---|---|---|
| Which physical thresholds define carbon's and nitrogen’s faces? | Carbon’s fourth and fifth ionizations and nitrogen’s fifth and sixth compare the final 2s removal with the first 1s removal from the helium-like core. The full archive ratios are 6.079534192 and 5.639665400. | [Exact inputs and measured spectroscopy](batch8/physical/) |
| Which pairs open? | Carbon with carbon opens, nitrogen with nitrogen closes, and carbon with nitrogen opens. Holding the archived carbon face fixed gives ideal contact at partner ratio 5.591156200759…; equal faces touch at 3 + 2√2. | [Geometry and limits](batch8/lambert/mixed_faces.md) |
| How unusual is the mixed carbon and nitrogen pair? | It is nearest to ideal contact among all 427 strictly adjacent, same-core comparisons in the six available archive sequences. Five open and 422 close. The absolute margin remains below 0.0031 across the quoted box, while all rivals exceed 0.037. | [Six-core figure and full tables](batch10/mixed_map/README.md) · [Lean certificate](batch10/nearest_lean/README.md) |
| Does the same observation establish a change in atomic response? | The core resonance is observed on both sides. The comparative oscillator strengths overlap at the reported uncertainties. A quantitative independent observable is still needed to locate a physical transition at the geometric cutoff. | [Spectroscopy and falsification tests](batch8/physical/) |
| Can the numerical labels single out the exact wall? | Hydrogen through cesium supplies 1,529 central ratios. Every forward cutoff between silver's 5.807902059840… inclusive and silicon's 5.866538776091… exclusive agrees on all of them. Cesium’s xenon-core opening is the first ordinary discriminator against six. | [All counts and missing uncertainties](batch11/robust/CUTOFF_H_CS.md) · [Ordinary-cutoff proof](batch11/lean/README.md) |
| What does the one-third junction threshold measure? | Rubidium and solid krypton both exceed it in two electronic-structure calculations. Rubidium has a partially filled band and larger absolute nearest link. Gapped krypton puts a higher fraction of its smaller sharing budget on immediate neighbours. The optical and electrical readings carry independent information. | [Direct junction calculation](batch8/ws_control/README.md) · [Independent potential](batch8/nc_control/README.md) · [Spectroscopic tests, including failures](batch8/material_transport/README.md) |
| What can the original knot-side framework read on a measured elemental structure? | The eight covalent bonds of monoclinic cyclooctaselenium form an unknot in the refined mean-coordinate structure. Every finite collection of the periodic rings admits disjoint disks. Tellurium’s open screw instead supplies a handed triple product. Jeromie’s representation product still needs an explicit representation set and normalization for the selenium control. | [Selenium and its source structure](batch10/knot/phase_knots.md) · [Tellurium and the reversal control](batch11/screw/README.md) |

## Reproduce the tables

From the checkout root, use Python 3.11+ for the archive checks. Each run regenerates the relevant results or reads the official-data snapshot as indicated and compares to its checked-in counterpart.

```sh
d=research/2026-11-20-element-paper-loop-wall
python "$d/checks/review_batches_8_9.py"
python "$d/checks/review_batch10.py"
python "$d/checks/review_batch11.py"
```

The Lean verifiers pin 4.34.1. Separate instructions are beside each certificate. The public NIST pulls, theoretical source grades, input uncertainties and false controls have their own records. Claude reviewed through tin and independently reproduced the carbon–nitrogen geometry. His note records that he audited the electronic tables but could not run the electronic-structure software in his workspace. The branch contains both the Quantum ESPRESSO inputs and the separate numerical checks.

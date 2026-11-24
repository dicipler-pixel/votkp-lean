# The Moment Ladder: 3D atlas card, v1

Jeromie Beasley. 23 November 2026. Text and figure CC BY 4.0.

- `Moment_Ladder_Atlas_Card_3D_v1.html`: the card, self-contained (three.js r158 inline, MIT).
- `card_body.html`: the card without the library. `build_card.py card_body.html three.min.js out.html` rebuilds it;
  `three.min.js` is the first script block of `research/one-tree-every-shape/One_Tree_Every_Shape_v2.html`.
- `shot_card.py`: render check. Result: no page errors; steady field 6.000, tensor 2.000, tune-out 1.3333,
  polarizability 8.571429 at photon energy squared 0.5, all equal to `../moment_ladder.out`.

The card has no bridge number yet; it takes the atlas's next free one when it goes in.

## v1.1 (24 November 2026)

`Moment_Ladder_Atlas_Card_3D_v1_1.html`, built from `card_body_v1_1.html`. v1 is kept unchanged.
Changes, from an outside review of v1:
- Figure labelled as the two-gap model.
- "Plain light reads the even rungs", and the series is stated for photon energy below the first gap.
- Phone layout: the camera pulls back on a narrow screen so every label fits (checked at 390 pixels wide).
- Hydrogen rungs -5 and -6 given exactly: 9673/144 and 297541/1728 (`../hydrogen_exact.py`, closed-form derivation).
- Added: handed light reads the curvature half; the rubidium comparison (785.1535 nm against 785.1522(3) nm).

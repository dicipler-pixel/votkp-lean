# The Moment Ladder: 3D atlas card, v1

Jeromie Beasley. 23 November 2026. Text and figure CC BY 4.0.

- `Moment_Ladder_Atlas_Card_3D_v1.html`: the card, self-contained (three.js r158 inline, MIT).
- `card_body.html`: the card without the library. `build_card.py card_body.html three.min.js out.html` rebuilds it;
  `three.min.js` is the first script block of `research/one-tree-every-shape/One_Tree_Every_Shape_v2.html`.
- `shot_card.py`: render check. Result: no page errors; steady field 6.000, tensor 2.000, tune-out 1.3333,
  polarizability 8.571429 at photon energy squared 0.5, all equal to `../moment_ladder.out`.

The card has no bridge number yet; it takes the atlas's next free one when it goes in.

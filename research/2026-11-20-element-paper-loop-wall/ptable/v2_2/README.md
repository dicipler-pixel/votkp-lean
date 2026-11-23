# Periodic Table of Elemental Peels v2.2 - Jeromie Beasley, 23 Nov 2026 (built with AI assistance)

v2.1 kept whole, plus one new view, **Shapes**:
1. Every removal step and anion rung carried from the disk onto a triangle, square, diamond or hexagon (chart that keeps
   angles, or stretched to the faces). The wall moves with the shape; the counts never change: 8 of 3,570 steps and
   53 of 65 baseline anion rungs outside in every shape (checked in the browser).
2. The address on the diamond: each element at (anion rung Gamma_0, first core opening Gamma), one edge per book, the wall on
   each edge; hover gives the direction (B (-) A) and size (A (+) B) diagonals.
3. Which shape groups the columns (H to At, 77 elements, first 8 steps): circle 0.688, diamond 0.675, cube 0.623,
   triangle family 0.779, raw energies 0.052; no shape beats the circle beyond its bootstrap spread (PT-SHAPES-01B).
Each element's drawer gains "On the shapes": its nearest element on each shape.
build22.py makes this file from v2.1; shapes_view.js is the added code.

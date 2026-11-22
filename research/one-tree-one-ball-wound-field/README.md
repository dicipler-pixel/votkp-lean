# One Tree, One Ball: the wound field (new ball project, 22 Nov 2026)

Jeromie Beasley. AI-assisted (Claude). Built on the real One Tree, One Ball ball (hyperboloid frame, Poincaré-ball view, six-arm tree of peel steps); none of the earlier page's points of interest are carried over.
Input: Ink's note on the Koryak/Levin thread (screened Laplacian, V_mid/V_edge = 1/cosh(L/2 lambda)).

Four eyes: (1) each cell is one peel step, 2 cosh(theta) = 2 + g_m/G, field = cosh of the place on the ladder; (2) the shape of the wound (long cut 1/cosh, round in a sheet 1/I0, round in a body x/sinh); (3) healing walks the edge in; (4) drugs move the edge, not the wall (prediction, untested).

WOUND-BALL-01 (`wound_ball_check.py`, output `.out`):
- cell chain solved directly = cosh(n theta)/cosh(N theta) to 3e-14;
- centre field 1/cosh(rho) = (1 - Gamma^2)/(1 + Gamma^2), Gamma = tanh(rho/2) the edge's ball radius;
- the wall: arccosh 3 = ln(3 + 2 sqrt 2), so the critical shell for one-third survival is exactly Gamma^2 = 1/2; width 3.5255 lambda;
- slab / disc / ball closed forms against direct radial solves, 6 digits.
Measured inputs quoted on the page: wound-edge lateral field 115-180 mV/mm in a band about 1 mm wide (Nuccitelli et al., Wound Repair Regen 16:432, 2008); skin battery 20-50 mV (Barker et al. 1982, as cited there). Lambda itself not measured.

## v2 (22 Nov 2026, after Ink, Lean Green and Gray Trace checked v1)
v1 is kept unchanged. v2 adds a Map slider showing both ways of putting the cable into the ball, side by side:
- page map: edge at display radius Gamma = tanh(rho/2); the wall Gamma^2 = 1/2 keeps 1/3 of the edge field at the centre, width 3.53 lambda;
- physical map (Ink and Lean Green): Gamma = tanh(rho), the cable's normalized input admittance; one segment of length d has trace 2 cosh d and moves a point 2d; the wall keeps 1/sqrt2, width 1.76 lambda.
The wall is labelled an analogy, not a biological boundary. Wording fixes from Lean Green: "display radius"; "largest width retaining the selected centre fraction in this model". Manicka and Levin's tissue-wide field noted as the term that could reach past lambda. Which map the page keeps is Jeromie's call.

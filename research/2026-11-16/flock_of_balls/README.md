# Flock of Balls on the Field — v1 (16 Nov 2026)

Jeromie Beasley, AI-assisted. Whole Light at the Hypersurface balls on one field (3, 4 or 7): A at the centre, the others one peel step
out along the arms. Two pages, one on the Mixer v2 ball and one on the white ball.

What changed against Three Balls on the Field v1 (checked first in `../tb/gap_clock_check_01.out`: the link there was an instant jump,
all balls shared one clock, and the gap between faces did not enter the link):

- **The gap is real.** A link is a stretch of field of hyperbolic length d; light crosses it at speed 1 and meets the faces on the way
  (Γ = tanh(step/2), returns Γ², passes 1 − Γ²). An arm–arm link crosses the two faces of the centre cell; where they stand apart
  (g > 1) the light between them only tunnels, sech(κδ). **HYPOTHESIS: gap layer.**
- **A clock per ball.** Centre rate 1; a ball one step out runs at 1/z. **HYPOTHESIS: clock ratio z.** "All equal" is kept for comparison.
- **Ball fields.** Default: held by the faces toward rest, changed only by light that arrives. **MODEL CHOICE.** The delayed face push is
  kept as an option; under it rest is unstable (K6b), and it is not energy-booked.
- **Books.** Light in the balls + light in the gaps = 1 on every step (exact rotations).

Checks, kill lines written before the run (`fl_check_01.js`, `fl_check_01.out`): K1 travel time, K2 books (≤ 1e-12), K3 one face,
K4 gap and the wall, K5 clocks (ratios 3, 5, 7), K6 rest, K7 step size: all hold. Exploration: the flock does not lock in these runs,
with clocks at z or equal.

Page: balls 3 / 4 / 7, kick any ball, zoom by percent (wheel, buttons, typed), move over the field (arrow keys or WASD, Q/E up and down,
shift-drag or right-drag, double-click a ball, "Go to"), every view its own switch with All / None, the ball's own eyes (Mixer ball) and
layers (white ball) on together, numbers in a drawer on the left. Nothing sits on the right of the screen.

Not in this version: the electron sea (it needs its own travel time); energy of light in transit is booked as light count only; gap
lengths are held at the mean steps.

Build: `python3 fl_build_v1.py` (hosts are the two ball pages held inside Two Balls, Linked v1). Page test: `fl_shot_v1.py`.

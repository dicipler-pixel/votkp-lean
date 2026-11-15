# SCRIPT: BALLFILM2-NARRATION-01
# Narration and action cues for the film of the two knot eyes of Balls in One Ball, Mixer v4. Same beat format as BALLFILM-NARRATION-01.
SEGMENTS = [
 ("intro", "knot", [
  ("For nearly ninety years it was believed that the cost of untying two knots tied in one rope is the sum of the two costs.", [], []),
  ("In twenty twenty five Mark Brittenham and Susan Hermiller showed that it is not. Here is that result inside the ball, in two eyes.", [('tw','ka',90,180,0.0,1.0)], ['g']),
 ]),
 ("knot", "knot", [
  ("Eye eight. A knot, its mirror, and what a step can see. This is the torus knot of two strands and seven crossings, called seven one, round the centre of the ball.", [('js',"MIXER_API.set('kn',7);MIXER_API.set('kc',0);MIXER_API.set('kt',2);MIXER_API.set('ka',90)",0.0)], []),
  ("The crossings slider runs from three to thirteen. Three crossings is the trefoil.", [('tw','kn',7,13,0.0,0.35),('tw','kn',13,3,0.35,0.75),('tw','kn',3,7,0.85,1.0)], ['g']),
  ("Now the run side. Take one step of ratio t up the gold arm, and seven steps up the same arm. The Alexander polynomial of the knot is the comparison of where those two balls land. Four routes give the same value on the left: the polynomial itself, a ratio of hyperbolic cosines, the two balls on the arm, and the cubic from the Knot Mirror paper.", [('tw','kt',2,9,0.1,0.45),('tw','kt',9,1.01,0.45,0.8),('tw','kt',1.01,2,0.8,1.0)], ['g']),
  ("Reverse the step, t to one over t, and the value does not move. Switch to the mirror knot and it still does not move. The Alexander polynomial is blind to the hand.", [('ck','button[data-m="-1"]',0.45),('ck','button[data-m="1"]',0.9)], ['tap']),
  ("The turn side is the ring. Sweep the angle from zero to a half turn. The same expression now has zeros, at one seventh, three sevenths and five sevenths of the half turn. Each zero passed adds two to the signature. At the end the signature is six.", [('tw','ka',90,0,0.0,0.15),('tw','ka',0,180,0.2,0.9)], ['g']),
  ("For the mirror knot it is minus six. So the signature sees the hand, and the polynomial does not.", [('ck','button[data-m="-1"]',0.1),('ck','button[data-m="1"]',0.9)], ['mir']),
  ("Each crossing change removes two crossings. Seven, five, three, then no knot at all. Three changes, which is half the signature, and no fewer will do.", [('tw','kc',0,3,0.15,0.6)], ['arc']),
 ]),
 ("sum", "sum", [
  ("Eye nine. Knot plus mirror: five, not six. First join two copies of seven one with the same hand. The signatures add to twelve, and half of twelve is six. So six changes are forced.", [('js',"MIXER_API.set('sc',0)",0.0),('ck','button[data-j="1"]',0.02)], []),
  ("Make five changes and a trefoil is still left. One more is needed. Nothing is saved.", [('tw','sc',0,5,0.0,0.6)], ['g']),
  ("Now join the knot to its mirror. The signatures cancel to zero. The polynomial and the determinant are the same as before, forty nine for both sums. They cannot tell the two sums apart. And the signature no longer forbids anything.", [('js',"MIXER_API.set('sc',0)",0.0),('ck','button[data-j="0"]',0.03)], ['g']),
  ("Brittenham and Hermiller redrew the mirror sum as a braid of five strands and twenty crossings. I checked that braid here: signature zero, determinant forty nine, and the Alexander polynomial of seven one, squared.", [('ck','button[data-b="1"]',0.05)], ['tap']),
  ("Change the two gold crossings. The knot becomes K fourteen a, one eight six three six. The program Snap Pie identifies it by that name.", [('tw','sc',0,2,0.05,0.4)], ['arc']),
  ("Three more changes: to K fifteen n, eight one five five six, to K twelve n, four one two, and to the unknot. Those three are as published. I did not run them again here. Two, and one, and one, and one. Five, not six.", [('tw','sc',2,5,0.05,0.55)], ['g','tap']),
  ("Why can the mirror pair save a change when the same hand pair cannot? The signature is the only one of these counts that sees the hand, and in the mirror sum it cancels. That much is proved. Whether five is the true cost, or whether fewer will do, is still open.", [], []),
 ]),
 ("outro", "knot", [
  ("The counterexample belongs to Mark Brittenham and Susan Hermiller. The ball, the tree and the two eyes are from Balls in One Ball, mixer version four.", [('js',"MIXER_API.set('kc',0);MIXER_API.set('ka',180)",0.0)], ['g']),
 ]),
]

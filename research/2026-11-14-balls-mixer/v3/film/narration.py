# SCRIPT: BALLFILM-NARRATION-01
# Narration and action cues for the film of Balls in One Ball, Mixer v3. One segment per eye, in film order.
# Each segment is a list of beats: (text, actions, narrator cues). Times inside a beat are fractions of that beat.
#   actions: ('tw', param, v0, v1, f0, f1)  slide a slider      ('js', code, f)  run page code      ('ck', selector, f)  press a button
#   cues:    'g' hand rises for the beat    'tap' cane tap near the end    'arc' arc to the centre of the ball    'mir' mirror turn
# Plain scientific English. Words the voice says wrongly (heteronyms) are avoided.
L = 5.828427124746190
SEGMENTS = [
 ("intro", "tree", [
  ("This is Balls in One Ball. One hyperbolic ball holds a whole tree of balls. Every ball has six arms, and each arm is one peel step of ratio z.", [], []),
  ("A step of ratio z sits at gamma, which is z minus one over z plus one, and its length is the logarithm of z.", [('tw','zt',5,2,0.0,0.5),('tw','zt',2,5,0.5,1.0)], ['g']),
  ("Seven eyes follow. In each one the sliders move, the numbers on the left are computed from the step matrices as you watch, and I will say why each number comes out the way it does.", [], []),
 ]),
 ("field", "field", [
  ("Eye one. Four balls in one ball. The centre, and three neighbours, I, J and K, one step away along three axes. Their step ratios are three, five and seven, so they sit at gamma one half, two thirds and three quarters.", [], []),
  ("Slide the ratio of ball I across its full range. A larger ratio is a longer step, so the ball moves out toward the rim. The rim is the ground. It is infinitely far away, and no finite step reaches it.", [('tw','zI',3,13,0.0,0.4),('tw','zI',13,1.5,0.4,0.8),('tw','zI',1.5,3,0.8,1.0)], ['g']),
  ("The coloured cap in front of each ball is its face: the plane halfway between that ball and the centre. Two faces either cross or stand apart. One number decides it. Call it g: the hyperbolic sine of half of one step, times the hyperbolic sine of half of the other.", [], []),
  ("When g is below one the faces cross, at the angle whose cosine is g. That is an overlap. With ratios three and five they cross at fifty eight point nine degrees. When g is above one the faces miss, and the gap between them is the inverse hyperbolic cosine of g. With five and seven the gap is zero point one six eight.", [('tw','zJ',5,13,0.3,0.55),('tw','zJ',13,1.5,0.55,0.85),('tw','zJ',1.5,5,0.85,1.0)], ['g','tap']),
  ("Why does a gap open at all? In flat space two planes at right angles always meet. Here space spreads so fast that two planes far enough out never meet. Overlap holds two balls together. The gap keeps them apart.", [('tw','zK',7,13,0.0,0.3),('tw','zK',13,1.5,0.3,0.75),('tw','zK',1.5,7,0.75,1.0)], ['arc']),
  ("The moving points show flow along each arm, out from the centre or in from the rim. Turning the flow around changes no size on this page.", [('ck','button[data-d="0"]',0.25),('ck','button[data-d="1"]',0.5),('ck','button[data-d="0"]',0.8),('ck','button[data-d="1"]',0.9)], ['g']),
 ]),
 ("pair", "pair", [
  ("Eye two. Two neighbours, both at ratio five. Their faces cross, with g equal to zero point eight exactly. The gold path is a square of four steps: out along one arm, out along the other, then each step undone.", [('js',"MIXER_API.set('zI',5);MIXER_API.set('zJ',5);MIXER_API.set('np',40)",0.0)], []),
  ("On a flat sheet that square would shut. Here it does not. It is a turn of one hundred and forty seven point four eight degrees about the white point, where the two faces cross.", [('tw','np',1,120,0.1,1.0)], ['g']),
  ("The reason: each step is two mirror flips, and two mirrors that cross at an angle make a turn by twice that angle. Four steps give four times the crossing angle. Repeat the square and the centre is carried round a ring. It never goes further than three point five two five five. The walk is held.", [('tw','np',120,40,0.0,0.3)], ['tap']),
  ("Now raise one ratio from five to seven. The crossing angle shrinks, the white point slides outward, and at g equal to one the faces let go. Past that, the square is no longer a turn. It is a run, of zero point six seven two nine each pass, and the centre is carried off toward the rim. Nothing comes back.", [('tw','zJ',5,7,0.05,0.75)], ['g','arc']),
  ("Bring it back to five, and reverse the flow on one arm. Every size stays the same, and the sense of the turn flips. Size is blind to direction. Handedness is not.", [('tw','zJ',7,5,0.0,0.2),('ck','button[data-d="0"]',0.3),('ck','button[data-d="0"]',0.62),('ck','button[data-d="0"]',0.85)], ['g']),
  ("Slide both ratios across the full range and the same rule decides each case.", [('tw','zI',5,1.5,0.0,0.2),('tw','zI',1.5,13,0.2,0.5),('tw','zJ',5,13,0.5,0.7),('tw','zJ',13,5,0.7,0.85),('tw','zI',13,5,0.85,1.0)], []),
 ]),
 ("close", "close", [
  ("Eye three. When the balls lock into a lattice. Now each arm takes the same step, and each ball reached in up to five steps is drawn: four thousand six hundred and eighty seven paths.", [], []),
  ("The faces cross at an angle alpha, and three hundred and sixty over alpha balls fit round each edge. When that count is a whole number the turned copies land exactly on each other. Five round an edge. Six round an edge, at z equal to two plus root three. Eight round an edge. At these steps the smallest distance between two balls stays at one full step. The tree has become a lattice.", [('ck','button[data-q="0"]',0.3),('ck','button[data-q="1"]',0.47),('ck','button[data-q="2"]',0.66)], ['g','tap']),
  ("At ratio three the count is five point one. Not whole. So new balls keep landing between old ones, and by depth five two of them are only zero point zero two three apart. Ratio five does the same: zero point four two six. Whole number ratios are not the locking steps.", [('ck','button[data-q="3"]',0.0),('ck','button[data-q="4"]',0.62)], []),
  ("On the line, where gamma squared is one half, the faces only touch. Past it, at ratio seven, no ball lands on any other and each keeps its gap.", [('ck','button[data-q="5"]',0.0),('ck','button[data-q="6"]',0.5)], ['arc']),
  ("Sweep the whole slider and the three states pass by in order: lattice points, crowding between them, and then open spacing past the line.", [('tw','zq',1.5,9,0.0,0.85),('ck','button[data-q="0"]',0.95)], ['g']),
 ]),
 ("tree", "tree", [
  ("Eye four. The tree and its level shells. Nine hundred and thirty seven balls, four steps deep, at ratio five.", [('js',"MIXER_API.set('zt',5)",0.0)], []),
  ("The gold shells are the levels. L steps straight out along one arm reach gamma of z to the power L. The reason is that ratios multiply while lengths add: L steps of ratio z make one step of ratio z to the L. Balls reached by turning from arm to arm fall inside their shell.", [('tw','zt',5,1.5,0.1,0.4),('tw','zt',1.5,9,0.4,0.8),('tw','zt',9,5,0.8,1.0)], ['g']),
  ("Now stand on a neighbour. The whole tree slides by one peel step, and the tree seen from the new ball matches the tree seen from the centre, to fifteen decimal places. There is no special ball. Each ball is a centre.", [('ck','button[data-s="0"]',0.1),('ck','button[data-s="1"]',0.4),('ck','button[data-s="2"]',0.6),('ck','button[data-s="-1"]',0.9)], ['tap']),
  ("At ratios five and seven a Lean proof shows that no path through the tree ever comes back to its start. That is freeness. It is not the same as keeping a spacing, which is what eye three measured.", [('tw','zt',5,7,0.1,0.4)], ['g']),
 ]),
 ("thomas", "thomas", [
  ("Eye five. One step, then another. Step along I, then along J, both at ratio five. The pink line is the single straight step that reaches the same ball. It is shorter than the two steps together: two point six against three point two.", [('js',"MIXER_API.set('zI',5);MIXER_API.set('zJ',5)",0.0)], []),
  ("And something is left over. The frame has turned. The dim axes are the frame carried by the straight step. The bright axes are the frame carried by the two steps. The turn between them obeys one rule: the tangent of half the turn equals gamma one times gamma two.", [], ['g']),
  ("With ratio five on both arms gamma is two thirds, so the tangent of the half angle is four ninths. That gives forty seven point nine two five degrees. And because four ninths is a fraction, the turn is a whole number right triangle: sixty five, seventy two, ninety seven. This is Euclid's rule for such triangles, with nine and four.", [], ['tap']),
  ("Ratios three and five give gamma one half and two thirds. The product is one third, and the triangle is three, four, five.", [('tw','zI',5,3,0.0,0.4)], ['g']),
  ("Take the steps in the other order. The same size of turn, in the opposite sense. Order is the handedness of the walk.", [('ck','button[data-o="1"]',0.12),('ck','button[data-o="0"]',0.85)], ['mir']),
  ("Across the full range of both sliders the turn from the matrices and the turn from the rule agree to fifteen decimal places.", [('tw','zI',3,13,0.0,0.25),('tw','zI',13,1.5,0.25,0.5),('tw','zJ',5,13,0.5,0.7),('tw','zJ',13,1.5,0.7,0.9),('tw','zJ',1.5,5,0.9,1.0)], []),
 ]),
 ("line", "line", [
  ("Eye six. Across the line. Both arms take the same step, and the gold shell marks the line, gamma squared equal to one half, at z equal to three plus two root two.", [('js',"MIXER_API.set('zl',5);MIXER_API.set('np',40)",0.0)], []),
  ("Below the line the square is a turn about a fixed point. At ratio three that point is zero point eight eight from the centre. At ratio five it is one point seven six, and in the ball it sits exactly on the line shell.", [('tw','zl',5,3,0.1,0.35),('tw','zl',3,5,0.55,0.8)], ['g']),
  ("At ratio five the centre comes back to within one tenth of its start after eighty three passes, and to within one hundredth after one thousand three hundred and forty five. It never lands exactly, because the turn is not a whole fraction of a full circle.", [('tw','np',40,120,0.0,0.6)], ['tap']),
  ("Raise the step toward the line. The fixed point moves outward and the ring through the centre grows. On the line the fixed point reaches the rim, and the ring opens.", [('tw','zl',5,L,0.05,0.8)], ['g']),
  ("Past the line there is no fixed point inside the ball. The square is a run. At ratio seven each pass carries the centre two point nine five six further out. So the line is where holding ends. Five is inside it. Seven is outside.", [('tw','zl',L,7,0.05,0.4),('tw','zl',7,9,0.75,0.9)], ['arc']),
  ("The whole slider, from the smallest step to the largest.", [('tw','zl',9,1.5,0.0,0.45),('tw','zl',1.5,5,0.45,1.0)], []),
 ]),
 ("chain", "chain", [
  ("Eye seven. The twin prime chain as one path in the tree. Each twin pair is a ball. The pair eleven and thirteen is the centre.", [('js',"MIXER_API.set('nc',2)",0.0)], []),
  ("A twin pair above five can only start with a number ending in one, seven or nine. A start ending in three would put a five at the end of its partner. That rule is proved in Lean. Each ending picks an arm: one goes along I, seven along J, nine along K.", [('tw','nc',2,60,0.1,1.0)], ['g','tap']),
  ("Each step is the true ratio between one starting number and the next. Ratios multiply, so the lengths add up to the logarithm of the last starting number over eleven. After two thousand four hundred pairs the path has walked nine point nine four.", [('tw','nc',60,2400,0.0,0.8)], ['g']),
  ("But it keeps changing arm, so it ends only five point eight five from the centre. That is fifty nine per cent of what it walked. This eye draws the rule. It makes no claim about the primes themselves.", [('tw','nc',2400,2,0.45,0.75),('tw','nc',2,400,0.75,1.0)], []),
 ]),
 ("outro", "tree", [
  ("Seven eyes, one ball. Faces that cross hold. Faces that miss leave a gap. A square of steps is a turn inside the line and a run outside it. Two steps turn the frame by a whole number triangle. And from each ball the tree is the same.", [('js',"MIXER_API.set('zt',5)",0.0)], ['g']),
  ("Each number in the four new eyes was computed two ways, from the matrices and from the rule, and checked away from the page to fifty digits. The mixer and all the scripts are open for you to check.", [], ['tap']),
 ]),
]

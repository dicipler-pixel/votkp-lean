# SCRIPT: PINGPONG_CONTROLS
# KILL/CONTROL: (a) even z that are not powers of 2 (6,10,12,20) must pass the same inclusion test (the hand proof uses only z even);
# (b) NEGATIVE control: odd z (3,5,7) and z=1 must produce violations (the proof genuinely needs v_pi(z)>=2 and z-1 a unit).
# If (b) shows zero violations the test is blind and Check 2 proves nothing.
import random, sys
sys.path.insert(0,'.')
from pingpong_check import *
rng=random.Random(777)
for z in (6,10,12,20,2,64,3,5,7,1):
    bad=0;tested=0
    for _ in range(3000):
        w=rand_pt(rng)
        for s in names:
            if not inU(invname[s],w):
                fw=mob(letter_matrix(z,s),w);tested+=1
                if not inU(s,fw): bad+=1
    print("z=%d tested %d violations %d"%(z,tested,bad))

# SCRIPT: TORUS-ROOTS-01
# Open problem 1 of the vacuum-disk paper: the missing torus-knot roots.
# Prediction written before the run (from Dirac Time Thm 13.1 arcs, TORUS-DIRS-03): the directions are -k^2/(pq) mod 1 with
#   8_19 = T(3,4):  {11/12, 2/3}      (three components, two distinct values)
#   10_124 = T(3,5): {14/15, 11/15}   (four components, two distinct values)
# Why this decides it: the solver is the paper's own (DRAWING-TORUS-02 / DRAWING-ROBUST-01), unchanged; only the number of
# starts and a second drawing (the torus braid closure) are added. Each polished non-degenerate root has Im V0 = 0 and
# Re V0/pi^2 rational, read with tolerance 1e-8.
# Kill: a non-degenerate rational root outside the predicted set. Support: 2/3 found for 8_19, 11/15 for 10_124.
import sys, random
sys.path.insert(0,'/home/claude/up/vd5/votkp_vacuum_disk_v5/scripts')
import snappy, drawing_torus_02 as D
KI=D.KI
def braid_pd(word):
    L=snappy.Link(braid_closure=word); return [tuple(x) for x in L.PD_code()]
jobs=[('8_19 KnotInfo PD',eval(KI['8_19']['pd_notation']),int(sys.argv[1])),
      ('8_19 braid (s1 s2)^4',braid_pd([1,2]*4),int(sys.argv[1])),
      ('10_124 KnotInfo PD',eval(KI['10_124']['pd_notation']),int(sys.argv[2])),
      ('10_124 braid (s1 s2)^5',braid_pd([1,2]*5),int(sys.argv[2]))]
for label,pd,st in jobs:
    D.report(label+', %d crossings'%len(pd),pd,st); sys.stdout.flush()

# SCRIPT: TWIN-PAPER-NUMBER-CHECK-01
# Re-read every headline number in the paper from the raw run outputs and compare with what the paper prints.
import csv
rows=list(csv.DictReader(open('swarm/precision/out/walk_1e12.csv')))
def at(X): return min(rows,key=lambda r:abs(float(r['X'])-X))
paper_turn={1e8:12.2048,1e9:12.2695,1e10:12.2969,1e11:12.3197,1e12:12.3442}
paper_c={1e8:0.108528,1e9:0.108568,1e10:0.108590,1e11:0.108607,1e12:0.108618}
paper_ro={1e8:12.46514,1e10:12.46507,1e11:12.46508,1e12:12.46508}
bad=0
for X,v in paper_turn.items():
    t=float(at(X)['turn_deg']); ok=abs(t-v)<6e-5; bad+=not ok; print('turn',X,t,v,'ok' if ok else 'MISMATCH')
for X,v in paper_c.items():
    t=float(at(X)['d_minus_L_over_sqrt3']); ok=abs(t-v)<6e-7; bad+=not ok; print('c',X,t,v,'ok' if ok else 'MISMATCH')
for X,v in paper_ro.items():
    t=float(at(X)['turn_if_tilt_dies_deg']); ok=abs(t-v)<6e-6; bad+=not ok; print('readout',X,t,v,'ok' if ok else 'MISMATCH')
s=float(at(1e12)['sum_r2']); print('sum r2',s, 'ok' if abs(s-1.2685628)<1e-7 else 'MISMATCH')
print('MISMATCHES',bad)

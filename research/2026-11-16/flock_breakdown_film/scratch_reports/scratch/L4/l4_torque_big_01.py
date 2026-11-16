# SCRIPT: L4-TORQUE-BIG-01  the opposite of weak coupling: torque 3 and 10 (the shipped value is 1). From L4-ISO-01 a ball holding all the light turns its spin at sqrt((omega rate)^2 + torque^2): at large torque all balls approach the same turning rate.
# Kill line (the same as kill line 1/2 of L4-SYNC-02, written before): LOCKED only if a pair with unequal free rates has measured rates within 0.02 in both last windows, both balls heavy, and r above the surrogate + 3 sd.
# Added question (answered by the run, not assumed): if rates do merge, is it coupling or the common torque? Control: torque 10 with the links closed is not available (gamma 0 closes the ports: run it, gamma = 0.0 gives each ball alone).
import subprocess, json
def run(P): return json.loads(subprocess.run(['node','l4_sync_02.js',json.dumps(P)],capture_output=True,text=True).stdout)
for sign in ('asis','swap'):
  for tq in (3.0,10.0):
    for g in (0.0,0.3,1.0):
        P=dict(N=3,clocks='z',torque=tq,gamma=g,gloss=0,sign=sign,T=400,h=0.005); r=run(P)
        ag=[(p['i'],p['j'],round(p['dr'][0],3),round(p['dr'][1],3)) for p in r['pairs']]
        print('sign %s torque %g gamma %g: free %s rates last window %s | pair rate gaps (i,j,win1,win2) %s | heavy %s | r %.3f surrogate %.3f | %s'%(sign,tq,g,[round(x,3) for x in r['free']],[round(x,3) for x in r['rates'][1]],ag,[round(x,2) for x in r['heavy']],r['rMean'],r['surMean'],r['verdict2']))

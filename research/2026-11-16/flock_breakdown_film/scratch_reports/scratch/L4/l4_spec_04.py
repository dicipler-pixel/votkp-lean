# SCRIPT: L4-SPEC-04  follow-up to L4-SPEC-03. Shared, pulled spectral lines exist. Are they the NONLINEAR pull (the field turning under the light, torque) or plain mixing of a linear system (normal modes)?
# Test: split the same coincidence count by torque. With torque 0 every ball field is fixed and the whole flock is a linear unitary map: any shared line there is a normal mode.
# KILL LINE (written before the run): the shared lines are called linear mixing (not a Kuramoto-type pull) if the coincidence fraction at torque 0 is at least half the fraction at torque 1.
# Also by gamma, to see that the lines need coupling at all.
import json, itertools, collections
rows=[json.loads(l) for l in open('sweep2.jsonl') if l.strip()]
rows=[r for r in rows if r['P']['clocks']=='z' and r['P'].get('sinkRate',0)==0]
c=collections.defaultdict(lambda:[0,0]); g=collections.defaultdict(lambda:[0,0])
for r in rows:
    n=len(r['free']); hv=[i for i in range(n) if r['heavy'][i]>=0.5]
    for i,j in itertools.combinations(hv,2):
        if abs(r['free'][i]-r['free'][j])<=0.02: continue
        for key in ('up','dn'):
            hit=abs(r['spec'][i][key]['nu']-r['spec'][j][key]['nu'])<0.03
            c[r['P']['torque']][0]+=hit; c[r['P']['torque']][1]+=1
            g[r['P']['gamma']][0]+=hit; g[r['P']['gamma']][1]+=1
for k in sorted(c): print('torque %g: %d coincide of %d heavy unequal-rate peak pairs = %.3f'%(k,c[k][0],c[k][1],c[k][0]/c[k][1]))
for k in sorted(g): print('gamma %g: %d of %d = %.3f'%(k,g[k][0],g[k][1],g[k][0]/g[k][1]))
f0=c[0.0][0]/c[0.0][1]; f1=c[1.0][0]/c[1.0][1]
print('verdict:', 'linear mixing (torque 0 fraction %.3f >= half of torque 1 fraction %.3f)'%(f0,f1) if f0>=f1/2 else 'torque-dependent (NOT plain linear mixing)')

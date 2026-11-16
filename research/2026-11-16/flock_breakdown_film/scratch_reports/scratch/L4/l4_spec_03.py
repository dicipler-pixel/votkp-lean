# SCRIPT: L4-SPEC-03  follow-up to L4-SPEC-02 (which found shared spectral peaks in z-clock cells, 10 times chance).
# Question: are the shared peaks PULLED lines (a common frequency that neither ball has on its own) or just one ball's own line seen in the other (light has moved across)?
# A free ball has nu_up = +free/2 and nu_dn = -free/2 (header of l4_sync_01.js). A coincident pair is PULLED if the shared peak is more than 0.1 from BOTH balls' own free lines (+-free/2 for the same branch).
# KILL LINE (written before the run): the shared lines are called locking only if at least half of the coincidences are PULLED. Otherwise they are leakage of own lines or mixing, not locking.
import json, itertools
rows=[json.loads(l) for l in open('sweep2.jsonl') if l.strip()]
rows=[r for r in rows if r['P']['clocks']=='z' and r['P'].get('sinkRate',0)==0]
tot=pulled=own=0; byN={}
for r in rows:
    n=len(r['free']); hv=[i for i in range(n) if r['heavy'][i]>=0.5]
    for i,j in itertools.combinations(hv,2):
        if abs(r['free'][i]-r['free'][j])<=0.02: continue
        for key,sg in (('up',1),('dn',-1)):
            a=r['spec'][i][key]['nu']; b=r['spec'][j][key]['nu']
            if abs(a-b)<0.03:
                c=(a+b)/2; fi=sg*r['free'][i]/2; fj=sg*r['free'][j]/2
                p=abs(c-fi)>0.1 and abs(c-fj)>0.1
                tot+=1; pulled+=p; own+= (not p)
                byN.setdefault(r['P']['N'],[0,0]); byN[r['P']['N']][0]+=1; byN[r['P']['N']][1]+=p
print('coincident heavy unequal-rate pairs: %d ; PULLED (> 0.1 from both own lines): %d ; at an own line: %d'%(tot,pulled,own))
print('by N (coincidences, pulled):',byN)
print('verdict:', 'locking supported' if pulled>=tot/2 else 'NOT locking: most shared lines sit on one ball own line')

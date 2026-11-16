# SCRIPT: L4-READ-02  reads sweep2.jsonl and applies KILL LINE 1 + KILL LINE 2 (headers of l4_sync_01.js / l4_sync_02.js) to every cell.
# For clocks 'equal' the line needs the matching torque-0 run (same N, gamma, gloss, sign, kappa, sink): sd(on) < 0.5 and sd(off) > 0.5.
import json, collections, sys
rows=[json.loads(l) for l in open('sweep2.jsonl') if l.strip()]
def key(P,tq=None):
    return (P['N'],P['clocks'],P['torque'] if tq is None else tq,P['gamma'],P['gloss'],P['sign'],P.get('kappa',0.25),P.get('sinkBall',-1),P.get('sinkRate',0))
idx={key(r['P']):r for r in rows}
eps=0.02
def judge(r):
    P=r['P']; n=P['N'] if False else len(r['free']); kl1=[]
    for p in r['pairs']:
        i,j=p['i'],p['j']
        if not (p['dr'][0]<eps and p['dr'][1]<eps): continue
        if P['clocks']=='z':
            if p['dfree']>eps: kl1.append((i,j))
        else:
            off=idx.get(key(P,0.0))
            if p['sd']<0.5 and off is not None:
                po=[q for q in off['pairs'] if q['i']==i and q['j']==j][0]
                if po['sd']>0.5: kl1.append((i,j))
    kl2=[pr for pr in kl1 if r['heavy'][pr[0]]>=0.5 and r['heavy'][pr[1]]>=0.5]
    rok=r['rMean']>r['surMean']+3*r['surSd']
    return kl1,kl2,rok
tot=collections.Counter(); locked=[]; kl1only=[]
for r in rows:
    kl1,kl2,rok=judge(r); tag=r['P'].get('tag','?')
    tot[tag]+=1
    if kl1: kl1only.append((r,kl1,kl2,rok))
    if kl2 and rok: locked.append((r,kl1,kl2,rok))
print('cells read:',len(rows),dict(tot))
print('cells meeting kill line 1 on some pair:',len(kl1only),' cells LOCKED by kill line 2 (pair + weight + r over surrogate):',len(locked))
def desc(r): P=r['P']; return 'N=%d %s torque=%g gamma=%g gloss=%g sign=%s kappa=%g sink=(%d,%g) tag=%s'%(P['N'],P['clocks'],P['torque'],P['gamma'],P['gloss'],P['sign'],P.get('kappa',0.25),P.get('sinkBall',-1),P.get('sinkRate',0),P.get('tag'))
for r,k1,k2,rok in kl1only: print('  KL1', desc(r),'pairs',k1,'KL2 pairs',k2,'r-excess %.2f sd'%r['rExcess'],'rMean %.3f sur %.3f'%(r['rMean'],r['surMean']),'minheavy',[round(x,2) for x in r['heavy']])
# r excess distribution
ex=sorted(r['rExcess'] for r in rows)
print('r excess over surrogate (in surrogate s.d.): min %.2f  median %.2f  max %.2f ; cells above +3: %d ; cells below -3: %d'%(ex[0],ex[len(ex)//2],ex[-1],sum(1 for x in ex if x>3),sum(1 for x in ex if x<-3)))
top=sorted(rows,key=lambda r:-r['rExcess'])[:8]
print('top r-excess cells:'); [print('  ',desc(r),'excess %.1f rMean %.3f sur %.3f heavy %s'%(r['rExcess'],r['rMean'],r['surMean'],[round(x,2) for x in r['heavy']])) for r in top]
bot=sorted(rows,key=lambda r:r['rExcess'])[:5]
print('lowest r-excess cells (anti-locking side):'); [print('  ',desc(r),'excess %.1f rMean %.3f sur %.3f'%(r['rExcess'],r['rMean'],r['surMean'])) for r in bot]
# books
print('worst books error over all cells %.2e'%max(r['book'] for r in rows))
# sign comparison: how much does the swap change rMean?
d=[];
for r in rows:
    if r['P']['sign']=='asis':
        k=list(key(r['P'])); k[5]='swap'; s=idx.get(tuple(k))
        if s: d.append(abs(r['rMean']-s['rMean']))
print('as-written vs swapped, same cell: |delta rMean| mean %.3f max %.3f over %d pairs of cells'%(sum(d)/len(d),max(d),len(d)))

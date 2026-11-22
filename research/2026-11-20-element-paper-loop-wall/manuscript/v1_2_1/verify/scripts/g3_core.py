# SCRIPT: G3-CORE-COUNTS
import gzip,json,math,collections
B='/home/claude/votkp-lean/'
R=json.load(gzip.open(B+'data/element_thresholds_20261011.json.gz'))['records']
D=json.loads((lambda s:s[s.index('{'):s.rindex('}')+1])(open(B+'research/2026-11-20-element-paper-loop-wall/mixer/element_data_v1.js').read()))['el']
W=3+2*math.sqrt(2)
rec={r['Z']:r for r in R}
tot=0;gr=collections.Counter()
for Z in range(1,86):
    th=rec[Z]['thresholds']; assert len(th)==Z,(Z,len(th)); tot+=len(th)
    for t in th: gr[t['grade']]+=1
print('positive-index energies H..At',tot,gr)
ordinary=0; out=[]
for Z in range(1,86):
    ie=[t['IE_eV'] for t in rec[Z]['thresholds']]
    for k in range(len(ie)-1):
        ordinary+=1
        z=ie[k+1]/ie[k]
        if z>W: out.append((Z,k+1,z))
print('ordinary',ordinary,'outside',len(out),out)
# radon..oganesson adjacent pairs
extra=0
for Z in range(86,119):
    n=len(rec[Z]['thresholds']); extra+=max(n-1,0)
print('extra pairs Rn..Og',extra,'total',ordinary+extra)
# EA
EA={e['Z']:e['ea'] for e in D if e['ea']}
print('adopted ea count',len(EA),sorted(EA))

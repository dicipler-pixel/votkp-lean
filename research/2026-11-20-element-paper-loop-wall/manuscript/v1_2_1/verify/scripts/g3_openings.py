# SCRIPT: G3-OPENING-MAP-SCREENING-ADDRESS
import gzip,json,math
B='/home/claude/votkp-lean/'
R=json.load(gzip.open(B+'data/element_thresholds_20261011.json.gz'))['records']
rec={r['Z']:r for r in R}
W=3+2*math.sqrt(2)
def ies(Z): return {t['q']:t for t in rec[Z]['thresholds'] if t['IE_eV'] is not None}
CORES={'helium':2,'neon':10,'argon':18,'krypton':36,'xenon':54,'radon':86}
seqs={}
for nm,N in CORES.items():
    s=[]
    for Z in range(N+1,119):
        q=Z-N-1; d=ies(Z)
        if q in d and q+1 in d:
            s.append((Z,rec[Z]['symbol'],d[q+1]['IE_eV']/d[q]['IE_eV']))
    seqs[nm]=s
    outs=[x[1] for x in s if x[2]>W]
    # steps until crossing inward (position of first inside)
    first_in=next((i for i,x in enumerate(s) if x[2]<=W),None)
    print(nm,len(s),'first',s[0][1],round(s[0][2],3),'outside',outs,'first inside index',first_in,'Zrange',s[0][0],s[-1][0])
print('total',sum(len(v) for v in seqs.values()))
# also first ordinary ratio per core: nonmonotone check
for nm,s in seqs.items():
    if nm!='radon':
        z=[x[2] for x in s]; print(nm,'monotone decreasing',all(a>b for a,b in zip(z,z[1:])), [round(v,4) for v in z[:3]])
print('Fr',seqs['radon'][0], 'Fr box',(22.4-1.9)/(4.0727411+1.1e-6),(22.4+1.9)/(4.0727411-1.1e-6))
# 433 minus radon
print('433 check (He..Xe+Rn):',sum(len(v) for v in seqs.values()))
# crossing carbon-nitrogen etc
for nm in ['helium','neon','argon','krypton','xenon']:
    s=seqs[nm]; i=next(i for i,x in enumerate(s) if x[2]<=W); print(nm,'outside->inside between',s[i-1][1],round(s[i-1][2],2),'and',s[i][1],round(s[i][2],2))
# address classes
cls={}
def first_core(Z):
    for nm in ['xenon','krypton','argon','neon','helium']:
        N=CORES[nm]
        if N<Z:
            q=Z-N-1;d=ies(Z); 
            return d[q+1]['IE_eV']/d[q]['IE_eV']
    return None
import sys
sys.path.insert(0,'/home/claude/votkp-lean/research/2026-11-20-element-paper-loop-wall/batch12/lean/window')
D=json.loads((lambda s:s[s.index('{'):s.rindex('}')+1])(open(B+'research/2026-11-20-element-paper-loop-wall/mixer/element_data_v1.js').read()))['el']
ea={e['Z']:e['ea'] for e in D}
members={}
for Z in range(1,86):
    a=None if not ea[Z] else ('outside' if ies(Z)[0]['IE_eV']/ea[Z]>W else 'inside')
    f=first_core(Z); c=None if f is None else ('outside' if f>W else 'inside')
    members.setdefault((a or 'none',c or 'none'),[]).append(rec[Z]['symbol'])
for k,v in sorted(members.items(),key=lambda kv:-len(kv[1])): print(k,len(v),' '.join(v))
# strongest ordinary step per element
strong={}
for Z in range(1,86):
    ie=[t['IE_eV'] for t in rec[Z]['thresholds']]
    if len(ie)>1:
        zs=[ie[k+1]/ie[k] for k in range(len(ie)-1)]
        strong[Z]=zs.index(max(zs))+1
print('strongest step index:',{rec[Z]['symbol']:strong[Z] for Z in (11,12,13,14,19,20,21)})
# elements with all ordinary inside
allin=[rec[Z]['symbol'] for Z in range(1,86) if len(rec[Z]['thresholds'])>1 and all(rec[Z]['thresholds'][k+1]['IE_eV']/rec[Z]['thresholds'][k]['IE_eV']<=W for k in range(Z-1))]
print('all-inside count',len(allin),'Mg' in allin, 'Ca' in allin)
print('strongest depth: core opening is the strongest? count of elements where strongest step index > first eligible core ->') 

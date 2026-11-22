# SCRIPT: G3-APPENDIX-B-D-CHECK
import gzip,json,math,re,random
B='/home/claude/votkp-lean/'
R=json.load(gzip.open(B+'data/element_thresholds_20261011.json.gz'))['records']
rec={r['Z']:r for r in R}
W=3+2*math.sqrt(2)
D=json.loads((lambda s:s[s.index('{'):s.rindex('}')+1])(open(B+'research/2026-11-20-element-paper-loop-wall/mixer/element_data_v1.js').read()))['el']
ea={e['Z']:e['ea'] for e in D}
pt=json.load(open(B+'research/2026-11-20-element-paper-loop-wall/ptable/ptable_data.json'))['elements']
ea_pt={e['Z']:(e['anion']['EA'] if e['anion'] else None) for e in pt}
print('EA mismatch element_data vs ptable:',[ (z,ea[z],ea_pt[z]) for z in ea if (ea[z] or 0)!=(ea_pt[z] or 0)])
EAx=dict(ea); EAx[66]=0.015; EAx[69]=0.032
EAx[84]=11905.631*6.62607015e-34*299792458*100/1.602176634e-19
G=lambda z:(z-1)/(z+1)
def ies(Z): return [t['IE_eV'] for t in rec[Z]['thresholds']]
def cell(z):
    return ('**%.4f (%.4f)**' if z>W else '%.4f (%.4f)')%(z,G(z))
t=open('/home/claude/paper_v12/build/src/17_tables.md').read()
sec=t[t.index('Appendix B'):t.index('Appendix C')]
rows=[l for l in sec.split('\n') if re.match(r'\| \d+ \|',l)]
bad=0
CO=[(2,'K'),(10,'L'),(18,'A'),(36,'Kr'),(54,'Xe')]
for l in rows:
    c=[x.strip() for x in l.strip().strip('|').split('|')]
    Z=int(c[0]); ie=ies(Z)
    exp=[]
    exp.append('%g'%ie[0])
    if ea.get(Z) or Z in(66,69,84): 
        e=EAx[Z]; z=ie[0]/e
        s=cell(z)
        if Z in(66,69): s+=' estimate'
        if Z==84: s+=' preliminary'
        exp.append(s)
    else: exp.append('none')
    for N,_ in CO:
        if N<Z:
            q=Z-N-1; exp.append(cell(ie[q+1]/ie[q]))
        else: exp.append('—')
    got=c[2:]
    # first IE compare numerically
    try:
        ok_ie=abs(float(got[0])-ie[0])<5e-5*max(1,ie[0])
    except: ok_ie=False
    mism=[(i,g,e) for i,(g,e) in enumerate(zip(got[1:],exp[1:])) if g!=e]
    if not ok_ie or mism: bad+=1; print('Z',Z,c[1],'IE',got[0],ie[0],mism)
print('appendix B rows',len(rows),'rows with mismatch',bad)
# Appendix D
sec=t[t.index('Appendix D'):]
rowsD=[l for l in sec.split('\n') if re.match(r'\| [A-Z]',l)]
name2Z={r['name']:r['Z'] for r in R}; name2Z['Aluminum']=13;name2Z['Cesium']=55;name2Z['Caesium']=55
last=0;badD=0;n=0
for l in rowsD:
    c=[x.strip() for x in l.strip().strip('|').split('|')]
    if c[0] in('Element',): continue
    Z=name2Z[c[0]];n+=1;I=ies(Z)[0];A=EAx[Z];z=I/A;g=G(z)
    chk=[abs(float(c[1])-A)<6e-5*max(1,1),c[2]=='%.4f'%z,c[3]=='%.5f'%g,c[4]=='%.4f'%(1/(2*g*g)),c[5]==('outside' if z>W else 'inside')]
    if not all(chk): badD+=1;print('D mismatch',c,chk,'%.4f %.5f %.4f'%(z,g,1/(2*g*g)),A)
    if z<last: print('order broken',c[0])
    last=z
print('appendix D rows',n,'bad',badD)

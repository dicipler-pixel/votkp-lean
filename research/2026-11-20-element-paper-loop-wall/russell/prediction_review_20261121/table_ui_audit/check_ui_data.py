"""Run: python check_ui_data.py path/to/votkp-lean. Analysis of the original table v1."""
import math, json, gzip, hashlib, sys, re
from pathlib import Path
from collections import Counter
root = Path(sys.argv[1]); work = root/'research/2026-11-20-element-paper-loop-wall'
archive = root/'data/element_thresholds_20261011.json.gz'
src = json.loads(gzip.decompress(archive.read_bytes()))['records']
table = json.loads((work/'ptable/ptable_data.json').read_text())['elements']
raw_js = (work/'mixer/element_data_v1.js').read_text()
ledger = json.loads(raw_js[raw_js.index('{'):raw_js.rindex('}')+1])['el']
counts=Counter(); mismatches=[]; rendered=[]; octaves={}; ordinary=[]; anions=[]
def check(k,v,actual,where):
    counts[k]+=1
    expected = float(format(v,'.7g')) if isinstance(v, float) else v
    if expected!=actual:
        mismatches.append((where,k,expected,actual))
for rec,e,aff in zip(src,table,ledger):
    Z=e['Z']; sym=e['sym']; assert Z==rec['Z']==aff['Z'] and sym==rec['symbol']==aff['s']
    ies=[float(r['IE_eV']) for r in rec['thresholds']]
    assert len(ies)==len(e['ie'])==Z
    counts.update(r['grade'] for r in rec['thresholds'])
    for k,(ie,ui) in enumerate(zip(ies,e['ie']),1):
        check('IE',ie,ui,(sym,k))
    for k,(i,j,s) in enumerate(zip(ies,ies[1:],e['steps']),1):
        z=j/i; g=(z-1)/(z+1); out=(j-i)**2*2>(j+i)**2
        for name,val in dict(k=k,z=z,g2=g*g,Em=(j-i)**2,Ep=(j+i)**2,out=out).items():check(name,val,s[name],(sym,k))
        ordinary.append((z,out,sym,k));rendered.append((s['g2'],sym,k))
    for c in e['cores']:
        n=c['N']; k=Z-n; z=ies[k]/ies[k-1]; g=(z-1)/(z+1)
        for name,val in dict(step=k,z=z,g2=g*g,out=2*g*g>1).items():check('core.'+name,val,c[name],sym)
    check('ledger',math.log(ies[-1]/ies[0]),e['ledger'],sym)
    a=e['anion']; ea=aff['ea']
    if ea:
        z=ies[0]/ea; g=(z-1)/(z+1); eta=(ies[0]-ea)/2; chi=(ies[0]+ea)/2; om=chi*chi/(2*eta); out=2*g*g>1
        for name,val in dict(EA=ea,z0=z,g2=g*g,chi=chi,eta=eta,omega=om,omega_over_eta=om/eta,uptake=1/g,out=out,IExEA=ies[0]*ea).items():check('anion.'+name,val,a[name],sym)
        anions.append((z,out,sym,0))
    else: assert a is None
    if e['tone']:
        oc,t=e['tone'];octaves.setdefault(oc,[]).append((sym,t,e['sig'][0]))
    if e['optic']:
        op=e['optic'];counts[('optics',op['metal'],op['mean_R']>.5)]+=1
    for t in e['lean']:
        decl=(root/t['file']).read_text().splitlines()[t['line']-1]
        check('indexed theorem',True,re.search(r'\btheorem\s+'+re.escape(t['name'])+r'\b',decl) is not None,sym)
assert len(table)==85
print('Pinned gzip SHA256',hashlib.sha256(archive.read_bytes()).hexdigest())
print('Fields examined (rounding to 7 significant digits for the display JSON):',counts)
print('Mismatches:',len(mismatches),mismatches[:12])
for n,rows in [('ordinary',ordinary),('anion',anions),('combined',ordinary+anions)]:
    print(n,'outside',sum(r[1] for r in rows),'of',len(rows),'nearest inside/outside',max(r for r in rows if not r[1]),min(r for r in rows if r[1]))
print('3D minimum floor changes',sum(x<0.03**2 for x,_,_ in rendered),'of',len(rendered),'links; smallest=',min(rendered),'area inflation=',.03**2/min(rendered)[0])
for o,lines in octaves.items():print(o,lines)
if mismatches:sys.exit(1)

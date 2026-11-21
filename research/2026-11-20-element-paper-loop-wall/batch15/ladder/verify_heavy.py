"""Check batches 15 and 17 row-by-row against the archive and charge-keyed ASD downloads."""
import csv
import gzip
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
PAPER=HERE.parents[1]
ARCH=PAPER.parents[1]/'data/element_thresholds_20261011.json.gz'
assert hashlib.sha256(ARCH.read_bytes()).hexdigest()=='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
with gzip.open(ARCH,'rt') as f:
    atoms=json.load(f,parse_float=F)['records']
def read(path):
    with path.open() as f:
        return list(csv.DictReader(f))
def optional(s):
    return None if s is None or s=='' else F(s)
def rounded(x,places):
    scale=10**places
    n,r=divmod(abs(x.numerator)*scale,x.denominator)
    return F((1 if x>=0 else -1)*(n+int(2*r>=x.denominator)),scale)
def wall(z):
    return 'outside' if 2*(z-1)**2>(z+1)**2 else 'inside'
for n,start,filename in [(15,71,'batch15_lu_re.csv'),(17,81,'batch17_tl_at.csv')]:
    folder=PAPER/f'batch{n}/ladder'
    def keyed(name,column):
        data=read(folder/name)
        index={(int(r['Z']),int(r[column])):r for r in data}
        assert len(index)==len(data)
        return index
    grid=keyed(filename,'k')
    detailed=keyed('rungs_detailed.csv','k')
    current=keyed('asd_states_20261121.csv','q')
    aff={int(r['Z']):r for r in read(folder/'affinities.csv')}
    counts=Counter()
    for atom in atoms[start-1:start+4]:
        z,sym=atom['Z'],atom['symbol']
        a=aff[z]
        levels=[(optional(a['EA_eV']),optional(a['unc_eV']))]
        for q,t in enumerate(atom['thresholds']):
            obs=current.pop((z,q))
            energy=obs['NIST_energy_eV']
            grade={'[':'S','(':'T'}.get(energy[0],'E')
            assert (F(energy.strip('[]()')),optional(obs['NIST_unc_eV']),grade,obs['NIST_refs'])==(
                F(t['IE_eV']),optional(t['unc_eV']),t['grade'],t['references'])
            assert q==t['q']
            counts[grade]+=1
            levels.append((F(t['IE_eV']),optional(t['unc_eV'])))
        for k,(x,dx) in enumerate(levels):
            row=grid.pop((z,k))
            assert optional(row['IE_k (eV)'])==x and row['symbol']==sym
            assert row['source']==(a['status'] if k==0 else atom['thresholds'][k-1]['grade'])
            if x is None or k==z:
                assert not row['z_k'] and not row['Gamma_k']
                continue
            y,dy=levels[k+1]
            ratio,gamma=y/x,(y-x)/(y+x)
            assert F(row['z_k'])==rounded(ratio,6) and F(row['Gamma_k'])==rounded(gamma,6)
            counts['ordinary' if k else 'numeric anion']+=1
            detail=detailed.pop((z,k))
            assert detail['wall']==wall(ratio)
            if dx is None or dy is None:
                assert detail['z_lo']==detail['z_hi']=='' and detail['box_wall']=='unavailable'
                counts['missing range']+=1
                continue
            lo,hi=(y-dy)/(x+dx),(y+dy)/(x-dx)
            assert abs(F(detail['z_lo'])-lo)<=F(1,2*10**9) and abs(F(detail['z_hi'])-hi)<=F(1,2*10**9)
            assert wall(lo)==wall(hi)==detail['box_wall']==wall(ratio)
            assert wall(ratio)=='inside' or not lo<=1<=hi
            counts['complete range']+=1
    assert not grid and not detailed and not current
    print('Batch',n,dict(sorted(counts.items())))

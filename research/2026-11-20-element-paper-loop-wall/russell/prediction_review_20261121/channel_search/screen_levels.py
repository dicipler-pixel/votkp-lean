"""Re-scan the pinned observed-level snapshots and the source H–At threshold CSV.

Usage: python screen_levels.py H_to_At_thresholds.csv /path/to/cache
Each file's Git object ID is verified whether downloaded or cached.
"""
import csv
import hashlib
import re
import sys
from collections import Counter
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from urllib.request import urlopen

Q=Fraction
root=Path(sys.argv[2])
manifest=Path(__file__).with_name('level_search_manifest.csv')
rival=(Q('7.576234')/Q('1.30447')+Q('8.15168')/Q('1.3895212'))/2
units=Q('8065.543937')
with open(sys.argv[1]) as f:
    thresholds={(r['symbol'],int(r['k'])):r for r in csv.DictReader(f)}

def load_snapshot(entry):
    repo,commit,path,expected=(entry[k] for k in ['repository','commit','path','git_blob_sha1'])
    dest=root/repo.split('/')[-1]/path
    if not dest.exists():
        raw=urlopen(f'https://raw.githubusercontent.com/{repo}/{commit}/{path}', timeout=40).read()
    else:
        raw=dest.read_bytes()
    object_hash=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    if object_hash!=expected:
        raise ValueError(f'Source digest differs for {path}')
    if not dest.exists():
        dest.parent.mkdir(parents=True,exist_ok=True)
        dest.write_bytes(raw)
    return raw.decode('utf-8',errors='replace').splitlines()

def observed_levels(entry,lines):
    p=Path(entry['path'])
    if entry['repository'].endswith('/chianti-database'):
        s,stage=p.stem.split('_')
        for line in lines:
            if line.strip()=='-1':break
            if len(line)<72 or not line[:7].strip().isdigit():continue
            yield s.title(),int(stage)-1,' '.join(line[7:52].split()),line[52:57].strip(),line[57:72].strip()
    else:
        symbol=re.sub(r'[0-9]','',p.parent.name).title()
        for r in csv.DictReader(lines):
            if r['energy_tier'] in ('nist','exp','measured'):
                yield symbol,0,r['level'],r['J'],r['energy_cm']

def energy(s,k):
    value=thresholds.get((s,k),{}).get('energy_eV')
    return Q(value) if value else None

getcontext().prec=60
wall_dec=3+2*Decimal(2).sqrt()
rival_dec=Decimal(rival.numerator)/Decimal(rival.denominator)
window_width=rival_dec-wall_dec
bins={j:[] for j in range(-10,11)}
counts=Counter()
writer=csv.writer(sys.stdout)
writer.writerow('symbol selected_charge k role level J observed_cm-1 z'.split())
with manifest.open() as f:
    for src in csv.DictReader(f):
        for s,q,level,J,wavenumber in observed_levels(src,load_snapshot(src)):
            if not wavenumber:continue
            d=Q(wavenumber)/units
            limit=energy(s,q+1)
            if limit is None or not 0<d<limit:continue
            for role,k in [('intermediate',q),('final',q-1)]:
                lo,hi=energy(s,k),energy(s,k+1)
                if lo is None or hi is None:continue
                counts[(src['repository'],role)]+=1
                z=(hi-d)/(lo+d) if role=='intermediate' else (hi+d)/lo
                if len(sys.argv)>3 and role=='final':
                    exact_z=Decimal(z.numerator)/Decimal(z.denominator)
                    scaled=(exact_z-wall_dec)/window_width
                    if -10<=scaled<11:
                        j=int(scaled.to_integral_value(rounding='ROUND_FLOOR'))
                        assert abs(scaled-scaled.to_integral_value())>Decimal('1e-35')
                        bins[j].append((s,q,level))
                if z>1 and z*z-6*z+1>0 and z<rival:
                    writer.writerow([s,q,k,role,level,J,wavenumber,f'{float(z):.12f}'])
for group,total in sorted(counts.items()):
    print(*group,total,file=sys.stderr)

if len(sys.argv)>3:
    with open(sys.argv[3],'w') as f:
        out=csv.writer(f)
        out.writerow(['window_offset','lo','hi','level_count','configuration_term_count','element_count','elements'])
        for j,items in bins.items():
            lo=wall_dec+j*window_width
            hi=lo+window_width
            elements=sorted({x[0] for x in items})
            out.writerow([j,f'{lo:.12f}',f'{hi:.12f}',len(items),len(set(items)),len(elements),' '.join(elements)])

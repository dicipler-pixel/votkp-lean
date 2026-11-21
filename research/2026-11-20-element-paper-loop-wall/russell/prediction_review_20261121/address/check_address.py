"""Compare first-core and any-ordinary addresses in the two 85-element ledgers.

Usage: python check_address.py H_to_At_thresholds.csv element_data_v1.js output_dir
"""
import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction as Q
from pathlib import Path

CORES = {2:'He', 10:'Ne', 18:'Ar', 36:'Kr', 54:'Xe'}
def side(a,b):
    # For positive energies and forward or reversed order.
    f=2*(b-a)**2-(b+a)**2
    return 'O' if f>0 else 'I' if f<0 else 'T'

def load(csvfile,mixer):
    text=mixer.read_text().strip()
    atoms=json.loads(text.removeprefix('window.ELEMENT_DATA=').removesuffix(';'),parse_float=Q)['el']
    byZ=defaultdict(list)
    for r in csv.DictReader(csvfile.open()): byZ[int(r['Z'])].append(r)
    out=[]
    for Z in range(1,86):
        rows=sorted(byZ[Z],key=lambda r:int(r['k']))
        mx=atoms[Z-1]; symbol=mx['s']
        assert [int(r['k']) for r in rows]==list(range(Z+1))
        assert all(s['symbol']==symbol for s in rows)
        e=[None]+[Q(k['energy_eV']) for k in rows[1:]]
        assert all(Q(v)==v2 for v,v2 in zip(mx['ie'],e[1:])) and len(mx['ie'])==Z
        ratios={k:e[k+1]/e[k] for k in range(1,Z)}
        outerKs=sorted(Z-N for N in CORES if Z>N)
        ordered=sorted(outerKs,key=ratios.get,reverse=True)
        assert len({ratios[k] for k in ordered})==len(ordered)
        outsider=[k for k in ratios if side(e[k],e[k+1])=='O']
        anyOrd='N' if not ratios else ('O' if outsider else 'I')
        first='N' if not outerKs else side(e[outerKs[0]],e[outerKs[0]+1])
        top=ordered[0] if ordered else None
        runner=ordered[1] if len(ordered)>1 else None
        rank=outerKs.index(top)+1 if top else 0
        def bound(k):
            a,b=rows[k]['uncertainty_eV'],rows[k+1]['uncertainty_eV']
            if not a or not b:return None
            da,db=Q(a),Q(b)
            if e[k]-da<=0:return None
            return ((e[k+1]-db)/(e[k]+da),(e[k+1]+db)/(e[k]-da))
        boxes={k:bound(k) for k in ordered}
        if not top:rank_cert='no named core'
        elif not runner:rank_cert='sole named core'
        elif any(b is None for b in boxes.values()):rank_cert='width missing'
        elif boxes[top][0]>max(boxes[k][1] for k in ordered[1:]):rank_cert='separated'
        else:rank_cert='overlapping boxes'
        all_box='no named core'
        if top:
            assert all(ratios[top]>ratios[k] for k in ratios if k!=top)
            other_bounds=[bound(k) for k in ratios if k!=top]
            if boxes[top] is None or any(item is None for item in other_bounds):
                all_box='width missing'
            elif all(boxes[top][0]>item[1] for item in other_bounds):
                all_box='separated'
            else:all_box='overlapping boxes'
        extended=side(Q(rows[0]['energy_eV']),e[1]) if rows[0]['energy_eV'] else 'N'
        mixer_side=side(Q(mx['ea']),e[1]) if mx['ea'] else 'N'
        out.append(dict(Z=Z,symbol=symbol,mixer=mixer_side,extended=extended,
            affinity_status=rows[0]['grade_or_status'],first=first,any_ordinary=anyOrd,
            first_core=CORES[Z-outerKs[0]] if outerKs else '',first_k=outerKs[0] if outerKs else '',
            outside_k='/'.join(map(str,outsider)),dominant_core=CORES[Z-top] if top else '',
            dominant_k=top or '',dominant_ordinal=rank,rank_box_status=rank_cert,dominant_vs_all_box=all_box,dominant_z=f'{float(ratios[top]):.9f}' if top else '',
            next_named_core=CORES[Z-runner] if runner else '',
            next_named_z=f'{float(ratios[runner]):.9f}' if runner else ''))
    return out

def address_stats(keys):
    cc=Counter(keys)
    collisions=sum(n*(n-1)//2 for n in cc.values())
    return len(cc),max(cc.values()),collisions
def encoding(r,ledger,second):
    return (r[ledger],r[second])
def vote(labels):return 'I' if labels.count('I')>labels.count('O') else 'O'
def summary(pred):
    conf=Counter((p['actual'],p['predicted']) for p in pred)
    raw=[conf[a,b] for a,b in [('O','O'),('O','I'),('I','O'),('I','I')]]
    n=sum(raw);return raw,(raw[0]+raw[3])/n,0.5*(raw[0]/sum(raw[:2])+raw[3]/sum(raw[2:]))

def run(args):
    rows=load(args.extended,args.mixer)
    args.output.mkdir(exist_ok=True,parents=True)
    def save(name,items):
        with (args.output/name).open('w') as f:
            writer=csv.DictWriter(f,fieldnames=items[0].keys(),lineterminator='\n')
            writer.writeheader();writer.writerows(items)
    save('addresses.csv',rows)
    for path in (args.extended,args.mixer):
        print(path.name,hashlib.sha256(path.read_bytes()).hexdigest())
    mismatches=[r['symbol'] for r in rows if r['any_ordinary']!=r['first']]
    print('different ordinary component:',mismatches)
    assert mismatches==['He']
    print('dominant name vs outermost switches:',
          [(r['symbol'],r['first_core'],r['dominant_core']) for r in rows if r['first_core']!=r['dominant_core']][:8])
    keys=Counter((r['first_core'],r['dominant_core']) for r in rows)
    print('first and dominant:', sorted(keys.items()))
    print('dominant vs ALL ordinary rank box:',dict(Counter(r['dominant_vs_all_box'] for r in rows)))
    print('rank boxes:',dict(Counter(r['rank_box_status'] for r in rows)))
    print('dominant ordinal:', sorted(Counter(r['dominant_ordinal'] for r in rows).items()))
    predictions=[]
    for ledger in ('mixer','extended'):
        print('\nledger:',ledger)
        for mode in ('first','any_ordinary','ranked','named'):
            if mode in ('first','any_ordinary'): aa=[encoding(r,ledger,mode) for r in rows]
            elif mode=='ranked': aa=[(r[ledger],r['any_ordinary'],r['dominant_ordinal']) for r in rows]
            else: aa=[(r[ledger],r['any_ordinary'],r['dominant_ordinal'],r['dominant_core']) for r in rows]
            print(mode,'bins/max/tied pairs',address_stats(aa))
            if mode in ('first','any_ordinary'):print(' sizes',sorted(Counter(aa).items()))
        train=[r for r in rows if r['Z']<=54 and r[ledger] in ('I','O')]
        test=[r for r in rows if r['Z']>=55 and r[ledger] in ('I','O')]
        def key(r):return (r['any_ordinary'],r['dominant_ordinal'])
        majority=vote([r[ledger] for r in train])
        print('train/test',len(train),len(test),'training labels by feature',
              {str(k):dict(Counter(t[ledger] for t in train if key(t)==k)) for k in sorted({key(t) for t in train})})
        for name in ('majority','ranked'):
            ps=[]
            for t in test:
                labels=[r[ledger] for r in train if key(r)==key(t)]
                pred=vote(labels) if name=='ranked' and labels else majority
                ps.append(dict(ledger=ledger,method=name,Z=t['Z'],symbol=t['symbol'],actual=t[ledger],
                               predicted=pred,training_examples_with_same_feature=len(labels)))
            print(name,summary(ps))
            predictions.extend(ps)
    save('heldout_affinities.csv',predictions)
    print('PASS')
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    for argument in ('extended','mixer','output'):p.add_argument(argument,type=Path)
    run(p.parse_args())

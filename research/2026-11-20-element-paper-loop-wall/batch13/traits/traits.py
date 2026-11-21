"""Subshell occupation comparisons on each complete Ba–Tb NIST ladder."""
import csv
import sys
from collections import Counter
from pathlib import Path

DIR = Path(__file__).resolve().parent
PAPER = DIR.parents[1]
sys.path.insert(0, str(PAPER/'batch11/independent'))
from assign_openings import occupation

ORBITALS = 'spdf'
MODELS = ('Kilbane_2010', 'Banerjee_2023', 'Carvajal_2024')


def key(orbital):
    return (int(orbital[:-1]), ORBITALS.index(orbital[-1]))


def describe(vector):
    return ' '.join(f'{orb}:{vector[orb]}' for orb in sorted(vector,key=key) if vector[orb])


def compare(initial,final):
    if sum(initial.values())-sum(final.values()) != 1:
        raise ValueError('threshold must remove exactly one electron')
    for v in (initial,final):
        if any(n<0 or n>2*(2*key(o)[1]+1) for o,n in v.items()):
            raise ValueError('invalid subshell occupation')
    kept = initial & final
    lost = initial-final
    gained = final-initial
    r = sum(gained.values())
    k = sum(kept.values())
    l1 = sum(abs(initial[o]-final[o]) for o in initial.keys()|final.keys())
    if l1 != 2*r+1 or sum(final.values()) != k+r or sum(lost.values()) != r+1:
        raise ValueError('retention and net loss do not agree')
    unchanged = {o:n for o,n in initial.items() if n==final[o] and n}
    return dict(K=k,R=r,l1=l1,lost=describe(lost),gained=describe(gained),retained=describe(kept),
                occupied_before=len(initial),occupied_after=len(final),unchanged_count=len(unchanged),
                unchanged=describe(unchanged))


def load(path):
    with path.open() as f:
        return list(csv.DictReader(f))


def write(name, rows):
    with (DIR/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys(),lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


def main():
    files=[PAPER/f'batch{n}/ladder/asd_states_20261121.csv' for n in (12,13)]
    entries=[entry for path in files for entry in load(path)]
    states={(int(r['Z']),int(r['q'])):r for r in entries}
    if len(entries)!=len(states) or set(states)!={(z,q) for z in range(56,66) for q in range(z)}:
        raise ValueError('missing, duplicate or spurious ion')
    mainrows=[]
    summary=[]
    for z in range(56,66):
        path=[]
        records=[]
        for q in range(z):
            state=states[z,q]; sym=state['element']
            initial=state['ground_shells']
            final=states[z,q+1]['ground_shells'] if q+1<z else ''
            a,b=occupation(initial),occupation(final)
            assert sum(a.values())==z-q
            metrics=compare(a,b)
            grade={'[':'S','(':'T'}.get(state['NIST_energy_eV'][0],'E')
            r=dict(Z=z,element=sym,removal_k=q+1,before_q=q,after_q=q+1,remaining=z-q-1,
                   ASD_before=initial,ASD_after=final or 'bare',
                   threshold_grade=grade,threshold_ref=state['NIST_refs'],**metrics)
            mainrows.append(r)
            records.append(r)
            path.append(metrics['R'])
        positive=[r for r in records if r['R']]
        summary.append(dict(Z=z,element=sym,transitions=z,R0=path.count(0),R_positive=len(positive),
                            largest_R=max(path),sum_R=sum(path),
                            removals_with_positive_R=' '.join(str(r['removal_k']) for r in positive)))
    alts=load(DIR/'table_A2.csv')
    bykey={(int(r['Z']),int(r['q'])):r for r in alts}
    model_rows=[]
    for z in range(57,66):
        for q in range(3,7):
            inset=(z,q) in bykey and (z,q+1) in bykey
            # The two adjacent flanks involve one term outside Table A.2.
            coverage='two tabulated states' if inset else 'one tabulated state plus ASD flank'
            b=occupation(states[z,q]['ground_shells'])
            a=occupation(states[z,q+1]['ground_shells'])
            base=compare(b,a)
            for model in MODELS:
                pair=[bykey[z,i][model] if (z,i) in bykey else states[z,i]['ground_shells']
                      for i in (q,q+1)]
                for i,nist_occ in ((q,b),(q+1,a)):
                    if (z,i) in bykey:
                        assert occupation(bykey[z,i]['NIST_in_2024_table'])==nist_occ
                alt=compare(*[occupation(cfg) for cfg in pair])
                model_rows.append(dict(Z=z,symbol=bykey[z,4]['symbol'],removal_k=q+1,
                    coverage=coverage,model=model,alternate_before=pair[0],alternate_after=pair[1],
                    ASD_R=base['R'],alternate_R=alt['R'],ASD_K=base['K'],alternate_K=alt['K'],
                    ASD_lost=base['lost'],alternate_lost=alt['lost'],
                    ASD_gained=base['gained'],alternate_gained=alt['gained'],
                    changes_R=base['R']!=alt['R'],
                    changes_identity=(base['lost'],base['gained'])!=(alt['lost'],alt['gained'])))
    write('occupancy_ledger.csv',mainrows)
    write('summary.csv',summary)
    write('alternative_configurations.csv',model_rows)
    for s in summary:
        print(s['element'],s['R_positive'],s['sum_R'],s['removals_with_positive_R'])
    print('Histogram of R on 605 ASD transitions:',sorted(Counter(r['R'] for r in mainrows).items()))
    for coverage in ['two tabulated states','one tabulated state plus ASD flank']:
        for model in MODELS:
            subset=[r for r in model_rows if r['coverage']==coverage and r['model']==model]
            print(coverage,model,'R changes',[(r['symbol'],r['removal_k'],r['ASD_R'],r['alternate_R'])
                for r in subset if r['changes_R']],'; net loss/gain changes',sum(r['changes_identity'] for r in subset))

if __name__=='__main__':
    main()

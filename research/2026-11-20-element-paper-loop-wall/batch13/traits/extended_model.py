"""Compare 108 true in-table transitions, including the high-charge gadolinium case."""
import argparse
import bisect
import re
import csv
from pathlib import Path
from traits import DIR, PAPER, load, occupation, compare, write

SYMS = ['La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb']
STAGES = 'V VI VII VIII IX X XI XII XIII XIV XV XVI XVII'.split()


def expand(cell,electrons):
    groups=re.findall(r'([45][spdf])(\d*?)(?=[45][spdf]|$)',cell)
    if not groups or ''.join(o+n for o,n in groups)!=cell:
        raise ValueError(('unparsed cell',cell))
    tail=''.join(o+(f'^{{{n}}}' if n else '') for o,n in groups)
    for core in ('[Kr]','[Kr]4d^{10}','[Cd]'):
        occ=occupation(core)
        if any(o in occ for o,n in groups):
            continue
        cfg=core+tail
        if sum(occupation(cfg).values())==electrons:
            return cfg
    raise ValueError(('no valid inherited core',electrons,cell))


def extract(pdf):
    import pymupdf
    doc=pymupdf.open(pdf)
    page,=[p for p in doc if 'TABLE II. Ground' in p.get_text()]
    words=page.get_text('words')
    anchor,=[w for w in words if w[4]=='VIII']
    cols=sorted((w for w in words if abs(w[1]-anchor[1])<.4 and w[4] in STAGES),key=lambda w:w[0])
    assert [w[4] for w in cols]==STAGES
    fields=[w[0]-.5 for w in cols]
    output=[]
    for z,sym in enumerate(SYMS,57):
        row,=[w for w in words if w[4]==sym and w[0]<fields[0] and w[1]>anchor[1]]
        cells=['']*13
        for word in sorted(words,key=lambda w:w[0]):
            if abs(word[1]-row[1])>3 or word[0]<fields[0]:
                continue
            column=bisect.bisect_right(fields,word[0])-1
            cells[column]+=word[4]
        for q,raw in enumerate(cells,4):
            output.append(dict(Z=z,symbol=sym,q=q,source_cell=raw,expanded=expand(raw,z-q)))
    write('kilbane_2010.csv',output)


def evaluate():
    data=load(DIR/'kilbane_2010.csv')
    model={(int(r['Z']),int(r['q'])):r['expanded'] for r in data}
    assert len(model)==117
    for row in load(DIR/'table_A2.csv'):
        assert occupation(model[int(row['Z']),int(row['q'])])==occupation(row['Kilbane_2010'])
    states={}
    for n in (12,13):
        for r in load(PAPER/f'batch{n}/ladder/asd_states_20261121.csv'):
            states[int(r['Z']),int(r['q'])]=r['ground_shells']
    result=[]
    for z,sym in enumerate(SYMS,57):
        for q in range(4,16):
            bb,aa=states[z,q],states[z,q+1]
            b,a=model[z,q],model[z,q+1]
            base=compare(occupation(bb),occupation(aa))
            alt=compare(occupation(b),occupation(a))
            result.append(dict(Z=z,symbol=sym,removal_k=q+1,ASD_before=bb,ASD_after=aa,
                        model_before=b,model_after=a,ASD_R=base['R'],model_R=alt['R'],
                        ASD_lost=base['lost'],ASD_gained=base['gained'],model_lost=alt['lost'],
                        model_gained=alt['gained'],changes_R=base['R']!=alt['R'],
                        changes_identity=(base['lost'],base['gained'])!=(alt['lost'],alt['gained'])))
    write('extended_comparison.csv',result)
    print('108 paired transitions; R changes',sum(r['changes_R'] for r in result),
          '; loss/gain identity changes',sum(r['changes_identity'] for r in result))
    for r in result:
        if r['changes_R']:
            print(r['symbol'],r['removal_k'],r['ASD_R'],'->',r['model_R'])
    print('ASD R sum',sum(r['ASD_R'] for r in result),'model R sum',sum(r['model_R'] for r in result))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--extract-pdf',type=Path)
    args=p.parse_args()
    if args.extract_pdf:
        extract(args.extract_pdf)
    evaluate()

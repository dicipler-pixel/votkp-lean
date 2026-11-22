"""Join the separately frozen ratings to source grades. No claim excerpts are printed."""
from collections import Counter
from pathlib import Path
import csv,sys
root=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent
def read(name):
    with (root/name).open() as f:
        rows=list(csv.DictReader(f,delimiter='\t'))
    return {r['token']:r for r in rows}
key=read('answer_key.tsv'); a=read('rater_a.tsv'); b=read('rater_b.tsv')
assert len(key)==24 and a.keys()==b.keys()==key.keys()
assert all(row['label'] in ('E','O','M','U') for r in (a,b) for row in r.values())
for lab,ratings in [('A',a),('B',b)]:
    print(lab,'coverage:',dict(sorted(Counter(r['label'] for r in ratings.values()).items())))
    print(lab,'by original grade:',dict(sorted(Counter((r['label'],key[k]['old_grade']) for k,r in ratings.items()).items())))
same=sum(a[k]['label']==b[k]['label'] for k in key)
agreement=Counter((a[k]['label'],b[k]['label']) for k in key)
print('all agreements',same,'/',len(key), list(sorted(agreement.items())))
joint=[]
for k,entry in key.items():
    if a[k]['label']==b[k]['label'] and a[k]['label'] in ('E','O'):
        guess='T' if a[k]['label']=='E' else 'F'
        joint.append((k,entry['id'],a[k]['label'],guess,entry['old_grade'],guess==entry['old_grade']))
for row in joint:print('scoreable:',*row)
print('joint coverage and correct',len(joint),sum(r[-1] for r in joint))
for k in key:
    if a[k]['label']!=b[k]['label']:print('disagreed',k,key[k]['id'],a[k]['label'],b[k]['label'])

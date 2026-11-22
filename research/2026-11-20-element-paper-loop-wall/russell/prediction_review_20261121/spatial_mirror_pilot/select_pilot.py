"""Build questions from signed public sources. Do not send grades or the key to raters."""
import argparse, ast, csv, hashlib, json, re, zipfile
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('bundle',type=Path);p.add_argument('out',type=Path)
a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(a.bundle) as z:
    read=lambda f:z.read('russell-rebuild/ledger/'+f).decode()
    quotes=read('ledger_read3.md').split('## THOUGHT-PROCESS MAP')[0]
    laws=ast.literal_eval(next(x.value for x in ast.parse(read('laws_uo.py')).body if isinstance(x,ast.Assign)))
    law_body=ast.parse(read('laws_class.py')).body
items={}
for k,pg,raw in re.findall(r'(?ms)^([GU]\d+)\s*\|\s*([^|]+?)\s*\|(.*?)(?=^[GU]\d+\s*\||^##|\Z)',quotes):
    m=re.search(r'\|\s*([ABCD](?:[/→][ABCD])*|—)\s*\|\s*([^|]+)\s*\|',raw)
    items[k]=(' '.join(raw[:m.start()].strip().split()),m[2].strip())
for n,law,page in laws:items['L'+str(n)]=(law,'')
for node in law_body:
    if not (isinstance(node,ast.Expr) and isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Name) and node.value.func.id=='c'):continue
    ns,_,grade=node.value.args[:3]
    numbers=range(*(ast.literal_eval(v) for v in ns.args)) if isinstance(ns,ast.Call) else ast.literal_eval(ns)
    for n in ([numbers] if isinstance(numbers,int) else numbers):
        k='L'+str(n);items[k]=(items[k][0],ast.literal_eval(grade))
assert len(items)==585
def h(k,prefix):return hashlib.sha256(('Jeromie-20261121-spatial-inversion-pilot-v1|'+prefix+'|'+k).encode()).hexdigest()
chosen=[]
# Keep all source collections represented. Pure original grades only. Four
# independent quoted claims of each grade per source yields 24 observations.
for source in 'GUL':
    for grade in ('T','F'):
        pool=sorted((k for k,v in items.items() if k.startswith(source) and v[1]==grade),key=lambda k:h(k,'selection'))
        chosen+=pool[:4]
order=sorted(chosen,key=lambda k:h(k,'order'))
with (a.out/'blind.tsv').open('w') as f, (a.out/'answer_key.tsv').open('w') as key:
    w=csv.writer(f,delimiter='\t');v=csv.writer(key,delimiter='\t');w.writerow(('token','claim'));v.writerow(('token','id','old_grade'))
    for i,k in enumerate(order):
        token='P%02d'%(i+1);w.writerow((token,' '.join(items[k][0].split())));v.writerow((token,k,items[k][1]))
print('Source records',len(items),'selected',len(order))

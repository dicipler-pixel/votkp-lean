"""Independently check all Os–Hg printed rows and each reported rectangular wall."""
import hashlib
import importlib.util
from pathlib import Path
DIR=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('parent_verify',DIR.parents[1]/'batch13/ladder/verify.py')
core=importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)

def check(xs):
    return core.check(xs,DIR,first=76,last=80,outside=[('Os',0)])

def run():
    path=DIR/'batch16_os_hg.csv'
    original=core.read(path)
    result=check(original)
    print('Pinned archive SHA256:',core.HASH)
    print('Printed CSV SHA256:',hashlib.sha256(path.read_bytes()).hexdigest())
    print('Printed rows:',len(original))
    for k,v in sorted(result.items()):
        print(k,v)
    def invent(xs):
        next(r for r in xs if r['symbol']=='Hg' and r['k']=='0')['IE_k (eV)']='0.005'
    def confuse(xs):
        next(r for r in xs if r['symbol']=='Hg' and r['k']=='0')['source']='bound'
    def wrong(xs):
        next(r for r in xs if r['symbol']=='Os' and r['k']=='0')['IE_k (eV)']='1.029'
    def ratio(xs):
        xs[14]['Gamma_k']='-0.100000'
    for label,mutate in [('Hg sensitivity limit as point',invent),('Hg falsely bound',confuse),
                         ('wrong Os source',wrong),('changed reflection',ratio),
                         ('missing bare-nucleus row',lambda x:x.pop())]:
        xs=[r.copy() for r in original]
        mutate(xs)
        try:
            check(xs)
        except ValueError:
            print('rejected:',label)
        else:
            raise AssertionError('false control passed: '+label)
if __name__=='__main__':
    run()

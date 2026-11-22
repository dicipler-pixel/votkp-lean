"""Compile every named positive theorem in the self-contained research files and audit axiom use."""
from pathlib import Path
import argparse,os,re,shutil,subprocess,tempfile
from concurrent.futures import ThreadPoolExecutor
p=argparse.ArgumentParser();p.add_argument('root',type=Path);p.add_argument('--bin',type=Path,required=True)
p.add_argument('--skip-kernel',action='store_true')
a=p.parse_args();root=a.root.resolve();bin=a.bin.resolve()
names=['TwoFaceForms','BoundaryAgreement','ObliqueFaces','FiniteWallGap','PellControls','OpticalWall','PreparedRoute','HalfPower','FaceFidelity','TripleReadout']
env=dict(os.environ,PATH=str(bin)+os.pathsep+os.environ['PATH'])
def check(name):
    paths=list(root.rglob(name+'.lean'));assert len(paths)==1,(name,paths)
    src=paths[0].read_text()
    # Files have one outer namespace (or none), with no reserved theorem keywords inside comments.
    chunks=re.split(r'/-.*?-/',src,flags=re.S);code=' '.join(chunks)
    ns=re.findall(r'^namespace (\S+)',code,re.M);assert len(ns)<=1
    decls=re.findall(r'^\s*(?:(?:private|protected)\s+)?(?:theorem|lemma)\s+([^\s(:]+)',code,re.M)
    qualified=[(ns[0]+'.' if ns else '')+n for n in decls]
    assert qualified and len(set(qualified))==len(qualified)
    with tempfile.TemporaryDirectory() as d:
        tmp=Path(d)
        shutil.copyfile(paths[0],tmp/(name+'.lean'))
        def run(args,where=tmp,custom_env=env):
            r=subprocess.run(args,cwd=where,capture_output=True,text=True,env=custom_env,timeout=300)
            if r.returncode: raise RuntimeError((args,r.stdout,r.stderr))
            return r.stdout+r.stderr
        run([str(bin/'lean'),'-o',name+'.olean',name+'.lean'])
        e=dict(env,LEAN_PATH=d)
        (tmp/'AllAxioms.lean').write_text('import '+name+'\n'+'\n'.join('#print axioms '+n for n in qualified)+'\n')
        output=run([str(bin/'lean'),'AllAxioms.lean'],custom_env=e)
        axioms=set()
        for n in qualified:
            line=[l for l in output.splitlines() if l.startswith("'"+n+"' ")]
            assert len(line)==1,(n,line)
            if 'does not depend on any axioms' in line[0]:continue
            m=re.search(r'depends on axioms: \[(.*?)\]',line[0]);assert m,line
            axioms.update(m[1].split(', '))
        assert axioms<= {'propext','Classical.choice','Quot.sound'},axioms
        if not a.skip_kernel:
            run([str(bin/'leanchecker'),name],custom_env=e)
        if name=='BoundaryAgreement':
            control=next(root.rglob('FalseAtThird.lean'))
            shutil.copyfile(control,tmp/control.name)
            r=subprocess.run([str(bin/'lean'),control.name],cwd=tmp,env=e,capture_output=True,text=True)
            assert r.returncode and re.search(r'error: .*grind.* failed',r.stdout+r.stderr)
        return name,len(decls),sorted(axioms)
print(subprocess.check_output([str(bin/'lean'),'--version'],text=True).strip(),flush=True)
with ThreadPoolExecutor(max_workers=2) as executor:
    rows=[]
    for row in executor.map(check,names):
        rows.append(row);print(row[0],row[1],', '.join(row[2]),flush=True)
print('modules',len(rows),'named theorems',sum(n for _,n,_ in rows),'leanchecker',not a.skip_kernel,'negative control rejected',flush=True)

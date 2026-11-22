"""Regenerate selected committed result files from public inputs only; no web access."""
import argparse,csv,hashlib,os,subprocess,sys,tempfile,zipfile
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('archive',type=Path);p.add_argument('--root',type=Path,default=Path(__file__).parent)
a=p.parse_args();root=a.root.resolve();arc=a.archive.resolve()
assert hashlib.sha256(arc.read_bytes()).hexdigest()=='75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
def run(script,*args):
    return subprocess.check_output([sys.executable,str(root/script),*map(str,args)],env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
def equal(data,reference):
    expected=(root/reference).read_bytes()
    if data!=expected:raise ValueError('reproduction difference: '+reference)
    print('MATCH',reference,len(data),flush=True)
with tempfile.TemporaryDirectory() as d:
    tmp=Path(d)
    with zipfile.ZipFile(tmp/'scores.zip','w') as z:
        z.write(root/'H_to_At_thresholds.csv','H_to_At_thresholds.csv')
    for script,output in [('check_rivals.py','rival_boxes.csv'),('si_ag_dependency.py','si_ag_shared_boxes.csv')]:
        run('rivals/'+script,tmp/'scores.zip',arc,tmp);equal((tmp/output).read_bytes(),'rivals/'+output)
    for script,refs in [('scan.py',['heavy_archived_pairs.csv']),('literature.py',['heavy_affinity_screen.csv','additional_ordinary_theory.csv'])]:
        run('ground_state_search/'+script,arc,tmp)
        for f in refs: equal((tmp/f).read_bytes(),'ground_state_search/'+f)
    run('hydrogenic_pairs/pair_scan.py',arc,tmp)
    for f in ('candidates.csv','comparison.csv'):equal((tmp/f).read_bytes(),'hydrogenic_pairs/'+f)
    for script,reference in [('channel_search/check.py','channel_search/result.csv'),('channel_search/check_path.py','channel_search/path_result.csv')]:
        equal(run(script,arc),reference)
    for stem,log in [('channel_search/oxygen_settings','oxygen_settings.txt'),('precision/photon_budget','photon_budget.txt'),('real_port/energy_map_control','energy_map_control.txt'),('hydrogenic_orbitals/all_orbitals','outputs.txt'),('spatial_mirror_pilot/score_pilot','result.txt')]:
        equal(run(stem+'.py'),stem.rsplit('/',1)[0]+'/'+log)
print('All selected output bytes match.')

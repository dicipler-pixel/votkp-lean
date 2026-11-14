archive/neutrinos/ledger_test/batch.py

\# SCRIPT: BATCH run a list of (tag, delta, hspec, eps_max, N, K) jobs on 2 cores; append results to a jsonl (restartable: done t ags skipped) import sys, os, json, time from multiprocessing import Pool SIM = __import__('os').environ.get('MCCORMICK_SIM', 'PBH_neutrino_simulation/simulation') sys.path.insert(0, SIM); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))) def one(job):

from run_burst import run tag, d, h, em, N, K = job t1 = time.time() try: o = run(d, fnu=0.409, N=N, K=K, eps0=0.1, eps_max=em, qshape=1.0, hspec=h, kapcap=5e5)

H = o\['hist'\] r = dict(tag=tag, d=d, hspec=h, N=N, K=K, status=o\['status'\], eps=float(o\['eps'\]), peakC=float(o\['peakC'\]),

eps_peak=float(o\['eps_peak'\]), steps=int(o\['steps'\]), capsteps=int(o\['capsteps'\]), sec=time.time()-t1, hist_eps=\[float(x) for x in H\[::5, 1\]\], hist_C=\[float(x) for x in H\[::5, 2\]\], hist_r=\[float(x) for x in H\[::5, 3\]\]) except Exception as ex:

r = dict(tag=tag, d=d, hspec=h, status='error:' + repr(ex)\[:120\], sec=time.time()-t1) return r if __name__ == '__main__':

jobs = json.load(open(sys.argv\[1\])); out = sys.argv\[2\] done = set() if os.path.exists(out):

for line in open(out):

try: done.add(json.loads(line)\['tag'\]) except Exception: pass todo = \[j for j in jobs if j\[0\] not in done\] print('todo', len(todo), flush=True) with Pool(2) as p:

for r in p.imap_unordered(one, todo):

with open(out, 'a') as f: f.write(json.dumps(r) + '\\n') print(r\['tag'\], r\['d'\], r\['status'\], 'peakC=%.6f' % r.get('peakC', float('nan')), 'eps_peak=%.3f' % r.get('eps_peak', float('nan')),

'eps=%.2f' % r.get('eps', float('nan')), 'steps', r.get('steps'), '%.0fs' % r\['sec'\], flush=True)



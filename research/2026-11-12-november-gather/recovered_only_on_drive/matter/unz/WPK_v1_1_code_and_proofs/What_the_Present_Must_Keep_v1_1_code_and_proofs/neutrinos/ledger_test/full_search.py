# SCRIPT: FULL-SEARCH  three-valued trisection for delta_c under a general collision history (logic copied from next/runs/trisect3.py;
# only the run call differs: run_burst.run with hspec). 'U' (undecided/crash) points never move the bracket; retried once at eps_max*1.5.
# Added: edge flag if the final bracket still touches an initial end (the true threshold may then lie outside).
# Usage: full_search.py queue.json   (list of [tag, hspec, lo, hi, tol]); results appended to full_results.jsonl, skip tags already done.
import sys, os, json, time
from multiprocessing import Pool
SIM = __import__('os').environ.get('MCCORMICK_SIM', 'PBH_neutrino_simulation/simulation')
sys.path.insert(0, SIM); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
N, K, EM = 400, 32, 14.0
MAXST = 250000   # a near-critical run stalls (self-similar shrinking core); such a run is 'U' and is not retried
def classify(s): return 'C' if s == 'BH' else ('D' if s == 'dispersed' else 'U')
def one(a):
    from run_burst import run
    d, h, em = a; t1 = time.time()
    try:
        o = run(d, fnu=0.409, N=N, K=K, eps0=0.1, eps_max=em, qshape=1.0, hspec=h, kapcap=5e5, max_steps=MAXST)
        i = dict(d=d, status=o['status'], eps=float(o['eps']), steps=int(o['steps']), sec=time.time()-t1, eps_max=em)
    except Exception as ex:
        i = dict(d=d, status='error:' + repr(ex)[:80], eps=float('nan'), steps=-1, sec=time.time()-t1, eps_max=em)
    i['out'] = classify(i['status']); return i
def search(tag, h, lo, hi, tol, p):
    lo0, hi0 = lo, hi; log = []; und = []; nonmono = False; t0 = time.time()
    while hi - lo > tol:
        a = lo + (hi-lo)/3; b = lo + 2*(hi-lo)/3
        res = p.map(one, [(a, h, EM), (b, h, EM)])
        bad = [k for k, i in enumerate(res) if i['out'] == 'U' and i['status'] != 'stepcap']
        for i in res:
            if i['status'] == 'stepcap': und.append((i['d'], 'stepcap'))
        if bad:
            rr = p.map(one, [(res[k]['d'], h, EM*1.5) for k in bad])
            for k, i in zip(bad, rr):
                i['retry'] = True
                if i['out'] == 'U': und.append((i['d'], i['status']))
                res[k] = i
        for i in res: log.append(i); print(tag, 'delta=%.6f %s [%s] eps=%.2f %.0fs' % (i['d'], i['out'], i['status'], i['eps'], i['sec']), flush=True)
        oa, ob = res[0]['out'], res[1]['out']
        if oa == 'U' and ob == 'U': print(tag, 'STOP both undecided', flush=True); break
        if oa == 'D' and ob == 'C': lo, hi = a, b
        elif oa == 'C' and ob == 'D': nonmono = True; print(tag, 'STOP non-monotonic', flush=True); break
        elif oa == 'C': hi = a
        elif ob == 'D': lo = b
        elif oa == 'D': lo = a
        elif ob == 'C': hi = b
        print(tag, 'bracket [%.6f, %.6f]' % (lo, hi), flush=True)
    edge = (lo == lo0) or (hi == hi0)
    r = dict(tag=tag, hspec=h, lo=lo, hi=hi, dc=0.5*(lo+hi), err=0.5*(hi-lo), edge=edge, nonmono=nonmono, undecided=und,
             minutes=(time.time()-t0)/60, log=log, N=N, K=K)
    print('RESULT %s delta_c=%.6f +- %.6f edge=%s (%.1f min)' % (tag, r['dc'], r['err'], edge, r['minutes']), flush=True)
    return r
if __name__ == '__main__':
    Q = json.load(open(sys.argv[1])); out = 'full_results.jsonl'; done = set()
    if os.path.exists(out):
        for l in open(out): done.add(json.loads(l)['tag'])
    with Pool(2) as p:
        for tag, h, lo, hi, tol in Q:
            if tag in done: continue
            r = search(tag, h, lo, hi, tol, p)
            with open(out, 'a') as f: f.write(json.dumps(r) + '\n')

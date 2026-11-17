# SCRIPT: SEA-EXPORT-01
# Stores the rest seas the page needs (the tied way), and reference numbers for checking the page's own sea mathematics against SEA-RUNS-01.
import json, base64, importlib.util, numpy as np
sp_ = importlib.util.spec_from_file_location('sr', 'sea_runs_01.py'); m = importlib.util.module_from_spec(sp_); sp_.loader.exec_module(m)
out = {}; ref = {}
for world, N, clocks, ends in (('w3_v2', 3, 'z', 'sealed'), ('w3_v2', 3, 'equal', 'sealed'), ('w3_v2', 3, 'dilation', 'sealed'), ('w3_v2', 3, 'z', 'container'), ('w7c_v2', 7, 'z', 'sealed')):
    cfg = dict(world=world, machine='C', ends=ends, clocks=clocks, feed='kick', push=True, T=30.0); r = m.run(cfg); key = ('C', world, clocks, ends == 'container'); P, mg, rk, ud = m._REST[key]; M = P.shape[0]
    iu = np.triu_indices(M); tri = np.empty(2*len(iu[0]), np.float32); tri[0::2] = P[iu].real; tri[1::2] = P[iu].imag
    out['%d|%s|%s' % (N, clocks, 'container' if ends == 'container' else 'sealed')] = dict(M=M, rank=rk, margin=mg, h=m.world(world)['h'], b64=base64.b64encode(tri.tobytes()).decode())
    ref['%d|%s|%s' % (N, clocks, ends)] = dict(M=M, rank=rk, trace_end=r['trace_end'], lifted_end=r['lifted_end'], tie_at_start=r['tie_at_start'], tie_end=r['tie_end'], first_move_time=r['first_move_time'], ball_turn_max=r['ball_turn_max'], unitary_dev=ud)
    print(N, clocks, ends, 'M', M, 'rank', rk, 'margin %.4f' % mg, 'bytes', len(out[list(out)[-1]]['b64']), {k: v for k, v in ref[list(ref)[-1]].items() if k not in ('M', 'rank')})
json.dump(out, open('rest_seas_01.json', 'w')); json.dump(ref, open('rest_ref_01.json', 'w'))

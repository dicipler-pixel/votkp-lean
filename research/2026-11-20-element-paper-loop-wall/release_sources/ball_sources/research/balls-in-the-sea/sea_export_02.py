# SCRIPT: SEA-EXPORT-02
# Adds the rest seas for 4 balls (ratio clocks and equal clocks) and for 7 balls with equal clocks to those stored by SEA-EXPORT-01. Same method.
import json, base64, importlib.util, numpy as np
sp_ = importlib.util.spec_from_file_location('sr', 'sea_runs_01.py'); m = importlib.util.module_from_spec(sp_); sp_.loader.exec_module(m)
out = json.load(open('rest_seas_01.json')); ref = json.load(open('rest_ref_01.json'))
for world, N, clocks, ends in (('w4_v2', 4, 'z', 'sealed'), ('w4_v2', 4, 'equal', 'sealed'), ('w7c_v2', 7, 'equal', 'sealed')):
    cfg = dict(world=world, machine='C', ends=ends, clocks=clocks, feed='kick', push=True, T=30.0); r = m.run(cfg); key = ('C', world, clocks, False); P, mg, rk, ud = m._REST[key]; M = P.shape[0]
    iu = np.triu_indices(M); tri = np.empty(2*len(iu[0]), np.float32); tri[0::2] = P[iu].real; tri[1::2] = P[iu].imag; k = '%d|%s|sealed' % (N, clocks)
    out[k] = dict(M=M, rank=rk, margin=mg, h=m.world(world)['h'], b64=base64.b64encode(tri.tobytes()).decode())
    ref[k] = dict(M=M, rank=rk, trace_end=r['trace_end'], lifted_end=r['lifted_end'], tie_at_start=r['tie_at_start'], tie_end=r['tie_end'], first_move_time=r['first_move_time'], ball_turn_max=r['ball_turn_max'], unitary_dev=ud, proj_dev=r.get('proj_dev'))
    print(k, 'M', M, 'rank', rk, 'margin %.4f' % mg, {a: b for a, b in ref[k].items() if a not in ('M', 'rank')})
json.dump(out, open('rest_seas_02.json', 'w')); json.dump(ref, open('rest_ref_02.json', 'w'))

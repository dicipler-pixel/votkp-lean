# SCRIPT: SEA-EXPORT-03 — the 7-ball ratio-clock rest sea in double precision (the others stay as SEA-EXPORT-02 left them).
import json, base64, importlib.util, numpy as np
sp_ = importlib.util.spec_from_file_location('sr', 'sea_runs_02.py'); m = importlib.util.module_from_spec(sp_); sp_.loader.exec_module(m)
out = json.load(open('rest_seas_02.json'))
cfg = dict(world='w7c_v2', machine='C', ends='sealed', clocks='z', feed='kick', push=True, T=30.0); r = m.run(cfg); P, mg, rk, ud = m._REST[('C', 'w7c_v2', 'z', False)]; M = P.shape[0]
iu = np.triu_indices(M); tri = np.empty(2*len(iu[0]), np.float64); tri[0::2] = P[iu].real; tri[1::2] = P[iu].imag
out['7|z|sealed'] = dict(M=M, rank=rk, margin=mg, h=m.world('w7c_v2')['h'], double=True, b64=base64.b64encode(tri.tobytes()).decode()); json.dump(out, open('rest_seas_03.json', 'w')); print('7|z|sealed double', M, rk, len(out['7|z|sealed']['b64']))

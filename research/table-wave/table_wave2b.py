# SCRIPT: TABLE-WAVE-02B  (noise line for the period-pair wave; kill: 0.352 not above the 99th percentile of 500 shuffles)
import json, numpy as np
exec(open('table_wave2.py').read().split("fs1=np.linspace")[0])
fs2=np.linspace(0.35,0.65,61); rng=np.random.default_rng(6)
sh=[best(u_cub,rng.permutation(y),fs2,3)[0] for _ in range(500)]
print('period-pair wave in the cube-root coordinate: 0.352 ; shuffles median %.3f, 99th percentile %.3f, share of shuffles above 0.352: %.3f'%(np.median(sh),np.percentile(sh,99),np.mean(np.array(sh)>=0.352)))

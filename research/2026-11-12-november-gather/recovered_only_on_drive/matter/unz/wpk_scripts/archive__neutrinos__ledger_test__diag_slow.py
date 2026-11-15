archive/neutrinos/ledger_test/diag_slow.py

\# SCRIPT: DIAG-SLOW find why a near-threshold fully-coupled run stalls: run with progress prints every 20000 steps (wraps run_bu rst via a step cap) import sys, os, time, numpy as np sys.path.insert(0, __import__('os').environ.get('MCCORMICK_SIM', 'PBH_neutrino_simulation/simulation')) sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))) from run_burst import run d = float(sys.argv\[1\]); em = float(sys.argv\[2\]) t1 = time.time() o = run(d, fnu=0.409, N=400, K=32, eps0=0.1, eps_max=em, qshape=1.0, hspec={'base': \['const', 1e4\]}, kapcap=5e5) H = o\['hist'\] print(d, o\['status'\], 'eps=%.3f steps=%d %.0fs' % (o\['eps'\], o\['steps'\], time.time()-t1)) for row in H\[::max(1, len(H)//25)\]: print(' eps %.3f Cmax %.4f r %.3f' % (row\[1\], row\[2\], row\[3\])) print(' last', H\[-1\]\[1\], H\[-1\]\[2\], H\[-1\]\[3\])



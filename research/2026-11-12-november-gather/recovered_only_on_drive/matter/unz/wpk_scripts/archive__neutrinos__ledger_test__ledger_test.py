archive/neutrinos/ledger_test/ledger_test.py

\# SCRIPT: LEDGER-TEST checks of ledger.py: (1) instant: S from tau0 must equal sum w j0(k(tau-tau0))^2 ; (2) burst on coupled ba se vs pure-streaming formula import numpy as np, time from ledger import \* from scipy.special import spherical_jn t1=time.time() tg=np.array(\[0.1,0.5,1.0,1.7,3.0,6.0\]) S=S_curve({'base':\['inst'\]},tg) ex=np.array(\[sum(w\*spherical_jn(0,k\*(t-0.1))\*\*2 for k,w in zip(ks,wE)) for t in tg\]) print('inst S', np.round(S,6)); print('j0^2 ', np.round(ex,6), 'maxdiff %.2e'%np.abs(S-ex).max(), '%.1fs'%(time.time()-t1)) t1=time.time() for eb in (1.0,3.0):

tg=np.array(\[eb,1.25\*eb,1.25\*eb\*1.01,14.0\]) Sb=S_curve({'base':\['const',1e4\],'windows':\[\[eb,1.25\*eb,0.0\]\]},tg) S0=S_curve({'base':\['const',1e4\]},tg) pure=sum(w\*spherical_jn(0,k\*0.25\*eb)\*\*2 for k,w in zip(ks,wE)) print('eb',eb,'Sbase',np.round(S0,6),'Sburst',np.round(Sb,6),'ledger=%.6f'%((S0\[-1\]-Sb\[-1\])),'1-sum w j0^2(k\*0.25eb)=%.6f'%(1 -pure),'%.1fs'%(time.time()-t1))



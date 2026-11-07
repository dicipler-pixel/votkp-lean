# SCRIPT: FILM-GEO-LINK-01
# Exploratory. In FILM-PHASE-01 some pairs (Ag-Na, K-Na, Mg-Na, K-Mg) had large phase gaps but small film colour gaps.
# Question: is the film's under-reading set by how close both tracks ride to the rim (the ground, Gamma = -1),
# i.e. by the pair's smaller geometric turn? Residual of film gap after phase gap, against the pair's min |turn|.
import subprocess, re, numpy as np
from scipy.stats import spearmanr
f=subprocess.run(['python3','-W','ignore','film_phase_01.py'],capture_output=True,text=True).stdout
g=subprocess.run(['python3','-W','ignore','geo_phase_01.py'],capture_output=True,text=True).stdout
turn={m.group(1):float(m.group(2)) for m in re.finditer(r'^ (\w+)\s+(?:True|False)\s+([+-][\d.]+)',g,re.M)}
P=[(m.group(1),m.group(2),float(m.group(4)),float(m.group(5))) for m in re.finditer(r'^\s*(\w+)-(\w+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)',f,re.M)]
ph=np.log([p[2] for p in P]); fe=np.log([p[3] for p in P]); k,c=np.polyfit(ph,fe,1); res=fe-(k*ph+c)
mt=np.array([min(abs(turn[a]),abs(turn[b])) for a,b,_,_ in P])
print('pairs',len(P),' log film gap ~ %.2f log phase gap'%k)
print('residual vs pair min|turn|: rho=%.2f p=%.4f'%spearmanr(mt,res))
for i in np.argsort(res)[:6]: print('  under-read:',P[i][0]+'-'+P[i][1],' residual %.2f'%res[i],' min|turn| %.2f'%mt[i])

# SCRIPT: MIXER-DATA-01
# Exports the real data the VOTKP mixer runs on (no invented numbers): knot tetrahedra shapes (4-8 crossings),
# all gluing solutions for 5_2, 6_1, 6_2 (from the ROOTS-DISK search), element reflection tracks (refractiveindex.info),
# the drawing spectra and torus directions (DRAWING-POLY runs), Jones polynomials of the shown knots, HOMFLY line results.
import numpy as np, snappy, warnings, re, sys, json, database_knotinfo as d
warnings.filterwarnings('ignore'); sys.path.insert(0,'/home/claude/votkp_research'); import ri_load
from roots_disk_02 import solve_all
w=np.exp(1j*np.pi/3)
out={'tet':[], 'sols':{}, 'elements':[], 'jones':{}}
KI={r['name']:r for r in d.link_list()}
for nm,r in KI.items():
    if not re.match(r'^\d+_\d+$',nm or '') or not 4<=int(nm.split('_')[0])<=8: continue
    M=snappy.Manifold(nm)
    if M.solution_type()!='all tetrahedra positively oriented': continue
    for s in M.tetrahedra_shapes('rect'): s=complex(s); out['tet'].append([round(s.real,6),round(s.imag,6),nm])
for nm in ['5_2','6_1','6_2']:
    M=snappy.Manifold(nm); zg=np.array([complex(s) for s in M.tetrahedra_shapes('rect')]); S=solve_all(M,starts=1500)
    out['sols'][nm]=[{'z':[[round(c.real,6),round(c.imag,6)] for c in s],'geo':bool(np.max(abs(s-zg))<1e-6)} for s in S]
S=ri_load.element_sets(); nonm={'B','C','Ge','Se','Si','Te'}; lv=np.linspace(0.40,0.70,31)
for el,dd in S.items():
    o=np.argsort(dd['lam']); n=np.interp(lv,dd['lam'][o],dd['n'][o]); k=np.interp(lv,dd['lam'][o],dd['k'][o])
    out['elements'].append({'el':el,'metal':el not in nonm,'n':np.round(n,4).tolist(),'k':np.round(k,4).tolist()})
for nm in ['4_1','5_2','6_1','6_3','7_4','8_5','8_20']:
    v=eval(KI[nm]['jones_polynomial_vector']); out['jones'][nm]={'lo':v[0],'c':v[2:],'vol':float(KI[nm]['volume']),'sig':int(KI[nm]['signature']),'det':int(KI[nm]['determinant'])}
out['spectra']={'4_1':[[2.02988,0],[-2.02988,0]],'5_2':[[2.82812,-3.0241],[0,1.1135],[-2.82812,-3.0241]],
 '6_1':[[3.16396,3.0789],[1.4151,0.211],[-1.4151,0.211],[-3.16396,3.0789]],
 '6_2':[[4.40083,-3.997],[1.53058,0.3291],[0,2.4011],[-1.53058,0.3291],[-4.40083,-3.997]],
 '6_3':[[5.69302,0],[0.9243,1.8906],[0.9243,-1.8906],[-0.9243,1.8906],[-0.9243,-1.8906],[-5.69302,0]]}
out['torus']={'3_1':[2,3,[5/6]],'5_1':[2,5,[1/10,9/10]],'7_1':[2,7,[3/14,5/14,13/14]],'8_19':[3,4,[11/12]],'10_124':[3,5,[14/15]]}
out['homfly']={'N':list(range(9)),'rho':[0.597,-0.067,0.863,0.819,0.784,0.811,0.842,0.853,0.858],'r2':[0.810,0.795,0.795,0.804,0.816,0.820,0.827,0.826,0.830]}
json.dump(out,open('/home/claude/mixer/votkp_data.json','w'),separators=(',',':'))
print('tet',len(out['tet']),'sols',{k:len(v) for k,v in out['sols'].items()},'elements',len(out['elements']))

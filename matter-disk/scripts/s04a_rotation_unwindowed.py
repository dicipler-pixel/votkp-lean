# SCRIPT: MATTER-PEEL-03  rapidity across the Cayley pole: rotation part of census levels on approach to the critical wall
import numpy as np
exec(open('nhssh_lib_and_s03a_occupations.py').read().split('w=1.0')[0]); w=1.0
# exact algebra check: |tanh(W/2)|<1 iff |Im W|<pi/2 (principal branch)
rng=np.random.default_rng(1); Z=rng.normal(size=4000)+1j*rng.normal(size=4000); W=np.log(Z)
print('theorem check, mismatches:',np.sum((np.abs(np.tanh(W/2))<1)!=(np.abs(W.imag)<np.pi/2)))
for zN in [-28.0]:
    print(' negative ratio z=',zN,' Im W=',np.log(complex(zN)).imag/np.pi,'pi   Gamma=',np.tanh(np.log(complex(zN))/2))
def census_rot(v,u,N=2000,Lc=80):
    nu=np.linalg.eigvals(corr(v,w,u,N,Lc)).astype(complex)
    z=(1-nu)/nu; W=np.log(z); G=1-2*nu
    return np.max(np.abs(W.imag))/np.pi, np.max(np.abs(G))
u=0.5
print('approach from v<w side (critical at v=0.5): v, max|Im W|/pi, max|Gamma|')
for v in [0.0,0.1,0.2,0.3,0.4,0.45,0.48,0.49,0.495,0.5]:
    r,g=census_rot(v,u); print(f'  v={v:5.3f}  rot={r:.4f} pi   |Gamma|max={g:.4f}  {"OUT" if g>1+1e-9 else "in"}')
print('opposite: approach from v>w side (critical at v=1.5)')
for v in [2.5,2.0,1.7,1.6,1.55,1.52,1.51,1.505,1.5]:
    r,g=census_rot(v,u); print(f'  v={v:5.3f}  rot={r:.4f} pi   |Gamma|max={g:.4f}  {"OUT" if g>1+1e-9 else "in"}')
print('inside the PT-broken zone (0.5<v<1.5):')
for v in [0.6,1.0,1.4]:
    r,g=census_rot(v,u); print(f'  v={v:5.3f}  rot={r:.4f} pi   |Gamma|max={g:.4f}  {"OUT" if g>1+1e-9 else "in"}')

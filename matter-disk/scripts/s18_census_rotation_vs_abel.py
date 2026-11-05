# SCRIPT: s18_census_rotation_vs_abel
"""s18: independent check of the Abel phase. Plain finite blocks (no commuting operator):
the largest census rotation max|Im eps|/pi over the block's levels, at the nine (u,v) points of s11,
against theta/pi from the elliptic formula. Endpoint filter |nu|,|1-nu| > 1e-9, principal log."""
import numpy as np
exec(open('s15_exit_ladder.py').read().split('out=[]')[0])
pts=[(0.3,0.4171),(0.3,0.5562),(0.3,0.6604),(0.5,0.2809),(0.5,0.3746),(0.5,0.4448),(0.7,0.0492),(0.7,0.0656),(0.7,0.0779)]
lines=[' u     v       block   census max|Im eps|/pi   Abel theta/pi    difference']
worst=0
for u,v in pts:
    th=predict(v,1.0,u)[1]/np.pi
    for L in (40,80):
        nu=np.linalg.eigvals(block(v,1.0,u,L))
        nu=nu[(np.abs(nu)>1e-9)&(np.abs(1-nu)>1e-9)]
        rot=np.max(np.abs(np.log((1-nu)/nu).imag))/np.pi
        worst=max(worst,abs(rot-th))
        lines.append(f'{u:.1f}  {v:.4f}   {L:4d}      {rot:.9f}          {th:.9f}     {rot-th:+.2e}')
lines.append(f'largest |difference| over 9 points and 2 block sizes: {worst:.2e}')
print('\n'.join(lines)); open('../outputs/s18_census_rotation_vs_abel.txt','w').write('\n'.join(lines)+'\n')

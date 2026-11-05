# SCRIPT: MATTER-DISK-S11-V2  is the disk exit the quarter-turn of the author's offset?
# WHY THIS CHECK PROVES WHAT IT CLAIMS
# The Offset Belongs to the Boundary gives the endpoint offset of a gapped chain in closed form,
# 2 artanh(v/sqrt(E_min E_max)). Continued to the opened SSH chain it predicts a complex level offset
# whose imaginary part is Im tau_inf = 2 arctan(u/sqrt(E(0)E(pi))). Then <K> = 1 + u^2/(E(0)E(pi))
# = sec^2(Im tau_inf/2) exactly, so <K> = 2 is the same statement as Im tau_inf = pi/2: a quarter turn.
# If the census rotation (max over block levels of |Im Log((1-nu)/nu)|/pi) is this offset, then the gap
# between measured rotation and 2 arctan(u/sqrt(E0 Epi))/pi must shrink as the block grows.
# KILL (written before the run): at u = 0.3, 0.5, 0.7 and v at 60%, 80%, 95% of the way to the exit,
# the gap at block 160 exceeds the gap at block 20 by more than 1e-9, or exceeds 2e-3 at block 160.
# (v2: non-increase is judged within an absolute slack of 1e-9, so roundoff on a noise-floor gap
# cannot flip PASS/FAIL; strict decrease is not required.)
# OPPOSITE: the same comparison against the plain Hermitian-form guess 2 arctan(u/E(pi))/pi must NOT pass.
import numpy as np
src=open('nhssh_lib_and_s03a_occupations.py').read().split('w=1.0')[0]; ns={}; exec(src,ns)
w=1.0
def rot(v,u,Lc,N=4000,d=1e-9):
    nu=np.linalg.eigvals(ns['corr'](v,w,u,N,Lc)); nu=nu[(abs(nu)>d)&(abs(1-nu)>d)]
    return np.max(np.abs(np.log((1-nu)/nu).imag))/np.pi
def vexit(u): # E(0)E(pi)=u^2 with E0^2=(v+w)^2-u^2, Epi^2=(w-v)^2-u^2, v<w-u
    from scipy.optimize import brentq
    return brentq(lambda v: np.sqrt(((v+w)**2-u**2)*((w-v)**2-u**2))-u**2, 0.0, w-u-1e-12)
ok=True; okopp=True
for u in [0.3,0.5,0.7]:
    ve=vexit(u)
    for f in [0.6,0.8,0.95]:
        v=f*ve; E0=np.sqrt((v+w)**2-u**2); Ep=np.sqrt((w-v)**2-u**2)
        pred=2*np.arctan(u/np.sqrt(E0*Ep))/np.pi; opp=2*np.arctan(u/Ep)/np.pi
        gaps=[]
        for Lc in [20,40,80,160]:
            gaps.append(rot(v,u,Lc)-pred)
        g=np.abs(gaps); good=(g[-1]<=g[0]+1e-9) and g[-1]<2e-3; ok&=good
        okopp&= not (abs(gaps[-1]+pred-opp)<2e-3)
        print(f'u={u} v={v:.4f} pred={pred:.5f} opposite={opp:.5f} gaps by block 20,40,80,160: '+' '.join(f'{x:+.2e}' for x in gaps)+('  PASS' if good else '  FAIL'))
print('VERDICT:','census rotation converges to the offset quarter-turn form' if ok else 'KILLED at the stated bar')
print('OPPOSITE (Hermitian-form guess must fail):','fails as required' if okopp else 'ALSO PASSES - test does not discriminate')

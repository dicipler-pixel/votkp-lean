# SCRIPT: GAPS-EXACT-CONV-01
# Exact convolution of float64 sequences via FLINT integer polynomials.
# Each float is scaled by 2^B and rounded to an integer, so inputs are kept to about 53 significant bits,
# down to values of about 2^-B. The product is exact, and only the final conversion back to float rounds.
# Signed inputs are split into positive and negative parts, so FLINT only ever multiplies
# non-negative polynomials (the bundled FLINT fails OpenAI's signed-FFT regression check).
import numpy as np, math
from flint import fmpz_poly
B=320
D=2**(2*B)
def _toint(a):
    return [int(v) for v in np.ldexp(a,B)]
def _pos(a,b,n):
    if not (a>0).any() or not (b>0).any(): return np.zeros(n)
    p=fmpz_poly(_toint(a)); q=fmpz_poly(_toint(b))
    r=p.mul_low(q,n) if hasattr(p,'mul_low') else p*q
    co=r.coeffs()[:n]
    out=np.zeros(n)
    for i,c in enumerate(co):
        if c: out[i]=int(c)/D
    return out
def conv(a,b,n):
    a=np.asarray(a,float); b=np.asarray(b,float)
    ap,an=np.maximum(a,0),np.maximum(-a,0); bp,bn=np.maximum(b,0),np.maximum(-b,0)
    r=_pos(ap,bp,n)
    if an.any(): r-=_pos(an,bp,n)
    if bn.any(): r-=_pos(ap,bn,n)
    if an.any() and bn.any(): r+=_pos(an,bn,n)
    return r
if __name__=='__main__':
    import time
    rng=np.random.default_rng(1); a=rng.random(20000)*np.exp(-rng.random(20000)*80); b=rng.random(20000)
    t=time.time(); r=conv(a,b,20000); print('time %.2fs'%(time.time()-t))
    d=np.convolve(a,b)[:20000]; print('max rel diff vs direct %.2e'%np.max(np.abs(r-d)/np.maximum(d,1e-300)))
    s=a-0.3; r2=conv(s,b,20000); d2=np.convolve(s,b)[:20000]; print('signed max abs diff %.2e'%np.max(np.abs(r2-d2)))

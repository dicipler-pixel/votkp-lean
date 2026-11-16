# SCRIPT: W15-STRETCH (watcher) independent check of L2 claim: on an arm-arm link the geodesic a->b meets face a first then face b (0<s1<s2<d) and the in-cell stretch s2-s1 exceeds delta=arccosh g (g>1) by at least 0.1284 on the grid z=1.5..13 step 0.25.
import numpy as np
eta = np.diag([1.,-1,-1,-1]); mk = lambda p,q: p@eta@q
def pt(r,u): return np.array([np.cosh(r), np.sinh(r)*u[0], np.sinh(r)*u[1], np.sinh(r)*u[2]])
O = np.array([1.,0,0,0]); zs = np.arange(1.5, 13.01, 0.25); worst = 9; viol = 0; n = 0; mn_stretch = 9
for za in zs:
  for zb in zs:
    ra, rb = np.log(za), np.log(zb); pa, pb = pt(ra,[1,0,0]), pt(rb,[0,1,0]); d = np.arccosh(mk(pa,pb))
    tv = (pb - np.cosh(d)*pa)/np.sinh(d)           # unit tangent at pa toward pb
    pp = lambda s: np.cosh(s)*pa + np.sinh(s)*tv
    fa = lambda s: np.arccosh(max(1,mk(pp(s),O))) - np.arccosh(max(1,mk(pp(s),pa)))   # >0 when nearer ... crossing of equal distance to O and to pa
    fb = lambda s: np.arccosh(max(1,mk(pp(s),O))) - np.arccosh(max(1,mk(pp(s),pb)))
    def root(f):
        lo, hi = 0.0, d
        if f(lo)*f(hi) > 0: return None
        for _ in range(100):
            m = (lo+hi)/2
            if f(lo)*f(m) <= 0: hi = m
            else: lo = m
        return (lo+hi)/2
    s1, s2 = root(fa), root(fb); n += 1
    if s1 is None or s2 is None or not (0 < s1 < s2 < d): viol += 1; continue
    g = np.sinh(ra/2)*np.sinh(rb/2)
    mn_stretch = min(mn_stretch, s2-s1)
    if g > 1: worst = min(worst, (s2-s1) - np.arccosh(g))
print('pairs %d, ordering violations %d, shortest in-cell stretch %.4f, smallest (stretch - delta) over g>1: %.4f' % (n, viol, mn_stretch, worst))
# spot: z=7,9
za,zb=7,9; ra,rb=np.log(za),np.log(zb); pa,pb=pt(ra,[1,0,0]),pt(rb,[0,1,0]); d=np.arccosh(mk(pa,pb)); print('z=7,9 d=%.4f' % d)

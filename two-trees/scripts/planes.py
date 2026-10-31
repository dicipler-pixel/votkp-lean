# SCRIPT: LN7_PLANE_GAPS
# Checks the geometric inputs of the nested half-space proof at z = 7, exactly where possible.
# Normals (scaled by sqrt 7): N_u = (3, 4 e_u), <N,N> = 9 - 16 = -7, signature (+,-,-,-).
# H_u = { p : <p, N_u> <= 0 } = { x_u / t >= 3/4 = tanh(l/2) }.
import numpy as np, mpmath as mp
from fractions import Fraction as F
mp.mp.dps = 40
eta = np.diag([1,-1,-1,-1])
def ip(a,b): return int(np.array(a).dot(eta).dot(np.array(b)))
E = {'i':(1,1),'-i':(1,-1),'j':(2,1),'-j':(2,-1),'k':(3,1),'-k':(3,-1)}
def N(u):
    a,s = E[u]; v=[3,0,0,0]; v[a]=4*s; return v
def Q(u):
    a,s = E[u]; M=np.diag([7,7,7,7]); M[0,0]=25; M[a,a]=25; M[0,a]=M[a,0]=24*s; return M
inv={'i':'-i','-i':'i','j':'-j','-j':'j','k':'-k','-k':'k'}
print('<N_u,N_u> =', ip(N('i'),N('i')))
for u in E:
    assert ip(N(u),N(u)) == -7
    # Q_u N_{-u} = -7 N_u : B_u carries the plane of H_{-u} onto the plane of H_u, flipping the side
    assert list(Q(u).dot(N(inv[u]))) == [-7*c for c in N(u)]
    for w in E:
        g = F(abs(ip(N(inv[u]),N(w))),7)   # cosh of the distance between plane(-u) and plane(w)
        if w == inv[u]: continue
        assert g == (F(25,7) if w == u else F(9,7)), (u,w,g)
print('Q_u N_{-u} = -7 N_u for all u: True')
print('cosh d(plane(-u), plane(u)) = 25/7 = cosh l ; cosh d(plane(-u), plane(w perp)) = 9/7 = cosh delta')
# sinh d(point, plane) = |<p, N>| / sqrt7 for unit-time point p
O = [1,0,0,0]; BO = [F(25,7),F(24,7),0,0]
print('sinh d(O, plane i)     =', mp.nstr(abs(ip(O,N('i')))/mp.sqrt(7),15), ' sinh(l/2) =', mp.nstr(mp.sinh(mp.log(7)/2),15))
v = 3*25-4*24
print('sinh d(B_iO, plane i)  =', mp.nstr(abs(mp.mpf(v)/7)/mp.sqrt(7),15))
# independent numerical check of the plane-plane distance formula by direct minimisation
def pt(r, th, ph):  # point of H^3 with rapidity r in direction (th, ph)
    d = np.array([np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph), np.cos(th)])
    return np.concatenate([[np.cosh(r)], np.sinh(r)*d])
import itertools
from scipy.optimize import minimize
def on_plane(u, a, b):
    # parametrise plane x_u = (3/4) t by two coordinates in the plane's own hyperboloid: p = cosh-type param
    # plane is a copy of H^2: use orthonormal frame n0 = foot point, e1, e2
    ax,s = E[u]
    foot = np.zeros(4); foot[0]=4/np.sqrt(7); foot[ax]=s*3/np.sqrt(7)   # <foot,foot>=1, <foot,N>=0
    others=[k for k in (1,2,3) if k!=ax]
    e1=np.zeros(4); e1[others[0]]=1; e2=np.zeros(4); e2[others[1]]=1
    r=np.hypot(a,b); 
    if r==0: return foot
    return np.cosh(r)*foot + np.sinh(r)*(a*e1+b*e2)/r
def dist(p,q): return float(np.arccosh(max(1.0, p.dot(eta).dot(q))))
f=lambda z: dist(on_plane('-i',z[0],z[1]), on_plane('j',z[2],z[3]))
best=min((minimize(f, x0, method='Nelder-Mead', options={'xatol':1e-12,'fatol':1e-14,'maxiter':20000}) for x0 in np.random.default_rng(1).normal(size=(20,4))), key=lambda r:r.fun)
print('numerical min distance plane(-i) to plane(j) =', best.fun, '  delta =', float(mp.acosh(mp.mpf(9)/7)))

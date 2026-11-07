# SCRIPT: DRAWING-POLY-01
# Step 1: the knot potential read straight off the DRAWING (Cho-Kim-Kim, arXiv 1301.6219, Sec. 2).
# One variable z_k per side of the diagram. Each crossing with sides (a,b,c,d) adds
#   P = Li2(z_b/z_a) - Li2(z_b/z_c) + Li2(z_d/z_c) - Li2(z_d/z_a).
# Hyperbolicity equations exp(z_k dV/dz_k) = 1 are branch-free products of (1 - ratio)^(+-1).
# Modified potential V0 = V - sum_k (z_k dV/dz_k) log z_k ; at the geometric solution V0 = i(vol + i cs) mod pi^2.
# Check 1 (this script): the paper's own figure-eight potential (8 sides, 4 crossings) must give vol(4_1) = 2.02988.
import numpy as np
from mpmath import polylog, mpc
from scipy.optimize import least_squares
def build(crossings):                  # crossings: list of (a,b,c,d) side indices -> list of (eps, p, q) for eps*Li2(z_p/z_q)
    T=[]
    for a,b,c,dd in crossings: T+= [(+1,b,a),(-1,b,c),(+1,dd,c),(-1,dd,a)]
    return T
def zdV(T,z,n):                        # z_k dV/dz_k with principal logs
    g=np.zeros(n,complex)
    for e,p,q in T:
        L=np.log(1-z[p]/z[q]); g[p]+=-e*L; g[q]+=e*L
    return g
def V0(T,z,n):
    V=sum(e*complex(polylog(2,mpc(z[p]/z[q]))) for e,p,q in T)
    return V-np.sum(zdV(T,z,n)*np.log(z))
def H(T,z,n):                          # exp(z_k dV/dz_k) - 1, branch-free
    return np.exp(zdV(T,z,n))-1
def solve(T,n,starts=300,seed=1):
    rng=np.random.default_rng(seed); sols=[]
    def f(x):
        z=np.concatenate([[1.0+0j],x[:n-1]+1j*x[n-1:]]); h=H(T,z,n); return np.concatenate([h.real,h.imag])
    for _ in range(starts):
        x0=rng.normal(0,2,2*(n-1))
        try: r=least_squares(f,x0,xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=4000)
        except Exception: continue
        if r.cost<1e-20:
            z=np.concatenate([[1.0+0j],r.x[:n-1]+1j*r.x[n-1:]])
            ratios=[z[p]/z[q] for e,p,q in T]
            if min(min(abs(u),abs(1-u)) for u in ratios)>1e-6: sols.append(z)
    return sols
if __name__=='__main__':
    fig8=[(0,5,1,6),(5,2,4,1),(7,3,6,4),(2,0,3,7)]   # from the paper's V, 0-based: [z6/z1, z6/z2, z7/z2, z7/z1] -> (a,b,c,d)=(1,6,2,7) etc.
    T=build(fig8); sols=solve(T,8)
    vals=sorted({(round(V0(T,z,8).imag,6),round(((-V0(T,z,8).real+np.pi**2/2)%np.pi**2)-np.pi**2/2,5)) for z in sols})
    print('figure-eight from the drawing: solutions found %d ; distinct (Im V0 = vol, cs mod pi^2):'%len(sols),vals)
    print('expected vol(4_1) = 2.029883, cs = 0')

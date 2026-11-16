# SCRIPT: SMALL-FIELD-GAP-03
# Weak-coupling (small-field, phase-basis) limit of H = sum_e C2(e) + lam sum_p (3 - Re tr U_p), alpha = 1.
# Near U = 1 each colour a decouples: H_a = sum_e -d^2/da_e^2 + (lam/4) sum_p (B a)_p^2, B = plaquette-edge curl.
# Normal modes omega = sqrt(lam*mu), mu a nonzero eigenvalue of B^T B (zero modes are gauge directions).
# Colour-singlet (gauge-invariant) lowest excitation needs two quanta: small-field gap = 2 sqrt(lam*mu_min).
# Normalisation check (kill if it fails): one plaquette gives mu = 4, gap 4 sqrt(lam), which is the repo's
# one-plaquette operator 4*C2(U) + lam(3 - Re chi) at weak coupling (2 sqrt(4 lam)).
import sys, numpy as np
sys.path[:0]=[p for p in sys.argv[1:]]
import spatial_gauge as sg
def curl(edges,faces):
    ix={tuple(e):i for i,e in enumerate(edges)}
    B=np.zeros((len(faces),len(edges)))
    for f,cyc in enumerate(faces):
        for k in range(len(cyc)):
            a,b=cyc[k],cyc[(k+1)%len(cyc)]
            if (a,b) in ix: B[f,ix[(a,b)]]+=1
            elif (b,a) in ix: B[f,ix[(b,a)]]-=1
            else: raise ValueError('face edge missing')
    return B
def mu_min(B):
    w=np.linalg.eigvalsh(B@B.T); w=w[w>1e-9]; return w.min(), len(w)
print("graph          links faces  rank  mu_min    small-field gap / sqrt(lam)")
B1=np.array([[1.,1.,1.,1.]]); m,_=mu_min(B1); print(f"{'one plaquette':14s} {4:5d} {1:5d} {1:5d} {m:8.5f}   {2*np.sqrt(m):.5f}")
for n in ('two','strip','corner','cube','double_cube'):
    md=sg.model(n); B=curl(md['edges'],md['faces']); m,r=mu_min(B)
    print(f"{n:14s} {len(md['edges']):5d} {len(md['faces']):5d} {r:5d} {m:8.5f}   {2*np.sqrt(m):.5f}")
# size dependence: 2D periodic L x L torus (all plaquettes), and open 1 x n strips
def torus(L):
    E={};edges=[];faces=[]
    v=lambda x,y:(x%L)*L+(y%L)
    for x in range(L):
        for y in range(L):
            for d in ((1,0),(0,1)):
                e=(v(x,y),v(x+d[0],y+d[1])); E[e]=len(edges); edges.append(e)
    for x in range(L):
        for y in range(L):
            faces.append((v(x,y),v(x+1,y),v(x+1,y+1),v(x,y+1)))
    return edges,faces
def strip(n):
    v=lambda x,y:x*2+y
    edges=[(v(x,0),v(x,1)) for x in range(n+1)]+[(v(x,y),v(x+1,y)) for x in range(n) for y in (0,1)]
    faces=[(v(x,0),v(x+1,0),v(x+1,1),v(x,1)) for x in range(n)]
    return edges,faces
print("\nopen 1 x n strips:  n  mu_min   2sqrt(mu_min)")
for n in (1,2,3,5,8,13,21,34):
    m,_=mu_min(curl(*strip(n))); print(f"{n:22d} {m:8.5f} {2*np.sqrt(m):.5f}")
print("\nperiodic L x L tori: L  mu_min   2sqrt(mu_min)   predicted 4 sin^2(pi/L)")
for L in (3,4,6,8,12,16):
    m,_=mu_min(curl(*torus(L))); print(f"{L:22d} {m:8.5f} {2*np.sqrt(m):.5f}   {4*np.sin(np.pi/L)**2:.5f}")

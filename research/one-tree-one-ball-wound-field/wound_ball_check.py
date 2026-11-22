# SCRIPT: WOUND-BALL-01  checks behind the One Tree, One Ball wound-field page (Jeromie Beasley, 22 Nov 2026, AI-assisted)
# Model (Ink's): screened Laplacian on the cell graph, (delta^T G delta + g_m) V = s, field held at the wound edges.
# Each check says what would make it fail.
import numpy as np
from scipy.special import i0
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
print("== 1. a chain of cells is a ladder of equal peel steps ==")
# Discrete: G(2V_n - V_{n-1} - V_{n+1}) + g_m V_n = 0  =>  V_n = cosh(n th) with 2 cosh th = 2 + g_m/G.
# Fails if the direct linear solve with V = 1 at both edges differs from cosh(n th)/cosh(N th).
for G,gm,N in [(1.0,0.01,40),(2.5,0.3,12),(1.0,1e-4,300)]:
    th=np.arccosh(1+gm/(2*G)); n=np.arange(-N,N+1); M=2*N+1
    A=diags([-G*np.ones(M-1),(2*G+gm)*np.ones(M),-G*np.ones(M-1)],[-1,0,1]).tolil()
    b=np.zeros(M); A[0,:]=0;A[0,0]=1;b[0]=1; A[M-1,:]=0;A[M-1,M-1]=1;b[M-1]=1
    V=spsolve(A.tocsr(),b); C=np.cosh(n*th)/np.cosh(N*th)
    print(f" G={G} g_m={gm} N={N}: theta={th:.6f} (continuum a/lambda={np.sqrt(gm/G):.6f})  max|solve-closed|={np.max(abs(V-C)):.1e}  centre={V[N]:.6e}")
print("\n== 2. the centre field is the ball radius of the edge ==")
# Edge at rapidity rho = L/(2 lambda). Ball radius Gamma = tanh(rho/2) = (z-1)/(z+1), z = e^rho.  Claim: 1/cosh(rho) = (1-Gamma^2)/(1+Gamma^2).
for rho in [0.5,1,2,10,50]:
    g=np.tanh(rho/2); print(f" rho={rho}: 1/cosh={1/np.cosh(rho):.6e}  (1-G^2)/(1+G^2)={(1-g*g)/(1+g*g):.6e}")
print(" Ink's numbers, lambda = 1 mm: L=4 ->",f"{1/np.cosh(2):.4f}"," L=20 ->",f"{1/np.cosh(10):.2e}"," L=100 ->",f"{1/np.cosh(50):.2e}")
print("\n== 3. the wall is the one-third shell ==")
w=np.log(3+2*np.sqrt(2)); g=np.tanh(w/2)
print(f" wall rapidity ln(3+2 sqrt2) = {w:.10f}, arccosh(3) = {np.arccosh(3):.10f}, Gamma^2 = {g*g:.10f}, centre field = {1/np.cosh(w):.10f}")
print(f" so a wound of width L = 2 ln(3+2 sqrt2) lambda = {2*w:.6f} lambda keeps exactly 1/3 of the edge field at its centre")
print("\n== 4. shape of the wound: slab, round (disc), ball ==")
# slab: 1/cosh(R/l); disc (2D sheet, radial): 1/I0(R/l); ball (3D): (R/l)/sinh(R/l).
# Check the disc and ball by solving the radial ODE numerically.  Fails if the solve differs from the closed form.
from scipy.integrate import solve_bvp
for R in [1.0,2.0,3.0]:
    out=[]
    for dim in [1,2,3]:
        f=lambda r,y: np.vstack([y[1], y[0]-(dim-1)/r*y[1]])
        r=np.linspace(1e-6,R,400); y=np.vstack([np.ones_like(r),np.zeros_like(r)])
        sol=solve_bvp(f,lambda ya,yb: np.array([ya[1],yb[0]-1]),r,y,tol=1e-9,max_nodes=100000)
        out.append(sol.sol(1e-6)[0])
    cf=[1/np.cosh(R),1/i0(R),R/np.sinh(R)]
    print(f" R/lambda={R}: slab {out[0]:.6f} ({cf[0]:.6f})  disc {out[1]:.6f} ({cf[1]:.6f})  ball {out[2]:.6f} ({cf[2]:.6f})")
print("\n== 5. critical width under drugs ==")
# centre < threshold c  when  L > L* = 2 lambda arccosh(1/c), lambda = lambda0 sqrt(fG/fm).
for c in [0.5,1/3,0.1,0.01]: print(f" threshold {c:.4f}: L*/lambda = {2*np.arccosh(1/c):.4f}")
for fG,fm in [(1,1),(4,1),(1,4),(0.25,1)]: print(f" gap x{fG}, leak x{fm}: lambda factor {np.sqrt(fG/fm):.3f}")

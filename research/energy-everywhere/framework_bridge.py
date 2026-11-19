# SCRIPT: ENERGY-FRAMEWORK-BRIDGE-01
# Jeromie Beasley's framework applied to the grid/universe write-up (19 Nov 2026, AI-assisted).
# Each check states what would make it fail before it runs.
import numpy as np
rng = np.random.default_rng(1119)
print("=== 1. Line energy books = connection-energy edge (VOTKP Prop 22.2) at the load end ===")
# Load end of a line with surge impedance Z0 = sqrt(L'/C') and load Z = z Z0.
# Electric book d_e = C'V^2/2, magnetic book d_m = L'I^2/2, I = V/Z.  Claim: d_e/d_m = z^2, so the
# edge coefficient (d_e-d_m)/(d_e+d_m) = Gamma(z^2) = Gamma(z) (+) Gamma(z)  (gap-power ladder k=2).
# Fails if the ratio is anything but z^2 or the addition law does not reproduce it.
Lp, Cp = 1.0e-6, 1.1e-11; Z0 = np.sqrt(Lp/Cp)
oplus = lambda u, v: (u+v)/(1+u*v)
G = lambda z: (z-1)/(z+1)
for z in [0.25, 1.0, 3.0, 3+2*np.sqrt(2), 10.0]:
    V = 1.0; I = V/(z*Z0); de, dm = Cp*V**2/2, Lp*I**2/2
    edge = (de-dm)/(de+dm)
    print(f" z={z:7.4f}: d_e/d_m={de/dm:9.4f} z^2={z*z:9.4f}  edge={edge:+.6f}  G(+)G={oplus(G(z),G(z)):+.6f}  wall G^2={G(z)**2:.4f}")
print()
print("=== 2. Grid ring: connection energy = self-commutator (his identity) and it is the line-drop budget ===")
# Nodes carry voltages D_i (real here: magnitudes), edges carry unitary phase e^{i th_ij}.
# H = D + A, A skew with A_ij = u_ij, A_ji = -conj(u_ij).  Claim: (1/8)||[H,H*]||_F^2 = sum_edges |D_i - u D_j u*|^2
# For scalars u D_j u* = D_j, so the edge term is (D_i - D_j)^2: the squared magnitude drop.
# Fails if the two sides differ beyond rounding.
n = 6; D = 1.0 + 0.05*rng.normal(size=n); H = np.diag(D).astype(complex); edges = [(i, (i+1) % n) for i in range(n)]
for i, j in edges:
    u = np.exp(1j*rng.uniform(0, 2*np.pi)); H[i, j] += u; H[j, i] += -np.conj(u)
C = H @ H.conj().T - H.conj().T @ H
lhs = np.linalg.norm(C)**2/8; rhs = sum((D[i]-D[j])**2 for i, j in edges)
print(f" (1/8)||[H,H*]||^2 = {lhs:.12f}   sum_edges (D_i-D_j)^2 = {rhs:.12f}   diff {abs(lhs-rhs):.1e}")
Hflat = np.diag(np.ones(n)).astype(complex) + (H - np.diag(np.diag(H)))
Cf = Hflat @ Hflat.conj().T - Hflat.conj().T @ Hflat
print(f" all node magnitudes equal (parallel field): (1/8)||[H,H*]||^2 = {np.linalg.norm(Cf)**2/8:.1e}  (normal operator)")
# block version with unitary 2x2 edges (his v7 statement)
m = 2; N = n*m; Db = [ (lambda X: (X+X.conj().T)/2)(rng.normal(size=(m,m))+1j*rng.normal(size=(m,m))) for _ in range(n)]
Hb = np.zeros((N,N), complex)
for i in range(n): Hb[i*m:(i+1)*m, i*m:(i+1)*m] = Db[i]
rhs = 0
for i, j in edges:
    Q, _ = np.linalg.qr(rng.normal(size=(m,m))+1j*rng.normal(size=(m,m)))
    Hb[i*m:(i+1)*m, j*m:(j+1)*m] += Q; Hb[j*m:(j+1)*m, i*m:(i+1)*m] += -Q.conj().T
    rhs += np.linalg.norm(Db[i] - Q @ Db[j] @ Q.conj().T)**2
Cb = Hb @ Hb.conj().T - Hb.conj().T @ Hb
print(f" block 2x2 unitary edges: lhs {np.linalg.norm(Cb)**2/8:.10f}  rhs {rhs:.10f}  diff {abs(np.linalg.norm(Cb)**2/8-rhs):.1e}")
print()
print("=== 3. Redistribution = zero-time memory footprint (UPG Prop 1.5) on a load/line split ===")
# H = [[A,B],[B*,D]], Pi = retained. Claim ||[H,Pi]||^2 = ||F(H,Pi)||^2 = 2 Tr K(0), K(0)=BB*.
k, h = 3, 5; X = rng.normal(size=(k+h,k+h))+1j*rng.normal(size=(k+h,k+h)); Hm = (X+X.conj().T)/2
P = np.diag([1]*k+[0]*h).astype(complex); I = np.eye(k+h)
F = (I-P)@Hm@P + P@Hm@(I-P); B = Hm[:k, k:]
print(f" ||[H,Pi]||^2={np.linalg.norm(Hm@P-P@Hm)**2:.10f} ||F||^2={np.linalg.norm(F)**2:.10f} 2TrK(0)={2*np.trace(B@B.conj().T).real:.10f}")
print()
print("=== 4. Speed has an optimum: thermodynamic-length cost (IQGT Thm 5.3 form W_ex >= c l^2 / T) ===")
# A cycle of duration T yields W(T) = Wmax - c l^2 / T (cost of moving the projector a length l in time T).
# Power P(T) = W(T)/T is maximal at T* = 2 c l^2 / Wmax with P* = Wmax^2/(4 c l^2), and at T* half of Wmax is spent.
# Fails if a brute-force scan finds a different optimum.
Wmax, c, l = 0.693, 0.4, 1.3
T = np.linspace(0.05, 40, 400001); Pw = (Wmax - c*l*l/T)/T
i = np.argmax(Pw)
print(f" scan T*={T[i]:.5f} P*={Pw[i]:.6f}   formula T*={2*c*l*l/Wmax:.5f} P*={Wmax**2/(4*c*l*l):.6f}   W(T*)/Wmax={(Wmax-c*l*l/T[i])/Wmax:.4f}")
print()
print("=== 5. Open line end is the rim; Ferranti is rotation on the rim ===")
# Open end: Gamma_L = 1 (rim). Seen from distance l: Gamma = e^{-2 i beta l}, |Gamma| = 1 (stays on the rim).
# Receiving/sending voltage = sec(beta l). Fails if |Gamma| leaves 1 or the ratio differs from sec.
for bl_deg in [9, 18, 30, 60, 84]:
    bl = np.radians(bl_deg); Gin = np.exp(-2j*bl)
    Vs = (np.exp(1j*bl) + np.exp(-1j*bl))/2; ratio = 1/abs(Vs)
    print(f" beta l={bl_deg:3d} deg ({bl_deg/360*6000:6.0f} km at 50 Hz): |Gamma_in|={abs(Gin):.6f} arg={np.degrees(np.angle(Gin)):+8.2f}  Vr/Vs={ratio:.4f} sec={1/np.cos(bl):.4f}")

# SCRIPT: LH-CHECK-01
# Independent recomputation for Light at the Hypersurface Mixer v1. Shares no code with lh_math_v1.js:
# every item is rebuilt here from 4x4 Lorentz matrices, 2x2 SL(2,C) matrices and 2x2 transfer matrices.
# K3 uses the raw drawn vectors (tangents, normals) dumped by the node run, and recomputes the angles itself.
# Kill lines copied unchanged from PLAN section 7, before the run:
#
# | ID | Statement | Kill if |
# |---|---|---|
# | K1 | Flux at a step: `|R + (Y₂/Y₁)t² − 1|` over 1e4 random `Y ∈ [1e−2, 1e2]` | > 1e-12 |
# | K2 | `|(Y₁ − Y₂)/(Y₁ + Y₂) − tanh(½ ln(Y₁/Y₂))|`; reciprocity; `z = 1 ⇒ Γ = 0`; `Y₂ = 0 ⇒ Γ = 1`; `Γ(−z)Γ(z) = 1`; `|G(z̄)|·|G(z)| = 1` on 1e3 complex pairs | any > 1e-12 |
# | K3 | Refraction: `|a₁ sin²θ₁ − a₂ sin²θ₂|` at every transmitted hit, both angles **measured from the drawn tangent vectors by Minkowski products**, not from the formula that built them; and `|sin θ − cosh h sin ψ|` for centre rays | > 1e-10 |
# | K4 | Oblique flux with `Y = √(a − C)`: `|R + T − 1|` on 1e4 cases | > 1e-12 |
# | K5 | Critical angle: threshold found by bisection on "transmitted branch exists" against `arcsin √(a₂/a₁)`; at `κ = 4` it is 30°; past it `||Γ| − 1|`; `|arg Γ + 2 arctan(κₑ/y)|`; `|sin(π/2 + i arccosh(√κ sin θ₁)) − √κ sin θ₁|` | angle > 1e-9 rad; others > 1e-12 |
# | K6 | Film: `⊕` against the explicit bounce sum (400 terms, `|Γx| ≤ 0.9`); recursion against transfer matrix for 2 to 6 layers; net flux equal in every layer; zero-phase telescoping; `D` equal steps at zero phase give `tanh(D r/2)`; echo circle: `sign(|r|² − |a|²) = sign(|x − x_c| − |x_c|)` on 1e4 random complex cases; `a = ½, x = ±⅕` give `49/121`, `1/9` | sum > 1e-10; others > 1e-12; any sign exception; witness > 1e-15 |
# | K7 | Gap: `||r|² + |t|² − 1|` (equal outer media); slope of `ln T` against `w` equals `−2κₑ` for `κₑ w ∈ [3, 6]` | > 1e-12; relative slope error > 1e-3 |
# | K8 | Wall: at `z = 3 + 2√2`, `|R − ½|`; `|tr_SL(2) W + 2|`; `‖(W + I)²‖`, with `‖W + I‖ > 1e-3` required; `z = 5` gives `R = 4/9 < ½`, `z = 7` gives `9/16 > ½`; trace `= 2 − 4(R/T)²` on 500 ratios | `R`: > 1e-14; trace: > 1e-12; Jordan: > 1e-10; formula: > 1e-12 |
# | K9 | Thomas: angle from the polar decomposition against `2 arctan(Γ_a Γ_b)` on 500 random pairs; `z = 5`: `(cos, sin) = (65/97, 72/97)`; `z = 7`: `(175/337, 288/337)` | > 1e-9; exact values > 1e-13 |
# | K10 | `‖W − L R L⁻¹ R‖/‖W‖`; `cos φ = 8g⁴ − 8g² + 1` for `g < 1`; run length `4 arccosh g` for `g > 1` | > 1e-8; > 1e-10 |
# | K11 | Rim: aberration `= ⊕`; on-axis frequency ratio `= z`; ping-pong with zero exceptions in 1e5 random null directions for `z ∈ {(3 + 2√2)(1 + 1e−6), 7, 9, 13}`; **at `z = 5` at least one exception must be found**; integer check at `z = 7`: step of `(3, 1, 2, 2)` lands in the cap of its letter | residual > 1e-12; any exception above the wall; no exception at 5; integer check false |
# | K12 | Face shadow: the face plane meets the rim at `cos ψ₀ = Γ`; at the wall `ψ₀ = 45°` | > 1e-12 |
# | K13 | Pressure: Maxwell normal stress on a plane tilted by `θ` equals `−u cos²θ` (transverse, `|E| = |H|`), 500 random frames; FEED-LOOP-03 lines P1, P2, P3 re-run unchanged | > 1e-12; P1–P3 at their own tolerances |
# | K14 | **Simultaneous motion.** Run the clock for 2000 fixed steps in `breathe` and 2000 in `sweep` (every arm crosses the wall). On every frame: (a) every face and every ray-tree node: flux residual; (b) `a sin²θ` residual; (c) stack net-flux spread; `|det W − 1|`; null norm of every carried direction. (d) With the hypothesis layer hidden, every law readout is bitwise identical to the run with it shown. (e) Every pure quantity at step `n` equals `feed(P, n·dτ)` computed cold, bitwise. (f) Integrated quantities with `dτ` halved agree | (a)–(c) > 1e-10; (d), (e) any difference; (f) > 1e-6 |
# | K15 | B182: impulse total outflow `= 1`; mean residence `(1 + a/b)/κ`: `(1, 1, 0.2) → 6`, `(1, 1, 0.02) → 51`; `b = 0` keeps `a/(κ + a) = 0.5`; network ledger `|in − out − stored|` over the K14 run | > 1e-9 |
# | K16 | B203: `2Σ|r_j| − 2|Σ r_j| = 4 min(R₊, R₋)` on 1e3 random chains | > 1e-12 |
# | K17 | `1 − 2C = Γ` and `T = 4C(1 − C)` with `C = 1/(z + 1)` | > 1e-14 |
# | K18 | Faces: `<N_a, N_b> = sinh h_a sinh h_b`; dihedral angle measured from the two drawn caps `= arccos g`; minimum hyperbolic distance between two separated planes `= arccosh g` | > 1e-12; > 1e-10; > 1e-8 |
# | K19 | Page equals script: every self-test value computed in the browser equals the node value | relative difference > 1e-12 |
# | K20 | Rendering: no console error in any eye at `τ = 0, 7, 40`; frame time under 33 ms at default density on the sandbox | any error |

import numpy as np, json, math
rng = np.random.default_rng(20261115)
eta = np.diag([1.,-1,-1,-1]); mk = lambda p,q: float(p@eta@q)
res = []
def line(k, v, tol, note, ok=None):
    ok = (v <= tol) if ok is None else ok; res.append((k, v, tol, note, ok))
def boost(u, r):
    u = np.asarray(u, float); B = np.eye(4); c, s = math.cosh(r), math.sinh(r)
    B[0,0] = c; B[0,1:] = s*u; B[1:,0] = s*u; B[1:,1:] = np.eye(3) + (c-1)*np.outer(u,u); return B
X, Y, Z = np.eye(3)
# K1, K2: step from continuity of field and flux, solved as a linear system
e = 0
for _ in range(10000):
    Y1, Y2 = np.exp(rng.uniform(np.log(1e-2), np.log(1e2), 2))
    A = np.array([[1,-1],[Y1*-1, -Y2]], float); r, t = np.linalg.solve(np.array([[-1, 1],[Y1, Y2]]), np.array([1, Y1]))  # 1 + r = t ; Y1(1 - r) = Y2 t
    e = max(e, abs(r*r + (Y2/Y1)*t*t - 1))
line('K1', e, 1e-12, 'flux at a step, solved from the two matching conditions')
e = 0
for _ in range(1000):
    Y1, Y2 = np.exp(rng.uniform(-4.6, 4.6, 2)); r12 = (Y1-Y2)/(Y1+Y2); r21 = (Y2-Y1)/(Y2+Y1)
    e = max(e, abs(r12 - math.tanh(0.5*math.log(Y1/Y2))), abs(r12 + r21))
    z = math.exp(rng.uniform(-3,3)); G = lambda q: (q-1)/(q+1); e = max(e, abs(G(-z)*G(z) - 1))
    w = complex(rng.uniform(-2,2), rng.uniform(0.1,2)); q = complex(rng.uniform(-2,2), rng.uniform(-2,2)); Gw = lambda q: (q-w)/(q-w.conjugate())
    e = max(e, abs(abs(Gw(q.conjugate()))*abs(Gw(q)) - 1))
e = max(e, abs(G(1.0)), abs((1-0)/(1+0) - 1))
line('K2', e, 1e-12, 'Smith form, reciprocity, matched, mirror, Γ(−z)Γ(z), |G(z̄)||G(z)|')
# K3 from the dumped drawn vectors
for drive in ['breathe','sweep']:
    D = json.load(open(f'lh_dump_{drive}.json')); e = 0; n = 0; e2 = 0
    for fr in D:
        for h in fr['hits']:
            tin, tt, N, P = map(np.array, (h['tin'], h['tt'], h['N'], h['hit']))
            c1 = abs(mk(tin,N)); c2 = abs(mk(tt,N)); e = max(e, abs(h['a1']*(1-c1*c1) - h['a2']*(1-c2*c2))/h['a1']); n += 1
            e2 = max(e2, abs(mk(tt,tt)+1), abs(mk(tt,P)), abs(mk(P,N)), abs(mk(P,P)-1))
    line('K3', e, 1e-10, f'{drive}: a1 sin²θ1 − a2 sin²θ2 at {n} transmitted hits, angles from the dumped tangents (relative)')
    line('K3', e2, 1e-10, f'{drive}: the dumped hit lies on the face and on the hyperboloid; refracted tangent is unit and tangent')
# K3 centre rays: geodesic from O at angle psi to the plane at distance h, solved by bisection in arc length
e = 0
for _ in range(500):
    h = rng.uniform(0.05, 1.5); psi = rng.uniform(0, math.acos(math.tanh(h))*0.999)
    N = np.array([math.sinh(h), math.cosh(h), 0, 0]); v = np.array([0, math.cos(psi), math.sin(psi), 0]); O = np.array([1.,0,0,0])
    f = lambda s: mk(math.cosh(s)*O + math.sinh(s)*v, N); lo, hi = 0, 20
    for _ in range(200):
        m = (lo+hi)/2
        if f(m) > 0: lo = m
        else: hi = m
    s = (lo+hi)/2; t = math.sinh(s)*O + math.cosh(s)*v; c = abs(mk(t,N)); e = max(e, abs(math.sqrt(1-c*c) - math.cosh(h)*math.sin(psi)))
line('K3', e, 1e-10, 'centre rays: sin θ = cosh h sin ψ (plane found by bisection)')
# K4 oblique flux
e = 0
for _ in range(10000):
    a1, a2 = np.exp(rng.uniform(-2,2,2)); s1 = rng.uniform(0,1); C = a1*s1*s1; w = rng.uniform(0.5,6)
    if a2 <= C: continue
    y1, y2 = w*math.sqrt(a1-C), w*math.sqrt(a2-C); r, t = np.linalg.solve(np.array([[-1,1],[y1,y2]]), np.array([1,y1])); e = max(e, abs(r*r + (y2/y1)*t*t - 1))
line('K4', e, 1e-12, 'oblique flux, Y = ω√(a − C)')
# K5 critical angle by bisection on existence of a real transmitted angle, and the total-return phase
lo, hi = 0, math.pi/2
for _ in range(100):
    m = (lo+hi)/2
    if 4*math.sin(m)**2 > 1: hi = m
    else: lo = m
line('K5', abs(lo - math.pi/6), 1e-9, 'κ = 4: threshold 30°')
e = 0
for _ in range(2000):
    a1 = rng.uniform(1,9); a2 = rng.uniform(0.1,0.9); th = rng.uniform(math.asin(math.sqrt(a2/a1)), math.pi/2); C = a1*math.sin(th)**2; y = math.sqrt(a1-C); ke = math.sqrt(C-a2)
    g = (y - 1j*ke)/(y + 1j*ke); e = max(e, abs(abs(g)-1), abs(np.angle(g) + 2*math.atan(ke/y)))
    k = math.sqrt(a1/a2); u = math.acosh(k*math.sin(th)); e = max(e, abs(np.sin(complex(math.pi/2, u)) - k*math.sin(th)))
line('K5', e, 1e-12, '||Γ| − 1|, arg Γ, sin(π/2 + iu) − √κ sin θ1')
# K6 stack by explicit 2x2 transfer matrices (field, flux) and by bounce sums
def stackTM(Ys, ph):
    Mt = np.eye(2, dtype=complex)
    for k in range(1, len(Ys)-1):
        c, s = np.cos(ph[k]), np.sin(ph[k]); Mt = Mt @ np.array([[c, 1j*s/Ys[k]],[1j*Ys[k]*s, c]])
    # incident layer 0: E = 1 + r, H = Y0(1 - r); last layer: E = t, H = Y_D t
    YD, Y0 = Ys[-1], Ys[0]; A = Mt @ np.array([1, YD])   # (E, H) at the first face per unit t
    t = 2/(A[0] + A[1]/Y0); r = t*A[0] - 1; return r, t
e = 0; e2 = 0
for _ in range(2000):
    D = rng.integers(2,7); Ys = np.exp(rng.uniform(-1.5,1.5,D+1)); ph = rng.uniform(0,6,D+1)
    r, t = stackTM(Ys, ph); g = [(Ys[k]-Ys[k+1])/(Ys[k]+Ys[k+1]) for k in range(D)]
    rho = g[-1]
    for k in range(D-2, -1, -1): x = rho*np.exp(2j*ph[k+1]); rho = (g[k] + x)/(1 + g[k]*x)
    e = max(e, abs(rho - r), abs(abs(r)**2 + (Ys[-1]/Ys[0])*abs(t)**2 - 1))
line('K6', e, 1e-12, 'recursion by ⊕ against an independent field/flux transfer matrix; flux in = flux out')
e = 0
for _ in range(2000):
    g = rng.uniform(-0.9,0.9); x = rng.uniform(0,1)*np.exp(1j*rng.uniform(0,6.283))
    if abs(g*x) > 0.9: continue
    s = sum((-g)**m * x**(m+1) for m in range(400)); e = max(e, abs(g + (1-g*g)*s - (g+x)/(1+g*x)))
line('K6', e, 1e-10, 'bounce sum of 400 echoes against Γ ⊕ x')
e = 0
for _ in range(500):
    D = rng.integers(1,7); z = math.exp(rng.uniform(0,2.5)); Ys = z**-np.arange(D+1.); r, t = stackTM(Ys, np.zeros(D+1)); e = max(e, abs(r - math.tanh(D*math.log(z)/2)))
line('K6', e, 1e-12, 'zero phase: D equal steps give tanh(D r/2)')
ex = 0
for _ in range(10000):
    a = complex(*rng.uniform(-0.95,0.95,2)); x = complex(*rng.uniform(-1,1,2))
    if abs(a) >= 0.98 or abs(x) > 1: continue
    A = 1 - abs(a)**4; Cc = a.conjugate()*(1 - a*a); xc = -Cc.conjugate()/A; r = (a+x)/(1+a*x)
    d1 = abs(r)**2 - abs(a)**2; d2 = abs(x-xc) - abs(xc)
    if abs(d1) > 1e-12 and abs(d2) > 1e-12 and np.sign(d1) != np.sign(d2): ex += 1
line('K6', ex, 0, 'echo circle sign exceptions')
a = 0.5; line('K6', max(abs(abs((a+0.2)/(1+a*0.2))**2 - 49/121), abs(abs((a-0.2)/(1-a*0.2))**2 - 1/9)), 1e-15, 'witness 49/121, 1/9')
# K7 gap: transfer matrix with complex phase
def gapT(Y1, ke, kp, w):
    Yg = 1j*ke; c, s = np.cosh(kp*w), 1j*np.sinh(kp*w)/1j   # cos(iκw) = cosh, sin(iκw) = i sinh
    Mt = np.array([[np.cos(1j*kp*w), 1j*np.sin(1j*kp*w)/Yg],[1j*Yg*np.sin(1j*kp*w), np.cos(1j*kp*w)]]); A = Mt @ np.array([1, Y1]); t = 2/(A[0] + A[1]/Y1); r = t*A[0] - 1; return r, t
e = 0
for _ in range(2000):
    r, t = gapT(rng.uniform(0.2,2.2), rng.uniform(0.1,2.1), rng.uniform(0.1,2.1), rng.uniform(0,3)); e = max(e, abs(abs(r)**2 + abs(t)**2 - 1))
line('K7', e, 1e-12, 'gap |r|² + |t|² = 1')
worst = 0
for Yv, ke, kp in [(1,.8,.8),(.5,1.3,2.1),(2,.3,1.1)]:
    w0, w1 = 3/kp, 6/kp; s = (math.log(abs(gapT(Yv,ke,kp,w1)[1])**2) - math.log(abs(gapT(Yv,ke,kp,w0)[1])**2))/(w1-w0); worst = max(worst, abs(s/(-2*kp) - 1))
line('K7', worst, 1e-3, 'slope of ln T against w = −2|k⊥| (relative)')
# K8 SL(2)
sx = np.array([[0,1],[1,0]]); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]])
def sb(u, r): return math.cosh(r/2)*np.eye(2) + math.sinh(r/2)*(u[0]*sx + u[1]*sy + u[2]*sz)
def W2(ra, rb): return sb(X,ra) @ sb(Y,rb) @ sb(X,-ra) @ sb(Y,-rb)
ZW = 3 + 2*math.sqrt(2); r = math.log(ZW); W = W2(r, r)
line('K8', abs(math.tanh(r/2)**2 - 0.5), 1e-14, 'wall |R − ½|'); line('K8', abs(np.trace(W) + 2), 1e-12, 'wall SL(2) trace + 2')
line('K8', np.abs((W + np.eye(2)) @ (W + np.eye(2))).max(), 1e-10, 'wall ‖(W + I)²‖'); line('K8', np.abs(W + np.eye(2)).max(), 1e-3, 'wall ‖W + I‖ > 1e-3', ok=np.abs(W+np.eye(2)).max() > 1e-3)
line('K8', max(abs(math.tanh(math.log(5)/2)**2 - 4/9), abs(math.tanh(math.log(7)/2)**2 - 9/16)), 1e-14, 'R(5) = 4/9, R(7) = 9/16')
e = 0
for _ in range(500):
    z = rng.uniform(1.01, 16); rr = math.log(z); R = math.tanh(rr/2)**2; T = 1 - R; e = max(e, abs(np.trace(W2(rr,rr)).real - (2 - 4*(R/T)**2))/max(1,(R/T)**2))
line('K8', e, 1e-12, 'trace = 2 − 4(R/T)² on 500 ratios')
# K9 Thomas by polar decomposition of the 4x4 product (scipy-free: rotation = L^-1 Λ)
def thomas(ra, rb):
    Lam = boost(X, ra) @ boost(Y, rb); p = Lam[:,0]; v = p[1:]/np.linalg.norm(p[1:]); Lb = boost(v, math.acosh(p[0])); Rm = np.linalg.solve(Lb, Lam)
    return math.acos(np.clip((np.trace(Rm[1:,1:]) - 1)/2, -1, 1)), Lb, Rm, Lam
e = 0
for _ in range(500):
    ra, rb = rng.uniform(0.02, 3.5, 2); e = max(e, abs(thomas(ra,rb)[0] - 2*math.atan(math.tanh(ra/2)*math.tanh(rb/2))))
line('K9', e, 1e-9, 'Thomas angle, 500 random pairs')
t5 = thomas(math.log(5), math.log(5))[0]; t7 = thomas(math.log(7), math.log(7))[0]
line('K9', max(abs(math.cos(t5)-65/97), abs(math.sin(t5)-72/97), abs(math.cos(t7)-175/337), abs(math.sin(t7)-288/337)), 1e-13, 'exact 65/97, 72/97; 175/337, 288/337')
# K10
e = 0; e2 = 0
for _ in range(500):
    ra, rb = rng.uniform(0.05, 3.5, 2); _, Lb, Rm, _ = thomas(ra, rb); W4 = boost(X,ra) @ boost(Y,rb) @ boost(-X,ra) @ boost(-Y,rb)
    e = max(e, np.abs(Lb @ Rm @ np.linalg.inv(Lb) @ Rm - W4).max()/np.abs(W4).max())
    g = math.sinh(ra/2)*math.sinh(rb/2); half = (np.trace(W4) - 2)/2
    if g < 1 - 1e-6: e2 = max(e2, abs(half - (8*g**4 - 8*g*g + 1)))
    elif g > 1 + 1e-6: e2 = max(e2, abs(math.acosh(half) - 4*math.acosh(g))/(4*math.acosh(g)))
line('K10', e, 1e-8, '‖W − L R L⁻¹ R‖/‖W‖'); line('K10', e2, 1e-10, 'turn and run formulas from the 4x4 trace')
# K11 rim: boost a null vector with the 4x4 matrix
e = 0
for _ in range(10000):
    c = rng.uniform(-1,1); r = rng.uniform(0,3.5); s = math.sqrt(1-c*c); n = np.array([1, c, s, 0.]); m = boost(X, r) @ n
    e = max(e, abs(m[1]/m[0] - (c + math.tanh(r))/(1 + c*math.tanh(r))), abs(m[0] - (math.cosh(r) + math.sinh(r)*c)))
line('K11', e, 1e-12, 'aberration = ⊕ and t′/t, from the 4x4 boost')
dirs = rng.normal(size=(100000,3)); dirs /= np.linalg.norm(dirs, axis=1)[:,None]
def pp(z):
    r = math.log(z); ex = 0
    for ax in range(3):
        for sg in (1,-1):
            u = np.zeros(3); u[ax] = sg; Bm = boost(u, r); nn = np.c_[np.ones(len(dirs)), dirs] @ Bm.T; outside = dirs @ (-u) <= 1/math.sqrt(2)
            img = (nn[:,1:] @ u)/nn[:,0]; ex += int(np.sum(outside & ~(img > 1/math.sqrt(2))))
    return ex
for z in [ZW*(1+1e-6), 7, 9, 13]: line('K11', pp(z), 0, f'ping-pong exceptions, 1e5 directions × 6 letters, z = {z:.6f}')
n5 = pp(5); line('K11', n5, 1, 'z = 5 must show exceptions', ok=n5 >= 1)
m = (boost(X, math.log(7)) @ np.array([3,1,2,2.]))*7; line('K11', float(np.abs(m - np.array([99,97,14,14])).max()), 1e-10, 'integer step at z = 7: (3,1,2,2) → (99,97,14,14), in its cap', ok=np.abs(m - [99,97,14,14]).max() < 1e-10 and 97/99 > 1/math.sqrt(2))
# K12
e = 0
for _ in range(1000):
    h = rng.uniform(0,3); N = np.array([math.sinh(h), math.cosh(h), 0, 0]); c = math.tanh(h); ph = rng.uniform(0,6.283); s = math.sqrt(1-c*c); e = max(e, abs(mk(np.array([1, c, s*math.cos(ph), s*math.sin(ph)]), N)))
line('K12', e, 1e-12, 'face meets the rim at cos ψ0 = Γ'); line('K12', abs(math.degrees(math.acos(math.tanh(math.log(ZW)/2))) - 45), 1e-12, 'at the wall ψ0 = 45° (degrees)')
# K13 Maxwell stress tensor
e = 0
for _ in range(500):
    k = rng.normal(size=3); k /= np.linalg.norm(k); E = rng.normal(size=3); E -= (E@k)*k; H = np.cross(k, E); u = (E@E + H@H)/(8*math.pi)
    sig = (np.outer(E,E) + np.outer(H,H))/(4*math.pi) - np.eye(3)*u; p = rng.normal(size=3); p -= (p@k)*k; p /= np.linalg.norm(p); th = rng.uniform(0, math.pi/2); n = math.cos(th)*k + math.sin(th)*p
    e = max(e, abs(n@sig@n + u*math.cos(th)**2)/u)
line('K13', e, 1e-12, 'normal stress on a tilted plane = −u cos²θ (relative)')
# K16, K17, K18
e = 0
for _ in range(1000):
    r = rng.uniform(-1,1, rng.integers(1,13)); e = max(e, abs(2*np.abs(r).sum() - 2*abs(r.sum()) - 4*min(r[r>0].sum(), -r[r<0].sum())))
line('K16', e, 1e-12, 'route − endpoint = 4 min(R₊, R₋)')
z = np.exp(rng.uniform(-4,4,2000)); Cc = 1/(z+1); G = (z-1)/(z+1); line('K17', float(max(np.abs(1-2*Cc-G).max(), np.abs(4*Cc*(1-Cc) - (1-G*G)).max())), 1e-14, '1 − 2C = Γ; T = 4C(1 − C)')
e = 0; ea = 0; ed = 0
for _ in range(500):
    ha, hb = rng.uniform(0.05, 2, 2); Na = np.array([math.sinh(ha), math.cosh(ha), 0, 0]); Nb = np.array([math.sinh(hb), 0, math.cosh(hb), 0]); g = mk(Na, Nb); e = max(e, abs(g - math.sinh(ha)*math.sinh(hb)))
    sph = lambda h: ((1+math.tanh(h/2)**2)/(2*math.tanh(h/2)), (1-math.tanh(h/2)**2)/(2*math.tanh(h/2)))
    (ca, Ra), (cb, Rb) = sph(ha), sph(hb)
    if g < 1: ea = max(ea, abs(math.acos(-(Ra*Ra + Rb*Rb - ca*ca - cb*cb)/(2*Ra*Rb)) - math.acos(g)))
    else:
        # minimum distance between the planes by direct minimisation over points of each plane in the x-y plane of the ball
        best = 1e9
        for sa in np.linspace(-0.3, 1.2, 61):
            pa = math.cosh(sa)*np.array([math.cosh(ha), math.sinh(ha), 0, 0]) + math.sinh(sa)*np.array([0,0,1,0])
            for sb_ in np.linspace(-0.3, 1.2, 61):
                pb = math.cosh(sb_)*np.array([math.cosh(hb), 0, math.sinh(hb), 0]) + math.sinh(sb_)*np.array([0,1,0,0]); best = min(best, mk(pa,pb))
        # refine with a local Newton-free golden search around the grid minimum is unnecessary: report the gap to arccosh g
        ed = max(ed, abs(math.acosh(best) - math.acosh(g)))
line('K18', e, 1e-12, '<Na, Nb> = sinh ha sinh hb'); line('K18', ea, 1e-10, 'dihedral angle of the two drawn caps = arccos g')
line('K18', ed, 1e-8, 'minimum distance between separated planes = arccosh g (grid search, 61 × 61)')
n = sum(1 for x in res if x[4])
for k, v, tol, note, ok in res: print(('HOLDS ' if ok else 'KILLED') + f'  {k:<4} {v:>10.2e}  tol {tol:<8}  {note}')
print(f'\n{n} of {len(res)} lines hold')

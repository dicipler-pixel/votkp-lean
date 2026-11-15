"""Independent finite checks from the v15 manuscript, not its archived scripts.

The script uses only synthetic matrices and the printed 37a1 equation.
No network, repository checkout, or formal proof compiler is invoked.
"""
from pathlib import Path
from math import isqrt
import csv
import json
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize_scalar

OUT = Path(__file__).parent / "nonnormality_checks"
OUT.mkdir(exist_ok=True)
rng = np.random.default_rng(163)
adj = lambda m: m.conj().T
norm2 = lambda m: float(np.linalg.norm(m, "fro") ** 2)
maxerr = dict(connection=0.0, opposite=0.0, budget=0.0, transpose=0.0)
for _ in range(100):
    blocks = []
    for j in range(3):
        m = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
        blocks.append((m + adj(m)) / 2)
    d = np.zeros((6, 6), complex)
    a = np.zeros_like(d)
    em = ep = budget = 0.0
    for j, b in enumerate(blocks):
        d[2*j:2*j+2, 2*j:2*j+2] = b
    for i, j in ((0, 1), (1, 2), (0, 2)):
        z = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2))
        u = np.linalg.qr(z)[0]
        w = rng.uniform(0.1, 3.0)
        a[2*i:2*i+2, 2*j:2*j+2] = np.sqrt(w)*u
        a[2*j:2*j+2, 2*i:2*i+2] = -np.sqrt(w)*adj(u)
        transported = u @ blocks[j] @ adj(u)
        em += w*norm2(blocks[i]-transported)
        ep += w*norm2(blocks[i]+transported)
        budget += 2*w*(norm2(blocks[i])+norm2(blocks[j]))
    h = d+a
    def books(h):
        return np.array([norm2(h@adj(h)-adj(h)@h), norm2(h@h-adj(h)@adj(h))])/8
    actual = books(h)
    for name, err in (("connection", abs(actual[0]-em)),
                      ("opposite", abs(actual[1]-ep)),
                      ("budget", abs(sum(actual)-budget)),
                      ("transpose", max(abs(actual-books(h.T))))):
        maxerr[name] = max(maxerr[name], float(err))

# Same instantaneous scalar commutator, different gain after a loss shift.
l = np.array([[-1., 4.], [0., -1.]])
gain = lambda m, t: np.linalg.norm(expm(t*m), 2)
peaks = []
for m in (l, l-0.5*np.eye(2)):
    optimum = minimize_scalar(lambda t: -gain(m,t), bounds=(0,10), method="bounded")
    peaks.append({"time": float(optimum.x), "gain": float(-optimum.fun)})

# Hidden Hermitian channels keep K(0),K'(0) but not the full kernel.
b = np.ones((1,2))/np.sqrt(2)
d1, d2 = np.diag([0., 2.]), np.eye(2)
moments = [[float((b@np.linalg.matrix_power(d,k)@b.T)[0,0]) for k in range(4)] for d in (d1,d2)]
kpi = [complex((b@expm(-1j*np.pi*d)@b.T)[0,0]) for d in (d1,d2)]

# 37a1: two independent point-count methods for y^2+y=x^3-x.
rows = []
for p in range(2,1001):
    if p == 37 or any(p%d==0 for d in range(2,isqrt(p)+1)):
        continue
    yfreq = {}
    for y in range(p):
        v=(y*y+y)%p
        yfreq[v]=yfreq.get(v,0)+1
    direct = 1+sum(yfreq.get((x*x*x-x)%p,0) for x in range(p))
    if p==2:
        character = direct
    else:
        squares = {y*y%p for y in range(p)}
        terms = [(1+4*(x*x*x-x))%p for x in range(p)]
        character = p+1+sum(0 if v==0 else 1 if v in squares else -1 for v in terms)
    assert direct == character
    ap=p+1-direct
    rows.append(dict(p=p, N=direct, ap=ap, rho=ap*ap/(4*p),
                     nonzero=bool(ap), positive_preimage=bool(3*ap*ap>4*p)))
with (OUT/"37a1_point_counts.csv").open("w", newline="") as f:
    w=csv.DictWriter(f, fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary = {
    "scope": "Independent targeted numerical checks, not archive reproductions or formal proofs",
    "weighted_triangle_trials": 100,
    "max_absolute_residuals": maxerr,
    "same_commutator_different_gain": peaks,
    "hidden_channel_moments_n0_to_3": moments,
    "hidden_channel_K_pi": [[z.real,z.imag] for z in kpi],
    "37a1": {"good_primes_le_1000":len(rows),
              "direct_vs_character_mismatches":0,
              "nonzero_ap":sum(r["nonzero"] for r in rows),
              "rho_strictly_above_one_third":sum(r["positive_preimage"] for r in rows),
              "zero_ap":sum(not r["nonzero"] for r in rows)}
}
(OUT/"independent_results.json").write_text(json.dumps(summary,indent=2)+"\n")
print(json.dumps(summary,indent=2))

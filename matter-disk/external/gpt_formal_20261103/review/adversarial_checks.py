"""Independent finite checks for the formal matter/gas review; see protocol."""
from pathlib import Path
import hashlib
import json
import math
import platform

import numpy as np
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parent
RNG = np.random.default_rng(2026110307)
TOL = 2e-12


def norm(a):
    return float(np.linalg.norm(a, 2))


def contraction(n):
    a = RNG.normal(size=(n,n)) + 1j * RNG.normal(size=(n,n))
    u, _ = np.linalg.qr(a)
    return (u * RNG.uniform(0, 1, n)) @ u.conj().T


def cross(c, k):
    b = c[:k, k:]
    return b @ b.conj().T


def eig(a):
    return np.linalg.eigvalsh((a + a.conj().T) / 2)


rows = []
stable_cases = 0
for case in range(128):
    n, k = 12, 5
    c = contraction(n)
    other = contraction(n)
    alpha = float(RNG.uniform(1e-5, .03))
    d = (1-alpha)*c + alpha*other
    delta = norm(c-d)
    xc, xd = cross(c, k), cross(d, k)
    change = norm(xc-xd)
    assert change <= delta + TOL
    ecs, eds = eig(xc), eig(xd)
    for theta in (.002, .01, .03, .06, .09, .13, .2):
        margin = float(np.min(np.abs(ecs-theta)))
        if margin > delta + 1e-11:
            assert np.count_nonzero(ecs >= theta) == np.count_nonzero(eds >= theta)
            stable_cases += 1
    rows.append(dict(delta=delta, gram_change=change, ratio=change/delta))

near_rows = []
theta = .09
for case in range(64):
    n, k = 12, 5
    z = RNG.normal(size=(n,n)) + 1j*RNG.normal(size=(n,n))
    u, _ = np.linalg.qr(z)
    p = u[:, :6] @ u[:, :6].conj().T
    alpha = float(RNG.uniform(.0001, .15))
    c = (1-alpha)*p + alpha*contraction(n)
    a, x = c[:k,:k], cross(c,k)
    f = a-a@a
    defect = c-c@c
    tau = norm(defect)
    ordering = [float(eig(f-x).min()), float(eig(x+tau*np.eye(k)-f).min())]
    assert min(ordering) >= -TOL
    ex, ef = eig(x), eig(f)
    margin = min(float(np.min(np.abs(ex-theta))),
                 float(np.min(np.abs(ef-theta))),
                 float(np.min(np.abs(ef-(theta+tau)))))
    if margin > 1e-11:
        lhs = int(np.count_nonzero(ef >= theta+tau))
        middle = int(np.count_nonzero(ex >= theta))
        rhs = int(np.count_nonzero(ef >= theta))
        assert lhs <= middle <= rhs
    near_rows.append(dict(tau=tau, ordering_min=min(ordering), margin=margin))

sharp = []
for eps in (1e-2, 1e-4, 1e-6):
    c = np.array([[.5,.5],[.5,.5]])
    d = np.array([[.5,.5-eps],[.5-eps,.5]])
    ratio = norm(cross(c,1)-cross(d,1))/norm(c-d)
    assert abs(ratio-(1-eps)) < 1e-9
    sharp.append(dict(epsilon=eps, ratio=ratio, exact_ratio=1-eps))

boundary = []
for eps in (1e-3,1e-6,1e-9):
    low = np.array([[.5,.3-eps],[.3-eps,.5]])
    high = np.array([[.5,.3+eps],[.3+eps,.5]])
    counts = [int(np.count_nonzero(eig(cross(c,1)) >= theta)) for c in (low,high)]
    assert counts == [0,1]
    boundary.append(dict(epsilon=eps, input_distance=norm(low-high), counts=counts))

# Fock basis integer encoding, mode0 most-significant bit: |n0 n1 n2 n3>.
modes = 4
annihilators = []
for j in range(modes):
    aj = np.zeros((2**modes,2**modes),complex)
    mask = 1 << (modes-1-j)
    for s in range(2**modes):
        if s & mask:
            parity = sum((s >> (modes-1-q)) & 1 for q in range(j))
            aj[s ^ mask,s] = (-1)**parity
    annihilators.append(aj)
psi = np.zeros(16,complex)
psi[12] = psi[3] = 1/math.sqrt(2)
expect = lambda op: complex(np.vdot(psi,op@psi))
c = np.array([[expect(annihilators[j].conj().T @ annihilators[i])
               for j in range(modes)] for i in range(modes)])
ns = [a.conj().T@a for a in annihilators]
na, nb = ns[0]+ns[1], ns[2]+ns[3]
cov = (expect(na@nb)-expect(na)*expect(nb)).real
schmidt = np.linalg.svd(psi.reshape(4,4),compute_uv=False)
probs = schmidt[schmidt>1e-12]**2
entropy = -float(np.sum(probs*np.log(probs)))
assert np.max(np.abs(c-.5*np.eye(4))) < TOL
assert abs(cov+1)<TOL and abs(entropy-math.log(2))<TOL

spectrum = np.array([-3.,-1.,1.,3.])
weights = [np.full(4,.25),np.array([3,7,1,5])/16]
hs = []
spectral_rows = []
for ix,w in enumerate(weights):
    e0 = np.array([1.,0.,0.,0.])
    v = np.sqrt(w)
    u = (e0-v)/np.linalg.norm(e0-v)
    r = np.eye(4)-2*np.outer(u,u)
    h = r @ np.diag(spectrum) @ r.T
    hs.append(h)
    coupling2 = float(h[0,1:]@h[1:,0])
    amplitude = complex(expm(-1j*math.pi*h/4)[0,0])
    assert abs(h[0,0])<TOL and abs(coupling2-5)<TOL
    assert np.max(np.abs(np.linalg.eigvalsh(h)-spectrum))<TOL
    for z in (.2+.7j, 2+1j, -4+.2j):
        g = np.linalg.inv(z*np.eye(4)-h)[0,0]
        formula = (z**3-5*z+3*ix)/(z**4-10*z*z+9)
        assert abs(g-formula)<TOL
    probability = abs(amplitude)**2
    assert abs(probability-(0 if ix==0 else 1/32))<TOL
    spectral_rows.append(dict(weights=w.tolist(),mean=float(w@spectrum),
                             second_moment=float(w@(spectrum**2)),
                             third_moment=float(w@(spectrum**3)),
                             coupling_square=coupling2,
                             survival_probability=probability))

report = {
    "status":"PASS",
    "protocol_sha256":hashlib.sha256((ROOT/'ADVERSARIAL_CHECK_PROTOCOL.md').read_bytes()).hexdigest(),
    "python":platform.python_version(),
    "scope":"Finite implementation checks and explicit counterexamples; not substitutes for analytic proofs.",
    "perturbation_pairs":len(rows),
    "max_random_lipschitz_ratio":max(r['ratio'] for r in rows),
    "certified_margin_cases":stable_cases,
    "near_projector_cases":len(near_rows),
    "minimum_ordering_eigenvalue":min(r['ordering_min'] for r in near_rows),
    "smallest_near_threshold_margin":min(r['margin'] for r in near_rows),
    "sharp_lipschitz_family":sharp,
    "discontinuous_threshold_family":boundary,
    "nonGaussian_counterexample":{
        "covariance_error":float(np.max(np.abs(c-.5*np.eye(4)))),
        "cross_gram_trace":float(np.trace(cross(c,2)).real),
        "number_covariance":cov,
        "bipartite_entropy":entropy,
        "fixed_total_number":float(expect(na+nb).real)},
    "full_spectrum_response_witness":spectral_rows,
}
(ROOT/'adversarial_results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))

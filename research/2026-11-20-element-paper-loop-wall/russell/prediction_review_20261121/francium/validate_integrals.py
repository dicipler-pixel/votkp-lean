"""Compare spinor MP2 with PySCF RMP2 and UMP2, plus a complex phase check."""
import json
import numpy as np
from pyscf import lib, scf, mp
from atomic_control import build, mp2
from eom_control import densities

lib.num_threads(1)
rng = np.random.default_rng(71)
for charge in (1, 2):
    mol = build('Rb', charge, 'coarse')
    hf = scf.RHF(mol) if charge == 1 else scf.UHF(mol)
    hf.chkfile = None
    hf.conv_tol = 1e-11
    hf.kernel()
    assert hf.converged
    correlation = mp.MP2(hf).kernel()[0]
    ghf = hf.to_ghf()
    custom, gap = mp2(ghf)
    ghf.mo_coeff = ghf.mo_coeff * np.exp(2j * np.pi * rng.random(ghf.mo_occ.size))
    phases, _ = mp2(ghf)
    assert max(abs(custom - correlation), abs(phases - correlation)) < 1e-9
    vals = dict(charge=charge, builtin=float(correlation), custom=custom, phases=phases,
                max_discrepancy_Ha=float(max(abs(custom-correlation), abs(phases-correlation))))
    print(json.dumps(vals))

# Test the implementation of the full (pq|rs) spinor tensor against *unpacked*,
# direct four-index AO sums on a very small spherical s,p test basis.
from pyscf import gto
m = gto.M(atom='He', basis=[[0,[1.3,1]], [1,[.4,1]]], verbose=0)
r = rng.standard_normal((2*m.nao, 5)) + 1j*rng.standard_normal((2*m.nao, 5))
c, _ = np.linalg.qr(r)
d = densities(c,c)
a=(d @ m.intor('int2e',aosym='s4') @ d.T).reshape((5,)*4)
full = m.intor('int2e').reshape((m.nao,)*4)
b = np.zeros_like(a)
for left in (c[:m.nao], c[m.nao:]):
    for right in (c[:m.nao], c[m.nao:]):
        b+=np.einsum('ip,jq,kr,ls,ijkl->pqrs',left.conj(),left,right.conj(),right,full,optimize=True)
err=np.max(abs(a-b))
assert err < 1e-12
print(json.dumps(dict(direct_complex_spinor_max_discrepancy_Ha=float(err))))

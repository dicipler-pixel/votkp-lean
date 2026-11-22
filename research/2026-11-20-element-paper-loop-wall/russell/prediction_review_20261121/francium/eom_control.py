"""Spin–orbit IP-EOM-CCSD with occupied orbitals and MP2 virtual natural spinors."""
import argparse
import json

import numpy as np
from pyscf import lib, scf
from pyscf.cc import gccsd, eom_gccsd
from pyscf.data.nist import HARTREE2EV
from atomic_control import build


def densities(left, right):
    """Coefficients of alpha + beta transition densities in packed real AO pairs."""
    nao = left.shape[0] // 2
    rows, cols = np.tril_indices(nao)
    d = np.zeros((left.shape[1], right.shape[1], len(rows)), dtype=complex)
    for spin in (0, 1):
        a = left[spin*nao:(spin+1)*nao]
        b = right[spin*nao:(spin+1)*nao]
        for i in range(left.shape[1]):
            d[i] += (a[rows, i, None].conj() * b[cols]).T
            d[i] += ((rows != cols)[:, None] * a[cols, i, None].conj() * b[rows]).T
    return d.reshape(-1, len(rows))


def contract(d, eri):
    return d.real @ eri + 1j * (d.imag @ eri)


def virtual_density(hf, eri):
    occupied = hf.mo_occ > 0
    o, v = hf.mo_coeff[:, occupied], hf.mo_coeff[:, ~occupied]
    eo, ev = hf.mo_energy[occupied], hf.mo_energy[~occupied]
    d = densities(o, v)
    ovov = (contract(d, eri) @ d.T).reshape(len(eo), len(ev), len(eo), len(ev))
    ijab = ovov.transpose(0, 2, 1, 3)
    ijab = ijab - ijab.swapaxes(2, 3)
    gap = eo[:, None, None, None] + eo[None, :, None, None] - ev[None, None, :, None] - ev[None, None, None, :]
    amplitude = ijab.conj() / gap
    dm = 0.5 * np.einsum('ijac,ijbc->ab', amplitude, amplitude.conj(), optimize=True)
    # Direct expression also fixes the complex conjugation convention above.
    e2_direct = 0.25 * np.sum(abs(ijab)**2 / gap)
    # Standard MP2 amplitude is <ab||ij>/denominator, its inner product with <ij||ab> gives energy.
    e2_from_t = (0.25 * np.sum(amplitude * ijab)).real
    assert abs(e2_direct - e2_from_t) < 1e-11
    eigenvalues, vectors = np.linalg.eigh(dm)
    return eigenvalues[::-1], vectors[:, ::-1], float(e2_direct)


def run(atom, basis, budget, threads):
    lib.num_threads(threads)
    mol = build(atom, 1, basis)
    hf = scf.GHF(mol)
    hf.with_soc = True
    hf.conv_tol = 1e-11
    hf.chkfile = None
    hf.kernel()
    if not hf.converged:
        raise RuntimeError('closed-cation reference failed to converge')
    eri = mol.intor('int2e', aosym='s4')
    vals, vectors, emp2 = virtual_density(hf, eri)
    if budget < len(vals):
        # Extend the budget to cover every member of a near-degenerate multiplet.
        keep = int(np.sum(vals >= vals[budget-1] - max(1e-11, vals[budget-1]*1e-5)))
    else:
        keep = len(vals)
    occ = hf.mo_occ > 0
    retained = vectors[:, :keep]
    virtual_fock = (retained.conj().T * hf.mo_energy[~occ]) @ retained
    vf_energy, vf_vectors = np.linalg.eigh(virtual_fock)
    coefficients = np.column_stack([hf.mo_coeff[:, occ], hf.mo_coeff[:, ~occ] @ (retained @ vf_vectors)])
    orbital_energies = np.concatenate([hf.mo_energy[occ], vf_energy])
    orbital_occupations = np.r_[hf.mo_occ[occ], np.zeros(keep)]
    coupler = gccsd.GCCSD(hf, mo_coeff=coefficients, mo_occ=orbital_occupations)
    coupler.max_memory = 650
    coupler.conv_tol = 1e-9
    coupler.conv_tol_normt = 1e-7
    coupler.max_cycle = 80

    def transform(c):
        d = densities(c, c)
        return contract(d, eri) @ d.T

    tensors = gccsd._make_eris_incore(coupler, mo_coeff=coefficients, ao2mofn=transform)
    assert np.max(abs(tensors.mo_energy - orbital_energies)) < 2e-5
    del eri
    ecorr, _, _ = coupler.kernel(eris=tensors)
    if not coupler.converged:
        raise RuntimeError('CCSD failed to converge')
    eom = eom_gccsd.EOMIP(coupler)
    eom.conv_tol = 1e-9
    roots, eigenvectors = eom.kernel(nroots=6, eris=tensors)
    if not np.all(eom.converged):
        raise RuntimeError('EOM failed to converge')
    r1 = [eom.vector_to_amplitudes(v)[0] for v in eigenvectors]
    hole_weights = [[float(np.vdot(v[-4:],v[-4:]).real), float(np.vdot(v[-6:-4],v[-6:-4]).real)] for v in r1]
    print(json.dumps(dict(atom=atom, basis=basis, virtual_budget=budget, retained=keep,
        normalized_right_vector_hole_weights_p32_p12=hole_weights,
        virtual_occupations_captured=float(vals[:keep].sum()/vals.sum()),
        full_space_closed_MP2_Hartree=emp2, active_CCSD_correlation_Hartree=float(ecorr),
        IE2_roots_eV=(np.asarray(roots)*HARTREE2EV).tolist())), flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('atom')
    p.add_argument('basis')
    p.add_argument('budget', type=int)
    p.add_argument('--threads', type=int, default=1)
    a = p.parse_args()
    run(a.atom, a.basis, a.budget, a.threads)

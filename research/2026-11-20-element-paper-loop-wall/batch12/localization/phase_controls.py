"""Falsifiers for plane-wave overlap signs, occupied-rank loss and log polarization."""
from argparse import ArgumentParser
from pathlib import Path

import numpy as np

from microscopic_response import load_states, overlap_matrix, shell_directions


def orthonormal(matrix):
    return np.linalg.qr(matrix)[0]


def site_toys():
    rng = np.random.default_rng(1701)
    # In one periodic chain with N sites, a contiguous half filled interval has
    # exactly one lost state under a unit shift. S(q)/q² = N/(2π²), per electron,
    # for a=1. Its full twist-overlap determinant vanishes on every such torus.
    for mesh in (4, 8, 16, 32):
        occupied = np.eye(mesh)[:, :mesh//2]
        shift = np.roll(np.eye(mesh), 1, axis=0)
        m = occupied.T @ shift @ occupied
        rank = m.shape[0]
        coefficient = (rank - np.sum(m*m))/rank/(2*np.pi/mesh)**2
        assert np.isclose(coefficient,mesh/(2*np.pi**2))
        assert np.linalg.matrix_rank(m) == rank - 1
    # Gauge-rotate the two endpoint occupied frames, permitting unequal ranks.
    for a,b in ((1,3),(4,4)):
        u = orthonormal(rng.normal(size=(9,a)) + 1j*rng.normal(size=(9,a)))
        v = orthonormal(rng.normal(size=(9,b)) + 1j*rng.normal(size=(9,b)))
        left = orthonormal(rng.normal(size=(a,a)) + 1j*rng.normal(size=(a,a)))
        right = orthonormal(rng.normal(size=(b,b)) + 1j*rng.normal(size=(b,b)))
        m = v.conj().T @ u
        changed = (v@right).conj().T @ (u@left)
        assert np.allclose(np.linalg.svd(m,compute_uv=False),
                           np.linalg.svd(changed,compute_uv=False))
        p,q = u@u.conj().T,v@v.conj().T
        loss = np.sum(abs(p-q)**2)/2
        assert np.isclose(loss,abs(a-b)/2 + min(a,b) - np.sum(abs(m)**2))
    # One filled, independent orbital per cell: two orthogonal point positions
    # at ±d in a cell, equally occupied by that orbital. WS-center variance
    # vanishes, but the continuum phase factor is cos(qd).
    for q in (0.01,0.1,0.5):
        d=0.3
        u=np.ones(2)/np.sqrt(2)
        twist=np.diag(np.exp(1j*q*np.array([-d,d])))
        overlap=u.conj()@twist@u
        L=(1-abs(overlap)**2)/q**2
        log_L=-np.log(abs(overlap)**2)/q**2
        assert np.isclose(L,(np.sin(q*d)/q)**2) and log_L>=L-1e-12
    print("toy half-filled chain: exact linear growth and zero twist determinant")
    print("gauge changes: principal angles and exact rank/overlap decomposition invariant")
    print("filled atomic orbital: cell-center coefficient zero, microscopic positive")


def check_qe_wrap(save,symbol,mesh):
    states, ranks, kfrac, keys, _, rec = load_states(save,symbol,mesh)
    lookup = {tuple(key):i for i,key in enumerate(keys)}
    grid = 32
    fractional_positions = np.indices((grid,)*3).reshape(3,-1).T / grid

    def fft_state(index):
        G,_,C = states[index]
        assert len(np.unique(G%grid,axis=0)) == len(G)
        cube = np.zeros((grid,grid,grid,ranks[index]), dtype=complex)
        cube[tuple(G.T%grid)] = C
        return np.fft.ifftn(cube,axes=(0,1,2),norm="ortho").reshape(-1,ranks[index])

    checked = 0
    rejected = 0
    max_error = 0.
    for kind, g, _ in shell_directions(rec):
        if kind != "shortest":
            continue
        for i, key in enumerate(keys):
            j = lookup[tuple((key+g)%mesh)]
            wrap = np.rint(kfrac[i]+g/mesh-kfrac[j]).astype(int)
            if not np.any(wrap) or min(ranks[i],ranks[j]) == 0:
                continue
            u,v = fft_state(i),fft_state(j)
            direct = v.conj().T @ (np.exp(2j*np.pi*fractional_positions@wrap)[:,None] * u)
            coeff = overlap_matrix(states[i],states[j],wrap)
            wrong = overlap_matrix(states[i],states[j],-wrap)
            max_error = max(max_error,np.max(abs(coeff-direct)))
            rejected += int(np.linalg.norm(coeff-wrong)>1e-3)
            checked += 1
            break
    assert checked > 0 and max_error < 1e-10 and rejected == checked
    print(f"{symbol} {mesh}^3: {checked} zone-wrap links checked on independent FFT grid, "
          f"max residual {max_error:.2e}; wrong wrap sign rejected on {rejected}")


if __name__ == "__main__":
    parser=ArgumentParser(description=__doc__)
    parser.add_argument("work",type=Path,help="norm-conserving QE work directory")
    args=parser.parse_args()
    site_toys()
    for el in ("Kr","Rb"):
        check_qe_wrap(args.work/"ws"/f"{el}-4"/"out/system.save",el,4)

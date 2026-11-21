"""Finite-q connected density structure factor of a smooth Slater projector.

Tr(P - P U_q* P U_q) / (Tr P |q|²), U_q = exp(i q·r), uses the actual
plane-wave position phase, with no Wigner–Seitz center approximation.
"""
import argparse
import csv
import hashlib
from itertools import product
from pathlib import Path
import struct
import sys
import xml.etree.ElementTree as ET

import numpy as np
from scipy.io import FortranFile

from site_tensor import BOHR_A
from weight_io import read_weights

EXPECTED_UPF = {
    "Kr": "42d25c77ed07bf438be5b8543f4afd66f10ae46f90d1b80155b6519f4c9bb8c3",
    "Rb": "b40d0424cd413a24da3396b6fb62081bbb13be49acbf1fc666ca976c239ed736",
}


def numbers(text):
    return np.fromstring(text, sep=" ")


def miller_keys(miller):
    """Integer keys preserving the identity of plane waves across k-dependent bases."""
    # Bound checked on every call, including the reciprocal-zone wraps.
    assert abs(miller).max(initial=0) < 128
    return ((miller[:,0]+128)*256 + miller[:,1]+128)*256 + miller[:,2]+128


def load_states(save, symbol, mesh, family="NC", stream=False):
    if family=="NC":
        potential=save/f"{symbol}.upf"
        expected=EXPECTED_UPF[symbol]
    else:
        potential=next(save.glob(f"{symbol}.*-kjpaw_psl.1.0.0.UPF"))
        expected={"Rb":"6e8ebe2c70064c509eb4a50578939662802c3b1dc99b51b8d302487842dc9fdb",
                  "Kr":"e642273d4df7ae7c3d0d195b301f30336ff2b5977163d35f429270c7728ed4e8"}[symbol]
    assert hashlib.sha256(potential.read_bytes()).hexdigest()==expected
    root = ET.parse(save / "data-file-schema.xml").getroot().find("output")
    structure = root.find("atomic_structure")
    cell = np.array([numbers(v.text) for v in structure.find("cell")]) * BOHR_A
    units = 2 * np.pi / float(structure.get("alat"))
    rec = np.array([numbers(v.text) for v in root.find("basis_set/reciprocal_lattice")])
    assert np.allclose(rec * units / BOHR_A, 2*np.pi*np.linalg.inv(cell).T)
    blocks = root.findall("band_structure/ks_energies")
    kcart = np.array([numbers(b.findtext("k_point")) for b in blocks])
    kfrac = kcart @ np.linalg.inv(rec)
    mesh_keys = np.rint((kfrac-kfrac[0])*mesh).astype(int) % mesh
    assert len(blocks) == mesh**3 == len(set(map(tuple,mesh_keys)))
    assert np.max(abs((kfrac-kfrac[0])*mesh - np.rint((kfrac-kfrac[0])*mesh))) < 1e-8
    assert np.ptp([float(b.find("k_point").get("weight")) for b in blocks]) < 1e-10

    energies = np.array([numbers(b.findtext("eigenvalues")) for b in blocks])
    mask = np.zeros_like(energies, dtype=bool)
    if symbol == "Rb":
        outer = energies[:,4:]
        order = np.argsort(outer,axis=None)
        count = mesh**3 // 2
        assert 2*count == mesh**3
        assert outer.flat[order[count]] - outer.flat[order[count-1]] > 1e-10
        rows, cols = np.unravel_index(order[:count], outer.shape)
        mask[rows,cols+4] = True
    else:
        first = 0 if family=="NC" else 5
        last = first+4
        assert energies[:,last].min() > energies[:,last-1].max()
        mask[:,first:last] = True
    def each_state():
        for i, active in enumerate(mask):
            selected = np.flatnonzero(active)
            if len(selected) == 0:
                yield None
                continue
            with FortranFile(save / f"wfc{i+1}.dat", "r") as src:
                ik,x,y,z,spin,gamma,scale = struct.unpack("=i3diid", src.read_record("u1"))
                assert ik == i+1 and spin == 1 and gamma == 0 and scale == 1
                assert np.allclose([x,y,z], kcart[i]*units,atol=1e-9,rtol=0)
                _,npw,npol,nbnd = src.read_record("i4")
                assert npol == 1 and nbnd == len(active) and npw == int(blocks[i].findtext("npw"))
                src.read_record("f8")
                miller = src.read_record("i4").reshape(-1,3)
                coefficients = []
                for band in range(selected[-1]+1):
                    vector = src.read_record("c16")
                    if active[band]:
                        coefficients.append(vector)
            order = np.argsort(miller_keys(miller))
            miller = miller[order]
            keys = miller_keys(miller)
            assert np.all(np.diff(keys) > 0)
            coeff = np.column_stack(coefficients)[order]
            gram = coeff.conj().T @ coeff
            if family=="NC":
                assert np.max(abs(gram - np.eye(len(selected)))) < 1e-7
            vals, basis = np.linalg.eigh(gram)
            assert vals.min()>1e-6
            coeff = coeff @ ((basis/np.sqrt(vals)) @ basis.conj().T)
            yield miller,keys,coeff
    states=each_state() if stream else list(each_state())
    return states, mask.sum(axis=1), kfrac, mesh_keys, cell, rec


def overlap_matrix(initial, final, wrap):
    """U_q transfers a source plane wave k+G to k'+(G+wrap)."""
    if initial is None or final is None:
        n = 0 if initial is None else initial[2].shape[1]
        m = 0 if final is None else final[2].shape[1]
        return np.empty((m,n), dtype=complex)
    miller, _, coeff = initial
    _, final_keys, final_coeff = final
    keys = miller_keys(miller + wrap)
    pos = final_keys.searchsorted(keys)
    existing = (pos < len(final_keys))
    existing[existing] = final_keys[pos[existing]] == keys[existing]
    return final_coeff[pos[existing]].conj().T @ coeff[existing]


def shell_directions(rec):
    """Cartesian axes of a cubic cell plus its shortest reciprocal-lattice star."""
    rows = []
    for g in product(range(-2,3), repeat=3):
        v = np.array(g) @ rec
        nonzero = np.flatnonzero(abs(v)>1e-7)
        if len(nonzero) and v[nonzero[0]]>0:
            rows.append((np.array(g), np.rint(v).astype(int), np.linalg.norm(v)))
    minimum = min(x[2] for x in rows)
    for g,v,length in rows:
        if np.isclose(length, minimum):
            yield "shortest", g, v
        elif np.isclose(length, 2.) and np.count_nonzero(v)==1:
            yield "axial", g, v


def phase_response(save, symbol, mesh, weights_path, family="NC"):
    states, ranks, kfrac, mesh_keys, cell, rec = load_states(save, symbol, mesh, family)
    index = {tuple(v):i for i,v in enumerate(mesh_keys)}
    rank = ranks.sum()
    assert rank > 0
    total_zero_q = sum(np.sum(abs(overlap_matrix(s,s,np.zeros(3,dtype=int)))**2)
                       for s in states)
    assert abs(total_zero_q - rank) < 1e-8
    if weights_path:
        X, weight_cell, weight_nu = read_weights(weights_path)
        assert np.allclose(cell,weight_cell) and np.isclose(2*rank/mesh**3,weight_nu)
        R = np.indices(X.shape).reshape(3,-1).T @ cell
        nu = 2*rank/mesh**3
    for kind,g,hkl in shell_directions(rec):
        q = g @ (2*np.pi*np.linalg.inv(cell).T) / mesh
        q2 = q @ q
        loss = 0.
        leakage = 0.
        negative_log_det_squared = 0.
        singular_blocks = 0
        for i,key in enumerate(mesh_keys):
            j = index[tuple((key + g) % mesh)]
            real_wrap = kfrac[i] + g/mesh - kfrac[j]
            wrap = np.rint(real_wrap).astype(int)
            assert np.max(abs(real_wrap-wrap)) < 1e-8
            overlap = overlap_matrix(states[i],states[j],wrap)
            square = np.sum(abs(overlap)**2)
            # Check the adjoint orientation independently with a reverse plane-wave match.
            reverse = overlap_matrix(states[j],states[i],-wrap)
            assert np.max(abs(overlap - reverse.conj().T), initial=0.) < 1e-10
            if ranks[i] != ranks[j]:
                singular_blocks += 1
            elif ranks[i]:
                _, log_abs = np.linalg.slogdet(overlap)
                negative_log_det_squared -= 2 * log_abs
            spill = min(ranks[i],ranks[j]) - square
            assert spill > -1e-9
            leakage += spill
            loss += abs(ranks[i]-ranks[j])/2
        L = (loss+leakage) / rank / q2
        row = dict(symbol=symbol, mesh=mesh, shell=kind,
                   h=int(hkl[0]),k=int(hkl[1]),l=int(hkl[2]),
                   q_inv_A=np.sqrt(q2), S_per_electron=(loss+leakage)/rank,
                   microscopic_L_A2=L, rank_change_A2=loss/rank/q2,
                   overlap_loss_A2=leakage/rank/q2,
                   unequal_rank_links=singular_blocks,
                   twist_modulus_zero_by_rank=bool(singular_blocks),
                   twist_log_L_A2=np.inf if singular_blocks else negative_log_det_squared/rank/q2)
        assert row["twist_log_L_A2"] >= L - 1e-9
        if weights_path:
            # The site coefficient is spin-summed, hence normalization by nu.
            Lsite = np.dot(X.ravel(), 1-np.cos(R@q)) / (nu*q2)
            row["WS_phase_L_A2"] = Lsite
            a = 2*np.max(abs(cell))
            radius = a * (np.sqrt(5)/4 if symbol == "Rb" else 1/2)
            # Replacing r by its cell center moves it by at most the WS covering radius.
            assert abs(np.sqrt(L) - np.sqrt(Lsite)) <= radius + 1e-9
        yield row


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("save", type=Path)
    parser.add_argument("symbol", choices=["Kr","Rb"])
    parser.add_argument("mesh", type=int)
    parser.add_argument("--weights", type=Path)
    parser.add_argument("--family",choices=["NC","PAW-smooth"],default="NC")
    args = parser.parse_args()
    rows = list(phase_response(args.save,args.symbol,args.mesh,args.weights,args.family))
    out = csv.DictWriter(sys.stdout,rows[0].keys())
    out.writeheader()
    out.writerows(rows)

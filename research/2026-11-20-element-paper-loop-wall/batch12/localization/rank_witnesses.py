"""One concrete occupied-to-empty sector per nontrivial rubidium twist."""
import argparse
import csv
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

import numpy as np

from microscopic_response import numbers, shell_directions

HARTREE_EV=27.211386245988


def witnesses(run,n):
    root=ET.parse(run/"out/system.save/data-file-schema.xml").getroot().find("output")
    states=root.findall("band_structure/ks_energies")
    assert len(states)==n**3
    reciprocal=np.array([numbers(v.text) for v in root.find("basis_set/reciprocal_lattice")])
    k=np.array([numbers(s.findtext("k_point")) for s in states])@np.linalg.inv(reciprocal)
    ids=np.rint((k-k[0])*n).astype(int)%n
    index={tuple(v):i for i,v in enumerate(ids)}
    energies=HARTREE_EV*np.array([numbers(s.findtext("eigenvalues"))[4:] for s in states])
    sorted_values=np.sort(energies.ravel())
    count=n**3//2
    mu=(sorted_values[count]+sorted_values[count-1])/2
    mask=energies<mu
    assert mask.sum()==count and not mask[:,1:].any()
    occupied=mask[:,0]
    for shell,g,hkl in shell_directions(reciprocal):
        targets=np.array([index[tuple((v+g)%n)] for v in ids])
        loss=np.flatnonzero(occupied & ~occupied[targets])
        assert len(loss)==np.sum(~occupied & occupied[targets])
        # Pick a pair closest in energy, independent of either wavefunction phase.
        a=loss[np.argmin(energies[targets[loss],0]-energies[loss,0])]
        b=targets[a]
        out=dict(mesh=n,shell=shell,h=hkl[0],k=hkl[1],l=hkl[2],
                 one_to_zero_sectors=len(loss),source_QE_k_index=a+1,
                 target_QE_k_index=b+1,source_outer_rank=1,target_outer_rank=0,
                 mu_eV=mu,finite_occupancy_gap_meV=1000*(sorted_values[count]-sorted_values[count-1]),
                 source_E5_minus_mu_eV=energies[a,0]-mu,
                 target_E5_minus_mu_eV=energies[b,0]-mu)
        for i,name in enumerate(("k1","k2","k3")):
            out["source_"+name]=k[a,i]
            out["target_"+name]=k[b,i]
        yield out


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("work",type=Path)
    args=parser.parse_args()
    rows=[]
    for n in (4,6,8,10,12):
        for folder in (args.work/"ws"/f"Rb-{n}",args.work/"mpi/ws"/f"Rb-{n}"):
            if (folder/"out/system.save"/f"wfc{n**3}.dat").exists():
                rows.extend(witnesses(folder,n))
    w=csv.DictWriter(sys.stdout,rows[0].keys(),lineterminator="\n")
    w.writeheader()
    w.writerows(rows)

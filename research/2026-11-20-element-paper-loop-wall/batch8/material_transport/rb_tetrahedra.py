"""Independent zero-width linear-tetrahedron calculation of the bcc Rb Fermi surface."""
import argparse
import csv
import gzip
from itertools import permutations
import json
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

from rb_fermi_surface import band_grid


def slice_volume(energies, level):
    """Occupied volume of each unit-volume tetrahedron and its energy derivative.

    Intersect a linear band with an isoenergy plane. Two-occupied vertices
    give a wedge cut into three tetrahedra; this form permits repeated levels.
    """
    a,b,c,d=energies.T
    volume=np.zeros(len(a))
    density=np.zeros(len(a))
    volume[level>=d]=1
    lower=(a<level)&(level<b)
    upper=(c<=level)&(level<d)
    for mask,initial,h1,h2,h3,sign in [
        (lower,a,b,c,d,1), (upper,d,c,b,a,-1)]:
        height=sign*(level-initial[mask])
        denom=np.abs((h1[mask]-initial[mask])*(h2[mask]-initial[mask])*(h3[mask]-initial[mask]))
        v=height**3/denom
        volume[mask]=v if sign==1 else 1-v
        density[mask]=3*height**2/denom
    middle=(b<=level)&(level<c)
    a,b,c,d=[x[middle] for x in (a,b,c,d)]
    ux,uy,us,ut=1/(c-a),1/(d-a),1/(c-b),1/(d-b)
    x,y,s,t=(level-a)*ux,(level-a)*uy,(level-b)*us,(level-b)*ut
    volume[middle]=x*y+s*y*(1-x)+s*t*(1-y)
    density[middle]=ux*y+x*uy+(us*y+s*uy)*(1-x)-s*y*ux+(us*t+s*ut)*(1-y)-s*t*uy
    return volume,density


def integrate(bands,b_cart,volume,signs):
    n=len(bands)
    gradient=[]
    corners=[]
    for perm in permutations((0,1,2)):
        vertex=bands
        energy=[vertex]
        slope=[None]*3
        for axis in perm:
            other=np.roll(vertex,-signs[axis],axis)
            slope[axis]=(other-vertex)*signs[axis]*n
            energy.append(other)
            vertex=other
        grad=np.linalg.solve(b_cart,np.stack(slope).reshape(3,-1)).T
        gradient.append(grad)
        corners.append(np.sort(np.stack(energy,axis=-1).reshape(-1,4),axis=1))
    energies=np.vstack(corners)
    gradient=np.vstack(gradient)
    mu=brentq(lambda e: slice_volume(energies,e)[0].mean()-.5,bands.min(),bands.max())
    v,w=slice_volume(energies,mu)
    assert np.all((v>=-1e-12)&(v<=1+1e-12)) and w.min()>-1e-12
    tensor=2*((gradient.T*w)@gradient)/len(w)
    k=np.trace(tensor)/3
    return [n,''.join('+' if i==1 else '-' for i in signs),mu,2*w.mean(),k,
            np.sqrt(180.9512818*k/volume),np.max(abs(tensor-k*np.eye(3)))/k]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('bundle',type=Path)
    p.add_argument('output',type=Path)
    args=p.parse_args()
    simple=np.array([[0.,0.,1.,1.],[0.,1.,1.,1.],[0.,0.,0.,1.]])
    v,w=slice_volume(simple,.25)
    np.testing.assert_allclose(v,[.25**2*(3-2*.25),.25**3,1-.75**3])
    np.testing.assert_allclose(w,[6*.25*.75,3*.25**2,3*.75**2])
    records=json.loads(gzip.decompress(args.bundle.read_bytes()))
    with args.output.open('w',newline='') as stream:
        writer=csv.writer(stream,lineterminator='\n')
        writer.writerow(['QE_grid','primitive_cube_diagonal','mu_eV','DOS_states_eV_cell',
                         'K_eV_A2','intraband_plasma_energy_eV','max_relative_cubic_deviation'])
        for item in records.values():
            cube,recip,volume,ef=band_grid(item)
            assert cube[:,:,:,3].max()<ef<cube[:,:,:,5].min()
            for signs in [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]:
                row=integrate(cube[:,:,:,4],recip,volume,signs)
                writer.writerow([format(i,'.10g') if isinstance(i,(float,np.floating)) else i for i in row])


if __name__=='__main__':
    main()

"""Fermi-shape-only control in a single effective scalar orbital per Rb site."""
import argparse
import csv
import gzip
import json
from itertools import product
from pathlib import Path

import numpy as np
from scipy.ndimage import map_coordinates

from rb_fermi_surface import ANG_PER_BOHR, band_grid


def evaluate(band,cell,m,offset):
    n=len(band)
    grid=np.indices((m,m,m),dtype=float)
    for i,value in enumerate(offset):
        grid[i]=(grid[i]+value)/m
    e=map_coordinates(band,grid*n,order=3,mode='grid-wrap')
    mid=e.size//2
    ordered=np.partition(e.ravel(),(mid-1,mid))
    mu=(ordered[mid-1]+ordered[mid])/2
    assert ordered[mid]-ordered[mid-1]>1e-13
    occupation=e<mu
    f=occupation.mean()
    assert f==.5
    candidates=np.array(list(product(range(-2,3),repeat=3)))
    lengths=np.linalg.norm(candidates@cell,axis=1)
    d=lengths[lengths>0].min()
    links=candidates[np.isclose(lengths,d,atol=1e-7,rtol=0)]
    assert len(links)==8
    fourier=np.fft.fftn(occupation)/occupation.size
    weights=np.array([2*abs(fourier[tuple(link%m)])**2 for link in links])
    b=2*f*(1-f)
    # All nonzero Fourier modes exhaust a site's projector budget exactly.
    total=2*np.sum(abs(fourier)**2)-2*f**2
    assert abs(total-b)<1e-12
    return [n,m,'/'.join(map(str,offset)),mu,weights.mean(),weights.min(),weights.max(),
            b,weights.sum()/b,abs(total-b)]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('bundle',type=Path)
    p.add_argument('output',type=Path)
    args=p.parse_args()
    records=json.loads(gzip.decompress(args.bundle.read_bytes()))
    with args.output.open('w',newline='') as stream:
        writer=csv.writer(stream,lineterminator='\n')
        writer.writerow(['QE_grid','quadrature_grid','fractional_offsets','median_eV','mean_X','min_X','max_X',
                         'B','nearest_shell_fraction','sum_rule_absolute_residual'])
        for item in records.values():
            cube,_,_,_=band_grid(item)
            lattice=np.array(item['cell'])*ANG_PER_BOHR
            for m in (48,72,96):
                for off in [(.137,.271,.413),(.389,.217,.079)]:
                    result=evaluate(cube[:,:,:,4],lattice,m,off)
                    writer.writerow([format(x,'.10g') if isinstance(x,(float,np.floating)) else x for x in result])


if __name__=='__main__':
    main()

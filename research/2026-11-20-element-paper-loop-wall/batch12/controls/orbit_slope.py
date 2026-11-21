"""Independent directional rank-flow slope on a triangulated cold rubidium Fermi pocket."""
import csv
import gzip
import json
import sys

import numpy as np
from scipy.ndimage import map_coordinates, spline_filter

from rank_flow import TRANSPORT, band_grid
from rank_slope import DIRECTIONS, UNIT


def sphere_grid(n, normal):
    theta = np.pi * np.arange(1,n) / n
    phi = np.pi * np.arange(2*n) / n
    u = np.cross(normal, [0,0,1])
    u /= np.linalg.norm(u)
    v = np.cross(normal,u)
    radial_plane = np.cos(phi)[:,None]*u + np.sin(phi)[:,None]*v
    rings = np.cos(theta)[:,None,None]*normal + np.sin(theta)[:,None,None]*radial_plane
    rays = np.vstack([normal, rings.reshape(-1,3), -normal])
    rows = 1 + np.arange((n-1)*2*n).reshape(n-1,2*n)
    east = np.roll(rows,-1,axis=1)
    north = np.zeros(2*n,dtype=int)
    south = np.full(2*n,len(rays)-1,dtype=int)
    tri = np.vstack([np.stack([north,rows[0],east[0]],axis=-1),
                     np.stack([rows[:-1],rows[1:],east[1:]],axis=-1).reshape(-1,3),
                     np.stack([rows[:-1],east[1:],east[:-1]],axis=-1).reshape(-1,3),
                     np.stack([rows[-1],south,east[-1]],axis=-1)])
    return rays, tri, rows[n//2-1]


def evaluate(points, tri, normal):
    a,b,c = (points[tri[:,i]] for i in range(3))
    areas = np.cross(b-a,c-a) / 2
    tetra_vol = np.sum(a*areas,axis=1)/3
    if tetra_vol.min() <= 0:
        raise AssertionError("mesh is inconsistently oriented")
    projections = areas @ normal
    plus = np.maximum(projections,0).sum()
    minus = -np.minimum(projections,0).sum()
    np.testing.assert_allclose(plus,minus,rtol=1e-10)
    return tetra_vol.sum(),plus


def radial_points(spline, k_to_bins, mu, radius, rays):
    def energy(r):
        return map_coordinates(spline, (rays @ k_to_bins * r[:,None]).T,
                               order=3, mode="grid-wrap", prefilter=False)

    lengths = np.full(len(rays),radius)
    lo,hi = energy(lengths*.90), energy(lengths*1.10)
    if lo.max() >= mu or hi.min() <= mu:
        raise AssertionError("root interval")
    step = radius*1e-4
    for _ in range(5):
        v = energy(lengths)
        deriv = (energy(lengths+step)-energy(lengths-step))/(2*step)
        if deriv.min() <= 0:
            raise AssertionError("root direction")
        lengths -= (v-mu)/deriv
    np.testing.assert_allclose(energy(lengths),mu,rtol=0,atol=2e-10)
    return rays * lengths[:,None]


def main():
    records = json.loads(gzip.decompress((TRANSPORT/'Rb_cold_band_inputs.json.gz').read_bytes()))
    with (TRANSPORT/'Rb_cold_orbits.csv').open() as f:
        mu_input = {int(r['QE_grid']):float(r['mu_eV']) for r in csv.DictReader(f)
                    if r['polar_quadrature']=='32' and r['field_direction']=='100'}
    writer = csv.writer(sys.stdout,lineterminator="\n")
    writer.writerow(("QE_mesh","polar_intervals","azimuth_intervals","direction","mu_eV",
                     "relative_mesh_volume_error","qLrank_A","central_area_over_V_A",
                     "outgoing_minus_central_over_V_A","sphere_discretization_error_A"))
    for grid, counts in ((24,(48,96)),(32,(48,96)),(40,(48,96,192))):
        cube, recip, cell_vol,_ = band_grid(records[str(grid)])
        radius = (3*np.pi**2/cell_vol)**(1/3)
        vfermi = 4*np.pi*radius**3/3
        spline = spline_filter(cube[...,4],mode="grid-wrap")
        k_to_bins = np.linalg.inv(recip) * grid
        mu = mu_input[grid]
        for n in counts:
            for label, normal in zip(DIRECTIONS,UNIT,strict=True):
                rays, tri, equator = sphere_grid(n,normal)
                pts = radial_points(spline,k_to_bins,mu,radius,rays)
                v, area = evaluate(pts,tri,normal)
                equatorial = pts[equator]
                central = (np.cross(equatorial,np.roll(equatorial,-1,axis=0))@normal).sum()/2
                _,base = evaluate(rays*radius,tri,normal)
                expected = n*np.sin(np.pi/n)*radius**2
                np.testing.assert_allclose(base,expected,rtol=1e-10)
                if area+1e-11 < central:
                    raise AssertionError("section exceeds outgoing area")
                writer.writerow((grid,n,2*n,"".join(map(str,label)),f"{mu:.10f}",
                                 f"{v/vfermi-1:.11f}",f"{area/vfermi:.10f}",f"{central/vfermi:.10f}",
                                 f"{(area-central)/vfermi:.10f}",f"{(base-np.pi*radius**2)/vfermi:.10f}"))


if __name__ == "__main__":
    main()

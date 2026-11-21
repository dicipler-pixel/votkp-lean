"""Nearest site distances for the four specified elemental Hg unit cells."""
from itertools import product
from math import cos, sin, radians, sqrt
from pathlib import Path
import csv

ROOT=Path(__file__).resolve().parent
def metric(a,b,c,alpha,beta,gamma):
    ca,cb,cg=map(lambda x:cos(radians(x)),(alpha,beta,gamma))
    def dist(p):
        x,y,z=p
        return sqrt((a*x)**2+(b*y)**2+(c*z)**2+2*(a*b*x*y*cg+a*c*x*z*cb+b*c*y*z*ca))
    return dist


def run():
    C=lambda p: tuple(v+w for v,w in zip(p,(.5,.5,0)))
    hg1=(0,0,0); hg2=(.762,0,.333); inv=tuple(-x for x in hg2)
    prim=[hg1,hg2,inv]
    data=[
      ('alpha', 'rhombohedral primitive','crystalline sample, pressure and T unspecified in CIF',
       [3.005]*3+[70.52]*3, [hg1],[0],'https://qiserver.ugr.es/cod/1538834.cif'),
      ('beta','I4/mmm','low-temperature tetragonal cell; handbook', [3.995,3.995,2.825,90,90,90],
       [hg1,(.5,.5,.5)],[0],'https://doi.org/10.1039/9781849735155'),
      ('gamma','C2/m','20.0(5) GPa at room temperature; Table II (2007)',
       [5.179,2.797,7.964,90,107.96,90],prim+[C(p) for p in prim],[0,1],'https://doi.org/10.1143/JPSJ.76.023601'),
      ('delta','P63/mmc','193 GPa room temperature, handbook',
       [2.612,2.612,4.284,90,90,120],[hg1,(2/3,1/3,.5)],[0],'https://doi.org/10.1088/2053-1591/2/1/016502')]
    output=[]
    for phase,sg,conds,cell,basis,reps,src in data:
        dist=metric(*cell)
        for i in reps:
            all_dist=[]
            for t in product(range(-2,3),repeat=3):
                for p in basis:
                    d=dist(tuple(x+y-z for x,y,z in zip(t,p,basis[i])))
                    if d>.00001:all_dist.append(round(d,6))
            lens=sorted(set(all_dist))
            output.append([phase,sg,conds,*cell,i,*lens[:2],all_dist.count(lens[0]),src])
    assert abs(output[0][10]-3.005)<1e-5 and abs(output[1][10]-2.825)<1e-5
    assert abs(output[2][10]-2.797)<1e-5 and abs(output[-1][10]-2.612)<1e-5
    with (ROOT/'mercury_cells.csv').open('w',newline='') as f:
        w=csv.writer(f,lineterminator='\n')
        w.writerow('phase space_group_or_setting conditions a_A b_A c_A alpha_deg beta_deg gamma_deg independent_site_index shortest_A second_distinct_A multiplicity_shortest source'.split());w.writerows(output)
    for r in output:print(r[0],r[9],*r[10:13])
if __name__=='__main__':run()

"""Scalar metric and neighbour audit of experimental conventional cells (Python stdlib)."""
import csv
import itertools
import math
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
ZERO = [(0,0,0)]
BCC = ZERO + [(0.5,0.5,0.5)]
FCC = ZERO + [(0,0.5,0.5),(0.5,0,0.5),(0.5,0.5,0)]
x,z = 0.1325,0.3444
PNMA = [(x,0.25,z),(0.5-x,0.75,0.5+z),(-x,0.75,-z),(0.5+x,0.25,0.5-z)]
cells = [
    ('Nb','Pnma',38,3100,(5.118,4.526,2.712),90,PNMA,'Nb20'),
    ('Nb','Pnma',50,3300,(5.021,4.513,2.681),90,PNMA,'Nb20'),
    ('Nb','bcc',38,3100,((15.852*2)**(1/3),)*3,90,BCC,'Nb20: volume'),
    ('Mo','rhombohedral',27,'room',(2.6544,)*3,109.47,ZERO,'Mo22'),
    ('Tc','tetragonal beta',0,'room',(2.829,2.829,3.990),90,BCC,'Tc21'),
    ('Tc','tetragonal beta',4.5,'room',(2.806,2.806,3.965),90,BCC,'Tc21'),
    ('Ru','fcc nanoparticle','ambient','room',(3.846,)*3,90,FCC,'Ru17: fault model'),
    ('Ru','tetragonal film','ambient','room',(3.19,3.19,3.19*0.88),90,BCC,'Ru18: substrate strain'),
]
def central(s):
    return float(re.fullmatch(r'([.\d]+)\(\d+\)',s).group(1))
rh = (HERE/'rh_s1.dat').read_text().splitlines()[1:]
assert len(rh)==47
for row in rh:
    a,v,p = map(central,row.split())
    assert abs(a**3/4-v)<0.021,(a,v,p)
    cells.append(('Rh','fcc',p,298,(a,)*3,90,FCC,'Rh24: Table S1'))

def shells(abc,angle,points,span):
    """Distances from inequivalent reference origin; listed phases each have one atomic orbit."""
    offset = points[0]
    records = []
    cos = 0 if angle==90 else math.cos(math.radians(angle))
    for vec in itertools.product(range(-span,span+1),repeat=3):
        for atom in points:
            u,v,w = (l*(atom[j]+vec[j]-offset[j]) for j,l in enumerate(abc))
            squared=u*u+v*v+w*w+2*cos*(u*v+u*w+v*w)
            if squared>1e-12:
                records.append(round(math.sqrt(squared),8))
    return sorted(set(records))[:2],records

out=[]
for element,phase,p,t,abc,angle,sites,source in cells:
    distances,values=shells(abc,angle,sites,2)
    check,extended=shells(abc,angle,sites,3)
    assert distances==check and values.count(distances[0])==extended.count(distances[0])
    a,b,c=abc
    if phase=='fcc':assert abs(distances[0]-a/math.sqrt(2))<1e-7
    if phase=='tetragonal beta':assert abs(distances[0]-min(a,c,math.sqrt(2*a*a+c*c)/2))<1e-7
    out.append((element,phase,p,t,f'{a:.6f}',f'{b:.6f}',f'{c:.6f}',angle,
                *[f'{d:.7f}' for d in distances],values.count(distances[0]),source))
with (HERE/'phase_contacts.csv').open('w') as f:
    writer=csv.writer(f,lineterminator='\n')
    writer.writerow(['element','phase','P_GPa','T_K','a_A','b_A','c_A','equal_cell_angles_deg','nearest_A','next_distinct_A','multiplicity_nearest_central_model','source'])
    writer.writerows(out)
print(len(out),'phase/condition records checked at two supercell sizes')

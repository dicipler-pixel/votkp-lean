"""Recalculate shortest distances in selected published cells. Requires gemmi and numpy."""
import csv
from itertools import product
from pathlib import Path
import gemmi
import numpy as np
# Fields: phase, pressure (GPa), space-group setting, a,b,c,beta,gamma; asymmetric
# unit coordinates, required atom count. Sources and constraints are in pressure_notes.md.
rows = [
 ('Rb-II',11.9,'Fm-3m',[5.224]*3+[90,90],[(0,0,0)],4),
 ('Rb-III',14.3,'C2221',[7.886,11.240,18.431,90,90],[(0,.0745,.25),(.1955,.3517,.2699),(.1219,.6273,.3186),(.9873,.4196,.4287),(.5805,.3931,.3871),(.3602,.6308,.4639),(.7442,.6753,.4139)],52),
 ('Rb-IV host',16.8,'I4/mcm',[10.3503,10.3503,5.1865,90,90],[(.7903,.0851,.5)],16),
 ('Rb-IV guest',16.8,'I4/mmm',[10.3503,10.3503,3.1797,90,90],[(0,0,0)],2),
 ('Rb-V',28,'I41/amd:1',[2.883,2.883,10.760,90,90],[(0,0,0)],4),
 ('Rb-VI',48.1,'Cmca',[9.372,5.550,5.528,90,90],[(0,.1704,.3177),(.2107,0,0)],16),
 ('Rb-VI',189,'Cmca',[8.282,4.920,4.9170,90,90],[(0,.180,.327),(.216,0,0)],16),
 ('Rb-VII',264,'P63/mmc',[2.5070,2.5070,8.258,90,120],[(0,0,0),(1/3,2/3,.25)],4),
 ('Sr-III',31,'I41/amd:1',[5.5629,5.5629,2.9912,90,90],[(0,0,0)],4),
 ('Sr-IV',41.7,'I 1 a 1',[5.7463,7.8013,5.5360,96.987,90],[(.30678,.16019,.64012),(.49028,.57693,.49028),(.70294,.13788,.36960)],12),
 ('Sr-V host',56,'I4/mcm',[6.958,6.958,3.959,90,90],[(.146,.646,0)],8),
 ('Y distorted-fcc hR24 model',102,'R-3m:H',[5.554,5.554,13.604,90,120],[(.521,-.521,.243),(0,0,.269)],24),
 ('Y distorted-fcc tI16 model',102,'I41/a:1',[5.524,5.524,7.926,90,90],[(.528,.219,.890)],16),
 ('Y oF16',138,'Fddd:1',[16.911,4.656,2.728,90,90],[(3/16,0,0)],16),
]
def positions(spacegroup, coords):
 ops=gemmi.find_spacegroup_by_name(spacegroup).operations()
 return np.array(sorted({tuple(np.round(np.mod(op.apply_to_xyz(v),1),9)%1) for op in ops for v in coords}))
def result(row):
 label,p,sg,values,coords,n=row
 a,b,c,beta,gamma=values
 cell=gemmi.UnitCell(a,b,c,90,beta,gamma)
 basis=np.array(cell.orth.mat).T
 pos=positions(sg,coords);assert len(pos)==n,(label,len(pos))
 # Bound integer translations rigorously using reciprocal vectors. If |r|<=R,
 # then |r_frac[j]| <= R * ||grad(f_j)||. Fractional site differences are <1.
 R=min(a,b,c)
 counts=np.ceil(1+R*np.linalg.norm(np.linalg.inv(basis),axis=0)).astype(int)
 shifts=np.array(list(product(*(range(-v,v+1) for v in counts))))
 vectors=(pos[:,None,None,:]-pos[None,:,None,:]+shifts)@basis
 d=np.linalg.norm(vectors,axis=-1); minimum=float(np.min(d[d>1e-6]))
 if label=='Rb-III':
  # The reproduced 4.1 A contact counts; see the single Rb4 discrepancy in the note.
  for v,nn in zip(coords,[10,10,8,11,11,10,11]):
   distances=np.linalg.norm((pos[:,None,:]+shifts-v)@basis,axis=-1)
   assert np.count_nonzero((distances>1e-6)&(distances<=4.1))==nn
 if label=='Sr-IV':assert abs(minimum-2.790)<.004
 if label=='Rb-VII':assert abs(minimum-2.507)<.001
 if label=='Y distorted-fcc tI16 model':
  # Ideal parameter control from Fig. 3(b): origin setting must recover fcc NN.
  ideal=positions(sg,[(.5,.25,.875)])
  fc=np.array(gemmi.UnitCell(a,a,a*2**.5,90,90,90).orth.mat).T
  dd=np.linalg.norm((ideal[:,None,None,:]-ideal[None,:,None,:]+shifts)@fc,axis=-1)
  assert abs(np.min(dd[dd>1e-6])-a/2)<1e-7
 return [label,p,sg,*values,n,f'{minimum:.5f}']
if __name__=='__main__':
 out=Path(__file__).with_name('pressure_contacts.csv')
 with out.open('w') as f:
  w=csv.writer(f,lineterminator='\n')
  w.writerow(['phase_or_component','P_GPa','space_group_setting','a_A','b_A','c_A','beta_deg','gamma_deg','cell_atoms','shortest_periodic_distance_A'])
  for row in rows:w.writerow(result(row))

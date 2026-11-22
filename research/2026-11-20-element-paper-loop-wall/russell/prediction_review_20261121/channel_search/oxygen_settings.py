"""Published oxygen inputs; rival and rounding conventions fixed before the search."""
from decimal import Decimal as D, getcontext
getcontext().prec=40
w=3+2*D(2).sqrt()
c=(D('7.576234')/D('1.30447')+D('8.15168')/D('1.3895212'))/2
i1,i2,cm=D('13.618055'),D('35.12112'),D('8065.543937')
print("ground I1/I2, exact-wall edge, registered rival edge (eV)",i1,i2,i1*w,i1*c)
for label,energy in [('triplet J0','356736.30'),('triplet J1','356844.98'),('triplet J2','357117.01'),('singlet J1','358668.90')]:
    threshold=i2+D(energy)/cm
    ratio=threshold/i1
    print(label,'threshold eV',f'{threshold:.8f}','ratio',f'{ratio:.10f}',
          'ordinary/wall difference meV',f'{1000*(threshold-i1*w):+.3f}',
          'rival difference meV',f'{1000*(threshold-i1*c):+.3f}')

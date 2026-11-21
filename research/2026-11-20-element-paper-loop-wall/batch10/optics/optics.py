"""Calculate normal-incidence semi-infinite reflectance and intensity attenuation length."""
import csv
import math
from pathlib import Path

base=Path(__file__).resolve().parent
with (base/'nk_inputs.csv').open() as src, (base/'optics.csv').open('w') as dest:
    reader=csv.DictReader(src)
    fields=[*reader.fieldnames,'R_vacuum','intensity_1_over_e_nm','matched_R']
    writer=csv.DictWriter(dest,fieldnames=fields,lineterminator='\n')
    writer.writeheader()
    for row in reader:
        n,k,wavelength=map(float,(row['n'],row['kappa'],row['vacuum_wavelength_nm']))
        N=complex(n,k)
        R=abs((1-N)/(1+N))**2
        assert abs(R-((1-n)**2+k*k)/((1+n)**2+k*k))<1e-12
        length=wavelength/(4*math.pi*k)
        assert length>0 and 0<R<1
        row.update(R_vacuum=f'{R:.6f}',intensity_1_over_e_nm=f'{length:.6f}',matched_R=abs((N-N)/(N+N))**2)
        writer.writerow(row)

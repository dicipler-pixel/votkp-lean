"""Fit observed Rb II Rydberg resonances as a channel-assignment false control.

Energy entries are the experimental column of McLaughlin and Babb MNRAS 486,
Table 3 (2019), reused from Kilbane et al., Phys. Rev. A 75, 032711 (2007).
"""
import csv
import math
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

R_INFINITY=13.605693122994
series=[(8,27.30),(9,27.50),(10,27.63),(11,27.74),(12,27.82),(13,27.89),(14,27.95)]

def fit(series):
    n,energy=np.transpose(series)
    def residual(params):
        limit, defect=params
        return limit-4*R_INFINITY/(n-defect)**2-energy
    ans=least_squares(residual,[28.2,.2],bounds=([27.5,-4],[29,4]),xtol=1e-14,gtol=1e-14,ftol=1e-14)
    return ans.x,math.sqrt(np.mean(ans.fun**2))

if __name__=='__main__':
    base=Path(__file__).parent
    rows=[]
    ground=27.28954
    upper=ground+7374.5*.00012398419843320026
    for start in (0,1,2,3):
        (limit,defect),rms=fit(series[start:])
        rows.append(dict(first_n=series[start][0],last_n=series[-1][0],number_of_lines=len(series[start:]),
            limit_eV=limit,defect=defect,rms_residual_eV=rms,minus_independent_ground_eV=limit-ground,
            minus_spectroscopic_upper_eV=limit-upper))
    with (base/'rb_channel_validation.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,rows[0].keys());writer.writeheader();writer.writerows(rows)
    print('Row with all 7 energies',rows[0])
    print('All 4 fitted limits closer to upper than lower',all(abs(row['minus_spectroscopic_upper_eV'])<abs(row['minus_independent_ground_eV']) for row in rows))

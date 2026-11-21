"""Extract an independent band classification and exact electron count from completed NC QE XML."""
import argparse
import csv
from pathlib import Path
import xml.etree.ElementTree as ET
import numpy as np


def row(save, el):
    output=ET.parse(save/'data-file-schema.xml').getroot().find('output')
    states=output.findall('band_structure/ks_energies')
    levels=np.array([np.fromstring(s.findtext('eigenvalues'),sep=' ') for s in states])*27.211386245981
    weights=np.array([float(s.find('k_point').get('weight')) for s in states]);assert np.ptp(weights)<1.e-10
    kv=len(states)
    if el=='Kr':
        val=levels[:,3]
        edge=levels[:,4].min()-val.max()
        category='insulating_gap_eV'
    else:
        # At discrete half filling the midgap around rank Nk/2 estimates the Fermi level;
        # this spacing is not an insulating band gap. Record full fifth-band dispersion.
        val=levels[:,4]
        occ=np.sort(levels[:,4:].ravel());ef=(occ[kv//2]+occ[kv//2-1])/2
        assert val.min()<ef<val.max() and levels[:,5].min()>ef and levels[:,3].max()<ef
        edge=ef
        category='ranked_mu_eV'
    return [el,kv,round(float(val.min()),8),round(float(val.max()),8),category,round(float(edge),8)]


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('work',type=Path);args=p.parse_args()
    import sys
    w=csv.writer(sys.stdout,lineterminator='\n');w.writerow(['element','Nk','upper_occupied_band_min_eV','upper_occupied_band_max_eV','quantity','value_eV'])
    for el in ('Kr','Rb'):
        for m in (4,6):
            save=args.work/'ws'/f'{el}-{m}'/'out/system.save'
            if save.exists() and 'JOB DONE.' in (save.parents[1]/'nscf.out').read_text():
                w.writerow(row(save,el))

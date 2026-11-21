"""Generate all printed rungs, interval and state checks for Z=61..65 from the pin."""
import argparse
import gzip
import hashlib
import json
import sys
from decimal import Decimal as D
from fractions import Fraction as F
from pathlib import Path

DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(DIR.parents[1] / 'batch12/ladder'))
from batch12_ladder import (
    CSV_HEADER, DETAILS, OPEN, COMPLETE, SHELLS, SCREEN, HASH, HARTREE,
    rows, save, net_loss, occupation, exact_q6, interval, side,
)


def build(archive, destination):
    if hashlib.sha256(archive.read_bytes()).hexdigest() != HASH:
        raise ValueError('Archive hash differs from the pin')
    with gzip.open(archive, 'rt') as f:
        atoms = json.load(f, parse_float=D)['records'][60:65]
    aff = {r['symbol']: r for r in rows(DIR/'affinities.csv')}
    states = {(int(r['Z']), int(r['q'])): r for r in rows(DIR/'asd_states_20261121.csv')}
    expected = {(z,q) for z in range(61,66) for q in range(z)}
    assert len(states) == len(rows(DIR/'asd_states_20261121.csv')) and set(states) == expected
    assert [r['Z'] for r in atoms] == list(range(61,66))
    ladder, detail, chem, screening, cores, diffs, ranges = [], [], [], [], [], [], []
    for atom in atoms:
        znum, symbol, thresholds = atom['Z'], atom['symbol'], atom['thresholds']
        assert [t['q'] for t in thresholds] == list(range(znum))
        configurations = [states[znum,q]['ground_shells'] for q in range(znum)] + ['']
        for q, t in enumerate(thresholds):
            source = states[znum,q]
            assert sum(occupation(configurations[q]).values()) == znum-q
            raw = source['NIST_energy_eV']
            public = (D(raw.strip('[]()')), D(source['NIST_unc_eV']) if source['NIST_unc_eV'] else None,
                      {'[':'S','(':'T'}.get(raw[0],'E'), source['NIST_refs'])
            pinned = (t['IE_eV'], t['unc_eV'], t['grade'], t['references'])
            if public != pinned:
                diffs.append([znum,symbol,q+1,*pinned,*public])
        a = aff[symbol]
        tag = a['status']
        ie1 = D(thresholds[0]['IE_eV'])
        ea = D(a['EA_eV']) if a['EA_eV'] else None
        uea = D(a['unc_eV']) if a['unc_eV'] else None
        steps = [(ea,uea,tag,a['source'])] + [
            (D(t['IE_eV']),t['unc_eV'],t['grade'],t['references']) for t in thresholds]
        for k,(x,dx,grade,ref) in enumerate(steps):
            if x is None or k == znum:
                ladder.append([znum,symbol,k,'' if x is None else x,'','',grade])
                continue
            y,dy,grade2,ref2 = steps[k+1]
            a0,b = F(x),F(y)
            z,g = b/a0,(b-a0)/(b+a0)
            wall = side(z)
            ladder.append([znum,symbol,k,x,exact_q6(z),exact_q6(g),grade])
            earlier = net_loss(configurations[k-1],configurations[k]) if k else 'detach extra electron'
            later = net_loss(configurations[k],configurations[k+1])
            core = SHELLS.get(znum-k)
            boundary = ''
            if core:
                matches = occupation(configurations[k]) == occupation(COMPLETE[core])
                boundary = core + (' closed (ASD)' if matches else ' electron count only (ASD)')
                cores.append([znum,symbol,k,znum-k,core,matches,*configurations[k-1:k+2],earlier,later,
                              exact_q6(z),exact_q6(g),wall])
            elif k == 0:
                boundary = tag+' anion'
            elif k == znum-1:
                boundary = 'He-like to H-like removal'
            ratio = y/x
            apex = (ratio.sqrt()-1)/(ratio.sqrt()+1)
            lo,hi,wall_box = interval(x,y,dx,dy)
            detail.append([znum,symbol,k,x,y,dx,dy,grade,grade2,ref,ref2,
                           *(f'{v:.10f}' for v in (ratio,(y-x)/(y+x),ratio.ln(),apex)),
                           lo,hi,wall,wall_box,earlier,later,boundary])
            if dx is not None and dy is not None:
                low = F(y-dy)/F(x+dx)
                if low <= 1:
                    high=F(y+dy)/F(x-dx)
                    ranges.append([znum,symbol,k,x,dx,y,dy,grade,grade2,ref,ref2,lo,hi,
                                   'touch' if low==1 else 'overlap', exact_q6((low-1)/(low+1)),
                                   exact_q6((high-1)/(high+1)),wall_box])
        h,he = steps[-1][0],steps[-2][0]
        s,sigma = (h-he)/(HARTREE*znum), znum-(2*he/HARTREE).sqrt()
        screening.append([znum,symbol,he,h,*(f'{v:.10f}' for v in
                         (h/he,s,sigma,s-sigma,he-HARTREE*znum*znum/2))])
        limit = ie1*(3-2*D(2).sqrt())
        value_rows = [('theory-only comparison', D(a['theory_eV']), None)]
        if ea is not None:
            value_rows.insert(0,(tag,ea,uea))
        if a['lower_bound_eV']:
            value_rows.append(('strict lower bound (boundary evaluation only)',D(a['lower_bound_eV']),None))
        for status,v,u in value_rows:
            chi,eta = (ie1+v)/2,(ie1-v)/2
            omega = chi**2/(2*eta)
            result = 'undetermined from lower bound' if status.startswith('strict') else side(F(ie1)/F(v))
            iu=steps[1][1]
            limits=(('','') if u is None or iu is None else
                    ((((ie1+iu)+(v-u))/((ie1+iu)-(v-u)))**2/2,
                     (((ie1-iu)+(v+u))/((ie1-iu)-(v+u)))**2/2))
            chem.append([znum,symbol,status,v,u,ie1,f'{limit:.9f}',exact_q6(F(ie1)/F(v)),
                         exact_q6((F(ie1)-F(v))/(F(ie1)+F(v))),eta,chi,f'{omega:.9f}',
                         f'{omega/eta:.9f}',*(f'{n:.9f}' if n!='' else n for n in limits),result])
    destination.mkdir(parents=True,exist_ok=True)
    for file,cols,data in [
        ('batch13_pm_tb.csv',CSV_HEADER,ladder),('rungs_detailed.csv',DETAILS,detail),('asg_openings.csv',OPEN,cores),
        ('screening.csv',SCREEN,screening),
        ('affinity_chemistry.csv','Z,symbol,scope,input_EA_eV,input_unc_eV,IE1_eV,critical_EA_eV,z0,Gamma0,eta_eV,chi_eV,omega_eV,omega_over_eta,omega_over_eta_lower,omega_over_eta_upper,wall'.split(','),chem),
        ('direction_limits.csv','Z,symbol,k,IE_k,unc_k,IE_next,unc_next,grade_k,grade_next,ref_k,ref_next,z_lower,z_upper,direction,Gamma_lower,Gamma_upper,box_wall'.split(','),ranges),
        ('asd_differences.csv','Z,symbol,k,pin_energy,pin_unc,pin_grade,pin_refs,live_energy,live_unc,live_grade,live_refs'.split(','),diffs)]:
        save(destination/file,cols,data)


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive',type=Path)
    parser.add_argument('--out',type=Path,default=DIR)
    args=parser.parse_args()
    build(args.archive,args.out)

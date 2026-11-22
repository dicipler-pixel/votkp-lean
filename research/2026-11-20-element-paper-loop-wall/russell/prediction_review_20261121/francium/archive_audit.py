"""Audit francium comparisons and leave-one-out controls against a pinned archive."""
import argparse
import csv
import gzip
import hashlib
import json
import math
from pathlib import Path

ARCHIVE_SHA = '75e67478d9a22ef85fa2d3f6ac36ad2860c6f8f62215127c558438a2cb53f62c'
WALL = 3 + 2 * math.sqrt(2)
RIVAL = 5.8372204179655185


def write_csv(path, rows):
    with path.open('w', newline='') as fp:
        w = csv.DictWriter(fp, rows[0].keys())
        w.writeheader()
        w.writerows(rows)


def main():
    args = argparse.ArgumentParser()
    args.add_argument('thresholds', type=Path)
    args.add_argument('--out', type=Path, default=Path(__file__).parent)
    opts = args.parse_args()
    digest = hashlib.sha256(opts.thresholds.read_bytes()).hexdigest()
    if digest != ARCHIVE_SHA:
        raise SystemExit(f'Archive SHA mismatch: {digest}')
    records = {r['Z']: r for r in json.load(gzip.open(opts.thresholds))['records']}
    def entry(z, q):
        return next(t for t in records[z]['thresholds'] if t['q'] == q)
    def energy(z, q):
        return entry(z, q)['IE_eV']
    def ratio(z):
        return energy(z, 1) / energy(z, 0)
    fr = energy(87, 0)
    print('archive_sha256', digest)
    print('disagreement_eV', fr*WALL, fr*RIVAL, 'width_eV', fr*(RIVAL-WALL))
    ul = entry(87,0)['unc_eV']
    print('strict_max_admissible_symmetric_IE2_halfwidth_eV', ((fr-ul)*RIVAL - (fr+ul)*WALL)/2)
    family=[3,11,19,37,55,87]
    forecasts=[]
    for a,b,c in zip(family,family[1:],family[2:]):
        pred=2*ratio(b)-ratio(a)
        e=entry(c,1)
        forecasts.append(dict(input_a=records[a]['symbol'],input_b=records[b]['symbol'],
            target=records[c]['symbol'],predicted_ratio=pred,predicted_IE2_eV=pred*energy(c,0),
            actual_IE2_eV=e['IE_eV'],actual_grade=e['grade'],ratio_archive=ratio(c),
            error_ratio=pred-ratio(c),error_eV=pred*energy(c,0)-e['IE_eV']))
    write_csv(opts.out/'continuation.csv',forecasts)
    # Match de Farias' Na–Cs regression using the pinned modern thresholds.
    pairs=[(energy(z,0),energy(z,1)) for z in (11,19,37,55)]
    avg_x=sum(x for x,y in pairs)/len(pairs); avg_y=sum(y for x,y in pairs)/len(pairs)
    slope=sum((x-avg_x)*(y-avg_y) for x,y in pairs)/sum((x-avg_x)**2 for x,y in pairs)
    intercept=avg_y-slope*avg_x
    print('Na–Cs IE2-on-IE1 regression slope, intercept, Fr',slope,intercept,slope*fr+intercept)
    t=(fr-energy(55,0))/(energy(37,0)-energy(55,0))
    print('Rb/Cs linear interpolation on neutral IE1, fraction, Fr eV',t,energy(55,1)+t*(energy(37,1)-energy(55,1)))
    rows=[]
    for n in (2,10,18,36,54,86):
        a,b,c,d = [entry(n+j,j) for j in range(4)]
        midpoint=(a['IE_eV']+c['IE_eV'])/2
        quadratic=(a['IE_eV']-d['IE_eV'])/3+c['IE_eV']
        rows.append(dict(sequence=records[n]['symbol'],target=records[n+1]['symbol']+'+',
            energy_left=a['IE_eV'],energy_right=c['IE_eV'],energy_right2=d['IE_eV'],
            grades_left_right_right2=''.join(x['grade'] for x in (a,c,d)),
            withheld=b['IE_eV'],withheld_grade=b['grade'],linear=midpoint,
            linear_error=midpoint-b['IE_eV'],quadratic=quadratic,quadratic_error=quadratic-b['IE_eV']))
    write_csv(opts.out/'noble_core_controls.csv',rows)
    chain=[]
    for z in range(86,119):
        t=next((t for t in records[z]['thresholds'] if t['q'] == z-86),
               dict(IE_eV=None,unc_eV=None,grade='missing',references=''))
        chain.append(dict(Z=z,element=records[z]['symbol'],ion_charge=z-86,
            IE_eV=t['IE_eV'],unc_eV=t['unc_eV'],grade=t['grade'],source=t['references']))
    write_csv(opts.out/'radonlike.csv',chain)
    source_values=[('Frozen period-index secant',forecasts[-1]['predicted_IE2_eV']),
        ('ASD semiempirical central',energy(87,1)),('van der Schoor X2C (2016)',20.673),
        ('van der Schoor nonrelativistic (2016)',21.765),('Sigman–Rives ANN (as cited in 2016 Table 4)',20.02),
        ('de Farias Mendeleev Commun. (2018)',23.80),('de Farias Chem. Res. J. (2018)',26.10)]
    prior=[]
    for source,v in source_values:
        z=v/fr
        prior.append(dict(source=source,IE2_eV=v,z_with_observed_IE1=z,
            Gamma=(z-1)/(z+1),margin_wall_eV=v-fr*WALL,margin_rival_eV=v-fr*RIVAL))
    write_csv(opts.out/'model_comparisons.csv',prior)
    log_ie2=math.log(20.673/21.765)
    log_ie1=-math.log(4.052/3.582)
    print('Groningen self-consistent ratios (NR, X2C)',21.765/3.582,20.673/4.052)
    print('mixed ratios (numerator only, denominator only)',20.673/3.582,21.765/4.052)
    print('log contributions (IE2, -IE1, denominator fraction of log shift)',log_ie2,log_ie1,log_ie1/(log_ie1+log_ie2))
    for row in rows:
        print('leave_alkali_out',row['target'],row['withheld_grade'],round(row['linear'],5),round(row['quadratic'],5))

if __name__ == '__main__':
    main()

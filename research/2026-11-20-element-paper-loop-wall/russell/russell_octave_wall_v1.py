# SCRIPT: RUSSELL-OCTAVE-WALL-01
# Russell's octave tones laid against the loop wall. Tones: 1+,2+,3+ generative, 4 apex (carbon family),
# 3-,2-,1- radiative, inert gas at the octave boundary (his helium octave is lithium to fluorine).
# For each main-group element: anion-rung reflection Gamma0 = (IE-EA)/(IE+EA) (hardness over
# electronegativity) and side of the wall; for each 1+/1-, 2+/2-, 3+/3- mate pair, the donor-to-acceptor
# reflection (IE_donor - EA_acceptor)/(IE_donor + EA_acceptor).
import gzip, json, sys, math
d = json.load(gzip.open(sys.argv[1])); rec = {r['Z']: r for r in d['records']}
IE1 = lambda Z: {x['q']: x['IE_eV'] for x in rec[Z]['thresholds']}[0]
EA = {3:0.618049,4:None,5:0.279723,6:1.2621226,7:None,8:1.4611136,9:3.4011898,
      11:0.547926,12:None,13:0.43283,14:1.3895212,15:0.746609,16:2.0771042,17:3.612725,
      19:0.501459,20:0.02455,31:0.301166,32:1.2326764,33:0.804486,34:2.020667,35:3.363588,
      37:0.485916,38:0.05206,49:0.38392,50:1.112070,51:1.047401,52:1.970875,53:3.0590465,
      55:0.471626,56:0.14462,81:0.320053,82:0.356721,83:0.942362,84:None,85:2.41578}
octaves = [('helium octave', [3,4,5,6,7,8,9]), ('neon octave', [11,12,13,14,15,16,17]),
           ('argon octave (main group)', [19,20,31,32,33,34,35]), ('krypton octave (main group)', [37,38,49,50,51,52,53]),
           ('xenon octave (main group)', [55,56,81,82,83,84,85])]
tones = ['1+','2+','3+','4 apex','3-','2-','1-']
W2 = 0.5
for name, Zs in octaves:
    print('==', name)
    for t, Z in zip(tones, Zs):
        a = EA[Z]
        if a is None: print(f'  {t:7s} {rec[Z]["name"]:11s} no bound anion'); continue
        g = (IE1(Z)-a)/(IE1(Z)+a)
        print(f'  {t:7s} {rec[Z]["name"]:11s} IE/EA {IE1(Z)/a:8.3f}  Gamma0 {g:.4f}  {"outside" if g*g > W2 else "inside"}')
    for k, (i, j) in enumerate([(0,6),(1,5),(2,4)]):
        Zd, Za = Zs[i], Zs[j]
        if EA[Za] is None: print(f'  mates {tones[i]}/{tones[j]} {rec[Zd]["name"]}-{rec[Za]["name"]}: acceptor has no bound anion'); continue
        z = IE1(Zd)/EA[Za]; g = (z-1)/(z+1)
        print(f'  mates {tones[i]}/{tones[j]} {rec[Zd]["name"]} gives to {rec[Za]["name"]}: IE/EA {z:.3f} Gamma {g:.4f} {"outside" if g*g > W2 else "inside"}')

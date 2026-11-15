archive/neutrinos/ledger_test/ledger_burst.py

\# SCRIPT: LEDGER-BURST ledger written by each probe burst on the fully coupled base (kinetic model): \# L_b = S_base(e_end) - S_burst(e_end), e_end = 1.25 eps_b \* 1.02 (just after collisions have erased the hidden moments) import json from ledger import \* C = 1e4; out = {} for eb in (0.25, 0.5, 1, 1.5, 2, 3, 4, 6):

tg = np.array(\[eb, 1.25\*eb, 1.25\*eb\*1.02, 14.0\]) S0 = S_curve({'base': \['const', C\]}, tg); Sb = S_curve({'base': \['const', C\], 'windows': \[\[eb, 1.25\*eb, 0.0\]\]}, tg) out\['%g' % eb\] = dict(Lb=float(S0\[2\]-Sb\[2\]), Lb_at14=float(S0\[3\]-Sb\[3\]), S_before=float(S0\[0\])) print(eb, out\['%g' % eb\], flush=True) tg = np.array(\[1.25\*1.02, 3.75\*1.02, 14.0\]) S0 = S_curve({'base': \['const', C\]}, tg); Sb = S_curve({'base': \['const', C\], 'windows': \[\[1, 1.25, 0.0\], \[3, 3.75, 0.0\]\]}, tg) out\['1+3'\] = dict(Lb=float(S0\[1\]-Sb\[1\]), L_first=float(S0\[0\]-Sb\[0\])) print('1+3', out\['1+3'\]) json.dump(out, open('ledger_burst.json', 'w'), indent=1)



# SCRIPT: MATTER-DISK-S12  the distance of an unbound nucleus outside the rim, as an exact identity
# WHY THIS CHECK PROVES WHAT IT CLAIMS
# VOTKP 15.4 observes that the distance outside the rim is "close to twice the decay energy over the
# neighbouring step". With z = S_next/S_first, S_first = -s < 0 and a = S_next/s > 1:
# Gamma = (z-1)/(z+1) = (a+1)/(a-1), so |Gamma| - 1 = 2/(a-1) = 2s/(S_next - s) exactly; for s << S_next
# this is 2s/S_next, the author's "twice the decay energy over the neighbouring step".
# z = -1 (the Cayley pole) is S_next = -S_first, i.e. S_first + S_next = 0.
# KILL (written before the run): the identity misses by more than 1e-12 on any of the three gap nuclei,
# using the NUBASE2020 separation energies printed by the author's own script (s10).
rows=[('5He',-734.8,20577.6,1.074),('5Li',-1966.1,19813.9,1.220),('8Be',-91.8,7366.6,1.025)]
ok=True
for k,s1,s2,printed in rows:
    z=s2/s1; G=abs((z-1)/(z+1)); s=-s1
    ident=2*s/(s2-s); approx=2*s/s2
    ok&=abs((G-1)-ident)<1e-12
    print(f'{k}: |Gamma|={G:.6f} (VOTKP {printed})  |Gamma|-1={G-1:.6f}  2s/(S_next-s)={ident:.6f}  2s/S_next={approx:.6f}')
print('VERDICT:','exact identity holds' if ok else 'KILLED')

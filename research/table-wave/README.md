# Is the periodic table a wave? Russell's octave against the data (24 Nov 2026)

Author: Jeromie Beasley

Data: first ionization energies for Z = 1 to 85 from the peel periodic table's own file
(`ptable_data.json`, branch element-paper/loop-wall). Kill lines were written in each script before its run.

`table_wave.py` (TABLE-WAVE-01), one smooth wave:
- Russell's fixed octave (wavelength 8 in Z) explains 0.537 of the variance on Z = 3 to 20. Held (line was one half).
- The same octave explains 0.048 on Z = 21 to 85. Held: it breaks where the long periods begin.
- Cube-root coordinate (6Z)^(1/3): best single wave 0.206 against 0.146 for plain Z. Held, narrowly.
- Against shuffled data the 0.206 is below the 99th percentile (0.211). KILL FIRED: one smooth wave failed this way.

`table_wave2.py` (TABLE-WAVE-02), a ramp built from three harmonics:
- Cube-root coordinate, one wave per period: 0.226 against a 99th percentile of 0.249. KILL FIRED.
- Sorted by the true periods, three harmonics: 0.526 (line was 0.6). KILL FIRED. Five harmonics reach 0.627.
- Cube-root coordinate, one wave per PAIR of periods: 0.352 at wavelength 2.151. Held against the one-period wave.
  Noise line run afterwards (02B): 99th percentile 0.261, none of 500 shuffles reached 0.352.
- Russell's octave read as valence (+1 +2 +3 4 -3 -2 -1 0) matches the usual valences of periods 2 and 3: 16 of 16.

Reading: the table repeats, but not as one smooth wave and not with one shape per period. The unit that passes the noise
line is the pair of periods, in the cube-root coordinate. Russell's octave is right as a valence wave for two periods
and for nothing after them.

Other properties (radius, electron affinity, polarizability, electronegativity, melting point) are tested in the section below.
The peel-step Gamma: best single wave in plain Z was 0.207 at wavelength 2.60, with no noise line run for it; in the cube-root
coordinate it was below the shuffle median. No wave was established for it.

## The rest of the properties (`table_wave3.py`, TABLE-WAVE-03)

Data: mendeleev 1.4.0, Z = 1 to 86 (2018 Schwerdtfeger-Nagle polarizabilities, Pyykko covalent radii, electron affinity,
Pauling electronegativity, melting point). Kill lines and a prediction were written in the file before the run.
A second control was added: the pair wave must also beat two neighbouring wavelength bands, which a smooth drift would not.

| property | elements | octave, Z 3-20 | octave, Z 21-86 | one per period (99% line) | one per PAIR (99% line) | pair wavelength | true periods, 3 harmonics |
|---|---|---|---|---|---|---|---|
| log first ionization energy | 86 | 0.537 | 0.042 | 0.215 (0.252) | 0.365 (0.241) | 2.16 | 0.494 |
| Pauling electronegativity | 77 | 0.783 | 0.073 | 0.347 (0.299) | 0.467 (0.270) | 2.13 | 0.592 |
| log covalent radius | 86 | 0.631 | 0.041 | 0.237 (0.239) | 0.469 (0.249) | 2.06 | 0.435 |
| log dipole polarizability | 86 | 0.584 | 0.026 | 0.316 (0.251) | 0.541 (0.251) | 2.13 | 0.637 |
| electron affinity | 73 | 0.090 | 0.152 | 0.175 (0.247) | 0.163 (0.244) | 2.53 | 0.093 |
| log melting point | 80 | 0.804 | 0.033 | 0.441 (0.278) | 0.599 (0.235) | 2.13 | 0.548 |

Outcome: five of six properties pass all three kill lines. Electron affinity fails all three, as predicted.
Melting point was predicted likely to fail and instead carries the strongest pair wave: that prediction was wrong.
Four of the five passing properties put the pair wave at 2.13 to 2.16 in the cube-root coordinate; radius at 2.06.
Russell's octave behaves the same way for all five: more than half the variance on Z = 3 to 20, under 8 percent beyond.
The ionization-energy row from this second data source agrees with the first run (0.537, 0.365 against 0.537, 0.352).

Not tested: Z above 86; densities; whether the pair wave's shape (not only its wavelength) is shared between properties.

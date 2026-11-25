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

Not tested: other properties (radius, electron affinity, polarizability); the peel-step Gamma showed no wave here.

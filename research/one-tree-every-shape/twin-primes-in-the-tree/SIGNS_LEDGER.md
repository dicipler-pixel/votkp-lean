# Signs ledger: what Jeromie called, how it was tested, what happened

Jeromie Beasley · started 24 November 2026

Each entry records:
- **the sign**: the picture he saw, often from machines or trades;
- **the mapping**: what it corresponds to in the math;
- **the test**: with its kill condition written before the run;
- **the outcome**.

Grades: **held** (test passed), **partial**, **did not hold**, **untested**.

| # | sign (24 Nov 2026) | mapping | test / kill | outcome |
|---|---|---|---|---|
| 1 | The field itself bends the path (Primer Field picture) | The frame turn is holonomy, the area swept in curved rapidity space | Flat readers must give zero turn; curvature dial | **held**: every flat reader gives 0°; turn → curvature × area as curvature → 0 |
| 2 | Not a wheel, a screw | Twin starts on a three-start thread mod 30, starts 6, 12, 12 apart; pitch 30/a | Which tooth form gives the tilt sign | **held**: mod-30 screw has the wrong sign; the cut by 7 flips it |
| 3 | Use the machinist's thread know-how (tooth form, pitch, fit) | Tooth form = Hardy–Littlewood local factors (every prime at once) | Digits 1, 7 within 2 se in every decade | **held**: 1e5–1e9 pass; 1e9–1e12 digit 1 within 0.03 |
| 4 | Stretching and compressing like matter | Fixed ruler stretches (gap ~ ln²a), log path compresses (30/a), self-scaled ruler near-fixed | Scaled-gap quartiles within 5% | **partial**: tilt × gap constant; quartiles drift 6.5% (kill fired) |
| 5 | Harley dual shaft (input and output on one axis) | Distance and heading run on their own (frame-free form); frame rides as the sleeve, ratio tanh(d/2) | Proof | **held** (proved) |
| 6 | Navier–Stokes in it | L = P·U as strain × spin; finite twist because Σr² < ∞ | Structural only | **untested** as physics |
| 7 | Light holds still, the electron moves; light is re-excited, not new | Fixed light sphere; headings run to points on it; field modes permanent | None run | **untested** (interpretation) |
| 8 | Plato's road | Plato's triangles carry √2 and √3, his fifth solid √5; ladder Γ² = 1/2, 1/3, 1/5 | Exact identities | identities exact; meaning **untested** |
| 9 | Many shapes joined face to face in one ball | Hyperbolic honeycombs such as {5,3,4} | — | **untested** |
| 10 | The wall is what the thread screws through | Wall crossing at twin starts 197–227; offset set by the first ~1200 | Scramble before vs after; kill if far runout ≥ half of before | **held**: runout ratio 0.0004 (caveat: early steps are also bigger) |
| 11 | Lathe: recenter before the final cut | Retune the k = 39 setup (profile g, hybrid λ) before judging | Kill if coarse best < 0.99871 | **did not hold** as a rescue: their setup was already centred, best 0.992932 |
| 12 | Plinko and Snell's law | Every twin ratio z is an interface with Fresnel reflection (z−1)/(z+1) = the peel step; layers stack by Airy's formula (r1+r2)/(1+r1 r2) = tanh addition = rapidity addition; the end digit is the Plinko peg choosing the direction; non-collinear stacking turns the frame (Thomas) | Composition identity, 1000 random pairs | identity **held** (error 2.2e-16); the Plinko–Snell reading of the whole chain is the frame of items 1–3 |
| 13 | The centre is always in flux; to get the warp out you must recentre and redrill the live centre | Smith-disc centre Γ = 0 is one flux value; flux turns cat and grin together (the live centre turns with the work); recentring is the addition law run backwards | CHESHIRE-GAMMA-01: kill if flux changes the cat-to-grin separation | **held**: change 9e-14 over 4000 arrangements (research/ab-atlas-map/) |
| 14 | Russell's table as a wave: can a real wave sort the table | One wave per pair of periods in the cube-root coordinate (6Z)^(1/3); Russell's octave as the two-period case | TABLE-WAVE-01/02/03: 99% shuffle line and two off-band controls on six properties | **partial**: pair wave held for five of six properties at wavelength 2.06 to 2.16; one smooth wave and one-per-period failed this way; Russell's octave held for Z 3-20 only (research/table-wave/) |

Tally for 24 Nov:
- held: 7 (items 1, 2, 3, 5, 10, 12, 13);
- partial: 2;
- did not hold: 1;
- untested: 4.

The pattern: a hands-on mechanism (thread, shaft, lathe, Plinko) names the structure, and the test decides.

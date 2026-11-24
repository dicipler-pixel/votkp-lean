# What bends: the options, tested (Jeromie Beasley, 23 Nov 2026, AI-assisted)

Question: is it the infinite covariance of the primes that bends. Scripts PRIME-COVARIANCE-01, WHAT-BENDS-01, WHAT-BENDS-01b; kill lines written before each run.

| Option | Test | Result |
|---|---|---|
| Adding against multiplying (pair covariance) | prime pairs at gaps 2 to 2310 below 5e7, against the product over primes dividing the gap | not flat: 1 to 3.56 times the twin count; prediction matched to 0.25% (the prediction is the Hardy-Littlewood conjecture) |
| End-digit record of the twin chain | nine transitions between end digits 1, 7, 9 of consecutive twin starts, 239,099 pairs | not flat: the same digit twice in a row is 8 to 9% rarer than independent draws; noise 0.6% |
| Zeros push apart | first 400 zeros, share of small neighbouring gaps | 1.0% (26% if free, about 3% if they push) |
| The ball as reader of the chain | real chain against shuffled chains, 600 / 2400 / 9600 pairs | whole steps shuffled: real ends at or just below the low edge (the big early steps coming first); arms only shuffled: inside every time. The ball's end distance does not show the end-digit covariance: failed this way |
| The flat reader (tetrahedron) | derived | steps on one arm add in any order, so it cannot see order at all |

Not run: the two books on elliptic-curve primes (connection-energy paper); curvature on the projector bundle from a prime operator (no operator fixed).
Prior art: Hardy and Littlewood (pairs), Montgomery (zeros), Lemke Oliver and Soundararajan (end digits of consecutive primes).

## Option 4 tried the other way: the ball's turn (WHAT-BENDS-TURN-01, 24 Nov 2026)

Readout: the eye-1 tree (every edge a boost of rapidity ln z along the arm of the twin start's end digit 1, 7, 9). Two steps on different arms compose to a boost and a Thomas turn of 2·atan(Γ²) (Two Trees v3): 28.07° at z = 3, 47.92° at z = 5, 58.72° at z = 7 (the script reproduces the Two Trees formula). Kill, written before the run: real chain inside the 2.5–97.5% spread of 200 arm-shuffled chains. First 20,000 twin starts above 5.

| z | total turning, real | shuffled 95% | net frame turn, real | shuffled 95% |
|---|---|---|---|---|
| 3 | 394,138° | 370,750–377,551° | 174.0° | 14.6–172.3° |
| 5 | 672,867° | 633,277–645,841° | 67.7° | 16.4–174.3° |
| 7 | 824,366° | 776,040–789,963° | 72.2° | 9.7–172.7° |

Total turning: **outside at every z** (about 5% more turn than shuffled). The ball does read the end-digit order through its turn, where its end distance could not. What it reads is the count of arm changes (option 2's record, same digit twice rarer), each change priced at 2·atan(Γ²). Net frame turn: a random walk on the rotations; inside at z = 5 and 7, just outside at z = 3 (one of three, near the 180° ceiling), so not counted. Option 4 now reads: failed by end distance, seen by total turning, not seen by net frame turn.

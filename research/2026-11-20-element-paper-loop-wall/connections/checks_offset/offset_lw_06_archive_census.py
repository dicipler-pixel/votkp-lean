# SCRIPT: OFFSET-LW-06
# The element archive read with the offset paper's level dictionary and census window.
#
# WHY THIS CHECK PROVES WHAT IT CLAIMS
#   Reproduction gate: the element paper states 3,570 ordinary steps from hydrogen to astatine with exactly 8
#   outside the wall (lithium, beryllium, boron, carbon, sodium, potassium, rubidium, caesium).  Recounting
#   from data/element_thresholds_20261011.json.gz with the wall written without sqrt 2 ((z - 3)^2 > 8, z > 3)
#   confirms that the archive and the definitions are being read the same way before anything is added.
#   Dictionary (E2 run backwards): give each peel step the "occupation" nu = 1/(1 + z), so that
#   Gamma = 1 - 2 nu and eps = ln z, exactly the offset paper's level relations (v31 Eq. 7, 12).  The loop wall
#   is then the offset paper's exact occupation window (v31 Eq. 100) at floor nu_w = (2 - sqrt 2)/4, i.e.
#   l_eps = ln[(1 - nu_w)/nu_w] = ln(3 + 2 sqrt 2).  This is algebra; the run lists the 8 outside steps in both
#   languages.  S1: the half-log rapidities of one atom telescope to (1/2) ln(IE_last/IE_first): the sum
#   belongs to the two ends of the ladder (checked on the archive to rounding).
#   LEAD L1 (exploratory, not a claim): weight each step by the fermionic entropy s(eps) of v31 Sec 7.9 and see
#   how much of each atom's total the outside steps carry.  Reported as numbers only.
import gzip, json, math, sys

path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/votkp-lean/data/element_thresholds_20261011.json.gz'
d = json.load(gzip.open(path))
recs = sorted(d['records'], key=lambda r: r['Z'])


def outside(z):
    return z > 3 and (z - 3) ** 2 > 8


def s(x):
    x = abs(x)
    return math.log1p(math.exp(-x)) + x / (1 + math.exp(x))


nu_w = (2 - math.sqrt(2)) / 4
print('wall: z_w = %.12f ; nu_w = %.12f ; ln[(1-nu_w)/nu_w] = %.12f ; ln z_w = %.12f'
      % (3 + 2 * math.sqrt(2), nu_w, math.log((1 - nu_w) / nu_w), math.log(3 + 2 * math.sqrt(2))))
n_steps = 0
outs = []
tele_worst = 0.0
S_out = 0.0
S_tot = 0.0
for r in recs:
    if r['Z'] > 85:
        continue
    th = sorted(r['thresholds'], key=lambda t: t['q'])
    ie = [t['IE_eV'] for t in th]
    hs = []
    for kq in range(len(ie) - 1):
        z = ie[kq + 1] / ie[kq]
        n_steps += 1
        hs.append(0.5 * math.log(z))
        eps = math.log(z)
        S_tot += s(eps)
        if outside(z):
            outs.append((r['name'], kq + 1, z))
            S_out += s(eps)
    if len(ie) > 1:
        tele_worst = max(tele_worst, abs(sum(hs) - 0.5 * math.log(ie[-1] / ie[0])))
print('ordinary steps Z = 1..85:', n_steps, ' outside:', len(outs))
for name, step, z in outs:
    nu = 1 / (1 + z)
    G = (z - 1) / (z + 1)
    print('  %-10s step %d  z=%.6f  Gamma^2=%.6f  nu=1/(1+z)=%.6f  nu(1-nu)=%.6f (wall 0.125)  eps=ln z=%.6f'
          % (name, step, z, G * G, nu, nu * (1 - nu), math.log(z)))
print('telescoping: max |sum_k h_k - (1/2) ln(IE_last/IE_first)| over atoms = %.1e' % tele_worst)
print('LEAD L1 (exploratory): entropy weight s(ln z) carried by the 8 outside steps: %.4f of %.4f (%.4f%%)'
      % (S_out, S_tot, 100 * S_out / S_tot))

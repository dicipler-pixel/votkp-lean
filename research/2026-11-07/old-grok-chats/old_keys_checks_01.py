# SCRIPT: OLD-KEYS-CHECKS-01
# Checks of the old Grok-chat material (FNTP_DCSASS, Kyber, TOE summary) and of the 3-6-9 bubble ladder.
# Keep / drop criteria were written BEFORE the runs:
#  A1 coil      : circular if E stays within a factor 2 for every input tried while the inputs vary over x100 each.
#  A2 FNRC      : a "crack" must take key or ciphertext as input; if the function has neither, it measures nothing.
#  B1 Goldbach  : keep the Hardy-Littlewood count if actual/predicted -> 1 (within 5% by n ~ 1e6, integral form).
#  B2 torus     : keep if every torus root turn equals -k^2/(pq) mod 1 for an integer k.
#  B3 circle    : exploratory. Hardy-Littlewood predict |f| near a/q scales like |mu(q)|/phi(q); report the
#                 prime generating function at each torus-root point and say where it peaks or vanishes.
#  C1 zeta      : keep winding-counting if the argument-principle count equals the number of zeros found directly.
#  C2 Schumann  : decay + direction holds if measured < ideal lossless modes and the ratio is near-constant.
#  C3 ln 2      : report |0.694 - ln 2|.
#  D  Kyber     : real ML-KEM-512 sizes, decaps round trip, 17 a primitive 256th root of unity mod 3329.
#  E  Cl(4,1)   : keep if the sandwich by the unit-sphere vector maps every embedded point x to x/|x|^2.
import math, numpy as np, mpmath as mp, sympy as sp
np.random.seed(1)
out = []
def say(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

# ---------- A1: the old coil, run as written ----------
def scalar_toroid_su3(freq=7.83, turns=100, radius=0.1, power=10, P_avg=0.242620):
    B = (4e-7 * turns * power) / (2 * radius)
    n = int(np.log(1e4 / (6.626e-34 * freq * P_avg)) / np.log(2))
    energy = 1e-34 * freq * P_avg * 2**n
    return B, energy
say('A1 coil: energy for varied inputs')
Es = []
for f in (0.783, 7.83, 78.3):
    for P in (0.0242620, 0.242620, 2.4262):
        for pw in (1, 10, 100):
            B, E = scalar_toroid_su3(freq=f, power=pw, P_avg=P); Es.append(E)
say('   min E = %.3e J, max E = %.3e J over 27 input sets (freq x100, P x100, power x100)' % (min(Es), max(Es)))
say('   spread max/min = %.2f while the input product varied by 10^6' % (max(Es)/min(Es)))
say('   ->', 'CIRCULAR: n is solved for the target, so E is pinned near 1e4/6.626 J whatever the inputs' if max(Es)/min(Es) < 2 else 'not pinned')

# ---------- A2: FNRC 'crack' ----------
import inspect
def fnrc_5d_spinor(t, u, freq=14.13, memory_steps=10):
    S = t + u
    psi = np.exp(1j * 2 * np.pi * freq * t * np.arange(memory_steps))
    for d in range(5):
        S += 0.1 * np.cos(2 * np.pi * freq * t) * (psi[d % memory_steps].real) * (1 if d < 4 else -1)
    return S
say('A2 FNRC inputs:', list(inspect.signature(fnrc_5d_spinor).parameters), '-> no key, ciphertext or lattice enters')

# ---------- B1: Goldbach counts vs Hardy-Littlewood ----------
N = 2_000_000
sieve = np.ones(N + 1, bool); sieve[:2] = False
for i in range(2, int(N**0.5) + 1):
    if sieve[i]: sieve[i*i::i] = False
primes = np.nonzero(sieve)[0]
C2 = 1.0
for p in primes[1:]: C2 *= 1 - 1.0 / (p - 1)**2
say('B1 twin-prime constant C2 (product over odd p < %d): %.9f  (old chat used 0.660161815)' % (primes[-1], C2))
def r2(n):  # ordered representations n = p + q
    ps = primes[primes < n]; return int(np.count_nonzero(sieve[n - ps]))
def HL(n):
    corr = 1.0
    for p in sp.primefactors(n):
        if p > 2: corr *= (p - 1) / (p - 2)
    integral = float(mp.quad(lambda t: 1 / (mp.log(t) * mp.log(n - t)), [2, n / 2, n - 2]))  # sharper main term: integral of dt/(ln t ln(n-t))
    simple = n / math.log(n)**2
    return 2 * C2 * corr * simple, 2 * C2 * corr * integral
for n in (10_000, 100_000, 1_000_000, 1_999_998):
    a = r2(n); s, i = HL(n)
    say('   n=%9d  actual r(n)=%7d   HL simple %9.0f (ratio %.3f)   HL integral %9.0f (ratio %.3f)' % (n, a, s, a / s, i, a / i))

# ---------- B2: torus turns as quadratic phases ----------
T = {'3_1': (2, 3, [5/6]), '5_1': (2, 5, [1/10, 9/10]), '7_1': (2, 7, [3/14, 5/14, 13/14]),
     '8_19': (3, 4, [11/12]), '10_124': (3, 5, [14/15])}
say('B2 torus turns vs -k^2/(pq) mod 1')
allok = True
for nm, (p, q, ts) in T.items():
    for t in ts:
        ks = [k for k in range(1, p * q) if abs(((-k * k) % (p * q)) / (p * q) - t) < 1e-12]
        allok &= bool(ks); say('   %-6s turn %-8s = -k^2/%d for k in %s' % (nm, sp.nsimplify(t), p * q, ks))
say('   ->', 'ALL quadratic phases' if allok else 'NOT all')

# ---------- B3: prime generating function at the torus-root points ----------
say('B3 Hardy-Littlewood f(x) = sum ln p x^p on radius R = e^(-1/n), n = 2e5, at x = R e^(2 pi i a/q)')
n0 = 200_000; R = math.exp(-1 / n0)
ps = primes[primes < 40 * n0].astype(float); w = np.log(ps) * R**ps
def fabs(frac): return abs(np.sum(w * np.exp(2j * np.pi * frac * ps)))
f0 = fabs(0.0)
for nm, (p, q, ts) in T.items():
    for t in ts:
        fr = sp.nsimplify(t); qq = fr.q
        pred = abs(int(sp.mobius(qq))) / int(sp.totient(qq))
        say('   %-6s a/q = %-6s  |f|/|f(1)| = %.4f   HL major-arc prediction |mu(q)|/phi(q) = %.4f' % (nm, fr, fabs(t) / f0, pred))

# ---------- C1: counting zeta zeros by winding ----------
mp.mp.dps = 20
def N_wind(Tm):  # Riemann-von Mangoldt via the phase of the completed function: N(T) = theta(T)/pi + 1 + S(T)
    return mp.siegeltheta(Tm) / mp.pi + 1 + mp.arg(mp.zeta(mp.mpf(1)/2 + 1j * Tm)) / mp.pi
zeros = [mp.zetazero(k).imag for k in range(1, 31)]
say('C1 first three zeros:', ', '.join('%.6f' % float(z) for z in zeros[:3]))
for Tm in (20, 30, 50, 100):
    say('   T=%4d  winding count N(T) = %.3f   zeros found directly below T = %d' % (Tm, float(N_wind(Tm)), sum(1 for z in zeros if z < Tm) if Tm <= float(zeros[-1]) else int(mp.nzeros(Tm))))

# ---------- C2: Schumann ----------
c = 2.99792458e8; a = 6.371e6
meas = [7.83, 14.3, 20.8, 27.3, 33.8]   # standard measured Schumann peaks (Hz)
say('C2 Schumann: ideal lossless f_n = c/(2 pi a) sqrt(n(n+1)) vs measured')
for k, fm in enumerate(meas, 1):
    fi = c / (2 * math.pi * a) * math.sqrt(k * (k + 1))
    say('   n=%d  ideal %.2f Hz  measured %.1f Hz  ratio %.3f' % (k, fi, fm, fm / fi))

# ---------- C3 ----------
say('C3 |0.694 - ln 2| = %.5f  (ln 2 = %.5f)' % (abs(0.694 - math.log(2)), math.log(2)))

# ---------- D: Kyber / ML-KEM-512 ----------
from kyber_py.ml_kem import ML_KEM_512
ek, dk = ML_KEM_512.keygen(); K, ct = ML_KEM_512.encaps(ek); K2 = ML_KEM_512.decaps(dk, ct)
say('D  ML-KEM-512 sizes: public key %d B, secret key %d B, ciphertext %d B, shared secret %d B; decaps round trip %s'
    % (len(ek), len(dk), len(ct), len(K), K == K2))
say('   ciphertext = 2*256*10/8 + 256*4/8 = %d B;  Grok layout 2*256*12/8 + 256*9/8 = %d B' % (2*256*10//8 + 256*4//8, 2*256*12//8 + 256*9//8))
q3 = 3329; say('   3329 - 1 = %s;  order of 17 mod 3329 = %d' % (sp.factorint(q3 - 1), sp.n_order(17, q3)))

# ---------- E: Cl(4,1) conformal inversion ----------
# basis e1,e2,e3,e+,e- with squares +,+,+,+,-; blades as bitmasks
sig = [1, 1, 1, 1, -1]
def bmul(a, b):
    s = 1; x = a >> 1
    while x:
        s *= (-1) ** bin(x & b).count('1'); x >>= 1
    m = a & b; i = 0
    while m:
        if m & 1: s *= sig[i]
        m >>= 1; i += 1
    return s, a ^ b
def gmul(A, B):
    C = {}
    for ba, va in A.items():
        for bb, vb in B.items():
            s, bc = bmul(ba, bb); C[bc] = C.get(bc, 0) + s * va * vb
    return {k: v for k, v in C.items() if abs(v) > 1e-12}
def vec(c): return {1 << i: c[i] for i in range(5) if c[i] != 0}
ep, em = np.eye(5)[3], np.eye(5)[4]; einf = ep + em; e0 = 0.5 * (em - ep)
def up(x): x = np.asarray(x, float); return np.r_[x, 0, 0] + 0.5 * x.dot(x) * einf + e0
def down(X):
    v = np.array([X.get(1 << i, 0) for i in range(5)]); x = v[:3]
    lam = -(v[3] * einf[3] - v[4] * einf[4])  # -X.einf with metric diag(+,+,+,+,-)
    return x / lam
S = vec(e0 - 0.5 * einf)   # the unit sphere as a vector
worst = 0
for _ in range(200):
    x = np.random.randn(3) * np.random.choice([0.3, 1, 3])
    Y = gmul(gmul(S, vec(up(x))), S)
    y = down(Y); worst = max(worst, np.linalg.norm(y - x / x.dot(x)))
say('E  Cl(4,1): sandwich S X S of 200 random points vs x/|x|^2: worst error %.2e' % worst)
open('/home/claude/oldkeys/old_keys_checks_01_output.txt', 'w').write('\n'.join(out) + '\n')

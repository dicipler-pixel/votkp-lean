#!/usr/bin/env python3
# SCRIPT: MEMORY-ENGINE-02
"""How fast can memory make electricity? The same coherent-feedback engine as MEMORY-ENGINE-01, now in time.

One qubit (gap w) refills from its bath at rate gamma: its excited share relaxes as p(t) = p_th + (p0 - p_th) e^(-gamma t),
p_th = 1/(1 + e^(w/T)). A fresh record (P(1) = m = 0) arrives every dt; the swap |e0> <-> |g1> sends w * p to the load
and leaves the qubit in its ground state (excited share = m = 0). So in steady state, every record finds
        p = p_th (1 - e^(-gamma dt)),     work per record W = w p,     power P = W / dt.
Two ceilings, both checked below:
  memory ceiling   P <= kT ln2 / dt                      (each record can give at most kT ln2)
  refill ceiling   P <= gamma w p_th <= 0.2785 gamma kT   (heat cannot come in faster than the bath refills the qubit)
Checks (why they prove it): the steady state formula is compared with a direct step-by-step run of the cycle (the run
does not use the formula); every row is checked against both ceilings and against the second law W <= T dH(record)."""
import math
kB = 1.380649e-23

def pth(x): return 1 / (1 + math.exp(x))
def H(p): return 0 if p <= 0 or p >= 1 else -p * math.log(p) - (1 - p) * math.log(1 - p)

def steady(x, gdt):
    p = pth(x) * (1 - math.exp(-gdt)); return x * p, p          # W/T, p  (T = 1)

def run(x, gdt, n=400):
    p = 0.0; W = []                                             # start cold; step the cycle n times
    for _ in range(n):
        p = pth(x) + (p - pth(x)) * math.exp(-gdt)              # refill for dt
        W.append(x * p); p = 0.0                                # swap with a fresh record: qubit left at m = 0
    return W[-1]

x_best = max((x / 10000 for x in range(1, 60000)), key=lambda x: x * pth(x))
print(f'best gap for power: w = {x_best:.4f} kT, refill ceiling 0.2785 -> exact {x_best * pth(x_best):.6f} gamma kT')
print('\nA. power against the record rate (gap w = 1.278 kT), in units of gamma kT; the stepped run vs the formula')
print('   records per refill time   W per record (kT)   power (gamma kT)   memory ceiling   refill ceiling   share of kT ln2 used   2nd law')
for r in [0.01, 0.1, 0.3, 1, 3, 10, 30, 100]:
    gdt = 1 / r; W, p = steady(x_best, gdt); Wrun = run(x_best, gdt); P = W * r
    mem = math.log(2) * r; ref = x_best * pth(x_best)
    ok = abs(W - Wrun) < 1e-12 and P <= mem + 1e-12 and P <= ref + 1e-12 and W <= H(p) + 1e-12
    print(f'   {r:8.2f}                    {W:.6f}            {P:.6f}           {mem:10.4f}      {ref:.4f}          {W / math.log(2):6.1%}               {ok}')
print('\nB. where the two ceilings cross (memory-limited below, refill-limited above): r* =', f'{x_best * pth(x_best) / math.log(2):.4f}', 'records per refill time')

print('\nC. what sets the speed: the bath refill rate gamma. Real numbers, one qubit, w = 1.278 kT:')
for lab, T, g in [('transmon at 0.2 K, refill 1 MHz', 0.2, 1e6), ('transmon at 0.2 K, refill 10 MHz (tunable bath)', 0.2, 1e7),
                  ('room temperature, refill 1 GHz', 300, 1e9)]:
    P = 0.2785 * g * kB * T; print(f'   {lab:48s}: up to {P:.2e} W per qubit')
print('   (for scale, the Aalto autonomous engine emits about 5e-18 W)')

print('\nD. faster AND fuller: a pipeline of K qubits, each record walks down the ladder (MEMORY-ENGINE-01 B) while a new')
print('   record enters every dt; each qubit refills between records. Work per record and power, gamma dt = 3:')
def pipeline(K, gdt, n=300):
    qs = [0.0] * K; xs = []
    for k in range(1, K + 1):
        t = 0.5 * k / K; xs.append(math.log((1 - t) / t) if t < 0.5 else 0.0)
    Wtot = 0
    for it in range(n):
        for i in range(K): qs[i] = pth(xs[i]) + (qs[i] - pth(xs[i])) * math.exp(-gdt)
        m = 0.0; W = 0.0
        for i in range(K):
            p = qs[i]; W += xs[i] * (p - m)                        # swap e0 <-> g1: work w (p - m)
            qs[i], m = m, p                                        # qubit takes the record's old P(1); record takes p
        Wtot = W
    return Wtot, m
for K in [1, 2, 4, 8, 16, 64]:
    W, m = pipeline(K, 3.0); print(f'   K = {K:3d}: W per record = {W:.4f} kT ({W / math.log(2):5.1%} of ln2), power = {W / 3.0:.4f} gamma kT, record leaves at P(1) = {m:.3f}')

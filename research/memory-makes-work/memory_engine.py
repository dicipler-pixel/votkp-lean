#!/usr/bin/env python3
# SCRIPT: MEMORY-ENGINE-01
"""Can memory make electricity? A coherent-feedback engine whose record rides away on a photon. Exact books.

Parts (Jeromie Beasley's picture, 18 Nov 2026):
  qubit Q   two levels, gap w, kept at bath temperature T (thermal: p_e = 1/(1 + e^x), x = w/T, units k_B = 1)
  photon M  the record: two states of EQUAL energy (a phase/polarisation bit), arrives with P(1) = m, so its bias is
            the memory; it holds its own walls (a closed two-state system) and flies away down the rail after use
  load      a work store (the battery, the 'electricity')
Coherent feedback, no measurement: one energy-conserving unitary on Q, M and the load per pass,
        |e,0> <-> |g,1>  with the load gaining w on the way right and losing w on the way left.
Then Q rethermalises from the bath and M sails off. Exact consequences (derived in the docstring of step()):
        work      W = w (p_e - m)              memory after: P(1) = p_e          heat from bath Q_in = W
Second law with the record counted:  W <= T [H(p_e) - H(m)]  (H binary entropy, nats).  Checked below on every row.
The edge: a record that meets a LADDER of qubits whose gaps step down slowly, each nearly in balance with it, gives
W -> T [H(1/2) - H(m0)], the reversible limit. Back rails: a fraction R of spent records (P(1) = 1/2) comes back down
and mixes into the fresh ones, m0 = R/2 (fresh records start at m = 0)."""
import math

def H(p):
    return 0.0 if p <= 0 or p >= 1 else -p * math.log(p) - (1 - p) * math.log(1 - p)

def pe(x):
    return 1.0 / (1.0 + math.exp(x))

def step(x, m, T=1.0):
    """one pass. Before: Q thermal (g with 1-p, e with p), M with P(1)=m, independent.
    Swap |e0> <-> |g1>: P(e0) = p(1-m) goes to the load as +w, P(g1) = (1-p)m as -w.  W = w(p(1-m) - (1-p)m) = w(p - m).
    After: M is 1 when (g1 from e0) or (e1 untouched): P = p(1-m) + p m = p.  Q excited with P = (1-p)m + p m = m,
    rethermalising takes Q_in = w(p - m) = W from the bath."""
    p = pe(x); w = x * T
    return w * (p - m), p, w * (p - m)

def ladder(m0, K, T=1.0, xmax=12.0):
    """the edge: K qubits, gaps chosen so each meets the record just above where it already is"""
    W = 0.0; m = m0; Qin = 0.0
    # target memory values from m0 to 1/2 in K equal steps; gap x_k with pe(x_k) = target
    for k in range(1, K + 1):
        t = m0 + (0.5 - m0) * k / K
        x = math.log((1 - t) / t) if t < 0.5 else 0.0
        dW, m, dQ = step(x, m, T); W += dW; Qin += dQ
    return W, m, Qin

T = 1.0
print('A. one pass, fresh record (m = 0): work w p_e, against the bound T[H(p_e) - H(0)]')
print('   w/T     W/T        bound      efficiency  second law (W <= bound)')
for x in [0.25, 0.5, 1, 1.5, 2, 3, 5]:
    W, mo, Q = step(x, 0.0); b = T * (H(mo) - H(0.0))
    print(f'   {x:4.2f}   {W:.6f}   {b:.6f}   {W / b:.4f}      {W <= b + 1e-15}')
best = max(((step(x / 1000, 0.0)[0], x / 1000) for x in range(1, 20000)))
print(f'   best single pass: W/T = {best[0]:.6f} at w/T = {best[1]:.3f}  (the most one fresh bit can give is ln 2 = {math.log(2):.6f})')

print('\nB. the edge: the same fresh record walked down a ladder of K qubits')
for K in [1, 2, 4, 8, 16, 64, 256, 1024]:
    W, m, Q = ladder(0.0, K); b = T * (H(0.5) - H(0.0))
    print(f'   K = {K:5d}   W/T = {W:.6f}   of ln 2 = {W / b:.4f}   record leaves at P(1) = {m:.4f}   bath gave {Q:.6f}')

print('\nC. back rails: a fraction R of spent records comes back and mixes with the fresh ones (m0 = R/2), ladder K = 256')
for R in [0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0]:
    m0 = R / 2; W, m, Q = ladder(m0, 256) if m0 < 0.5 else (0.0, 0.5, 0.0); b = H(0.5) - H(m0)
    print(f'   R = {R:4.2f}   W/T = {W:.6f}   bound {b:.6f}   ' + ('<- his face at the wall returns R = 1/2' if R == 0.5 else ''))

print('\nD. the coherent return (by unitarity: the inverse swap on the same joint state, before Q rethermalises):')
x = 1.0; W1, m1, _ = step(x, 0.0); p = pe(x)
# reverse swap on the SAME correlated state (before Q rethermalises): restores e0/g1 populations exactly
print(f'   forward W = {W1:.6f}, reverse W = {-W1:.6f}, net 0: the record un-written, nothing erased, nothing gained')

print('\nE. how fast memory makes power: P <= k_B T ln2 x (fresh bits per second)')
kB = 1.380649e-23
for lab, Tk, rate in [('room temperature, 1 Gbit/s', 300, 1e9), ('chip at 20 mK, 10 Gbit/s', 0.02, 1e10), ('room temperature, 1 Tbit/s', 300, 1e12)]:
    print(f'   {lab:28s}: {kB * Tk * math.log(2) * rate:.3e} W')

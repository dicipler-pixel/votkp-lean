#!/usr/bin/env python3
# SCRIPT: SURGE-ORBIT-01
"""Ferranti, the matched line, and a self-regulating pair.
1. A lossless line, length l, phase constant beta (50 Hz: wavelength 6000 km). Sending voltage 1. Receiving voltage with
   load Z_L = z Z0:  V_R = 1 / (cos(beta l) + j sin(beta l)/z). Open end (z -> inf): V_R = 1/cos(beta l) = the Ferranti rise.
   Voltage along the line, and the reactive balance: the line's capacitance (charge build-up) makes Q_C = w C V^2 per length,
   its inductance (current, momentum) absorbs Q_L = w L I^2; they cancel everywhere exactly when z = 1 (surge impedance load).
2. His face on the line: the end reflects Gamma = (z - 1)/(z + 1); at his wall z = 3 + 2 sqrt2 it returns Gamma^2 = 1/2 of the power.
3. A linear balance is neutral (any amplitude stays); self-regulation needs gain that saturates. Van der Pol pair:
   x'' - mu (1 - x^2) x' + x = 0: the surge (negative damping at small x) and the orbit (damping at large x) settle every start
   on one amplitude, 2."""
import numpy as np, cmath, math
lam = 6000.0
for L in [300, 500, 800, 1000, 1400]:
    b = 2 * math.pi * L / lam
    print(f'line {L:5d} km: Ferranti rise at the open end 1/cos(beta l) = {1 / math.cos(b):.4f}' + ('   (beyond a quarter wave: resonance)' if b >= math.pi / 2 else ''))
print('\n500 km line, receiving-end voltage against load z = Z_L/Z0, and the largest voltage along the line:')
b = 2 * math.pi * 500 / lam
for z in [1e9, 4, 3 + 2 * math.sqrt(2), 2, 1, 0.5]:
    VR = 1 / (math.cos(b) + 1j * math.sin(b) / z)
    xs = np.linspace(0, 500, 501); bx = 2 * math.pi * xs / lam            # distance from the receiving end
    I_R = VR / z
    V = [abs(VR * math.cos(t) + 1j * I_R * math.sin(t)) for t in (b - bx)]
    I = [abs(I_R * math.cos(t) + 1j * VR * math.sin(t)) for t in (b - bx)]
    imb = max(abs(v * v - i * i) for v, i in zip(V, I))
    G = (z - 1) / (z + 1)
    print(f'   z = {z:10.4g}: |V_R| = {abs(VR):.4f}, max |V| = {max(V):.4f}, min |V| = {min(V):.4f}, charge-vs-momentum imbalance max|V^2 - I^2| = {imb:.4f}, reflected power Gamma^2 = {G * G:.4f}')
print('\nvan der Pol pair, mu = 1: final amplitude from different starts (surge plus orbit)')
def vdp(x0, mu=1.0, T=200, h=0.001):
    x, v = x0, 0.0; amp = 0
    for k in range(int(T / h)):
        a = mu * (1 - x * x) * v - x
        v += h * a; x += h * v
        if k * h > T - 20: amp = max(amp, abs(x))
    return amp
for x0 in [0.001, 0.1, 1.0, 3.0, 6.0]:
    print(f'   start {x0:6.3f} -> amplitude {vdp(x0):.4f}')
print('   linear lossless oscillator (no surge, no orbit damping), analytic: energy is conserved, so every start keeps its own amplitude (neutral, no regulation)')

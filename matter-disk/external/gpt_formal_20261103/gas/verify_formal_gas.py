#!/usr/bin/env python3
"""Prospective finite-model controls for G1–G9 and R1–R4.

Analytic proofs are in the companion notes. Exact-arithmetic checks and
floating-point implementation controls are explicitly distinguished below.
No observations are generated or fitted here.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import math

import numpy as np
from scipy.constants import h, m_e, k, electron_volt
from scipy.linalg import expm
from scipy.optimize import brentq
from scipy.special import logsumexp

HERE = Path(__file__).resolve().parent
SEED = 20261103
rng = np.random.default_rng(SEED)
checks = {}


def solve(log_s, density):
    log_s = np.asarray(log_s, dtype=float)
    z = len(log_s)
    charges = np.arange(z + 1, dtype=float)
    log_a = np.r_[0.0, np.cumsum(log_s)]
    def state(y):
        lp = log_a - charges * y
        lp -= logsumexp(lp)
        p = np.exp(lp)
        mean = float(p @ charges)
        variance = float(p @ ((charges - mean) ** 2))
        return lp, p, mean, variance
    def residual(y):
        mean = state(y)[2]
        return y - math.log(density) - math.log(mean)
    y = brentq(residual, math.log(density) - 500.0,
               math.log(z * density), xtol=5e-14,
               rtol=4*np.finfo(float).eps)
    lp, p, mean, variance = state(y)
    return dict(log_x=y, x=math.exp(y), p=p, lp=lp, mean=mean,
                variance=variance, q=charges,
                neutrality=abs(math.exp(y)/density-mean),
                normalization=abs(float(p.sum())-1.0))


def cov(state, values):
    return float(state['p'] @ ((state['q']-state['mean']) * values))


def poly_mul(a, b):
    out = [F(0)] * (len(a)+len(b)-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += ai*bj
    return out


# G1: exact rational reconstruction, no tolerances.
for _ in range(100):
    size = int(rng.integers(1, 9))
    ladder = [F(int(rng.integers(1, 40)), int(rng.integers(1, 20))) for _ in range(size)]
    gamma = [(b-a)/(b+a) for a, b in zip(ladder, ladder[1:])]
    reconstructed = [ladder[0]]
    for g in gamma:
        reconstructed.append(reconstructed[-1]*(1+g)/(1-g))
    assert reconstructed == ladder
    scaled = [F(7, 3)*a for a in ladder]
    assert gamma == [(b-a)/(b+a) for a, b in zip(scaled, scaled[1:])]
checks['G1_exact_rational_roundtrip_and_scale_100'] = True

# G3: exact positive polynomial root manufactured at x=1.
manufactured_errors = []
for z in range(1, 9):
    s = [F(q+2, q+1) for q in range(z)]
    a = [F(1)]
    for sq in s:
        a.append(a[-1]*sq)
    mean = sum(F(q)*aq for q, aq in enumerate(a))/sum(a)
    density = 1/mean
    polynomial_at_one = sum(a)-density*sum(F(q)*aq for q, aq in enumerate(a))
    assert polynomial_at_one == 0
    solution = solve(np.log([float(v) for v in s]), float(density))
    manufactured_errors.append(abs(solution['x']-1.0))
checks['G3_exact_manufactured_neutrality_polynomials_8'] = max(manufactured_errors) < 1e-11

# G3–G7: random finite charge systems and their sensitivity controls.
step = 1e-5
density_errors = []
coefficient_errors = []
scale_errors = []
neutrality_errors = []
normalization_errors = []
density_signs = []
coefficient_signs = []
tail_signs = []
for _ in range(64):
    z = int(rng.integers(1, 9))
    logs = rng.uniform(-1.5, 1.5, z)
    density = math.exp(float(rng.uniform(-1, 1)))
    base = solve(logs, density)
    m, v = base['mean'], base['variance']
    minus = solve(logs, density*math.exp(-step))
    plus = solve(logs, density*math.exp(step))
    observed = (plus['log_x']-minus['log_x'])/(2*step)
    density_errors.append(abs(observed-m/(m+v)))
    den_up = solve(logs, density*1.01)
    density_signs.append(den_up['x'] > base['x'] and den_up['mean'] < m)
    tail_signs.extend(float(den_up['p'][r:].sum()) < float(base['p'][r:].sum())
                      for r in range(1, z+1))
    r = int(rng.integers(0, z))
    indicator = (base['q'] > r).astype(float)
    derivative = cov(base, indicator)/(m+v)
    lm, lp = logs.copy(), logs.copy()
    lm[r] -= step
    lp[r] += step
    observed = (solve(lp, density)['log_x']-solve(lm, density)['log_x'])/(2*step)
    coefficient_errors.append(abs(observed-derivative))
    up = logs.copy()
    up[r] += math.log(1.01)
    coefficient_signs.append(solve(up, density)['mean'] > m)
    for factor in (0.1, 0.5, 2.0, 10.0):
        scaled = solve(logs+math.log(factor), density*factor)
        scale_errors.append(float(np.max(abs(scaled['p']-base['p']))))
    coefficient_signs.append(solve(logs+math.log(1.01), density)['mean'] > m)
    neutrality_errors.append(base['neutrality'])
    normalization_errors.append(base['normalization'])
checks['G3_neutrality_and_normalization_64'] = max(neutrality_errors+normalization_errors) < 1e-11
checks['G4_density_elasticity'] = max(density_errors) < 2e-7
checks['G4_density_stochastic_order'] = all(density_signs+tail_signs)
checks['G5_single_coefficient_response'] = max(coefficient_errors) < 2e-7 and all(coefficient_signs)
checks['G7_coefficient_density_scale_covariance'] = max(scale_errors) < 1e-11

# G6: dimensionless fixed-partition temperature responses (k_B=1).
temperature_errors = []
temperature_signs = []
dictionary_errors = []
for _ in range(32):
    z = int(rng.integers(1, 9))
    thresholds = rng.uniform(0.2, 8, z)
    partitions = np.exp(rng.uniform(-0.5, 0.5, z+1))
    temperature = math.exp(float(rng.uniform(-0.5, 2)))
    density = math.exp(float(rng.uniform(-1, 1)))
    def logs_at(t, energies=thresholds, mass=1.0):
        return math.log(2)+1.5*math.log(mass*t)+np.diff(np.log(partitions))-energies/t
    base = solve(logs_at(temperature), density)
    cumulative = np.r_[0.0, np.cumsum(thresholds)]
    hv = 1.5*base['q']+cumulative/temperature
    predicted = cov(base, hv)/(base['mean']+base['variance'])
    observed = (solve(logs_at(temperature*math.exp(step)), density)['log_x']-
                solve(logs_at(temperature*math.exp(-step)), density)['log_x'])/(2*step)
    temperature_errors.append(abs(observed-predicted))
    temperature_signs.append(solve(logs_at(1.01*temperature), density)['mean'] > base['mean'])
    for factor in (0.5, 2.0):
        fixed_mass = solve(logs_at(factor*temperature, factor*thresholds), factor**1.5*density)
        changed_mass = solve(logs_at(factor*temperature, factor*thresholds, factor), factor**3*density)
        dictionary_errors.extend([float(np.max(abs(fixed_mass['p']-base['p']))),
                                  float(np.max(abs(changed_mass['p']-base['p'])))])
checks['G6_fixed_partition_temperature_response'] = max(temperature_errors) < 2e-7 and all(temperature_signs)
checks['G7_both_physical_scaling_dictionaries'] = max(dictionary_errors) < 1e-11

# R3: exact spectral moment and rational-resolvent checks.
energies = [F(-3), F(-1), F(1), F(3)]
weights = [[F(1, 4)]*4, [F(v, 16) for v in (3, 7, 1, 5)]]
moments = [[sum(w*e**r for w, e in zip(ws, energies)) for r in range(4)] for ws in weights]
assert moments == [[F(1), F(0), F(5), F(0)], [F(1), F(0), F(5), F(3)]]
denominator = [F(1)]
for e in energies:
    denominator = poly_mul(denominator, [-e, F(1)])
numerators = []
for ws in weights:
    num = [F(0)]*4
    for j, w in enumerate(ws):
        prod = [F(1)]
        for kidx, e in enumerate(energies):
            if kidx != j:
                prod = poly_mul(prod, [-e, F(1)])
        num = [a+w*b for a, b in zip(num, prod)]
    numerators.append(num)
assert denominator == [F(9), F(0), F(-10), F(0), F(1)]
assert numerators == [[F(0), F(-5), F(0), F(1)], [F(3), F(-5), F(0), F(1)]]
checks['R3_exact_moments_and_resolvent_polynomials'] = True
hamiltonian_errors = []
survival = []
third_hidden_moments = []
matrix_records = []
for ws in weights:
    s = np.sqrt(np.array([float(v) for v in ws]))
    e0 = np.array([1.0, 0.0, 0.0, 0.0])
    v = e0-s
    r = np.eye(4)-np.outer(v, v)/(1-s[0])
    hh = r @ np.diag([float(e) for e in energies]) @ r.T
    coupling, hidden = hh[0, 1:], hh[1:, 1:]
    hamiltonian_errors.extend([float(np.linalg.norm(r.T@r-np.eye(4))),
                               float(np.max(abs(np.linalg.eigvalsh(hh)-np.array(energies, dtype=float)))),
                               abs(hh[0, 0]), abs(float(coupling@coupling)-5)])
    survival.append(float(abs(expm(-1j*hh*math.pi/4)[0, 0])**2))
    third_hidden_moments.append(float(coupling@hidden@coupling))
    matrix_records.append(hh.tolist())
checks['R3_constructive_equal_spectrum_equal_footprint'] = max(hamiltonian_errors) < 2e-12
checks['R3_later_survival_0_versus_1_over_32'] = max(abs(survival[0]), abs(survival[1]-1/32)) < 2e-12
checks['R3_hidden_first_channel_moment_0_versus_3'] = max(abs(third_hidden_moments[0]), abs(third_hidden_moments[1]-3)) < 2e-12

# R4: the same kernel requires the hidden-source record as well.
hh = np.array([[0.0, 1.0], [1.0, 0.0]])
uu = expm(-1j*hh*math.pi/4)
source_survival = [float(abs((uu@np.array([1, sign*1j])/math.sqrt(2))[0])**2)
                   for sign in (1, -1)]
checks['R4_same_kernel_different_hidden_source'] = max(abs(source_survival[0]-1), abs(source_survival[1])) < 2e-12

# G8–G9: actual §8 helium values, followed by a synthetic partition opposite.
helium_i = np.array([24.587389011, 54.4177655282])
true_gamma = float(np.diff(helium_i)[0]/helium_i.sum())


def combinations(temperature, density, threshold, partitions, physical=False):
    z = len(threshold)
    if physical:
        beta = electron_volt/(k*temperature)
        log_lam3 = 3*math.log(h)-1.5*math.log(2*math.pi*m_e*k*temperature)
    else:
        beta = 1/temperature
        log_lam3 = -1.5*math.log(temperature)
    lu = np.log(partitions)
    logs = math.log(2)-log_lam3+np.diff(lu)-beta*threshold
    st = solve(logs, density)
    lp = st['lp']
    ld = lp[:-2]+lp[2:]-2*lp[1:-1]
    lb = lp[0]-lp[-1]-z*(st['log_x']+log_lam3)
    gd = lu[:-2]+lu[2:]-2*lu[1:-1]
    gb = lu[0]-lu[-1]-z*math.log(2)
    return dict(beta=beta, ld=ld, lb=lb, gd=gd, gb=gb)


def invert(pair, corrected):
    aa, bb = pair
    db = bb['beta']-aa['beta']
    dd = -((bb['ld']-(bb['gd'] if corrected else 0))-
           (aa['ld']-(aa['gd'] if corrected else 0)))/db
    total = ((bb['lb']-(bb['gb'] if corrected else 0))-
             (aa['lb']-(aa['gb'] if corrected else 0)))/db
    z = len(dd)+1
    i0 = (total-sum((z-1-r)*value for r, value in enumerate(dd)))/z
    ladder = np.r_[i0, i0+np.cumsum(dd)]
    gamma = np.diff(ladder)/(ladder[1:]+ladder[:-1])
    return ladder, gamma, dd, total


helium_records = []
for density in (1e18, 1e20, 1e22, 1e24, 1e26):
    for excited in (False, True):
        pair = []
        for temperature in (30000.0, 32000.0):
            middle = 2+4*math.exp(-10*electron_volt/(k*temperature)) if excited else 2
            pair.append(combinations(temperature, density, helium_i,
                                     np.array([1.0, middle, 1.0]), physical=True))
        naive = invert(pair, False)
        corrected = invert(pair, True)
        helium_records.append(dict(density_m3=density, synthetic_excited_partition=excited,
                                   naive_gamma=float(naive[1][0]), corrected_gamma=float(corrected[1][0]),
                                   naive_difference_eV=float(naive[2][0]), naive_sum_eV=float(naive[3]),
                                   naive_gamma_bias=float(naive[1][0]-true_gamma),
                                   corrected_gamma_error=float(abs(corrected[1][0]-true_gamma))))
fixed = [r for r in helium_records if not r['synthetic_excited_partition']]
excited = [r for r in helium_records if r['synthetic_excited_partition']]
checks['G8_incoming_section8_fixed_partition_inverse'] = max(abs(r['naive_gamma_bias']) for r in fixed) < 1e-10
checks['G9_excited_partition_naive_slope_false_control'] = min(abs(r['naive_gamma_bias']) for r in excited) > 1e-3
checks['G9_known_partition_correction_restores_inverse'] = max(r['corrected_gamma_error'] for r in excited) < 1e-10

general_inverse_errors = []
for _ in range(16):
    z = int(rng.integers(2, 9))
    threshold = rng.uniform(0.5, 4, z)
    partitions = np.exp(rng.uniform(-0.5, 0.5, z+1))
    pair = [combinations(t, math.exp(float(rng.uniform(-1, 1))), threshold, partitions)
            for t in (1.3, 2.7)]
    recovered = invert(pair, False)[0]
    general_inverse_errors.append(float(np.max(abs(recovered-threshold))))
checks['G8_general_ladder_inverse_16_with_changed_density'] = max(general_inverse_errors) < 1e-9

result = {
    'status': 'PASS' if all(checks.values()) else 'FAIL',
    'scope': 'Analytic theorem implementation controls and synthetic counterexamples; no new experimental observations',
    'seed': SEED,
    'protocol_sha256': hashlib.sha256((HERE/'PREREGISTERED_FORMAL_CONTROLS.md').read_bytes()).hexdigest(),
    'inverse_addendum_sha256': hashlib.sha256((HERE/'PREREGISTRATION_ADDENDUM_GAS_PEEL.md').read_bytes()).hexdigest(),
    'checks': {name: bool(value) for name, value in checks.items()},
    'max_errors': {
        'manufactured_root': max(manufactured_errors), 'charge_neutrality': max(neutrality_errors),
        'normalization': max(normalization_errors), 'density_elasticity_finite_difference': max(density_errors),
        'coefficient_elasticity_finite_difference': max(coefficient_errors),
        'temperature_elasticity_finite_difference': max(temperature_errors),
        'coefficient_density_scaling': max(scale_errors), 'physical_scaling_dictionaries': max(dictionary_errors),
        'hamiltonian_structure': max(hamiltonian_errors), 'general_inverse_thresholds': max(general_inverse_errors)},
    'spectral_witness': {'energies': [-3,-1,1,3], 'weights': [[str(x) for x in w] for w in weights],
        'moments_orders_0_to_3': [[str(x) for x in row] for row in moments],
        'resolvent_denominator_ascending': [str(x) for x in denominator],
        'resolvent_numerators_ascending': [[str(x) for x in row] for row in numerators],
        'hamiltonians_numerical_evaluations_of_exact_householder_formula': matrix_records,
        'time': math.pi/4, 'survival_probabilities': survival,
        'hidden_first_channel_moments': third_hidden_moments},
    'same_kernel_hidden_source_survival': source_survival,
    'gas_peel_inverse': {'helium_thresholds_eV': helium_i.tolist(), 'input_grades': ['E','T'],
                         'input_gamma': true_gamma, 'synthetic_partition_rule': 'U=(1,2+4 exp(-10 eV/kT),1)',
                         'records': helium_records},
}
(HERE/'formal_gas_results.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
assert all(checks.values()), checks

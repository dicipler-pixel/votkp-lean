# SCRIPT: s14_v4_coverage
# Merge check: every numbered result, figure and script of the sources must appear in v4.
# Each manifest row is (source, item, a distinctive string that only that item's content carries).
# KILL: any row missing from the v4 source text. A missing row is a compression and must be restored.
import glob, re, sys
tex = ''.join(open(f).read() for f in sorted(glob.glob('../paper/v4/*.tex')))
flat = re.sub(r'\s+', ' ', tex)
M = [
 # v3 (matter_then_on_down_v3): body results, appendix items, data rows
 ('v3', 'zero and span', r'K\mapsto cK'), ('v3', 'census formula eq', r'|\partial A|\,\frac{c}{\pi^2}'),
 ('v3', 'c=1 coefficient', '0.202692'), ('v3', 'Ising 41.8x', '41.8'), ('v3', 'rails spacing', r'4\pi K(\tilde u)/K'),
 ('v3', 'bridge prop', r'\int_{-\infty}^{\infty}H(\nu(\varepsilon))'), ('v3', 'offset log-odds', 'P(N_A=0)'),
 ('v3', 'census 0.16I example', '0.16I'), ('v3', 'defect split', 'C_{AB}C_{BA}'), ('v3', 'Gamma_b modulus', r'\sqrt{1-4\lambda}'),
 ('v3', 'speed limit', r'\dot\tau^2\le4gS'), ('v3', 'warm ring counts', '2 to 24 to 64'), ('v3', 'TrX warm', '0.170835'),
 ('v3', 'gas density-free', '0.37757506698375'), ('v3', 'partition bias', '0.36614943350748'),
 ('v3', 'peel add thm', r'u\oplus v=(u+v)/(1+uv)'), ('v3', 'Ising ladder residuals', r'8.0\times10^{-6}'),
 ('v3', 'helium thresholds', '54.4177655282'), ('v3', 'binding sum', '79.0051545392'), ('v3', 'ladder reconstruction', r'\prod_{j<q}(1+\Gamma_j)/(1-\Gamma_j)'),
 ('v3', 'quantum dots', 'quantum-dot'), ('v3', 'sodium 0.9938', '0.9938'), ('v3', 'Thomas-Fermi', 'Thomas'),
 ('v3', 'nuclear table 5He', '734.8'), ('v3', 'nuclear 5Li', '1966.1'), ('v3', 'nuclear 8Be', '7366.6'), ('v3', 'half lives', '81.9 as'),
 ('v3', 'rim distance', r'\frac{2s}{S_{\mathrm{next}}-s}'), ('v3', 'rim exact values', '0.220318'), ('v3', 'small-s values', '0.198457'),
 ('v3', 'resonance caution', 'is not a literal atomic or nuclear Smith reflection'), ('v3', 'half-turn 4000 draws', '4000'),
 ('v3', 'z=1-i gamma', r'z=1-i\gamma'), ('v3', 'cone Q>=0', r'M_{+-}M_{-+}'), ('v3', 'biorthogonal idempotent', r'3\times10^{-14}'),
 ('v3', 'metric 93%', '93'), ('v3', 'Renyi -1.79', '-1.79'), ('v3', 'exit 0.468', '0.468'), ('v3', 'Petermann K', '1+u^2/E(k)^2'),
 ('v3', 'average formula', r'\sqrt{A^2-B^2}'), ('v3', 'predictions', '0.7474014'), ('v3', 'massive 1.015-1.022 limit', 'mass term moves the exit'),
 ('v3', 'filter table', '0.271636929'), ('v3', 'w=0 counterexample', 'v^2=2u^2'), ('v3', 'quarter turn sec^2', r'\sec^2'),
 ('v3', 's11 rotation gap', r'3.4\times10^{-2}'), ('v3', 'open list', 'placing nuclear resonances'),
 ('v3', 'A.1', 'A.1 Zero and span'), ('v3', 'A.2', 'A.2 The census coefficient'), ('v3', 'A.3', 'A.3 The bridge'), ('v3', 'A.4', 'A.4 The offset'),
 ('v3', 'A.5', 'A.5 Defect split'), ('v3', 'A.6', 'A.6 The boundary coordinate'), ('v3', 'A.7', 'A.7 The Offset Speed Limit'), ('v3', 'A.8', 'A.8 Peel steps'),
 ('v3', 'A.9', 'A.9 Scale blindness'), ('v3', 'A.10', 'A.10 The last peel step'), ('v3', 'A.11', 'A.11 Ideal Saha'), ('v3', 'A.12', 'A.12 Outside the rim'),
 ('v3', 'A.13', 'A.13 No cone'), ('v3', 'A.14', 'A.14 The Petermann'), ('v3', 'A.15', 'A.15 The quarter-turn'), ('v3', 'Unsold', 'Ann.\\ Phys.\\ 387'),
 ('v3', 'Lean MatterDisk', 'MatterDisk.lean'), ('v3', 'fig02', 'fig02_boundary_and_gas'), ('v3', 'fig03 (signed rebuild)', 'fig03v4_one_chart'),
] + [('v3', 'script ' + s, s) for s in ['s01_bridge', 's02_ladder', 'nhssh_lib_and_s03a', 's03b_renyi', 's03c_metric_raw', 's03d_metric_rank', 's04a_rotation', 's04b_rotation', 's05a_exit', 's05b_predict', 's06_second_model', 's07_boundary', 's08_gas', 's09_check', 's10_nuclear', 's11_exit', 's12_nuclear']] + [
 # formal edition (Matter_Gases_VOTKP_Formal_Edition_20261103)
 ('gpt', 'B1 defect identity', 'F_A=T_A+X_A'), ('gpt', 'B2 bounds', r'\|B_C\|\le\tfrac12'), ('gpt', 'B3 two-sided', r'\tfrac14\min(a,b)'),
 ('gpt', 'B4 comparison', r'N^\partial_\varepsilon\le N^{\mathrm{raw}}_\varepsilon'), ('gpt', 'B5 trace estimate', r'\theta N^\partial_\varepsilon\le\Tr X_A'),
 ('gpt', 'B6 local unitary', 'U_A\\oplus U_B'), ('gpt', 'B7 stability', 'certified'), ('gpt', 'B8 near projector', 'varepsilon_\\eta'),
 ('gpt', 'B9 extension', r'\sqrt{A-A^2}'), ('gpt', 'B10 variance', r'\mathrm{Cov}(N_A,N_B)=-\Tr X_A'), ('gpt', 'B11 classical', r'\rho_{\mathrm{cl}}'),
 ('gpt', 'B11 entanglement', '|1100'), ('gpt', 'B12 matched boundary', r'C_\pm=\tfrac12I\pm r\sigma_y'), ('gpt', 'B13 info bound', r'4\Tr X_A\le I_G(A:B)'),
 ('gpt', 'B13 upper', r'\delta(1-\delta)'), ('gpt', 'B13 census bound', r'I_G(A:B)/(4\varepsilon(1-\varepsilon))'),
 ('gpt', 'D1 coordinate', r'\Gamma_b\le1-2\varepsilon'), ('gpt', 'D2 back to rim', 'disconnected control'), ('gpt', 'D3 idempotent', 'Y_A=A-A^2'),
 ('gpt', 'D4 radial disk', r'|\lambda-\tfrac14|\le r^2/4'), ('gpt', 'D5 C=[[2,1],[-2,-1]]', r'2&1\\-2&-1'), ('gpt', 'D5 embedding', r'\mathcal P(A)'),
 ('gpt', 'D6 branch', r'\cos(\Ima W)>0'), ('gpt', 'D7 Holder', r'2\sqrt{|\lambda-\tilde\lambda|}'), ('gpt', 'D7 nonnormal J', r'\pm\sqrt\delta'),
 ('gpt', 'G1 anchor', 'anchored coordinate equivalence'), ('gpt', 'G2 exp family', r'd\mu/dy=-V'), ('gpt', 'G3 unique', 'a unique neutral gas'),
 ('gpt', 'G3a helium cubic', r'u^3+\alpha u^2'), ('gpt', 'G4 density', r'\frac{\mu}{\mu+V}'), ('gpt', 'G5 coefficient', 'C_h=\\mathrm{Cov}_p(q,h_q)'),
 ('gpt', 'G6 temperature', r'\tfrac32q+E_q/k_BT'), ('gpt', 'G7 scaling', '(ab)^{3/2}'), ('gpt', 'G7a insufficiency', 'what the atom alone cannot know'),
 ('gpt', 'neutral fractions', '0.289781'), ('gpt', 'G8 inverse', r'(Z-1-r)D_r'), ('gpt', 'G9 partition', r'D_{\mathrm{app}}'), ('gpt', 'G9 conditioning', r'(\eta_1+\eta_2)/|\Delta\beta|'),
 ('gpt', 'G9 bias value', '0.0114256'), ('gpt', 'R1 reduced', 'hidden source'), ('gpt', 'R2 channel measure', r'd\mathsf M'),
 ('gpt', 'R3 witness', '(3,7,1,5)/16'), ('gpt', 'R3 resolvents', '5z^2+3z-9'), ('gpt', 'R4 kernel', r'J_\pm=\pm i/\sqrt2'),
 ('gpt', 'M1 moments', r'\delta(-1)^mm!h^m'), ('gpt', 'M2/readout reflected', '(5,1,7,3)/16'), ('gpt', 'K1', r'48av_0^3'),
 ('gpt', 'K2', r'\sin^3(kv_0t)'), ('gpt', 'K3', r'96a\eta\rho_*k^3v_0^3'), ('gpt', 'K4 reset', r'\mathcal E_s'), ('gpt', 'K null table', 'placement matters'),
 ('gpt', 'P1', r'\tfrac12(1+\sum|d_j|^2/|E|^2)'), ('gpt', 'P2', 'E(0)E(\\pi)=u^2'), ('gpt', 'P3', 'direct sum of identical cell projectors'),
 ('gpt', '9.4 energy origin', r'-\tfrac14,\tfrac34'), ('gpt', '9.4 negative census coefficient', r'a\log\xi+O(1)'),
 ('gpt', '10.1 condition numbers', '575'), ('gpt', '10.1 residual', r'4.4\times10^{-15}'), ('gpt', 'Lean 34', '34 positive declarations'),
 ('gpt', 'Lean (7,11,5,9)', '(7,11,5,9)/32'), ('gpt', 'Peschel', 'Peschel'), ('gpt', 'Wolf et al', 'Hastings'),
] + [('gpt', 'script ' + s, s) for s in ['verify_formal_gas', 'adversarial_checks', 'gaussian_information_checks', 'incoming_exit_filter', 'incoming_exit_residuals']] + [
 # reconciled review strengthening and angular cards
 ('review', 'metric det', r'\det Q=-\frac{u^2w^2\cos^2k}{16\,s^3}'), ('review', 'branch Gamma_end=i', r'\Gamma_{\mathrm{end}}=i'),
 ('review', 'complement parity', 'complement parity'), ('review', 'resolvent adjoint', r'R_{H^*}(z)=R_H(\bar z)^*'),
 ('review', 'Hermitian tangent counterexample', r'\sigma_z+i\theta\sigma_x'), ('review', 'Gaussian hypothesis on offset', 'quasi-free'),
 ('review', 'ANG1', '2k/\\pi'), ('review', 'ANG2', r'k\cot(k/\kappa)-\kappa'), ('review', 'ANG3 coefficient', '0.507092553'), ('review', 'ANG4 Henrici', '1.174462'),
 ('review', 'ANG4 E-', r'k^2\kappa^2/3'), ('review', 'cross weight vs E_H', 'cross weight would understate'),
 # Beyond the Event Horizon ed. 10 bridges
 ('bh', 'gap step', r'\tanh\Big(\tfrac12\ln\frac{\Delta_2}{\Delta_1}\Big)'), ('bh', 'Clairaut step', 'Clairaut'), ('bh', 'Schur-Cayley', 'Schur'),
 ('bh', 'membrane resistivity', '376.73'), ('bh', 'fermion record', r'\tanh\frac{\hbar\omega}{2k_BT_H}'), ('bh', 'off-diagonal block family', 'PHQHP'),
 ('bh', 'spectral vs geometric walls', 'Two kinds of wall'), ('bh', 'polar mirror', 'perfect mirror'), ('bh', 'ringdown 391', '391'),
] + [('new', 'figure ' + f, f) for f in ['fig04_reflection_chart', 'fig05_metric_signature', 'fig06_records_and_futures', 'fig07_exit_and_filter', 'fig08_angular_chain', 's13_v4_bridges']]
miss = [(a, b) for a, b, c in M if re.sub(r'\s+', ' ', c) not in flat]
by = {}
for a, b, c in M: by.setdefault(a, [0, 0]); by[a][0] += 1; by[a][1] += (a, b) not in miss
for k, (n, ok) in by.items(): print(f'{k:7s} {ok}/{n} present')
for a, b in miss: print('MISSING', a, b)
print('v4 source characters', len(tex), ' v3 source characters', len(open('../paper/matter_then_on_down_v3.tex').read()))
print('PASS' if not miss else 'FAIL')

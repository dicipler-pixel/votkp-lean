# SCRIPT: SWING_NOTES_BUILD_01 — builds Swing_Notes_and_Test_v1_20261116.html from the two result files and two redrawn series.
import json, math, html, importlib.util, io, contextlib
import numpy as np
o1 = json.load(open('swing_test_01.out.json')); o2 = json.load(open('swing_test_02.out.json'))
def load(name):
    sp = importlib.util.spec_from_file_location(name, name + '.py'); m = importlib.util.module_from_spec(sp)
    with contextlib.redirect_stdout(io.StringIO()): sp.loader.exec_module(m)
    return m
m1 = load('swing_test_01'); m2 = load('swing_test_02')
hb, _, _ = m1.run([10, 10], [3.0], 'mirror', 130); ho, _, _ = m1.run([10, 37], [3.0], 'load', 130)
N, V, P, A, B, phi, mg, rk = m2.setup(20); K = np.eye(2*N); K[2, 2] = -1; Pt = K @ P @ K; dB = []
for t in range(61): dB.append(float(np.linalg.norm((Pt - P)[np.ix_(B, B)]))); Pt = V @ Pt @ V.T
def chart(series, w=720, h=230, ymax=1.05, vline=None, xlabel='step', ylabel=''):
    n = max(len(s[0]) for s in series); X = lambda i: 52 + i*(w - 70)/(n - 1); Y = lambda v: h - 34 - v*(h - 54)/ymax; s = [f'<svg viewBox="0 0 {w} {h}" role="img" style="width:100%;max-width:{w}px;display:block;margin:10px 0">']
    for v in (0, 0.25, 0.5, 0.75, 1.0): s.append(f'<line x1="52" x2="{w-18}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="#22304d"/><text x="46" y="{Y(v)+4:.1f}" fill="#93a1bd" font-size="11" text-anchor="end" font-family="system-ui">{v:g}</text>')
    for i in range(0, n, 10): s.append(f'<text x="{X(i):.1f}" y="{h-16}" fill="#93a1bd" font-size="11" text-anchor="middle" font-family="system-ui">{i}</text>')
    if vline is not None: s.append(f'<line x1="{X(vline):.1f}" x2="{X(vline):.1f}" y1="14" y2="{h-34}" stroke="#f2c14e" stroke-dasharray="5 4"/><text x="{X(vline)+6:.1f}" y="24" fill="#f2c14e" font-size="12" font-family="system-ui">light can first arrive (step {vline})</text>')
    for data, col, name in series: s.append('<polyline fill="none" stroke="%s" stroke-width="2" points="%s"/>' % (col, ' '.join(f'{X(i):.1f},{Y(v):.1f}' for i, v in enumerate(data))))
    lx = 60
    for data, col, name in series: s.append(f'<rect x="{lx}" y="{h-10}" width="14" height="3" fill="{col}"/><text x="{lx+20}" y="{h-5}" fill="#e6ecf7" font-size="11.5" font-family="system-ui">{name}</text>'); lx += 30 + 7*len(name)
    s.append(f'<text x="{w-18}" y="{h-5}" fill="#93a1bd" font-size="11" text-anchor="end" font-family="system-ui">{xlabel}</text></svg>'); return ''.join(s)
f = lambda x, n=4: ('%.' + str(n) + 'g') % x; e = lambda x: '%.1e' % x
H = lambda t: '<span class="g held">HELD</span>' if t else '<span class="g kill">KILLED</span>'
a = o2['arc']; t4 = o1
rows = [
 ('T1', 'Sealed loop', 'If nothing can leave, the swing must come back exactly.', 'Energy off 1 by more than 1e-12, or the state at one round trip differs from the start.', f"Energy off by {e(o1['T1']['max_energy_dev'])}; return error {e(o1['T1']['return_error_at_2L'])}.", o1['T1']['held']),
 ('T2', 'Open end', 'Each meeting with the face keeps Γ² and the load returns nothing, so after n meetings the swing holds Γ^(2n).', 'Held differs from Γ^(2n) by more than 1e-12 for any n up to 20; or the books are off.', f"Held after meetings 1, 2, 3: {', '.join(f(x) for x in o1['T2']['held_after_1_2_3'])}. Largest error {e(o1['T2']['max_abs_err'])}; books off by {e(o1['T2']['books_dev'])}.", o1['T2']['held']),
 ('T3', 'Bigger container', 'What leaves must travel out and back, so it cannot re-enter before step L + 2D. Until then the run must match the open end exactly.', 'The two runs differ before step 84, or do not differ at step 84, or the books are off.', f"First difference at step {o1['T3']['measured_first_difference_step']} (derived: {o1['T3']['predicted_first_difference_step']}). Books off by {e(o1['T3']['books_dev'])}.", o1['T3']['held']),
 ('T3b', 'Bigger container, in time', 'A lossless two-sided face undoes itself on the pair (inside, outside). If what left returns at the same instant, the whole loss must come back on the next meeting.', 'Held differs from Γ² (odd meetings) or 1 (even meetings) by more than 1e-12; both face signs.', f"Held after meetings 1 to 4: {', '.join(f(x) for x in o1['T3b']['held_after_meetings_1_to_4'])}. Largest error {e(o1['T3b']['max_err_sign_plus'])} with either face sign.", o1['T3b']['held']),
 ('T4a', 'Squeeze in time, wall moving in', 'A wall moving at v multiplies the pulse energy by D = (1 − v)/(1 + v) at each meeting; in time, every meeting has the same v.', 'Energy after 20 meetings off D₀^20 by more than 1%.', f"D₀ = {f(o1['T4a']['D0'],6)}. Derived ×{f(o1['T4a']['predicted'],6)}, measured ×{f(o1['T4a']['measured'],6)} (off by {e(o1['T4a']['rel_err'])}).", o1['T4a']['held']),
 ('T4b', 'Squeeze in time, wall moving out', 'The same law with the sign of v reversed: the swing hands energy back.', 'Energy after 5 meetings off D₀^(−5) by more than 1%.', f"Derived ×{f(o1['T4b']['predicted'],6)}, measured ×{f(o1['T4b']['measured'],6)} (off by {e(o1['T4b']['rel_err'])}).", o1['T4b']['held']),
 ('T4c', 'Squeeze out of time', 'Out of time the meetings fall at every phase, gains and losses cancel.', 'Mean log gain per meeting over 200 meetings above 0.1 ln D₀.', f"Mean log gain {f(o1['T4c']['mean_log_gain_per_meeting'],3)} against a limit of {f(o1['T4c']['limit'],3)}; single meetings still move the energy by up to {f(o1['T4c']['largest_single_step'],3)} in the log.", o1['T4c']['held']),
 ('T4d', 'The books of the squeeze', 'Energy gained must equal the work done by the wall, with wall pressure 2 × incident energy density × D.', 'Gain and work differ by more than 0.1%.', f"Gain {f(o1['T4d']['gain'],9)}, work {f(o1['T4d']['work'],9)} (off by {e(o1['T4d']['rel_err'])}).", o1['T4d']['held']),
 ('T5', 'The rate moves with the squeeze', 'Energy × length is kept under a slow squeeze, so a 0.8 squeeze raises energy by 1.25 and cuts the period to 0.8. A leak does neither.', 'Energy ratio off 1.25 or period ratio off 0.8 by more than 1%.', f"Energy ×{f(o1['T5']['energy_ratio'],5)}; period ×{f(o1['T5']['period_end_over_start'],5)}.", o1['T5']['held']),
 ('T6a', 'The sea at rest (run 01)', 'A rest sea must be carried into itself by one step.', 'V P V† differs from P by more than 1e-12.', f"Differed by {f(o1['T6a']['rest_dev'],3)}. The step matrix has spectrum exactly on the chosen cut, so the chosen half was not a defined set.", False),
 ('T6c', 'Changes travel (run 01)', 'Depends on T6a.', 'Any change on B before step 24.', 'Failed with T6a: a sea that is not at rest changes on B by itself from step 1. T6b and E2 of run 01 are withdrawn with it.', False),
 ("T6a′", 'The sea at rest, cut in a gap (run 02)', 'The same line, with the filled half ending in the two widest gaps of the spectrum (found by the script).', 'V P V† differs from P by more than 1e-12.', f"Cut ends {f(a['margin'],3)} from the nearest spectrum point; {a['rank']} of {a['of']} states filled. Differs by {e(a['T6a']['rest_dev'])}. The other half of the circle: {e(o2['opposite_arc']['T6a']['rest_dev'])}.", a['T6a']['held']),
 ("T6b′", 'Tied at rest (run 02)', 'If the swing at rest is everywhere, the weight between two far swings is not zero while nothing moves.', 'Weight between A and B at or below 1e-12.', f"Weight between A and B at rest: {f(a['T6b']['weight_between_at_rest'],4)} (the other half: the same).", a['T6b']['held']),
 ("T6c′", 'Changes travel (run 02)', 'One step moves light one cell. A kick at cell 2 cannot reach B (cell 26) before step 24, whatever the sea holds.', 'Any change on B above 1e-12 before step 24; or none above 1e-9 by step 72.', f"Largest change on B before step 24: {e(a['T6c']['largest_change_before_crossing'])}. At step 24: {f(a['T6c']['change_at_steps_23_24_25_26'][1],4)}. Same for the other half.", a['T6c']['held']),
 ('T6d', 'All at once (the Moving Matrix way)', 'One matrix with direct links moves every ball together, so the far ball must change with no delay.', 'Change on the far ball at 1% of the light-crossing time below 1e-8.', f"Change on the far ball at 1% of the crossing time: {f(o1['T6d']['change_at_1_percent'],3)}; at 10%: {f(o1['T6d']['change_at_10_percent'],3)}.", o1['T6d']['held'])]
table = ''.join(f'<tr><td><b>{r[0]}</b><br>{r[1]}</td><td>{r[2]}</td><td>{r[3]}</td><td>{r[4]}</td><td>{H(r[5])}</td></tr>' for r in rows)
E1 = ''.join(f"<tr><td>{k}</td><td>{f(v['most_the_swing_gets_back'],6)}</td><td>{f(v['mean_held'],3)}</td></tr>" for k, v in o1['E1'].items())
E2 = ''.join(f"<tr><td>{k}</td><td>{f(v['weight_between'],3)}</td></tr>" for k, v in o2['E2'].items())
src = ''.join(f'<h3>{n}</h3><pre>{html.escape(open(n).read())}</pre>' for n in ('PREREG_SWING_01.md', 'PREREG_SWING_02.md', 'swing_test_01.py', 'swing_test_02.py'))
page = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>The Swing: notes and test</title>
<style>/* SCRIPT: SWING-NOTES-V1 page. Jeromie Beasley. 16 Nov 2026. AI-assisted. */
:root{{--bg:#070b14;--card:#0e1524;--ink:#e6ecf7;--dim:#93a1bd;--line:#22304d;--gold:#f2c14e;--cy:#5ad1e6;--gr:#7be0a1;--rd:#ff7a7a;--vi:#b79cff}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 Georgia,serif}}header{{padding:44px 6vw 20px;border-bottom:1px solid var(--line)}}h1{{font-size:2rem;margin:0 0 6px;font-weight:600}}
.sub{{color:var(--dim);font:.95rem system-ui,sans-serif}}main{{max-width:1000px;margin:0 auto;padding:10px 6vw 80px}}h2{{font-size:1.4rem;margin:44px 0 8px;color:var(--gold);font-weight:600}}h3{{font-size:1.05rem;margin:24px 0 6px;color:var(--cy)}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 18px;margin:14px 0}}.eq{{font-family:ui-monospace,Consolas,monospace;color:#d8e8ff;border-left:3px solid var(--cy);padding:4px 12px;margin:10px 0;overflow-wrap:anywhere}}
table{{border-collapse:collapse;width:100%;font:14px/1.45 system-ui,sans-serif;margin:12px 0}}th,td{{border-bottom:1px solid var(--line);padding:7px 8px;text-align:left;vertical-align:top}}th{{color:var(--dim);font-weight:600}}
.g{{display:inline-block;font:600 11px system-ui,sans-serif;letter-spacing:.04em;padding:2px 8px;border-radius:99px;border:1px solid}}.held{{color:var(--gr);border-color:var(--gr)}}.kill{{color:var(--rd);border-color:var(--rd)}}
.t{{color:var(--vi);border-color:var(--vi)}}pre{{font:12px/1.45 ui-monospace,Consolas,monospace;background:#0a1120;border:1px solid var(--line);border-radius:8px;padding:12px;white-space:pre-wrap;overflow-wrap:anywhere;color:#cfe3ff}}
q{{color:#f6dfa0}}footer{{color:var(--dim);font:13px system-ui,sans-serif;padding:20px 6vw 60px;border-top:1px solid var(--line)}}</style></head><body>
<header><h1>The Swing: notes and test</h1><div class="sub">The ground state as a swing, the open end, and the bigger container · Jeromie Beasley · 16 November 2026 · AI-assisted</div></header><main>
<p>These are the notes of one evening's talk turned into a test. The kill lines were written to a file before any run. One part was killed on the first run; it is recorded, and its rerun has its own file written before that run. The model is one line of light, faces and ends. It is small on purpose: every number in it can be derived by hand first.</p>
<h2>1 · The notes</h2>
<div class="card"><p><b>The swing.</b> The ground state, the sea of electrons, is <q>like a swing</q>, a <q>cosmic sync beam</q>.</p>
<p><b>The crux.</b> Is it <q>a charged loop like structure that holds itself together shut, all energy conserved</q>, or <q>an open container on some end</q>, or <q>no end no background</q>?</p>
<p><b>The bigger container.</b> An open end loses a little each cycle and needs feeding, <q>unless it is in another even bigger container, then it may just be a compression of sorts</q>.</p>
<p><b>The kick.</b> <q>If you want to get energy you must kick it like a photon.</q></p>
<p><b>The beam.</b> Everywhere at once, or must the sync travel along the links like light. A third option from the talk: the swing at rest is everywhere, and only changes to it travel.</p></div>
<h2>2 · The model</h2>
<p>A line of stretches of field joined by faces. Light crosses one cell per step. A face of step ratio z scatters by the proved rule, and an end is one of the two extremes of the same rule.</p>
<div class="eq">Γ = (z − 1)/(z + 1) &nbsp;·&nbsp; return Γ², pass 1 − Γ² &nbsp;·&nbsp; mirror: |Γ| = 1 &nbsp;·&nbsp; matched load: Γ = 0</div>
<p>A swing is the light held between two faces; its period is the round trip, 2L. There is no law of motion for the faces here and no torque, so nothing in this model can lock. Choices made to close it: one dimension, and the face sign (+ρ seen from the left).</p>
<h2>3 · The loss comes back</h2>
<p>The same swing, twice. With an open end it keeps a quarter at every meeting with its face (z = 3, Γ² = ¼) and nothing returns. Inside a bigger container of the same length, what left meets the swing again at the face, and the face hands all of it back: ¼, then 1, then ¼, then 1.</p>
{chart([(list(ho), '#ff7a7a', 'open end (matched load)'), (list(hb), '#7be0a1', 'inside a bigger container, in time')])}
<p style="color:var(--dim);font:13.5px system-ui">Share of the light held by the swing against step. Both runs are the same until what left has had time to come back.</p>
<h2>4 · At rest everywhere; changes travel</h2>
<p>Two swings joined by a link of 20 cells, sealed. The sea is half of the step matrix's spectrum, with the cut in a gap. At rest the two swings are already tied: the weight between them is {f(a['T6b']['weight_between_at_rest'],3)}. Kick one cell of the first swing, and the sea on the second does not move at all until light could have crossed.</p>
{chart([(dB, '#5ad1e6', 'change of the sea on the far swing')], vline=24)}
<p style="color:var(--dim);font:13.5px system-ui">Before step 24 the change is {e(a['T6c']['largest_change_before_crossing'])} (rounding). In the Moving Matrix, where one matrix with direct links moves everything together, the far ball has already changed by {f(o1['T6d']['change_at_1_percent'],2)} at 1% of the crossing time.</p>
<h2>5 · Every test, why it decides, its kill line, and what came out</h2>
<table><tr><th>Test</th><th>Why it decides the claim</th><th>Kill line (fixed before the run)</th><th>Result</th><th></th></tr>{table}</table>
<h2>6 · Looks with no kill line</h2>
<div class="card"><h3 style="margin-top:0">How much the swing gets back, against the size of the container</h3>
<table><tr><th>container length ÷ swing length</th><th>most the swing gets back in 400 round trips</th><th>mean held</th></tr>{E1}</table>
<p>Whole-number ratios (1, 2, 3) return all but a few parts in 100,000. Ratios in between return less: 1.5 gives 0.9988, 1.4 and 1.6 give 0.97 and 0.96. This was looked at after the fact and over one fixed span of time, so it is a lead toward the gear idea, not a result.</p></div>
<div class="card"><h3 style="margin-top:0">The tie at rest, against the length of the link</h3>
<table><tr><th>link length (cells)</th><th>weight between the two swings at rest</th></tr>{E2}</table><p>The tie weakens as the link grows and does not vanish.</p></div>
<h2>7 · What this says and does not say</h2>
<div class="card"><p><b>Says.</b> In this model an open end and a bigger container are told apart by one thing: whether what left comes back, and when. A container in time with the swing returns the whole loss. A squeeze in time feeds the swing and out of time does not, and the books of the squeeze close against the wall's work. A sea can be tied everywhere at rest and still pass no change faster than light: the third option is a consistent machine. The all-at-once machine differs from it in when the far sea first moves.</p>
<p><b>Grades.</b> T2, T3, T3b: derived from the proved face rule and checked. T4, T5: reproduction of the moving-mirror Doppler law and radiation pressure, shown in the face language; at v → 0 the wall pressure is the 2R of the ball pages with R = 1. T6′: checked on one layout with a declared choice of the filled half; a tie at rest in a filled sea is known physics, the point here is that it sits with the travel rule in one machine. T6d: checked on one three-ball matrix.</p>
<p><b>Does not say.</b> Which machine nature uses. Whether the universe is sealed, open or nested. Anything about locking or gear locking: this model is linear and cannot lock. Anything about the clock ratio z. The sea here has no interactions, is in one dimension, and the tie depends on which half is filled.</p></div>
<h2>8 · Evidence</h2>{src}</main><footer>Jeromie Beasley · 16 November 2026 · AI-assisted · Page SWING-NOTES-V1</footer></body></html>'''
open('Swing_Notes_and_Test_v1_20261116.html', 'w', encoding='utf-8').write(page); print(len(page))

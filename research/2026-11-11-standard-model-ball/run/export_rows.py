# SCRIPT: SM-END-PHASE-EXPORT
# Per-step rows (rapidity, lab turn, rest-frame turn) for the twin-prime chain word, 40 steps, from the 80-digit run, for the mixer.
exec(open('end_phase_02.py').read().split("random.seed(7)")[0])
import json
rows=run2(chain[:40])
json.dump([[float(e),float(a),float(o)] for e,a,o in rows], open('chain_rows.json','w'))
print(len(rows), rows[0][0], rows[-1])

# SCRIPT: BALLFILM-CUES-01 (narrator cue files per segment from the narration beats: hand, cane tap, arc to the centre of the ball, mirror turn)
import json
from narration import SEGMENTS
T=json.load(open('times.json'))
for name,eye,beats in SEGMENTS:
    c=dict(secs=T[name]['total']+0.5,taps=[],mirrors=[],arcs=[],gestures=[])
    for (text,acts,cues),(t0,d) in zip(beats,T[name]['marks']):
        if 'g' in cues: c['gestures'].append([t0+0.4, t0+min(d-0.4, 8.0), 62 if len(c['gestures'])%2==0 else 66])
        if 'tap' in cues: c['taps'].append(t0+d-1.3)
        if 'arc' in cues: c['arcs'].append([t0+0.45*d, 0.40, 0.444])
        if 'mir' in cues: c['mirrors'].append(t0+0.12*d)
    json.dump(c,open(f'cue_{name}.json','w'))
print('cues written')

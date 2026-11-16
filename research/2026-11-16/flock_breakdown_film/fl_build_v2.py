# SCRIPT: FL-BUILD-V2 — assembles the two Flock of Balls on the Field pages.
# Each takes one of the two ball pages held inside Two Balls, Linked v1 (the Mixer v2 ball and the white ball, with their eyes and layers
# exposed), removes the three-ball layer, and appends MM-MATH-V1, FL-MATH-V2 and FL-LAYER-V1. The original pages are not changed.
import os
D = os.path.dirname(os.path.abspath(__file__)); rd = lambda p: open(p, encoding='utf-8').read()
mm = rd(D + '/../mm/mm_math_v1.js'); flm = rd(D + '/fl_math_v2.js'); lay = rd(D + '/fl_layer_v1.js')
add = '\n<script>' + mm + '\n' + flm + '</script>\n<script>' + lay + '</script>\n'
import re
def one(src, title_new, out):
    s = rd(src); k = s.rfind('<script>/* SCRIPT: TB-LAYER-V3'); 
    if k < 0: k = s.rfind('<script>', 0, s.rfind('SCRIPT: TB-LAYER-V3'))
    e = s.find('</script>', k) + len('</script>'); assert k > 0 and 'TB-LAYER-V3' in s[k:k+200], src; s = s[:k] + s[e:]      # the host page with its eyes and layers exposed, without the three-ball layer
    assert 'TB-LAYER-V3' not in s and '__TBHOST' in s
    s = s.replace('const q = Math.min(3.999999, f*4), i','const q = Math.min(3.999999, Math.max(0, f*4)), i')   # V2: clamp, a tiny negative loop fraction gave step index -1 at page time 10
    s = re.sub(r'<title>[^<]*</title>', '<title>' + title_new + '</title>', s, count=1)
    i = s.rfind('</body>'); s = s[:i] + add + s[i:]; open(out, 'w', encoding='utf-8').write(s); print(out, len(s))
one('/home/claude/balls/ex_two_mixer.html', 'Flock of Balls on the Field', D + '/Flock_of_Balls_on_the_Field_Mixer_v2_20261116.html')
one('/home/claude/balls/ex_two_white.html', 'Flock of Balls on the Field, white ball', D + '/Flock_of_Balls_on_the_Field_White_v2_20261116.html')

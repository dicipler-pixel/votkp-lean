# SCRIPT: TWO-TREES-CORE-CHECK
# Checks the Two Trees core-Lean files (no Mathlib) with plain `lean`:
#   1. every file in lean/ compiles (exit 0), with the expected number of theorems;
#   2. no `sorry`, `admit`, `native_decide` or `axiom` declaration appears;
#   3. axiom audit: `#print axioms` for every theorem, each set inside {propext, Classical.choice, Quot.sound};
#   4. every false control in lean/controls/ is rejected (the expected number of distinct error positions).
# Kill condition: any failure exits 1 and the CI badge goes red.
import os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
LEAN = os.environ.get('LEAN', 'lean')
EXPECT = {'PeelTrees.lean': 74, 'PeelTrees2.lean': 49, 'PeelTrees3.lean': 7, 'PeelTrees4.lean': 12, 'PingPong7.lean': 17}
CONTROLS = {'Controls1.lean': 3, 'Controls4.lean': 3}
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}
fail = []
def run(path):
    r = subprocess.run([LEAN, path], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr
total = 0
for f, n in EXPECT.items():
    p = os.path.join(HERE, 'lean', f); src = open(p, encoding='utf-8').read()
    names = re.findall(r'^theorem\s+(\S+)', src, re.M); ns = re.search(r'^namespace\s+(\S+)', src, re.M).group(1)
    code_only = re.sub(r'--[^\n]*', '', re.sub(r'/-.*?-/', '', src, flags=re.S))   # comments removed
    bad = re.findall(r'\bsorry\b|\badmit\b|native_decide|^axiom\s', code_only, re.M)
    code, out = run(p)
    print('%-16s compile exit %d, theorems %d (expected %d), forbidden tokens %d' % (f, code, len(names), n, len(bad)))
    if code != 0: fail.append(f + ' does not compile'); print(out[-3000:])
    if len(names) != n: fail.append(f + ' theorem count')
    if bad: fail.append(f + ' forbidden token')
    end = '\nend %s' % ns; i = src.rindex(end)
    audit = src[:i] + end + '\n' + ''.join('#print axioms %s.%s\n' % (ns, t) for t in names)
    with tempfile.NamedTemporaryFile('w', suffix='.lean', delete=False, encoding='utf-8') as t:
        t.write(audit); tp = t.name
    code, out = run(tp); os.unlink(tp)
    lines = [l for l in out.splitlines() if 'depends on axioms' in l or 'does not depend on any axioms' in l]
    worst = set()
    for l in lines:
        m = re.search(r'axioms: \[(.*)\]', l)
        if m: worst |= {a.strip() for a in m.group(1).split(',')}
    print('%-16s axiom audit: %d of %d theorems reported, axioms used %s' % (f, len(lines), len(names), sorted(worst)))
    if code != 0 or len(lines) != len(names) or not worst <= ALLOWED: fail.append(f + ' axiom audit')
    total += len(names)
print('total theorems', total)
for f, n in CONTROLS.items():
    code, out = run(os.path.join(HERE, 'lean', 'controls', f))
    pos = sorted(set(re.findall(r'%s:(\d+):\d+: error' % re.escape(f), out)))
    print('%-16s false controls rejected at lines %s (expected %d)' % (f, pos, n))
    if code == 0 or len(pos) != n: fail.append(f + ' controls')
if fail:
    print('FAILED:', fail); sys.exit(1)
print('ALL CHECKS PASSED')

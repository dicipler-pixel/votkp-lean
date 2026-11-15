# SCRIPT: s17_make_html
# Builds the HTML edition of SCREEN-PROG-04 from the same LaTeX source as the PDF: pandoc (MathML) for the body,
# then numbered citations, numbered equations, the abstract, inline SVG figures and a reference list.
import re, subprocess, html, sys
src = open('screen04.tex').read()
# equation numbers in order of appearance; tag each display so MathML shows it
labels = []
def tag_eq(m):
    body = m.group(1); n = len(labels) + 1
    lab = re.search(r'\\label\{([^}]*)\}', body); labels.append(lab.group(1) if lab else None)
    body = re.sub(r'\\label\{[^}]*\}', '', body)
    return '\\begin{equation}' + body + '\\tag{%d}\\end{equation}' % n
src_h = re.sub(r'\\begin\{equation\}(.*?)\\end\{equation\}', tag_eq, src, flags=re.S)
eqnum = {l: i+1 for i, l in enumerate(labels) if l}
src_h = re.sub(r'\\begin\{center\}\s*\{\\LARGE.*?\\end\{center\}', '', src_h, flags=re.S)                 # own title block
src_h = re.sub(r'\\noindent\\textit\{AI-assisted:.*?\}\n', '', src_h, flags=re.S)
abstract = re.search(r'\\begin\{abstract\}\s*\\noindent(.*?)\\end\{abstract\}', src_h, re.S).group(1)
src_h = re.sub(r'\\begin\{abstract\}.*?\\end\{abstract\}', '', src_h, flags=re.S)
bib = re.search(r'\\begin\{thebibliography\}\{99\}\\small(.*?)\\end\{thebibliography\}', src_h, re.S).group(1)
src_h = re.sub(r'\\begin\{thebibliography\}.*?\\end\{thebibliography\}', '', src_h, flags=re.S)
src_h = src_h.replace('\\quad \\textbf', '\n\n\\textbf')
src_h = re.sub(r'\.\./figs/(f[0-9a-z_]+)\.pdf', r'FIG:\1', src_h)
keys = re.findall(r'\\bibitem\{([^}]*)\}', bib); num = {k: i+1 for i, k in enumerate(keys)}
def pd(tex, inline=False):
    out = subprocess.run(['pandoc', '-f', 'latex', '-t', 'html5', '--mathml'], input=tex, capture_output=True, text=True).stdout
    return re.sub(r'^<p>|</p>\s*$', '', out.strip()) if inline else out
body = pd(src_h)
body = re.sub(r'<span\s+class="citation"\s+data-cites="([^"]*)"></span>', lambda m: '[' + ', '.join('<a href="#ref-%s">%d</a>' % (k, num[k]) for k in m.group(1).split()) + ']', body)
body = re.sub(r'<a href="#(eq:[^"]*)"[^>]*>[^<]*</a>', lambda m: str(eqnum[m.group(1)]), body)
body = re.sub(r'<a href="#app:repro"[^>]*>[^<]*</a>', '<a href="#app-repro">A</a>', body)
body = body.replace('id="app:repro"', 'id="app-repro"')
# section numbering, matching the PDF; the appendix is A
secs = re.findall(r'<h1 id="([^"]*)">', body); n = 0
def numsec(m):
    global n
    t = m.group(2)
    if t in ('Declarations',): return m.group(0)
    if t == 'Reproduction': return '<h1 id="%s">A&ensp;%s</h1>' % (m.group(1), t)
    n += 1; return '<h1 id="%s">%d&ensp;%s</h1>' % (m.group(1), n, t)
body = re.sub(r'<h1 id="([^"]*)">([^<]*)</h1>', numsec, body)
state = {'sec': 0, 'sub': 0}
def numh(m):
    tag, attrs, text = m.group(1), m.group(2), m.group(3)
    if tag == 'h1':
        k = re.match(r'(\d+)&ensp;', text)
        if k: state['sec'] = int(k.group(1)); state['sub'] = 0
        elif 'A&ensp;' in text: state['sec'] = 'A'; state['sub'] = 0
        return m.group(0)
    if state['sec'] in (0,): return m.group(0)
    state['sub'] += 1
    return '<h2%s>%s.%d&ensp;%s' % (attrs, state['sec'], state['sub'], text)
body = re.sub(r'<(h1|h2)([^>]*)>([^<]*)', numh, body)
# inline the SVG figures
def svg(m):
    s = open('../figs/%s.svg' % m.group(1)).read()
    s = re.sub(r'<\?xml[^>]*\?>|<!DOCTYPE[^>]*>', '', s)
    s = re.sub(r'<svg ', '<svg role="img" aria-label="Figure" ', s, count=1)
    return '<div class="fig">' + s + '</div>'
body = re.sub(r'<img src="FIG:(f[0-9a-z_]+)"[^>]*/>', svg, body)
figs = re.findall(r'<figure id="(fig:[^"]*)">', body)
for i, f in enumerate(figs): body = body.replace('<figure id="%s">' % f, '<figure id="%s" data-n="%d">' % (f, i+1), 1)
body = re.sub(r'<figure id="([^"]*)" data-n="(\d+)">(.*?)<figcaption>', lambda m: '<figure id="%s">%s<figcaption><b>Figure %s.</b> ' % (m.group(1), m.group(3), m.group(2)), body, flags=re.S)
cnt = [0]
def eqn(m):
    cnt[0] += 1
    return '<div class="eq">' + m.group(0) + '<span class="eqn">(%d)</span></div>' % cnt[0]
body = re.sub(r'<math display="block".*?</math>', eqn, body, flags=re.S)
refs = ''.join('<li id="ref-%s">%s</li>' % (k, pd(t.strip(), True)) for k, t in zip(keys, re.split(r'\\bibitem\{[^}]*\}', bib)[1:]))
abs_html = pd(abstract.strip(), True)
page = open('page_template.html').read()
refblock = '<h1 id="references">References</h1><ol class="refs">' + refs + '</ol>'
i = body.index('<h1 id="app-repro">'); body = body[:i] + refblock + body[i:]
page = page.replace('{{ABSTRACT}}', abs_html).replace('{{BODY}}', body)
open('SCREEN-PROG-04.html', 'w').write(page)
print('equations', eqnum, '| figures', len(figs), '| refs', len(keys))

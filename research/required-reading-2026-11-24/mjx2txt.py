# SCRIPT: MJX2TXT-01  turn MathJax SVG equations back into readable linear text
import re,sys,html
from bs4 import BeautifulSoup
def node(g):
    t=g.get('data-mml-node')
    kids=[c for c in g.find_all(recursive=False) if c.name in('g','use','text','rect','svg')]
    def sub(k):
        if k.name=='use':
            c=k.get('data-c'); return chr(int(c,16)) if c else ''
        if k.name=='text': return k.get_text()
        if k.name=='rect': return ''
        return node(k)
    parts=[sub(k) for k in kids]
    mk=[k for k in kids if k.name in('g','svg')]
    P=[node(k) for k in mk]
    if t=='mfrac' and len(P)>=2: return '('+P[0]+')/('+P[1]+')'
    if t=='msup' and len(P)>=2: return P[0]+'^{'+P[1]+'}'
    if t=='msub' and len(P)>=2: return P[0]+'_{'+P[1]+'}'
    if t=='msubsup' and len(P)>=3: return P[0]+'_{'+P[1]+'}^{'+P[2]+'}'
    if t=='msqrt': return 'sqrt('+''.join(parts)+')'
    if t in('munderover',) and len(P)>=3: return P[0]+'_{'+P[1]+'}^{'+P[2]+'}'
    if t in('munder',) and len(P)>=2: return P[0]+'_{'+P[1]+'}'
    if t in('mover',) and len(P)>=2: return P[0]+'^^{'+P[1]+'}'
    if t=='mtr': return ' [ '+' , '.join(P)+' ] '
    if t=='mtext' or t=='mo': return ' '+''.join(parts)+' ' if t=='mtext' else ''.join(parts)
    return ''.join(parts)
def conv(fn,out):
    s=open(fn,encoding='utf-8',errors='ignore').read()
    s=re.sub(r'(?s)<script.*?</script>','',s); s=re.sub(r'(?s)<style.*?</style>','',s)
    def rep(m):
        try:
            g=BeautifulSoup(m.group(0),'lxml-xml').find('g',attrs={'data-mml-node':'math'})
            return ' ⟦'+node(g)+'⟧ '
        except Exception as e: return ' ⟦?⟧ '
    s=re.sub(r'(?s)<mjx-container.*?</mjx-container>',rep,s)
    s=re.sub(r'(?s)<svg.*?</svg>',' [figure] ',s)
    s=re.sub(r'<img[^>]*>',' [image] ',s)
    s=re.sub(r'<(h[1-6])[^>]*>','\n\n#### ',s)
    s=re.sub(r'</(p|div|h[1-6]|li|tr|table|section|figcaption|pre)>','\n',s); s=re.sub(r'<(br|hr)[^>]*>','\n',s); s=re.sub(r'</t[dh]>',' | ',s)
    s=re.sub(r'<[^>]+>','',s); s=html.unescape(s); s=re.sub(r'[ \t\xa0]+',' ',s); s=re.sub(r'\n\s*\n+','\n\n',s)
    open(out,'w').write(s); print(len(s))
conv(sys.argv[1],sys.argv[2])

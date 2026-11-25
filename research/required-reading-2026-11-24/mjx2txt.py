# SCRIPT: READ-MJX2TXT — MathJax-SVG html -> plain text with linear math (for reading papers in full)
import sys, re, html as H
from lxml import etree, html as LH
src=open(sys.argv[1],errors='ignore').read()
doc=LH.fromstring(src)
for bad in doc.xpath('//script|//style'): bad.getparent().remove(bad)
def ch(g):  # glyph text from <use data-c>
    out=''
    for u in g.iter():
        if u.tag.endswith('use') and u.get('data-c'):
            try: out+=chr(int(u.get('data-c'),16))
            except: pass
    return out
def node(g):
    t=g.get('data-mml-node')
    kids=[k for k in g if isinstance(k.tag,str) and k.get('data-mml-node')]
    if t is None:
        # wrapper g: descend
        return ''.join(node(k) for k in g if isinstance(k.tag,str)) if len(g) else ''
    if t in ('mi','mo','mn','mtext','mspace','ms'):
        return ch(g) if t!='mtext' else ch(g)
    if t=='msup' and len(kids)==2: return node(kids[0])+'^('+node(kids[1])+')'
    if t=='msub' and len(kids)==2: return node(kids[0])+'_('+node(kids[1])+')'
    if t=='msubsup' and len(kids)==3: return node(kids[0])+'_('+node(kids[1])+')^('+node(kids[2])+')'
    if t=='mfrac' and len(kids)==2: return '('+node(kids[0])+')/('+node(kids[1])+')'
    if t=='msqrt':
        inner=''.join(node(k) for k in g if isinstance(k.tag,str))
        return '√('+inner.replace('√','',1).strip()+')'
    if t=='mroot' and len(kids)==2: return 'root'+node(kids[1])+'('+node(kids[0])+')'
    if t in ('mover',) and len(kids)==2: return node(kids[0])+'^{'+node(kids[1])+'}'
    if t in ('munder',) and len(kids)==2: return node(kids[0])+'_{'+node(kids[1])+'}'
    if t=='munderover' and len(kids)==3: return node(kids[0])+'_{'+node(kids[1])+'}^{'+node(kids[2])+'}'
    if t=='mtable':
        def near(e,types):
            p=e.getparent()
            while p is not None:
                if p.get('data-mml-node') in types: return p
                p=p.getparent()
            return None
        rows=[r for r in g.iter() if r is not g and isinstance(r.tag,str) and r.get('data-mml-node') in ('mtr','mlabeledtr') and near(r,('mtable',)) is g]
        out=[]
        for r in rows:
            cells=[c for c in r.iter() if c is not r and isinstance(c.tag,str) and c.get('data-mml-node')=='mtd' and near(c,('mtr','mlabeledtr')) is r]
            out.append(' & '.join(node(c) for c in cells))
        labels=[c for c in g.iter() if isinstance(c.tag,str) and c.get('data-mml-node')=='mtd' and near(c,('mtr','mlabeledtr')) is None and near(c,('mtable',)) is g]
        lab=' '.join(node(c) for c in labels)
        body=' ; '.join(out)
        return (body if len(out)==1 else '[ '+body+' ]')+(('   '+lab) if lab else '')
    return ''.join(node(k) for k in g if isinstance(k.tag,str))
for c in doc.xpath('//mjx-container'):
    gs=c.xpath('.//*[@data-mml-node="math"]')
    txt=node(gs[0]) if gs else ''
    txt=txt.replace('⁡','')
    disp=c.get('display')=='true'
    span=etree.Element('span'); span.text=(' \n  ⟦ '+txt+' ⟧\n' if disp else ' ⟨'+txt+'⟩ ')
    span.tail=c.tail; c.getparent().replace(c,span)
for im in doc.xpath('//img'): 
    s=etree.Element('span'); s.text='[FIG]'; s.tail=im.tail; im.getparent().replace(im,s)
for svg in doc.xpath('//svg'):
    s=etree.Element('span'); s.text='[SVG-FIG]'; s.tail=svg.tail; svg.getparent().replace(svg,s)
for e in doc.xpath('//p|//div|//h1|//h2|//h3|//h4|//li|//tr|//figcaption|//br|//section|//table'):
    e.tail=(e.tail or '')+'\n'
    if e.tag in ('p','h1','h2','h3','h4','li','tr','figcaption'): e.text='\n'+(e.text or '')
for td in doc.xpath('//td|//th'): td.tail=' | '+(td.tail or '')
t=doc.text_content()
t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n\n',t)
open(sys.argv[2],'w').write(t); print(len(t))

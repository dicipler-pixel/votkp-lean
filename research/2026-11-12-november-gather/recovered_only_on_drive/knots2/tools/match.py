import json,os,re,sys
a=json.load(open('/home/claude/notes/nov_list/repo_script_names.json'))
b=json.load(open('/home/claude/notes/nov_list/repo_index.json'))
bybase={}
for e in b: bybase.setdefault(e['base'],[]).append(e)
roots=['/home/claude/nov/knots/unz/Recovered_Useful_Work_20261031','/home/claude/nov/knots/unz/Heegner_and_Full_Shared_Atlas_Recovery','/home/claude/nov/knots/unz/Knot_Mirror_Complete_Friend_Handoff_20261101','/home/claude/nov/knots/unz/IQGT_sources','/home/claude/nov/knots2/unz']
names={}
files=[]
for r in roots:
  for dp,_,fs in os.walk(r):
    for f in fs:
      p=os.path.join(dp,f)
      files.append((p,f))
      if re.search(r'\.(py|js|c|lean|md|txt|json|sh|html)$',f):
        try: t=open(p,errors='ignore').read(4000)
        except: continue
        for m in re.finditer(r'#\s*SCRIPT:\s*(.+)',t): names.setdefault(m.group(1).strip(),f)
        for m in re.finditer(r'(?://|/\*)\s*SCRIPT:\s*(.+)',t): names.setdefault(m.group(1).strip(),f)
out=[]
for n,f in sorted(names.items()):
  hit=a.get(n)
  if not hit:
    k=[x for x in a if x.strip().startswith(n.split()[0])] if n.split() else []
    hit=a[k[0]] if k else None
  if hit: out.append(f"{n} [{f}] ON REPO: {hit[0]}"+(f" (+{len(hit)-1} more)" if len(hit)>1 else ""))
  else:
    bb=bybase.get(f)
    out.append(f"{n} [{f}] "+(f"FILE-NAME ON REPO: {bb[0]['repo']}:{bb[0]['branch']}:{bb[0]['path']}" if bb else "ONLY ON DRIVE"))
print("\n".join(out)); print(len(names))
print('--- files without SCRIPT name, basename lookup')
seen=set(names.values())
for p,f in sorted(files):
  if f in seen: continue
  if re.search(r'\.(py|c|lean|js|sh)$',f):
    bb=bybase.get(f)
    print(f, '->', (f"{bb[0]['repo']}:{bb[0]['branch']}:{bb[0]['path']} ({len(bb)})" if bb else 'ONLY ON DRIVE'))

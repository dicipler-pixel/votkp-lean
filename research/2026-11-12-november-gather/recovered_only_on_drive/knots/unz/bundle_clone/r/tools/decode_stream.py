import json,pathlib
p=pathlib.Path('heegner_shared_recovery');A=json.load(open(p/'source/stream.json'))
def d(i,seen=None):
 if i<0:return None
 x=A[i]
 if isinstance(x,dict):return {str(A[int(k[1:])]) if k.startswith('_') and k[1:].isdigit() else k:d(v) for k,v in x.items()}
 if isinstance(x,list):return [d(v) for v in x]
 return x
conv=d(86);print(type(conv),len(conv));print(str(conv[0])[:1800]);json.dump(conv,open(p/'source/conversation.json','w'),ensure_ascii=False,indent=2)
rows=[]
for n,node in enumerate(conv,1):
 m=node.get('message') or {};c=m.get('content') or {};parts=c.get('parts') or [];txt='\n'.join(z if isinstance(z,str) else json.dumps(z,ensure_ascii=False) for z in parts);role=(m.get('author') or {}).get('role','unknown');rows.append({'number':n,'id':m.get('id'),'role':role,'text':txt,'create_time':m.get('create_time')})
(p/'messages').mkdir(exist_ok=True)
for r in rows:(p/'messages'/f"{r['number']:03}_{r['role']}.md").write_text(r['text'])
json.dump(rows,open(p/'source/messages.json','w'),ensure_ascii=False,indent=2)
(p/'source/transcript.md').write_text('\n\n'.join(f"## Message {r['number']} — {r['role']}\n\n{r['text']}" for r in rows))
for r in rows:print(r['number'],r['role'],len(r['text']),r['text'][:110].replace('\n',' '))

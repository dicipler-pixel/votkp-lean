# SCRIPT: WOUND-FILM-VOICE  one wav per scene, standing voice (Kokoro am_michael, speed 0.92)
import json, sys, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
T='/tmp/claude-0/-home-claude/502f5ad8-acd9-59a2-b5cf-d48e7967cc3a/scratchpad/film/tts/'
k=Kokoro(T+'kokoro-v1.0.onnx',T+'voices-v1.0.bin'); SR=24000
L=json.load(open('lines.json')); peak=0; outs={}
for sc,lines in L.items():
    out=[np.zeros(int(.6*SR),np.float32)]; starts=[]
    for ln in lines:
        starts.append(sum(len(x) for x in out)/SR)
        y,_=k.create(ln,voice='am_michael',speed=0.92,lang='en-us'); out+=[y.astype(np.float32),np.zeros(int(.38*SR),np.float32)]
    out.append(np.zeros(int(.9*SR),np.float32)); y=np.concatenate(out); outs[sc]=(y,starts); peak=max(peak,np.max(np.abs(y)))
cues={}
for sc,(y,st) in outs.items():
    sf.write(f'voice/{sc}.wav',y/peak*.89,SR); cues[sc]={'dur':len(y)/SR,'starts':st}; print(sc,round(len(y)/SR,2),[round(s,2) for s in st])
json.dump(cues,open('cues.json','w'),indent=1)

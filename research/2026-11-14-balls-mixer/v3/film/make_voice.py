# SCRIPT: BALLFILM-VOICE-01 (Kokoro am_michael, speed 0.92, int8 model; one WAV per beat, joined per segment; beat times saved)
import soundfile as sf, json, numpy as np
from kokoro_onnx import Kokoro
from narration import SEGMENTS
k=Kokoro('/home/claude/kokoro/kokoro-v1.0.int8.onnx','/home/claude/kokoro/voices-v1.0.bin')
T={}
for name,eye,beats in SEGMENTS:
    out=[]; t=0.35; marks=[]; sr=24000; out.append(np.zeros(int(0.35*sr),np.float32))
    for text,_,_ in beats:
        s,sr=k.create(text,voice='am_michael',speed=0.92,lang='en-us'); s=s.astype(np.float32)
        marks.append((t,len(s)/sr)); out.append(s); gap=np.zeros(int(0.55*sr),np.float32); out.append(gap); t+=len(s)/sr+0.55
    y=np.concatenate(out); sf.write(f'v_{name}.wav',y,sr); T[name]=dict(total=len(y)/sr,marks=marks); print(name,round(len(y)/sr,1),flush=True)
    json.dump(T,open('times.json','w'))
print('total',round(sum(v['total'] for v in T.values()),1))

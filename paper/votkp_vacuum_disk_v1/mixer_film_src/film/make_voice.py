# SCRIPT: VOTKP-FILM-VOICE-01  (Kokoro am_michael at speed 0.92, int8 model; one WAV per segment)
import soundfile as sf, json
from kokoro_onnx import Kokoro
from narration import SEGMENTS
k=Kokoro('/home/claude/kokoro/kokoro-v1.0.int8.onnx','/home/claude/kokoro/voices-v1.0.bin')
dur={}
for name,eye,text in SEGMENTS:
    s,sr=k.create(text.replace('Möbius','Moebius'),voice='am_michael',speed=0.92,lang='en-us')
    sf.write(f'v_{name}.wav',s,sr); dur[name]=len(s)/sr; print(name,round(dur[name],1),flush=True)
json.dump(dur,open('durations.json','w')); print('total',round(sum(dur.values()),1))

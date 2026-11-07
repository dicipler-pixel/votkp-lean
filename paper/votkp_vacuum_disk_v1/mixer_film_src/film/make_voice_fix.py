# SCRIPT: VOTKP-FILM-VOICE-02  (re-voice only the reworded segments; same voice and speed)
import soundfile as sf, json, sys
from kokoro_onnx import Kokoro
from narration import SEGMENTS
k=Kokoro('/home/claude/kokoro/kokoro-v1.0.int8.onnx','/home/claude/kokoro/voices-v1.0.bin')
dur=json.load(open('durations.json')); names=sys.argv[1:]
for name,eye,text in SEGMENTS:
    if name not in names: continue
    s,sr=k.create(text.replace('Möbius','Moebius'),voice='am_michael',speed=0.92,lang='en-us')
    sf.write(f'v_{name}.wav',s,sr); dur[name]=len(s)/sr; print(name,round(dur[name],1),flush=True)
json.dump(dur,open('durations.json','w'))

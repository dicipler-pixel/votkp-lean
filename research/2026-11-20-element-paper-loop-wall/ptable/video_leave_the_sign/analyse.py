# SCRIPT: SONG-ANALYSE-01
import librosa, numpy as np, json
y,sr=librosa.load('song.mp3',sr=22050,mono=True)
tempo,beats=librosa.beat.beat_track(y=y,sr=sr)
bt=librosa.frames_to_time(beats,sr=sr)
rms=librosa.feature.rms(y=y,hop_length=2205)[0]  # 0.1 s
t=np.arange(len(rms))*0.1
# 2-second smoothed loudness in dB
db=20*np.log10(np.convolve(rms,np.ones(20)/20,'same')+1e-6)
for i in range(0,len(t),40): print(f'{t[i]:6.1f}s {db[i]:6.1f} dB')
# structural boundaries
C=librosa.feature.chroma_cqt(y=y,sr=sr,hop_length=4096)
M=librosa.feature.mfcc(y=y,sr=sr,hop_length=4096)
F=np.vstack([librosa.util.normalize(C),librosa.util.normalize(M)])
b=librosa.segment.agglomerative(F,14)
print('boundaries',[round(float(x),1) for x in librosa.frames_to_time(b,sr=sr,hop_length=4096)])
print('tempo',tempo,'nbeats',len(bt))
json.dump({'beats':[float(x) for x in bt],'tempo':float(np.atleast_1d(tempo)[0])},open('beats.json','w'))

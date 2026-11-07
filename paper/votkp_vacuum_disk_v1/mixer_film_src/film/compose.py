# SCRIPT: VOTKP-FILM-COMPOSE-01  (live recording + narrator screen-blended bottom-right + voice; fades; concat to one MP4)
import json, subprocess
from narration import SEGMENTS
dur=json.load(open('durations.json')); off=0.0; parts=[]
for name,eye,_ in SEGMENTS:
    D=dur[name]+0.6
    cmd=['ffmpeg','-v','error','-y','-ss','1.6','-t',f'{D:.2f}','-i',f'rec/{name}.webm',
         '-stream_loop','-1','-ss',f'{off%110:.2f}','-i','narr_loop_clean.mp4','-i',f'v_{name}.wav',
         '-filter_complex',
         f"[0:v]fps=30,scale=1280:720,format=gbrp[bg];[1:v]fps=30,pad=1280:720:940:286:black,format=gbrp[n];"
         f"[bg][n]blend=all_mode=screen,format=yuv420p,fade=t=in:st=0:d=0.4,fade=t=out:st={D-0.45:.2f}:d=0.45[v];"
         f"[2:a]adelay=200|200,apad,atrim=0:{D:.2f},aformat=sample_rates=44100:channel_layouts=stereo[a]",
         '-map','[v]','-map','[a]','-t',f'{D:.2f}','-c:v','libx264','-preset','veryfast','-crf','21','-c:a','aac','-b:a','160k',f'seg_{name}.mp4']
    subprocess.run(cmd,check=True); parts.append(f'seg_{name}.mp4'); off+=D; print('composed',name,round(D,1),flush=True)
open('parts.txt','w').write(''.join(f"file {p}\n" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-i','parts.txt','-c','copy','-movflags','+faststart','VOTKP_Vacuum_Disk_Film_v1.mp4'],check=True)
print('done')

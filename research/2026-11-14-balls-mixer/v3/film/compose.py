# SCRIPT: BALLFILM-COMPOSE-01 (recording + narrator screen-blended inside the ball + voice; fades; joined into one MP4)
import json, subprocess
from narration import SEGMENTS
T=json.load(open('times.json')); lead=json.load(open('lead.json')); parts=[]
for name,eye,beats in SEGMENTS:
    D=T[name]['total']+0.5
    cmd=['ffmpeg','-v','error','-y','-ss',f"{lead[name]:.2f}",'-t',f'{D:.2f}','-i',f'rec/{name}.webm','-i',f'narr_{name}.mp4','-i',f'v_{name}.wav','-filter_complex',
      f"[0:v]fps=30,scale=1280:720,format=gbrp[bg];[1:v]fps=30,pad=1280:720:706:190:black,format=gbrp[n];"
      f"[bg][n]blend=all_mode=screen,format=yuv420p,fade=t=in:st=0:d=0.4,fade=t=out:st={D-0.45:.2f}:d=0.45[v];"
      f"[2:a]apad,atrim=0:{D:.2f},aformat=sample_rates=44100:channel_layouts=stereo[a]",
      '-map','[v]','-map','[a]','-t',f'{D:.2f}','-c:v','libx264','-preset','veryfast','-crf','22','-c:a','aac','-b:a','160k',f'seg_{name}.mp4']
    subprocess.run(cmd,check=True); parts.append(f'seg_{name}.mp4'); print('composed',name,round(D,1),flush=True)
open('parts.txt','w').write(''.join(f"file {p}\n" for p in parts))
subprocess.run(['ffmpeg','-v','error','-y','-f','concat','-i','parts.txt','-c','copy','-movflags','+faststart','Balls_in_One_Ball_Film_v1.mp4'],check=True); print('done')

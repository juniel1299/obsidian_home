from pathlib import Path
import subprocess,json,imageio_ffmpeg
p=Path(__file__).resolve().parent;f=imageio_ffmpeg.get_ffmpeg_exe()
shots=[('scene_0',1,10),('scene_1a',15,6),('scene_1b',27,8),('scene_2',51,6),('scene_3',69,35)]
for name,start,duration in shots:
 if (p/(name+'.mp4')).exists():continue
 vf='[0:v]fps=30,crop=1600:620:0:150,split=2[b][m];[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=18,scale=1080:1920,eq=brightness=-0.13:saturation=0.6[bg];[m]scale=1080:418,eq=gamma=1.04:saturation=0.9[main];[bg][main]overlay=0:475,setsar=1,format=yuv420p[out]'
 subprocess.run([f,'-y','-v','error','-ss',str(start),'-i',str(p/'engraved_trailer.mp4'),'-filter_complex_threads','2','-filter_complex',vf,'-map','[out]','-an','-t',str(duration),'-c:v','libx264','-preset','fast','-crf','17','-threads','4',str(p/(name+'.mp4'))],check=True)
(p/'concat.txt').write_text(''.join(f"file '{p/(name+'.mp4')}'\n" for name,_,_ in shots))
q=p/'sources.json';x=json.loads(q.read_text());x['segments']=[(s,d) for _,s,d in shots];q.write_text(json.dumps(x,ensure_ascii=False,indent=2))

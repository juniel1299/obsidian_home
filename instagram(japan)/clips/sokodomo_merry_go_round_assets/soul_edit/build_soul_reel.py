from pathlib import Path
import subprocess,json,imageio_ffmpeg
p=Path(__file__).resolve().parent;a=p.parent;f=imageio_ffmpeg.get_ffmpeg_exe()
shots=[('trailer',24,11,22),('living',0,23,110),('living',88,30,110),('purpose',18,5,110)]
for i,(source,start,duration,y) in enumerate(shots):
 if i<2 and (p/f'scene_{i}.mp4').exists():continue
 vf=f'[0:v]fps=30,crop=1440:760:240:{y},split=2[b][m];[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=18,scale=1080:1920,eq=brightness=-0.15:saturation=0.65[bg];[m]scale=1080:570,eq=gamma=1.07:saturation=0.94[main];[bg][main]overlay=0:450,setsar=1,format=yuv420p[out]'
 subprocess.run([f,'-y','-v','error','-ss',str(start),'-i',str(p/(source+'.mp4')),'-filter_complex_threads','2','-filter_complex',vf,'-map','[out]','-an','-t',str(duration),'-c:v','libx264','-preset','fast','-crf','17','-threads','4',str(p/f'scene_{i}.mp4')],check=True);print('Scene ready',i,flush=True)
(p/'concat.txt').write_text(''.join(f"file '{p/f'scene_{i}.mp4'}'\n" for i in range(len(shots))))
subprocess.run([f,'-y','-v','error','-f','concat','-safe','0','-i',str(p/'concat.txt'),'-i',str(a/'audio.m4a'),'-vf',f'ass={a}/layout_with_lyrics.ass:fontsdir=/System/Library/Fonts,format=yuv420p','-map','0:v','-map','1:a','-t','69','-r','30','-c:v','libx264','-preset','fast','-crf','17','-threads','4','-c:a','aac','-b:a','256k','-movflags','+faststart',str(a.parent/'SOKODOMO_Merry_Go_Round_reel_KO_JA_Soul.mp4')],check=True)
caption=(a.parent/'SOKODOMO_Merry_Go_Round_caption.txt').read_text().replace('『ハウルの動く城』','『ソウルフル・ワールド』')
(a.parent/'SOKODOMO_Merry_Go_Round_caption_Soul.txt').write_text(caption)
(p/'sources.json').write_text(json.dumps({'film':'Soul (2020)','visual_sources':{'trailer':'https://www.youtube.com/watch?v=xOsLIiBStEs','living':'https://www.youtube.com/watch?v=5i_DKxZu0aI'},'segments':shots,'audio_source':'https://www.youtube.com/watch?v=ZcGB8Yc_SlE','audio_range':'02:03–03:12','speed':1,'output':'1080x1920, 30fps, 69 seconds','lyrics':'Existing user supplied Korean and Japanese translation preserved'},ensure_ascii=False,indent=2))
print('DONE',flush=True)

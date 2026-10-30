from pathlib import Path
import subprocess,json,imageio_ffmpeg
p=Path(__file__).resolve().parent;root=p.parent;f=imageio_ffmpeg.get_ffmpeg_exe()
s=(root/'reel_assets/layout.ass').read_text().split('[Events]')[0]+'[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'
s+='Dialogue: 0,0:00:00.00,0:01:09.00,Header,,0,0,0,,{\\pos(540,245)}韓国人おすすめの一曲\n'
s+='Dialogue: 0,0:00:00.00,0:01:09.00,Title,,0,0,0,,{\\pos(540,1610)\\fs44}ソコドモ - メリーゴーランド\n'
(p/'layout.ass').write_text(s)
shots=[(3,18),(27,8),(48,15),(73,14),(105,14)]
for i,(start,dur) in enumerate(shots):
 vf='[0:v]fps=30,split=2[b][m];[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=18,scale=1080:1920,eq=brightness=-0.14:saturation=0.65[bg];[m]scale=1080:608,eq=saturation=0.97[main];[bg][main]overlay=0:450,setsar=1,format=yuv420p[out]'
 subprocess.run([f,'-y','-v','error','-ss',str(start),'-i',str(p/'howl_trailer.mp4'),'-filter_complex_threads','2','-filter_complex',vf,'-map','[out]','-an','-t',str(dur),'-c:v','libx264','-preset','fast','-crf','17','-threads','4',str(p/f'scene_{i}.mp4')],check=True);print('Scene ready',i,flush=True)
(p/'concat.txt').write_text(''.join(f"file '{p/f'scene_{i}.mp4'}'\n" for i in range(len(shots))))
(p/'sources.json').write_text(json.dumps({'audio':'https://www.youtube.com/watch?v=ZcGB8Yc_SlE','audio_range':'02:03–03:12','visual':'https://www.youtube.com/watch?v=ARCQf2CEr8k','film':"Howl’s Moving Castle",'segments':shots,'speed':1,'output':'1080x1920, 30fps, 69 seconds','caption_reference':'https://music.bugs.co.kr/track/32381760'},ensure_ascii=False,indent=2))
print('SCENES DONE',flush=True)

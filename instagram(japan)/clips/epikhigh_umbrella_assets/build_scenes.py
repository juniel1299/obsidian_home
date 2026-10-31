from pathlib import Path
import subprocess,json,imageio_ffmpeg
p=Path(__file__).resolve().parent;f=imageio_ffmpeg.get_ffmpeg_exe()
s=Path('clips/reel_assets/layout.ass').read_text().split('[Events]')[0]+'[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'
s+='Dialogue: 0,0:00:00.00,0:00:37.00,Header,,0,0,0,,{\\pos(540,245)}韓国人おすすめの一曲\n'
s+='Dialogue: 0,0:00:00.00,0:00:37.00,Title,,0,0,0,,{\\pos(540,1610)\\fs42}エピックハイ - 傘\n'
s+='Dialogue: 0,0:00:00.00,0:00:37.00,Title,,0,0,0,,{\\pos(540,1680)\\fs30}Feat. ユンナ\n'
s+='Dialogue: 0,0:00:00.00,0:00:37.00,Title,,0,0,0,,{\\pos(540,1800)\\fs21}Coffee Run • (CC) Blender Foundation | studio.blender.org\n'
(p/'layout.ass').write_text(s)
shots=[(17,14),(60,15),(149,8)]
for i,(start,duration) in enumerate(shots):
 vf='[0:v]fps=30,split=2[b][m];[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=18,scale=1080:1920,eq=brightness=-0.18:saturation=0.6[bg];[m]scale=1080:452,eq=saturation=0.85[main];[bg][main]overlay=0:475,setsar=1,format=yuv420p[out]'
 subprocess.run([f,'-y','-v','error','-ss',str(start),'-i',str(p/'coffee_run.mp4'),'-filter_complex_threads','2','-filter_complex',vf,'-map','[out]','-an','-t',str(duration),'-c:v','libx264','-preset','fast','-crf','17','-threads','4',str(p/f'scene_{i}.mp4')],check=True);print('Scene ready',i,flush=True)
(p/'concat.txt').write_text(''.join(f"file '{p/f'scene_{i}.mp4'}'\n" for i in range(len(shots))))
(p/'sources_and_license.json').write_text(json.dumps({'audio':'https://www.youtube.com/watch?v=Qr13kGXORrk','audio_range':'03:47–04:24','visual':'https://www.youtube.com/watch?v=PVGeM40dABA','film':'Coffee Run (2020)','project':'https://studio.blender.org/projects/coffee-run/','license_page':'https://studio.blender.org/projects/coffee-run/pages/licensing/','license':'CC BY 4.0','license_url':'https://creativecommons.org/licenses/by/4.0/','attribution':'(CC) Blender Foundation | studio.blender.org','changes':'Excerpts, vertical layout, subtitles, original audio replaced','segments':shots,'speed':1,'output':'1080x1920, 30fps, 37 seconds'},ensure_ascii=False,indent=2))
print('SCENES DONE',flush=True)

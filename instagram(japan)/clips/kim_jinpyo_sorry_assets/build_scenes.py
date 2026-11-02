from pathlib import Path
import subprocess,json,imageio_ffmpeg
p=Path(__file__).resolve().parent;f=imageio_ffmpeg.get_ffmpeg_exe()
s=Path('clips/reel_assets/layout.ass').read_text().split('[Events]')[0]+'[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'
s+='Dialogue: 0,0:00:00.00,0:01:00.00,Header,,0,0,0,,{\\pos(540,245)}韓国人おすすめの一曲\n'
s+='Dialogue: 0,0:00:00.00,0:01:00.00,Title,,0,0,0,,{\\pos(540,1610)\\fs40}キム・ジンピョ - 謝ってばかりでごめん\n'
s+='Dialogue: 0,0:00:00.00,0:01:00.00,Title,,0,0,0,,{\\pos(540,1680)\\fs30}Feat. G.NA\n'
(p/'layout.ass').write_text(s)
shots=[(0,10),(12,8),(31,10),(61,8),(79,14),(101,10)]
for i,(start,duration) in enumerate(shots):
 vf='[0:v]fps=30,crop=1600:650:0:110,split=2[b][m];[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=18,scale=1080:1920,eq=brightness=-0.12:saturation=0.65[bg];[m]scale=1080:438,eq=gamma=1.1:saturation=0.92[main];[bg][main]overlay=0:475,setsar=1,format=yuv420p[out]'
 subprocess.run([f,'-y','-v','error','-ss',str(start),'-i',str(p/'us_and_them_trailer.mp4'),'-filter_complex_threads','2','-filter_complex',vf,'-map','[out]','-an','-t',str(duration),'-c:v','libx264','-preset','fast','-crf','17','-threads','4',str(p/f'scene_{i}.mp4')],check=True);print('Scene ready',i,flush=True)
(p/'concat.txt').write_text(''.join(f"file '{p/f'scene_{i}.mp4'}'\n" for i in range(len(shots))))
(p/'sources.json').write_text(json.dumps({'audio':'https://www.youtube.com/watch?v=HLLSAB4Z00Q','audio_range':'01:51–02:51','visual':'https://www.youtube.com/watch?v=-xSs_xsf5sI','film':'Us and Them (2018)','segments':shots,'speed':1,'output':'1080x1920, 30fps, 60 seconds','caption_reference':'https://www.genie.co.kr/detail/albumInfo?axnm=80299530'},ensure_ascii=False,indent=2))
print('SCENES DONE',flush=True)

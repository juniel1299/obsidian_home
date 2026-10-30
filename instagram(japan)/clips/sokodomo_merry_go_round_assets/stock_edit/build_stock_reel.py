from pathlib import Path
import subprocess,json,imageio_ffmpeg,shutil
p=Path(__file__).resolve().parent;a=p.parent;old=a.parent/'nmixx_blue_valentine_assets/stock_edit';f=imageio_ffmpeg.get_ffmpeg_exe()
for name in ['rain_window.mp4','neon_street.mp4','text_shade.png']:
 if not (p/name).exists():shutil.copy2(old/name,p/name)
shots=[('traffic',14),('rain_window',10),('neon_street',12),('train_interior',18),('sunset_train',15)]
for i,(name,duration) in enumerate(shots):
 vf='fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,eq=brightness=-0.025:saturation=0.9,format=yuv420p'
 subprocess.run([f,'-y','-v','error','-i',str(p/(name+'.mp4')),'-vf',vf,'-an','-t',str(duration),'-c:v','libx264','-preset','fast','-crf','17','-threads','4',str(p/f'scene_{i}.mp4')],check=True);print('Scene ready',i,flush=True)
(p/'concat.txt').write_text(''.join(f"file '{p/f'scene_{i}.mp4'}'\n" for i in range(len(shots))))
vf=f'[0:v][2:v]overlay=0:0,ass={a}/layout_with_lyrics.ass:fontsdir=/System/Library/Fonts,format=yuv420p[out]'
subprocess.run([f,'-y','-v','error','-f','concat','-safe','0','-i',str(p/'concat.txt'),'-i',str(a/'audio.m4a'),'-loop','1','-i',str(p/'text_shade.png'),'-filter_complex_threads','2','-filter_complex',vf,'-map','[out]','-map','1:a','-t','69','-r','30','-c:v','libx264','-preset','fast','-crf','17','-threads','4','-c:a','aac','-b:a','256k','-movflags','+faststart',str(a.parent/'SOKODOMO_Merry_Go_Round_reel_KO_JA_stock.mp4')],check=True)
sources=[{'file':'traffic.mp4','creator':'Evgenij Mikhailov','page':'https://www.pexels.com/video/vibrant-night-urban-cityscape-with-traffic-36443796/','download':'https://videos.pexels.com/video-files/36443796/15453650_2160_3840_60fps.mp4'},{'file':'train_interior.mp4','creator':'Gaurav Budhiraja','page':'https://www.pexels.com/video/serene-empty-train-carriage-at-sunset-34799570/','download':'https://videos.pexels.com/video-files/34799570/14754187_1440_2560_30fps.mp4'},{'file':'sunset_train.mp4','creator':'Jerry Gen','page':'https://www.pexels.com/video/urban-train-passing-through-city-at-sunset-33912036/','download':'https://videos.pexels.com/video-files/33912036/14391493_3840_2160_30fps.mp4'}]
previous=json.loads((old/'sources_and_license.json').read_text());sources += [s for s in previous['sources'] if s['file'] in ['rain_window.mp4','neon_street.mp4']]
meta={'checked':'2026-10-31','license':'Pexels License','license_url':'https://www.pexels.com/license/','commercial_use_reference':'https://help.pexels.com/hc/en-us/articles/360042295214-Can-I-use-the-photos-and-videos-for-a-commercial-project','sources':sources,'timeline':shots,'speed':1,'audio_source':'https://www.youtube.com/watch?v=ZcGB8Yc_SlE','audio_range':'02:03–03:12','output':'1080x1920, 30fps, 69 seconds'}
(p/'sources_and_license.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
(a.parent/'SOKODOMO_Merry_Go_Round_stock_sources.txt').write_text('영상 출처 및 라이선스\n확인일: 2026-10-31\nPexels License\nhttps://www.pexels.com/license/\n상업적 사용 안내: '+meta['commercial_use_reference']+'\n\n'+'\n\n'.join(s['creator']+'\n'+s['page'] for s in sources)+'\n\n음원 권리는 별도이며, 배경 영상 교체가 음원 차단 해제를 보장하지는 않습니다.\n')
caption=(a.parent/'SOKODOMO_Merry_Go_Round_caption.txt').read_text().replace('🎬 映像：『ハウルの動く城』','🎬 映像：Pexelsのストック映像を使用')
(a.parent/'SOKODOMO_Merry_Go_Round_caption_stock.txt').write_text(caption)
print('DONE',flush=True)

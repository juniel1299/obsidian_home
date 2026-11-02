from pathlib import Path
import subprocess,imageio_ffmpeg
p=Path(__file__).resolve().parent;f=imageio_ffmpeg.get_ffmpeg_exe()
for duration,suffix,audio in [(60,'','audio.m4a'),(62,'_ending','audio_extended.m4a')]:
 if suffix:
  vf='[0:v]fps=30,crop=1600:650:0:110,split=2[b][m];[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=18,scale=1080:1920,eq=brightness=-0.12:saturation=0.65[bg];[m]scale=1080:438,eq=gamma=1.1:saturation=0.92[main];[bg][main]overlay=0:475,setsar=1,format=yuv420p[out]'
  subprocess.run([f,'-y','-v','error','-i',str(p/'us_and_them_trailer.mp4'),'-filter_complex_threads','2','-filter_complex',vf,'-map','[out]','-an','-t','12','-c:v','libx264','-preset','fast','-crf','17','-threads','4',str(p/'scene_0_ending.mp4')],check=True)
  (p/'concat_ending.txt').write_text(f"file '{p/'scene_0_ending.mp4'}'\n"+''.join(f"file '{p/f'scene_{i}.mp4'}'\n" for i in range(1,6)))
 ass=p/f'layout_with_lyrics{suffix}.ass'
 subprocess.run([f,'-y','-v','error','-f','concat','-safe','0','-i',str(p/f'concat{suffix}.txt'),'-i',str(p/audio),'-vf',f'ass={ass}:fontsdir=/System/Library/Fonts,format=yuv420p','-map','0:v','-map','1:a','-t',str(duration),'-r','30','-c:v','libx264','-preset','fast','-crf','17','-threads','4','-c:a','aac','-b:a','256k','-movflags','+faststart',str(p.parent/f'KIM_JIN_PYO_Sorry_reel_KO_JA{suffix}.mp4')],check=True)
 print('DONE',duration,flush=True)

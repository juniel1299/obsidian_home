from pathlib import Path
import subprocess,imageio_ffmpeg
p=Path(__file__).resolve().parent;f=imageio_ffmpeg.get_ffmpeg_exe()
subprocess.run([f,'-y','-v','error','-f','concat','-safe','0','-i',str(p/'concat.txt'),'-i',str(p/'audio.m4a'),'-vf',f'ass={p}/layout_with_lyrics.ass:fontsdir=/System/Library/Fonts,format=yuv420p','-map','0:v','-map','1:a','-t','65','-r','30','-c:v','libx264','-preset','fast','-crf','17','-threads','4','-c:a','aac','-b:a','256k','-movflags','+faststart',str(p.parent/'KWILL_Please_Dont_reel_KO_JA.mp4')],check=True)
print('DONE',flush=True)

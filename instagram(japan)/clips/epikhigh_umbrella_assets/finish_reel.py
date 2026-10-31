from pathlib import Path
import subprocess,imageio_ffmpeg
p=Path(__file__).resolve().parent;f=imageio_ffmpeg.get_ffmpeg_exe()
ass=p/('layout_with_lyrics.ass' if (p/'layout_with_lyrics.ass').exists() else 'layout.ass');out=p.parent/('EPIK_HIGH_Umbrella_reel_KO_JA.mp4' if ass.name=='layout_with_lyrics.ass' else 'EPIK_HIGH_Umbrella_reel.mp4')
subprocess.run([f,'-y','-v','error','-f','concat','-safe','0','-i',str(p/'concat.txt'),'-i',str(p/'audio.m4a'),'-vf',f'ass={ass}:fontsdir=/System/Library/Fonts,format=yuv420p','-map','0:v','-map','1:a','-t','37','-r','30','-c:v','libx264','-preset','fast','-crf','17','-threads','4','-c:a','aac','-b:a','256k','-movflags','+faststart',str(out)],check=True);print('DONE',str(out),flush=True)

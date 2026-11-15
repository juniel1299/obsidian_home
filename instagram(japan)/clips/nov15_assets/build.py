from pathlib import Path
import subprocess
import imageio_ffmpeg

p = Path(__file__).resolve().parent
ff = imageio_ffmpeg.get_ffmpeg_exe()
shots = [(28,25),(9.7,12.3),(22.8,0.9),(58.5,3.4),(62.5,4.5),(69.5,13),(1,6.9),(53.5,3)]
for i,(start,duration) in enumerate(shots):
    output = p / f'shot{i}.mp4'
    vf = ('[0:v]fps=30,crop=iw:ih*0.80:0:ih*0.08,split[b][m];'
          '[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,'
          'gblur=sigma=18,scale=1080:1920,eq=brightness=-0.16:saturation=0.65[bg];'
          '[m]scale=1080:-2[main];[bg][main]overlay=0:490,setsar=1,format=yuv420p[out]')
    subprocess.run([ff,'-y','-v','error','-ss',str(start),'-i',str(p/'film.mp4'),
                    '-filter_complex_threads','2','-filter_complex',vf,'-map','[out]',
                    '-t',str(duration),'-an','-c:v','libx264','-preset','veryfast',
                    '-threads','4','-crf','16',str(output)],check=True)
(p/'concat.txt').write_text(''.join(f"file 'shot{i}.mp4'\n" for i in range(len(shots))))

from pathlib import Path
from PIL import ImageFont
import subprocess,json,imageio_ffmpeg
p=Path(__file__).resolve().parent;f=imageio_ffmpeg.get_ffmpeg_exe()
cues=[(0,7.8,'오 사랑한 사람이여','ああ、愛した人よ'),(8.6,13.8,'더 이상 못 보아도','もう会えなくても'),(14.3,19.88,'사실 그대 있음으로','あなたがいてくれたから'),(19.88,25.6,'힘겨운 날들을 견뎌 왔음에','つらい日々を耐えてこられたことに'),(25.6,29.5,'감사하오','感謝しています'),(30.78,36.38,'좋은 사람 만나오','どうか素敵な人に出会ってください'),(36.38,44.1,'사는 동안 날 잊고 사시오','これからは私を忘れて生きてください'),(44.56,50.68,'진정 행복하길 바라겠소','心から幸せを願っています'),(50.68,58,'이 맘만 가져가오','この想いだけ、受け取ってください')]
def ts(t):
 c=round(t*100);return f'{c//360000}:{c//6000%60:02}:{c//100%60:02}.{c%100:02}'
def st(t):
 m=round(t*1000);return f'{m//3600000:02}:{m//60000%60:02}:{m//1000%60:02},{m%1000:03}'
s=Path('clips/reel_assets/layout.ass').read_text().split('[Events]')[0]+'[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'
s+='Dialogue: 0,0:00:00.00,0:00:58.00,Header,,0,0,0,,{\\pos(540,245)}韓国人おすすめの一曲\n'
s+='Dialogue: 0,0:00:00.00,0:00:58.00,Title,,0,0,0,,{\\pos(540,1610)\\fs44}キム・グァンジン - 手紙\n'
for a,b,k,j in cues:
 for style,text,y,font,size in [('KO',k,1385,'/System/Library/Fonts/AppleSDGothicNeo.ttc',48),('JA',j,1455,'/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc',44)]:
  ft=ImageFont.truetype(font,size);sz=min(size,int(size*900/max(1,ft.getlength(text))))
  s+=f'Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{{\\pos(540,{y})\\fs{sz}}}{text}\n'
(p/'layout_with_lyrics.ass').write_text(s);(p/'lyrics.json').write_text(json.dumps(cues,ensure_ascii=False,indent=2))
(p.parent/'KIM_KWANG_JIN_Letter_KO_JA.srt').write_text('\n\n'.join(f'{i}\n{st(a)} --> {st(b)}\n{k}\n{j}' for i,(a,b,k,j) in enumerate(cues,1))+'\n')
shots=[(3,9),(19,35),(68,14)]
for i,(start,duration) in enumerate(shots):
 vf='[0:v]fps=30,crop=1600:650:160:145,split=2[b][m];[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=18,scale=1080:1920,eq=brightness=-0.14:saturation=0.6[bg];[m]scale=1080:438,eq=saturation=0.88[main];[bg][main]overlay=0:475,setsar=1,format=yuv420p[out]'
 subprocess.run([f,'-y','-v','error','-ss',str(start),'-i',str(p/'love_letter_trailer.mp4'),'-filter_complex_threads','2','-filter_complex',vf,'-map','[out]','-an','-t',str(duration),'-c:v','libx264','-preset','fast','-crf','17','-threads','4',str(p/f'scene_{i}.mp4')],check=True);print('Scene ready',i,flush=True)
(p/'concat.txt').write_text(''.join(f"file '{p/f'scene_{i}.mp4'}'\n" for i in range(len(shots))))
subprocess.run([f,'-y','-v','error','-f','concat','-safe','0','-i',str(p/'concat.txt'),'-i',str(p/'audio.m4a'),'-vf',f'ass={p}/layout_with_lyrics.ass:fontsdir=/System/Library/Fonts,format=yuv420p','-map','0:v','-map','1:a','-t','58','-r','30','-c:v','libx264','-preset','fast','-crf','17','-threads','4','-c:a','aac','-b:a','256k','-movflags','+faststart',str(p.parent/'KIM_KWANG_JIN_Letter_reel_KO_JA.mp4')],check=True)
(p/'sources.json').write_text(json.dumps({'audio':'https://www.youtube.com/watch?v=ts6a_GAoghA','audio_range':'03:20–04:18','visual':'https://www.youtube.com/watch?v=tvneMVSrvbU','film':'Love Letter (1995), restoration trailer','segments':shots,'speed':1,'lyrics':'User supplied Korean with Japanese translation','output':'1080x1920, 30fps, 58 seconds','song_credit_reference':'https://music.bugs.co.kr/track/6458340'},ensure_ascii=False,indent=2))
caption='''まだ好きなのに、引き止める言葉ではなく、相手の幸せを願う言葉を選ぶ。\n\nキム・グァンジンの「편지（手紙）」は、別れを受け入れようとする人の想いを、静かに綴った一曲。作曲はキム・グァンジン、作詞はホ・スンギョンです。\n\n一緒に過ごした時間への感謝も、もう会えない寂しさも、心の中には残っている。\nそれでも、これからの人生が幸せであるようにと願う。\n\n淡々とした歌声だからこそ、言葉の一つひとつが深く響きます。\n大切だった人を思い出す夜に、ゆっくり聴いてほしい曲です。\n\n🎧 キム・グァンジン - 편지（手紙）\n🎬 映像：『Love Letter』（1995）\n\n#キムグァンジン #김광진 #편지 #手紙 #韓国音楽 #韓国バラード #韓国人おすすめの一曲 #失恋ソング\n'''
(p.parent/'KIM_KWANG_JIN_Letter_caption.txt').write_text(caption)
print('DONE',flush=True)

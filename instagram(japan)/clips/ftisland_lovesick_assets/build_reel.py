from pathlib import Path
from PIL import ImageFont
import subprocess,json,imageio_ffmpeg
p=Path(__file__).resolve().parent;f=imageio_ffmpeg.get_ffmpeg_exe()
cues=[(0,3.02,'그 사람 꼭 올거라고','あの人はきっと戻ってくると'),(3.02,7.7,'내 가슴에 해로운 거짓말을 하고','自分の心を傷つける嘘をついて'),(8.62,12.12,'꼭 올거라는 말은 안했지만','必ず戻るとは言われなかったけれど'),(12.12,15.7,'기다릴 수 밖에 없는 사람','それでも待つしかない人'),(16.06,19.4,'너무나 많이 사랑한 죄','愛しすぎたという罪'),(19.58,24,'널 너무나 많이 사랑한 죄','君をあまりにも愛しすぎた罪'),(24.62,28.72,'난 너로인해 그 죄로인해','僕は君のせいで、その罪のせいで'),(28.72,31.6,'기다림을 앓고 있다고','待ち続ける苦しみに病んでいる'),(32.26,35.5,'내가 더 많이 사랑한 죄','僕のほうがもっと愛した罪'),(35.76,39.8,'널 너무나 많이 그리워한 죄','君をあまりにも恋しく想った罪'),(40.76,44.92,'난 너로인해 그 죄로인해','僕は君のせいで、その罪のせいで'),(44.92,48,'눈물로 앓고 있다고','涙に暮れながら苦しんでいる'),(48.3,51.7,'헤어짐 늘 빠른 사랑','別れはいつも早く訪れる恋'),(52,56,'잊혀짐은 늘 더딘 사랑','忘れるにはいつも時間がかかる恋'),(56.58,60.1,'늘 나에게만 늘 모진 사랑','いつも僕にだけ残酷な恋'),(60.1,64,'나 혼자 앓고 있었다고','僕ひとりで苦しんでいたんだ')]
def ts(t):
 c=round(t*100);return f'{c//360000}:{c//6000%60:02}:{c//100%60:02}.{c%100:02}'
def st(t):
 m=round(t*1000);return f'{m//3600000:02}:{m//60000%60:02}:{m//1000%60:02},{m%1000:03}'
s=Path('clips/reel_assets/layout.ass').read_text().split('[Events]')[0]+'[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'
s+='Dialogue: 0,0:00:00.00,0:01:06.00,Header,,0,0,0,,{\\pos(540,245)}韓国人おすすめの一曲\n'
s+='Dialogue: 0,0:00:00.00,0:01:06.00,Title,,0,0,0,,{\\pos(540,1610)\\fs44}FTISLAND - 恋煩い（Love Sick）\n'
for a,b,k,j in cues:
 for style,text,y,font,size in [('KO',k,1385,'/System/Library/Fonts/AppleSDGothicNeo.ttc',48),('JA',j,1455,'/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc',44)]:
  ft=ImageFont.truetype(font,size);sz=min(size,int(size*900/max(1,ft.getlength(text))))
  s+=f'Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{{\\pos(540,{y})\\fs{sz}}}{text}\n'
(p/'layout_with_lyrics.ass').write_text(s);(p/'lyrics.json').write_text(json.dumps(cues,ensure_ascii=False,indent=2))
(p.parent/'FTISLAND_Love_Sick_KO_JA.srt').write_text('\n\n'.join(f'{i}\n{st(a)} --> {st(b)}\n{k}\n{j}' for i,(a,b,k,j) in enumerate(cues,1))+'\n')
shots=[('even_if_love_disappears_teaser',3,35),('even_if_love_disappears',36,4),('even_if_love_disappears',0,14),('even_if_love_disappears',69,6),('even_if_love_disappears',53,5),('even_if_love_disappears',80,2)]
for i,(source,start,duration) in enumerate(shots):
 vf='[0:v]fps=30,crop=1600:600:160:150,split=2[b][m];[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=18,scale=1080:1920,eq=brightness=-0.14:saturation=0.65[bg];[m]scale=1080:405,eq=saturation=0.94[main];[bg][main]overlay=0:475,setsar=1,format=yuv420p[out]'
 subprocess.run([f,'-y','-v','error','-ss',str(start),'-i',str(p/(source+'.mp4')),'-filter_complex_threads','2','-filter_complex',vf,'-map','[out]','-an','-t',str(duration),'-c:v','libx264','-preset','fast','-crf','17','-threads','4',str(p/f'scene_{i}.mp4')],check=True);print('Scene ready',i,flush=True)
(p/'concat.txt').write_text(''.join(f"file '{p/f'scene_{i}.mp4'}'\n" for i in range(len(shots))))
subprocess.run([f,'-y','-v','error','-f','concat','-safe','0','-i',str(p/'concat.txt'),'-i',str(p/'audio.m4a'),'-vf',f'ass={p}/layout_with_lyrics.ass:fontsdir=/System/Library/Fonts,format=yuv420p','-map','0:v','-map','1:a','-t','66','-r','30','-c:v','libx264','-preset','fast','-crf','17','-threads','4','-c:a','aac','-b:a','256k','-movflags','+faststart',str(p.parent/'FTISLAND_Love_Sick_reel_KO_JA.mp4')],check=True)
(p/'sources.json').write_text(json.dumps({'audio':'https://www.youtube.com/watch?v=Y_nfGFZonpE','audio_range':'01:40–02:46','visual':'https://www.youtube.com/watch?v=JA2iC3kHgEM','film':'Even If This Love Disappears from the World Tonight (2022)','segments':shots,'speed':1,'lyrics':'User supplied Korean with Japanese translation','output':'1080x1920, 30fps, 66 seconds','caption_reference':'https://music.bugs.co.kr/album/8027281'},ensure_ascii=False,indent=2))
caption='''待つのが苦しいと分かっていても、まだ帰ってくる気がしてしまう。\n\nFTISLANDの「사랑앓이（Love Sick）」は、2007年のデビューアルバム『Cheerful Sensibility』のタイトル曲。日本語にすると「恋煩い」という意味です。\n\n愛しすぎたことも、忘れられないことも、自分の罪のように感じてしまう。そんな行き場のない気持ちを、力強いバンドサウンドと絞り出すような歌声がまっすぐ届けてくれます。\n\n別れは一瞬でも、忘れるまでには長い時間がかかる。\nひとりで抱えてきた恋の痛みに、そっと重なる一曲です。\n\n🎧 FTISLAND - 사랑앓이（Love Sick／恋煩い）\n🎬 映像：『今夜、世界からこの恋が消えても』（2022）\n\n#FTISLAND #エフティーアイランド #FT아일랜드 #사랑앓이 #LoveSick #恋煩い #韓国音楽 #韓国人おすすめの一曲 #失恋ソング\n'''
(p.parent/'FTISLAND_Love_Sick_caption.txt').write_text(caption)
print('DONE',flush=True)

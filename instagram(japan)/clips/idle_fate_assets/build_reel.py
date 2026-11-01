from pathlib import Path
from PIL import ImageFont
import subprocess,json,imageio_ffmpeg
p=Path(__file__).resolve().parent;f=imageio_ffmpeg.get_ffmpeg_exe()
cues=[(0,4.68,'오늘도 아침엔 입에 빵을 물고','今日も朝はパンをくわえて'),(4.68,7.6,'똑같이 하루를 시작하고','いつも通りに一日を始める'),(7.6,12.66,'온종일 한 손엔 아이스 아메리카노','一日中、片手にはアイスアメリカーノ'),(12.66,16.6,'피곤해 죽겠네','もう疲れてたまらない'),(17,21.42,'지하철 속 이 장면 어제 꿈에서 봤나','地下鉄のこの光景、昨日夢で見たっけ'),(21.42,25,'아참 매일이지 지나치고','あ、毎日だったね、とやり過ごす'),(25.9,30.48,'바쁜 이 삶에 그냥 흔한 날에','忙しい毎日の、何でもない日に'),(30.48,32.9,'그 애를 보고 말야','あの人を見かけたんだ'),(32.9,37.78,'평온했던 하늘이 무너지고','穏やかだった空が崩れ落ちて'),(37.78,42.28,'어둡던 눈앞이 붉어지며','暗かった目の前が赤く染まる'),(42.28,46.28,'뭔가 잊고 온 게 있는 것 같아','何かを忘れてきたような気がする'),(46.28,50.48,'괜히 이상하게 막 울 것만 같고','なぜか変に、泣き出しそうになって'),(50.48,54.76,'그냥 지나치는 게 나을 것 같아','そのまま通り過ぎたほうがよさそう'),(54.76,60,'나는 생각은 딱 질색이니까','だって考えるのは大嫌いだから')]
def ts(t):
 c=round(t*100);return f'{c//360000}:{c//6000%60:02}:{c//100%60:02}.{c%100:02}'
def st(t):
 m=round(t*1000);return f'{m//3600000:02}:{m//60000%60:02}:{m//1000%60:02},{m%1000:03}'
s=Path('clips/reel_assets/layout.ass').read_text().split('[Events]')[0]+'[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'
s+='Dialogue: 0,0:00:00.00,0:01:00.00,Header,,0,0,0,,{\\pos(540,245)}韓国人おすすめの一曲\n'
s+='Dialogue: 0,0:00:00.00,0:01:00.00,Title,,0,0,0,,{\\pos(540,1610)\\fs40}i-dle - 傷つくのは嫌いだから（Fate）\n'
for a,b,k,j in cues:
 for style,text,y,font,size in [('KO',k,1385,'/System/Library/Fonts/AppleSDGothicNeo.ttc',48),('JA',j,1455,'/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc',44)]:
  ft=ImageFont.truetype(font,size);sz=min(size,int(size*900/max(1,ft.getlength(text))))
  s+=f'Dialogue: 0,{ts(a)},{ts(b)},{style},,0,0,0,,{{\\pos(540,{y})\\fs{sz}}}{text}\n'
(p/'layout_with_lyrics.ass').write_text(s);(p/'lyrics.json').write_text(json.dumps(cues,ensure_ascii=False,indent=2))
(p.parent/'IDLE_Fate_KO_JA.srt').write_text('\n\n'.join(f'{i}\n{st(a)} --> {st(b)}\n{k}\n{j}' for i,(a,b,k,j) in enumerate(cues,1))+'\n')
shots=[('your_name_jp',10,6),('your_name_trailer',16,11),('your_name_trailer',10,4),('your_name_trailer',27,31),('your_name_trailer',66,4),('your_name_trailer',75,4)]
for i,(source,start,duration) in enumerate(shots):
 vf='[0:v]fps=30,crop=1920:840:0:0,split=2[b][m];[b]scale=270:480:force_original_aspect_ratio=increase,crop=270:480,gblur=sigma=18,scale=1080:1920,eq=brightness=-0.15:saturation=0.65[bg];[m]scale=1080:472,eq=saturation=0.97[main];[bg][main]overlay=0:475,setsar=1,format=yuv420p[out]'
 subprocess.run([f,'-y','-v','error','-ss',str(start),'-i',str(p/(source+'.mp4')),'-filter_complex_threads','2','-filter_complex',vf,'-map','[out]','-an','-t',str(duration),'-c:v','libx264','-preset','fast','-crf','17','-threads','4',str(p/f'scene_{i}.mp4')],check=True);print('Scene ready',i,flush=True)
(p/'concat.txt').write_text(''.join(f"file '{p/f'scene_{i}.mp4'}'\n" for i in range(len(shots))))
subprocess.run([f,'-y','-v','error','-f','concat','-safe','0','-i',str(p/'concat.txt'),'-i',str(p/'audio.m4a'),'-vf',f'ass={p}/layout_with_lyrics.ass:fontsdir=/System/Library/Fonts,format=yuv420p','-map','0:v','-map','1:a','-t','60','-r','30','-c:v','libx264','-preset','fast','-crf','17','-threads','4','-c:a','aac','-b:a','256k','-movflags','+faststart',str(p.parent/'IDLE_Fate_reel_KO_JA.mp4')],check=True)
(p/'sources.json').write_text(json.dumps({'audio':'https://www.youtube.com/watch?v=kWmcsY7WmpU','audio_range':'00:06–01:06','visual_sources':{'your_name_jp':'https://www.youtube.com/watch?v=3KR8_igDs1Y','your_name_trailer':'https://www.youtube.com/watch?v=RuyHIkXdYf8'},'film':'Your Name. (2016)','segments':shots,'speed':1,'lyrics':'User supplied Korean, Japanese translation','title_reference':'https://wmg.jp/idle/news/90254','output':'1080x1920, 30fps, 60 seconds'},ensure_ascii=False,indent=2))
caption='''何でもない一日だったのに、あの人を見かけた瞬間、世界が変わった。\n\ni-dleの「나는 아픈 건 딱 질색이니까（Fate）」は、アルバム『2』に収録された一曲。軽やかなバンドサウンドに、ふいに訪れる運命のような出会いと、説明できない感情が重なります。\n\nすれ違っただけなのに、なぜか懐かしい。\n初めて会ったはずなのに、泣きたくなる。\n\n明るいメロディの奥にある切なさが、アニメのワンシーンみたいに胸に残る曲です。\n\n🎧 i-dle - 나는 아픈 건 딱 질색이니까（Fate）\n日本語タイトル：傷つくのは嫌いだから\n🎬 映像：『君の名は。』\n\n#idle #アイドゥル #아이들 #Fate #나는아픈건딱질색이니까 #傷つくのは嫌いだから #韓国音楽 #韓国人おすすめの一曲\n'''
(p.parent/'IDLE_Fate_caption.txt').write_text(caption)
print('DONE',flush=True)
